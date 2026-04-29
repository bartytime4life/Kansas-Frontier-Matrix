<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TODO-uuid-pipelines-ecology-readme
title: Ecology Pipeline
type: standard
version: v1
status: draft
owners: TODO(verify pipeline/ecology owner or CODEOWNERS)
created: 2026-04-29
updated: 2026-04-29
policy_label: TODO(verify public|restricted)
related: [../../README.md, ../README.md, ../habitat_layer_build/README.md, ../kansas_biodiversity_etl/README.md, ../../data/README.md, ../../policy/README.md, ../../schemas/README.md]
tags: [kfm, pipelines, ecology, biodiversity, remote-sensing, evidence, governance]
notes: [doc_id owners and policy_label require repository verification, intended replacement for a placeholder ecology README, hls_landsat_ingest.py behavior remains UNKNOWN until implemented and tested, active checkout and CI wiring must be verified before merge]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Ecology Pipeline

<p align="center">
  <strong>Ecology-context execution lane for reviewable, evidence-bound environmental derivatives.</strong><br>
  Evidence-first • map-first • time-aware • policy-aware • fail-closed
</p>

<p align="center">
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-8250df">
  <img alt="Surface: pipelines/ecology" src="https://img.shields.io/badge/surface-pipelines%2Fecology-0b7285">
  <img alt="Evidence: cite or abstain" src="https://img.shields.io/badge/evidence-cite--or--abstain-1f6feb">
  <img alt="Policy: fail closed" src="https://img.shields.io/badge/policy-fail--closed-c92a2a">
  <img alt="Release: not published" src="https://img.shields.io/badge/release-not%20published-6f42c1">
  <img alt="Runtime: needs verification" src="https://img.shields.io/badge/runtime-needs%20verification-d29922">
</p>

<p align="center">
  <a href="#scope">Scope</a> ·
  <a href="#repo-fit">Repo fit</a> ·
  <a href="#accepted-inputs">Inputs</a> ·
  <a href="#exclusions">Exclusions</a> ·
  <a href="#lifecycle-map">Lifecycle</a> ·
  <a href="#minimum-ecology-pipeline-contract">Contract</a> ·
  <a href="#quickstart">Quickstart</a> ·
  <a href="#validation-gates">Validation</a> ·
  <a href="#definition-of-done">Done</a>
</p>

> [!IMPORTANT]
> `pipelines/ecology/` is **not** a publication grant and not a public ecology truth surface.
> It may prepare ecology-context candidates, dry-runs, receipts, validation reports, and review handoffs. Public release still requires governed evidence closure, policy decisions, review state, release manifest, and rollback or correction references.

| Field | Value |
|---|---|
| **Status** | `draft` / `experimental` |
| **Owners** | `TODO(verify pipeline/ecology owner or CODEOWNERS)` |
| **Path** | `pipelines/ecology/README.md` |
| **Document role** | Directory README and operating contract for the ecology pipeline lane. |
| **Current evidence boundary** | `CONFIRMED`: this document defines the intended lane contract. `NEEDS VERIFICATION`: active checkout, branch state, adjacent links, script behavior, package runner, CI wiring, source descriptors, emitted artifacts, and public-route boundaries. |
| **Primary placeholder** | [`hls_landsat_ingest.py`][script-placeholder], treated as placeholder-only until implementation and tests prove behavior. |
| **Public posture** | Cite-or-abstain; fail closed on unresolved rights, sensitivity, source role, support scale, EvidenceRef resolution, or publication review. |
| **Lifecycle invariant** | `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED`. |

| What this document does | What it does not do |
|---|---|
| Defines the lane boundary for ecology-context processing. | Does not prove current runtime behavior. |
| Lists acceptable inputs, exclusions, validation gates, and handoff expectations. | Does not authorize live fetches, public tiles, or public claims. |
| Documents how ecology outputs should remain evidence-bound and policy-aware. | Does not let remote-sensing context become species occurrence truth. |
| Gives maintainers a merge/readiness checklist. | Does not replace parent pipeline, data, schema, policy, catalog, release, or UI contracts. |

---

## Scope

`pipelines/ecology/` is the execution-facing home for ecology-context pipeline work that is broader than a single species-occurrence ETL and narrower than KFM-wide ecological doctrine.

It is intended for fixture-first and source-described processing of ecological context inputs such as remote-sensing products, vegetation-index context, land-cover context, ecological condition indicators, and public-safe derivatives that may support later habitat, flora, fauna, agriculture, hydrology, or hazards interpretation.

### At a glance

