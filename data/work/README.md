<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid-TBD-NEEDS-VERIFICATION>
title: data/work
type: standard
version: v1
status: draft
owners: @bartytime4life
created: 2026-03-22
updated: 2026-04-12
policy_label: <TBD-NEEDS-VERIFICATION>
related: [../README.md, ../raw/README.md, ../quarantine/README.md, ../processed/README.md, ../catalog/README.md, ../catalog/stac/README.md, ../catalog/dcat/README.md, ../catalog/prov/README.md, ../receipts/README.md, ../proofs/README.md, ../published/README.md, ../registry/README.md, ../../contracts/README.md, ../../schemas/README.md, ../../policy/README.md, ../../tests/README.md, ../../tools/README.md, ../../scripts/README.md, ../../.github/workflows/README.md, ../../.github/CODEOWNERS]
tags: [kfm, data, work, staging, provenance]
notes: [Current public main confirms a README-only lane at `data/work/`; `created` stays pinned to the current-file reintroduction date on 2026-03-22; `doc_id` and `policy_label` still need verification; proof-aware carryover notes in this revision are doctrinally supported but still branch-convention-sensitive.]
[/KFM_META_BLOCK_V2] -->

# `data/work`

Repeatable, non-public staging zone for governed intermediate transforms, validation artifacts, and promotion handoff material.

