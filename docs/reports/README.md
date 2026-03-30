<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<NEEDS_VERIFICATION_UUID>
title: reports
type: standard
version: v1
status: draft
owners: @bartytime4life
created: 2026-02-14
updated: 2026-03-16
policy_label: public
related: [docs/reports/readme-structure-reconciliation.md, ../README.md, ../governance/, ../standards/, ../runbooks/, ../../data/, ../../contracts/, ../../schemas/, ../../policy/, ../../tests/, ../../.github/workflows/README.md]
tags: [kfm, docs, reports, governance]
notes: [Owner is grounded in the current public CODEOWNERS fallback for /docs/; created date reflects the current file lineage after a visible delete/recreate cycle and should be rechecked if the project prefers first-ever path appearance instead.]
[/KFM_META_BLOCK_V2] -->

# reports

Governed index for human-readable report artifacts, review-facing summaries, and report-adjacent evidence surfaces in Kansas Frontier Matrix (KFM).

> **Status:** experimental  
> **Doc status:** draft  
> **Owners:** `@bartytime4life` via current public `/.github/CODEOWNERS` fallback for `/docs/`  
> ![Status](https://img.shields.io/badge/status-experimental-orange)
> ![Doc](https://img.shields.io/badge/doc-draft-lightgrey)
> ![Scope](https://img.shields.io/badge/scope-docs%2Freports-blue)
> ![Trust](https://img.shields.io/badge/trust-governed%20surface-6f42c1)
> ![Evidence](https://img.shields.io/badge/evidence-current%20public%20main-success)
> ![Owner](https://img.shields.io/badge/owner-bartytime4life-181717)  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Current verified snapshot](#current-verified-snapshot) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Reference tables](#reference-tables) · [Task list](#task-list) · [FAQ](#faq) · [Appendix](#appendix)

> [!IMPORTANT]
> `docs/reports/` is a governed documentation surface, not a bypass around contracts, policy, release manifests, proof packs, or governed APIs. Reports may explain, summarize, validate, review, or contextualize released scope, but they do **not** create new authoritative truth on their own.

**Status markers used in this README:** **CONFIRMED** · **INFERRED** · **PROPOSED** · **UNKNOWN** · **NEEDS VERIFICATION**

## Scope

`docs/reports/` is the documentation-facing home for report-shaped artifacts meant to be read, reviewed, and navigated by humans.

In KFM terms, this directory is for materials such as:

- report indexes and landing pages
- validation or self-validation summaries intended for documentation surfaces
- release-facing, correction-facing, or review-facing human summaries
- report-adjacent figures, tables, or lightweight visuals that are safe to publish in docs
- narrative/report surfaces that remain explicitly downstream of release scope, evidence, policy, and review state

This directory should **not** become a shadow data lake, schema registry, policy bundle store, workflow engine, or second truth path.

## Repo fit

| Field | Value |
|---|---|
| Path | `docs/reports/README.md` |
| Local role | Directory contract and navigation index for report-shaped documentation under `docs/` |
| Upstream links | [`../README.md`](../README.md) · [`../governance/`](../governance/) · [`../standards/`](../standards/) · [`../runbooks/`](../runbooks/) |
| Adjacent governed boundaries | [`../../data/`](../../data/) · [`../../schemas/`](../../schemas/) · [`../../contracts/`](../../contracts/) · [`../../policy/`](../../policy/) · [`../../tests/`](../../tests/) |
| Workflow-scaffolding context | [`../../.github/workflows/README.md`](../../.github/workflows/README.md) |
| Related report evidence | [`readme-structure-reconciliation.md`](./readme-structure-reconciliation.md) is a known structural reconciliation artifact and should be treated cautiously if it outruns retrievable repo reality |
| Core rule | Reports stay **downstream** of governed release scope and preserve drill-through to evidence, release state, caveat state, and correction context |

## Accepted inputs

| Input type | Belongs here? | Notes |
|---|---|---|
| Human-readable report indexes and landing pages | Yes | Best fit for directory contracts, report family indexes, and reader-facing navigation |
| Validation / QA summaries meant for docs consumption | Yes | Keep them report-shaped and traceable back to validators, run receipts, or release scope |
| Release-facing or correction-facing human summaries | Yes | Must point back to release, proof-pack, correction, supersession, or rollback context |
| Review-facing stewardship summaries | Yes | Keep review state, limits, and obligations visible |
| Report-adjacent figures, diagrams, or compact tables | Yes, selectively | Must be public-safe, provenance-aware, and sized for docs rather than data delivery |
| Small machine-readable rollups used only as report companions | Sometimes | Allowed only when clearly derivative and explicitly non-authoritative |

## Exclusions

| Does **not** belong here | Put it here instead | Why |
|---|---|---|
| Canonical raw / work / processed / catalog data | [`../../data/`](../../data/) | Reports are documentation surfaces, not canonical data stores |
| Schemas, contract definitions, API envelopes | [`../../schemas/`](../../schemas/) · [`../../contracts/`](../../contracts/) | Machine-checked interfaces belong in contract-bearing locations |
| Policy bundles, reason-code registries, enforcement rules | [`../../policy/`](../../policy/) | Policy must remain explicit and enforceable outside report prose |
| Tests, fixtures, validation harnesses, workflow logic | [`../../tests/`](../../tests/) and execution surfaces | Reports may summarize tests, but they do not replace them |
| Secrets, tokens, signed URLs, internal endpoints | Not in docs | These are never acceptable report payloads |
| Precise restricted coordinates or other sensitive location detail | Governed redaction/generalization path | Reports must preserve policy-safe visibility |
| Free-form AI narrative without evidence linkage | Not here | KFM report surfaces remain evidence-linked and bounded |

## Current verified snapshot

| Path / signal | Status | Notes |
|---|---|---|
| `docs/reports/README.md` | **CONFIRMED** | Present on current public `main` as the directory contract for this lane |
| `docs/reports/readme-structure-reconciliation.md` | **CONFIRMED** | Present on current public `main`; the document itself warns that it records structural alignment, not functional completeness |
| First-level child lanes `audits/`, `releases/`, `self-validation/`, `story_nodes/`, `telemetry/`, and `validation/` | **CONFIRMED** | Visible in the current public `main` listing for `docs/reports/`; deeper contents were not re-enumerated in this README |
| `daily/` | **PROPOSED** | Not visible in the current public `main` listing; add only if a recurring report family truly materializes |
| Report-specific automation / CI | **UNKNOWN** | Workflow documentation exists, but this README does not verify report-specific merge or publish gates |

> [!NOTE]
> The snapshot above is grounded in the current public `main` listing for `docs/reports/`. Path presence should **not** be read as proof of implemented behavior, populated child inventories, or active automation.

## Directory tree

### Current public `main` snapshot

```text
docs/reports/
├── audits/
├── releases/
├── self-validation/
├── story_nodes/
├── telemetry/
├── validation/
├── README.md
└── readme-structure-reconciliation.md
```

<details>
<summary><strong>Interpretation notes and restrained future additions</strong></summary>

- The first-level lanes above are **CONFIRMED** as visible paths on current public `main`.
- Their presence does **not** by itself prove completed family inventories, active automation, or review-ready behavioral depth.
- `daily/` is **not** visible in the current public snapshot. Keep it **PROPOSED** unless a recurring report family actually materializes.
- When a reconciliation note and the live repo listing disagree, verified inventory wins.
- New top-level families should be rare. The default bias is to keep this directory small, legible, and intentionally governed.

</details>

## Quickstart

```bash
# inspect the directory contract
sed -n '1,260p' docs/reports/README.md

# inspect the related reconciliation note
sed -n '1,260p' docs/reports/readme-structure-reconciliation.md

# verify current owner coverage
sed -n '1,200p' .github/CODEOWNERS

# list first-level report lanes and files
find docs/reports -maxdepth 1 -mindepth 1 | sort

# inspect workflow-scaffolding claims before assuming automation exists
sed -n '1,260p' .github/workflows/README.md

# find report content that claims evidence or release linkage
rg -n "EvidenceBundle|EvidenceRef|ReleaseManifest|ProofPack|CorrectionNotice|ValidationReport|reports/" docs/reports docs
```

## Usage

### Add a report without creating a new truth path

1. Start from an already governed scope: a released dataset, a proof-backed release, a validation run, a correction event, or another inspectable source of truth.
2. Make the report’s **time basis**, **release basis**, and **evidence route** explicit.
3. Keep modeled, generalized, partial, stale, withdrawn, or correction-pending states visible rather than smoothing them away.
4. Put the authoritative machine-readable object somewhere else when that object already has a canonical home.
5. Update this README if the addition introduces a stable new report family rather than a one-off file.
6. Prefer a verified inventory update over prose that implies child families or automation that are not yet actually present on the branch you are editing.

### Recommended minimum trust block inside any consequential report

```md
> **Scope:** published / review / draft
> **Time basis:** valid time / as-of time / publication time / correction time
> **Release basis:** release ID, manifest, or proof-pack reference
> **Evidence route:** EvidenceRef / EvidenceBundle / validation report / source descriptor / correction notice
> **Sensitivity posture:** public-safe / generalized / restricted / withheld
> **Derived status:** observed / documentary / modeled / summarized / AI-assisted
```

That block is not a substitute for real contracts. It is a reader-facing reminder that reports are downstream of governed evidence and release state.

### Add a new top-level report family only when all of the following are true

- the family will hold multiple files over time
- the family has a stable reader need and a stable trust contract
- the content cannot live more clearly under an existing child family
- the new family does not duplicate `data/`, `schemas/`, `contracts/`, `policy/`, or `tests/`
- the family is not already present in the current branch inventory
- this README is updated in the same change

## Diagram

```mermaid
flowchart TD
    A[(Canonical source / policy / contracts)] --> B[Governed ingest + validation]
    B --> C[Promoted release scope]
    C --> D[Evidence + release objects]
    D --> E[docs/reports/]
    E --> F[Human-readable report surfaces]
    F --> G[Reader drill-through]
    G --> D

    H[Correction / rollback / supersession] --> C
    I[Derived figures / summaries] --> E

    classDef core fill:#eef6ff,stroke:#5b8def,stroke-width:1px;
    classDef reports fill:#f8f5ff,stroke:#8a63d2,stroke-width:1px;
    class A,B,C,D,H core;
    class E,F,G,I reports;
```

## Reference tables

### Current public first-level lanes

| Lane | Current public visibility | Review note |
|---|---|---|
| [`audits/`](./audits/) | Present | Path presence is confirmed; functional completeness is not implied |
| [`releases/`](./releases/) | Present | Path presence is confirmed; treat it as a report-family lane rather than a release authority store |
| [`self-validation/`](./self-validation/) | Present | Path presence is confirmed; keep docs-facing validation summaries downstream of canonical validators |
| [`story_nodes/`](./story_nodes/) | Present | Path presence is confirmed; deeper Story Node inventory is outside this README’s current verified scope |
| [`telemetry/`](./telemetry/) | Present | Path presence is confirmed; any rollups here should remain public-safe and derivative |
| [`validation/`](./validation/) | Present | Path presence is confirmed; report summaries must still point back to authoritative validation objects |
| `daily/` | Not present on current public `main` | Keep **PROPOSED** until a recurring report family is real |

### Report classes at a glance

| Report class | Primary use | Minimum linkage | Must **not** do |
|---|---|---|---|
| Narrative / explainer report | Human-readable interpretation of released scope | Time basis + release scope + evidence route + caveat state | Invent unsupported claims or detach narrative from evidence |
| Validation / QA summary | Explain what was checked and what passed/failed | Validation report, run receipt, checksums, or equivalent | Quietly replace authoritative validation artifacts |
| Release / correction summary | Explain what changed, why, and how it propagates | `ReleaseManifest`, proof-pack, correction or rollback context | Pretend release or correction happened without evidence-bearing objects |
| Review / stewardship summary | Capture policy or review context in human-readable form | Decision path, obligations, sensitivity posture, approval/correction context | Bypass formal review objects or hide restrictions |

### Minimum trust cues for any consequential report

| Cue | Why it matters | Example |
|---|---|---|
| Time basis | Prevents hidden temporal collapse | “As-of 2026-03-14 release scope” |
| Release basis | Keeps reports downstream of governed publication | `rel.kansas.water.2026-03-14` |
| Evidence route | Preserves drill-through | `EvidenceBundle`, validation report, or correction notice |
| Policy / sensitivity note | Makes withholding and generalization visible | “Generalized”, “public-safe”, “withheld” |
| Derived / modeled marker | Prevents reports from masquerading as direct observation | “Modeled”, “summarized”, “AI-assisted”, “documentary” |
| Correction path | Keeps truth reversible and inspectable | superseded-by / withdrawn / correction-pending |

### State cues worth preserving

| State | Reader-facing meaning | Typical consequence |
|---|---|---|
| Draft | Not yet publication-stable | Keep caveats and review needs explicit |
| Review | Under active stewardship or quality check | Link to validator, reviewer, or decision context |
| Published | Intended for normal downstream consumption | Preserve release basis and correction path |
| Superseded | Newer authoritative scope exists | Point to replacement |
| Withdrawn | No longer safe or valid for use | Keep reason visible |
| Correction-pending | Known issue exists but replacement is not complete | Avoid false finality |

## Task list

- [ ] The file states what belongs here and what does not.
- [ ] Current public snapshot and directory tree stay synchronized with the branch being documented.
- [ ] Reports are kept downstream of governed release scope rather than acting as source-of-truth stores.
- [ ] Every consequential report shows a time basis and evidence route.
- [ ] Sensitive locations, secrets, tokens, and signed URLs are excluded.
- [ ] Generalized / withheld / stale / correction states are visible where relevant.
- [ ] New top-level report families update this index in the same change.
- [ ] This README distinguishes visible path presence from functional completeness or active automation.
- [ ] Reconciliation prose does not outrun the verified inventory.
- [ ] Links, code fences, and Mermaid all render cleanly.
- [ ] Any machine-readable companion is clearly derivative and points back to the authoritative object.

## FAQ

### Are reports authoritative in KFM?

No. Reports are governed documentation surfaces. Authoritative truth still lives in the governed evidence path, contract layer, policy layer, release layer, and evidence-resolution path.

### Can reports include AI-assisted material?

Yes, but only when it remains explicitly downstream of admissible scope, evidence linkage, and policy-safe release state. A report must not let AI prose become a second truth path.

### Where should Story Nodes live?

The current public `main` tree shows `docs/reports/story_nodes/` as a first-level child of `docs/reports/`. That confirms the lane exists at path level. Deeper Story Node inventory, conventions, and behavioral claims should still be verified from the working branch before this README says more than path presence.

### Can this directory hold large exports or raw dumps?

No. Large or canonical payloads belong in governed data locations. Reports may reference them, summarize them, or render small public-safe derivatives, but they should not absorb them.

### Does this README replace the older reconciliation note?

This file is the current directory contract on public `main`. `readme-structure-reconciliation.md` remains useful as a structural/scaffold report, but it should not outrank verified live inventory or this README’s direct directory contract.

## Appendix

<details>
<summary><strong>Directory rules worth keeping explicit</strong></summary>

### Keep `docs/reports/` small

This directory should grow by **clear family** and **clear reader need**, not by drift.

### Prefer one canonical home per subsystem

If something is primarily a dataset, schema, policy bundle, test harness, or deployment artifact, its canonical home is elsewhere even when a report references it.

### Reports should be inspection-friendly

A report should help a reader answer:

- What am I looking at?
- What scope and time basis apply?
- What evidence or release supports this?
- What caveats, generalizations, or policy states apply?
- How would correction or supersession be communicated?

### Strong non-goals for this directory

- not a second catalog system
- not a contract registry
- not a policy bundle store
- not a raw evidence dump
- not a place to hide unverified implementation claims

### Verification discipline

When the mounted repo, the current public branch listing, and a planning or reconciliation document disagree, prefer:

1. directly retrievable repo inventory
2. current authoritative directory contract
3. older reconciliation prose

That ordering keeps report navigation trustworthy.

</details>

[Back to top](#reports)