| Question | Ecology pipeline answer |
|---|---|
| What is this lane allowed to do? | Prepare reviewable ecology-context artifacts from declared inputs, fixtures, source descriptors, and prior-stage lifecycle material. |
| What is this lane not allowed to do? | Publish sensitive locations, infer species presence from context alone, bypass rights review, or let a map layer stand in for evidence. |
| What is the current script status? | `hls_landsat_ingest.py` is treated as a placeholder; runtime behavior remains `UNKNOWN` until implemented and tested. |
| What lifecycle invariant applies? | `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED`. |
| What should fail closed? | Unknown rights, unknown sensitivity, missing source role, missing support scale, unresolved EvidenceRef, exact sensitive geometry, and unreviewed public release. |

### Lane boundaries

`ecology/` should coordinate with adjacent lanes instead of absorbing them.

| Adjacent lane | Relationship | Boundary rule |
|---|---|---|
| [`../habitat_layer_build/README.md`][habitat-pipeline] | Builds habitat layer candidates from governed habitat inputs. | Ecology may provide context dependencies; habitat layer claims still need habitat-specific source roles and gates. |
| [`../kansas_biodiversity_etl/README.md`][biodiversity-pipeline] | Handles Kansas biodiversity occurrence ETL and geoprivacy-heavy publication logic. | Ecology must not treat occurrence records as public ecological context unless biodiversity policy allows it. |
| [`../README.md`][pipelines-readme] | Defines the shared pipeline contract. | Ecology inherits pipeline lifecycle, no-network-first, evidence-closure, and no-public-raw-path rules. |

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Repo fit

`pipelines/ecology/` sits under the governed execution surface. It should stay thin, reviewable, and subordinate to data lifecycle, schemas/contracts, policy, validation, release, and governed runtime surfaces.

### Upstream and adjacent surfaces

| Surface | Relationship | Verification status |
|---|---|---|
| [`../../README.md`][root-readme] | Root KFM identity, truth path, map/AI boundaries, and inspectable-claim posture. | `NEEDS VERIFICATION` in the active checkout before merge. |
| [`../README.md`][pipelines-readme] | Parent pipeline rules, lifecycle map, accepted inputs, exclusions, validation gates, and definition of done. | `NEEDS VERIFICATION`; update if this lane changes shared commands or object families. |
| [`../../data/README.md`][data-readme] | Lifecycle storage, registry, fixtures, raw/work/quarantine/processed/catalog/proofs/published boundaries. | `NEEDS VERIFICATION`; this lane must not redefine storage authority. |
| [`../../policy/README.md`][policy-readme] | Rights, sensitivity, release, source-role, review, and runtime decision logic. | `NEEDS VERIFICATION`; policy must remain inspectable and testable. |
| [`../../schemas/README.md`][schemas-readme] | Parent schema lane and schema-home ambiguity guardrail. | `NEEDS VERIFICATION`; do not create parallel schema authority. |
| [`./hls_landsat_ingest.py`][script-placeholder] | Current ecology script placeholder. | `UNKNOWN` behavior until inspected, implemented, and tested. |

### Downstream consumers

| Consumer | Allowed relationship |
|---|---|
| Governed API | May consume only released or policy-safe artifacts with EvidenceBundle linkage. |
| MapLibre shell / Evidence Drawer | May display released ecology-context layers with source role, freshness, support scale, review state, policy state, and limitations. |
| Focus Mode / governed AI | May synthesize only over released, evidence-resolved, policy-checked context; it must abstain or deny otherwise. |
| Habitat, flora, fauna, agriculture, hydrology, hazards lanes | May consume ecology-context artifacts as dependencies, never as silent replacement truth. |

> [!WARNING]
> Public clients and routine UI surfaces must not read this pipeline’s `RAW`, `WORK`, `QUARANTINE`, local scratch outputs, or unpublished candidates directly.

### Neighbor update hooks

Update or cross-link neighboring docs when this lane changes shared behavior.

| Change in ecology lane | Neighbor doc likely affected |
|---|---|
| New lifecycle transition, source family, or object family | [`../README.md`][pipelines-readme] and [`../../data/README.md`][data-readme] |
| New schema or contract expectation | [`../../schemas/README.md`][schemas-readme] or confirmed schema-home ADR |
| New rights, sensitivity, or source-role rule | [`../../policy/README.md`][policy-readme] |
| New public layer, Evidence Drawer payload, or Focus Mode context | governed API / UI docs after active path verification |
| Any candidate that can supersede public artifacts | release docs, rollback docs, and correction records |

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Accepted inputs

Inputs belong here only when they can be described, reproduced, validated, and reviewed.

