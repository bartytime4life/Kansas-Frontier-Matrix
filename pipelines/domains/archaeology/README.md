<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-archaeology-readme
title: Archaeology Domain Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <archaeology-pipeline-owner>
  - <archaeology-domain-steward>
  - <cultural-review-steward>
  - <source-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/domains/archaeology/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - docs/domains/archaeology/README.md
  - docs/domains/archaeology/ARCHITECTURE.md
  - docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - docs/domains/archaeology/CULTURAL_REVIEW.md
  - docs/domains/archaeology/PRESERVATION_MATRIX.md
  - docs/domains/archaeology/IDENTITY_MODEL.md
  - docs/domains/archaeology/SOURCE_REGISTRY.md
  - pipeline_specs/archaeology/
  - contracts/domains/archaeology/
  - schemas/contracts/v1/domains/archaeology/
  - policy/domains/archaeology/
  - data/raw/archaeology/
  - data/work/archaeology/
  - data/quarantine/archaeology/
  - data/processed/archaeology/
  - data/catalog/domain/archaeology/
  - data/published/layers/archaeology/
  - data/registry/sources/archaeology/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/archaeology/
  - release/manifests/archaeology/
tags:
  - kfm
  - pipelines
  - domains
  - archaeology
  - cultural-heritage
  - sensitivity
  - exact-location-denial
  - cultural-review
  - steward-review
  - evidence
  - policy
  - governance
notes:
  - "This README replaces the greenfield scaffold for pipelines/domains/archaeology."
  - "Archaeology pipeline logic is executable implementation support only; it does not own object meaning, schemas, source descriptors, policy, lifecycle data, catalog truth, cultural decisions, or release decisions."
  - "Exact archaeological geometry, burial/sacred/culturally sensitive context, collection-security detail, private landowner detail, and unresolved sensitivity fail closed by default."
  - "Concrete executable behavior, source activation, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# 🏺 Archaeology Domain Pipeline

