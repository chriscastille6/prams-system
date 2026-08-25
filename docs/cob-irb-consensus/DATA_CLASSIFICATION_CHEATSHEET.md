# What is vs is not Confidential (generally available)

**Educational summary for CoB IRB / PRAMS workflows — not legal advice.**  
**Authority:** Nicholls State University [Data Classification Policy (July 2024)](https://www.nicholls.edu/information-tech/wp-content/uploads/sites/30/2025/10/Nicholls-State-University-Data-Classification-Policy-July-2024.pdf) · [IT policy index](https://www.nicholls.edu/information-tech/policyandprocedure/)  
**Related:** FERPA; La. R.S. 17:3914 (student PII); Louisiana public-records law (Title 44 — openness with exemptions); EO JML 25-109 §6 (no PII / confidential / restricted into AI until required policies exist).

Being a **public institution** does **not** mean “everything we hold is Public.” It means (1) some records are subject to public-records requests, and (2) many education/personnel/research materials still sit in **Confidential** or **Internal** under campus classification until properly released or exempted. When unsure: treat as Internal/Confidential and ask **Legal Counsel / data owner**.

## Nicholls three levels (official floor)

| Level | Policy idea | Typical examples (from IT policy summaries) | Default controls |
|--------|-------------|-----------------------------------------------|------------------|
| **Confidential** | Unauthorized disclosure would cause serious harm | PII (SSN, license, passport); financial/NPFI; health; **student records** (grades, transcripts, student IDs — FERPA); personnel (salary, performance); **sensitive/proprietary research** and unpublished manuscripts | Encrypt in transit/at rest; least privilege; MFA on sensitive systems |
| **Internal** | Not for general public release | Internal email/memos/reports; non-public budgets/plans; internal project docs; aggregated analysis not cleared for public release | Need-to-know; passwords/RBAC |
| **Public** | Intended for open release | Course catalogs, press releases, job postings; **published** research; marketing materials | Integrity / accuracy before release |

Data **Owners** (departments/units) classify. Reclassify when use changes (e.g., Internal draft → Public report).

## CoB IRB / PRAMS quick map

| Item | Usual class | Where it should live |
|------|-------------|----------------------|
| Social Science IRB Standards, process pages, mock Qualtrics text | **Public** | GitHub / browser pack |
| Protocol short titles, approval/renewal dates without identifiers | Often **Internal** | Drive registry / PRAMS metadata |
| Live `protocol_registry.json` with PI names | **Internal** | Nicholls Drive only |
| Consent forms, CITI certificates, HSIRB packets, recruitment with people | **Confidential** (or Internal until Counsel says otherwise) | Nicholls Drive; never GitHub / consumer AI |
| Student rosters, grades, Canvas exports, credit ledgers tied to students | **Confidential** (FERPA / La. R.S. 17:3914) | Not in GitHub; not in consumer AI; instructor/approved systems only |
| Qualtrics response exports with identifiers | **Confidential** | Qualtrics / Drive with least privilege |
| Synthetic demo data, empty schemas | **Public** | GitHub |
| Published, journal-released manuscripts | **Public** (once published) | Anywhere appropriate |
| Unpublished manuscripts / proprietary research drafts | Often **Confidential** | Drive / restricted |

## FERPA “usually” vs “usually not” (education records)

Useful teaching frame (from campus AOL legal/ethics materials — still not Counsel advice):

**Usually protected as education records (when maintained by the school and directly related to a student):** grades, transcripts, student IDs, submitted student work, identifiable survey/assessment rows, many LMS exports.

**Usually not an education record by themselves:** a course **syllabus** / catalog description about the course (instructional material, not tied to one student); already-public institutional announcements.

**Default before disclosure of education records:** consent or a valid exception; public reports use de-identified / *k*-safe aggregates — not row dumps.

## Public records (Louisiana) — openness ≠ “paste into AI”

Public institutions face a **presumption of openness** under Title 44, **with exemptions** (examples discussed in campus materials include proprietary/unpublished research and academic exam materials under R.S. 44:4(16), and other postsecondary provisions Counsel may cite).  

**Often treated as more open:** published catalogs, final public reports, job postings already released.  
**Often not freely open / still Internal–Confidential until cleared:** unfinished drafts, Confidential-class files, small-*n* stewarded packs, personnel files, education records.

Public-records eligibility ≠ permission to put the file into consumer AI (EO §6 still applies to confidential/restricted/PII inputs).

## AI paste rule of thumb

| Class | Consumer / non-approved AI |
|--------|----------------------------|
| Public | Generally OK if accurate and not mixed with restricted content |
| Internal | Prefer synthetic/minimized; escalate if unsure |
| Confidential | **Do not paste** unless an IT-approved enterprise path exists |

## Where fuller campus narrative lives

- Official: Nicholls Data Classification PDF (link above)  
- Practice / teaching deck in AOL: `aol_site/aol_privacy_bridge_pitch.html` (EO → BoR → FERPA → Confidential → public records → IT/Counsel)  
- AOL FERPA tutorial / PID drafts under `AOL/docs/` (when present)  

Escalate grey cases to **Legal Counsel**; IT policy is the floor, not a substitute for Counsel on public-records or FERPA edge cases.