| Input class | Belongs here when… | Required posture |
|---|---|---|
| `SourceDescriptor` / source intake records | The pipeline needs source role, source family, rights, cadence, access posture, and activation state. | Required before live source activation. |
| No-network fixtures | The lane needs a small reproducible test before live fetching or broad processing. | Preferred first slice. |
| Public-safe remote-sensing or ecology-context samples | The sample is clipped, synthetic, already admitted, or fixture-bounded. | Must include CRS, support scale, temporal scope, checksum, and source role. |
| Prior-stage lifecycle artifacts | The pipeline consumes governed `RAW`, `WORK`, `QUARANTINE`, or `PROCESSED` material through declared paths. | Must preserve stage provenance and not upgrade release state by placement. |
| Build configuration | The run defines AOI, time window, transform, masks, index family, output family, and dependency refs. | Must be versioned or hashable where practical. |
| Validation and review records | The run needs to show why a candidate passed, failed, generalized, or stayed in quarantine. | Must use stable outcomes and reason codes. |
| Redaction or generalization receipts | A transform reduces or withholds sensitive precision. | Required before any public-safe derivative can claim a sensitivity transform. |

### Minimum source fields

```json
{
  "source_id": "TODO-verify-source-id",
  "source_family": "remote_sensing_context | land_cover_context | ecology_fixture | TODO",
  "source_role": "context | observation | model | derived | generalized | TODO",
  "retrieved_at": "ISO8601-or-fixture-created-at",
  "rights_posture": "TODO-verify",
  "sensitivity_posture": "TODO-verify",
  "crs": "TODO-verify",
  "temporal_scope": "TODO-verify",
  "support_resolution": "TODO-verify",
  "publication_intent": "dry_run_only | candidate | TODO"
}
```

> [!NOTE]
> A source being public or machine-readable does not make it automatically publishable. Rights, sensitivity, source role, temporal support, spatial support, and review state still control release.

### Acceptance test for a new input

An input is not ready for pipeline use until a reviewer can answer all of these without guessing.

- [ ] What is the source identity and source role?
- [ ] What rights, attribution, redistribution, and access terms apply?
- [ ] What sensitivity or exact-location risk applies?
- [ ] What spatial support, CRS, extent, and precision class apply?
- [ ] What temporal scope, product time, retrieval time, and valid time apply?
- [ ] What lifecycle stage is the input entering from?
- [ ] What output stage is being attempted?
- [ ] Which policy gates can block it?
- [ ] What evidence or receipt will be emitted if it passes or fails?

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Exclusions

Do not put these in `pipelines/ecology/`.

| Excluded item | Why it does not belong | Put it here instead |
|---|---|---|
| Raw source dumps, archives, rasters, or bulk provider payloads | Lifecycle storage belongs outside executable pipeline definitions. | `../../data/raw/` after source intake. |
| Work-in-progress transformed artifacts as durable truth | Pipeline scratch output is not public evidence. | `../../data/work/` or `../../data/quarantine/`. |
| Released public artifacts or public aliases | Publication is a governed transition, not a folder copy. | `../../release/` and release-backed `../../data/published/` surfaces. |
| Secrets, API keys, cookies, tokens, private service URLs | Pipeline definitions must remain safe to review. | Secret manager or deployment configuration outside repo-visible docs. |
| Canonical schema definitions embedded only in this lane | Schemas must remain reusable and validator-addressable. | `../../schemas/` or `../../contracts/` after schema-home decision. |
| Policy allow/deny semantics hidden in script conditionals | Policy must stay inspectable, testable, and deny-by-default. | `../../policy/` plus tests. |
| Biodiversity occurrence publication | Occurrence records carry geoprivacy, rights, and steward-access burdens. | [`../kansas_biodiversity_etl/README.md`][biodiversity-pipeline] and domain policy. |
| Habitat layer publication | Habitat candidates require habitat-specific support, source-role, and release checks. | [`../habitat_layer_build/README.md`][habitat-pipeline]. |
| Exact sensitive species, rare-plant, nest, den, roost, archaeological, cultural, or steward-controlled locations | Exact public exposure can create ecological, cultural, legal, or institutional harm. | Restricted steward lanes, redaction/generalization transforms, or `../../data/quarantine/`. |
| UI popups, MapLibre styles, or public API routes | Public clients should consume governed release-safe payloads, not pipeline internals. | `../../apps/`, `../../packages/`, and governed API contracts after verification. |
| Free-form AI summaries as pipeline output truth | AI is interpretive and cannot manufacture evidence or release state. | Governed AI runtime envelopes after EvidenceBundle and policy checks. |

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Directory tree

### Expected lane inventory to verify

```text
pipelines/ecology/
├── README.md              # directory contract and orientation surface
└── hls_landsat_ingest.py  # placeholder until behavior is implemented and tested
```

### Proposed implementation shape

The shape below is a target layout only. Do not create or rename files until the active checkout, package runner, and repo conventions are verified.

