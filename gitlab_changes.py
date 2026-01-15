# gitlab_changes.py
from __future__ import annotations

import os
import re
import sys
import time
import json
import shutil
import subprocess
from pathlib import Path
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Set, Tuple
from urllib.parse import quote

import requests

# Rich UI (required for the "visually appealing" interactive wizard)
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.prompt import Prompt, Confirm
    from rich.progress import (
        Progress,
        SpinnerColumn,
        BarColumn,
        TextColumn,
        TimeElapsedColumn,
        TimeRemainingColumn,
    )
except Exception:
    print("ERROR: This interactive version requires 'rich'. Install with:\n  python -m pip install rich\n")
    raise

console = Console()


@dataclass
class Settings:
    gitlab_base: str
    project: str
    from_ref: str
    to_ref: str
    out_file: str
    unidiff: bool
    straight: bool
    per_page: int
    sleep: float
    run_codex: bool


def project_id_for_api(project: str) -> str:
    # numeric id stays as-is; path must be URL-encoded including slashes
    return project if project.isdigit() else quote(project.strip("/"), safe="")


def api_get_with_retries(
    session: requests.Session,
    url: str,
    params: Optional[dict] = None,
    label: str = "",
    retries: int = 3,
    backoff: float = 2.0,
) -> requests.Response:
    for attempt in range(1, retries + 1):
        r = session.get(url, params=params)
        if r.status_code == 429 and attempt < retries:
            console.log(
                f"[yellow]Rate limited (429)[/]. Sleeping {backoff * attempt:.1f}s then retrying: {label or r.url}"
            )
            time.sleep(backoff * attempt)
            continue
        if not r.ok:
            msg = r.text[:1200]
            raise RuntimeError(f"HTTP {r.status_code} for {r.url}\n{msg}")
        return r
    raise RuntimeError(f"Failed after retries: {url}")


def api_get_json(session: requests.Session, url: str, params: Optional[dict] = None, label: str = "") -> Any:
    return api_get_with_retries(session, url, params=params, label=label).json()


def api_get_all_pages(
    session: requests.Session,
    url: str,
    params: Optional[dict] = None,
    per_page: int = 100,
    label: str = "",
) -> List[Any]:
    """
    Fetch list endpoints with pagination (page/per_page + X-Next-Page).
    """
    items: List[Any] = []
    page = 1
    base_params = dict(params or {})
    base_params["per_page"] = per_page

    while True:
        p = dict(base_params)
        p["page"] = page
        r = api_get_with_retries(session, url, params=p, label=label)
        data = r.json()
        if isinstance(data, list):
            items.extend(data)
        else:
            return items

        next_page = r.headers.get("X-Next-Page", "")
        if not next_page:
            break
        page = int(next_page)

    return items


def md(s: str) -> str:
    return (s or "").replace("\r\n", "\n")


def extract_issue_links_from_text(text: str, project_web_base: str) -> List[str]:
    """
    Best-effort extraction:
    - full issue URLs already in text
    - same-project shorthand: #123 -> project issue URL
    """
    if not text:
        return []

    links: Set[str] = set()

    for m in re.finditer(r"(https?://[^\s\])>]+/-/issues/\d+)", text):
        links.add(m.group(1))

    for m in re.finditer(r"(?<!\w)#(\d+)", text):
        iid = m.group(1)
        links.add(f"{project_web_base}/-/issues/{iid}")

    return sorted(links)


