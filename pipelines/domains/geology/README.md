<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-geology-readme
title: Geology Domain Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <geology-pipeline-owner>
  - <geology-domain-steward>
  - <hydrology-domain-steward>
  - <source-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/domains/geology/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - docs/domains/geology/README.md
  - docs/domains/geology/POLICY.md
  - docs/domains/geology/PRESERVATION_MATRIX.md
  - docs/domains/geology/OPEN_QUESTIONS.md
  - pipeline_specs/geology/
  - contracts/domains/geology/
  - schemas/contracts/v1/domains/geology/
  - policy/domains/geology/
  - policy/sensitivity/geology/
  - data/raw/geology/
  - data/work/geology/
  - data/quarantine/geology/
  - data/processed/geology/
  - data/catalog/domain/geology/
  - data/triplets/geology/
  - data/published/layers/geology/
  - data/registry/sources/geology/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/geology/
  - release/manifests/geology/
tags:
  - kfm
  - pipelines
  - domains
  - geology
  - natural-resources
  - stratigraphy
  - lithology
  - structures
  - subsurface
  - hydrostratigraphy
  - evidence
  - policy
  - governance
notes:
  - "This README replaces the greenfield scaffold for pipelines/domains/geology."
  - "Geology pipeline logic is executable implementation support only; it does not own object meaning, schemas, source descriptors, policy, lifecycle data, catalog truth, resource decisions, permits, titles, or release decisions."
  - "Geology outputs must preserve anti-collapse boundaries between occurrence, deposit, estimate, permit, production, reserve, map interpretation, and source observation."
  - "Exact subsurface, private-well, sensitive resource, infrastructure-adjacent, and unresolved-rights material fail closed by default."
  - "Concrete executable behavior, source activation, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# 🪨 Geology Domain Pipeline

