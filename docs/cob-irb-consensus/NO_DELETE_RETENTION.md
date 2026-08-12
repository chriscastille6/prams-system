# Hard rule: no file deletion

**Under no circumstances may CoB IRB Drive files (or registry rows) be permanently deleted.**

IRB representatives must always be able to find prior materials. Updates are **supersessions with an audit trail**, not erasures.

## What “update” means

1. Keep the previous file (or registry snapshot).
2. Add or promote the new version as current.
3. Record **when** it changed and **what** changed (project `UPDATE_LOG.md` and/or registry `change_log`).
4. Move superseded packet files into that project’s `_archive/` folder with a dated subfolder — do **not** send them to Trash.

## What is allowed

| Action | Allowed? |
|--------|----------|
| Add new files / new protocol rows | Yes |
| Edit metadata and save a new export / new packet version | Yes |
| Mark a protocol `archived` in the registry (still retained) | Yes |
| Move older files into `_archive/YYYY-MM-DD_label/` | Yes |
| Highlight / note what changed in `UPDATE_LOG.md` or `CHANGE_NOTE.md` | Yes |
| Delete, Trash, or permanently remove Drive files | **No** |
| Remove protocol rows from the registry JSON | **No** (archive status only) |
| Empty Drive Trash for CoB HSIRB materials | **No** |

## Registry tool (browser)

The registry UI has **no Delete control**. Edits append a `change_log` entry. Export downloads a **dated snapshot** for Drive `_archive/` plus the live `protocol_registry.json` to keep as current — prior snapshots stay on Drive.

## If someone already deleted something

Restore from Google Drive Trash / version history immediately. Record the incident in minutes. Re-export registry from the last known good snapshot if needed.
