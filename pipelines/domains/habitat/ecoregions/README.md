<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-habitat-ecoregions-readme
title: Habitat Ecoregions Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <habitat-pipeline-owner>
  - <habitat-domain-steward>
  - <ecoregions-steward>
  - <spatial-foundation-reviewer>
  - <source-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/domains/habitat/ecoregions/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/habitat/README.md
  - pipelines/domains/habitat/land_cover/README.md
  - docs/domains/habitat/README.md
  - docs/domains/habitat/sublanes/ecoregions.md
  - docs/domains/habitat/sublanes/ecological_systems.md
  - docs/domains/spatial-foundation/README.md
  - docs/domains/fauna/README.md
  - docs/domains/flora/README.md
  - pipeline_specs/habitat/ecoregions.yaml
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
  - ecoregions
  - ecological-system
  - regionalization
  - biophysical-context
  - landscape-context
  - source-role
  - evidence-bundle
  - geoprivacy
  - public-safe
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/habitat/ecoregions path as a nested executable Habitat ecoregions sublane."
  - "Ecoregions pipeline logic is executable implementation support only; it does not own source descriptors, source catalog profiles, connectors, schemas, policy, lifecycle data, catalog truth, species or plant occurrence truth, critical-habitat designation truth, or release decisions."
  - "Ecoregion polygons are regionalization context. They classify places by a named framework/version; they do not prove species presence, plant presence, habitat patch quality, regulatory status, or cross-domain truth."
  - "Source roles must come from admitted SourceDescriptors. Legacy words such as authority/context/model in older notes must be resolved into the approved source-role vocabulary before claim-bearing use."
  - "Cross-lane joins with Fauna, Flora, Hydrology, Soil, Hazards, Agriculture, or land context must preserve owning-domain truth, sensitivity, EvidenceBundle refs, and public-safe transform state."
  - "Concrete executable behavior, source activation, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat Ecoregions Pipeline

