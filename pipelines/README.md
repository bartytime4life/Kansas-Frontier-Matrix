<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TODO-uuid-pipelines-readme
title: KFM Pipelines
type: standard
version: v1
status: draft
owners: TODO(pipeline/data platform owners)
created: TODO(YYYY-MM-DD)
updated: TODO(YYYY-MM-DD)
policy_label: TODO(public|restricted)
related: [NEEDS_VERIFICATION:../docs/architecture/pipeline-lifecycle.md, NEEDS_VERIFICATION:../schemas/contracts/v1/, NEEDS_VERIFICATION:../policy/, NEEDS_VERIFICATION:../data/README.md]
tags: [kfm, pipelines, lifecycle, governance, evidence]
notes: [NEEDS VERIFICATION: drafted from attached KFM corpus and current workspace scan; replace placeholders after mounted-repo inspection.]
[/KFM_META_BLOCK_V2] -->

# KFM Pipelines

Purpose: define the governed pipeline home for moving spatial evidence through KFM’s lifecycle without bypassing evidence, policy, review, or publication gates.

<a id="top"></a>

![Status: experimental](https://img.shields.io/badge/status-experimental-orange)
![Truth posture: evidence bounded](https://img.shields.io/badge/truth--posture-evidence--bounded-blue)
![Lifecycle: governed](https://img.shields.io/badge/lifecycle-governed-2ea44f)
![Repo evidence: needs verification](https://img.shields.io/badge/repo--evidence-needs--verification-lightgrey)

| Field | Value |
|---|---|
| **Status** | **experimental / draft** |
| **Owners** | `TODO(pipeline/data platform owners)` |
| **Path** | `pipelines/` |
| **Document role** | Directory README and review gate for pipeline definitions, dry-runs, and lane processing flows |
| **Current evidence boundary** | **CONFIRMED:** this README was drafted without a mounted KFM Git repository. **UNKNOWN:** actual current `pipelines/` contents, package manager, CI wiring, and runtime behavior. |
| **Quick jumps** | [Scope](#scope) · [Repo fit](#repo-fit) · [Inputs](#inputs) · [Exclusions](#exclusions) · [Directory tree](#directory-tree) · [Pipeline contract](#minimum-pipeline-contract) · [Lifecycle](#lifecycle-map) · [Validation gates](#validation-gates) · [FAQ](#faq) |

> [!IMPORTANT]
> This README describes the intended KFM role of `pipelines/`. It does **not** prove that any pipeline, workflow, connector, fixture, validator, release artifact, or API route already exists. Treat implementation-shaped examples as **PROPOSED** until verified in the mounted repository.

---

## Scope

`pipelines/` is the repo home for **governed, repeatable processing flows** that transform admitted source material into validated, catalogable, reviewable, and eventually publishable KFM artifacts.

A KFM pipeline is not just a script. A pipeline is a reviewable transition with:

- a declared source and authority posture,
- explicit lifecycle inputs and outputs,
- schema and policy checks,
- deterministic identity where practical,
- receipts and validation reports,
- rollback or correction references,
- and no hidden route around the trust membrane.

### What this directory should make obvious

| Question | Pipeline answer |
|---|---|
| What source or artifact is being processed? | A `SourceDescriptor`, source intake record, dataset version, fixture, or governed prior-stage artifact. |
| What lifecycle transition is attempted? | Example: `RAW -> WORK`, `WORK -> PROCESSED`, or `PROCESSED -> PUBLISHED_CANDIDATE`. |
| What evidence supports visible claims? | `EvidenceRef -> EvidenceBundle` closure or a documented abstain/deny/error outcome. |
| What can safely leave the pipeline? | Only artifacts that pass schema, source-role, rights, sensitivity, citation, spatial, temporal, review, and release checks appropriate to risk. |
| How is failure handled? | Fail closed to `QUARANTINE`, `ABSTAIN`, `DENY`, `ERROR`, or a blocked promotion state. |

[Back to top](#top)

---

## Repo fit

### Path

```text
pipelines/
```

### Upstream dependencies

These are intended repo relationships and must be verified against the actual checkout before merge.

| Upstream surface | Expected relationship | Link status |
|---|---|---|
| [`../docs/architecture/pipeline-lifecycle.md`][docs-pipeline-lifecycle] | Human architecture for lifecycle rules and transitions | **NEEDS VERIFICATION** |
| [`../schemas/contracts/v1/`][schemas-contracts] | Machine-checkable object contracts after schema-home ADR | **NEEDS VERIFICATION** |
| [`../data/registry/`][data-registry] | Source descriptors, source authority records, and registry inputs | **NEEDS VERIFICATION** |
| [`../data/fixtures/`][data-fixtures] | Valid and invalid no-network fixtures for pipeline tests | **NEEDS VERIFICATION** |
| [`../policy/`][policy] | Rights, sensitivity, source-role, publication, and no-bypass policies | **NEEDS VERIFICATION** |
| [`../tools/validators/`][validators] | Reusable validators invoked by pipelines and CI | **NEEDS VERIFICATION** |

### Downstream consumers

| Downstream surface | Pipeline responsibility |
|---|---|
| [`../data/processed/`][data-processed] | Receives validated transformed artifacts, never unsupported claims. |
| [`../data/catalog/`][data-catalog] / [`../data/triplets/`][data-triplets] | Receives catalog and graph-ready derivatives after closure checks. |
| [`../data/receipts/`][data-receipts] / [`../data/proofs/`][data-proofs] | Receives process memory, proof objects, validation reports, and rollback references. |
| [`../release/`][release] | Receives release candidates only after promotion gates pass. |
| [`../apps/governed-api/`][governed-api] | Serves governed responses from released or policy-safe artifacts. |
| [`../apps/web/`][web-app] | Displays map, Evidence Drawer, Focus Mode, and export states from governed payloads only. |

[Back to top](#top)

---

## Inputs

Accepted inputs are narrow by design.

| Input class | Belongs here when… | Required posture |
|---|---|---|
| `SourceDescriptor` / source intake records | A pipeline needs to know source role, cadence, rights, support, and activation state | **Required before live source activation** |
| No-network fixtures | A pipeline needs repeatable tests before live connectors | **Required for first PRs** |
| Prior-stage lifecycle artifacts | A pipeline consumes `RAW`, `WORK`, `QUARANTINE`, or `PROCESSED` outputs through declared paths | **Must preserve stage provenance** |
| Schema and policy references | A run declares which contracts and policies it expects | **Must be versioned or hashable where practical** |
| Dry-run configuration | A pipeline proves behavior without publication | **Default for first slices** |
| Review or promotion candidate metadata | A run prepares a promotion package | **Must include receipts and rollback target** |

> [!NOTE]
> A source being public does not make it automatically publishable. Rights, sensitivity, source role, spatial support, temporal support, freshness, and review state still matter.

[Back to top](#top)

---

## Exclusions

Do not put these in `pipelines/`.

| Excluded item | Why it does not belong | Put it here instead |
|---|---|---|
| Raw source dumps | Lifecycle storage belongs outside executable pipeline definitions | `../data/raw/` |
| Work-in-progress transformed data | Pipelines may produce it, but should not store bulk stage data beside code | `../data/work/` or `../data/quarantine/` |
| Released public artifacts | Publication is a governed transition, not a folder copy | `../release/` and `../data/published/` |
| Secrets, API keys, tokens, cookies, model keys | Pipeline definitions must be reviewable and safe to publish internally | Secret manager or deployment config outside repo |
| Canonical policy decisions encoded only in scripts | Policy must be inspectable and testable outside ad hoc code | `../policy/` plus tests |
| Canonical object schemas embedded only in a runner | Schemas must remain reusable and validator-addressable | `../schemas/contracts/v1/` after ADR |
| Browser or map renderer truth logic | Public clients must not own trust-bearing state | `../apps/governed-api/`, `../apps/web/`, and typed payload contracts |
| Free-form AI prompts as pipeline truth | AI is interpretive, not the root evidence source | governed AI runtime contracts and evidence-bound receipts |

[Back to top](#top)

---

## Directory tree

**PROPOSED / NEEDS VERIFICATION** until the real repository is mounted.

```text
pipelines/
├── README.md
├── hydrology_huc12_dryrun/
│   ├── README.md
│   └── run.py
└── <domain>_<slice>/
    ├── README.md
    ├── run.py
    ├── manifests/
    │   └── pipeline.manifest.json
    └── fixtures/ -> ../../data/fixtures/<domain>/
```

### Naming pattern

Use names that expose both the domain and the proof burden.

| Pattern | Meaning | Example |
|---|---|---|
| `<domain>_<source-or-object>_dryrun/` | Fixture-first proof lane with no live fetch and no publication | `hydrology_huc12_dryrun/` |
| `<domain>_<transition>/` | Lifecycle transition runner | `soil_processed_to_catalog/` |
| `<domain>_<source>_watcher/` | Source refresh detector, only after source rights and cadence are verified | `hydrology_wbd_watcher/` |
| `<domain>_<release>_dryrun/` | Promotion package rehearsal | `habitat_release_dryrun/` |

[Back to top](#top)

---

## Lifecycle map

```mermaid
flowchart LR
  A[SourceDescriptor<br/>SourceIntakeRecord] --> B[RAW]
  B --> C{Admission gates}
  C -->|schema/source/rights pass| D[WORK]
  C -->|fail or ambiguity| E[QUARANTINE]
  D --> F{Transform + validate}
  E --> F
  F -->|valid + policy safe| G[PROCESSED]
  F -->|invalid / unsafe| E
  G --> H{Catalog + proof closure}
  H -->|STAC / DCAT / PROV<br/>EvidenceBundle closure| I[CATALOG / TRIPLET]
  H -->|missing proof| E
  I --> J{PromotionDecision}
  J -->|approved| K[PUBLISHED]
  J -->|blocked| E
  K --> L[Governed API]
  L --> M[Map / Evidence Drawer / Export / Focus Mode]
  K --> N[Correction / Withdrawal / Rollback]
  N --> J
```

### Stage responsibilities

| Stage | Pipeline role | Must not do |
|---|---|---|
| `RAW` | Preserve source arrival and intake identity | Pretend raw source data is public truth |
| `WORK` | Normalize, repair, enrich, and prepare with receipts | Hide transforms or overwrite lineage |
| `QUARANTINE` | Hold unsupported, unsafe, ambiguous, or failed records | Quietly drop records without disposition |
| `PROCESSED` | Emit validated artifacts and reports | Publish or serve directly to public clients |
| `CATALOG / TRIPLET` | Build catalog and graph-ready derivatives with closure | Let derived views replace canonical evidence |
| `PUBLISHED` | Release public-safe artifacts through promotion gates | Treat publication as a file move |
| `CORRECTION / WITHDRAWAL / ROLLBACK` | Repair released claims with visible lineage | Silently overwrite public history |

[Back to top](#top)

---

## Minimum pipeline contract

Every pipeline directory should include a local `README.md` and a machine-readable manifest once the repo convention is confirmed.

### Human README checklist

A pipeline README should answer:

- What lifecycle transition does this pipeline attempt?
- What sources, descriptors, fixtures, or prior-stage artifacts does it consume?
- What object families are affected?
- Which schemas and policies must pass?
- Which receipts, validation reports, catalog records, proof objects, or release candidates does it emit?
- What are the finite outcomes?
- What is the rollback or correction path?
- What remains `UNKNOWN` or `NEEDS VERIFICATION`?

### Illustrative manifest shape

```yaml
# ILLUSTRATIVE EXAMPLE — PROPOSED, not confirmed repo schema
pipeline_id: hydrology_huc12_dryrun
status: proposed
owner: TODO(pipeline/data platform owner)
lifecycle_transition:
  from: PROCESSED
  to: PUBLISHED_CANDIDATE
network: disabled
source_descriptors:
  - data/registry/sources/hydrology/wbd_huc12.source.json
schemas:
  - schemas/contracts/v1/source_descriptor.schema.json
  - schemas/contracts/v1/evidence_bundle.schema.json
  - schemas/contracts/v1/policy_decision.schema.json
policies:
  - policy/source_role.rego
  - policy/rights.rego
  - policy/sensitivity.rego
fixtures:
  valid:
    - data/fixtures/hydrology/huc12_public_safe.valid.json
  invalid:
    - data/fixtures/evidence_bundle/missing_ref.invalid.json
emits:
  receipts:
    - RunReceipt
    - ValidationReport
    - PolicyDecision
  candidates:
    - ReleaseManifest
    - RollbackReference
outcomes:
  - PASS
  - QUARANTINE
  - ABSTAIN
  - DENY
  - ERROR
publication_performed: false
```

[Back to top](#top)

---

## Quickstart

### 1. Inspect before running

```bash
# From the repository root.
git status --short
git branch --show-current

# Confirm this directory and adjacent governance surfaces exist.
find pipelines -maxdepth 2 -type f | sort
find docs schemas contracts policy data tools tests -maxdepth 2 -type f 2>/dev/null | sort | head -200
```

### 2. Prefer no-network dry-runs first

```bash
# PROPOSED placeholder.
# Replace with the repo-native command after package manager and runner conventions are verified.

python pipelines/hydrology_huc12_dryrun/run.py --dry-run --no-network
```

### 3. Run validators before widening trust

```bash
# PROPOSED placeholders.
# Use repo-native wrappers if they exist.

python tools/validators/validate_source_registry.py --fixtures data/fixtures
python tools/validators/validate_evidence_bundle.py --fixtures data/fixtures/evidence_bundle
python tools/validators/validate_layer_manifest.py --fixtures data/fixtures
```

> [!WARNING]
> Do not run live fetches, source watchers, bulk tile generation, release publishing, or destructive cleanup until source rights, endpoint behavior, credentials, policy gates, rollback, and CI expectations are verified.

[Back to top](#top)

---

## Validation gates

Pipeline work is not ready for public-facing use until gates pass at the correct risk level.

| Gate | Required evidence | Fail-closed outcome |
|---|---|---|
| Source admission | Descriptor exists, source role is declared, rights and cadence are reviewed | Reject, defer, or quarantine |
| Schema | Valid and invalid fixtures exercise expected shape | Block merge or promotion |
| Source-role | Observation, model, regulatory, documentary, derived, and generalized roles stay distinct | Quarantine or deny unsupported claim |
| Rights | License, terms, attribution, redistribution, and access class are known | Block public release |
| Sensitivity | Exact-location, cultural, living-person, restricted, or critical infrastructure exposure is classified | Redact, generalize, restrict, or deny |
| Spatial | CRS, geometry validity, support, and precision are meaningful | Hold in `WORK` or `QUARANTINE` |
| Temporal | Time basis, effective date, observation date, or validity interval is explicit | Hold or abstain |
| Evidence closure | `EvidenceRef` resolves to `EvidenceBundle` for consequential claims | Runtime must abstain, deny, or error |
| Catalog/proof | Catalog, provenance, receipts, release manifest, and rollback references cross-link | Block promotion |
| Public boundary | No public route reads `RAW`, `WORK`, `QUARANTINE`, or canonical/internal stores directly | Block release |

### Definition of done for a first pipeline slice

- [ ] Repo conventions inspected and documented.
- [ ] Pipeline has a local README with status, owner, inputs, exclusions, and rollback.
- [ ] Source descriptors are present and inactive unless rights/endpoints are verified.
- [ ] Valid and invalid fixtures run without network access.
- [ ] Pipeline emits or simulates `RunReceipt`, `ValidationReport`, and `PolicyDecision`.
- [ ] No public raw/work/quarantine path exists.
- [ ] No release or publication occurs in the first dry-run.
- [ ] Rollback is a documented reference, not an afterthought.
- [ ] CI command is repo-native or clearly marked `NEEDS VERIFICATION`.

[Back to top](#top)

---

## Pipeline families

| Family | Status | Description | First safe slice |
|---|---|---|---|
| Documentation/control-plane pipelines | **PROPOSED** | Check source ledgers, authority registers, ADR links, and README completeness | no-network doc lint and link inventory |
| Schema/contract pipelines | **PROPOSED** | Validate object shapes and fixture coverage | `SourceDescriptor`, `EvidenceBundle`, `PolicyDecision` |
| Source registry pipelines | **PROPOSED** | Validate source role, activation state, rights, cadence, support, and citation fields | inactive descriptor validation |
| Domain dry-runs | **PROPOSED** | Prove one lane without live source activation | hydrology HUC12 public-safe fixture |
| Catalog/proof pipelines | **PROPOSED** | Build catalog/provenance/proof closure | dry-run `ReleaseManifest` and rollback reference |
| API/UI payload pipelines | **PROPOSED** | Validate `LayerManifest`, `EvidenceDrawerPayload`, and `FocusModePayload` | fixture-only payload examples |
| Release dry-runs | **PROPOSED** | Rehearse promotion without publication | `publication_performed: false` |

[Back to top](#top)

---

## Operating rules

### Pipelines may

- read declared inputs from governed lifecycle homes,
- produce stage outputs with receipts,
- create dry-run promotion candidates,
- write validation reports,
- write public-safe derived artifacts only after gates,
- and fail closed with reviewable reason codes.

### Pipelines must not

- publish directly from `RAW`, `WORK`, or `QUARANTINE`,
- let source availability substitute for rights review,
- let a map layer imply a supported claim,
- let generated language substitute for `EvidenceBundle`,
- write secrets to receipts or logs,
- silently downgrade geometry precision without a transform receipt,
- or turn a derived graph, tile, search index, summary, or scene into sovereign truth.

[Back to top](#top)

---

## FAQ

### Can a pipeline write directly to `PUBLISHED`?

No. Publication is a governed state transition. A pipeline may prepare a candidate and proof package, but promotion requires validators, policy, review state, release manifest, and rollback target.

### Can a pipeline call a live source?

Only after a source descriptor, rights posture, endpoint behavior, cadence, attribution, credentials, failure mode, and source-role policy are verified. The default first slice should be fixture-first and no-network.

### Can a pipeline call an AI model?

Only as an evidence-subordinate, governed operation. Model output cannot become root truth, cannot bypass `EvidenceRef -> EvidenceBundle`, and must emit bounded outcomes or receipts when used.

### Can the UI read pipeline outputs directly?

Public and ordinary UI clients should use governed APIs and released artifacts. Pipeline internals, `RAW`, `WORK`, `QUARANTINE`, canonical stores, and unpublished candidate outputs are not normal public paths.

[Back to top](#top)

---

## Open questions

| Question | Status | Why it matters |
|---|---|---|
| Where is the canonical repo and active branch? | **UNKNOWN** | Required before path claims become implementation claims |
| Does `pipelines/` already exist, and what does it contain? | **UNKNOWN** | Needed before revising rather than creating |
| What package manager and language stack are authoritative? | **UNKNOWN** | Determines runnable quickstart and CI commands |
| Is `schemas/contracts/v1/` the final machine schema home? | **NEEDS VERIFICATION** | Avoids contract/schema drift |
| Which CI workflows already exist? | **UNKNOWN** | Prevents speculative workflow names |
| Who owns pipeline review and release approval? | **TODO** | Required for separation of duty and review accountability |
| Which source families have verified rights and terms? | **NEEDS VERIFICATION** | Blocks live connector activation and public release |
| Where are receipts, proofs, and releases emitted today? | **UNKNOWN** | Prevents invented artifact paths |

[Back to top](#top)

---

## Appendix

<details>
<summary><strong>Suggested review prompt for new pipeline PRs</strong></summary>

Use this prompt during review:

```text
Does this pipeline preserve RAW -> WORK/QUARANTINE -> PROCESSED -> CATALOG/TRIPLET -> PUBLISHED?

Does it declare:
- source role,
- lifecycle transition,
- input and output homes,
- schemas,
- policies,
- fixtures,
- receipts,
- evidence closure,
- sensitivity handling,
- rights posture,
- rollback target,
- and finite failure outcomes?

Does it avoid:
- direct public reads from RAW/WORK/QUARANTINE,
- live fetch without descriptor and rights review,
- publication without promotion,
- AI or renderer ownership of truth,
- secret leakage,
- and unsupported claims?
```

</details>

<details>
<summary><strong>Glossary</strong></summary>

| Term | Meaning |
|---|---|
| `SourceDescriptor` | Declares source identity, role, rights, cadence, support, activation state, and citation obligations. |
| `EvidenceRef` | A reference that must resolve to an `EvidenceBundle` before consequential claims are released. |
| `EvidenceBundle` | Inspectable support package for claims, layers, Focus outputs, exports, or review actions. |
| `PolicyDecision` | Decision record for rights, sensitivity, release eligibility, obligations, or denial. |
| `RunReceipt` | Process memory for a pipeline run: inputs, versions, hashes, tools, outcomes, and timestamps. |
| `ValidationReport` | Machine or reviewer-readable result of schema, policy, source-role, spatial, temporal, or catalog checks. |
| `ReleaseManifest` | Release-facing manifest that binds promoted artifacts, digests, evidence, and rollback/correction references. |
| `LayerManifest` | Map-layer contract that connects data source, business meaning, evidence route, freshness, policy, and review state. |
| `FocusModePayload` | Evidence-bounded synthesis payload with finite outcomes such as `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`. |

</details>

[docs-pipeline-lifecycle]: ../docs/architecture/pipeline-lifecycle.md
[schemas-contracts]: ../schemas/contracts/v1/
[data-registry]: ../data/registry/
[data-fixtures]: ../data/fixtures/
[policy]: ../policy/
[validators]: ../tools/validators/
[data-processed]: ../data/processed/
[data-catalog]: ../data/catalog/
[data-triplets]: ../data/triplets/
[data-receipts]: ../data/receipts/
[data-proofs]: ../data/proofs/
[release]: ../release/
[governed-api]: ../apps/governed-api/
[web-app]: ../apps/web/