```text
pipelines/ecology/
├── README.md
├── hls_landsat_ingest.py
├── config/
│   └── ecology_context.example.yaml
├── fixtures/
│   ├── good/
│   │   └── ecology_context_candidate.valid.json
│   └── bad/
│       ├── missing_source_role.invalid.json
│       ├── missing_support_resolution.invalid.json
│       ├── unknown_rights.invalid.json
│       └── exact_sensitive_geometry.invalid.json
├── harvest/
│   └── README.md
├── normalize/
│   └── README.md
├── validate/
│   └── README.md
├── emit/
│   └── README.md
└── outputs/
    └── .gitkeep           # working output only; public release belongs outside this lane
```

### Placement rule

If executable code belongs in a central package or tool directory after active-checkout inspection, keep this README as the lane index and move implementation to the confirmed package home. Do not let a convenient script location become hidden contract authority.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Lifecycle map

```mermaid
flowchart LR
    SD[SourceDescriptor<br/>source role + rights + cadence] --> AD{Admission gate}
    FIX[No-network fixture<br/>or admitted ecology input] --> RAW[RAW]
    RAW --> WORK[WORK<br/>normalize / mask / derive context]
    AD -->|pass| WORK
    AD -->|fail| Q[QUARANTINE<br/>reason-coded hold]

    WORK --> VAL{Validation gates}
    VAL -->|fail| Q
    VAL -->|pass| PROC[PROCESSED<br/>ecology-context candidate]

    PROC --> CAT[CATALOG / TRIPLET<br/>catalog + provenance refs]
    PROC --> RCPT[RunReceipt<br/>spec_hash + inputs + outputs]
    CAT --> EB[EvidenceBundle candidate]
    RCPT --> EB

    EB --> PD{PromotionDecision}
    PD -->|approved| PUB[PUBLISHED<br/>release-backed artifact]
    PD -->|blocked| Q

    PUB --> API[Governed API]
    API --> UI[MapLibre / Evidence Drawer / Focus Mode]

    UI -. forbidden normal path .-> RAW
    UI -. forbidden normal path .-> WORK
    UI -. forbidden normal path .-> Q
```

The critical boundary is between `PROCESSED` and `PUBLISHED`: this lane may prepare candidates, receipts, validation reports, and evidence refs, but it does not make the release decision by itself.

### Stage responsibilities

| Stage | Ecology lane responsibility | Public visibility |
|---|---|---|
| `RAW` | Receive admitted source material through source intake rules. | Not public. |
| `WORK` | Normalize, mask, derive, and inspect intermediate artifacts. | Not public. |
| `QUARANTINE` | Hold failed, sensitive, rights-unclear, or review-blocked artifacts with reason codes. | Not public except governed review surfaces. |
| `PROCESSED` | Produce reviewable ecology-context candidates and validation outputs. | Not public by default. |
| `CATALOG / TRIPLET` | Attach catalog/provenance/evidence references for review and traceability. | Not public unless promotion approves. |
| `PUBLISHED` | Release-backed artifact with manifest, policy decision, evidence closure, and rollback target. | Public or semi-public according to release and policy state. |

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Minimum ecology pipeline contract

Every ecology pipeline run should be able to answer these questions before it can support a public-facing claim.

| Contract question | Required answer |
|---|---|
| What lifecycle transition is attempted? | Example: `RAW -> WORK`, `WORK -> PROCESSED`, or `PROCESSED -> CATALOG_CANDIDATE`. |
| What source role is being used? | Context, observation, model, derived, generalized, steward-reviewed, or other typed role. |
| What spatial support applies? | CRS, extent, support resolution, geometry validity, nodata/mask rules, and precision class. |
| What temporal support applies? | Observed time, source time, valid time, retrieval time, or product time window. |
| What evidence supports visible claims? | `EvidenceRef -> EvidenceBundle` closure or explicit `ABSTAIN` / `DENY` / `ERROR`. |
| Which policies apply? | Rights, sensitivity, source-role, publication, no-bypass, correction, and rollback policy refs. |
| What does the run emit? | `RunReceipt`, `ValidationReport`, candidate `LayerManifest`, catalog refs, and rollback/correction refs where applicable. |
| What is the finite outcome? | `PASS`, `HOLD`, `QUARANTINE`, `ABSTAIN`, `DENY`, or `ERROR`. |

### Illustrative manifest shape