def wizard() -> Tuple[Settings, str]:
    console.print(
        Panel.fit(
            "[bold]GitLab Changes Exporter[/bold]\nInteractive wizard for compare → MRs → commits → diffs",
            border_style="cyan",
        )
    )

    gitlab_base = Prompt.ask("GitLab base URL", default="https://gitlab.com").strip().rstrip("/")
    project = Prompt.ask("Project path or numeric ID (e.g. [dim]group/subgroup/project[/dim])").strip().strip("/")
    from_ref = Prompt.ask("From ref (tag/branch/SHA)", default="v1.37").strip()
    to_ref = Prompt.ask("To ref (tag/branch/SHA)", default="release-1.38").strip()

    unidiff = Confirm.ask("Use unified diff format (unidiff)?", default=True)
    straight = Confirm.ask("Use straight compare (from..to) instead of merge-base (from...to)?", default=False)

    per_page = int(Prompt.ask("per_page for paginated endpoints", default="100"))
    sleep = float(Prompt.ask("Delay between API calls in seconds (helps avoid rate limits)", default="0"))

    # Output default
    safe_from = re.sub(r"[^\w\.-]+", "_", from_ref)
    safe_to = re.sub(r"[^\w\.-]+", "_", to_ref)
    out_default = f"changes_{safe_from}_to_{safe_to}.md"
    out_file = Prompt.ask("Output markdown file", default=out_default).strip()

    # Token: prefer env var if present, otherwise prompt (hidden)
    env_token = os.environ.get("GITLAB_TOKEN", "")
    use_env = False
    if env_token:
        use_env = Confirm.ask("Found GITLAB_TOKEN in environment. Use it?", default=True)

    if use_env:
        token = env_token
    else:
        console.print(
            "\n[dim]Need a token? In GitLab: Avatar → Edit profile → Personal access tokens → create token (copy once).[/dim]\n"
        )
        token = Prompt.ask("GitLab Personal Access Token", password=True)

    run_codex = Confirm.ask(
        "After export, run Codex CLI to generate changelog.csv + tests.csv (optional)?",
        default=False,
    )

    # Show summary table
    t = Table(title="Run configuration", header_style="bold magenta")
    t.add_column("Setting", style="cyan", no_wrap=True)
    t.add_column("Value", style="white")
    t.add_row("GitLab", gitlab_base)
    t.add_row("Project", project)
    t.add_row("From → To", f"{from_ref} → {to_ref}")
    t.add_row("unidiff", str(unidiff))
    t.add_row("straight", str(straight))
    t.add_row("per_page", str(per_page))
    t.add_row("sleep", str(sleep))
    t.add_row("out_file", out_file)
    t.add_row("run_codex", str(run_codex))
    console.print(t)

    if not Confirm.ask("Proceed?", default=True):
        console.print("[yellow]Cancelled.[/yellow]")
        sys.exit(0)

    settings = Settings(
        gitlab_base=gitlab_base,
        project=project,
        from_ref=from_ref,
        to_ref=to_ref,
        out_file=out_file,
        unidiff=unidiff,
        straight=straight,
        per_page=per_page,
        sleep=sleep,
        run_codex=run_codex,
    )
    return settings, token


def _safe_json_loads(text: str) -> Any:
    """
    Codex should write clean JSON when output schema is used, but this makes parsing robust
    if anything else sneaks into the file.
    """
    try:
        return json.loads(text)
    except Exception:
        start = text.find("{")
        end = text.rfind("}")
        if start != -1 and end != -1 and end > start:
            return json.loads(text[start : end + 1])
        raise


