<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-agriculture-readme
title: Agriculture Domain Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <agriculture-pipeline-owner>
  - <agriculture-domain-steward>
  - <source-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/domains/agriculture/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - docs/domains/agriculture/ARCHITECTURE.md
  - docs/domains/agriculture/PIPELINE.md
  - docs/domains/agriculture/SOURCES.md
  - docs/domains/agriculture/SOURCE_REGISTRY.md
  - docs/domains/agriculture/sublanes/cropland.md
  - pipeline_specs/agriculture/
  - connectors/usda/nass/
  - connectors/nrcs/ssurgo/
  - connectors/nrcs/scan/
  - connectors/kansas/mesonet/
  - connectors/noaa/uscrn/
  - connectors/nasa/smap/
  - connectors/nasa/hls/
  - contracts/domains/agriculture/
  - schemas/contracts/v1/domains/agriculture/
  - policy/domains/agriculture/
  - policy/sensitivity/agriculture/
  - data/raw/agriculture/
  - data/work/agriculture/
  - data/quarantine/agriculture/
  - data/processed/agriculture/
  - data/catalog/domain/agriculture/
  - data/triplets/agriculture/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/agriculture/
  - release/manifests/agriculture/
tags:
  - kfm
  - pipelines
  - domains
  - agriculture
  - crop
  - cropland
  - irrigation
  - conservation
  - yield
  - stress-indicators
  - aggregation
  - evidence
  - policy
  - governance
notes:
  - "This README replaces the greenfield scaffold for pipelines/domains/agriculture."
  - "Agriculture pipeline logic is executable implementation support only; it does not own object meaning, schemas, source descriptors, policy, lifecycle data, catalog truth, or release decisions."
  - "Agriculture outputs are privacy-, parcel-, operator-, and aggregation-sensitive. Public release defaults to deny or aggregate until EvidenceBundle, AggregationReceipt, PolicyDecision, steward review, ReleaseManifest, and rollback close."
  - "Concrete executable behavior, source activation, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# 🌾 Agriculture Domain Pipeline