```yaml
# ILLUSTRATIVE EXAMPLE — PROPOSED, not confirmed repo schema
pipeline_id: ecology_context_dryrun
status: proposed
owner: TODO(verify pipeline/ecology owner)
network: disabled
publication_performed: false

lifecycle_transition:
  from: RAW
  to: PROCESSED_CANDIDATE

source_descriptors:
  - data/registry/sources/ecology/TODO.source.json

schemas:
  - schemas/contracts/v1/source/source_descriptor.schema.json
  - schemas/contracts/v1/evidence/evidence_bundle.schema.json
  - schemas/contracts/v1/policy/decision_envelope.schema.json
  - schemas/contracts/v1/release/release_manifest.schema.json

policies:
  - policy/source_role.rego
  - policy/rights.rego
  - policy/sensitivity.rego
  - policy/public_boundary.rego

fixtures:
  valid:
    - pipelines/ecology/fixtures/good/ecology_context_candidate.valid.json
  invalid:
    - pipelines/ecology/fixtures/bad/unknown_rights.invalid.json
    - pipelines/ecology/fixtures/bad/exact_sensitive_geometry.invalid.json

emits:
  receipts:
    - RunReceipt
    - ValidationReport
    - PolicyDecision
  candidates:
    - LayerManifest
    - CatalogRefs
    - RollbackReference

outcomes:
  - PASS
  - HOLD
  - QUARANTINE
  - ABSTAIN
  - DENY
  - ERROR
```

### Candidate output contract

| Field | Required? | Why it matters |
|---|---:|---|
| `ecology_candidate_id` | Yes | Stable candidate reference for review and rollback. |
| `source_descriptor_refs` | Yes | Evidence, rights, and source-role traceability. |
| `source_roles` | Yes | Prevents semantic role collapse. |
| `input_artifact_refs` | Yes | Supports rebuild and rollback. |
| `spec_hash` | Yes | Deterministic identity for transform configuration. |
| `crs` | Yes | Spatial correctness. |
| `extent` | Yes | Spatial scope. |
| `temporal_scope` | Yes | Time-aware claim boundary. |
| `support_resolution` | Yes | Prevents overclaiming precision. |
| `limitations` | Yes | Evidence Drawer and API disclosure. |
| `validation_report_ref` | Yes | Gate auditability. |
| `run_receipt_ref` | Yes | Process memory. |
| `catalog_refs` | When release candidate | Catalog closure. |
| `evidence_bundle_ref` | When release candidate | Claim traceability. |
| `rollback_ref` | When superseding or publishing | Reversible change. |

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Source-role guardrails

Ecology-context products must keep source roles visible. A context layer is not an observation record, a model is not a legal designation, and a map layer is not proof by itself.

| Source role | Can support | Cannot support |
|---|---|---|
| `remote_sensing_context` | Contextual environmental condition, change, or index claims when source/time/support are clear. | Species presence, legal habitat designation, or exact ecological cause by itself. |
| `land_cover_context` | Landscape class context and coarse habitat-adjacent interpretation. | Occurrence proof, habitat preference truth, or regulatory status. |
| `vegetation_index_context` | Vegetation condition or anomaly context with limitations visible. | Field-confirmed ecological condition without corroborating evidence. |
| `modeled_ecology_context` | Model-bounded context where model identity, parameters, limitations, and validation are visible. | Observation truth, regulatory claims, or exact public location claims. |
| `generalized_public_derivative` | Public-safe summarized or generalized context after transform receipt. | Restricted exact geometry, steward-only evidence, or hidden sensitive-source reconstruction. |
| `biodiversity_occurrence_dependency` | Dependency linkage to governed occurrence records when biodiversity policy allows. | Direct public exposure or inferred habitat truth without occurrence-lane gates. |

> [!CAUTION]
> Ecology-context layers can make false precision look authoritative. When support scale, uncertainty, masking, or source role is unclear, hold the artifact or force `ABSTAIN` rather than letting a renderer or model make an unsupported claim.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Quickstart

These commands are safe orientation commands. They do not prove runtime readiness.

### 1. Inspect the active checkout

```bash
# Run from repository root.
git status --short
git branch --show-current

# Confirm the current ecology lane contents.
find pipelines/ecology -maxdepth 2 -type f | sort
wc -l pipelines/ecology/README.md pipelines/ecology/hls_landsat_ingest.py
```

### 2. Check placeholder status without running a live ingest

```python
from pathlib import Path

required = [
    Path("pipelines/ecology/README.md"),
    Path("pipelines/ecology/hls_landsat_ingest.py"),
]

for path in required:
    if not path.exists():
        raise SystemExit(f"missing required ecology lane file: {path}")
    print(f"{path}: {path.stat().st_size} bytes")

print("Ecology lane inventory check complete. Runtime behavior still requires implementation evidence.")
```

### 3. Do not run live fetches until gates are ready

```bash
# PROPOSED ONLY — replace with repo-native command after implementation.
# The first real command should be fixture-first and no-network.
python pipelines/ecology/hls_landsat_ingest.py --dry-run --no-network
```

> [!WARNING]
> Do not run live remote-sensing harvests, bulk raster processing, broad tile generation, public release, or destructive cleanup until source descriptors, rights, endpoint behavior, credentials, sensitivity policy, rollback, and CI expectations are verified.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Validation gates

