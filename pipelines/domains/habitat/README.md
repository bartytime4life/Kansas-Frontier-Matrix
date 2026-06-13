<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-habitat-readme
title: Habitat Domain Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <habitat-pipeline-owner>
  - <habitat-domain-steward>
  - <fauna-domain-steward>
  - <flora-domain-steward>
  - <source-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/domains/habitat/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/biodiversity/README.md
  - pipelines/biodiversity/vegetation_stress/README.md
  - pipelines/cross_lane/riparian_vegetation/README.md
  - docs/domains/habitat/README.md
  - docs/domains/habitat/ARCHITECTURE.md
  - docs/domains/habitat/DATA_LIFECYCLE.md
  - docs/domains/habitat/IDENTITY_MODEL.md
  - docs/domains/habitat/PRESERVATION_MATRIX.md
  - docs/domains/habitat/CANONICAL_PATHS.md
  - docs/domains/habitat/API_CONTRACTS.md
  - docs/runbooks/habitat/PROMOTION_RUNBOOK.md
  - pipeline_specs/habitat/
  - contracts/domains/habitat/
  - schemas/contracts/v1/domains/habitat/
  - policy/domains/habitat/
  - policy/sensitivity/habitat/
  - data/raw/habitat/
  - data/work/habitat/
  - data/quarantine/habitat/
  - data/processed/habitat/
  - data/catalog/domain/habitat/
  - data/triplets/habitat/
  - data/published/layers/habitat/
  - data/registry/sources/habitat/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/habitat/
  - release/manifests/habitat/
tags:
  - kfm
  - pipelines
  - domains
  - habitat
  - ecology
  - land-cover
  - suitability
  - connectivity
  - corridors
  - restoration
  - stewardship-zones
  - evidence
  - policy
  - governance
notes:
  - "This README replaces the greenfield scaffold for pipelines/domains/habitat."
  - "Habitat pipeline logic is executable implementation support only; it does not own species records, plant records, hydrology truth, soil truth, schemas, source descriptors, policy, lifecycle data, catalog truth, or release decisions."
  - "Habitat outputs must preserve anti-collapse boundaries between habitat patches, land cover, suitability models, critical-habitat designations, occurrence evidence, and public-safe derivatives."
  - "Sensitive ecological context, species/plant joins, exact vulnerable habitat, stewardship-controlled data, and unresolved rights fail closed by default."
  - "Concrete executable behavior, source activation, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# 🌿 Habitat Domain Pipeline

