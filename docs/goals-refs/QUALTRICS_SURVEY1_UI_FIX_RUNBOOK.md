# Qualtrics Survey 1 UI blockers — fix runbook

**Protocol:** IRBE20260914-003CBA — Goals as Reference Points / Everyday Decisions (`goals-refs`)  
**Not:** ARIM / goal-setting lab study  
**Audience:** Chris Castille (or any Mac/Qualtrics editor session)  
**Date of AI UI pilot findings:** 2026-09-14 (desktop Qualtrics)  
**Jon Murphy:** Addendum 1 (campus recruitment + optional bonus) approved 2026-09-14  

---

## STATUS / recruiting gate

**NOT READY TO RECRUIT.** Survey 1 is **not cleared**. Do **not** send faculty announcements or campus recruitment until Critical Qualtrics fixes are applied **live** and retested (**R1–R7** in this runbook).

| Tracker | Link |
|---------|------|
| CoS Drive activity report (`goals-refs` folder) | https://drive.google.com/file/d/1iwnoD3rshpQ6ns0xL9qp4OtdRwfN4Pdo/view |
| Faculty OS board | https://docs.google.com/document/d/163vnZGH_H8tfk98LN6zTBe52BS2wuyM7yEvWDnXa48I/edit |
| Sibling status note (this PR) | [COS_STATUS.md](./COS_STATUS.md) |

Fix steps below are unchanged; this section is the go/no-go gate only.

---

## Scope and limits

| Item | Status in this repo |
|------|---------------------|
| Live Survey 1 | Outside repo — edit in Nicholls Qualtrics only |
| Live Survey 2 | Outside repo — disconnected opt-in (Addendum 1) |
| Exported `.qsf` | **None found** in this repository (searched `**/*.{qsf,QSF}`) |
| This PR | Runbook only — **does not** claim live survey edits or invent API credentials |

**Live links (reference only; do not paste ResponseIds or real participant data here):**

- Survey 1 (research record): `https://nicholls.az1.qualtrics.com/jfe/form/SV_eRS6lxPutE2bmpU`
- Survey 2 (bonus / findings, disconnected): `https://nicholls.az1.qualtrics.com/jfe/form/SV_cYXnQT7hArWiq0e` (Survey ID `SV_cYXnQT7hArWiq0e`)

Related Drive packet (not in git): `goals-refs` / `Addendum_1_IRBE20260914`.  
Related repo materials: `apps/studies/assets/irb/goals-refs/`; CoB HSIRB consensus pack lives on branch `feat/cob-irb-consensus-pack` under `docs/cob-irb-consensus/` (includes mock consent that already specifies decline → end survey).

---

## Before you touch anything

1. **Delete AI pilot / test responses** in Survey 1 (and Survey 2 if any) before campus recruitment.  
   Qualtrics → Survey → **Data & Analysis** → select test rows → **Delete** (or filter by recorded date 2026-09-14 pilot).  
   Reminder from pilot: at least one AI pilot response was recorded.
2. Work in **Survey 1** (`SV_eRS6lxPutE2bmpU`) as **PI / Collaborator** with edit rights.
3. Prefer **Preview** / anonymous test link for retests; scrub any accidental real PII from chat/logs.
4. Publish (or re-activate) only after the retest checklist at the bottom passes.

---

## Finding → hypothesis map (non-binding)

Hypotheses below are **diagnostic guesses from the 2026-09-14 pilot**. They are not confirmed until you open Survey Flow / question validation in the live project.

| # | Severity | Observed behavior | Leading hypothesis (non-binding) | Fix target |
|---|----------|-------------------|----------------------------------|------------|
| 1 | **Critical** | “I do not consent” (or equivalent) + **Next** still advances to later items (e.g. “Which program do you favor?”) | Missing **Survey Flow Branch** + **End of Survey** after consent; and/or consent item lacks **Force Response**; and/or only soft Display Logic with no terminate | Consent decline → immediate End of Survey; vignette blocks never shown |
| 2 | **Critical** | Debrief promises independent Survey 2 / bonus / findings; run ends on generic Qualtrics thank-you on Survey 1 URL with **no** Survey 2 link/redirect | Default **End of Survey** message still in use; no **Redirect to URL**; no custom EOS message with bare Survey 2 hyperlink; no Survey Flow EOS override | End of Survey → Survey 2 with **no** shared token / ResponseId / timestamp linking |
| 3 | **Medium** | Leaving a choice blank + Next advances with no error | **Force Response** (and/or Request Response) not enabled on required questions; page break placement may skip validation | Enable Force Response on required items |
| 4 | Nit | No progress indicator; no on-page Back; buttons say “Next page.” | Look & Feel / Survey Options defaults | Optional low-risk polish only |
| 5 | Nit | Desktop / ~500px layout mostly OK | N/A | No change required |
| 6 | Info | Path taken had no age gate / matrix / free-text; Survey 1 did not ask name/email/ID | Anonymity claim OK for that path | Keep Survey 1 free of identifiers; email (if any) only on disconnected Survey 2 |