> **Status:** `active directory` · **Doc state:** `draft`  
> **Owners:** `@bartytime4life` *(current public `.github/CODEOWNERS` coverage for `/data/`)*  
> **Path:** `data/work/README.md`  
> **Current public tree:** `data/work/` contains `README.md` only on public `main`  
> **Repo fit:** parent [`../README.md`](../README.md) · upstream [`../raw/README.md`](../raw/README.md) · lateral [`../quarantine/README.md`](../quarantine/README.md) · downstream [`../processed/README.md`](../processed/README.md), [`../catalog/README.md`](../catalog/README.md), [`../receipts/README.md`](../receipts/README.md), [`../proofs/README.md`](../proofs/README.md), [`../published/README.md`](../published/README.md), [`../registry/README.md`](../registry/README.md) · shared controls [`../../contracts/README.md`](../../contracts/README.md), [`../../schemas/README.md`](../../schemas/README.md), [`../../policy/README.md`](../../policy/README.md), [`../../tests/README.md`](../../tests/README.md), [`../../tools/README.md`](../../tools/README.md), [`../../scripts/README.md`](../../scripts/README.md), [`../../.github/workflows/README.md`](../../.github/workflows/README.md), [`../../.github/CODEOWNERS`](../../.github/CODEOWNERS)  
> ![Status: active directory](https://img.shields.io/badge/status-active%20directory-0a7d5a)
> ![Doc: draft](https://img.shields.io/badge/doc-draft-8250df)
> ![Owners: @bartytime4life](https://img.shields.io/badge/owners-%40bartytime4life-0969da)
> ![Public tree: README only](https://img.shields.io/badge/public%20tree-README--only-lightgrey)
> ![Catalog: DCAT+STAC+PROV](https://img.shields.io/badge/catalog-DCAT%2BSTAC%2BPROV-5b4bdb)
> ![Trust: fail-closed](https://img.shields.io/badge/trust-fail--closed-d73a49)
>
> **Quick jump:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Reference tables](#reference-tables) · [Definition of done](#definition-of-done--promotion-gates) · [FAQ](#faq) · [Appendix](#appendix)

> [!IMPORTANT]
> `data/work/` is **not** a publication surface, **not** a canonical endpoint, and **not** a client-facing integration path. In KFM, public and role-limited access crosses the governed API, policy, and evidence boundary; normal UI and runtime surfaces must not read `data/work/` directly.

> [!NOTE]
> Current public `main` confirms the lane, not a populated working inventory. This README therefore separates the **CONFIRMED live tree** from a **PROPOSED working deepening** instead of treating starter structure as checked-in reality.

---

## Scope

`data/work/` sits in the governed KFM truth path between immutable intake and release-ready processed scope:

`Source edge -> RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG -> PUBLISHED`

Within that path, `data/work/` is the operational zone for **repeatable transformation, normalization, enrichment, QA staging, and handoff preparation** before outputs can support stable dataset-version identity, catalog closure, release evidence, or governed publication.

In KFM terms, material leaving this lane should do so through a **governed state transition**, not a convenience copy. `data/work/` reduces ambiguity; it does not declare outward truth.

### Evidence posture used in this README

| Label | Meaning here |
|---|---|
| **CONFIRMED** | Current public `main` proves that `data/work/` exists as a top-level `data/` zone and currently contains `README.md` only. Adjacent public READMEs also confirm neighboring lifecycle lanes. |
| **INFERRED** | A role or relationship follows strongly from confirmed sibling READMEs and KFM doctrine, but is not proven by a populated subtree inside `data/work/` itself. |
| **PROPOSED** | Starter run layout, filename conventions, and working patterns that fit the repo’s doctrine and adjacent docs but are not yet proven as checked-in branch reality. |
| **UNKNOWN** | Working-branch-only content, emitted artifact inventory, local helper commands, and automation beyond the current public tree. |
| **NEEDS VERIFICATION** | Any value that should be checked before merge or release, including final `doc_id`, `policy_label`, deeper subtree shape, local command wiring, and branch-local proof-object placement. |

### What this directory is for

- intermediate transforms and QA staging
- derivation, normalization, enrichment, reprojection, and generalization work
- reviewable handoff preparation before `data/processed/`
- work notes that keep transform decisions inspectable while context is fresh
- temporary, non-public run material that is still in-flight and not yet release-backed

### What this directory is not for

- direct public serving
- long-term narrative publication
- release manifests, proof packs, or outward catalog closure
- source registration or dataset identity records
- hiding blocked material that should be isolated in `data/quarantine/`
- turning convenient scratch into de facto published truth

[Back to top](#datawork)

---

## Repo fit

### Path and current public state

| Item | Current reading |
|---|---|
| **Path** | `data/work/README.md` |
| **Current public tree state** | `data/work/` currently shows `README.md` only |
| **Owner coverage** | `/data/` is assigned to `@bartytime4life` in the current public `.github/CODEOWNERS` file |
| **Parent surface** | [`../README.md`](../README.md) defines the wider `data/` lifecycle |
| **Lifecycle position** | between [`../raw/README.md`](../raw/README.md) and [`../processed/README.md`](../processed/README.md), with [`../quarantine/README.md`](../quarantine/README.md) as the fail-closed sibling lane |
| **Current public README history** | latest visible public-main update on `2026-04-01`; current-file reintroduction visible on `2026-03-22` after a `2026-03-21` deletion |
| **Why the history note matters** | it keeps the KFM meta block dates reviewable instead of implied |

### Adjacency and flow

| Direction | Surface | Why it matters here | Status |
|---|---|---|---|
| Upstream | [`../raw/README.md`](../raw/README.md) | Immutable, source-native intake for evidence-bearing inputs | **CONFIRMED** |
| Lateral | [`../quarantine/README.md`](../quarantine/README.md) | Explicit fail-closed lane for blocked, ambiguous, or review-held material | **CONFIRMED** |
| Downstream | [`../processed/README.md`](../processed/README.md) | Stable dataset versions and release-adjacent processed artifacts | **CONFIRMED** |
| Downstream | [`../catalog/README.md`](../catalog/README.md) | Catalog-closure parent for outward `DCAT + STAC + PROV` metadata | **CONFIRMED** |
| Downstream | [`../catalog/stac/README.md`](../catalog/stac/README.md) | Spatial and temporal asset discovery | **CONFIRMED** |
| Downstream | [`../catalog/dcat/README.md`](../catalog/dcat/README.md) | Dataset and distribution discovery | **CONFIRMED** |
| Downstream | [`../catalog/prov/README.md`](../catalog/prov/README.md) | Catalog-facing lineage and provenance bundles | **CONFIRMED** |
| Adjacent process memory | [`../receipts/README.md`](../receipts/README.md) | Central receipt placement for run memory, validation context, and replay/audit support | **CONFIRMED** |
| Adjacent release evidence | [`../proofs/README.md`](../proofs/README.md) | Release manifests, proof packs, attestations, and rollback/correction evidence | **CONFIRMED** |
| Adjacent publication state | [`../published/README.md`](../published/README.md) | Optional materialized surface for already release-backed scope | **CONFIRMED** |
| Adjacent registration | [`../registry/README.md`](../registry/README.md) | Source admission, dataset identity, and onboarding guidance | **CONFIRMED** |
| Shared controls | [`../../contracts/README.md`](../../contracts/README.md) · [`../../schemas/README.md`](../../schemas/README.md) · [`../../policy/README.md`](../../policy/README.md) · [`../../tests/README.md`](../../tests/README.md) · [`../../tools/README.md`](../../tools/README.md) · [`../../scripts/README.md`](../../scripts/README.md) · [`../../.github/workflows/README.md`](../../.github/workflows/README.md) · [`../../.github/CODEOWNERS`](../../.github/CODEOWNERS) | Contract surfaces, schema-home boundary, policy posture, validation, helper lanes, workflow control, and review ownership | **CONFIRMED public surfaces** |

### Upstream / downstream rule of thumb

- Admit source-native material from `data/raw/`.
- Keep active, repeatable transform work in `data/work/`.
- Move blocked or unclear material into `data/quarantine/`.
- Hand off stable outputs to `data/processed/`.
- Keep catalog closure in `data/catalog/`.
- Keep process memory and release proof adjacent, not buried inside working payload folders.
- Reach `data/published/` only through a governed, release-backed state transition.

[Back to top](#datawork)

---

## Accepted inputs

The following belong here when they are part of a **repeatable, reviewable, non-public** transformation path.

### Confirmed fit

- normalized tabular or spatial intermediates
- reprojected or schema-aligned vector/raster working outputs
- enrichment outputs that still need review or downstream stabilization
- QA staging products, samples, and validation-side artifacts
- redaction or generalization candidates before processed release
- run-local notes that explain non-obvious transform decisions

### Proposed starter artifacts

Use these as **starter patterns**, not as already-proven branch conventions:

- `run_record.json`
- `run_manifest.json`
- `validation_report.json`
- `checksums.txt`
- `NOTES.md`
- `spec_hash.txt`
- small `manifests/`, `qa/`, and `logs/` subfolders inside a run area

### Proposed proof-aware carryovers

April 2026 KFM doctrine deepening makes a small proof quartet increasingly important: `spec_hash`, `run_receipt`, `ai_receipt`, and attestation references. For `data/work/`, treat those as **PROPOSED carryovers**, not as confirmed local naming or placement standards.

That means:

- a local `spec_hash` file or reference can be a good fit when it helps replay or explain the work
- `run_receipt` or `ai_receipt` artifacts may appear here only when the active branch confirms that convention
- attestation references or bundle pointers should stay explicit if they exist, but they do **not** turn `data/work/` into a release-proof lane
- centrally queryable receipts still belong in [`../receipts/README.md`](../receipts/README.md), and release-significant proof still belongs in [`../proofs/README.md`](../proofs/README.md)

### Good-fit test

An artifact likely belongs in `data/work/` if all six checks pass:

1. It derives from admitted or reviewable upstream material.
2. It is needed to transform, normalize, enrich, validate, or prepare a handoff.
3. It remains reproducible enough to replay or explain.
4. It is **not yet** the stable processed release artifact.
5. It should **not** be read directly by normal client or runtime surfaces.
6. If it carries proof-aware context such as `spec_hash`, `run_receipt`, `ai_receipt`, or attestation references, that context is still clearly pre-release and not being mistaken for outward proof.

[Back to top](#datawork)

---

## Exclusions

| Excluded content | Why it does not belong here | Put it here instead |
|---|---|---|
| Immutable upstream captures | Intake must stay source-native and append-friendly | [`../raw/README.md`](../raw/README.md) |
| Blocked, ambiguous, or review-held material | Work is not the fail-closed holding lane | [`../quarantine/README.md`](../quarantine/README.md) |
| Canonical processed artifacts | `data/work/` is pre-release staging, not the stable processed zone | [`../processed/README.md`](../processed/README.md) |
| STAC / DCAT / PROV closure files | Outward discovery and lineage belong downstream of processed handoff | [`../catalog/README.md`](../catalog/README.md) |
| Central run receipts that must stay queryable across runs | Process memory should remain easy to resolve during replay, correction, and audit | [`../receipts/README.md`](../receipts/README.md) |
| Release manifests, proof packs, attestations, rollback evidence | Release proof is a separate trust surface | [`../proofs/README.md`](../proofs/README.md) |
| Materialized published scope | Publication is a governed state, not a convenience copy out of work | [`../published/README.md`](../published/README.md) |
| Source-registration entries or identity schemas | Onboarding and dataset identity should stay small, explicit, and diffable | [`../registry/README.md`](../registry/README.md) |
| Policy bundles, contract schemas, or runtime code | Preserve lane boundaries instead of hiding control-plane assets in staging | [`../../policy/README.md`](../../policy/README.md) · [`../../contracts/README.md`](../../contracts/README.md) · [`../../schemas/README.md`](../../schemas/README.md) · app/package surfaces |

> [!WARNING]
> “Useful for an analyst right now” is **not** enough. If the artifact weakens reproducibility, obscures provenance, or tempts direct UI/runtime consumption, it does not belong here in unmanaged form.

[Back to top](#datawork)

---

## Directory tree

### Confirmed current public tree

```text
data/work/
└── README.md
```

### Confirmed current `data/` sibling excerpt

```text
data/
├── catalog/
├── processed/
├── proofs/
├── published/
├── quarantine/
├── raw/
├── receipts/
├── registry/
├── work/
└── README.md
```

### Proposed working deepening

```text
data/work/
├── README.md
└── <domain-or-dataset>/
    └── <run-id>/
        ├── staging/
        ├── qa/
        ├── logs/
        ├── manifests/
        ├── NOTES.md
        ├── run_record.json
        ├── run_manifest.json
        ├── validation_report.json
        ├── checksums.txt
        ├── spec_hash.txt
        ├── run_receipt.json
        ├── ai_receipt.json
        └── attestations/
```

> [!NOTE]
> The deeper `run_receipt.json`, `ai_receipt.json`, and `attestations/` examples above are **PROPOSED proof-aware carryovers**, not confirmed checked-in structure. Avoid adopting them verbatim unless the active branch confirms the convention.

> [!NOTE]
> Avoid inventing a pseudo-quarantine subtree under `data/work/`. If a run becomes blocked by rights, sensitivity, validation, or review, move or reference it explicitly in [`../quarantine/README.md`](../quarantine/README.md).

### Naming guidance

Prefer deterministic, boring names over clever names.

- `<domain-or-dataset>`: stable domain or dataset family name
- `<run-id>`: sortable run key, batch key, or date-based identifier
- `NOTES.md`: short human-readable explanation of what changed and why
- `run_*` / `validation_*` files: only after the active branch confirms those names are acceptable
- proof-aware names such as `run_receipt.json`, `ai_receipt.json`, or attestation bundle pointers: only after the active branch confirms whether this lane keeps local copies, central mirrors, or references only

[Back to top](#datawork)

---

## Quickstart

### Inspect the current lane

```bash
find data/work -maxdepth 2 -print | sort
```

### Inspect the surrounding lane contract

```bash
sed -n '1,220p' data/README.md
sed -n '1,220p' data/raw/README.md
sed -n '1,220p' data/quarantine/README.md
sed -n '1,220p' data/processed/README.md
sed -n '1,220p' data/work/README.md
```

### Create a starter run area

```bash
RUN_ID="2026-04-12-example-001"
mkdir -p "data/work/<dataset>/${RUN_ID}"/{staging,qa,logs,manifests}
```

### Record the purpose of the work

```bash
cat > "data/work/<dataset>/${RUN_ID}/NOTES.md" <<'EOF'
# Working note

- Source input: data/raw/<source-batch>/
- Intended handoff: data/processed/<dataset>/
- Public exposure: blocked
- Reviewer: TBD
- Status: draft
EOF
```

### Escalate blocked work explicitly

```bash
# Illustrative only — verify local handling rules before adopting verbatim.
CASE_ID="q-$(date -u +%Y%m%d)-<dataset>-001"
mkdir -p "data/quarantine/${CASE_ID}"
```

### Validate with confirmed local tooling only

Use the checked-out command set documented in [`../../tools/README.md`](../../tools/README.md), [`../../scripts/README.md`](../../scripts/README.md), and any narrower helper-lane README that the active branch actually exposes. Do not assume an unverified `promote`, `gate`, or `publish` CLI exists just because doctrine or earlier planning documents mention one.

### Keep proof-aware artifacts explicit only when they exist

```bash
# Illustrative only — verify branch-local naming before adopting.
touch "data/work/<dataset>/${RUN_ID}/spec_hash.txt"
```

If the active branch already emits `run_receipt`, `ai_receipt`, or attestation references for the run, keep them explicit and reviewable rather than burying them in free-form notes.

[Back to top](#datawork)

---

## Usage

### 1. Admit from raw, do not reinvent raw

Start from admitted source material in [`../raw/README.md`](../raw/README.md). `data/work/` should never become a shadow raw archive.

### 2. Transform in small, reviewable steps

Prefer a chain of understandable intermediates over one opaque mega-step. This keeps replay, QA, and handoff review legible.

### 3. Attach evidence while the work is fresh

If a normalization decision, reprojection, filter threshold, enrichment step, or redaction choice matters, capture it here before it becomes tribal memory.

If a run already emits proof-aware support objects such as `spec_hash`, `run_receipt`, `ai_receipt`, or attestation references, record or reference them explicitly so the work stays explainable. Keep their status visible as pre-release support unless and until downstream review promotes them.

### 4. Escalate failure or ambiguity to quarantine

When rights are unclear, validation fails, sensitivity is unresolved, or review blocks advancement, use [`../quarantine/README.md`](../quarantine/README.md) rather than leaving “temporary” blocked material mixed into normal work runs.

### 5. Keep receipts and proofs adjacent, not hidden

Receipts preserve **process memory**. Proofs preserve **release evidence**. If process memory needs to stay centrally queryable, place it in [`../receipts/README.md`](../receipts/README.md). If evidence belongs to release proof, use [`../proofs/README.md`](../proofs/README.md). `data/work/` should not become a junk drawer for all governance artifacts.

### 6. Hand off cleanly to processed

Promotion out of `data/work/` should reduce ambiguity, not move it downstream. By the time material leaves this lane, its target processed identity, validation context, and downstream catalog intent should be clear.

[Back to top](#datawork)

---

## Diagram

```mermaid
flowchart LR
    A[data/raw/] --> B[data/work/]
    B -->|blocked or unclear| Q[data/quarantine/]
    B -->|run / validation memory| R[data/receipts/]
    B -->|stable handoff| C[data/processed/]
    C --> K[data/catalog/ <br/> dcat · stac · prov]
    C --> P[data/proofs/]
    K --> U[data/published/]
    P --> U
    U --> G[Governed API / trust-visible shell]

    G -. never direct .-> B
    G -. never direct .-> Q
    G -. never direct .-> A
```

### Reading rule

The key relationship is not just left-to-right flow. It is the **blocked path**: normal governed surfaces do **not** read `data/work/`, `data/quarantine/`, or `data/raw/` directly.

[Back to top](#datawork)

---

## Reference tables

### Zone comparison

| Zone | Primary job | Public-facing? | Working rule |
|---|---|---:|---|
| `data/raw/` | Immutable intake | No | Preserve source-native capture and terms context |
| `data/work/` | Repeatable transform + QA staging | No | Keep intermediates reviewable and non-public |
| `data/quarantine/` | Fail-closed hold | No | Isolate blocked or unclear material explicitly |
| `data/processed/` | Stable processed outputs | Indirect only | Carry governed dataset versions and release-adjacent artifacts |
| `data/catalog/` | `DCAT + STAC + PROV` closure | Indirect only | Make release-backed truth discoverable, traceable, and cross-linkable |
| `data/published/` | Optional materialized published scope | Indirect only | Materialize only already governed, release-backed scope |

### Receipts vs proofs at this boundary

| Surface | Primary job | Keep it here when... |
|---|---|---|
| `data/receipts/` | Queryable process memory | the artifact explains fetch, run, validation, replay, audit, or correction context across runs |
| `data/proofs/` | Release evidence | the artifact proves promotion, release meaning, rollback, correction, withdrawal, or supersession |

### Current public sibling surfaces relevant to `data/work/`

| Sibling | Current public state | Why `data/work/` maintainers should care |
|---|---|---|
| [`../raw/README.md`](../raw/README.md) | README-backed live lane | Defines where source-native inputs start |
| [`../quarantine/README.md`](../quarantine/README.md) | README-backed live lane | Prevents blocked work from leaking forward |
| [`../processed/README.md`](../processed/README.md) | README-backed live lane | Defines the immediate downstream handoff target |
| [`../catalog/README.md`](../catalog/README.md) | Live parent with `dcat/`, `stac/`, and `prov/` | Clarifies where closure happens after processed handoff |
| [`../receipts/README.md`](../receipts/README.md) | README-backed live lane | Separates process memory from payload staging |
| [`../proofs/README.md`](../proofs/README.md) | README-backed live lane | Separates release proof from in-flight work |
| [`../published/README.md`](../published/README.md) | README-backed live lane | Reminds maintainers that publication is downstream, not implicit |
| [`../registry/README.md`](../registry/README.md) | README-backed lane; current public tree also shows `data/registry/schemas/README.md` | Keeps source/dataset identity out of staging clutter |

### Typical starter artifact classes

| Artifact class | Typical use | Status in this README |
|---|---|---|
| normalized intermediate dataset | schema/CRS/unit alignment | **CONFIRMED fit** |
| QA sample or validation output | pass/fail or warning context | **CONFIRMED fit** |
| transform note | preserves non-obvious decisions | **CONFIRMED fit** |
| `run_record.json` | compact run summary | **PROPOSED starter pattern** |
| `run_manifest.json` | file inventory + digests + roles | **PROPOSED starter pattern** |
| `validation_report.json` | structured validation result | **PROPOSED starter pattern** |
| `checksums.txt` | quick integrity check | **PROPOSED starter pattern** |
| `spec_hash.txt` | stable spec or input hash carryover | **PROPOSED starter pattern** |
| `run_receipt.json` | machine-checkable run audit object | **PROPOSED proof-aware carryover** |
| `ai_receipt.json` | model-mediated proposal or synthesis audit object | **PROPOSED proof-aware carryover** |
| attestation ref / bundle pointer | integrity or origin evidence for emitted artifacts | **PROPOSED proof-aware carryover** |

[Back to top](#datawork)

---

## Definition of done / promotion gates

A work run is ready to leave `data/work/` only when the following are satisfied:

- [ ] Inputs resolve back to admitted source material in `data/raw/` or to an explicitly resolved quarantine case.
- [ ] Intermediate outputs are reproducible enough to replay or explain.
- [ ] QA evidence exists and unresolved issues are visible.
- [ ] Rights, sensitivity, redaction, and generalization implications are explicit.
- [ ] The intended target in `data/processed/` is named.
- [ ] Receipt placement is clear if process memory must be retained centrally in `data/receipts/`.
- [ ] Release-evidence placement is clear if the work is approaching proof-bearing promotion in `data/proofs/`.
- [ ] If the run emits proof-aware artifacts such as `spec_hash`, `run_receipt`, `ai_receipt`, or attestation refs, their placement and downstream references are explicit.
- [ ] Promotion is being treated as a governed state transition rather than as a convenience folder copy.
- [ ] No outward catalog or published scope is being generated directly from `data/work/`.
- [ ] Any blocked subset has been moved or referenced to `data/quarantine/`.
- [ ] Local validators, scripts, and conventions used by the run have been verified on the active branch.

### Promotion-minded checklist

| Gate | Minimum expectation | Result if missing |
|---|---|---|
| Integrity | checksums or equivalent run-level integrity record where needed | hold or re-run |
| Validation | QA output, schema sanity, spatial/temporal sanity | hold or quarantine |
| Provenance | transform notes and upstream traceability | no trustworthy handoff |
| Rights / sensitivity | explicit labels or review notes | default deny |
| Handoff clarity | processed target and next zone are named | hold |
| Receipt / proof separation | process memory and release proof are not buried in staging | cleanup before promotion |
| Proof-aware traceability | any emitted `spec_hash` / receipt / attestation refs are explicit and not confused with release proof | hold / clarify |
| Reviewability | the run can be explained without guesswork | hold |

[Back to top](#datawork)

---

## FAQ

### Is `data/work/` the same as `data/quarantine/`?

No. `data/work/` is the normal repeatable transform and QA lane. [`../quarantine/README.md`](../quarantine/README.md) is the stricter fail-closed lane for blocked, ambiguous, or review-held material.

### Why can’t we publish directly from `data/work/`?

Because KFM treats publication as a governed trust-state change, not a convenient file move. `data/work/` is where ambiguity is reduced, not where outward truth is declared.

### Where should receipts go?

If receipts need to remain centrally queryable across runs, corrections, or audits, use [`../receipts/README.md`](../receipts/README.md). Keep only local, run-specific context in the work run itself unless branch conventions say otherwise.

### Where should proof packs and attestations go?

Use [`../proofs/README.md`](../proofs/README.md) for release-significant evidence. `data/work/` is not the release-evidence home.

### Should `run_receipt.json` or `ai_receipt.json` live here?

Sometimes, but only as **PROPOSED** local carryovers until the active branch confirms naming and placement. If the artifact is needed mainly for centrally queryable process memory, prefer [`../receipts/README.md`](../receipts/README.md). If it is release-significant or promotion-bearing proof, use [`../proofs/README.md`](../proofs/README.md).

### Does “README-only on public main” mean the lane is unused?

No. It only means the **currently visible public subtree** is documentation-light. This README should not speculate about populated working branches, external storage mappings, or private runtime usage without direct verification.

### Can normal UI or API surfaces read previews from here?

Not as a normal governed path. Any preview behavior still has to respect the trust membrane and should not normalize direct reads from `data/work/`.

[Back to top](#datawork)

---

## Appendix

<details>
<summary><strong>Confirmed current public-tree signals</strong></summary>

### Confirmed on public `main`

- `data/` currently shows `catalog/`, `processed/`, `proofs/`, `published/`, `quarantine/`, `raw/`, `receipts/`, `registry/`, `work/`, and `README.md`.
- `data/work/` currently shows `README.md` only.
- `data/catalog/` currently shows `dcat/`, `stac/`, and `prov/`.
- `data/registry/` currently shows `README.md` and `schemas/README.md`.
- Public `.github/CODEOWNERS` coverage assigns `/data/` to `@bartytime4life`.
- The public file history for `data/work/README.md` shows a current-main update on `2026-04-01`, plus a `2026-03-21` deletion / `2026-03-22` reintroduction sequence for the current-file incarnation.

### Why that matters here

This README can now distinguish:
- **live path existence** from
- **README-level directory contracts** from
- **deeper working patterns that still need branch verification**.

</details>

<details>
<summary><strong>Proposed starter artifacts</strong></summary>

```json
{
  "status": "PROPOSED example",
  "artifacts": [
    "NOTES.md",
    "run_record.json",
    "run_manifest.json",
    "validation_report.json",
    "checksums.txt",
    "spec_hash.txt",
    "run_receipt.json",
    "ai_receipt.json",
    "attestation-ref-or-bundle-pointer"
  ],
  "note": "Use only after the active branch confirms naming and placement conventions."
}
```

</details>

<details>
<summary><strong>Open verification items before merge</strong></summary>

- final `doc_id` for the KFM meta block
- final `policy_label` for this directory
- whether `created:` should remain pinned to the current-file `2026-03-22` reintroduction or instead trace back to the earlier January path history
- whether branch-local working runs already use a stricter naming convention
- whether any branch-side automation writes receipts locally vs centrally to `data/receipts/`
- whether release-adjacent proof placement is fully standardized in branch-local tooling
- whether `run_receipt` / `ai_receipt` are expected as local carryovers, central mirrors, or reference-only objects on the active branch
- any active validator or handoff command documented in `tools/` or `scripts/`
- whether external object storage or runtime packaging mirrors this lane beyond the public repo

</details>

---

_This README stays trust-visible and verification-first: it preserves the live public path, makes the lifecycle boundary legible, keeps deeper working shape explicit instead of implied, and treats proof-aware carryovers as doctrine-supported but still branch-verification-sensitive._

[Back to top](#datawork)