> Executable Archaeology and Cultural Heritage pipeline lane for converting admitted, reviewable archaeology source material into governed candidates, quarantine records, processed records, catalog/triplet handoffs, receipts, and release-review packages — **without exposing sensitive locations or bypassing cultural review, evidence, policy, sensitivity, or release gates**.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-archaeology%20domain%20pipeline-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![sensitivity](https://img.shields.io/badge/default%20sensitivity-fail%20closed-d62728)
![publication](https://img.shields.io/badge/publication-cultural%20review%20%2B%20release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/archaeology/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Archaeology and Cultural Heritage  
**Placement posture:** archaeology child lane under `pipelines/domains/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; public output requires lifecycle, EvidenceBundle, sensitivity transform, cultural/steward review, policy, catalog/triplet, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. What belongs here](#3-what-belongs-here)
- [4. What does not belong here](#4-what-does-not-belong-here)
- [5. Archaeology pipeline scope](#5-archaeology-pipeline-scope)
- [6. Source-family posture](#6-source-family-posture)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Stage responsibilities](#8-stage-responsibilities)
- [9. Required gates](#9-required-gates)
- [10. Sensitivity, cultural review, and public-safety posture](#10-sensitivity-cultural-review-and-public-safety-posture)
- [11. Directory contract](#11-directory-contract)
- [12. Inputs and outputs](#12-inputs-and-outputs)
- [13. Minimal archaeology pipeline candidate record](#13-minimal-archaeology-pipeline-candidate-record)
- [14. Dry-run, tests, fixtures, receipts, and proofs](#14-dry-run-tests-fixtures-receipts-and-proofs)
- [15. Promotion, publication, correction, and rollback](#15-promotion-publication-correction-and-rollback)
- [16. Definition of done](#16-definition-of-done)
- [17. Open questions](#17-open-questions)

---

## 1. Purpose

`pipelines/domains/archaeology/` is the executable pipeline lane for Archaeology and Cultural Heritage-domain transformations.

It supports candidate processing for object families such as:

- archaeological site candidates and confirmed-site records;
- surveys, survey projects, and survey transects;
- artifact and artifact-record candidates;
- features, site components, context, and provenience context;
- excavation and stratigraphic units;
- remote-sensing anomalies, LiDAR candidates, and candidate features;
- geophysics observations;
- 3D documentation metadata;
- cultural review and steward review records;
- collection accession and repository records;
- chronology assertions and cultural-temporal period context;
- sensitivity transforms and publication-transform receipts.

This directory implements or will implement the **how** of Archaeology processing. It does not define Archaeology object meaning, schemas, policy, source descriptors, cultural decisions, lifecycle storage, catalog truth, or release approval.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/archaeology/`? | Archaeology is a domain lane under the domain-pipeline umbrella. | CONFIRMED path responsibility pattern; executable behavior NEEDS VERIFICATION |
| Where do declarative specs live? | `pipeline_specs/archaeology/` or accepted spec home. | PROPOSED / NEEDS VERIFICATION |
| Where do source fetchers live? | `connectors/<source>/`, not here. | CONFIRMED separation |
| Where do schemas live? | `schemas/contracts/v1/domains/archaeology/` or accepted schema home. | PROPOSED / NEEDS VERIFICATION |
| Where does policy live? | `policy/domains/archaeology/`, `policy/sensitivity/`, `policy/rights/`, and `policy/release/` as applicable. | PROPOSED / NEEDS VERIFICATION |
| Where do outputs live? | Lifecycle homes under `data/`, not beside pipeline code. | CONFIRMED lifecycle posture |
| Can this lane publish? | No. It may prepare candidates and release handoffs only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Archaeology pipeline code is subordinate to source descriptors, source roles, rights, cultural/steward review, EvidenceBundle closure, sensitivity transforms, policy decisions, release manifests, correction notices, and rollback cards. A successful run is not public release and never authorizes sensitive-location exposure.

[⬆ Back to top](#top)

---

## 3. What belongs here

Files belong here when their primary responsibility is executable Archaeology-domain processing.

Appropriate contents include:

- fixture-only dry-run entrypoints for Archaeology pipeline behavior;
- archaeology-specific candidate builders;
- archaeology-specific normalizers for admitted lifecycle inputs;
- sensitivity-transform helpers, if not centralized elsewhere;
- cultural-review and steward-review handoff helpers;
- quarantine routing helpers for sensitive or unresolved material;
- validator wrappers, if not reusable under `tools/`;
- catalog/triplet handoff helpers, if not centralized in `pipelines/catalog/`;
- receipt emitters, if not shared;
- thin adapters that read governed lifecycle inputs, not live source systems.

A good placement test:

> If the code transforms Archaeology lifecycle inputs into candidates, processed records, restricted catalog/triplet handoffs, receipts, or review handoffs, it may belong here. If it fetches source data, defines meaning, defines schema, encodes policy, stores lifecycle data, carries exact sensitive locations in docs, or approves release, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 4. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers / connectors | `connectors/<source>/` |
| Source catalog profiles | `docs/sources/catalog/...` |
| Source descriptors / source registry entries | `data/registry/sources/archaeology/` or approved registry home |
| Archaeology architecture / doctrine | `docs/domains/archaeology/...` |
| Archaeology object meaning contracts | `contracts/domains/archaeology/...` |
| JSON Schemas | `schemas/contracts/v1/domains/archaeology/...` |
| Policy bundles, sensitivity rules, publication rules | `policy/domains/archaeology/`, `policy/sensitivity/`, `policy/rights/`, `policy/release/` |
| Declarative run specs | `pipeline_specs/archaeology/...` |
| Fixtures | `fixtures/domains/archaeology/` or accepted fixture home |
| Tests | `tests/pipelines/domains/archaeology/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions | `release/candidates/archaeology/`, `release/manifests/archaeology/`, `release/rollback_cards/`, `release/correction_notices/` |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, `packages/ui/`, `packages/maplibre-runtime/` |
| Exact sensitive archaeological coordinates or location-revealing examples | Nowhere in this README; only governed restricted lifecycle/proof homes with review controls |

> [!WARNING]
> The previous scaffold wording allowed “docs, contracts, schemas, policies, fixtures, tests, packages, pipelines, registries, or data lifecycle artifacts” here. This README narrows the boundary: **only executable Archaeology pipeline logic belongs here.** The other responsibility roots remain separate authority surfaces.

[⬆ Back to top](#top)

---

## 5. Archaeology pipeline scope

Archaeology pipeline work may include these governed processing responsibilities:

| Scope area | Pipeline responsibility | Publication posture |
|---|---|---|
| Site and candidate records | Normalize candidate or confirmed records with evidence, source role, review state, and sensitivity class. | Exact geometry denied by default. |
| Survey material | Normalize surveys, projects, transects, and bounded survey metadata. | Public output requires sensitivity transform and review. |
| Artifact and context records | Normalize artifact metadata, context, and provenience references. | Collection security and cultural sensitivity reviewed. |
| Excavation and stratigraphy | Normalize excavation and stratigraphic unit metadata. | Restricted unless review and transformation close. |
| Remote sensing and LiDAR candidates | Prepare candidate features and uncertainty notes. | Candidate-only until review; no public exact exposure. |
| Geophysics and 3D documentation | Normalize observation and documentation metadata. | Public derivative requires transform and review. |
| Cultural and steward review | Prepare handoff records and review state transitions. | Review decisions are not generated by this pipeline. |
| Sensitivity transforms | Apply approved generalization/redaction transforms. | Transform receipt required before public-safe product. |
| Catalog/triplet handoff | Prepare restricted or public-safe catalog/graph candidates after evidence closure. | Does not replace canonical review state. |

[⬆ Back to top](#top)

---

## 6. Source-family posture

Archaeology pipeline code may consume only admitted or fixture-bound source material.

Candidate source families may include, subject to source descriptors, rights, and steward review:

- survey and project records;
- archive and collection repository records;
- remote-sensing and LiDAR candidate data;
- geophysics observation data;
- 3D documentation metadata;
- chronology or cultural-temporal context;
- steward-curated or restricted-review material;
- local upload material only through source-descriptor, rights, sensitivity, and review gates.

This README does not activate any source. Each source family requires SourceDescriptor coverage, source role, rights posture, sensitivity classification, attribution, fixtures, validation, and review routing before use.

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Archaeology pipeline must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal Archaeology pipeline stance:

1. **Read** approved fixtures, immutable raw captures, work candidates, quarantine inputs in remediation mode, or prior processed baselines.
2. **Normalize** into work candidates with source role, rights, temporal scope, spatial scope, cultural-review posture, sensitivity class, evidence references, and restricted geometry handling.
3. **Quarantine** unresolved rights, source-role mismatch, schema drift, cultural sensitivity, exact-location risk, collection-security risk, private-land detail, or validation failure.
4. **Promote to processed** only after validation, policy, evidence, sensitivity, cultural/steward review, and reviewer gates appropriate to significance.
5. **Prepare catalog/triplet handoffs** only after processed-state and evidence closure, and only with sensitivity-safe payloads.
6. **Publish** only through release decisions, public-safe artifacts, rollback targets, and correction paths.

Do not treat a move from one lifecycle folder to another as promotion. Promotion is a governed state transition with receipts and review evidence.

[⬆ Back to top](#top)

---

## 8. Stage responsibilities

| Stage | Archaeology pipeline may do | MUST NOT |
|---|---|---|
| Fixture / dry run | Prove logic without network access or sensitive real coordinates. | Claim source activation or production readiness. |
| RAW read | Read immutable captures with descriptors and checksums. | Mutate raw captures or expose content publicly. |
| WORK | Normalize, validate, transform, and prepare candidates. | Expose work candidates to public UI/API. |
| QUARANTINE | Route unresolved, restricted, sensitive, invalid, or over-precise material. | Promote without remediation and review. |
| PROCESSED | Write validated restricted records when all required gates close. | Treat processed records as released/public. |
| CATALOG / TRIPLET handoff | Prepare restricted or public-safe catalog and relationship projections. | Replace canonical truth or review state with graph projections. |
| RELEASE handoff | Prepare candidate notes for release process. | Write release decisions without release workflow authority. |
| PUBLISHED | None directly from this lane. | Write public artifacts directly. |

[⬆ Back to top](#top)

---

## 9. Required gates

Every Archaeology pipeline run must check or explicitly fail closed on:

1. **Source descriptor gate** — every input has stable source identity, role, cadence, rights, and sensitivity posture.
2. **Source-role gate** — context, candidate, archive, and steward-reviewed records are not silently upgraded to confirmed site truth.
3. **Rights gate** — unknown or restrictive license, permission, cultural protocol, attribution, or redistribution terms block public release.
4. **Sensitivity gate** — exact-location, burial/sacred/culturally sensitive, collection-security, private-land, or looting-risk exposure fails closed.
5. **Cultural/steward review gate** — required review state is recorded before any promotion beyond candidate or quarantine.
6. **Candidate-vs-confirmed gate** — candidates remain candidates unless confirmation evidence and review close.
7. **Geometry gate** — exact geometry is withheld, generalized, redacted, delayed, or denied unless restricted authority permits use.
8. **Schema gate** — candidate and processed records match approved schemas.
9. **Contract gate** — object meanings match Archaeology contracts and do not invent new semantics silently.
10. **Evidence gate** — claim-bearing outputs resolve EvidenceBundle support or abstain.
11. **Temporal gate** — observation, survey, event, curation, retrieval, processing, catalog, and release times remain distinct.
12. **Spatial gate** — CRS, geometry precision, aggregation/generalization method, and public-safe transforms are recorded.
13. **Policy gate** — policy decisions are finite and recorded; no silent allow.
14. **Validation gate** — validators exercise pass, fail, restrict, abstain, deny, and error paths, not only success.
15. **Receipt gate** — every run records input refs, versions, parameters, transforms, hashes, output refs, and outcomes.
16. **No-direct-publish gate** — no writes to public UI, public API, or `data/published/` without release workflow authority.
17. **Catalog/triplet gate** — catalog and graph projections preserve provenance and do not replace canonical records or review state.
18. **Release gate** — public release requires ReleaseManifest, rollback target, correction path, and review state.

[⬆ Back to top](#top)

---

## 10. Sensitivity, cultural review, and public-safety posture

Archaeology is a fail-closed domain. The safe default is non-public, restricted, or quarantine until the record proves otherwise.

Default posture:

- exact locations are denied from public outputs by default;
- cultural and steward review is required for sensitive or uncertain records;
- candidate features are not confirmations;
- public products must use approved sensitivity transforms;
- generated summaries cannot replace evidence, cultural review, steward review, policy, or release state;
- public map layers must be generalized, redacted, delayed, restricted, or withheld where needed;
- outputs that could enable site exposure, cultural harm, collection-security risk, private-land exposure, or public misinterpretation must abstain, deny, quarantine, or require reviewer handoff.

> [!CAUTION]
> Archaeology products can become harmful through precision, context, or joins. Evaluate the derived product, not only the source record.

[⬆ Back to top](#top)

---

## 11. Directory contract

Recommended shape:

```text
pipelines/domains/archaeology/
├── README.md                         # this file
├── PIPELINE_CONTRACT.md              # PROPOSED: Archaeology execution contract
├── run_dry_fixture.py                # PROPOSED if repo Python convention is accepted
├── normalize_site_candidate.py       # PROPOSED
├── normalize_survey_record.py        # PROPOSED
├── normalize_remote_sensing_candidate.py # PROPOSED
├── apply_sensitivity_transform.py    # PROPOSED; may belong in shared tools if reused
├── build_review_handoff.py           # PROPOSED
├── build_catalog_handoff.py          # PROPOSED if not centralized in pipelines/catalog/
├── validate_archaeology_candidate.py # PROPOSED wrapper if not centralized in tools/
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/archaeology/
├── README.md                         # PROPOSED / NEEDS VERIFICATION
├── site_candidate_dry_run.yaml       # PROPOSED
├── sensitivity_transform.yaml        # PROPOSED; policy ownership must be resolved
├── review_handoff.yaml               # PROPOSED
└── catalog_handoff.yaml              # PROPOSED
```

Generated outputs must not be written beside the code that generated them. Use lifecycle homes under `data/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 12. Inputs and outputs

### Inputs

| Input class | Allowed source | Required condition |
|---|---|---|
| No-network fixture | `fixtures/domains/archaeology/` or accepted fixture home | Synthetic or redacted; no sensitive real coordinates. |
| Raw archaeology capture | `data/raw/archaeology/<source_id>/<run_id>/` | Immutable source-edge capture with source descriptor, checksums, and ingest receipt. |
| Work candidate | `data/work/archaeology/<run_id>/` | Candidate-only; not public. |
| Quarantine input | `data/quarantine/archaeology/<reason>/<run_id>/` | Audit/remediation mode only. |
| Prior processed baseline | `data/processed/archaeology/<dataset_id>/<version>/` | Validated restricted baseline for diff/supersession. |
| Source registry / descriptor | `data/registry/sources/archaeology/`, `docs/sources/catalog/...` | Source role, rights, cadence, attribution, sensitivity. |
| Cultural/steward review state | approved review/proof home | Required before promotion where applicable. |
| Policy / schema / contract refs | `policy/`, `schemas/`, `contracts/` | Referenced by validators, not stored here. |

### Outputs

| Output class | Correct home | Notes |
|---|---|---|
| Archaeology work candidate | `data/work/archaeology/<run_id>/` | Candidate only. |
| Archaeology quarantine record | `data/quarantine/archaeology/<reason>/<run_id>/` | Failed, restricted, unresolved, or unsafe material. |
| Archaeology processed dataset version | `data/processed/archaeology/<dataset_id>/<version>/` | Validated/restricted; not automatically public. |
| Public-safe catalog candidate | `data/catalog/domain/archaeology/...` or approved catalog home | After processed-state, transform, and evidence gates. |
| Triplet / graph delta | `data/triplets/archaeology/...` or approved graph-delta home | Projection; does not replace canonical truth or review state. |
| Sensitivity-transform receipt | `data/receipts/...` or approved receipt/proof home | Required before public-safe derivative. |
| Run receipt | `data/receipts/pipeline/...` | Process memory, not release proof. |
| Evidence / validation proof | `data/proofs/...` | EvidenceBundle, validation reports, proof packs. |
| Release handoff | `release/candidates/archaeology/...` | Only through release workflow. |

[⬆ Back to top](#top)

---

## 13. Minimal archaeology pipeline candidate record

The final schema is not defined here. This example shows the minimum information an Archaeology pipeline candidate should preserve.

```yaml
schema_version: kfm.archaeology_pipeline_candidate.v1
candidate_id: arch_<object_family>_<run_id>_<hash>
pipeline_id: domains.archaeology
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: <archaeological_site|survey_project|artifact_record|remote_sensing_anomaly|lidar_candidate|cultural_review|sensitivity_transform|...>
source_inputs:
  - source_id: src_archaeology_example
    source_role: <candidate|context|survey|archive|restricted>
    lifecycle_ref: data/raw/archaeology/<source_id>/<run_id>/
    input_hash: sha256:<hash>
    rights_state: needs_review
spatial_scope:
  geometry_ref: restricted_internal_ref
  exact_geometry_public: false
  public_precision: denied_until_transform_and_release
temporal_scope:
  observed_at: null
  surveyed_at: YYYY-MM-DD
  curated_at: null
  retrieved_at: YYYY-MM-DDThh:mm:ssZ
  processed_at: YYYY-MM-DDThh:mm:ssZ
method:
  transform_family: archaeology_candidate_normalization
  algorithm_version: <version>
  parameter_hash: sha256:<hash>
review:
  cultural_review_required: true
  steward_review_required: true
  review_state: not_started
sensitivity:
  default_tier: T4_RESTRICTED
  exact_location_risk: deny_public
  cultural_sensitivity: needs_review
  collection_security_risk: needs_review
  public_release_default: DENY
policy:
  outcome: ABSTAIN
  reason_code: CULTURAL_REVIEW_AND_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
outputs:
  candidate_record: data/work/archaeology/run_YYYYMMDDThhmmssZ/candidate.yml
  receipt: data/receipts/pipeline/archaeology/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 14. Dry-run, tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic-or-redacted, and no-network** until source activation, rights review, cultural review, sensitivity review, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/archaeology/
├── test_no_network_dry_run.py                  # PROPOSED
├── test_no_sensitive_real_coordinates.py       # PROPOSED
├── test_source_role_required.py                # PROPOSED
├── test_rights_unknown_denied.py               # PROPOSED
├── test_candidate_not_confirmed.py             # PROPOSED
├── test_cultural_review_required.py            # PROPOSED
├── test_exact_geometry_denied.py               # PROPOSED
├── test_sensitivity_transform_receipt_required.py # PROPOSED
├── test_missing_evidence_abstains.py           # PROPOSED
├── test_receipt_hashes.py                      # PROPOSED
└── test_no_direct_publish.py                   # PROPOSED
```

A dry run should prove:

- fixtures load without network access;
- fixtures are synthetic or redacted and contain no sensitive real coordinates;
- every input has source identity and source role;
- unknown rights produce `ABSTAIN`, `DENY`, or quarantine;
- candidate records cannot become confirmed records without review and evidence closure;
- exact geometry is withheld from public-safe outputs;
- missing EvidenceBundle support produces `ABSTAIN`;
- cultural/steward review is required where sensitivity is unresolved;
- invalid records fail validation;
- receipts include input hashes, method hashes, transform refs, output refs, and outcomes;
- no outputs are written to public UI, public API, `data/published/`, or release manifests by default.

[⬆ Back to top](#top)

---

## 15. Promotion, publication, correction, and rollback

Archaeology pipelines may prepare candidates. They do not publish.

Required promotion chain:

```text
archaeology source/work input
  -> archaeology candidate
  -> validation report
  -> policy decision
  -> cultural / steward review where required
  -> sensitivity transform receipt where required
  -> EvidenceBundle closure
  -> processed restricted dataset version
  -> catalog / triplet candidate
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, restricted, and quarantined runs remain auditable;
- candidate rollback preserves receipts and proof state;
- processed versions are superseded by governed state transition, not hidden overwrite;
- public artifact rollback is owned by `release/`, not by this directory;
- correction notices must point back to source, evidence, sensitivity transform, validation, cultural/steward review, catalog, release, and rollback state.

[⬆ Back to top](#top)

---

## 16. Definition of done

This README is done when it:

- replaces the greenfield scaffold with a usable Archaeology pipeline contract;
- identifies this directory as executable Archaeology pipeline logic only;
- corrects the boundary so docs, schemas, contracts, policy, fixtures, tests, data, registries, receipts, proofs, and release decisions do not live here;
- preserves source-role, candidate-vs-confirmed, evidence, cultural review, sensitivity transform, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- denies direct publication and exact sensitive-location exposure;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable Archaeology pipeline implementation is done only when it has:

- owners and review burden;
- source-descriptor coverage;
- synthetic or redacted no-network fixtures;
- schema-backed candidates;
- Archaeology contract conformance;
- rights, sensitivity, cultural review, temporal, spatial, and evidence tests;
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
| `ARCH-PIPE-001` | Which Archaeology child modules should be implemented first: site candidates, survey records, remote-sensing candidates, sensitivity transforms, or review handoffs? | NEEDS VERIFICATION |
| `ARCH-PIPE-002` | Which object family owns sensitivity-transform and publication-transform receipts if they become reusable outside Archaeology? | PROPOSED / NEEDS ADR |
| `ARCH-PIPE-003` | Which source descriptors are first-wave approved for fixture-only dry runs? | NEEDS VERIFICATION |
| `ARCH-PIPE-004` | Which CI job owns Archaeology pipeline invariant tests? | UNKNOWN |
| `ARCH-PIPE-005` | Should catalog handoff logic live here or in centralized `pipelines/catalog/` with Archaeology adapters? | NEEDS VERIFICATION |
| `ARCH-PIPE-006` | Which public-safe map/API products are allowed after review and release, and at what generalization? | NEEDS VERIFICATION |
| `ARCH-PIPE-007` | Which roles must approve candidate-to-processed and processed-to-release transitions for sensitive archaeology records? | NEEDS VERIFICATION |
| `ARCH-PIPE-008` | How should cross-lane joins with People/Land, Hydrology, Roads, Hazards, or Settlements be denied, restricted, or generalized? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic, fixture-only dry runs and negative tests. Do not add live source fetching, real precise-location examples, public map layers, release handoff automation, or direct API payload generation until source roles, rights, cultural review, sensitivity transforms, evidence closure, and rollback are proven.