> Executable Geology and Natural Resources pipeline lane for converting admitted geologic, stratigraphic, lithologic, structural, subsurface, geophysical, geochemical, hydrostratigraphic, and resource-context source material into governed candidates, quarantine records, processed records, catalog/triplet handoffs, receipts, and release-review packages — without collapsing interpretation, resource claims, permits, production records, or public-safe release state.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-geology%20domain%20pipeline-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![anti-collapse](https://img.shields.io/badge/anti--collapse-required-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/geology/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Geology and Natural Resources  
**Placement posture:** geology child lane under `pipelines/domains/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; public output requires lifecycle, EvidenceBundle, source-role, sensitivity, anti-collapse, policy, catalog/triplet, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. What belongs here](#3-what-belongs-here)
- [4. What does not belong here](#4-what-does-not-belong-here)
- [5. Geology pipeline scope](#5-geology-pipeline-scope)
- [6. Source-family posture](#6-source-family-posture)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Sensitivity, anti-collapse, and public-safe geometry](#9-sensitivity-anti-collapse-and-public-safe-geometry)
- [10. Directory contract](#10-directory-contract)
- [11. Inputs and outputs](#11-inputs-and-outputs)
- [12. Minimal geology pipeline candidate record](#12-minimal-geology-pipeline-candidate-record)
- [13. Dry-run, tests, fixtures, receipts, and proofs](#13-dry-run-tests-fixtures-receipts-and-proofs)
- [14. Promotion, publication, correction, and rollback](#14-promotion-publication-correction-and-rollback)
- [15. Definition of done](#15-definition-of-done)
- [16. Open questions](#16-open-questions)

---

## 1. Purpose

`pipelines/domains/geology/` is the executable pipeline lane for Geology and Natural Resources-domain transformations.

It supports candidate processing for:

- bedrock and surficial geology;
- geologic age, stratigraphy, and lithology;
- faults, folds, lineaments, structures, and geomorphology;
- boreholes, well logs, cores, samples, and subsurface observations;
- geophysical and geochemical observations;
- hydrostratigraphic units and geology-hydrology bridges;
- mineral occurrence and resource-context records;
- extraction, reclamation, permit, production, estimate, and reserve context without collapsing those meanings;
- public-safe geology map products after evidence, policy, and release review;
- catalog, graph, Evidence Drawer, and Focus Mode handoff packages.

This directory implements or will implement the **how** of Geology processing. It does not define Geology object meaning, schemas, policy, source descriptors, resource decisions, permit/title decisions, lifecycle storage, catalog truth, or release approval.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/geology/`? | Geology is a domain lane under the domain-pipeline umbrella. | CONFIRMED path responsibility pattern; executable behavior NEEDS VERIFICATION |
| Where do declarative specs live? | `pipeline_specs/geology/` or accepted spec home. | PROPOSED / NEEDS VERIFICATION |
| Where do source fetchers live? | `connectors/<source>`, not here. | CONFIRMED separation |
| Where do schemas live? | `schemas/contracts/v1/domains/geology/` or accepted schema home. | PROPOSED / NEEDS VERIFICATION |
| Where does policy live? | `policy/domains/geology/`, `policy/sensitivity/geology/`, `policy/rights/`, and `policy/release/` as applicable. | PROPOSED / NEEDS VERIFICATION |
| Where do outputs live? | Lifecycle homes under `data/`, not beside pipeline code. | CONFIRMED lifecycle posture |
| Can this lane publish? | No. It may prepare candidates and release handoffs only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Geology pipeline code is subordinate to source descriptors, source roles, rights, EvidenceBundle closure, sensitivity transforms, anti-collapse checks, policy decisions, release manifests, correction notices, and rollback cards. A successful run is not public release and never turns context into resource, permit, reserve, title, or extraction truth.

[⬆ Back to top](#top)

---

## 3. What belongs here

Files belong here when their primary responsibility is executable Geology-domain processing.

Appropriate contents include:

- fixture-only dry-run entrypoints for Geology pipeline behavior;
- geology-specific candidate builders;
- bedrock, surficial, stratigraphic, lithologic, and structure normalizers;
- borehole, well-log, core, sample, geophysics, and geochemistry normalizers;
- hydrostratigraphy bridge helpers, if not centralized elsewhere;
- anti-collapse validators for occurrence, deposit, estimate, permit, production, and reserve distinctions;
- public-safe geometry transform helpers, if not centralized elsewhere;
- quarantine routing helpers for sensitive, unresolved, or over-precise material;
- catalog/triplet handoff helpers, if not centralized in `pipelines/catalog/`;
- receipt emitters, if not shared;
- thin adapters that read governed lifecycle inputs, not live source systems.

A good placement test:

> If the code transforms Geology lifecycle inputs into candidates, processed records, restricted catalog/triplet handoffs, receipts, or review handoffs, it may belong here. If it fetches source data, defines meaning, defines schema, encodes policy, stores lifecycle data, or approves release, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 4. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers / connectors | `connectors/<source>` |
| Source catalog profiles | `docs/sources/catalog/...` |
| Source descriptors / source registry entries | `data/registry/sources/geology/` or approved registry home |
| Geology architecture / doctrine | `docs/domains/geology/...` |
| Geology object meaning contracts | `contracts/domains/geology/...` |
| JSON Schemas | `schemas/contracts/v1/domains/geology/...` |
| Policy bundles, sensitivity rules, release rules | `policy/domains/geology/`, `policy/sensitivity/geology/`, `policy/rights/`, `policy/release/` |
| Declarative run specs | `pipeline_specs/geology/...` |
| Fixtures | `fixtures/domains/geology/` or accepted fixture home |
| Tests | `tests/pipelines/domains/geology/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions | `release/candidates/geology/`, `release/manifests/geology/`, `release/rollback_cards/`, `release/correction_notices/` |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, `packages/ui/`, `packages/maplibre-runtime/` |
| Sensitive exact subsurface, private-well, or resource-location examples | Not in this README; use governed restricted lifecycle/proof homes with review controls |

> [!WARNING]
> The previous scaffold wording allowed “docs, contracts, schemas, policies, fixtures, tests, packages, pipelines, registries, or data lifecycle artifacts” here. This README narrows the boundary: **only executable Geology pipeline logic belongs here.** The other responsibility roots remain separate authority surfaces.

[⬆ Back to top](#top)

---

## 5. Geology pipeline scope

Geology pipeline work may include these governed processing responsibilities:

| Scope area | Pipeline responsibility | Publication posture |
|---|---|---|
| Geologic maps | Normalize bedrock, surficial, geomorphology, and map-unit context. | Public only when source role, scale, and evidence close. |
| Stratigraphy / lithology | Normalize units, ages, lithologic descriptions, and correlations. | Interpretive uncertainty must remain visible. |
| Structures | Normalize faults, folds, lineaments, and structural context. | Scale and confidence limits required. |
| Subsurface observations | Normalize boreholes, cores, samples, and well logs. | Exact private or sensitive locations fail closed. |
| Geophysics / geochemistry | Normalize observations, methods, values, and qualifiers. | Method and uncertainty required before claims. |
| Hydrostratigraphy | Prepare geology × hydrology bridge candidates. | Hydrology ownership remains with Hydrology; joins are derived. |
| Mineral/resource context | Normalize occurrence/deposit/resource context without collapsing meanings. | Resource implications require source-role and sensitivity review. |
| Permits / production / reserves | Preserve legal and administrative distinctions. | KFM does not issue permit, reserve, title, or extraction truth. |
| Reclamation context | Normalize reclamation or disturbed-land context where admitted. | Avoid unsupported regulatory or operational claims. |
| Catalog/triplet handoff | Prepare restricted or public-safe catalog/graph candidates after evidence closure. | Does not replace canonical review state. |

[⬆ Back to top](#top)

---

## 6. Source-family posture

Geology pipeline code may consume only admitted or fixture-bound source material.

Candidate source families may include, subject to source descriptors, rights, and steward review:

- state or federal geologic maps;
- stratigraphic, lithologic, and structure datasets;
- borehole, well-log, core, sample, geophysics, and geochemistry records;
- mineral occurrence, deposit, estimate, production, permit, and reclamation context;
- hydrostratigraphy and groundwater-adjacent geology references;
- remote sensing, elevation, geomorphology, and hazards context through governed cross-lane joins;
- local upload or steward-curated material only through source-descriptor, rights, sensitivity, and review gates.

This README does not activate any source. Each source family requires SourceDescriptor coverage, source role, rights posture, sensitivity classification, attribution, fixtures, validation, and review routing before use.

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Geology pipeline must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal Geology pipeline stance:

1. **Read** approved fixtures, immutable raw captures, work candidates, quarantine inputs in remediation mode, or prior processed baselines.
2. **Normalize** into work candidates with source role, rights, temporal scope, spatial scope, scale, uncertainty, anti-collapse class, evidence references, and public-safe geometry posture.
3. **Quarantine** unresolved rights, source-role mismatch, schema drift, sensitivity risk, over-precise location, private-well/resource exposure, or validation failure.
4. **Promote to processed** only after validation, policy, evidence, sensitivity/public-safe transform, review, and reviewer gates appropriate to significance.
5. **Prepare catalog/triplet handoffs** only after processed-state and evidence closure, and only with sensitivity-safe payloads.
6. **Publish** only through release decisions, public-safe artifacts, rollback targets, and correction paths.

Do not treat a move from one lifecycle folder to another as promotion. Promotion is a governed state transition with receipts and review evidence.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Geology pipeline run must check or explicitly fail closed on:

1. **Source descriptor gate** — every input has stable source identity, role, cadence, rights, and sensitivity posture.
2. **Source-role gate** — map, observation, context, model, administrative, permit, and production records are not silently collapsed.
3. **Anti-collapse gate** — occurrence, deposit, estimate, permit, production, reserve, title, map polygon, and AI summary remain distinct.
4. **Rights gate** — unknown or restrictive license, permission, attribution, or redistribution terms block public release.
5. **Sensitivity gate** — exact subsurface, private-well, sensitive resource, infrastructure-adjacent, and restricted records fail closed.
6. **Public-safe geometry gate** — public products require approved generalization, redaction, aggregation, or denial decisions with receipts.
7. **Scale and uncertainty gate** — map scale, method, confidence, uncertainty, and spatial resolution are recorded.
8. **Review gate** — required steward or domain review state is recorded before promotion beyond candidate or quarantine where applicable.
9. **Schema gate** — candidate and processed records match approved schemas.
10. **Contract gate** — object meanings match Geology contracts and do not invent new semantics silently.
11. **Evidence gate** — claim-bearing outputs resolve EvidenceBundle support or abstain.
12. **Temporal gate** — observation, sampling, publication, valid, retrieval, processing, catalog, and release times remain distinct.
13. **Spatial gate** — CRS, geometry precision, aggregation/generalization method, and public-safe transforms are recorded.
14. **Policy gate** — policy decisions are finite and recorded; no silent allow.
15. **Validation gate** — validators exercise pass, fail, restrict, abstain, deny, and error paths, not only success.
16. **Receipt gate** — every run records input refs, versions, parameters, transforms, hashes, output refs, and outcomes.
17. **No-direct-publish gate** — no writes to public UI, public API, or `data/published/` without release workflow authority.
18. **Catalog/triplet gate** — catalog and graph projections preserve provenance and do not replace canonical records or review state.
19. **Release gate** — public release requires ReleaseManifest, rollback target, correction path, and review state.

[⬆ Back to top](#top)

---

## 9. Sensitivity, anti-collapse, and public-safe geometry

Geology is fail-closed where exact subsurface, private-well, sensitive resource, infrastructure-adjacent, or unresolved-rights material could be exposed or overinterpreted.

Default posture:

- candidate records are not confirmations;
- generalized map polygons are not deposit, reserve, permit, title, or production truth;
- public products must preserve source role, scale, method, uncertainty, and EvidenceBundle support;
- sensitive exact geometry is generalized, redacted, delayed, restricted, aggregated, or withheld where needed;
- generated summaries cannot replace evidence, source role, steward review, transform receipts, policy, or release state;
- outputs that could imply unsupported resource value, extraction status, permit status, reserve status, private ownership, or infrastructure vulnerability must abstain, deny, quarantine, or require reviewer handoff.

[⬆ Back to top](#top)

---

## 10. Directory contract

Recommended shape:

```text
pipelines/domains/geology/
├── README.md                         # this file
├── PIPELINE_CONTRACT.md              # PROPOSED: Geology execution contract
├── run_dry_fixture.py                # PROPOSED if repo Python convention is accepted
├── normalize_map_unit.py             # PROPOSED
├── normalize_stratigraphy.py         # PROPOSED
├── normalize_structure.py            # PROPOSED
├── normalize_subsurface_observation.py # PROPOSED
├── normalize_geochemistry.py         # PROPOSED
├── normalize_resource_context.py     # PROPOSED
├── validate_anti_collapse.py         # PROPOSED
├── apply_public_safe_geometry.py     # PROPOSED; may belong in shared tools if reused
├── build_catalog_handoff.py          # PROPOSED if not centralized in pipelines/catalog/
├── validate_geology_candidate.py     # PROPOSED wrapper if not centralized in tools/
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/geology/
├── README.md                         # PROPOSED / NEEDS VERIFICATION
├── map_unit_dry_run.yaml             # PROPOSED
├── subsurface_observation_dry_run.yaml # PROPOSED
├── anti_collapse_checks.yaml         # PROPOSED
├── public_safe_geometry.yaml         # PROPOSED; policy ownership must be resolved
└── catalog_handoff.yaml              # PROPOSED
```

Generated outputs must not be written beside the code that generated them. Use lifecycle homes under `data/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 11. Inputs and outputs

### Inputs

| Input class | Allowed source | Required condition |
|---|---|---|
| No-network fixture | `fixtures/domains/geology/` or accepted fixture home | Synthetic, generalized, or redacted where needed. |
| Raw geology capture | `data/raw/geology/<source_id>/<run_id>/` | Immutable source-edge capture with source descriptor, checksums, and ingest receipt. |
| Work candidate | `data/work/geology/<run_id>/` | Candidate-only; not public. |
| Quarantine input | `data/quarantine/geology/<reason>/<run_id>/` | Audit/remediation mode only. |
| Prior processed baseline | `data/processed/geology/<dataset_id>/<version>/` | Validated restricted baseline for diff/supersession. |
| Source registry / descriptor | `data/registry/sources/geology/`, `docs/sources/catalog/...` | Source role, rights, cadence, attribution, sensitivity. |
| Cross-lane context | Hydrology, Hazards, Soil, Agriculture, Roads, Settlements, or other lifecycle homes | Must preserve source role and domain ownership. |
| Policy / schema / contract refs | `policy/`, `schemas/`, `contracts/` | Referenced by validators, not stored here. |

### Outputs

| Output class | Correct home | Notes |
|---|---|---|
| Geology work candidate | `data/work/geology/<run_id>/` | Candidate only. |
| Geology quarantine record | `data/quarantine/geology/<reason>/<run_id>/` | Failed, restricted, unresolved, or unsafe material. |
| Geology processed dataset version | `data/processed/geology/<dataset_id>/<version>/` | Validated/restricted; not automatically public. |
| Public-safe catalog candidate | `data/catalog/domain/geology/...` or approved catalog home | After processed-state, transform, and evidence gates. |
| Triplet / graph delta | `data/triplets/geology/...` or approved graph-delta home | Projection; does not replace canonical truth or review state. |
| Public-safe geometry / anti-collapse receipt | `data/receipts/...` or approved receipt/proof home | Required before public-safe derivative. |
| Run receipt | `data/receipts/pipeline/...` | Process memory, not release proof. |
| Evidence / validation proof | `data/proofs/...` | EvidenceBundle, validation reports, proof packs. |
| Release handoff | `release/candidates/geology/...` | Only through release workflow. |

[⬆ Back to top](#top)

---

## 12. Minimal geology pipeline candidate record

The final schema is not defined here. This example shows the minimum information a Geology pipeline candidate should preserve.

```yaml
schema_version: kfm.geology_pipeline_candidate.v1
candidate_id: geol_<object_family>_<run_id>_<hash>
pipeline_id: domains.geology
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: <map_unit|stratigraphic_unit|lithology|structure|borehole|well_log|core|sample|geophysics_observation|geochemistry_observation|mineral_occurrence|resource_context|...>
source_inputs:
  - source_id: src_geology_example
    source_role: <observation|map|context|model|administrative|restricted>
    lifecycle_ref: data/raw/geology/<source_id>/<run_id>/
    input_hash: sha256:<hash>
    rights_state: needs_review
anti_collapse:
  occurrence_is_deposit: false
  estimate_is_reserve: false
  permit_is_production: false
  map_polygon_is_claim: false
spatial_scope:
  geometry_ref: restricted_or_public_safe_ref
  public_precision: denied_until_public_safe_transform
temporal_scope:
  observed_at: null
  sampled_at: null
  published_at: null
  valid_start: null
  valid_end: null
  retrieved_at: YYYY-MM-DDThh:mm:ssZ
  processed_at: YYYY-MM-DDThh:mm:ssZ
method:
  transform_family: geology_candidate_normalization
  algorithm_version: <version>
  parameter_hash: sha256:<hash>
scale_and_uncertainty:
  source_scale: unknown
  confidence: needs_review
  limitations:
    - candidate_only
sensitivity:
  subsurface_precision_risk: needs_review
  private_well_risk: needs_review
  resource_location_risk: needs_review
  public_release_default: DENY_UNTIL_REVIEW
policy:
  outcome: ABSTAIN
  reason_code: SOURCE_ROLE_AND_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
outputs:
  candidate_record: data/work/geology/run_YYYYMMDDThhmmssZ/candidate.yml
  receipt: data/receipts/pipeline/geology/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 13. Dry-run, tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until source activation, rights review, sensitivity review, anti-collapse review, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/geology/
├── test_no_network_dry_run.py                # PROPOSED
├── test_source_role_required.py              # PROPOSED
├── test_rights_unknown_denied.py             # PROPOSED
├── test_occurrence_not_deposit.py            # PROPOSED
├── test_estimate_not_reserve.py              # PROPOSED
├── test_permit_not_production.py             # PROPOSED
├── test_map_polygon_not_claim.py             # PROPOSED
├── test_public_safe_geometry_required.py     # PROPOSED
├── test_missing_evidence_abstains.py         # PROPOSED
├── test_receipt_hashes.py                    # PROPOSED
└── test_no_direct_publish.py                 # PROPOSED
```

A dry run should prove:

- fixtures load without network access;
- every input has source identity and source role;
- unknown rights produce `ABSTAIN`, `DENY`, or quarantine;
- occurrence, deposit, estimate, reserve, permit, production, title, and map interpretation remain distinct;
- sensitive or over-precise geometry is withheld from public-safe outputs;
- missing EvidenceBundle support produces `ABSTAIN`;
- steward review and public-safe transform receipts are required where sensitivity is unresolved;
- invalid records fail validation;
- receipts include input hashes, method hashes, transform refs, output refs, and outcomes;
- no outputs are written to public UI, public API, `data/published/`, or release manifests by default.

[⬆ Back to top](#top)

---

## 14. Promotion, publication, correction, and rollback

Geology pipelines may prepare candidates. They do not publish.

Required promotion chain:

```text
geology source/work input
  -> geology candidate
  -> validation report
  -> policy decision
  -> anti-collapse and public-safe transform receipt where required
  -> EvidenceBundle closure
  -> processed geology dataset version
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
- correction notices must point back to source, evidence, anti-collapse checks, public-safe transforms, validation, catalog, release, and rollback state.

[⬆ Back to top](#top)

---

## 15. Definition of done

This README is done when it:

- replaces the greenfield scaffold with a usable Geology pipeline contract;
- identifies this directory as executable Geology pipeline logic only;
- corrects the boundary so docs, schemas, contracts, policy, fixtures, tests, data, registries, receipts, proofs, and release decisions do not live here;
- preserves source-role, anti-collapse, evidence, public-safe geometry, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- denies direct publication and sensitive geology/resource exposure;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable Geology pipeline implementation is done only when it has:

- owners and review burden;
- source-descriptor coverage;
- synthetic/generalized/redacted no-network fixtures;
- schema-backed candidates;
- Geology contract conformance;
- rights, sensitivity, scale, anti-collapse, temporal, spatial, and evidence tests;
- deterministic receipts;
- no-direct-publish tests;
- CI coverage;
- steward-review handoff;
- release, correction, and rollback documentation.

[⬆ Back to top](#top)

---

## 16. Open questions

| ID | Question | Status |
|---|---|---|
| `GEOL-PIPE-001` | Which Geology child modules should be implemented first: map units, stratigraphy, subsurface observations, anti-collapse checks, public-safe geometry, or catalog handoff? | NEEDS VERIFICATION |
| `GEOL-PIPE-002` | Which object family owns public-safe geometry and anti-collapse receipts if they become reusable outside Geology? | PROPOSED / NEEDS ADR |
| `GEOL-PIPE-003` | Which source descriptors are first-wave approved for fixture-only dry runs? | NEEDS VERIFICATION |
| `GEOL-PIPE-004` | Which CI job owns Geology pipeline invariant tests? | UNKNOWN |
| `GEOL-PIPE-005` | Should catalog handoff logic live here or in centralized `pipelines/catalog/` with Geology adapters? | NEEDS VERIFICATION |
| `GEOL-PIPE-006` | Which public-safe map/API products are allowed after review and release, and at what generalization? | NEEDS VERIFICATION |
| `GEOL-PIPE-007` | How should cross-lane joins with Hydrology, Hazards, Soil, Agriculture, Roads, Settlements, or People/Land be denied, restricted, or generalized? | NEEDS VERIFICATION |
| `GEOL-PIPE-008` | How should the segment-vs-flat path conflict for schemas and policy be resolved before adding machine contracts? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Start with synthetic/generalized fixture-only dry runs and negative tests. Do not add live source fetching, precise sensitive-location examples, public resource-claim products, public map layers, release handoff automation, or direct API payload generation until source roles, rights, anti-collapse checks, public-safe transforms, evidence closure, and rollback are proven.