| Gate | Required evidence | Fail-closed outcome |
|---|---|---|
| Source admission | Descriptor exists; source role, rights, cadence, access posture, and activation state are declared. | `HOLD`, `QUARANTINE`, or `DENY`. |
| Rights | License, source terms, attribution, redistribution posture, and access class are known. | Block public release. |
| Sensitivity | Exact-location, rare-species, restricted, steward-controlled, cultural, or critical exposure is classified. | Redact, generalize, restrict, embargo, quarantine, or deny. |
| Source-role semantics | Context layers, observations, modeled surfaces, detections, and derived products stay distinct. | Abstain or deny unsupported claims. |
| Spatial support | CRS, extent, geometry/raster validity, support resolution, nodata/masks, and precision class are explicit. | Hold in `WORK` or `QUARANTINE`. |
| Temporal support | Observation/product/retrieval/valid-time windows are explicit. | Hold or abstain. |
| Evidence closure | Consequential claims resolve from `EvidenceRef` to `EvidenceBundle`. | Runtime must `ABSTAIN`, `DENY`, or `ERROR`. |
| Catalog/proof closure | Catalog refs, provenance refs, validation reports, receipts, release candidate refs, and rollback refs cross-link. | Block promotion. |
| Public boundary | No public route reads `RAW`, `WORK`, `QUARANTINE`, or unpublished candidates. | Block release. |
| Correction readiness | Supersession, rollback, or withdrawal target is recorded when an artifact can affect public claims. | Block promotion or mark candidate `HOLD`. |

### Negative test fixtures to add first

| Fixture | Expected outcome | Reason |
|---|---|---|
| `missing_source_role.invalid.json` | `DENY` or `HOLD` | Prevents role collapse. |
| `missing_support_resolution.invalid.json` | `HOLD` | Prevents unsupported precision. |
| `unknown_rights.invalid.json` | `DENY_PUBLIC_RELEASE` | Unknown rights cannot publish. |
| `exact_sensitive_geometry.invalid.json` | `QUARANTINE` or `DENY_PUBLIC_RELEASE` | Exact sensitive geometry fails closed. |
| `unresolved_evidence_ref.invalid.json` | `ABSTAIN` or `ERROR` | Claims cannot expose without EvidenceBundle closure. |
| `direct_public_raw_path.invalid.json` | `DENY` | Public clients must not read pipeline internals. |

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Policy and sensitivity posture

Ecology-context work can expose ecological, cultural, legal, and stewardship risk even when source data appears public. The lane must default to public-safe derivatives, not public exactness.

| Risk class | Default handling |
|---|---|
| Unknown rights or redistribution terms | Block public release; hold until source terms are verified. |
| Unknown sensitivity | Quarantine or restrict; do not assume public-safe. |
| Exact rare-species, nest, den, roost, hibernacula, spawning, rare-plant, or steward-controlled locations | Redact, generalize, restrict, embargo, or deny public output. |
| Cultural, archaeological, or sovereignty-sensitive location context | Quarantine or steward review before public transformation. |
| Unsupported precision | Generalize or abstain from precise claims. |
| Remote-sensing/model uncertainty | Expose limitations in Evidence Drawer and runtime payloads. |
| Live-source volatility | Record retrieval time, product time, source cadence, and freshness state. |

### Public-safe transform receipt

Every public-safe transform should leave a reviewable receipt.

```yaml
# ILLUSTRATIVE EXAMPLE — PROPOSED, not confirmed repo schema
redaction_receipt:
  receipt_id: TODO
  input_artifact_ref: TODO
  output_artifact_ref: TODO
  transform_type: generalization | suppression | rounding | masking | aggregation | embargo
  reason_codes:
    - sensitivity_unknown
    - exact_location_risk
  reviewer: TODO(verify reviewer identity convention)
  created_at: TODO(ISO8601)
  rollback_ref: TODO
```

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Risk register

| Risk | How it appears | Mitigation |
|---|---|---|
| Remote-sensing context becomes occurrence proof | Map popup or AI answer implies species presence from NDVI/land-cover context alone. | Source-role guardrails; EvidenceRef closure; Focus Mode `ABSTAIN` for unsupported claims. |
| Public exact-location exposure | Sensitive feature geometry passes from candidate to layer output. | Sensitivity policy, redaction/generalization receipt, public boundary tests. |
| Rights overconfidence | Public source is treated as freely redistributable. | SourceDescriptor rights fields; unknown rights block public release. |
| Hidden schema authority | Pipeline embeds local JSON shape that drifts from shared schema. | Use confirmed schema home; add ADR if `schemas/` vs `contracts/` is unresolved. |
| Direct public path to pipeline internals | UI or API consumes `outputs/`, `WORK`, or `QUARANTINE` directly. | No-public-raw-path tests; governed API only. |
| Unreviewed live fetching | Placeholder script begins network calls without descriptors or source terms. | No-network-first dry-run; live activation gate. |
| Silent replacement of prior candidates | New derivative overwrites prior artifact or public alias. | `spec_hash`, release manifest, rollback reference, correction lineage. |
| AI or renderer becomes truth source | Focus Mode or MapLibre popup emits claim without evidence bundle. | Governed runtime envelope; citation validation; Evidence Drawer required. |

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Rollback and correction

