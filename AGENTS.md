# AGENTS.md — Release changelog + test plan generator

This folder contains:
- `gitlab_changes.py` — exports GitLab changes between refs into a Markdown file
- `output/changes_*.md` — generated output, e.g. `output/changes_v1.37_to_release-1.38.md`

## Your job (agent)
Given a generated `changes_*.md` file, produce two CSV outputs that can be copy-pasted/imported into Google Sheets:

1) `changelog.csv` — a table with columns:
  - Latest tested version
  - №
  - Issue
  - Merge request

2) `tests.csv` — a test plan matrix with columns:
  - SUB
  - API 23
  - API 25
  - API 27
  - API 28
  - API 29
  - API 30
  - API 31
  - API 33
  - API 34
  - API 35
  - API 36

## Input
- Prefer the file passed in the user prompt (example: `output/changes_v1.37_to_release-1.38.md`).
- If not specified, use the newest `changes_*.md` in `output/`. If none exist, use the newest `changes_*.md` in the current folder.
- The report ends with `## End of report`. Ensure you read through that marker. If the file is large, read in chunks until the end marker.

## Output rules (strict)
- Output CSV, not Markdown.
- Use comma as separator.
- Include a header row in each CSV.
- Quote fields that contain commas, quotes, or newlines (RFC4180 style).
- No extra commentary around the CSV content.

## How to fill `changelog.csv`
- Create 1 row per Merge Request found in the changes file.
- `№` = 1..N in the order you decide (prefer: merged_at ascending if available, otherwise MR number ascending).
- `Merge request` column format:
  - `!<iid> <title>`
- `Issue` column:
  - If the MR explicitly lists related/closing issues, include them like:
    - `#62 [rendering] Widget corners are twisted`
  - If multiple issues: separate with `; `
  - If none: write `Issue wasn't created`
- `Latest tested version` column:
  - Put a single label ONLY in the first row (leave the rest blank), format:
    - `Revisions comparison: <from_ref> → <to_ref>`

## How to fill `tests.csv` (test plan)
Goal: create comprehensive, risk-focused test points:
- Derive change-specific tests from MR titles/descriptions, commit messages, file lists, and diffs.
- Add app health smoke/regression tests.
- Think like an experienced Android developer: what can break, what user flows are affected, what regressions are likely.

### Structure guidance
- Use section rows as headings (put text in SUB, leave API columns empty).
- Example headings (use only what applies):
  - `update from old version`
  - `SDK / build / install`
  - `UI edge-to-edge / system bars`
  - `Activities / navigation`
  - `Widgets`
  - `Permissions`
  - `Background / alarms / idle`
  - `Data / storage / migrations`
  - `Networking / sync`
  - `Notifications`
  - `Billing`
  - `Localization / resources`
  - `Other changes`

- Under headings, add specific test rows, e.g.
  - `install clean + launch`
  - `upgrade from previous version`
  - `Status bar is ok (WelcomeActivity)`
  - `Nav bar is ok (SettingsActivity)`
  - `Widget: open event`
  - `Calendar events fetched`
  - `Permission request works`
  - `Exception posts notification (no widgets)`

### Change-to-test mapping (use flexibly)
- `build.gradle`, `gradle.properties`, `AndroidManifest.xml`, SDK/AGP changes → build/install/upgrade tests, permission/manifest behavior, API level compatibility.
- Activities/Fragments/Navigation changes → launch flows, back stack, deep links, configuration changes (rotation, multi-window).
- UI/layout/Compose/theme/resources → visual checks, edge-to-edge/system bars, dark/light, font scale, locale.
- Background/WorkManager/alarms/services → background execution, idle/doze, scheduling reliability.
- Permissions → prompt flow, denial handling, "never ask again" behavior.
- Storage/DB/migrations/files → data migration, data loss, cache clearing, offline mode.
- Networking/API changes → login/auth, sync, error handling, retries.
- Notifications → channels, badges, taps open correct screen.
- Widgets → add/update/remove, resize, click actions.
- Billing → purchase/restore/cancel flows.

### Cell values
- Default value is empty (so testers can fill it).
- Use:
  - `TBD` to explicitly mark "must test here"
  - `no GP` for rows that require Google Play on devices where it’s not available
  - `N/A` when a test is not applicable on a given API

### IMPORTANT
Don’t invent results. You are creating a plan (what to test), not a report.

## Deliverables
- Write `changelog.csv` and `tests.csv` into the same folder as the changes file (or print them to stdout if instructed).
- Ensure the CSVs can be pasted directly into Google Sheets without manual cleanup.
