<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/656e8d6e-0e66-4802-99b8-ee963673cd08
title: docs/investigations/README.md
type: standard
version: v2
status: draft
owners: TBD
created: 2026-02-24
updated: 2026-03-01
policy_label: public
related: []
tags: [kfm, investigations]
notes:
  - Directory contract for investigation artifacts (spikes, research notes, experiments).
  - This folder is *not* a decision record; promote outcomes to an ADR/policy/spec when needed.
  - Directory layout expanded to include indexing, templates, run receipts, and evidence bundle scaffolding.
[/KFM_META_BLOCK_V2] -->

# docs/investigations
Short-lived research notes and reproducible experiments that reduce uncertainty *before* we change governed interfaces, pipelines, or narratives.

![Status](https://img.shields.io/badge/status-draft-yellow)
![Policy](https://img.shields.io/badge/policy-public-brightgreen)
![Scope](https://img.shields.io/badge/scope-investigations-blue)
![Traceability](https://img.shields.io/badge/traceability-required-orange)
![Lifecycle](https://img.shields.io/badge/lifecycle-pre--decision-lightgrey)

> **NOTE**
> This directory is for *learning + de-risking* work. Anything that changes behavior (data promotion, APIs, UI narratives, access rules) must be **promoted** to the appropriate governed artifact (ADR/policy/spec) before shipping.

## Quick navigation
- [Where this fits in the repo](#where-this-fits-in-the-repo)
- [What belongs here](#what-belongs-here)
- [What must NOT go here](#what-must-not-go-here)
- [Directory layout](#directory-layout)
  - [Top-level layout](#top-level-layout)
  - [Per-investigation layout](#per-investigation-layout)
  - [Folder semantics table](#folder-semantics-table)
- [Naming and lifecycle](#naming-and-lifecycle)
- [Reproducibility contract](#reproducibility-contract)
- [Investigation template](#investigation-template)
- [Promotion path](#promotion-path)
- [Safety and governance](#safety-and-governance)
- [FAQ](#faq)

---

## Where this fits in the repo
`docs/investigations/` sits **upstream** of decisions and implementations:

```mermaid
flowchart LR
  Q[Question or risk] --> I[Investigation record]
  I --> E[Evidence and experiments]
  E --> F[Findings]
  F --> D[Decision needed]
  D --> P[Promote outcome]
  P --> ADR[ADR or policy/spec]
  P --> PR[Implementation PR and tests]
```

### Primary outcomes
An investigation should produce at least one of:
- A **reproducible** experiment (commands, inputs, outputs, environment)
- A **bounded** recommendation with assumptions/risks/tradeoffs
- A **decision request** (what decision is needed, by whom, by when)
- A **promotion target** (where this result must land if acted upon)

---

## What belongs here
Acceptable inputs for `docs/investigations/` include:

- **Spikes / feasibility checks**  
  “Can we do X with our constraints?” “What breaks if we do Y?”

- **Comparative evaluations**  
  e.g., library/tool options, schema approaches, indexing strategies, map rendering approaches.

- **Reproduction notes**  
  How to reproduce a bug, perf regression, validation failure, or data anomaly.

- **Evidence-bound explorations**  
  Small studies that support or refute a claim *without* asserting it as a shipped truth.

- **Prototypes with clear scope**  
  Proof-of-concepts explicitly labeled as non-production.

- **Threat modeling / risk discovery**  
  What could go wrong; what controls/gates we need; what to test.

---

## What must NOT go here
Exclusions (default-deny):

- **Final decisions**  
  Use an ADR / decision log / policy doc (path varies by repo — link it here once known).

- **Production-facing user narratives**  
  Anything that will be shown in UI/story mode must be promoted to a governed story/spec.

- **Secrets or sensitive credentials**  
  No API keys, tokens, internal URLs with credentials, private keys, or customer data.

- **Vulnerable location targeting**  
  No precise coordinates or step-by-step instructions that could increase harm. Use coarse geography and mark “needs governance review”.

- **Unlicensed datasets / unclear provenance**  
  If the source/license is unknown, do not promote beyond this folder; flag for governance review.

---

## Directory layout
The goal of this layout is: **discoverable + reproducible + promotion-ready** without forcing every investigation to be heavyweight.

> **TIP**
> Create only what you need, but when an investigation produces *evidence artifacts* (plots/tables/derived files), prefer the “full” layout so promotion is straightforward.

### Top-level layout
```text
docs/investigations/                                  # Pre-decision research + experiments (bounded, auditable)
├─ README.md                                          # This file (directory contract)
│
├─ INDEX.md                                           # Optional: human-friendly list of investigations
├─ index.yml                                          # Optional: machine index (status/tags/links)
│
├─ _templates/                                        # Starters aligned with KFM practices (copy/paste)
│  ├─ investigation.README.template.md                # Investigation record template
│  ├─ status.template.yml                             # Investigation status/metadata template
│  ├─ run-receipt.template.json                       # Run receipt skeleton (for experiments)
│  ├─ evidence-bundle.template.json                   # EvidenceBundle skeleton (if artifacts become citeable)
│  └─ promotion-packet.template.md                    # “promotion checklist + links” starter
│
├─ _shared/                                           # Optional shared helpers for investigations
│  ├─ scripts/                                        # Tiny helper scripts (safe; no secrets)
│  ├─ env/                                            # Shared environment notes (tool versions, base images)
│  └─ assets/                                         # Reusable diagrams/images used across investigations
│
├─ 2026/                                              # Optional year partition (recommended once > ~20 items)
│  ├─ 2026-02-24_short-slug/                           # Investigation folder (date + slug)
│  └─ 2026-03-01_another-slug/
│
└─ _archive/                                          # Optional: closed/superseded investigations (no longer active)
   └─ 2025/...
```

### Per-investigation layout
One investigation = one folder. Keep the top-level `README.md` readable; push scratch into `appendix/`.

```text
docs/investigations/YYYY/YYYY-MM-DD_short-slug/
├─ README.md                                          # Canonical record (question → method → findings → recommendation)
├─ status.yml                                         # Lightweight metadata (owners, status, links, policy label)
│
├─ plan/                                              # Optional: pre-work planning (helps time-boxing)
│  ├─ question.md                                     # Exact question + decision it informs
│  ├─ hypotheses.md                                   # Testable hypotheses / expected outcomes
│  └─ method.md                                       # Planned method (what will be done, what counts as “done”)
│
├─ inputs/                                            # What was used (pointers first, samples when needed)
│  ├─ sources.yml                                     # Source list (URLs/paths), versions, licenses, hashes (if available)
│  ├─ samples/                                        # Small excerpts only (never full sensitive datasets)
│  └─ checksums.txt                                   # Optional: digests for any local sample artifacts
│
├─ env/                                               # Repro environment (prefer lockfiles + container digest)
│  ├─ README.md                                       # How to run (OS, toolchain, prerequisites)
│  ├─ container/                                      # Optional: containerized repro
│  │  ├─ Dockerfile
│  │  └─ image.digest                                 # Recorded container digest (if built/pulled)
│  ├─ requirements.txt / poetry.lock / package-lock.json
│  └─ tool-versions.txt                               # Optional: pinned versions (python/node/gdal/proj/etc.)
│
├─ code/                                              # Minimal repro code only (no production code here)
│  ├─ README.md                                       # How to run scripts/notebooks
│  ├─ scripts/                                        # CLI scripts used for repro
│  └─ notebooks/                                      # Notebooks (keep deterministic; avoid hidden state)
│
├─ runs/                                              # Per-run working folders (optional but recommended)
│  ├─ 2026-03-01T120000Z_run-01/                       # Each run is time-stamped
│  │  ├─ command.txt                                  # Exact command(s) invoked
│  │  ├─ stdout.log / stderr.log
│  │  └─ notes.md                                     # Deviations from plan; anomalies
│  └─ ...
│
├─ receipts/                                          # Run receipts (structured provenance; promotes cleanly later)
│  ├─ run_2026-03-01T120000Z.abcd.json                 # See run-receipt template
│  └─ ...
│
├─ qa/                                                # Validation outputs (if you validated anything)
│  ├─ report_2026-03-01T120000Z.abcd.json              # Machine-readable summary if possible
│  └─ notes.md                                        # Human interpretation of QA results
│
├─ outputs/                                           # Results (small + reviewable)
│  ├─ figures/                                        # PNG/SVG charts (small)
│  ├─ tables/                                         # CSV/MD tables (small)
│  └─ excerpts/                                       # Small text excerpts (redacted if needed)
│
├─ evidence/                                          # Only if outputs might become citeable evidence
│  ├─ evidence_refs.md                                # Human list of candidate EvidenceRefs
│  ├─ bundles/                                        # EvidenceBundle JSON (immutable-by-digest if used)
│  └─ rights.md                                       # Rights/attribution notes for media
│
├─ promotion/                                         # “Handoff packet” if we act on this investigation
│  ├─ decision_request.md                             # What decision is needed + options
│  ├─ promotion_checklist.md                           # Minimal gates to satisfy (links to artifacts)
│  └─ links.md                                        # PR/ADR/spec links once created
│
└─ appendix/                                          # Scratch notes that should not distract from the top record
   ├─ scratch.md
   └─ misc/
```

> **WARNING**
> If anything in `outputs/` or `evidence/` includes sensitive location info, **generalize** it and mark “needs governance review”. Do not put precise coordinates here.

### Folder semantics table

| Path | Required | What goes here | What must NOT go here |
|---|---:|---|---|
| `README.md` | ✅ | The canonical write-up + links | Final decisions (ADR/policy/spec), secrets |
| `status.yml` | ✅ (recommended) | Owners, status, links, policy label, next decision | Sensitive content; credentials |
| `plan/` | ⬜ | Hypotheses, method, DoD | Results (those go in `outputs/`) |
| `inputs/` | ⬜ | Source pointers, tiny samples, hashes | Full datasets; unlicensed exports |
| `env/` | ⬜ | Lockfiles, container digest, tool versions | Hidden “it works on my machine” assumptions |
| `code/` | ⬜ | Minimal repro scripts/notebooks | Production code; secrets |
| `runs/` | ⬜ | Run-by-run logs + commands | Credentials; large raw outputs |
| `receipts/` | ⬜ (recommended if code runs) | Structured run receipts | Ad-hoc notes only (put those in `runs/`) |
| `qa/` | ⬜ | QA reports + interpretation | Unvalidated claims presented as truth |
| `outputs/` | ⬜ | Charts/tables/excerpts (small) | Huge binaries; sensitive raw dumps |
| `evidence/` | ⬜ | Candidate EvidenceRefs + bundles for later promotion | Anything that cannot be rights-cleared |
| `promotion/` | ⬜ | Decision request + checklist + links to ADR/PR | The ADR itself (promote it out) |
| `appendix/` | ⬜ | Scratch | Anything that should be in the main README |

---

## Naming and lifecycle

### Folder naming
- Prefer: `YYYY-MM-DD_short-slug/`
- Slug: lowercase, hyphenated, short, descriptive.
- Optional partition: `YYYY/` folder to keep the root tidy.

### Status lifecycle
Recommended `status.yml` values:
- `active` (in progress)
- `paused` (blocked; list what’s missing)
- `done` (completed; may or may not be promoted)
- `promoted` (outcome landed in ADR/policy/spec/PR)
- `superseded` (replaced by a newer investigation)
- `archived` (kept for history; no longer relevant)

---

## Reproducibility contract
Every investigation should include enough detail to **re-run** or **audit**:

- **Inputs:** links/paths, versions, hashes when available  
- **Environment:** tool versions (runtime, OS/container, library versions)  
- **Steps:** commands or pseudocode sufficient to reproduce  
- **Outputs:** expected outputs + where to find them  
- **Conclusion:** what we learned + what we still don’t know  

> **TIP**
> If you can’t make it reproducible, make it *auditable*: record enough detail that someone else can re-run it later.

### When to add receipts + evidence bundles
- If you ran code or transformed data: add `receipts/` and record run metadata.
- If outputs might be cited later (Story Nodes / Focus Mode): add `evidence/` and make sure rights + provenance are captured.

---

## Investigation template

<details>
<summary><strong>Click to expand: Investigation README template</strong></summary>

```markdown
<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid>
title: docs/investigations/YYYY/YYYY-MM-DD_short-slug/README.md
type: standard
version: v1
status: draft
owners: <name/team>
created: YYYY-MM-DD
updated: YYYY-MM-DD
policy_label: public|restricted|...
related:
  - <link to issue/ticket>
  - <link to relevant ADR/policy/spec if it exists>
tags: [kfm, investigation]
notes:
  - One-line: what uncertainty this reduces
[/KFM_META_BLOCK_V2] -->

# <Investigation title>
One sentence: what we are trying to learn and why it matters.

## Question
- What is the exact question?
- What decision will this inform?

## Context
- Background, constraints, and why now.

## Assumptions
- List assumptions explicitly.
- Mark anything that needs verification.

## Method
- Steps taken, tools used, and what was measured.
- Include commands or pseudocode.
- Link to `env/` and `code/` if present.

## Evidence ledger
| Artifact | Source | Version / hash | Sensitivity | Notes |
|---|---|---|---|---|
| <file/link> | <origin> | <sha/version> | public|restricted|... | <why it matters> |

## Runs and receipts (if applicable)
- `runs/<run-folder>/...` for logs/commands
- `receipts/run_<run_id>.json` for structured provenance

## Findings
- Bullet findings with supporting evidence links.
- Be explicit about uncertainty.

## Risks and tradeoffs
- What could go wrong if we act on this?
- What do we lose by not acting?

## Recommendation
- Proposed next step(s)
- Minimum verification steps to convert Unknown → Confirmed

## Promotion target
If we act on this investigation, where does it land?
- [ ] ADR / decision record: <path/link>
- [ ] Spec / contract: <path/link>
- [ ] Policy / governance: <path/link>
- [ ] Implementation PR: <link>
- [ ] Test plan / gate update: <link>

## Open questions
- What remains unknown?
- What would change our mind?

## Appendix
- Extra charts, logs, scratch notes (or link to `appendix/`).
```

</details>

---

## Promotion path

### Promote when…
Promote an investigation outcome when it:
- Changes a **governed interface** (API, schema, contract)
- Changes **promotion gates** (RAW → WORK → PROCESSED → CATALOG/TRIPLET → PUBLISHED)
- Changes a **user-facing claim** (maps/stories/reporting)
- Changes **access control / redaction rules**
- Commits the team to a **new dependency** or architectural invariant

### Minimal promotion checklist
- [ ] Clear decision statement (“We will … because …”)
- [ ] Evidence links preserved (inputs/outputs/hashes if available)
- [ ] Risks/tradeoffs captured
- [ ] Tests or validation gates defined (or updated)
- [ ] Rollback plan is possible (or explicit exception documented)

> **NOTE**
> A promoted narrative (Story Node) must be citation-valid and policy-allowed. If citations cannot be verified, promotion should fail closed.

---

## Safety and governance
- Treat investigations as **default-deny** for sensitive content.
- If sensitivity is unclear: **redact/generalize** and mark “needs governance review”.
- Don’t bypass the trust membrane (clients → governed API → policy boundary → storage).
- Prefer **additive glue** (registries, indexes, ADRs, small diffs) over sweeping rewrites.

---

## FAQ

### Can investigations be messy?
Yes—*but bounded*. Put scratch notes in an Appendix, and keep the top sections readable.

### Where do big artifacts go?
Prefer links to durable storage and record hashes/versions here. Avoid committing huge binaries unless the repo explicitly allows it.

### Do I have to use the template?
No, but every investigation must still meet the reproducibility contract.

---

**Back to top:** [docs/investigations](#docsinvestigations)