Protocol alignment (repo `apps/studies/assets/irb/goals-refs/protocol.json`): consent must allow opt-out and exit without penalty; measures follow consent. Addendum 1: Survey 2 stays **disconnected** from Survey 1 (no shared token, no ResponseId/timestamp join key).

---

## Fix A — Critical: consent decline must force-exit

### Goal

Selecting non-consent must **stop** the session before any vignette / program-favor / study measures. Declined participants must not see later questions.

### Recommended pattern (Survey Flow)

1. Open Survey 1 → **Survey** module → **Survey Flow**.
2. Confirm the **Consent** question lives in its **own block** (or the first block), **before** demographics / vignettes / “Which program do you favor?”.
3. Immediately **after** the Consent block in Survey Flow, **Add a New Element** → **Branch**.
4. Branch condition (example wording — match your live choice text exactly):
   - **If** Consent question **Is Selected** → `I do not consent` / `I do not agree` / equivalent decline option  
   *(If you use “I consent” as the only continue option, branch on the decline choice, not on “not equal to consent,” unless you also Force Response.)*
5. **Under that Branch**, **Add a New Element** → **End of Survey**.
6. Click **Customize** on that End of Survey element:
   - Check **Override Survey Options**.
   - **Custom end of survey message** (Library or typed): thank them; state they may close the window; **no** study measures collected; optional HSIRB/PI contact per approved consent.
   - Optional: mark as **Screened Out** (useful in Data & Analysis filters).  
   - **Do not** enable Redirect to Survey 2 on the decline path (bonus/findings are for completers per Addendum 1 intent).
7. **Save Flow**.

### Also set on the consent question itself

1. Select the consent multiple-choice question.
2. **Force Response** (required): Question → validation / requirements → **Force Response** **On**.  
   Without this, blank consent + Next can skip your Branch condition.
3. Keep consent on its own **page** (page break after consent) so Next submits consent before any later block renders.

### Vignette data for non-consent path

- If Branch + End of Survey fire **before** vignette blocks, vignette fields stay empty — that satisfies “do not collect vignette data on decline.”
- Prefer **keeping** the response row (consent = decline, Finished / Screened Out) as a research-admin record of the opt-out, unless the approved protocol explicitly requires **Do not record response**.  
  - Hypothesis only: protocol text in-repo treats electronic consent as part of the research record — default to **record the decline**, not “Do not record.”
- If someone already advanced past consent in the broken build, delete those pilot rows (see checklist).

### Retest (A)

Preview as new respondent:

- [ ] Select decline → Next → **immediate** end message; **no** later questions.
- [ ] Select consent → Next → study questions appear as designed.
- [ ] Leave consent blank → Next → **validation error**, not advance.

---

## Fix B — Critical: end of Survey 1 → disconnected Survey 2

### Goal

After a **completed** Survey 1 (consent yes + measures + debrief), participants reach Survey 2 (bonus / findings opt-in) **without** any link that could join datasets.

### Hard rule (Addendum 1)

**Forbidden** on the Survey 2 URL or as embedded/query fields passed from Survey 1:

- `ResponseID` / `${e://Field/ResponseID}`
- Survey 1 `SID` + response id pairs
- Timestamps, IP, or custom “match codes” shared across surveys
- Piped embedded data that is unique per Survey 1 session

**Allowed:** the bare anonymous Survey 2 link only:

`https://nicholls.az1.qualtrics.com/jfe/form/SV_cYXnQT7hArWiq0e`

### Option B1 — Redirect (cleanest UX)

1. Survey Flow → at the **end** of the completer path (after debrief block), **Add** → **End of Survey** (or customize the default terminator).
2. **Customize** → **Override Survey Options** → **Redirect to a URL**.
3. Paste **only** the bare Survey 2 URL above — **no** `?` query string, **no** piped fields.
4. Ensure no other Survey Options redirect appends parameters.
5. **Save Flow**.

### Option B2 — Custom end message with explicit link (safest if redirect is blocked on account)

1. End of Survey → **Custom end of survey message**.
2. Debrief text (approved language) plus a clear line, e.g.:  
   “Optional and separate: to enter the bonus drawing and/or request a summary of findings, open this independent form (not linked to your answers):”  
   then hyperlink the bare Survey 2 URL.
3. Do **not** also pipe ResponseId into the message “for your records” if that could encourage screenshot-joining; keep Survey 2 fully optional and unlinked.

### Debrief copy check