def run_codex_csv_generation(changes_md_path: str, from_ref: str, to_ref: str) -> None:
    """
    Runs: codex exec (non-interactive) with an output schema.
    Writes: changelog.csv and tests.csv next to the changes markdown file.
    """
    if not shutil.which("codex"):
        console.print(
            "[yellow]Codex CLI not found on PATH.[/yellow]\n"
            "Install: npm i -g @openai/codex\n"
            "Then run: codex (to sign in)\n"
        )
        return

    md_file = Path(changes_md_path).resolve()
    workdir = md_file.parent

    # Codex prefers running inside a git repo, but supports --skip-git-repo-check.
    skip_git_repo_check = not (workdir / ".git").exists()

    schema = {
        "type": "object",
        "properties": {
            "changelog_csv": {"type": "string"},
            "tests_csv": {"type": "string"},
        },
        "required": ["changelog_csv", "tests_csv"],
        "additionalProperties": False,
    }

    schema_path = workdir / ".codex_release_schema.json"
    out_json_path = workdir / ".codex_release_output.json"

    schema_path.write_text(json.dumps(schema, ensure_ascii=False, indent=2), encoding="utf-8")

    prompt = f"""
Read the file: {md_file.name}

Task:
1) Produce changelog.csv as CSV text with header:
Latest tested version,№,Issue,Merge request

Rules:
- One row per Merge Request in the changes file.
- № is sequential starting at 1.
- Merge request cell: "!<iid> <title>"
- Issue cell:
  - Prefer issues explicitly listed as closing/related issues.
  - Otherwise extract #<num> references from MR/commit messages if present.
  - If none: "Issue wasn't created"
- Latest tested version: Only in the FIRST row:
  "Revisions comparison: {from_ref} → {to_ref}"
  (Leave this column empty for all other rows.)

2) Produce tests.csv as CSV text with header:
SUB,API 23,API 25,API 27,API 28,API 29,API 30,API 31,API 33,API 34,API 35,API 36

Rules:
- Build a TEST PLAN (not results). Default cells empty.
- Include:
  - change-specific tests inferred from MR titles/descriptions/commit messages/diffs
  - plus general regression tests to confirm the app is OK
- Use section heading rows (SUB filled, API columns empty) to group tests.
- Use "TBD" if you want to mark "must test here"; otherwise leave blank.

Output format:
Return ONLY a JSON object with exactly:
- changelog_csv: "<csv text>"
- tests_csv: "<csv text>"
No extra keys, no markdown fences.
""".strip()

    cmd = [
        "codex",
        "exec",
        "--cd",
        str(workdir),
        "--sandbox",
        "read-only",
        "--ask-for-approval",
        "never",
        "--output-schema",
        str(schema_path),
        "-o",
        str(out_json_path),
    ]

    if skip_git_repo_check:
        cmd.append("--skip-git-repo-check")

        # --- build a Codex command that works across CLI versions ---
    # In some Codex builds, --ask-for-approval is a *global* flag and must come BEFORE the subcommand.
    # Also, older builds may not support it at all, so we feature-detect via `codex --help`.
    supports_ask_for_approval = False
    try:
        help_txt = subprocess.check_output(["codex", "--help"], text=True, stderr=subprocess.STDOUT)
        supports_ask_for_approval = "--ask-for-approval" in help_txt
    except Exception:
        supports_ask_for_approval = False

    cmd = ["codex"]

    # Put global flags BEFORE `exec` (fixes: "unexpected argument '--ask-for-approval' found")
    if supports_ask_for_approval:
        cmd += ["--ask-for-approval", "never"]

    cmd += [
        "exec",
        "--cd", str(workdir),
        "--sandbox", "read-only",
        "--output-schema", str(schema_path),
        "-o", str(out_json_path),
    ]

    if skip_git_repo_check:
        cmd.append("--skip-git-repo-check")

    # Read prompt from stdin (avoids Windows quoting pain)
    cmd.append("-")

    console.print("[cyan]Running Codex (non-interactive) to generate CSVs...[/cyan]")
    subprocess.run(cmd, input=prompt, text=True, check=True)


    raw = out_json_path.read_text(encoding="utf-8")
    data = _safe_json_loads(raw)

    changelog_csv = str(data["changelog_csv"]).strip() + "\n"
    tests_csv = str(data["tests_csv"]).strip() + "\n"

    (workdir / "changelog.csv").write_text(changelog_csv, encoding="utf-8")
    (workdir / "tests.csv").write_text(tests_csv, encoding="utf-8")

    console.print("[green]Generated:[/green] changelog.csv, tests.csv")