> Executable Habitat-domain pipeline lane for converting admitted land-cover, ecological-system, habitat-patch, suitability, connectivity, corridor, stewardship, wetland, restoration, and sensitive-ecology context into governed candidates, quarantine records, processed records, catalog/triplet handoffs, receipts, and release-review packages — without collapsing modeled habitat, regulatory designation, species occurrence, plant occurrence, or public-safe release state.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-habitat%20domain%20pipeline-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![anti-collapse](https://img.shields.io/badge/source--role%20anti--collapse-required-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/habitat/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Habitat  
**Placement posture:** habitat child lane under `pipelines/domains/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; public output requires lifecycle, EvidenceBundle, source-role, sensitivity, policy, catalog/triplet, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. What belongs here](#3-what-belongs-here)
- [4. What does not belong here](#4-what-does-not-belong-here)
- [5. Habitat pipeline scope](#5-habitat-pipeline-scope)
- [6. Source-family posture](#6-source-family-posture)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Sensitivity, anti-collapse, and public-safe geometry](#9-sensitivity-anti-collapse-and-public-safe-geometry)
- [10. Directory contract](#10-directory-contract)
- [11. Inputs and outputs](#11-inputs-and-outputs)
- [12. Minimal habitat pipeline candidate record](#12-minimal-habitat-pipeline-candidate-record)
- [13. Dry-run, tests, fixtures, receipts, and proofs](#13-dry-run-tests-fixtures-receipts-and-proofs)
- [14. Promotion, publication, correction, and rollback](#14-promotion-publication-correction-and-rollback)
- [15. Definition of done](#15-definition-of-done)
- [16. Open questions](#16-open-questions)

---

## 1. Purpose

`pipelines/domains/habitat/` is the executable pipeline lane for Habitat-domain transformations.

It supports candidate processing for:

- habitat patches and habitat classes;
- land-cover and ecological-system context;
- suitability, quality, condition, and connectivity candidates;
- corridors, buffers, stewardship zones, and restoration-opportunity context;
- critical-habitat or regulatory-context joins without replacing regulatory source authority;
- wetland, riparian, soil, hydrology, hazards, flora, and fauna context joins;
- public-safe habitat derivatives after evidence, policy, and release review;
- catalog, graph, Evidence Drawer, and Focus Mode handoff packages.

This directory implements or will implement the **how** of Habitat processing. It does not define Habitat object meaning, schemas, policy, source descriptors, species truth, plant truth, hydrology truth, soil truth, lifecycle storage, catalog truth, or release approval.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/habitat/`? | Habitat is a domain lane under the domain-pipeline umbrella. | CONFIRMED path responsibility pattern; executable behavior NEEDS VERIFICATION |
| Where do declarative specs live? | `pipeline_specs/habitat/` or accepted spec home. | PROPOSED / NEEDS VERIFICATION |
| Where do source fetchers live? | `connectors/<source>`, not here. | CONFIRMED separation |
| Where do schemas live? | `schemas/contracts/v1/domains/habitat/` or accepted schema home. | PROPOSED / NEEDS VERIFICATION |
| Where does policy live? | `policy/domains/habitat/`, `policy/sensitivity/habitat/`, `policy/rights/`, and `policy/release/` as applicable. | PROPOSED / NEEDS VERIFICATION |
| Where do outputs live? | Lifecycle homes under `data/`, not beside pipeline code. | CONFIRMED lifecycle posture |
| Can this lane publish? | No. It may prepare candidates and release handoffs only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Habitat pipeline code is subordinate to source descriptors, source roles, rights, EvidenceBundle closure, sensitivity transforms, anti-collapse checks, policy decisions, release manifests, correction notices, and rollback cards. A successful run is not public release and never turns modeled suitability into species occurrence, plant occurrence, critical-habitat designation, or regulatory truth.

[⬆ Back to top](#top)

---

## 3. What belongs here

Files belong here when their primary responsibility is executable Habitat-domain processing.

Appropriate contents include:

- fixture-only dry-run entrypoints for Habitat pipeline behavior;
- habitat-specific candidate builders;
- land-cover, ecological-system, patch, suitability, condition, and connectivity normalizers;
- corridor, restoration-opportunity, and stewardship-zone candidate builders;
- source-role anti-collapse validators;
- public-safe geometry and sensitivity transform helpers, if not centralized elsewhere;
- quarantine routing helpers for sensitive, unresolved, or over-precise material;
- catalog/triplet handoff helpers, if not centralized in `pipelines/catalog/`;
- receipt emitters, if not shared;
- thin adapters that read governed lifecycle inputs, not live source systems.

A good placement test:

> If the code transforms Habitat lifecycle inputs into candidates, processed records, restricted catalog/triplet handoffs, receipts, or review handoffs, it may belong here. If it fetches source data, defines meaning, defines schema, encodes policy, stores lifecycle data, or approves release, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 4. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers / connectors | `connectors/<source>` |
| Source catalog profiles | `docs/sources/catalog/...` |
| Source descriptors / source registry entries | `data/registry/sources/habitat/` or approved registry home |
| Habitat architecture / doctrine | `docs/domains/habitat/...` |
| Habitat object meaning contracts | `contracts/domains/habitat/...` |
| JSON Schemas | `schemas/contracts/v1/domains/habitat/...` |
| Policy bundles, sensitivity rules, release rules | `policy/domains/habitat/`, `policy/sensitivity/habitat/`, `policy/rights/`, `policy/release/` |
| Declarative run specs | `pipeline_specs/habitat/...` |
| Fixtures | `fixtures/domains/habitat/` or accepted fixture home |
| Tests | `tests/pipelines/domains/habitat/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions | `release/candidates/habitat/`, `release/manifests/habitat/`, `release/rollback_cards/`, `release/correction_notices/` |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, `packages/ui/`, `packages/maplibre-runtime/` |
| Animal taxa or occurrence truth | Fauna lane |
| Plant taxa, specimen, or occurrence truth | Flora lane |
| Hydrology, soil, agriculture, or hazards root truth | Their owning domain lanes |
| Sensitive ecology details or location-revealing examples | Not in this README; use governed restricted lifecycle/proof homes with review controls |

> [!WARNING]
> The previous scaffold wording allowed “docs, contracts, schemas, policies, fixtures, tests, packages, pipelines, registries, or data lifecycle artifacts” here. This README narrows the boundary: **only executable Habitat pipeline logic belongs here.** The other responsibility roots remain separate authority surfaces.

[⬆ Back to top](#top)

---

## 5. Habitat pipeline scope

Habitat pipeline work may include these governed processing responsibilities:

| Scope area | Pipeline responsibility | Publication posture |
|---|---|---|
| Land cover | Normalize land-cover context and source metadata. | Public only when source role, scale, and evidence close. |
| Habitat patches | Build habitat patch candidates, boundaries, and uncertainty notes. | Candidate until validation and review close. |
| Suitability / quality / condition | Normalize modeled surfaces and caveats. | Model outputs are not species occurrences or regulatory truth. |
| Connectivity / corridors | Prepare connectivity, corridor, and fragmentation candidates. | Derived; requires method and uncertainty. |
| Stewardship zones | Normalize administrative or stewardship context. | Administrative role must stay distinct from ecological condition. |
| Restoration opportunity | Prepare restoration-opportunity candidates. | Avoid unsupported land-management or success claims. |
| Critical habitat / regulatory context | Preserve regulatory source role and effective dates. | Habitat pipeline does not issue designations. |
| Cross-lane joins | Prepare habitat × fauna/flora/hydrology/soil/agriculture/hazards relationship candidates. | Other domains keep ownership; joins are derived. |
| Catalog/triplet handoff | Prepare restricted or public-safe catalog/graph candidates after evidence closure. | Does not replace canonical review state. |

[⬆ Back to top](#top)

---

## 6. Source-family posture

Habitat pipeline code may consume only admitted or fixture-bound source material.

Candidate source families may include, subject to source descriptors, rights, and steward review:

- land-cover and ecological-system datasets;
- wetland, riparian, floodplain, and hydrology context;
- critical-habitat or stewardship-context services;
- protected-area, conservation, and administrative context;
- habitat suitability, condition, connectivity, and restoration models;
- fauna and flora occurrence context only through governed joins and sensitivity controls;
- soil, hazards, agriculture, and remote-sensing context through governed cross-lane joins;
- local upload or steward-curated material only through source-descriptor, rights, sensitivity, and review gates.

This README does not activate any source. Each source family requires SourceDescriptor coverage, source role, rights posture, sensitivity classification, attribution, fixtures, validation, and review routing before use.

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Habitat pipeline must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal Habitat pipeline stance:

1. **Read** approved fixtures, immutable raw captures, work candidates, quarantine inputs in remediation mode, or prior processed baselines.
2. **Normalize** into work candidates with source role, rights, temporal scope, spatial scope, scale, uncertainty, model/method posture, sensitivity posture, evidence references, and public-safe geometry handling.
3. **Quarantine** unresolved rights, source-role mismatch, schema drift, sensitivity risk, over-precise geometry, private-location exposure, join-induced risk, or validation failure.
4. **Promote to processed** only after validation, policy, evidence, sensitivity/public-safe transform, review, and reviewer gates appropriate to significance.
5. **Prepare catalog/triplet handoffs** only after processed-state and evidence closure, and only with sensitivity-safe payloads.
6. **Publish** only through release decisions, public-safe artifacts, rollback targets, and correction paths.

Do not treat a move from one lifecycle folder to another as promotion. Promotion is a governed state transition with receipts and review evidence.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Habitat pipeline run must check or explicitly fail closed on:

1. **Source descriptor gate** — every input has stable source identity, role, cadence, rights, and sensitivity posture.
2. **Source-role gate** — observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic records are not silently collapsed.
3. **Anti-collapse gate** — habitat patch, land cover, suitability model, regulatory designation, species occurrence, plant occurrence, and AI summary remain distinct.
4. **Rights gate** — unknown or restrictive license, permission, attribution, or redistribution terms block public release.
5. **Sensitivity gate** — sensitive ecology, species/plant joins, steward-controlled data, private-location risk, and exact vulnerable habitat fail closed.
6. **Public-safe geometry gate** — public products require approved generalization, redaction, aggregation, delay, restriction, or denial decisions with receipts.
7. **Scale and uncertainty gate** — source scale, method, confidence, uncertainty, and spatial resolution are recorded.
8. **Review gate** — required steward or domain review state is recorded before promotion beyond candidate or quarantine where applicable.
9. **Schema gate** — candidate and processed records match approved schemas.
10. **Contract gate** — object meanings match Habitat contracts and do not invent new semantics silently.
11. **Evidence gate** — claim-bearing outputs resolve EvidenceBundle support or abstain.
12. **Temporal gate** — observation, source vintage, valid, retrieval, processing, catalog, and release times remain distinct.
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

Habitat is fail-closed where derived ecology, species/plant joins, stewardship context, exact vulnerable habitat, or unresolved rights could create sensitive exposure or overinterpretation.

Default posture:

- habitat models are not species occurrences;
- modeled suitability is not regulatory designation;
- land-cover classification is not habitat condition truth without evidence and method caveats;
- public products must preserve source role, scale, method, uncertainty, and EvidenceBundle support;
- sensitive exact geometry is generalized, redacted, delayed, restricted, aggregated, or withheld where needed;
- generated summaries cannot replace evidence, source role, steward review, transform receipts, policy, or release state;
- outputs that could imply unsupported critical habitat, species presence, plant presence, private land condition, or restoration success must abstain, deny, quarantine, or require reviewer handoff.

[⬆ Back to top](#top)

---

## 10. Directory contract

Recommended shape:

```text
pipelines/domains/habitat/
├── README.md                         # this file
├── PIPELINE_CONTRACT.md              # PROPOSED: Habitat execution contract
├── run_dry_fixture.py                # PROPOSED if repo Python convention is accepted
├── normalize_land_cover.py           # PROPOSED
├── normalize_habitat_patch.py        # PROPOSED
├── normalize_suitability_surface.py  # PROPOSED
├── normalize_connectivity.py         # PROPOSED
├── normalize_stewardship_zone.py     # PROPOSED
├── build_restoration_candidate.py    # PROPOSED
├── validate_source_role_anticollapse.py # PROPOSED
├── apply_public_safe_geometry.py     # PROPOSED; may belong in shared tools if reused
├── build_catalog_handoff.py          # PROPOSED if not centralized in pipelines/catalog/
├── validate_habitat_candidate.py     # PROPOSED wrapper if not centralized in tools/
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/habitat/
├── README.md                         # PROPOSED / NEEDS VERIFICATION
├── land_cover_dry_run.yaml           # PROPOSED
├── habitat_patch_build.yaml          # PROPOSED
├── suitability_surface_build.yaml    # PROPOSED
├── source_role_anticollapse.yaml     # PROPOSED
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
| No-network fixture | `fixtures/domains/habitat/` or accepted fixture home | Synthetic, generalized, or redacted where needed. |
| Raw habitat capture | `data/raw/habitat/<source_id>/<run_id>/` | Immutable source-edge capture with source descriptor, checksums, and ingest receipt. |
| Work candidate | `data/work/habitat/<run_id>/` | Candidate-only; not public. |
| Quarantine input | `data/quarantine/habitat/<reason>/<run_id>/` | Audit/remediation mode only. |
| Prior processed baseline | `data/processed/habitat/<dataset_id>/<version>/` | Validated restricted baseline for diff/supersession. |
| Source registry / descriptor | `data/registry/sources/habitat/`, `docs/sources/catalog/...` | Source role, rights, cadence, attribution, sensitivity. |
| Cross-lane context | Fauna, Flora, Hydrology, Soil, Agriculture, Hazards, Roads, Settlements, or other lifecycle homes | Must preserve source role and domain ownership. |
| Policy / schema / contract refs | `policy/`, `schemas/`, `contracts/` | Referenced by validators, not stored here. |

### Outputs

| Output class | Correct home | Notes |
|---|---|---|
| Habitat work candidate | `data/work/habitat/<run_id>/` | Candidate only. |
| Habitat quarantine record | `data/quarantine/habitat/<reason>/<run_id>/` | Failed, restricted, unresolved, or unsafe material. |
| Habitat processed dataset version | `data/processed/habitat/<dataset_id>/<version>/` | Validated/restricted; not automatically public. |
| Public-safe catalog candidate | `data/catalog/domain/habitat/...` or approved catalog home | After processed-state, transform, and evidence gates. |
| Triplet / graph delta | `data/triplets/habitat/...` or approved graph-delta home | Projection; does not replace canonical truth or review state. |
| Public-safe geometry / anti-collapse receipt | `data/receipts/...` or approved receipt/proof home | Required before public-safe derivative. |
| Run receipt | `data/receipts/pipeline/...` | Process memory, not release proof. |
| Evidence / validation proof | `data/proofs/...` | EvidenceBundle, validation reports, proof packs. |
| Release handoff | `release/candidates/habitat/...` | Only through release workflow. |

[⬆ Back to top](#top)

---

## 12. Minimal habitat pipeline candidate record

The final schema is not defined here. This example shows the minimum information a Habitat pipeline candidate should preserve.

```yaml
schema_version: kfm.habitat_pipeline_candidate.v1
candidate_id: hab_<object_family>_<run_id>_<hash>
pipeline_id: domains.habitat
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: <habitat_patch|habitat_class|land_cover|suitability_surface|connectivity|corridor|stewardship_zone|restoration_opportunity|...>
source_inputs:
  - source_id: src_habitat_example
    source_role: <observed|regulatory|modeled|aggregate|administrative|candidate|synthetic>
    lifecycle_ref: data/raw/habitat/<source_id>/<run_id>/
    input_hash: sha256:<hash>
    rights_state: needs_review
anti_collapse:
  suitability_is_occurrence: false
  land_cover_is_condition_truth: false
  regulatory_context_is_model_output: false
  ai_summary_is_evidence: false
spatial_scope:
  geometry_ref: restricted_or_public_safe_ref
  public_precision: denied_until_public_safe_transform
temporal_scope:
  source_vintage: null
  observed_at: null
  valid_start: null
  valid_end: null
  retrieved_at: YYYY-MM-DDThh:mm:ssZ
  processed_at: YYYY-MM-DDThh:mm:ssZ
method:
  transform_family: habitat_candidate_normalization
  algorithm_version: <version>
  parameter_hash: sha256:<hash>
scale_and_uncertainty:
  source_scale: unknown
  confidence: needs_review
  limitations:
    - candidate_only
sensitivity:
  join_induced_risk: needs_review
  sensitive_ecology_risk: needs_review
  public_release_default: DENY_UNTIL_REVIEW
policy:
  outcome: ABSTAIN
  reason_code: SOURCE_ROLE_AND_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
outputs:
  candidate_record: data/work/habitat/run_YYYYMMDDThhmmssZ/candidate.yml
  receipt: data/receipts/pipeline/habitat/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 13. Dry-run, tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until source activation, rights review, sensitivity review, anti-collapse review, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/habitat/
├── test_no_network_dry_run.py                # PROPOSED
├── test_source_role_required.py              # PROPOSED
├── test_rights_unknown_denied.py             # PROPOSED
├── test_suitability_not_occurrence.py        # PROPOSED
├── test_land_cover_not_condition_truth.py    # PROPOSED
├── test_regulatory_not_model_output.py       # PROPOSED
├── test_sensitive_join_quarantines.py        # PROPOSED
├── test_public_safe_geometry_required.py     # PROPOSED
├── test_missing_evidence_abstains.py         # PROPOSED
├── test_receipt_hashes.py                    # PROPOSED
└── test_no_direct_publish.py                 # PROPOSED
```

A dry run should prove:

- fixtures load without network access;
- every input has source identity and source role;
- unknown rights produce `ABSTAIN`, `DENY`, or quarantine;
- habitat patch, land cover, suitability, regulatory designation, and occurrence context remain distinct;
- sensitive or over-precise geometry is withheld from public-safe outputs;
- missing EvidenceBundle support produces `ABSTAIN`;
- steward review and public-safe transform receipts are required where sensitivity is unresolved;
- invalid records fail validation;
- receipts include input hashes, method hashes, transform refs, output refs, and outcomes;
- no outputs are written to public UI, public API, `data/published/`, or release manifests by default.

[⬆ Back to top](#top)

---

## 14. Promotion, publication, correction, and rollback

Habitat pipelines may prepare candidates. They do not publish.

Required promotion chain:

```text
habitat source/work input
  -> habitat candidate
  -> validation report
  -> policy decision
  -> anti-collapse and public-safe transform receipt where required
  -> EvidenceBundle closure
  -> processed habitat dataset version
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

- replaces the greenfield scaffold with a usable Habitat pipeline contract;
- identifies this directory as executable Habitat pipeline logic only;
- corrects the boundary so docs, schemas, contracts, policy, fixtures, tests, data, registries, receipts, proofs, and release decisions do not live here;
- preserves source-role, anti-collapse, evidence, public-safe geometry, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- denies direct publication and sensitive ecology exposure;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable Habitat pipeline implementation is done only when it has:

- owners and review burden;
- source-descriptor coverage;
- synthetic/generalized/redacted no-network fixtures;
- schema-backed candidates;
- Habitat contract conformance;
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
| `HAB-PIPE-001` | Which Habitat child modules should be implemented first: land cover, habitat patches, suitability surfaces, source-role anti-collapse, public-safe geometry, or catalog handoff? | NEEDS VERIFICATION |
| `HAB-PIPE-002` | Which object family owns public-safe geometry and source-role anti-collapse receipts if they become reusable outside Habitat? | PROPOSED / NEEDS ADR |
| `HAB-PIPE-003` | Which source descriptors are first-wave approved for fixture-only dry runs? | NEEDS VERIFICATION |
| `HAB-PIPE-004` | Which CI job owns Habitat pipeline invariant tests? | UNKNOWN |
| `HAB-PIPE-005` | Should catalog handoff logic live here or in centralized `pipelines/catalog/` with Habitat adapters? | NEEDS VERIFICATION |
| `HAB-PIPE-006` | Which public-safe map/API products are allowed after review and release, and at what generalization? | NEEDS VERIFICATION |
| `HAB-PIPE-007` | How should cross-lane joins with Fauna, Flora, Hydrology, Soil, Hazards, Agriculture, or People/Land be denied, restricted, or generalized? | NEEDS VERIFICATION |
| `HAB-PIPE-008` | How should the segment-vs-flat path conflict for schemas and policy be resolved before adding machine contracts? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Start with synthetic/generalized fixture-only dry runs and negative tests. Do not add live source fetching, precise sensitive-ecology examples, public species/plant inference products, public map layers, release handoff automation, or direct API payload generation until source roles, rights, anti-collapse checks, public-safe transforms, evidence closure, and rollback are proven.
