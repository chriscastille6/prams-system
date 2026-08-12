# CoB IRB Data Map

Shared CoB Drive folder URL is recorded below (user-supplied).

## Classification → location

| Class | Examples | Allowed tools / location | Never |
|--------|----------|---------------------------|--------|
| **Public** | Social Science standards, process HTML, consensus checklist, Qualtrics mock copy, `protocol_registry.schema.json`, `protocol_registry.demo.json` (synthetic) | GitHub; open in browser | — |
| **Internal** | Meeting minutes, deliberation notes, access list, **live** `protocol_registry.json`, process drafts | Nicholls Google Drive (CoB IRB) | Commit to GitHub; paste into consumer AI |
| **Confidential** | HSIRB packets with real PI/participant identifiers, CITI certificates of named individuals, Qualtrics response CSVs, recruitment lists | Drive (restricted) and/or Qualtrics | GitHub; consumer AI; public pages |

## Protocol registry

| Artifact | Classification | Notes |
|----------|----------------|--------|
| Schema + empty example | Public | Shipped in this pack |
| Synthetic demo JSON | Public | Fake protocol IDs and PI labels only |
| Live registry used by CoB IRB | Internal | Drive only; import into browser via file picker; export and save back to Drive |

## Qualtrics

| Artifact | Classification | Owner |
|----------|----------------|--------|
| Mock survey question text in this pack | Public | CoB guidance |
| Live surveys and responses | Confidential (often) | PI; responses stay in Qualtrics |

## Retention (no delete)

| Rule | Practice |
|------|----------|
| Never permanently delete CoB HSIRB Drive files | Move superseded files to project `_archive/` |
| Never remove protocol rows from the registry | Set `status: archived`; append `change_log` |
| Always record updates | Project `UPDATE_LOG.md` + archive `CHANGE_NOTE.md` + registry snapshots |

Full policy: [NO_DELETE_RETENTION.md](NO_DELETE_RETENTION.md).

## Drive URL

- **Shared folder URL:** https://drive.google.com/drive/folders/1jGaOtprui6PUq7r5W6qR6QYC9sRRXQpG
- **Folder ID:** `1jGaOtprui6PUq7r5W6qR6QYC9sRRXQpG`
- **Source:** User-supplied CoB shared folder URL (locked into this pack for docs/pointers only; do not browse/list contents from agents)
- **Data Owner:** CoB IRB representatives
- **Access:** Managed by Data Owner (least privilege; MFA via university Google accounts). **Confirmed (user, 2026-08-11):** Jon Murphy and Chris Castille both have **Editor** on the root folder.
- **Note (observed layout):** Drive title is currently “A Study in Decision Making” (owner Murphy), with existing children such as `Approvals/`, `Submitted Documentation/`, plus `CITI_Certificates/` for named investigator certificates. Recommended CoB schema folders in [DRIVE_FOLDER_SCHEMA.md](DRIVE_FOLDER_SCHEMA.md) can be added alongside without replacing this URL.