1. Find the debrief question or Text/Graphic block that currently **promises** redirect to Survey 2.
2. Align wording with the mechanism you chose (auto-redirect **or** clickable link).
3. Remove any claim that Survey 1 “will send you” somewhere if the default thank-you is still active — the pilot failure mode was the generic “Your response has been recorded” with no Survey 2 affordance.

### Survey 2 side (quick)

1. Confirm Survey 2 does **not** expect a URL token from Survey 1.
2. Confirm Survey 2 collects contact only if Addendum 1 allows, and stores it **only** in Survey 2.

### Retest (B)

- [ ] Complete Survey 1 through debrief → land on Survey 2 **or** see a working Survey 2 link.
- [ ] Inspect the browser address bar for Survey 2: **no** ResponseId, timestamp, or custom join query params.
- [ ] Decline-consent path (Fix A) does **not** open Survey 2.

---

## Fix C — Medium: Force Response on required questions

### Goal

Blank required choices must not advance.

1. For each required multiple-choice / vignette choice / attention check:
   - Open the question → enable **Force Response**.
2. Optional softer control: **Request Response** (warning only) — **not sufficient** alone for Critical/Medium pilot failures; use Force Response on required items.
3. Confirm **page breaks**: validation runs when the respondent leaves the page; a question on the same page as Next is fine, but do not rely on later pages to “catch” earlier blanks.
4. If any item is intentionally optional (e.g. optional comments), leave Force Response **Off** and label it optional in the stem.

### Retest (C)

- [ ] On a required question, leave unanswered → Next → error, stay on page.
- [ ] Answer → Next → advances.

---

## Fix D — Optional nits (low risk only)

Apply only if they will not disturb logic already tested.

| Nit | Where | Suggested setting |
|-----|--------|-------------------|
| Progress bar | **Look & Feel** → General / Progress | Show progress bar |
| Back button | **Survey Options** → Responses (or equivalent) | Allow respondents to go back (**On**) — retest that Back cannot bypass consent Branch oddly |
| Next label | Look & Feel → Buttons / Motion, or question page settings | Change “Next page” → **Next** or **Continue** |

Skip age gate / matrix / free-text changes unless the approved instrument requires them; pilot path did not include those.

---

## Suggested Survey Flow sketch (completer vs decline)

```text
[Block: Consent]     ← Force Response on consent item
    |
    +-- Branch: Consent = Decline
    |      └── End of Survey (custom decline message; NO Survey 2 redirect)
    |
[Block(s): Demographics / Vignettes / Attention]  ← Force Response on required items
    |
[Block: Debrief]
    |
[End of Survey — completers]
    Customize → Redirect to bare Survey 2 URL
    OR custom message with bare Survey 2 hyperlink
    (NO ResponseId / timestamp / join token)
```

---

## Publish and cleanup

1. **Tools / Publish** (or your account’s activate flow) so the anonymous link serves the new flow.
2. **Data & Analysis:** delete remaining test/pilot rows (including the 2026-09-14 AI pilot response) before recruitment emails/flyers go out.
3. Optionally export a new `.qsf` from Qualtrics (**Tools → Export → QSF**) and store it in the Drive packet `Addendum_1_IRBE20260914` — **not** required for this PR; do not commit response CSVs or real PII to git.

---

## Retest checklist (copy/paste)

Run in **Preview** or a private anonymous window. Use synthetic answers only.

| Step | Action | Pass criteria |
|------|--------|---------------|
| R1 | Decline consent → Next | Ends immediately; no vignette / “program favor” items |
| R2 | Consent blank → Next | Force Response error; no advance |
| R3 | Consent yes → leave a required vignette blank → Next | Force Response error; no advance |
| R4 | Full complete path through debrief | Survey 2 opens via redirect **or** clear link |
| R5 | Inspect Survey 2 URL | Bare form URL only — no shared token / ResponseId / timestamp params |
| R6 | Decline path | Does **not** reach Survey 2 |
| R7 | Data & Analysis | Decline row has no vignette answers; completer row has measures; delete all test rows before go-live |

---

## Repo investigation notes (for reviewers)

| Search | Result |
|--------|--------|
| `goals-refs` assets | `apps/studies/assets/irb/goals-refs/` (`protocol.json`, `study_config.json`, vignettes) |
| Protocol consent language | Electronic consent with opt-out / exit; measures after consent; Qualtrics (or equivalent) named as collection method |
| `.qsf` export | **Not present** — live edits are Qualtrics UI only |
| `docs/cob-irb-consensus` | On `feat/cob-irb-consensus-pack`; mock consent already says decline → end survey |
| ARIM / goal-setting lab packet | Separate (`apps/studies/assets/irb/goal-setting/`) — **out of scope** |

---

## Success criterion

Chris can open this runbook beside Qualtrics and fix Critical #1–#2 and Medium #3 without guessing, then pass R1–R7 before recruiting.
