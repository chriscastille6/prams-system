# CoB IRB Drive Folder Schema

**Data Owner:** CoB IRB representatives  
**Shared folder URL:** https://drive.google.com/drive/folders/1jGaOtprui6PUq7r5W6qR6QYC9sRRXQpG  
**Folder ID:** `1jGaOtprui6PUq7r5W6qR6QYC9sRRXQpG`  
**Editors (confirmed 2026-08-11):** Jon Murphy, Chris Castille

**Hard rule:** [NO_DELETE_RETENTION.md](NO_DELETE_RETENTION.md) — never delete Drive files; only update, supersede, and archive with dated change notes.

**Also present on this root today (do not remove):** `Approvals/`, `Submitted Documentation/`, `CITI_Certificates/` (investigator certificates for packet work). Keep those; add the numbered CoB schema folders below as the shared root grows beyond a single protocol.

Recommended folder layout on Nicholls Google Drive under the shared root above. Create these folders if they do not already exist. Do **not** sync filled contents into GitHub.

```
CoB-HSIRB/                          ← shared root (folder id 1jGaOtprui6PUq7r5W6qR6QYC9sRRXQpG)
├── 00_Access/
│   └── ACCESS_LIST.md              ← who has Editor vs Viewer (Internal)
├── 01_Minutes/
│   └── YYYY-MM-DD_meeting.md       ← deliberation / consensus notes (append-only preferred)
├── 02_Working_Drafts/
│   └── …                           ← process drafts before they are Public
├── 03_Protocol_Registry/
│   ├── protocol_registry.json      ← LIVE current registry
│   └── _archive/                   ← dated registry snapshots (never delete)
│       └── protocol_registry_YYYY-MM-DD.json
├── 04_Packets_Staging/             ← Confidential when filled
│   └── {protocol_id}/              ← one folder per project / protocol
│       ├── UPDATE_LOG.md           ← running change log (required)
│       ├── CURRENT/                ← latest packet files
│       └── _archive/               ← superseded versions (never delete)
│           └── YYYY-MM-DD_short-label/
│               ├── CHANGE_NOTE.md  ← what changed, why, who
│               └── …               ← prior PDFs/docs moved here
└── 05_Templates/                   ← blank forms / copies of Public templates
    └── project_UPDATE_LOG_template.md
```

## Per-project update workflow

When a packet or file must change:

1. Copy everything currently in `CURRENT/` into `_archive/YYYY-MM-DD_short-label/`.
2. Add `CHANGE_NOTE.md` in that archive folder (date, who, what changed, why).
3. Put the new/updated files in `CURRENT/`.
4. Append a row to that project’s `UPDATE_LOG.md`.
5. If approval/renewal metadata changed, update the registry tool → export live JSON **and** a dated snapshot into `03_Protocol_Registry/_archive/` (do not trash the previous live file until the new live file is saved; then **move** the previous live file into `_archive/`, do not delete it).

## Access model

| Role | Drive access | Typical use |
|------|--------------|-------------|
| CoB IRB representative | Editor on root | Minutes, registry, staging — **no Trash emptying** |
| CoB IRB chair / lead (if designated) | Editor | Same + access list |
| PI (case-by-case) | Viewer or limited folder only | Own packet staging when needed — not the full registry by default |
| Students / public | None | Use Public GitHub pack only |

## Registry file rules

1. Keep the **live** `protocol_registry.json` under `03_Protocol_Registry/`.
2. Open the browser registry tool → **Import** from Drive.
3. After edits → **Export current** and **Export dated snapshot**; place snapshot in `_archive/`; replace live only by uploading the new current file and **moving** (not deleting) the prior live file into `_archive/`.
4. Never remove protocol rows — set `status` to `archived` only.
5. Never commit the live file to GitHub. The repo may contain only schema + synthetic demo.

## Minutes template (copy into `01_Minutes/`)

```markdown
# CoB IRB notes — YYYY-MM-DD

Attendees: (names)
Protocols discussed: (protocol_id list only; no participant data)
Consensus / actions:
Renewals flagged:
Files updated (protocol_id → archive label): 
Next meeting:
```

## Project UPDATE_LOG template

See `05_Templates` copy: also in the Public pack at [templates/project_UPDATE_LOG_template.md](templates/project_UPDATE_LOG_template.md).