Any ecology-context output that can affect public interpretation needs a rollback or correction path before promotion.

| Scenario | Required action |
|---|---|
| Candidate fails validation before release | Keep in `WORK` or `QUARANTINE`; emit reason-coded validation report. |
| Candidate supersedes a prior candidate | Preserve prior artifact ref; emit supersession note and rollback ref. |
| Published artifact is later found rights-unsafe | Withdraw or restrict release; record correction notice and rights reason. |
| Published artifact is later found sensitivity-unsafe | Remove or generalize public artifact; record redaction receipt and correction notice. |
| Source data or transform is corrected | Re-run with new `spec_hash`; emit new receipt and correction lineage. |
| EvidenceRef no longer resolves | Block or withdraw dependent public claims until closure is restored. |

### Correction-ready public claim

A public ecology-context claim should be able to answer:

```text
What was claimed?
Which released artifact carried it?
Which EvidenceBundle supported it?
Which source roles were involved?
Which policy decision allowed it?
Which release manifest promoted it?
Which prior artifact or claim did it supersede?
What rollback target exists?
What correction path applies if rights, sensitivity, or evidence changes?
```

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Implementation plan

### Smallest safe first PR

1. Replace the placeholder ecology README with this directory contract.
2. Verify active checkout, branch, file presence, adjacent links, and `hls_landsat_ingest.py` status.
3. Keep `hls_landsat_ingest.py` placeholder-only unless no-network dry-run behavior, fixtures, and tests are added in the same PR.
4. Add or plan tiny public-safe fixtures only after source descriptor and schema-home conventions are verified.
5. Add negative tests for unknown rights, missing source role, missing support resolution, exact sensitive geometry, unresolved EvidenceRef, and public raw-path bypass.
6. Update parent pipeline docs only if shared lane behavior changes.

### Expansion sequence

| Phase | Goal | Exit condition |
|---|---|---|
| Phase 0 | Active checkout and convention verification. | Branch, path, adjacent docs, package runner, schema home, policy home, and test runner are known. |
| Phase 1 | Documentation and no-network fixture slice. | README, source descriptor fixture, valid/invalid candidates, and validation expectations are reviewable. |
| Phase 2 | Placeholder runner or dry-run script. | `--dry-run --no-network` emits deterministic receipt-like output. |
| Phase 3 | Validation and policy gates. | Fixtures pass/fail as expected; public boundary and sensitivity tests exist. |
| Phase 4 | Candidate handoff to catalog/release review. | Candidate manifests, EvidenceBundle refs, policy decisions, and rollback refs are generated or simulated. |
| Phase 5 | Live source activation. | Rights, endpoint behavior, credentials, cadence, attribution, source role, and sensitivity controls are verified. |

> [!TIP]
> Keep each phase reversible. If a change cannot be rolled back cleanly, it is probably too large for the next ecology PR.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Definition of done

This README is ready when a maintainer can inspect `pipelines/ecology/` and quickly determine:

1. what this lane is allowed to process;
2. what `hls_landsat_ingest.py` is allowed or not yet allowed to do;
3. what inputs are acceptable;
4. where outputs belong;
5. which gates block release;
6. what remains unverified;
7. how an ecology-context artifact becomes reviewable evidence instead of an unsupported map or model-derived assertion.

### Merge readiness checklist

- [ ] Active checkout inspected; branch, file sizes, package runner, and target path verified.
- [ ] `doc_id`, owners, policy label, and related links resolved or deliberately left as reviewed placeholders.
- [ ] `hls_landsat_ingest.py` is either documented as placeholder-only or implemented with no-network dry-run support.
- [ ] Source descriptors exist for every source family used by an ecology run.
- [ ] Good and bad fixtures are present, public-safe, no-network, and small enough for review.
- [ ] Negative tests cover unknown rights, missing source role, missing support resolution, exact sensitive geometry, and unresolved EvidenceRef.
- [ ] The pipeline emits or simulates `RunReceipt`, `ValidationReport`, `PolicyDecision`, and candidate manifest refs.
- [ ] No live source activation occurs without rights, endpoint, cadence, attribution, and source-role verification.
- [ ] No public UI/API route reads pipeline internals, `RAW`, `WORK`, `QUARANTINE`, or unpublished candidates.
- [ ] Candidate handoff does not auto-publish or mutate public aliases.
- [ ] Parent [`../README.md`][pipelines-readme] is updated if pipeline family names, commands, gates, or directory shape change.
- [ ] Rollback and correction behavior is documented for any output that can supersede prior candidates.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## FAQ

