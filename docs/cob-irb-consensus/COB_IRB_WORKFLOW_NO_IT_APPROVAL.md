# CoB IRB workflow (no IT product approval, no local server)

**Audience:** Chris Castille and Jon Murphy  
**Constraints:** IT will not approve/secure faculty SaaS. **Django/local runserver is out** for shared use. Prefer **browser-openable tooling** (no install) + Nicholls Google Drive + shared GitHub for code/docs.

Shared Drive root: https://drive.google.com/drive/folders/1jGaOtprui6PUq7r5W6qR6QYC9sRRXQpG

## Recommended stack (revised)

| Piece | Where | Notes |
|--------|--------|--------|
| **Materials** (packets, CITI, approvals) | Nicholls Google Drive | Campus storage + SSO/MFA; you + Jon = Editors |
| **IRB management UI** | Static browser pack in GitHub (`docs/cob-irb-consensus/browser/`) | Open via GitHub Pages or download ZIP → open `index.html` / tiny static preview — **no install, no always-on server** |
| **Protocol registry** (approval / renewal / archive) | Drive JSON + browser registry tool (import/export) | Live registry never committed to git |
| **Standards / consensus checklists** | Same browser pack | Social science vs biomedical framing |
| **Code & decision history** | Shared GitHub repo | Public/shell only; no Confidential packets |
| **Full Django PRAMS** | Optional for Chris only if useful offline | **Not** the shared Jon+Chris deployment path |

## Credentials and trust (who controls passwords?)

**You do not need to be the password admin for CoB IRB reps.**

| Surface | Credential | Who controls the password |
|--------|------------|---------------------------|
| **Confidential packets / CITI** | Nicholls Google (SSO/MFA) | **Each person** (campus account — IT identity, not you) |
| **Who may open which Drive folders** | Drive sharing (Editor / Viewer) | **Data Owner** (you + CoB IRB practice) — access list, not passwords |
| **Static browser pack** (standards, checklist, registry UI) | None | N/A — trust = Public/Internal content + Drive for live registry JSON |
| **Live registry JSON** | Same as Drive | Whoever has Editor on that Drive folder |
| **Django PRAMS** (optional, Chris-only for now) | Local app account | Only if you run that app; self-serve change/reset needs working email — **do not promise this to CoB reps** as the shared path |

**Trust stack (security perspective for “mostly Chris + a few CoB IRB Editors”):**

1. **Confidentiality** — Drive ACLs + university MFA; proposals never in GitHub.  
2. **Integrity** — no-delete / `_archive/` + dated registry snapshots; GitHub for Public code/docs.  
3. **Accountability** — Drive access list + UPDATE_LOG / meeting notes (who changed what).  
4. **Least privilege** — Viewer vs Editor; per-protocol folders when you outgrow one shared root.  

CoB reps asked to “control their password”: answer **yes** for the shared path — they already control their **Nicholls Google** password. You control **who is on the Drive**, not their campus credentials. That is a viable, more honest security story than running a second password database you cannot support.

## Day-to-day (you and Jon)

