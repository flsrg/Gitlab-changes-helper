\# AGENTS.md — Release changelog + test plan generator



This folder contains:

\- `gitlab\_changes.py` — exports GitLab changes between refs into a Markdown file

\- `changes\_\*.md` — generated output, e.g. `changes\_v1.37\_to\_release-1.38.md`



\## Your job (agent)

Given a generated `changes\_\*.md` file, produce two CSV outputs that can be copy-pasted/imported into Google Sheets:



1\) `changelog.csv` — a table with columns:

&nbsp;  - Latest tested version

&nbsp;  - №

&nbsp;  - Issue

&nbsp;  - Merge request



2\) `tests.csv` — a test plan matrix with columns:

&nbsp;  - SUB

&nbsp;  - API 23

&nbsp;  - API 25

&nbsp;  - API 27

&nbsp;  - API 28

&nbsp;  - API 29

&nbsp;  - API 30

&nbsp;  - API 31

&nbsp;  - API 33

&nbsp;  - API 34

&nbsp;  - API 35

&nbsp;  - API 36



\## Input

\- Prefer the file passed in the user prompt (example: `changes\_v1.37\_to\_release-1.38.md`).

\- If not specified, use the newest `changes\_\*.md` in the current folder.



\## Output rules (strict)

\- Output \*\*CSV, not Markdown\*\*.

\- Use \*\*comma\*\* as separator.

\- Include a \*\*header row\*\* in each CSV.

\- Quote fields that contain commas, quotes, or newlines (RFC4180 style).

\- No extra commentary around the CSV content.



\## How to fill `changelog.csv`

\- Create 1 row per Merge Request found in the changes file.

\- `№` = 1..N in the order you decide (prefer: merged\_at ascending if available, otherwise MR number ascending).

\- `Merge request` column format:

&nbsp; - `!<iid> <title>`

\- `Issue` column:

&nbsp; - If the MR explicitly lists related/closing issues, include them like:

&nbsp;   - `#62 \[rendering] Widget corners are twisted`

&nbsp; - If multiple issues: separate with `; `

&nbsp; - If none: write `Issue wasn't created`

\- `Latest tested version` column:

&nbsp; - Put a single label ONLY in the first row (leave the rest blank), format:

&nbsp;   - `Revisions comparison: <from\_ref> → <to\_ref>`



\## How to fill `tests.csv` (test plan)

Goal: create \*\*comprehensive test points\*\*:

\- Change-specific tests derived from:

&nbsp; - MR titles/descriptions

&nbsp; - commit messages

&nbsp; - file list and diffs (activities, UI, Gradle/SDK changes, resources/strings)

\- PLUS general “app health” tests (smoke/regression)



\### Structure guidance

\- Use section rows as headings (put text in SUB, leave API columns empty):

&nbsp; - Example headings:

&nbsp;   - `update from old version`

&nbsp;   - `SDK / build / install`

&nbsp;   - `UI edge-to-edge / system bars`

&nbsp;   - `Activities`

&nbsp;   - `Widget`

&nbsp;   - `Permissions`

&nbsp;   - `Background / alarms / idle`

&nbsp;   - `Billing`

&nbsp;   - `Other changes`

\- Under headings, add specific test rows, e.g.

&nbsp; - `install clean + launch`

&nbsp; - `upgrade from previous version`

&nbsp; - `Status bar is ok (WelcomeActivity)`

&nbsp; - `Nav bar is ok (SettingsActivity)`

&nbsp; - `Widget: open event`

&nbsp; - `Calendar events fetched`

&nbsp; - `Permission request works`

&nbsp; - `Exception posts notification (no widgets)`

&nbsp; - Billing flows if relevant



\### Cell values

\- Default value is empty (so testers can fill it).

\- Use:

&nbsp; - `TBD` if you want to explicitly mark “must test here”

&nbsp; - `no GP` for rows that require Google Play on devices where it’s not available

&nbsp; - `N/A` when a test is not applicable on a given API



\### IMPORTANT

Don’t invent results. You are creating a \*\*plan\*\* (what to test), not a report.



\## Deliverables

\- Write `changelog.csv` and `tests.csv` into the current folder (or print them to stdout if instructed).

\- Ensure the CSVs can be pasted directly into Google Sheets without manual cleanup.



