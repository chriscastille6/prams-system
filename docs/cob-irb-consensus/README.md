# CoB IRB Consensus Tooling (post–Bayou PAL)

Public pack for College of Business HSIRB representatives: proportionate social/behavioral standards, process guidance, consensus checklist, Drive-held protocol registry (browser tool), and Qualtrics PI guidance.

## Quick start (no install)

```bash
cd docs/cob-irb-consensus/browser
python3 -m http.server 8765
```

Open http://localhost:8765/

Or open `browser/index.html` directly (Mermaid diagrams and demo JSON fetch work more reliably via the static server).

## Contents

| Path | Description |
|------|-------------|
| [CHARTER.md](CHARTER.md) | Operating charter — purpose, Data Owner, what this is not |
| [NO_DELETE_RETENTION.md](NO_DELETE_RETENTION.md) | Hard rule: never delete; update + archive with change notes |
| [COB_IRB_WORKFLOW_NO_IT_APPROVAL.md](COB_IRB_WORKFLOW_NO_IT_APPROVAL.md) | Day-to-day use for Chris + Jon without IT product approval |
| [PRAMS_GITHUB_GDRIVE_PLAN.md](PRAMS_GITHUB_GDRIVE_PLAN.md) | Plan: PRAMS code on GitHub + study materials on Nicholls Drive (Jon Murphy UX) |
| [DATA_MAP.md](DATA_MAP.md) | Public / Internal / Confidential map (shared Drive URL recorded) |
| [DATA_CLASSIFICATION_CHEATSHEET.md](DATA_CLASSIFICATION_CHEATSHEET.md) | Generally available: what is vs isn’t Confidential (Nicholls floor + CoB IRB) |
| [STANDARDS_AUDIT.md](STANDARDS_AUDIT.md) | Audit vs classification / Drive / GitHub (pass/fail + fixes) |
| [DRIVE_FOLDER_SCHEMA.md](DRIVE_FOLDER_SCHEMA.md) | Drive folders, per-project `_archive/`, access model |
| [templates/](templates/) | `UPDATE_LOG` and `CHANGE_NOTE` templates |
| [browser/](browser/) | HTML pack: standards, process, checklist, registry (renewal + CITI), retention, Qualtrics |
| [mock-qualtrics/](mock-qualtrics/) | Synthetic Qualtrics question templates for PIs |

## Jon / CoB IRB — renewal & CITI (shared path)

1. Open `browser/registry.html` (static server or Pages).
2. **Import** live `protocol_registry.json` from Drive (never commit the filled file).
3. Check **Needs renewal**: yellow ≤30 days; red overdue (pause continuing activity until renewed).
4. Check **CITI attention**: open Drive CITI folder → confirm each investigator PDF → set `citi_on_drive` + expiration → **CITI recheck** prompts if needed.
5. **Export** a dated snapshot to Drive `_archive/`; update the live registry file (no delete).

Details: [COB_IRB_WORKFLOW_NO_IT_APPROVAL.md](COB_IRB_WORKFLOW_NO_IT_APPROVAL.md), [browser/process.html](browser/process.html).

## Hard rules

- **No file deletion** — update and archive with dated change notes only ([NO_DELETE_RETENTION.md](NO_DELETE_RETENTION.md)).
- Live `protocol_registry.json` stays on CoB IRB Google Drive — never commit filled data; keep dated snapshots under Drive `_archive/`.
- CITI PDFs stay on Drive only — never commit certificates to GitHub ([STANDARDS_AUDIT.md](STANDARDS_AUDIT.md)).
- Qualtrics responses stay in Qualtrics (PI-owned).
- No in-house signup or credit ledger.
- No auto-email bots; use Copy reminder in the registry tool.

## Optional later

Publish `browser/` via GitHub Pages from the public shell repo when ready.