1. Open the CoB IRB browser pack (bookmark GitHub Pages URL once published, or open from a Drive copy of the static `browser/` folder).
2. Use **standards / process / checklist** for review consensus.
3. **Registry:** Import `protocol_registry.json` from Drive → review renewal + CITI flags → Export dated snapshot back to Drive `_archive/` (no delete).
4. Click through to **Drive** for packets and CITI (root link + [CITI_Certificates](https://drive.google.com/drive/folders/1JTJadjcEZEkOQwjSvsTkz2PcbOzqNFKi) + per-protocol folders as you grow them).
5. Use **GitHub Issues / PRs** for tooling decisions and feature requests (synthetic examples only in issues).
6. Keep Confidential out of consumer AI prompts (JML 25-109 §6; Nicholls Confidential default).

### Renewal check (Jon)

| Color | Meaning | Action |
|-------|---------|--------|
| **Green** | Renewal due &gt;30 days out | No action |
| **Yellow** | Due within 30 days | Clock is ticking — start continuing-review packet; use Copy PI reminder |
| **Red** | Overdue | Treat as not protected; pause continuing activity until renewed |

Registry cards and the top **Needs renewal** list use these bands. Set renewal = approval + 1 year when the letter says a 12-month period.

### CITI check (Jon) — investigators on a project

Django only knows the logged-in PI’s uploaded cert. For CoB shared work, use the **browser registry**:

1. Open registry → **Open CITI folder** (Drive).
2. For each protocol, list investigators (`pi` / `co_i`).
3. Confirm the PDF is in Drive → set **CITI on Drive** = yes; enter **expiration** from the certificate (human read — no auto-OCR).
4. Flags: green valid; yellow expiring ≤30 days; red missing, expired, or not on Drive.
5. Click **CITI recheck** for the checklist, then export registry back to Drive.

See [STANDARDS_AUDIT.md](STANDARDS_AUDIT.md) for GitHub vs Drive boundaries.

## Is this “shadow IT”?

**Nuance — classify by what touches Confidential data.**

| Practice | Shadow-IT risk | Framing |
|----------|----------------|---------|
| Materials on **Nicholls Google Drive** with university accounts | **Low** | Using an IT-provided system as Data Owner |
| Opening **Public/Internal HTML** from GitHub or a Drive copy of the static pack | **Low–moderate** | Like a shared handbook/checklist; no new campus SaaS; document Data Owner workflow |
| Shared **GitHub** for code + synthetic fixtures | **Low** if scrubbed | Already the public shell model |
| Hosting Confidential packets or live registries **in GitHub** | **High** | Don’t |
| Standing up **unapproved cloud SaaS** that stores IRB/student data | **High** (classic shadow IT) | Don’t without IT path |
| Installing **Antigravity** (or similar AI IDE) and feeding it protocols/CITI/Drive exports | **Higher** | Third-party AI on Confidential ≈ shadow AI + EO/policy risk unless IT-approved enterprise path |
| Embedding a full IRB app in **Canvas** | **Mixed** | Canvas is IT-managed, but IRB admin ≠ course tooling; LTI/external tools often need IT; mixes teaching FERPA space with research ops |

**Practical answer:** Drive + static browser pack + scrubbed GitHub is the *least* shadow-IT-looking option that still avoids “please approve our SaaS.” Antigravity as the place Confidential IRB work happens is the piece most likely to be called out. Prefer Antigravity/Cursor only for **code/docs on Public/synthetic** content—not for pasting packets.

## Canvas?

Possible as a **link hub** (module page with links to Drive + browser pack), not as the system of record.

- **Good:** One Canvas page Jon and you bookmark: “Open Drive,” “Open IRB pack,” “GitHub repo.”
- **Poor fit:** Rebuilding PRAMS inside Canvas; storing packets as course files; LTI that needs IT approval to feel “official.”

If you use Canvas, keep it as **navigation only**; files stay on Drive.

## Antigravity for Jon?

You *can* ask Jon to install an AI coding tool to help **develop** the static pack—but that is optional and separate from *using* the IRB tool.

- **To use the IRB tool:** he needs a browser + Drive access only.
- **To develop features with you:** shared GitHub; AI tools on synthetic/Public only.
- Do **not** make Antigravity the runtime for Confidential registry/packets.

## What we stop recommending

- Shared Django `runserver` / always-on local server as the Jon+Chris path  
- IT-approved bayoupal redeploy as a near-term dependency  
- Cloud hosts that look like unapproved SaaS for Confidential data  

## Next build steps (aligned to this model)

1. Publish `docs/cob-irb-consensus/browser/` to **GitHub Pages** (or keep a zipped copy in Drive for offline open).  
2. Put a one-page “start here” in Drive root linking to Pages + registry empty file + no-delete rule.  
3. Optional Canvas module = same three links.  
4. Keep Django PRAMS Drive buttons + `irb_expiration` badges as a **Chris-side convenience** only until/unless a non-server path replaces them.

See also: [PRAMS_GITHUB_GDRIVE_PLAN.md](PRAMS_GITHUB_GDRIVE_PLAN.md), [NO_DELETE_RETENTION.md](NO_DELETE_RETENTION.md), [STANDARDS_AUDIT.md](STANDARDS_AUDIT.md), [browser/](browser/).
