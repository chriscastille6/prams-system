# CoB IRB Operating Charter

**Al Danos College of Business — HSIRB representatives**  
Nicholls State University

## Purpose

Provide a shared mental model and lightweight tooling for College of Business (CoB) social and behavioral research review after Bayou PAL / SONA hosting is unavailable. This pack supports proportionate ethics review, process consensus among CoB IRB representatives, and tracking of approved-protocol renewal dates.

## Data Owner

**CoB IRB representatives** own:

- Who may access the shared university Google Drive folder
- The live protocol registry file (approval / renewal / archive)
- Working drafts, meeting minutes, and deliberation notes

Drive location: https://drive.google.com/drive/folders/1jGaOtprui6PUq7r5W6qR6QYC9sRRXQpG (folder id `1jGaOtprui6PUq7r5W6qR6QYC9sRRXQpG`; see `DRIVE_FOLDER_SCHEMA.md` / `DATA_MAP.md`). **Editors confirmed (2026-08-11):** Jon Murphy, Chris Castille.

## What lives where

| Class | Examples | Location |
|--------|----------|----------|
| **Public** | Social Science IRB Standards, CoB process pages, consensus checklist, Qualtrics mock templates, empty registry schema, synthetic demo registry | This GitHub pack (`docs/cob-irb-consensus/`) |
| **Internal** | Minutes, deliberation drafts, **live** `protocol_registry.json` | CoB IRB Google Drive |
| **Confidential** | Real HSIRB packets with identifiers, Qualtrics response exports, participant data | Drive and/or Qualtrics only — never GitHub, never consumer AI |

## What PIs own

- Project-specific Qualtrics surveys and response data
- Recruitment and session scheduling for their own studies
- Course-credit arrangements with instructors (this pack does not run a credit ledger)

## Hard rule: no deletion

**Files and registry rows are never permanently deleted.** Updates supersede prior versions: move old packet files into a project `_archive/` folder with a dated change note; keep registry history via `change_log` and dated Drive snapshots. See [NO_DELETE_RETENTION.md](NO_DELETE_RETENTION.md). IRB representatives must always be able to find prior materials.

## What this is not

- IT-approved or IT-secured SaaS
- A participant signup / SONA replacement
- A credit accounting system
- An automated email notification service (reps copy a reminder and send via university email)
- A system that erases history (Trash / permanent delete is out of policy)

## IT posture (how to describe this)

Public research-governance guidance on GitHub; operational files on Nicholls Google Drive under CoB IRB access control. Faculty/IRB **Data Owner** workflows per Nicholls Data Classification and Acceptable Use policies. No claim of IT product endorsement. No Confidential data in GitHub or consumer AI (including Louisiana EO JML 25-109 §6 constraints on PII/confidential inputs to AI).

## Authority

This charter does not replace Nicholls HSIRB authority, institutional policy, or federal human-subjects requirements. It improves fit between CoB social/behavioral research and proportionate review.

## Adoption

CoB IRB representatives adopt this charter by agreeing on Drive access, using the browser pack for guidance and registry work, and keeping live registry / packets off GitHub.
