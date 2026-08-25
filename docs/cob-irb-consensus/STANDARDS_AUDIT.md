# CoB IRB standards audit (Confidential / Drive / GitHub)

**Date:** 2026-08-12  
**Standards:** [DATA_CLASSIFICATION_CHEATSHEET.md](DATA_CLASSIFICATION_CHEATSHEET.md), [COB_IRB_WORKFLOW_NO_IT_APPROVAL.md](COB_IRB_WORKFLOW_NO_IT_APPROVAL.md), [NO_DELETE_RETENTION.md](NO_DELETE_RETENTION.md)

## Summary

| Check | Result | Notes |
|--------|--------|--------|
| Browser pack is Public guidance + demo/empty registry only | **Pass** | Live registry via import/export; demo JSON is synthetic |
| “Open Drive” links do not embed file bytes | **Pass** | `drive_folder_url` / nav links only |
| Registry has no delete control | **Pass** | Archive status + change_log only |
| `db.sqlite3`, `media/`, `.env` gitignored | **Pass** | Local Django DB/media stay off GitHub |
| No CITI PDFs / PI date files in git | **Fail → fixed** | `docs/citiCompletionCertificate_*.pdf` and `docs/citi_pi_dates.txt` were tracked; removed from index + gitignored |
| Study packet materials under `apps/studies/assets/irb/` | **Warn** | Some consent/CITI paths exist in the tree historically; treat as debt — prefer Drive for Confidential packets; do not add new certs to git |
| CoB consensus pack itself | **Pass** | Under `docs/cob-irb-consensus/` (untracked until you commit the pack intentionally) |

## Hard failures addressed this pass

1. Stop tracking Confidential CITI artifacts under `docs/`:
   - `docs/citiCompletionCertificate_4689946_59381539.pdf`
   - `docs/citi_pi_dates.txt`
2. `.gitignore` patterns added for `docs/citi*.pdf`, `docs/citi_pi_dates.txt`, and `**/hsirb_amendment_*/CITI/*.pdf`.

Remaining tracked study-material files under `apps/studies/assets/irb/` (e.g. consent docx) are **warned**, not mass-deleted, to avoid breaking local rebuild scripts. Do not commit new investigator certificates or live registries.

## Pass criteria for ongoing work

- GitHub: code + Public guidance + synthetic demos only  
- Drive: Confidential packets, CITI PDFs, live `protocol_registry.json`  
- Browser pack: metadata flags for renewal/CITI; Open Drive / Open CITI folder for files  
- No-delete: updates archive; never Trash  

## Follow-ups (not blocking this feature pass)

- Optional scrub commit: remove remaining sensitive assets from git history if they were ever pushed remote  
- Prefer per-protocol Drive folders as packets migrate off local MEDIA  