> Executable Habitat sublane for transforming admitted ecoregion and biophysical regionalization inputs into governed ecoregion candidates, quarantine records, normalized records, catalog/triplet handoffs, receipts, and release-review packages — while preserving source framework, source version, hierarchy level, geometry lineage, evidence, policy, sensitivity, and release boundaries.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-habitat%20ecoregions-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![anti-collapse](https://img.shields.io/badge/ecoregion%20%E2%89%A0%20occurrence%20truth-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/habitat/ecoregions/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Habitat  
**Sublane:** Ecoregions / biophysical regionalization context  
**Placement posture:** nested executable sublane under `pipelines/domains/habitat/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; public-safe ecoregion outputs require lifecycle, EvidenceBundle, source-role, sensitivity, policy, catalog/triplet, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Ecoregion anti-collapse rules](#3-ecoregion-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Ecoregion scope](#6-ecoregion-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal ecoregion candidate record](#11-minimal-ecoregion-candidate-record)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/habitat/ecoregions/` is the executable sublane for Habitat ecoregion and biophysical regionalization processing.

It supports candidate processing for:

- ecoregion polygons and regionalization snapshots;
- framework identity such as EPA/Omernik, USFS/Bailey, or another admitted ecoregion authority;
- ecoregion hierarchy levels, names, codes, parent/child relations, and source version;
- geometry, CRS, source extent, and source-vintage lineage;
- ecoregion context joins to HabitatPatch, EcologicalSystem, LandCoverObservation, suitability, connectivity, restoration, and stewardship workflows;
- cross-lane context joins to Fauna, Flora, Hydrology, Soil, Hazards, Agriculture, and Spatial Foundation without adopting their truth;
- public-safe layer handoffs with attribute include-lists and precision/generalization constraints where approved;
- quarantine records for missing source descriptor, missing framework, missing level, invalid hierarchy, geometry ambiguity, CRS/source-vintage ambiguity, source-role collapse, sensitivity failure, schema drift, or validation failure;
- validation, catalog, triplet, EvidenceBundle, release-review, correction, and rollback handoff packages.

This directory implements or will implement the **how** of Habitat ecoregion processing. It does not fetch source data, define Habitat object meaning, define schemas, encode policy, store lifecycle data, decide release, own species or plant occurrence truth, own critical-habitat designation truth, own hydrology/soil/hazards/agriculture truth, or certify public map products.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/habitat/`? | Habitat is a domain lane under the domain-pipeline umbrella. | CONFIRMED path responsibility pattern; behavior NEEDS VERIFICATION |
| Why `ecoregions/`? | This is a narrow executable sublane for Habitat ecoregion/regionalization context processing. | PROPOSED / NEEDS VERIFICATION |
| Is this a connector? | No. Source fetching belongs in `connectors/<source>` or an accepted source-edge home. | CONFIRMED separation |
| Does this own ecoregion doctrine? | No. Human-facing doctrine remains in `docs/domains/habitat/` and `docs/domains/habitat/sublanes/ecoregions.md`. | CONFIRMED doc separation |
| Does this own source profiles? | No. Source profiles and SourceDescriptors remain in source/catalog and registry homes. | CONFIRMED source separation |
| Can this sublane publish? | No. It may prepare candidates and release handoffs only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Ecoregion pipeline output is not public release, not species occurrence evidence, not plant occurrence evidence, not critical-habitat designation, and not a cross-domain truth shortcut. It is regionalization context that must carry source framework, version, source role, evidence, sensitivity, policy, correction, and rollback refs.

[⬆ Back to top](#top)

---

## 3. Ecoregion anti-collapse rules

Ecoregion processing must preserve regionalization context, source role, hierarchy, geometry, time, and release state.

Disallowed collapses:

```text
ecoregion polygon -> species occurrence truth
ecoregion polygon -> plant occurrence truth
ecoregion polygon -> HabitatPatch
ecoregion polygon -> critical-habitat designation
ecoregion context -> regulatory truth
ecoregion context -> hydrology / soil / hazards / agriculture truth
EPA/Omernik framework -> USFS/Bailey framework without framework ref
Level III -> Level IV without hierarchy receipt
source version A -> source version B without source-vintage receipt
public layer -> canonical truth
generated summary -> evidence
pipeline run -> release approval
```

Required distinctions:

- source identity, source role, framework, version, level, native code, native label, geometry lineage, and source vintage are explicit;
- hierarchy relations are recorded as relationships with receipts, not inferred silently;
- ecoregions can provide context for Habitat reasoning but cannot overwrite Fauna, Flora, Hydrology, Soil, Hazards, Agriculture, Spatial Foundation, or release authority;
- joins to sensitive occurrence or exact habitat context fail closed until geoprivacy/public-safe transform, review, policy, correction, and rollback state are present;
- publication requires public-safe transforms, release review, correction path, and rollback target.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Habitat ecoregion processing.

Appropriate contents include:

- fixture-only dry-run entrypoints;
- ecoregion source-candidate normalizers;
- framework, level, code, label, and source-version preservation helpers;
- ecoregion hierarchy validators;
- geometry, CRS, extent, topology, and source-vintage validators;
- public-safe attribute include-list helpers for released layer candidates;
- cross-lane context-join preflight helpers that preserve owning-domain truth;
- policy/sensitivity preflight helpers for controlled ecology joins;
- quarantine routing helpers for missing source descriptor, framework gaps, invalid hierarchy, source-role collapse, evidence gaps, rights uncertainty, sensitivity failure, or schema failures;
- receipt emitters, if not shared;
- handoff helpers for validation, catalog, triplet, and release workflow.

A good placement test:

> If the code transforms admitted ecoregion lifecycle inputs into Habitat ecoregion candidates, quarantine records, validation handoffs, receipts, or downstream handoff packages, it may belong here. If it fetches source data, defines schemas, stores lifecycle data, decides policy, owns source profiles, writes catalog records directly, approves release, or creates public API/map payloads, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers / connectors | `connectors/<source>` or accepted connector home |
| Source catalog profiles | `docs/sources/catalog/...` |
| Source descriptors / source registry entries | `data/registry/sources/habitat/` or approved registry home |
| Habitat doctrine and object meaning | `docs/domains/habitat/...`, `contracts/domains/habitat/` |
| JSON Schemas | `schemas/contracts/v1/domains/habitat/` or accepted schema home |
| Policy, rights, sensitivity, release rules | `policy/...` responsibility roots |
| Declarative run specs | `pipeline_specs/habitat/...` |
| Fixtures | `fixtures/domains/habitat/ecoregions/` or accepted fixture home |
| Tests | `tests/pipelines/domains/habitat/ecoregions/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Fauna/Flora occurrence truth | `docs/domains/fauna/`, `docs/domains/flora/`, and their corresponding responsibility roots |
| Critical-habitat regulatory designation truth | Accepted Habitat critical-habitat source/profile/pipeline roots, not this context lane |
| Hydrology, soil, hazards, agriculture, or land truth | Owning domain roots |
| Spatial Foundation CRS/basemap/generalization authority | Spatial Foundation responsibility roots |
| Release decisions and manifests | `release/...` responsibility roots |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 6. Ecoregion scope

| Scope area | Pipeline responsibility | Failure behavior |
|---|---|---|
| Source identity | Preserve source id, descriptor refs, rights, source role, framework, version, and source extent. | Quarantine if missing. |
| Framework | Preserve named ecoregion framework and source version. | Quarantine on ambiguity. |
| Hierarchy | Preserve level, code, label, parent/child refs, and hierarchy receipt. | Quarantine on mismatch. |
| Geometry | Preserve source geometry refs, CRS, extent, simplification/generalization refs, and source vintage. | Quarantine on geometry/CRS ambiguity. |
| Context joins | Prepare ecoregion context for Habitat and cross-lane relationships. | Deny or quarantine if owning-domain refs or policy are missing. |
| Public-safe layer | Prepare candidate layer metadata and attribute include-lists only after review refs. | No direct publication. |
| Sensitive joins | Preserve geoprivacy/redaction/generalization receipts. | Fail closed if unresolved. |
| Release handoff | Prepare public-safe candidates only after evidence and policy closure. | No direct release decision. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Habitat ecoregions run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, immutable raw captures, work inputs, quarantine inputs in remediation mode, or prior processed ecoregion baselines.
2. **Normalize** into Habitat work candidates with source role, framework, level, code, label, hierarchy refs, source version, geometry refs, time refs, evidence refs, policy refs, and receipt refs.
3. **Quarantine** missing source descriptor, missing framework/version, invalid hierarchy, geometry ambiguity, source-role collapse, rights failure, sensitivity failure, evidence gap, schema drift, or validation failure.
4. **Emit receipts** with input refs, source refs, framework refs, hierarchy refs, geometry refs, transform refs, validation refs, output refs, and outcomes.
5. **Support promotion** only by feeding downstream validation and review workflows.
6. **Never publish directly.**

Ecoregions processing is a lifecycle transformation. It is not catalog closure, release approval, or public artifact creation by itself.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Habitat ecoregions run must check or explicitly fail closed on:

1. **Input lifecycle gate** — input is fixture, raw capture, work input, quarantine-remediation input, or accepted baseline.
2. **Source descriptor gate** — source identity, role, rights, citation, cadence/vintage, and sensitivity posture are known.
3. **Framework gate** — source framework, source version, native code/label, and hierarchy level are preserved.
4. **Hierarchy gate** — parent/child and level transitions carry explicit evidence or receipt refs.
5. **Source-role gate** — modeled, observed, regulatory, aggregate, administrative, candidate, and synthetic records remain distinct.
6. **Geometry/CRS gate** — geometry refs, CRS, extent, simplification/generalization, and source vintage are explicit where applicable.
7. **Temporal gate** — source time, valid time, retrieval time, processing time, release time, and correction time remain distinct.
8. **Cross-lane ownership gate** — ecoregion context joins do not become Fauna, Flora, Hydrology, Soil, Hazards, Agriculture, Spatial Foundation, or land truth.
9. **Evidence gate** — claim-bearing downstream candidates can resolve EvidenceBundle support or abstain.
10. **Policy/sensitivity gate** — unresolved rights, controlled joins, exact exposure risk, or public-safe transform gaps fail closed.
11. **Schema/contract gate** — candidates match accepted Habitat schema and ecoregion semantics.
12. **Correction/rollback gate** — release-facing handoff includes correction path and rollback target expectations.
13. **No-direct-publish gate** — no writes to public UI, public API, published layers, or release manifests as a pipeline side effect.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/habitat/ecoregions/
├── README.md                         # this file
├── ECOREGIONS_PIPELINE_CONTRACT.md   # PROPOSED: ecoregions execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/generalized fixture only
├── normalize_ecoregion_candidate.py  # PROPOSED
├── preserve_framework_identity.py    # PROPOSED
├── validate_ecoregion_hierarchy.py   # PROPOSED
├── validate_geometry_crs.py          # PROPOSED
├── validate_source_role.py           # PROPOSED
├── validate_context_joins.py         # PROPOSED
├── validate_policy_public_safe.py    # PROPOSED
├── route_quarantine.py               # PROPOSED
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/habitat/ecoregions.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted lifecycle homes under `data/work/habitat/`, `data/quarantine/habitat/`, `data/processed/habitat/`, `data/catalog/domain/habitat/`, `data/triplets/habitat/`, `data/published/layers/habitat/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/habitat/ecoregions/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Raw source capture | `data/raw/habitat/<source_id>/<run_id>/` | Immutable source-edge capture with descriptor and receipt. |
| Work candidate | `data/work/habitat/<run_id>/` | Candidate only. |
| Quarantine record | `data/quarantine/habitat/<reason>/<run_id>/` | Failed, restricted, unresolved, or unsafe material. |
| Processed ecoregion record | `data/processed/habitat/<dataset_id>/<version>/` | Only after validation and governed promotion. |
| Catalog/triplet handoff | `data/catalog/domain/habitat/`, `data/triplets/habitat/` | Projection only; not publication. |
| Receipt | `data/receipts/pipeline/habitat/ecoregions/<run_id>.yml` or accepted receipt home | Records inputs, frameworks, hierarchy, geometry, checks, outputs. |
| Evidence proof | `data/proofs/evidence_bundle/` or accepted proof home | Required for claim-bearing records. |
| Release handoff | `release/candidates/habitat/` | Reviewable, release-gated output only. |

[⬆ Back to top](#top)

---

## 11. Minimal ecoregion candidate record

The final schema is not defined here. This example shows the minimum information a Habitat ecoregion candidate should preserve.

```yaml
schema_version: kfm.habitat_ecoregion_candidate.v1
candidate_id: habitat_ecoregion_<framework>_<level>_<native_code>_<version>_<hash>
pipeline_id: domains.habitat.ecoregions
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: EcoregionSnapshot
source:
  source_id: <source_id>
  source_role: <observed|modeled|regulatory|aggregate|administrative|candidate|synthetic>
  lifecycle_ref: data/raw/habitat/<source_id>/<run_id>/
  input_hash: sha256:<hash>
  rights_state: needs_review
framework:
  framework_name: <epa_omernik|usfs_bailey|other>
  framework_version: null
  native_level: null
  native_code: null
  native_label: null
  parent_code: null
  child_codes: []
spatial:
  geometry_ref: null
  crs: null
  source_extent: null
  simplification_receipt_ref: null
time:
  source_version_date: null
  valid_start: null
  valid_end: null
  retrieved_at: null
  processed_at: YYYY-MM-DDThh:mm:ssZ
context:
  allowed_join_domains: []
  context_join_policy: needs_review
policy:
  outcome: ABSTAIN
  reason_code: SOURCE_DESCRIPTOR_FRAMEWORK_POLICY_OR_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
anti_collapse:
  ecoregion_is_occurrence_truth: false
  ecoregion_is_critical_habitat_designation: false
  context_join_is_cross_domain_truth: false
  generated_summary_is_evidence: false
outputs:
  candidate_record: data/work/habitat/run_YYYYMMDDThhmmssZ/ecoregion_candidate.yml
  receipt: data/receipts/pipeline/habitat/ecoregions/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until source activation, ecoregion spec, evidence, policy, sensitivity, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/habitat/ecoregions/
├── test_no_network_dry_run.py              # PROPOSED
├── test_source_descriptor_required.py      # PROPOSED
├── test_framework_identity_required.py     # PROPOSED
├── test_hierarchy_preserved.py             # PROPOSED
├── test_source_version_required.py         # PROPOSED
├── test_geometry_crs_required.py           # PROPOSED
├── test_source_role_preserved.py           # PROPOSED
├── test_not_occurrence_truth.py            # PROPOSED
├── test_not_critical_habitat_designation.py # PROPOSED
├── test_context_join_requires_policy.py    # PROPOSED
├── test_public_safe_transform_required.py  # PROPOSED
├── test_evidence_gap_abstains.py           # PROPOSED
├── test_receipt_hashes.py                  # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, source descriptors are required, framework identity and hierarchy are preserved, ecoregion context is not occurrence truth or regulatory designation truth, controlled joins fail closed, receipts are deterministic, and no run writes directly to public UI, public API, catalog store, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Habitat ecoregions pipelines may prepare candidates and handoff packages. They do not publish.

Required chain:

```text
admitted ecoregion source capture
  -> ecoregion work candidate
  -> validation report
  -> policy decision
  -> EvidenceBundle closure
  -> processed ecoregion / regionalization record
  -> catalog / triplet candidate
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, restricted, stale, conflicted, and quarantined ecoregion runs remain auditable;
- receipts preserve source refs, framework refs, hierarchy refs, geometry refs, transform refs, evidence refs, source-role refs, policy outcomes, and failure reasons;
- processed versions are produced by governed promotion, not hidden overwrite;
- downstream artifacts are invalidated if source refs, framework refs, hierarchy refs, geometry refs, EvidenceBundle refs, policy refs, source-role refs, correction refs, or rollback refs drift;
- release rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/habitat/ecoregions/README.md` file;
- identifies this directory as a nested executable Habitat ecoregions sublane;
- prevents connector, source-profile, schema, contract, policy, fixture, test, data, proof, catalog, graph, public API, UI, and release authority from being placed here;
- preserves ecoregion framework, level, hierarchy, geometry, source version, source roles, context joins, evidence, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- blocks ecoregion-as-occurrence-truth, ecoregion-as-critical-habitat-designation, context-join-as-cross-domain-truth, generated-summary-as-evidence, and direct publication writes;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has source-descriptor coverage, synthetic/generalized/redacted no-network fixtures, schema-backed candidates, contract conformance, framework/hierarchy/source-role/evidence/policy/no-direct-publish tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `HAB-ECO-001` | Should ecoregion execution remain one sublane, or split by source framework such as EPA/Omernik, USFS/Bailey, and NatureServe/USNVC adjacency? | NEEDS VERIFICATION / ADR |
| `HAB-ECO-002` | Which source-edge job owns each ecoregion retrieval before this sublane reads lifecycle inputs? | NEEDS VERIFICATION |
| `HAB-ECO-003` | Which schema owns EcoregionSnapshot, EcoregionContextJoin, hierarchy records, and quarantine reasons? | NEEDS VERIFICATION |
| `HAB-ECO-004` | Which first-wave source is approved for fixture-only dry runs: EPA Level III/IV, USFS/Bailey, NatureServe crosswalk, or synthetic hierarchy? | NEEDS VERIFICATION |
| `HAB-ECO-005` | Which CI job owns Habitat ecoregions invariant tests? | UNKNOWN |
| `HAB-ECO-006` | Where should shared ecoregion framework/crosswalk tables live so this executable lane does not become classification authority? | NEEDS VERIFICATION / ADR |
| `HAB-ECO-007` | What public-safe precision, zoom, attribute include-list, and caveat levels are allowed for released ecoregion layers? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/generalized fixture-only dry runs and negative tests. Do not add live source fetching, source-profile editing, schema authority, policy authority, direct catalog writes, public layer writes, release-manifest writes, or generated region summaries until source roles, framework identity, hierarchy preservation, EvidenceBundle closure, public-safe transforms, release review, and rollback are proven.