> Executable Agriculture-domain pipeline lane for converting admitted agricultural source material into governed candidates, processed records, catalog/triplet handoffs, receipts, and release-review packages — **without bypassing evidence, policy, aggregation, sensitivity, or release gates**.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-agriculture%20domain%20pipeline-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![lifecycle](https://img.shields.io/badge/lifecycle-RAW%E2%86%92PUBLISHED-0a7ea4)
![sensitivity](https://img.shields.io/badge/sensitivity-aggregation%20required-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/agriculture/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Agriculture  
**Placement posture:** agriculture child lane under `pipelines/domains/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; agriculture outputs must pass lifecycle, evidence, aggregation, sensitivity, policy, catalog/triplet, release, correction, and rollback gates

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. What belongs here](#3-what-belongs-here)
- [4. What does not belong here](#4-what-does-not-belong-here)
- [5. Agriculture pipeline scope](#5-agriculture-pipeline-scope)
- [6. Source-family posture](#6-source-family-posture)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Stage responsibilities](#8-stage-responsibilities)
- [9. Required gates](#9-required-gates)
- [10. Sensitivity, aggregation, and public-safety posture](#10-sensitivity-aggregation-and-public-safety-posture)
- [11. Directory contract](#11-directory-contract)
- [12. Inputs and outputs](#12-inputs-and-outputs)
- [13. Minimal agriculture pipeline candidate record](#13-minimal-agriculture-pipeline-candidate-record)
- [14. Dry-run, tests, fixtures, receipts, and proofs](#14-dry-run-tests-fixtures-receipts-and-proofs)
- [15. Promotion, publication, correction, and rollback](#15-promotion-publication-correction-and-rollback)
- [16. Definition of done](#16-definition-of-done)
- [17. Open questions](#17-open-questions)

---

## 1. Purpose

`pipelines/domains/agriculture/` is the executable pipeline lane for Agriculture-domain transformations.

It supports Agriculture objects and candidate products such as:

- crop observations;
- crop progress and condition candidates;
- cropland and field candidates;
- crop rotation and land-use context;
- aggregate yield observations;
- irrigation links;
- conservation-practice context;
- soil-crop suitability candidates;
- vegetation, drought, pest, and stress indicators;
- agricultural-economy observations;
- public-safe, aggregate, release-reviewed products.

This directory implements or will implement the **how** of Agriculture processing. It does not define Agriculture object meaning, policy, schemas, source roles, source descriptors, data storage, or release approval.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/agriculture/`? | Agriculture is a domain lane under the domain-pipeline umbrella. | CONFIRMED path responsibility pattern; executable behavior NEEDS VERIFICATION |
| Where do declarative specs live? | `pipeline_specs/agriculture/` or accepted spec home. | PROPOSED / NEEDS VERIFICATION |
| Where do source fetchers live? | `connectors/<source>/`, not here. | CONFIRMED separation |
| Where do schemas live? | `schemas/contracts/v1/domains/agriculture/` or accepted schema home. | PROPOSED / NEEDS VERIFICATION |
| Where does policy live? | `policy/domains/agriculture/`, `policy/sensitivity/agriculture/`, `policy/rights/`, and `policy/release/` as applicable. | PROPOSED / NEEDS VERIFICATION |
| Where do outputs live? | Lifecycle homes under `data/`, not beside pipeline code. | CONFIRMED lifecycle posture |
| Can this lane publish? | No. It may prepare candidates and release handoffs only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Agriculture pipeline code is subordinate to source descriptors, source roles, rights, aggregation thresholds, EvidenceBundle closure, sensitivity review, policy decisions, release manifests, correction notices, and rollback cards. A successful run is not a public release.

[⬆ Back to top](#top)

---

## 3. What belongs here

Files belong here when their primary responsibility is executable Agriculture-domain processing.

Appropriate contents include:

- fixture-only dry-run entrypoints for Agriculture pipeline behavior;
- Agriculture-specific normalizers;
- Agriculture-specific candidate builders;
- Agriculture-specific aggregation and threshold application helpers, if not centralized elsewhere;
- Agriculture-specific validator wrappers, if not reusable under `tools/`;
- Agriculture-specific catalog/triplet handoff helpers, if not centralized in `pipelines/catalog/`;
- Agriculture-specific receipt emitters, if not shared;
- thin adapters that read governed lifecycle inputs, not live source systems;
- child README or contract files explaining local executable behavior.

A good placement test:

> If the code transforms Agriculture-domain lifecycle inputs into Agriculture candidates, processed records, catalog/triplet handoffs, or receipts, it may belong here. If it fetches source data, defines meaning, defines schema, encodes policy, stores lifecycle data, or approves release, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 4. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| USDA, NRCS, NOAA, NASA, Kansas Mesonet, or other source fetchers | `connectors/<source>/` |
| Source catalog profiles | `docs/sources/catalog/...` |
| Source descriptors / source registry entries | `data/registry/sources/agriculture/` or approved registry home |
| Agriculture architecture / doctrine | `docs/domains/agriculture/...` |
| Agriculture object meaning contracts | `contracts/domains/agriculture/...` |
| JSON Schemas | `schemas/contracts/v1/domains/agriculture/...` |
| Policy bundles or sensitivity rules | `policy/domains/agriculture/`, `policy/sensitivity/agriculture/`, `policy/rights/`, `policy/release/` |
| Declarative run specs | `pipeline_specs/agriculture/...` |
| Fixtures | `fixtures/domains/agriculture/` or accepted fixture home |
| Tests | `tests/pipelines/domains/agriculture/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions | `release/candidates/agriculture/`, `release/manifests/agriculture/`, `release/rollback_cards/`, `release/correction_notices/` |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, `packages/ui/`, `packages/maplibre-runtime/` |

> [!WARNING]
> The previous scaffold wording allowed “docs, contracts, schemas, policies, fixtures, tests, packages, pipelines, registries, or data lifecycle artifacts” here. This README narrows the boundary: **only executable Agriculture pipeline logic belongs here.** The other responsibility roots remain separate authority surfaces.

[⬆ Back to top](#top)

---

## 5. Agriculture pipeline scope

Agriculture pipeline work may include these governed processing responsibilities:

| Scope area | Pipeline responsibility | Publication posture |
|---|---|---|
| Cropland / crop cover | Normalize crop-cover or cropland candidates from admitted sources. | Aggregate or public-safe only after release review. |
| Crop progress / condition | Normalize temporal crop progress observations. | Do not overstate beyond source role and reporting scale. |
| Yield observations | Process aggregate yield observations and supporting metadata. | Field/operator-specific output denied unless explicitly authorized and aggregated. |
| Field candidates | Create candidate geometries only; never publish as parcel/operator truth. | Default restricted / review-required. |
| Irrigation links | Connect agricultural context with water-use or hydrologic context where allowed. | Sensitive/private implications require review. |
| Soil-crop suitability | Compose Agriculture with Soil under scale and source-role limits. | Suitability is interpretive; must cite evidence or abstain. |
| Conservation context | Normalize conservation-practice indicators and restoration-adjacent context. | Avoid private-operation inference. |
| Stress indicators | Prepare drought, pest, vegetation, or hazard-linked stress candidates. | Derived, not emergency/regulatory/crop-loss truth. |
| Agricultural economy | Aggregate economic observations and context. | Aggregate only; private/operator-resolvable data denied by default. |

[⬆ Back to top](#top)

---

## 6. Source-family posture

Agriculture pipeline code may consume only admitted or fixture-bound source material.

Candidate source families named in Agriculture docs include, but are not limited to:

- USDA NASS / CDL-style crop and cropland products;
- NRCS SSURGO / soil context where Agriculture has a governed join;
- NRCS SCAN-style soil moisture or station context where admitted;
- Kansas Mesonet-style weather/agricultural climate context where admitted;
- NOAA climate or station context where admitted;
- NASA SMAP / HLS or other remote-sensing context where admitted;
- local upload or steward-curated material only through source-descriptor and rights gates.

This README does not activate any source. Each source family requires a SourceDescriptor, source role, rights posture, cadence, sensitivity classification, attribution, fixtures, and validation before use.

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Agriculture pipeline must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal Agriculture pipeline stance:

1. **Read** approved fixtures, immutable raw captures, work candidates, quarantine inputs in remediation mode, or prior processed baselines.
2. **Normalize** into Agriculture work candidates with source role, rights, temporal scope, spatial scope, aggregation status, evidence references, and sensitivity posture.
3. **Quarantine** unresolved rights, source-role mismatch, schema drift, sensitivity risk, field/operator-resolvable records, over-precise geometry, or validation failures.
4. **Promote to processed** only after validation, policy, evidence, aggregation, and reviewer gates appropriate to significance.
5. **Prepare catalog/triplet handoffs** only after processed-state and evidence closure.
6. **Publish** only through release decisions, public-safe artifacts, rollback targets, and correction paths.

Do not treat a move from one lifecycle folder to another as promotion. Promotion is a governed state transition with receipts and review evidence.

[⬆ Back to top](#top)

---

## 8. Stage responsibilities

| Stage | Agriculture pipeline may do | MUST NOT |
|---|---|---|
| Fixture / dry run | Prove logic without network access. | Claim source activation or production readiness. |
| RAW read | Read immutable captures with descriptors and checksums. | Mutate raw captures or infer public status. |
| WORK | Normalize, enrich, validate, aggregate, and prepare candidates. | Expose work candidates to public UI/API. |
| QUARANTINE | Route unresolved, restricted, sensitive, invalid, or over-precise material. | Promote without remediation and review. |
| PROCESSED | Write validated Agriculture records when gates close. | Treat processed records as released/public. |
| CATALOG / TRIPLET handoff | Prepare catalog and relationship projections. | Replace canonical truth with graph projections. |
| RELEASE handoff | Prepare candidate notes for release process. | Write release decisions without release workflow authority. |
| PUBLISHED | None directly from this lane. | Write public artifacts directly. |

[⬆ Back to top](#top)

---

## 9. Required gates

Every Agriculture pipeline run must check or explicitly fail closed on:

1. **Source descriptor gate** — every input has stable source identity, role, cadence, rights, and sensitivity posture.
2. **Source-role gate** — contextual sources are not silently upgraded to authoritative crop, field, yield, or economic truth.
3. **Rights gate** — unknown or restrictive license, attribution, or redistribution terms block public release.
4. **Aggregation gate** — field/operator/parcel-resolvable material is denied from public release unless aggregation and review close.
5. **Sensitivity gate** — private-property, operator, parcel, infrastructure-adjacent, water-use, or economic sensitivity fails closed.
6. **Schema gate** — candidate and processed records match approved schemas.
7. **Contract gate** — object meanings match Agriculture contracts and do not invent new semantics silently.
8. **Evidence gate** — claim-bearing outputs resolve EvidenceBundle support or abstain.
9. **Temporal gate** — observation, reporting, retrieval, processing, valid, catalog, and release times remain distinct.
10. **Spatial gate** — CRS, precision, scale, aggregation grid, county/HUC boundaries, and public-safe transforms are recorded.
11. **Policy gate** — policy decisions are finite and recorded; no silent allow.
12. **Validation gate** — validators exercise pass, fail, abstain/deny/error paths, not only success.
13. **Receipt gate** — every run records input refs, versions, parameters, hashes, output refs, and outcomes.
14. **No-direct-publish gate** — no writes to public UI, public API, or `data/published/` without release workflow authority.
15. **Catalog/triplet gate** — catalog and graph projections preserve provenance and do not replace canonical Agriculture records.
16. **Release gate** — public release requires ReleaseManifest, rollback target, correction path, and review state.

[⬆ Back to top](#top)

---

## 10. Sensitivity, aggregation, and public-safety posture

Agriculture outputs can expose private, economic, operational, or property-adjacent information.

Default posture:

- field/operator-resolvable records are denied from public release unless approved aggregation and review close;
- parcel-adjacent, irrigation, water-use, yield, management, and economic inference risks are reviewed before downstream use;
- source roles and reporting units must be preserved;
- county, HUC, grid, or other aggregation must be recorded with threshold logic and aggregation receipts where required;
- public map layers must be generalized, delayed, redacted, restricted, or withheld as required;
- generated summaries cannot replace evidence, policy, or review state;
- outputs that could be mistaken for official emergency, regulatory, crop-loss, or crop-insurance determinations must abstain, deny, or carry explicit release-reviewed limitations.

> [!CAUTION]
> Agriculture products are often useful because they combine crop, soil, hydrology, climate, hazard, and land-use signals. That same combination can create join-induced privacy and operational risk. Evaluate the derived product, not only the inputs.

[⬆ Back to top](#top)

---

## 11. Directory contract

Recommended shape:

```text
pipelines/domains/agriculture/
├── README.md                         # this file
├── PIPELINE_CONTRACT.md              # PROPOSED: Agriculture execution contract
├── run_dry_fixture.py                # PROPOSED if repo Python convention is accepted
├── normalize_crop_observation.py     # PROPOSED
├── normalize_field_candidate.py      # PROPOSED
├── build_aggregation_receipt.py      # PROPOSED; may belong in shared tools if reused
├── build_catalog_handoff.py          # PROPOSED if not centralized in pipelines/catalog/
├── validate_agriculture_candidate.py # PROPOSED wrapper if not centralized in tools/
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/agriculture/
├── README.md                         # PROPOSED / NEEDS VERIFICATION
├── crop_observation_dry_run.yaml     # PROPOSED
├── cropland_candidate_build.yaml     # PROPOSED
├── aggregation_thresholds.yaml       # PROPOSED; policy ownership must be resolved
└── catalog_handoff.yaml              # PROPOSED
```

Generated outputs must not be written beside the code that generated them. Use lifecycle homes under `data/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 12. Inputs and outputs

### Inputs

| Input class | Allowed source | Required condition |
|---|---|---|
| No-network fixture | `fixtures/domains/agriculture/` or accepted fixture home | Safe default for tests and dry runs. |
| Raw agriculture capture | `data/raw/agriculture/<source_id>/<run_id>/` | Immutable source-edge capture with source descriptor, checksums, and ingest receipt. |
| Work candidate | `data/work/agriculture/<run_id>/` | Candidate-only; not public. |
| Quarantine input | `data/quarantine/agriculture/<reason>/<run_id>/` | Audit/remediation mode only. |
| Prior processed baseline | `data/processed/agriculture/<dataset_id>/<version>/` | Validated baseline for diff/supersession. |
| Source registry / descriptor | `data/registry/sources/agriculture/`, `docs/sources/catalog/...` | Source role, rights, cadence, attribution, sensitivity. |
| Cross-lane context | Soil, Hydrology, Atmosphere, Hazards, Habitat, People/Land, or other domain lifecycle homes | Must preserve source role and domain ownership. |
| Policy / schema / contract refs | `policy/`, `schemas/`, `contracts/` | Referenced by validators, not stored here. |

### Outputs

| Output class | Correct home | Notes |
|---|---|---|
| Agriculture work candidate | `data/work/agriculture/<run_id>/` | Candidate only. |
| Agriculture quarantine record | `data/quarantine/agriculture/<reason>/<run_id>/` | Failed, restricted, unresolved, or unsafe material. |
| Agriculture processed dataset version | `data/processed/agriculture/<dataset_id>/<version>/` | Validated; not automatically public. |
| Agriculture catalog candidate | `data/catalog/domain/agriculture/...` or approved catalog home | After processed-state and evidence gates. |
| Agriculture triplet / graph delta | `data/triplets/agriculture/...` or approved graph-delta home | Projection; does not replace canonical truth. |
| Aggregation receipt | `data/receipts/...` or approved receipt/proof home | Required for public-safe aggregation claims. |
| Run receipt | `data/receipts/pipeline/...` | Process memory, not release proof. |
| Evidence / validation proof | `data/proofs/...` | EvidenceBundle, validation reports, proof packs. |
| Release handoff | `release/candidates/agriculture/...` | Only through release workflow. |

[⬆ Back to top](#top)

---

## 13. Minimal agriculture pipeline candidate record

The final schema is not defined here. This example shows the minimum information an Agriculture pipeline candidate should preserve.

```yaml
schema_version: kfm.agriculture_pipeline_candidate.v1
candidate_id: ag_<object_family>_<run_id>_<hash>
pipeline_id: domains.agriculture
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: <crop_observation|field_candidate|yield_observation|irrigation_link|stress_indicator|...>
source_inputs:
  - source_id: src_agriculture_example
    source_role: <primary|observation|context|aggregate|restricted>
    lifecycle_ref: data/raw/agriculture/<source_id>/<run_id>/
    input_hash: sha256:<hash>
    rights_state: needs_review
spatial_scope:
  geometry_ref: <governed_geometry_or_area_ref>
  public_precision: withheld_until_aggregation_review
  aggregation_unit: <county|huc|grid|withheld>
temporal_scope:
  observed_start: YYYY-MM-DD
  observed_end: YYYY-MM-DD
  reported_at: YYYY-MM-DDThh:mm:ssZ
  retrieved_at: YYYY-MM-DDThh:mm:ssZ
  processed_at: YYYY-MM-DDThh:mm:ssZ
method:
  transform_family: agriculture_normalization
  algorithm_version: <version>
  parameter_hash: sha256:<hash>
aggregation:
  required: true
  aggregation_receipt_ref: null
  threshold_state: not_evaluated
sensitivity:
  operator_resolvable: unknown
  parcel_resolvable: unknown
  private_operation_inference: needs_review
  public_release_default: DENY
policy:
  outcome: ABSTAIN
  reason_code: AGGREGATION_AND_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
outputs:
  candidate_record: data/work/agriculture/run_YYYYMMDDThhmmssZ/candidate.yml
  receipt: data/receipts/pipeline/agriculture/run_YYYYMMDDThhmmssZ.yml
review:
  reviewer_required: true
  reviewer_roles:
    - agriculture-domain-steward
    - policy-steward
    - release-steward
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 14. Dry-run, tests, fixtures, receipts, and proofs

Default execution is **fixture-only and no-network** until source activation, rights review, sensitivity review, aggregation review, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/agriculture/
├── test_no_network_dry_run.py             # PROPOSED
├── test_source_role_required.py           # PROPOSED
├── test_rights_unknown_denied.py          # PROPOSED
├── test_operator_resolvable_denied.py     # PROPOSED
├── test_aggregation_required.py           # PROPOSED
├── test_missing_evidence_abstains.py      # PROPOSED
├── test_schema_drift_quarantines.py       # PROPOSED
├── test_receipt_hashes.py                 # PROPOSED
└── test_no_direct_publish.py              # PROPOSED
```

A dry run should prove:

- fixtures load without network access;
- every input has source identity and source role;
- unknown rights produce `ABSTAIN`, `DENY`, or quarantine;
- field/operator/parcel-resolvable outputs are denied or held until aggregation review;
- missing EvidenceBundle support produces `ABSTAIN`;
- cross-lane context preserves domain ownership and source role;
- invalid records fail validation;
- receipts include input hashes, method hashes, output refs, and outcomes;
- no outputs are written to public UI, public API, `data/published/`, or release manifests by default.

[⬆ Back to top](#top)

---

## 15. Promotion, publication, correction, and rollback

Agriculture pipelines may prepare candidates. They do not publish.

Required promotion chain:

```text
agriculture source/work input
  -> agriculture candidate
  -> validation report
  -> policy decision
  -> aggregation receipt where required
  -> EvidenceBundle closure
  -> processed agriculture dataset version
  -> catalog / triplet candidate
  -> steward review
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, and quarantined runs remain auditable;
- candidate rollback preserves receipts and proof state;
- processed versions are superseded by governed state transition, not hidden overwrite;
- public artifact rollback is owned by `release/`, not by this directory;
- correction notices must point back to source, evidence, aggregation, validation, catalog, release, and rollback state.

[⬆ Back to top](#top)

---

## 16. Definition of done

This README is done when it:

- replaces the greenfield scaffold with a usable Agriculture pipeline contract;
- identifies this directory as executable Agriculture pipeline logic only;
- corrects the boundary so docs, schemas, contracts, policy, fixtures, tests, data, registries, receipts, proofs, and release decisions do not live here;
- preserves Agriculture source-role, evidence, aggregation, sensitivity, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- denies direct publication;
- gives maintainers a fixture-first expansion pattern.

Future executable Agriculture pipeline implementation is done only when it has:

- owners and review burden;
- source-descriptor coverage;
- no-network fixtures;
- schema-backed candidates;
- Agriculture contract conformance;
- rights, sensitivity, aggregation, temporal, spatial, and evidence tests;
- deterministic receipts;
- no-direct-publish tests;
- CI coverage;
- steward-review handoff;
- release, correction, and rollback documentation.

[⬆ Back to top](#top)

---

## 17. Open questions

| ID | Question | Status |
|---|---|---|
| `AG-PIPE-001` | Which Agriculture child modules should be implemented first: crop observations, cropland candidates, aggregation receipts, stress indicators, or catalog handoff? | NEEDS VERIFICATION |
| `AG-PIPE-002` | Should `AggregationReceipt` live under a shared receipt schema family or Agriculture-specific schema family? | PROPOSED / NEEDS ADR |
| `AG-PIPE-003` | Which aggregation units and thresholds are acceptable for public Agriculture products? | NEEDS VERIFICATION |
| `AG-PIPE-004` | Which source descriptors are first-wave approved for fixture-only dry runs? | NEEDS VERIFICATION |
| `AG-PIPE-005` | Which CI job owns Agriculture pipeline invariant tests? | UNKNOWN |
| `AG-PIPE-006` | Should Agriculture catalog handoff logic live here or in centralized `pipelines/catalog/` with Agriculture adapters? | NEEDS VERIFICATION |
| `AG-PIPE-007` | How should operator-resolvable, parcel-resolvable, irrigation, and water-use candidates be routed by default? | NEEDS VERIFICATION |
| `AG-PIPE-008` | Which public-safe map/API products are allowed after release, and at what aggregation/generalization? | NEEDS VERIFICATION |

---

## Maintainer note

Start with fixture-only dry runs and negative tests. Do not add live source fetching, field/operator-resolvable outputs, public map layers, release handoff automation, or direct API payload generation until source roles, rights, aggregation, sensitivity, evidence closure, and rollback are proven.