def main():
    settings, token = wizard()

    api_base = f"{settings.gitlab_base}/api/v4"
    pid = project_id_for_api(settings.project)

    project_web_base = (
        f"{settings.gitlab_base}/{settings.project}"
        if not settings.project.isdigit()
        else f"{settings.gitlab_base}/projects/{settings.project}"
    )

    session = requests.Session()
    session.headers.update({"PRIVATE-TOKEN": token})

    # Caches
    commit_details_cache: Dict[str, Dict[str, Any]] = {}
    commit_diffs_cache: Dict[str, List[Dict[str, Any]]] = {}
    commit_mrs_cache: Dict[str, List[Dict[str, Any]]] = {}
    mr_details_cache: Dict[int, Dict[str, Any]] = {}
    mr_commits_cache: Dict[int, List[Dict[str, Any]]] = {}
    mr_closes_cache: Dict[int, List[Dict[str, Any]]] = {}

    def maybe_sleep():
        if settings.sleep > 0:
            time.sleep(settings.sleep)

    def get_commit_details(sha: str) -> Dict[str, Any]:
        if sha in commit_details_cache:
            return commit_details_cache[sha]
        maybe_sleep()
        u = f"{api_base}/projects/{pid}/repository/commits/{sha}"
        data = api_get_json(session, u, label="commit_details")
        commit_details_cache[sha] = data
        return data

    def get_commit_diffs(sha: str) -> List[Dict[str, Any]]:
        if sha in commit_diffs_cache:
            return commit_diffs_cache[sha]
        maybe_sleep()
        u = f"{api_base}/projects/{pid}/repository/commits/{sha}/diff"
        params = {"unidiff": "true" if settings.unidiff else "false"}
        data = api_get_all_pages(session, u, params=params, per_page=settings.per_page, label="commit_diff")
        commit_diffs_cache[sha] = data
        return data

    def get_commit_mrs(sha: str) -> List[Dict[str, Any]]:
        if sha in commit_mrs_cache:
            return commit_mrs_cache[sha]
        maybe_sleep()
        u = f"{api_base}/projects/{pid}/repository/commits/{sha}/merge_requests"
        data = api_get_all_pages(session, u, per_page=settings.per_page, label="commit->mrs")
        commit_mrs_cache[sha] = data
        return data

    def get_mr_details(iid: int) -> Dict[str, Any]:
        if iid in mr_details_cache:
            return mr_details_cache[iid]
        maybe_sleep()
        u = f"{api_base}/projects/{pid}/merge_requests/{iid}"
        data = api_get_json(session, u, label="mr_details")
        mr_details_cache[iid] = data
        return data

    def get_mr_commits(iid: int) -> List[Dict[str, Any]]:
        if iid in mr_commits_cache:
            return mr_commits_cache[iid]
        maybe_sleep()
        u = f"{api_base}/projects/{pid}/merge_requests/{iid}/commits"
        data = api_get_all_pages(session, u, per_page=settings.per_page, label="mr_commits")
        mr_commits_cache[iid] = data
        return data

    def get_mr_closes_issues(iid: int) -> List[Dict[str, Any]]:
        if iid in mr_closes_cache:
            return mr_closes_cache[iid]
        maybe_sleep()
        u = f"{api_base}/projects/{pid}/merge_requests/{iid}/closes_issues"
        try:
            data = api_get_all_pages(session, u, per_page=settings.per_page, label="closes_issues")
        except Exception:
            data = []
        mr_closes_cache[iid] = data
        return data

    progress = Progress(
        SpinnerColumn(),
        TextColumn("[bold]{task.description}[/bold]"),
        BarColumn(),
        TextColumn("{task.completed}/{task.total}"),
        TimeElapsedColumn(),
        TimeRemainingColumn(),
        console=console,
        transient=False,
    )

    with progress:
        # Step 1: Compare
        compare_task = progress.add_task("Compare refs", total=1)
        compare_url = f"{api_base}/projects/{pid}/repository/compare"
        compare_params = {
            "from": settings.from_ref,
            "to": settings.to_ref,
            "straight": "true" if settings.straight else "false",
            "unidiff": "true" if settings.unidiff else "false",
            "per_page": settings.per_page,
        }
        compare = api_get_json(session, compare_url, params=compare_params, label="compare")
        progress.advance(compare_task, 1)

        compare_commits = compare.get("commits") or []
        diffs_summary = compare.get("diffs") or []
        compare_web = compare.get("web_url") or ""

        compare_shas = [c.get("id") for c in compare_commits if c.get("id")]
        compare_set: Set[str] = set(compare_shas)

        # Step 2: Discover MRs by commit association
        discover_task = progress.add_task("Discover merge requests from commits", total=max(1, len(compare_shas)))
        mr_index: Dict[int, Dict[str, Any]] = {}
        commit_has_mr: Dict[str, bool] = {sha: False for sha in compare_shas}

        for sha in compare_shas:
            mrs = get_commit_mrs(sha)
            if mrs:
                commit_has_mr[sha] = True
            for mr in mrs:
                iid = mr.get("iid")
                if iid is not None:
                    mr_index[int(iid)] = mr
            progress.advance(discover_task, 1)

        mr_iids = sorted(mr_index.keys())

        # Step 3: Pre-fetch MR commit lists
        prefetch_task = progress.add_task("Fetch MR commit lists", total=max(1, len(mr_iids)))
        mr_to_commits: Dict[int, List[Dict[str, Any]]] = {}
        for iid in mr_iids:
            commits = get_mr_commits(iid)
            commits_in_range = [c for c in commits if (c.get("id") or c.get("sha")) in compare_set]
            mr_to_commits[iid] = commits_in_range
            progress.advance(prefetch_task, 1)

        # Direct commits
        direct_shas = [sha for sha in compare_shas if not commit_has_mr.get(sha, False)]

        # Unique SHAs we expect to diff
        unique_shas: List[str] = []
        seen: Set[str] = set()
        for iid in mr_iids:
            for c in mr_to_commits.get(iid, []):
                sha = c.get("id") or c.get("sha") or ""
                if sha and sha not in seen:
                    seen.add(sha)
                    unique_shas.append(sha)
        for sha in direct_shas:
            if sha and sha not in seen:
                seen.add(sha)
                unique_shas.append(sha)

        build_task = progress.add_task("Fetch commit diffs + build markdown", total=max(1, len(unique_shas)))
        progressed: Set[str] = set()

        lines: List[str] = []
        lines.append(f"# GitLab changes: {settings.from_ref} → {settings.to_ref}\n")
        lines.append(f"- Project: `{settings.project}`")
        lines.append(f"- GitLab: {settings.gitlab_base}")
        if compare_web:
            lines.append(f"- Compare page: {compare_web}")
        lines.append("")

        lines.append("## Summary\n")
        lines.append(f"- Commits in range: **{len(compare_commits)}**\n")

        if diffs_summary:
            lines.append("### Files changed (from compare)\n")
            for d in diffs_summary:
                path = d.get("new_path") or d.get("old_path") or ""
                flags = []
                if d.get("new_file"):
                    flags.append("new")
                if d.get("deleted_file"):
                    flags.append("deleted")
                if d.get("renamed_file"):
                    flags.append("renamed")
                if d.get("too_large"):
                    flags.append("too_large")
                if d.get("collapsed"):
                    flags.append("collapsed")
                suffix = f" ({', '.join(flags)})" if flags else ""
                lines.append(f"- `{path}`{suffix}")
            lines.append("")

        # MR sections (per requested structure)
        if not mr_iids:
            lines.append("## Merge request\n")
            lines.append("> No merge requests were detected from commits in this compare range.\n")
        else:
            for iid in mr_iids:
                mr = get_mr_details(iid)
                title = mr.get("title") or mr_index[iid].get("title") or ""
                web_url = mr.get("web_url") or mr_index[iid].get("web_url") or ""
                state = mr.get("state") or ""
                merged_at = mr.get("merged_at") or ""
                author = (mr.get("author") or {}).get("name") or ""
                source_branch = mr.get("source_branch") or ""
                target_branch = mr.get("target_branch") or ""
                description = mr.get("description") or ""

                lines.append(f"## Merge request !{iid} {md(title)}\n")
                if web_url:
                    lines.append(f"- MR URL: {web_url}")
                if state:
                    lines.append(f"- State: {state}")
                if merged_at:
                    lines.append(f"- Merged at: {merged_at}")
                if author:
                    lines.append(f"- Author: {author}")
                if source_branch or target_branch:
                    lines.append(f"- Branches: `{source_branch}` → `{target_branch}`")
                lines.append("")

                if description.strip():
                    lines.append("**Description:**\n")
                    lines.append("```text")
                    lines.append(md(description).rstrip())
                    lines.append("```\n")

                closes = get_mr_closes_issues(iid)
                if closes:
                    lines.append("**Related issues (closes on merge, best effort):**")
                    seen_issues = set()
                    for iss in closes:
                        key = iss.get("web_url") or str(iss.get("id") or iss.get("iid") or "")
                        if key in seen_issues:
                            continue
                        seen_issues.add(key)
                        if iss.get("web_url"):
                            lines.append(f"- #{iss.get('iid')} {md(iss.get('title') or '')} — {iss['web_url']}")
                        else:
                            lines.append(f"- {md(iss.get('title') or '')}")
                    lines.append("")

                lines.append("### Commits (detailed)\n")

                mr_commits = mr_to_commits.get(iid, [])
                if not mr_commits:
                    lines.append("> No commits from this MR were found inside the compare range.\n")
                    lines.append("---\n")
                    continue

                mr_files: Set[str] = set()

                for j, mc in enumerate(mr_commits, start=1):
                    sha = mc.get("id") or mc.get("sha") or ""
                    short_id = mc.get("short_id") or (sha[:8] if sha else "")
                    c_title = mc.get("title") or ""

                    # Fetch full commit details (better message fidelity + URL)
                    cd = get_commit_details(sha) if sha else {}
                    full_message = cd.get("message") or mc.get("message") or ""
                    commit_web = cd.get("web_url") or ""
                    author_name = cd.get("author_name") or mc.get("author_name") or ""
                    author_email = cd.get("author_email") or mc.get("author_email") or ""
                    created_at = cd.get("created_at") or mc.get("created_at") or ""

                    lines.append(f"#### {j}. `{short_id}` {md(c_title)}\n")
                    if sha:
                        lines.append(f"- SHA: `{sha}`")
                    if commit_web:
                        lines.append(f"- Commit URL: {commit_web}")
                    if author_name or author_email:
                        lines.append(f"- Author: {author_name} <{author_email}>")
                    if created_at:
                        lines.append(f"- Created: {created_at}")
                    lines.append("")

                    msg_issue_links = extract_issue_links_from_text(full_message, project_web_base)
                    if msg_issue_links:
                        lines.append("**Issue links found in commit message (best effort):**")
                        for lnk in msg_issue_links:
                            lines.append(f"- {lnk}")
                        lines.append("")

                    lines.append("**Full commit message:**\n")
                    lines.append("```text")
                    lines.append(md(full_message).rstrip())
                    lines.append("```\n")

                    diffs = get_commit_diffs(sha) if sha else []
                    if sha and sha not in progressed:
                        progressed.add(sha)
                        progress.advance(build_task, 1)

                    lines.append("**Diff (per commit):**\n")
                    for d in diffs or []:
                        old_path = d.get("old_path") or ""
                        new_path = d.get("new_path") or ""
                        label = new_path if old_path == new_path else f"{old_path} -> {new_path}"
                        if new_path:
                            mr_files.add(new_path)
                        elif old_path:
                            mr_files.add(old_path)

                        lines.append(f"##### `{label}`\n")
                        lines.append("```diff")
                        lines.append(md(d.get("diff") or "").rstrip())
                        lines.append("```\n")

                if mr_files:
                    lines.append("**Files touched in this MR (derived from commit diffs):**")
                    for p in sorted(mr_files):
                        lines.append(f"- `{p}`")
                    lines.append("")

                lines.append("---\n")

        # Direct commits section
        if direct_shas:
            lines.append("## Direct commits (no merge request detected)\n")
            lines.append("> These commits are in the compare range but GitLab did not report an associated MR for them.\n")

            for idx, sha in enumerate(direct_shas, start=1):
                cd = get_commit_details(sha)
                short_id = cd.get("short_id") or sha[:8]
                title = cd.get("title") or ""
                commit_web = cd.get("web_url") or ""
                full_message = cd.get("message") or ""
                author_name = cd.get("author_name") or ""
                author_email = cd.get("author_email") or ""
                created_at = cd.get("created_at") or ""

                lines.append(f"### {idx}. `{short_id}` {md(title)}\n")
                lines.append(f"- SHA: `{sha}`")
                if commit_web:
                    lines.append(f"- Commit URL: {commit_web}")
                if author_name or author_email:
                    lines.append(f"- Author: {author_name} <{author_email}>")
                if created_at:
                    lines.append(f"- Created: {created_at}")
                lines.append("")

                msg_issue_links = extract_issue_links_from_text(full_message, project_web_base)
                if msg_issue_links:
                    lines.append("**Issue links found in commit message (best effort):**")
                    for lnk in msg_issue_links:
                        lines.append(f"- {lnk}")
                    lines.append("")

                lines.append("**Full commit message:**\n")
                lines.append("```text")
                lines.append(md(full_message).rstrip())
                lines.append("```\n")

                diffs = get_commit_diffs(sha)
                if sha and sha not in progressed:
                    progressed.add(sha)
                    progress.advance(build_task, 1)

                lines.append("**Diff (per commit):**\n")
                for d in diffs or []:
                    old_path = d.get("old_path") or ""
                    new_path = d.get("new_path") or ""
                    label = new_path if old_path == new_path else f"{old_path} -> {new_path}"
                    lines.append(f"#### `{label}`\n")
                    lines.append("```diff")
                    lines.append(md(d.get("diff") or "").rstrip())
                    lines.append("```\n")

                lines.append("---\n")

    # Write report
    with open(settings.out_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    console.print(
        Panel.fit(
            f"[bold green]Done![/bold green]\nWrote: [white]{settings.out_file}[/white]",
            border_style="green",
        )
    )

    # Optional Codex step
    if settings.run_codex:
        try:
            run_codex_csv_generation(settings.out_file, settings.from_ref, settings.to_ref)
        except subprocess.CalledProcessError as e:
            console.print(Panel.fit(f"[bold red]Codex failed[/bold red]\n{e}", border_style="red"))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[yellow]Interrupted.[/yellow]")
        sys.exit(130)
    except Exception as e:
        console.print(Panel.fit(f"[bold red]Error[/bold red]\n{e}", border_style="red"))
        sys.exit(1)