### Is `pipelines/ecology/` the canonical ecology truth source?

No. It is an execution lane for candidate processing and dry-run evidence. Canonical authority remains with source descriptors, schemas/contracts, policy, catalog/proof objects, review records, and release state.

### Can this lane publish ecological layers?

Not directly. This lane may prepare candidates and proof inputs. Publication requires governed promotion, evidence closure, policy decisions, review state, release manifest, and rollback reference.

### Can `hls_landsat_ingest.py` fetch live sources?

`NEEDS VERIFICATION`. Treat it as placeholder-only until it has a source descriptor, fixture-first dry-run, rights and endpoint verification, no-secret handling, tests, and receipts.

### Can remote sensing prove species presence?

No. Remote-sensing context can help frame ecological interpretation, but species presence, rare-species exposure, occurrence evidence, and steward-controlled data require separate evidence and policy gates.

### Can MapLibre read this pipeline’s work outputs?

No. MapLibre and ordinary UI surfaces should consume governed release-safe artifacts through governed APIs or released layer manifests, never this lane’s `RAW`, `WORK`, `QUARANTINE`, or unpublished candidates.

### What happens if a sensitive input is discovered after processing?

The affected candidate should be held, quarantined, redacted, generalized, restricted, or denied. Any public or semi-public artifact already affected should receive correction, withdrawal, rollback, or supersession handling.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Appendix

<details>
<summary>Review prompt for ecology pipeline PRs</summary>

```text
Does this ecology pipeline preserve RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED?

Does it declare:
- source role,
- rights posture,
- sensitivity posture,
- lifecycle transition,
- input and output homes,
- schemas,
- policies,
- fixtures,
- receipts,
- evidence closure,
- support resolution,
- temporal scope,
- rollback target,
- and finite failure outcomes?

Does it avoid:
- direct public reads from RAW / WORK / QUARANTINE,
- live fetch without descriptor and rights review,
- publication without promotion,
- treating remote-sensing context as species presence proof,
- treating occurrence records as habitat truth,
- AI or renderer ownership of truth,
- secret leakage,
- unsupported precision,
- and silent overwrites of correction history?
```

</details>

<details>
<summary>Glossary</summary>

| Term | Meaning |
|---|---|
| `SourceDescriptor` | Declares source identity, role, rights, cadence, support, activation state, and citation obligations. |
| `EvidenceRef` | A reference that must resolve to an `EvidenceBundle` before consequential claims are exposed. |
| `EvidenceBundle` | Inspectable support package for claims, layers, Focus outputs, exports, or review actions. |
| `PolicyDecision` | Decision record for rights, sensitivity, release eligibility, obligations, or denial. |
| `RunReceipt` | Process memory for a pipeline run: inputs, versions, hashes, tools, outcomes, and timestamps. |
| `ValidationReport` | Machine or reviewer-readable result of schema, policy, source-role, spatial, temporal, or catalog checks. |
| `LayerManifest` | Map-layer contract that connects data source, meaning, evidence route, freshness, policy, and review state. |
| `ReleaseManifest` | Release-facing manifest that binds promoted artifacts, digests, evidence, and rollback/correction references. |
| `RedactionReceipt` | Record of a precision-reducing, withholding, generalization, or public-safety transform. |
| `spec_hash` | Deterministic identity over declared source, schema, transform, policy, and parameter inputs where practical. |

</details>

<details>
<summary>Open verification backlog</summary>

- [ ] Verify the active repository branch and dirty state.
- [ ] Verify whether `pipelines/ecology/README.md` and `pipelines/ecology/hls_landsat_ingest.py` exist in the current checkout.
- [ ] Inspect `hls_landsat_ingest.py` and classify it as placeholder, dry-run runner, live connector, or deprecated script.
- [ ] Verify package runner and test conventions.
- [ ] Verify schema home: `schemas/`, `contracts/`, or another accepted registry.
- [ ] Verify policy home and whether OPA/Rego, Python validators, or another mechanism is accepted.
- [ ] Verify source registry path and source descriptor schema.
- [ ] Verify public API and UI boundary tests that prevent direct reads from pipeline internals.
- [ ] Verify release manifest, proof pack, correction, and rollback object families.
- [ ] Verify owners and CODEOWNERS mapping for `pipelines/ecology/`.

</details>

---

[root-readme]: ../../README.md
[pipelines-readme]: ../README.md
[data-readme]: ../../data/README.md
[policy-readme]: ../../policy/README.md
[schemas-readme]: ../../schemas/README.md
[habitat-pipeline]: ../habitat_layer_build/README.md
[biodiversity-pipeline]: ../kansas_biodiversity_etl/README.md
[script-placeholder]: ./hls_landsat_ingest.py
