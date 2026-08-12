# Mock Qualtrics block — Eligibility screener

**Synthetic template only.** Align items with the approved protocol’s inclusion/exclusion criteria.

## Survey title

`[STUDY SHORT TITLE] — Eligibility (demo)`

## Intro text

Please answer the following questions to see whether you appear eligible for `[STUDY SHORT TITLE]`. Your answers are used only for eligibility screening as described in the protocol.

## Q1 — Age

Are you 18 years of age or older?

- Yes
- No → ineligible branch

## Q2 — Affiliation (edit to match protocol)

Are you currently `[e.g., enrolled as a student at Nicholls State University / employed in an organization of type X]`?

- Yes
- No → ineligible branch (if required by protocol)

## Q3 — Protocol-specific inclusion

`[CUSTOM YES/NO ITEM FROM PROTOCOL]`

- Yes
- No

## Q4 — Exclusion check

Do any of the following apply? `[LIST EXCLUSION CRITERIA FROM PROTOCOL]`

- None of these apply
- One or more apply → ineligible branch

## Branches

- **Eligible:** Continue to consent acknowledgment or main measures (separate blocks).
- **Ineligible:** “Based on your answers, you do not appear eligible for this study. Thank you for your interest.”

## Notes for PIs

- Do not store eligibility CSVs in GitHub.
- If screening collects identifiers, classify as Confidential and keep in Qualtrics / Drive under Data Owner controls.
