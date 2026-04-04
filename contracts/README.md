<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<TODO-uuid>
title: contracts
type: standard
version: v1
status: draft
owners: @bartytime4life
created: <TODO: verify YYYY-MM-DD>
updated: 2026-04-04
policy_label: public
related: [tests/README.md, tests/integration/README.md, tests/policy/README.md, tests/reproducibility/README.md, tests/unit/README.md, tests/e2e/README.md, contracts/README.md, schemas/README.md, schemas/contracts/README.md, schemas/contracts/v1/README.md, schemas/tests/README.md, policy/README.md, docs/standards/README.md, .github/workflows/README.md, .github/PULL_REQUEST_TEMPLATE.md, .github/CODEOWNERS]
tags: [kfm, tests, contracts, verification, schema-drift, fail-closed]
notes: [doc_id and created date need verification; updated reflects this revision draft; current public main shows tests/contracts as README-only while adjacent schema lanes are live under schemas/contracts and schemas/tests]
[/KFM_META_BLOCK_V2] -->

# contracts

Contract-facing verification family for KFM schema drift, valid/invalid example packs, and fail-closed object validation.

> **Status:** experimental  
> **Owners:** `@bartytime4life`  
> **Path:** `tests/contracts/README.md`  
> **Repo fit:** downstream of [`../README.md`](../README.md), [`../../contracts/README.md`](../../contracts/README.md), [`../../schemas/README.md`](../../schemas/README.md), [`../../schemas/contracts/README.md`](../../schemas/contracts/README.md), [`../../schemas/contracts/v1/README.md`](../../schemas/contracts/v1/README.md), [`../../schemas/tests/README.md`](../../schemas/tests/README.md), [`../../policy/README.md`](../../policy/README.md), [`../../docs/standards/README.md`](../../docs/standards/README.md), [`../../.github/workflows/README.md`](../../.github/workflows/README.md), [`../../.github/PULL_REQUEST_TEMPLATE.md`](../../.github/PULL_REQUEST_TEMPLATE.md), and [`../../.github/CODEOWNERS`](../../.github/CODEOWNERS); lateral to [`../policy/`](../policy/), [`../integration/`](../integration/), [`../reproducibility/`](../reproducibility/), [`../accessibility/`](../accessibility/), and [`../unit/`](../unit/); upstream of future executable cases under `tests/contracts/**` and any escalation into [`../integration/`](../integration/) or [`../e2e/`](../e2e/).  
> **Quick jump:** [Scope](#scope) · [Repo fit](#repo-fit) · [Current verified snapshot](#current-verified-snapshot) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Diagram](#diagram) · [Tables](#tables) · [Task list / definition of done](#task-list--definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)  
>
> ![status](https://img.shields.io/badge/status-experimental-orange)
> ![family](https://img.shields.io/badge/family-tests--contracts-1f6feb)
> ![owners](https://img.shields.io/badge/owners-%40bartytime4life-6f42c1)
> ![current public inventory](https://img.shields.io/badge/current%20public%20inventory-README--only-lightgrey)
> ![adjacent schema lane](https://img.shields.io/badge/adjacent%20schema%20lane-live%20scaffold-8250df)
> ![schema fixtures](https://img.shields.io/badge/schema--tests%20fixtures-scaffold-lightgrey)
> ![workflow lane](https://img.shields.io/badge/workflows-README--only-lightgrey)
> ![truth posture](https://img.shields.io/badge/truth-CONFIRMED%20%7C%20INFERRED%20%7C%20PROPOSED%20%7C%20UNKNOWN-2ea043)

> [!IMPORTANT]
> The parent [`tests/README.md`](../README.md) keeps `contracts/` as a first-class repo family in the public `tests/` tree.
> This README follows that repo-visible plural path and keeps the directory narrow on purpose: verify machine-readable contract truth here, and escalate broader seams elsewhere.

> [!CAUTION]
> Current public evidence confirms a **directory boundary and README surface here**, while adjacent schema-side lanes are now visibly real under [`../../schemas/contracts/`](../../schemas/contracts/README.md) and [`../../schemas/tests/`](../../schemas/tests/README.md).
> Treat validator entrypoints, fixture packs, shared helpers, and merge-blocking workflow claims below as **PROPOSED** or **NEEDS VERIFICATION** unless the checked-out branch proves them directly.

---

## Scope

`tests/contracts/` is the contract-facing verification family inside KFM’s governed `tests/` surface.

Its job is specific: prove that trust-bearing objects are shaped correctly, reject invalid states deterministically, and fail closed when required evidence, policy, or correction fields are missing. This family should help the repo answer a harder question than “did the test pass?”:

- did the contract fail loudly instead of drifting silently?
- did an invalid object stay invalid instead of being normalized into something plausible?
- did negative states remain explicit instead of being flattened into “success”?
- did downstream lanes inherit stable assumptions instead of wishful ones?

### Working role

`tests/contracts/` is the natural home for shape validation and example-pack truth for contract families such as:

- `SourceDescriptor`
- `IngestReceipt`
- `ValidationReport`
- `DatasetVersion`
- `CatalogClosure`
- `DecisionEnvelope`
- `ReviewRecord`
- `ReleaseManifest` / `ReleaseProofPack`
- `ProjectionBuildReceipt`
- `EvidenceBundle`
- `RuntimeResponseEnvelope`
- `CorrectionNotice`

### Status vocabulary used here

| Label | Meaning here |
| --- | --- |
| **CONFIRMED** | Directly visible in the current public repo tree or in adjacent repo documentation |
| **INFERRED** | Conservative interpretation of visible repo structure or adjacent docs, but not a settled implementation fact |
| **PROPOSED** | Strong repo- and doctrine-aligned starter shape not yet verified as mounted implementation |
| **UNKNOWN** | Not proven from current public repo evidence |
| **NEEDS VERIFICATION** | A detail that should be checked against the active checkout, runner, or platform settings before merge |

### What this family should prove

- required fields exist
- invalid shapes are rejected
- contract examples stay synchronized with canonical docs
- negative outcomes remain first-class rather than being silently normalized away
- contract drift is caught before integration, UI, runtime, or release layers build on it

### What this family should **not** try to prove alone

- cross-service wiring
- end-to-end publication or release assembly
- UI trust-state rendering
- policy bundle semantics beyond contract-facing fixtures
- digest stability or rerun reproducibility as a primary burden
- accessibility behavior such as keyboard, motion, or non-color-only trust cues
- geospatial correctness beyond object-shape expectations

For those, escalate into [`../integration/`](../integration/), [`../policy/`](../policy/), [`../reproducibility/`](../reproducibility/), [`../accessibility/`](../accessibility/), or [`../e2e/`](../e2e/).

[Back to top](#contracts)

---

## Repo fit

### Upstream authorities this family should stay aligned with

| Upstream surface | Why it matters here | Current visible posture |
| --- | --- | --- |
| [`../README.md`](../README.md) | Defines `tests/` as a governed verification surface and keeps `contracts/` visible as its own family | Experimental directory index for verification families |
| [`../../contracts/README.md`](../../contracts/README.md) | Human-readable contract doctrine, trust-object list, and first-wave starter pressure | Draft doc surface; canonical machine-home still unresolved |
| [`../../schemas/README.md`](../../schemas/README.md) | Documents the wider `schemas/` boundary and warns against parallel schema authority | No longer README-only on public `main`; still authority-sensitive |
| [`../../schemas/contracts/README.md`](../../schemas/contracts/README.md) | Makes the live schema-side machine-file subtree explicit | `v1/` and `vocab/` are visible on public `main` |
| [`../../schemas/contracts/v1/README.md`](../../schemas/contracts/v1/README.md) | Shows the current public family split for first-wave machine contracts | `common/`, `correction/`, `data/`, `evidence/`, `policy/`, `release/`, `runtime/`, and `source/` are branch-visible |
| [`../../schemas/tests/README.md`](../../schemas/tests/README.md) | Documents the schema-side fixture scaffold and its non-canonical posture | `fixtures/contracts/v1/{valid,invalid}` is visible but scaffold-only |
| [`../../policy/README.md`](../../policy/README.md) | Keeps deny-by-default posture, reasons/obligations, and finite outcomes close to contract verification | Experimental; OPA/Rego described as the starter engine |
| [`../../docs/standards/README.md`](../../docs/standards/README.md) | Keeps standards/profile routing separate from executable proof | Cross-cutting standards stay documented without silently becoming tests |
| [`../../.github/workflows/README.md`](../../.github/workflows/README.md) | Documents the automation lane and warns against treating historical workflow activity as current checked-in inventory | Experimental; public `main` inventory is README-only |
| [`../../.github/PULL_REQUEST_TEMPLATE.md`](../../.github/PULL_REQUEST_TEMPLATE.md) | Pull requests already require honest truth labels and evidence / proof links | Review template expects visible proof, not polished overclaiming |
| [`../../.github/CODEOWNERS`](../../.github/CODEOWNERS) | Keeps current owner and review boundary explicit | `/tests/` currently falls under `@bartytime4life` |

### Lateral family boundaries

Use sibling test families rather than stretching this README beyond its burden:

- [`../unit/`](../unit/) for deterministic local helpers and pure local behavior
- [`../policy/`](../policy/) for policy grammar and deny-by-default behavior checks
- [`../integration/`](../integration/) for cross-boundary governed slices
- [`../reproducibility/`](../reproducibility/) for rerun consistency, digest stability, and receipt-backed rebuild checks
- [`../accessibility/`](../accessibility/) for trust-visible shell operability
- [`../e2e/`](../e2e/) for full runtime, release, and correction proof

### Downstream consequences

If this directory stays weak, later lanes become easier to bluff:

- integration tests inherit unstable payload assumptions
- policy tests drift into free text because example packs are missing
- e2e cases can “pass” on objects that should have failed earlier
- docs imply a contract system that the repo does not yet enforce
- runtime or UI surfaces risk sounding confident on unverified payload shapes

### Path reconciliation note

The repo now exposes four adjacent but non-identical surfaces:

- [`../../contracts/`](../../contracts/README.md) for human-readable contract law and authority-facing guidance
- [`../../schemas/contracts/`](../../schemas/contracts/README.md) for live machine-file scaffolds and vocab registries
- [`../../schemas/tests/`](../../schemas/tests/README.md) for nested schema-side fixture scaffolds
- `tests/contracts/` for the root contract-facing verification family

This README should keep those roles legible instead of flattening them into one implied authority.

[Back to top](#contracts)

---

## Current verified snapshot

| Item | Status | Why it matters |
| --- | --- | --- |
| `tests/contracts/` exists as its own repo-visible family | **CONFIRMED** | Keep the family visible instead of folding it into generic tests prose |
| The current public directory listing shows `README.md` only inside `tests/contracts/` | **CONFIRMED** | README presence is not proof of executable suite depth |
| The parent `tests/` tree currently exposes `accessibility/`, `contracts/`, `e2e/`, `integration/`, `policy/`, `reproducibility/`, and `unit/` | **CONFIRMED** | Use the actual sibling-family boundaries already visible on `main` |
| `tests/e2e/` already exposes visible leaf families `correction/`, `release_assembly/`, and `runtime_proof/` | **CONFIRMED** | Escalation targets are not hypothetical anymore |
| `.github/workflows/` is documentation-visible but README-only on current public `main` | **CONFIRMED** | Do not assume merge-blocking contract automation from current tree alone |
| `schemas/` is no longer effectively README-only on current public `main` | **CONFIRMED** | This README must reflect live schema-side reality, not an older blank-tree story |
| `schemas/contracts/` now exposes `README.md`, `v1/`, and `vocab/` | **CONFIRMED** | Contract-machine scaffolds are branch-visible nearby |
| `schemas/contracts/v1/` exposes `common/`, `correction/`, `data/`, `evidence/`, `policy/`, `release/`, `runtime/`, and `source/` | **CONFIRMED** | First-wave family names are now visible in the public machine-file lane |
| `schemas/tests/fixtures/contracts/v1/{valid,invalid}` exists as a nested scaffold | **CONFIRMED** | A schema-side fixture lane is visible, but it does not settle canonical fixture-home law |
| Exact validator command, fixture inventory used by runners, local runner, required checks, branch protections, and rulesets | **NEEDS VERIFICATION** | These cannot be derived from public directory listings alone |

> [!NOTE]
> The asymmetry is the key current fact:
> `tests/contracts/` is still README-only, while adjacent schema-side lanes are real but scaffold-heavy.
> Reviewers should keep both halves visible at once.

[Back to top](#contracts)

---

## Accepted inputs

This directory should accept only materials that help verify contract truth.

### Belongs here

- valid JSON examples for trust-bearing object families
- invalid JSON examples that prove fail-closed behavior
- contract-specific validator entrypoints
- schema-to-example conformance tests
- fixture manifests or discovery manifests for contract waves
- regression cases for negative states such as `deny`, `abstain`, `stale-visible`, `generalized`, `superseded`, or `withdrawn`
- minimal helper utilities used only to load, normalize, or validate contract fixtures
- local documentation that makes a contract case reviewable without inventing new authority
- runner-facing glue that points at the checked-out machine contract lane without copying those schemas into a second home

### Usually belongs nearby, not here

- policy bundle rule tests → [`../policy/`](../policy/)
- cross-component orchestration → [`../integration/`](../integration/)
- runtime proof traces and correction drills → [`../e2e/`](../e2e/)
- rerun consistency, `spec_hash` stability, and receipt comparison → [`../reproducibility/`](../reproducibility/)
- accessibility-critical trust-surface cases → [`../accessibility/`](../accessibility/)
- canonical schema definitions → currently visible under [`../../schemas/contracts/`](../../schemas/contracts/README.md), while authority remains unresolved with [`../../contracts/`](../../contracts/README.md)
- schema-side illustrative or mirrored fixture scaffolds → [`../../schemas/tests/`](../../schemas/tests/README.md)
- runbooks, ADRs, and long-form guidance → `docs/**`

---

## Exclusions

This directory should stay strict but small.

| Excluded from `tests/contracts/` | Put it here instead |
| --- | --- |
| Pure helper or local-function checks | [`../unit/`](../unit/) |
| Policy allow/deny reasoning beyond fixture compatibility | [`../policy/`](../policy/) |
| Reproducibility or digest-stability checks | [`../reproducibility/`](../reproducibility/) |
| Keyboard, screen-reader, reduced-motion, or non-color-only trust cues | [`../accessibility/`](../accessibility/) |
| Cross-service or cross-adapter seams | [`../integration/`](../integration/) |
| Full runtime/public-route, release-proof, or correction-visible sweeps | [`../e2e/`](../e2e/) |
| Database migration tests | package- or service-local test lanes |
| Geospatial CRS / topology / raster QA | geospatial validation suites or broader integration/e2e lanes |
| Canonical schema files, policy bundles, or route contracts as primary records | Their owning repo surfaces |
| Nested schema-side fixture scaffolds treated as singular truth by inertia | [`../../schemas/tests/`](../../schemas/tests/README.md) only if explicitly marked non-authoritative |
| Narrative examples that are only documentation | [`../../contracts/README.md`](../../contracts/README.md) or `docs/**` |

> [!IMPORTANT]
> A contract-facing test family should be **strict but small**.
> The goal is to catch structural dishonesty early, not to absorb every other verification concern in the repo.

[Back to top](#contracts)

---

## Directory tree

### Current public `main` snapshot — test-family view

```text
tests/
├── README.md
├── accessibility/
├── contracts/
│   └── README.md
├── e2e/
│   ├── README.md
│   ├── correction/
│   ├── release_assembly/
│   └── runtime_proof/
├── integration/
├── policy/
├── reproducibility/
└── unit/
```

### Current public `main` snapshot — adjacent schema-side reality

```text
schemas/
├── README.md
├── contracts/
│   ├── README.md
│   ├── v1/
│   │   ├── README.md
│   │   ├── common/
│   │   │   └── header_profile.schema.json
│   │   ├── correction/
│   │   │   └── correction_notice.schema.json
│   │   ├── data/
│   │   │   └── dataset_version.schema.json
│   │   ├── evidence/
│   │   │   └── evidence_bundle.schema.json
│   │   ├── policy/
│   │   │   └── decision_envelope.schema.json
│   │   ├── release/
│   │   │   └── release_manifest.schema.json
│   │   ├── runtime/
│   │   │   └── runtime_response_envelope.schema.json
│   │   └── source/
│   │       └── source_descriptor.schema.json
│   └── vocab/
│       ├── obligation_codes.json
│       ├── reason_codes.json
│       └── reviewer_roles.json
└── tests/
    └── fixtures/
        └── contracts/
            └── v1/
                ├── README.md
                ├── invalid/
                │   └── README.md
                └── valid/
                    └── README.md
```

### PROPOSED maturity shape for this directory

```text
tests/contracts/
├── README.md
├── cases/
│   └── wave-01-core/
│       ├── decision-envelope/
│       ├── evidence-bundle/
│       ├── runtime-response-envelope/
│       ├── correction-notice/
│       ├── release-manifest/
│       ├── source-descriptor/
│       └── dataset-version/
├── manifests/
│   └── contract_cases.v1.json
├── helpers/
│   ├── __init__.py
│   ├── load_case.py
│   └── normalize_json.py
├── validators/
│   ├── jsonschema_runner.py
│   └── manifest.py
└── reports/
    └── .gitkeep
```

### Coordination pattern to prefer

Point validators at the checked-out machine contract lane and any explicitly chosen fixture lane, rather than cloning schemas into a third authority surface.

```text
schemas/contracts/v1/**/*.schema.json              # current public machine-file scaffold
schemas/tests/fixtures/contracts/v1/{valid,invalid}/  # current public nested fixture scaffold
tests/contracts/**                                 # root verification family, runners, manifests, reports
```

[Back to top](#contracts)

---

## Quickstart

### Safe inspection commands

```bash
# inspect the family exactly as the checked-out branch exposes it
find tests/contracts -maxdepth 4 -type f | sort

# inspect sibling test-family docs to keep placement honest
sed -n '1,220p' tests/README.md
sed -n '1,220p' tests/integration/README.md
sed -n '1,220p' tests/policy/README.md
sed -n '1,220p' tests/reproducibility/README.md
sed -n '1,220p' tests/unit/README.md
sed -n '1,220p' tests/accessibility/README.md
sed -n '1,220p' tests/e2e/README.md

# inspect adjacent contract / schema / fixture / workflow doctrine
sed -n '1,260p' contracts/README.md
sed -n '1,220p' schemas/README.md
sed -n '1,260p' schemas/contracts/README.md
sed -n '1,260p' schemas/contracts/v1/README.md
sed -n '1,220p' schemas/tests/README.md
sed -n '1,220p' schemas/tests/fixtures/contracts/v1/README.md
sed -n '1,220p' policy/README.md
sed -n '1,220p' docs/standards/README.md
sed -n '1,220p' .github/workflows/README.md
sed -n '1,220p' .github/PULL_REQUEST_TEMPLATE.md
sed -n '1,220p' .github/CODEOWNERS
```

### Fast drift check

Use this before inventing new names or object families:

```bash
grep -RIn \
  -e 'SourceDescriptor' \
  -e 'IngestReceipt' \
  -e 'ValidationReport' \
  -e 'DatasetVersion' \
  -e 'CatalogClosure' \
  -e 'DecisionEnvelope' \
  -e 'EvidenceBundle' \
  -e 'RuntimeResponseEnvelope' \
  -e 'CorrectionNotice' \
  -e 'ReleaseManifest' \
  -e 'ABSTAIN' \
  -e 'DENY' \
  -e 'ERROR' \
  -e 'schemas/contracts/v1' \
  -e 'schemas/tests/fixtures/contracts/v1' \
  tests contracts schemas policy docs .github 2>/dev/null || true
```

### PROPOSED future validator shape

The command below is illustrative only.
It uses a **real current public schema path** and a **PROPOSED root-test case path**.
Do **not** treat it as current repo behavior until a real validator entrypoint is checked in and referenced by the checked-out branch.

```bash
python -m jsonschema \
  --instance tests/contracts/cases/wave-01-core/runtime-response-envelope.answer.valid.json \
  schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
```

### Workflow caution

> [!CAUTION]
> Do **not** assume that adding files under `tests/contracts/` automatically makes them merge-blocking.
> Current public evidence proves a workflow documentation lane, not a visible checked-in workflow YAML gate on `main`.

[Back to top](#contracts)

---

## Usage

### Placement rules

1. Put **shape validation** here, but read schemas from the checked-out contract lane instead of cloning them.
2. Put **semantic policy decisions** in [`../policy/`](../policy/).
3. Put **service wiring** in [`../integration/`](../integration/).
4. Put **rerun / digest / receipt stability** in [`../reproducibility/`](../reproducibility/).
5. Put **trust-visible accessibility behavior** in [`../accessibility/`](../accessibility/).
6. Put **public-surface behavior**, **release proof**, and **correction flows** in [`../e2e/`](../e2e/).
7. Keep any helper code here **small, deterministic, and non-authoritative**.
8. When schema-side reality and contract-side doctrine diverge, document the divergence and stop the PR rather than smoothing it away.

### Naming guidance

Use case names that preserve family, polarity, and intent.

| Good example | Why it helps |
| --- | --- |
| `runtime_response_envelope.answer.valid.json` | family + outcome + polarity |
| `decision_envelope.missing_reason.invalid.json` | failure reason is obvious |
| `correction_notice.supersession.valid.json` | correction lineage remains visible |
| `evidence_bundle.partial_scope.invalid.json` | contract drift is reviewable in Git |

Avoid vague buckets such as `misc/`, `contract_v2/`, or `helpers_everything/`.

### First executable wave

Start with the families that are both high-leverage and already branch-visible in the public `schemas/contracts/v1/` lane:

1. `DecisionEnvelope`
2. `EvidenceBundle`
3. `RuntimeResponseEnvelope`
4. `CorrectionNotice`
5. `ReleaseManifest`
6. `SourceDescriptor`
7. `DatasetVersion`

Then expand into the contract-lattice names that remain doctrinally important but are **not** yet surfaced as first-wave public `v1` family files on `main`:

8. `IngestReceipt`
9. `ValidationReport`
10. `CatalogClosure`
11. `ReviewRecord`
12. `ProjectionBuildReceipt`

### Failure philosophy

A KFM contract case should prefer:

- explicit rejection over permissive coercion
- named invalid examples over hidden assumptions
- visible negative states over flattened “success”
- one real wave over pseudo-complete scaffolding
- stable, reviewable examples over clever test magic

[Back to top](#contracts)

---

## Diagram

```mermaid
flowchart LR
    D[contracts/<br/>human-readable contract law] --> C[tests/contracts/<br/>shape validation + case review]
    S[schemas/contracts/v1/**/*.schema.json<br/>live machine-file scaffold] --> C
    F[schemas/tests/fixtures/contracts/v1<br/>nested fixture scaffold] -. only if explicitly designated .-> C
    P[policy/<br/>reason & obligation vocab] --> C
    C -. local helper behavior .-> U[tests/unit/]
    C -. rerun / digest stability .-> R[tests/reproducibility/]
    C -. trust-visible accessibility .-> X[tests/accessibility/]
    C --> I[tests/integration/<br/>cross-boundary seams]
    C --> E[tests/e2e/<br/>runtime proof + release/correction]
    C --> G[PR review + docs<br/>drift becomes visible in Git]
```

The directional point stays the same:
`tests/contracts/` should **consume and verify** contract truth, not quietly become a second or third contract authority.

[Back to top](#contracts)

---

## Tables

### Family placement matrix

| If the work mainly tests… | Primary home | Why |
| --- | --- | --- |
| object shape and required fields | `tests/contracts/` | Keep machine-contract truth explicit and reviewable |
| policy result logic, reason codes, or obligation vocab | `tests/policy/` | Decision grammar should stay isolated when possible |
| pure local helper behavior | `tests/unit/` | Cheapest convincing proof wins |
| rerun consistency, `spec_hash` stability, or receipt comparison | `tests/reproducibility/` | Determinism is its own verification burden |
| keyboard / motion / screen-reader / non-color-only trust cues | `tests/accessibility/` | Accessibility is a first-class trust burden |
| route behavior across real boundaries | `tests/integration/` | This family exists for cross-boundary proof |
| full runtime/public behavior, release proof, or correction lineage | `tests/e2e/` | That burden is broader than one contract or integration slice |

### Candidate first cases

| Family | Why it belongs early | Current public schema-side signal | Minimum negative case |
| --- | --- | --- | --- |
| `RuntimeResponseEnvelope` | Trust-bearing runtime object for `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | [`../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json`](../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json) | missing `result`, missing `audit_ref`, unsupported surface state |
| `EvidenceBundle` | Keeps evidence inspectable at point of use | [`../../schemas/contracts/v1/evidence/evidence_bundle.schema.json`](../../schemas/contracts/v1/evidence/evidence_bundle.schema.json) | missing lineage or rights/sensitivity state |
| `DecisionEnvelope` | Bridges policy posture into machine-readable outcomes | [`../../schemas/contracts/v1/policy/decision_envelope.schema.json`](../../schemas/contracts/v1/policy/decision_envelope.schema.json) | missing reason/obligation shape |
| `CorrectionNotice` | Preserves correction lineage | [`../../schemas/contracts/v1/correction/correction_notice.schema.json`](../../schemas/contracts/v1/correction/correction_notice.schema.json) | missing affected release or replacement linkage |
| `ReleaseManifest` | Binds outward release to proof and rollback posture | [`../../schemas/contracts/v1/release/release_manifest.schema.json`](../../schemas/contracts/v1/release/release_manifest.schema.json) | missing release refs or correction posture |
| `SourceDescriptor` | Keeps source-edge identity explicit before downstream derivation | [`../../schemas/contracts/v1/source/source_descriptor.schema.json`](../../schemas/contracts/v1/source/source_descriptor.schema.json) | missing source kind, rights, or freshness basis |
| `DatasetVersion` | Preserves versioned identity and lineage before promotion | [`../../schemas/contracts/v1/data/dataset_version.schema.json`](../../schemas/contracts/v1/data/dataset_version.schema.json) | missing version lineage, temporal basis, or status field |

### Contract-family design rules

| Rule | Why it matters |
| --- | --- |
| One valid and one invalid example is the minimum unit of seriousness | prose-only doctrine drifts too easily |
| Invalid cases should be named by failure reason | Git review becomes faster and less ambiguous |
| Keep fixtures deterministic | contract tests should not depend on network or clock jitter |
| Prefer explicit schema-version fields | later migration is easier to audit |
| Preserve negative-state vocabulary | KFM trust posture depends on visible failure classes |
| Do not duplicate canonical schemas here | this family proves behavior; it does not own singular authority |
| Keep schema-side scaffolds and root-test runners synchronized | current repo reality is split enough already |

[Back to top](#contracts)

---

## Task list / definition of done

### First executable suite bootstrap

- [ ] Confirm whether an existing repo-wide runner, validator, or shared fixture convention already governs this family
- [ ] Reconcile `tests/contracts/` with the live `schemas/contracts/v1/` subtree and `schemas/tests/fixtures/contracts/v1/` scaffold
- [ ] Confirm authoritative schema home between `contracts/` and `schemas/`
- [ ] Decide whether any schema-side fixture leaf is mirror-only, illustrative-only, or runnable input
- [ ] Add one real wave before adding broad subtrees
- [ ] Create first-wave contract cases for the highest-leverage families already visible under `schemas/contracts/v1/`
- [ ] Add paired valid / invalid examples
- [ ] Add one deterministic validator entrypoint
- [ ] Add one family-level manifest or discovery mechanism
- [ ] Wire the family into a real merge-blocking workflow
- [ ] Document how failures surface in PR review
- [ ] Cross-link runner inputs and schema sources from [`../../contracts/README.md`](../../contracts/README.md), [`../../schemas/contracts/README.md`](../../schemas/contracts/README.md), and [`../../schemas/tests/README.md`](../../schemas/tests/README.md)

### Definition of done

This family is meaningfully established when all of the following are true:

1. there is no silent conflict between `tests/contracts/`, `contracts/`, `schemas/contracts/`, and `schemas/tests/fixtures/contracts/`
2. at least one real wave of contract artifacts exists
3. each first-wave family has valid and invalid examples
4. validators run deterministically in local and CI contexts
5. failure output is readable enough for code review
6. adjacent docs stop describing this family as README-only intention
7. the PR can point to fixtures, proof of behavior, and proof of failure behavior
8. public `main` shows more than a scaffold README in this directory

### Review gates

Before accepting changes here, check:

- does this add verification, or just more wording?
- does it create duplicate authority with `contracts/`, `schemas/contracts/`, or `schemas/tests/`?
- does it preserve fail-closed semantics?
- does it keep negative states explicit?
- does it stay narrow enough to remain reviewable?
- can the PR link validation evidence, proof packs, screenshots, or follow-up issues where they exist?

[Back to top](#contracts)

---

## FAQ

### Why is this directory named `contracts/`, not `contract/`?

Because the current repo-visible path is `tests/contracts/`, and nearby repo docs already reference that family. This README stays faithful to the mounted public tree instead of normalizing it to a different shorthand.

### Why does this README mention `schemas/contracts/` and `schemas/tests/` so often?

Because the current public branch now visibly contains both a live schema-side machine-file lane and a nested schema-side fixture scaffold. Ignoring them would make this README less accurate than the repo it is supposed to describe.

### Why not store canonical schemas directly under `tests/contracts/`?

Because this family should verify contract truth, not quietly replace it. Until the repo explicitly chooses the authoritative schema home, duplicating schemas here increases drift risk.

### Why are valid/invalid fixtures emphasized so heavily?

Because fail-closed behavior and visible negative outcomes are treated throughout the current contract-facing docs as trust requirements, not edge cases. Contract examples are the smallest executable proof of that posture.

### Should reproducibility cases live here?

Not as a primary burden. A contract case may participate in a broader rerun proof, but digest stability, receipt comparison, and bounded-drift reruns belong first in [`../reproducibility/`](../reproducibility/).

### Why is so much marked PROPOSED or NEEDS VERIFICATION?

Because the current public branch shows a strong documentation pattern, but it still does not prove a publicly confirmed executable contract harness in this directory.

### Should API endpoint tests live here?

Not usually. Keep object-shape checks here; move route wiring and full runtime behavior into integration or e2e lanes.

---

## Appendix

<details>
<summary><strong>Evidence notes, contract lattice, and open checks</strong></summary>

### Evidence notes

This revision is grounded first in the current public repo surfaces that define this family and its neighbors:

- `tests/contracts/README.md`
- `tests/README.md`
- `tests/integration/README.md`
- `tests/policy/README.md`
- `tests/reproducibility/README.md`
- `tests/unit/README.md`
- `tests/accessibility/README.md`
- `tests/e2e/README.md`
- `contracts/README.md`
- `schemas/README.md`
- `schemas/contracts/README.md`
- `schemas/contracts/v1/README.md`
- `schemas/contracts/v1/common/README.md`
- `schemas/contracts/v1/source/README.md`
- `schemas/contracts/v1/data/README.md`
- `schemas/contracts/v1/evidence/README.md`
- `schemas/contracts/v1/policy/README.md`
- `schemas/contracts/v1/release/README.md`
- `schemas/contracts/v1/runtime/README.md`
- `schemas/contracts/v1/correction/README.md`
- `schemas/tests/README.md`
- `schemas/tests/fixtures/contracts/v1/README.md`
- `policy/README.md`
- `docs/standards/README.md`
- `.github/workflows/README.md`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/CODEOWNERS`
- repo root `README.md`
- `.github/README.md`

The file keeps current public-tree facts separate from doctrine-aligned starter shape.
It does **not** imply runnable CI, live validator enforcement, or real fixture inventory in this directory unless the current public tree proves those artifacts directly.

### Doctrinal contract lattice echoed here

The current contract-facing docs repeatedly center the following trust-bearing families:

- `SourceDescriptor`
- `IngestReceipt`
- `ValidationReport`
- `DatasetVersion`
- `CatalogClosure`
- `DecisionEnvelope`
- `ReviewRecord`
- `ReleaseManifest`
- `ReleaseProofPack`
- `ProjectionBuildReceipt`
- `EvidenceBundle`
- `RuntimeResponseEnvelope`
- `CorrectionNotice`

Current public `main` now also gives one more useful signal:
some of those families are already branch-visible as first-wave `*.schema.json` scaffold files under `schemas/contracts/v1/`, while others remain doctrine-facing names that have not yet surfaced there.

### Open verification items

- Is `contracts/` or `schemas/` the singular authoritative machine-contract home?
- Are schema-side `valid/invalid` leaves intended to stay illustrative, mirrored, generated, or eventually runnable?
- Is there a real validator script or package entrypoint not yet surfaced in docs?
- Are there checked-in workflow YAML files on the active working branch that do not appear on current public `main`?
- Does any existing thin slice already exercise contract validation indirectly?
- Which of the visible `schemas/contracts/v1/**/*.schema.json` files are still placeholder bodies on the working branch under review?
- How should this family coordinate with `tests/reproducibility/` once receipt-backed rebuild checks become real?

</details>
