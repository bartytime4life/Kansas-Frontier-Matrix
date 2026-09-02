<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-geology-bedrock-units-readme
title: Geology Bedrock Units Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <geology-pipeline-owner>
  - <geology-domain-steward>
  - <bedrock-geology-steward>
  - <stratigraphy-steward>
  - <structures-steward>
  - <surficial-geology-steward>
  - <kgs-source-steward>
  - <usgs-source-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public-with-generalization-gates
path: pipelines/domains/geology/bedrock_units/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/geology/README.md
  - pipelines/domains/geology/surficial_units/README.md
  - pipelines/domains/geology/cross_sections/README.md
  - pipelines/domains/geology/boreholes/README.md
  - docs/domains/geology/README.md
  - docs/domains/geology/sublanes/bedrock_geology.md
  - docs/domains/geology/sublanes/stratigraphy.md
  - docs/domains/geology/sublanes/structures.md
  - docs/domains/geology/POLICY.md
  - docs/domains/geology/PRESERVATION_MATRIX.md
  - docs/sources/catalog/kansas/ksgs.md
  - pipeline_specs/geology/bedrock_units.yaml
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
  - bedrock-units
  - bedrock-geology
  - geologic-units
  - lithostratigraphy
  - lithology
  - stratigraphy
  - contacts
  - structures
  - boundary-version
  - kgs
  - usgs
  - evidence
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/geology/bedrock_units path as a nested executable Geology bedrock-units sublane."
  - "Bedrock-units pipeline logic is executable implementation support only; it does not own source descriptors, source catalog profiles, connectors, schemas, policy, lifecycle data, catalog truth, stratigraphic truth, structural truth, surficial truth, well-log truth, or release decisions."
  - "Bedrock units are consolidated-rock map/context candidates. They must not collapse into surficial units, soil map units, mineral occurrences, hazard risk, hydrology measurements, ownership/title, or release-approved public layers."
  - "Unit symbols, lithostratigraphic names, lithology, geologic age, contacts, structures, map series, scale, source vintage, and GeologyBoundaryVersion refs must be preserved."
  - "Public-facing bedrock layers require generalized/public-safe geometry, evidence closure, policy outcome, release review, correction path, and rollback target."
  - "Concrete executable behavior, source activation, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geology Bedrock Units Pipeline

> Executable Geology sublane for transforming admitted bedrock geologic-map source captures and fixtures into governed `GeologicUnit` and `GeologyBoundaryVersion` candidates, quarantine records, normalized records, catalog/triplet handoffs, receipts, and release-review packages — while preserving unit identity, lithology, age, contacts, structures, source version, map scale, evidence, policy, correction path, and rollback boundaries.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-geology%20bedrock%20units-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![anti-collapse](https://img.shields.io/badge/bedrock%20unit%20%E2%89%A0%20surficial%20unit-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/geology/bedrock_units/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Geology and Natural Resources  
**Sublane:** Bedrock units / consolidated-rock geology  
**Placement posture:** nested executable sublane under `pipelines/domains/geology/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; public-safe bedrock outputs require lifecycle, EvidenceBundle, source-role, sensitivity, policy, catalog/triplet, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Bedrock-unit anti-collapse rules](#3-bedrock-unit-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Bedrock-unit scope](#6-bedrock-unit-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal bedrock-unit candidate record](#11-minimal-bedrock-unit-candidate-record)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/geology/bedrock_units/` is the executable sublane for Geology bedrock-unit processing.

It supports candidate processing for:

- `GeologicUnit` records typed to consolidated rock;
- lithostratigraphic formations, members, groups, lithology descriptors, and age assignments;
- bedrock map polygons, contacts, faults, folds, and other bedrock-expressed structure references where delivered with the bedrock map;
- `StratigraphicInterval`, `StratigraphicCorrelation`, and `GeologicAge` references where admitted by stratigraphy review;
- `CrossSection` context where section panels reference bedrock units while remaining interpretive outputs;
- `GeologyBoundaryVersion` records for map interpretation version, source scale, uncertainty, source vintage, and geometry lineage;
- public-safe generalized bedrock map candidates and metadata packages where release policy permits;
- quarantine records for missing source descriptor, missing unit symbol, unresolved stratigraphic name, invalid boundary version, geometry ambiguity, CRS/source-vintage ambiguity, source-role collapse, rights uncertainty, schema drift, or validation failure;
- validation, catalog, triplet, EvidenceBundle, release-review, correction, and rollback handoff packages.

This directory implements or will implement the **how** of bedrock-unit processing. It does not fetch source data, define Geology object meaning, define schemas, encode policy, store lifecycle data, decide release, own surficial geology, own soil map-unit truth, own hydrology/hazard/resource truth, or create public map/API products by itself.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/geology/`? | Geology is a domain lane under the domain-pipeline umbrella. | CONFIRMED path responsibility pattern; behavior NEEDS VERIFICATION |
| Why `bedrock_units/`? | This is a narrow executable sublane for consolidated-rock geologic units and map boundary versions. | PROPOSED / NEEDS VERIFICATION |
| Is this a connector? | No. Source fetching belongs in `connectors/<source>` or an accepted source-edge home. | CONFIRMED separation |
| Does this own bedrock doctrine? | No. Human-facing doctrine remains in `docs/domains/geology/sublanes/bedrock_geology.md`; object meaning belongs in contracts. | CONFIRMED doc separation |
| Does this own stratigraphy or structures? | No. It references accepted stratigraphy/structure context but must not become their sole authority. | CONFIRMED boundary posture |
| Can this sublane publish? | No. It may prepare candidates and release handoffs only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Bedrock-unit pipeline output is not public release, not surficial-unit truth, not soil truth, not hazard risk, not resource proof, and not a cross-domain shortcut. It is source-bound consolidated-rock geology evidence that must carry source role, boundary version, evidence, policy, correction, and rollback refs.

[⬆ Back to top](#top)

---

## 3. Bedrock-unit anti-collapse rules

Bedrock-unit processing must preserve source role, map-unit semantics, stratigraphic uncertainty, geometry lineage, cross-lane ownership, and release state.

Disallowed collapses:

```text
bedrock polygon -> surficial unit
bedrock polygon -> soil mapunit
bedrock polygon -> mineral occurrence
bedrock context -> hazard risk
bedrock contact -> fault without structure evidence
stratigraphic correlation -> map fact
well top -> continuous bedrock boundary without model receipt
cross-section interpretation -> source map boundary
source map unit -> generalized public layer without transform receipt
source version A -> source version B without boundary-version receipt
AI summary -> EvidenceBundle
pipeline run -> release approval
```

Required distinctions:

- source identity, source role, source product, source version, map-unit symbol, unit label, lithology, geologic age, geometry lineage, CRS, scale, and rights posture are explicit;
- bedrock, surficial, soil, hydrology, hazards, mineral resources, boreholes, well logs, and public layers remain separate authority classes;
- contacts, faults, folds, and cross sections carry source or method receipts;
- generalization, simplification, tiling, or public-safe precision transforms carry receipts;
- every public claim resolves evidence or abstains;
- publication requires public-safe transforms, release review, correction path, and rollback target.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Geology bedrock-unit processing.

Appropriate contents include:

- fixture-only dry-run entrypoints;
- bedrock source-candidate normalizers;
- map-unit symbol, label, lithology, age, and stratigraphic-name preservation helpers;
- boundary-version and source-vintage validators;
- geometry, CRS, scale, simplification, and public-safe generalization validators;
- stratigraphic interval and correlation handoff helpers that preserve interpretation status;
- structure/contact relation helpers where source evidence is present;
- cross-section reference helpers that keep section panels interpretive;
- borehole/well-log evidence-link helpers without taking ownership of well-log truth;
- cross-lane ownership validators for Surficial, Soil, Hydrology, Hazards, Natural Resources, Archaeology, Habitat, and Infrastructure relations;
- quarantine routing helpers for missing source descriptor, missing map-unit code, geometry drift, source-role collapse, rights uncertainty, evidence gaps, or schema failures;
- receipt emitters, if not shared;
- handoff helpers for validation, catalog, triplet, and release workflow.

A good placement test:

> If the code transforms admitted bedrock geology lifecycle inputs into Geology bedrock-unit candidates, quarantine records, validation handoffs, receipts, or downstream handoff packages, it may belong here. If it fetches source data, defines schemas, stores lifecycle data, decides policy, owns source profiles, writes catalog records directly, approves release, or creates public API/map payloads, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers / connectors | `connectors/kansas/kgs/`, `connectors/usgs/`, or accepted connector home |
| Source catalog profiles | `docs/sources/catalog/...` |
| Source descriptors / source registry entries | `data/registry/sources/geology/`, `data/registry/sources/kansas/`, or approved registry home |
| Geology doctrine and object meaning | `docs/domains/geology/...`, `contracts/domains/geology/` |
| JSON Schemas | `schemas/contracts/v1/domains/geology/` or accepted schema home |
| Policy, rights, sensitivity, release rules | `policy/...` responsibility roots |
| Declarative run specs | `pipeline_specs/geology/...` |
| Fixtures | `fixtures/domains/geology/bedrock_units/` or accepted fixture home |
| Tests | `tests/pipelines/domains/geology/bedrock_units/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Surficial / unconsolidated cover units | `pipelines/domains/geology/surficial_units/` and related contracts |
| Borehole logs, well logs, cores, cuttings, and well tops | `pipelines/domains/geology/boreholes/`, `pipelines/domains/geology/well_logs/`, and related contracts |
| Mineral occurrences, resources, extraction, or reclamation context | Natural-resources / mineral-occurrence responsibility roots |
| Soil map units, hydrology measurements, hazards risk, or archaeology truth | Owning domain roots |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Release decisions and manifests | `release/...` responsibility roots |

[⬆ Back to top](#top)

---

## 6. Bedrock-unit scope

| Scope area | Pipeline responsibility | Failure behavior |
|---|---|---|
| Source identity | Preserve source id, descriptor refs, rights, source role, product, version, and map scale. | Quarantine if missing. |
| Unit identity | Preserve map-unit symbol, native label, formation/member/group refs, lithology, and age. | Quarantine on unresolved identity. |
| Boundary version | Preserve geometry refs, source vintage, CRS, compilation scale, uncertainty, and digest. | Quarantine on ambiguity or drift. |
| Contacts/structures | Preserve source relation and structure evidence. | Deny silent fault/contact reinterpretation. |
| Stratigraphy | Carry interval and correlation refs as evidence-bound interpretation. | Deny if promoted to map fact without support. |
| Cross-lane context | Prepare advisory links to Surficial, Soil, Hydrology, Hazards, Habitat, Resources, and Infrastructure. | Deny if owning-domain refs or policy are missing. |
| Public-safe geometry | Prepare generalized/simplified candidates only with transform receipts. | Fail closed if unresolved. |
| Release handoff | Prepare public-safe candidates only after evidence and policy closure. | No direct publication. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Geology bedrock-units run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, immutable raw captures, work inputs, quarantine inputs in remediation mode, or prior processed bedrock baselines.
2. **Normalize** into Geology work candidates with source role, unit identity, boundary version, geometry refs, source vintage, map scale, lithology/age refs, stratigraphy refs, structure refs, evidence refs, policy refs, and receipt refs.
3. **Quarantine** missing source descriptor, missing map-unit symbol, unresolved unit name, invalid boundary version, geometry/CRS ambiguity, unsupported reinterpretation, source-role collapse, rights failure, evidence gap, schema drift, or validation failure.
4. **Emit receipts** with input refs, source refs, unit refs, boundary refs, transform refs, validation refs, output refs, and outcomes.
5. **Support promotion** only by feeding downstream validation and review workflows.
6. **Never publish directly.**

Bedrock-unit processing is a lifecycle transformation. It is not catalog closure, release approval, or public artifact creation by itself.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Geology bedrock-units run must check or explicitly fail closed on:

1. **Input lifecycle gate** — input is fixture, raw capture, work input, quarantine-remediation input, or accepted baseline.
2. **Source descriptor gate** — source identity, role, rights, citation, cadence/vintage, and sensitivity posture are known.
3. **Source-role gate** — mapped source boundaries, interpretations, generalized derivatives, modeled surfaces, and generated summaries remain distinct.
4. **Unit identity gate** — source map-unit symbol, native label, lithostratigraphic refs, lithology, age, and vocabulary refs are explicit.
5. **Boundary-version gate** — geometry refs, CRS, compilation scale, source version, digest, and transform lineage are explicit.
6. **Structure/contact gate** — contacts, faults, folds, and structure features carry source or method support.
7. **Stratigraphy/correlation gate** — stratigraphic interval and correlation assertions preserve interpretation state and uncertainty.
8. **Cross-lane ownership gate** — bedrock context does not become Surficial, Soil, Hydrology, Hazards, Mineral Resource, Archaeology, Habitat, or Infrastructure truth.
9. **Public-safe geometry gate** — simplification/generalization/redaction/tiling transforms are explicit before release-facing handoff.
10. **Evidence gate** — claim-bearing downstream candidates can resolve EvidenceBundle support or abstain.
11. **Policy/sensitivity gate** — unresolved rights, controlled joins, exact exposure risk, or public-safe transform gaps fail closed.
12. **Schema/contract gate** — candidates match accepted Geology schema and `GeologicUnit` / `GeologyBoundaryVersion` semantics.
13. **Correction/rollback gate** — release-facing handoff includes correction path and rollback target expectations.
14. **No-direct-publish gate** — no writes to public UI, public API, published layers, or release manifests as a pipeline side effect.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/geology/bedrock_units/
├── README.md                         # this file
├── BEDROCK_UNITS_PIPELINE_CONTRACT.md # PROPOSED: bedrock-unit execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/generalized fixture only
├── normalize_bedrock_candidate.py    # PROPOSED
├── preserve_map_unit_identity.py     # PROPOSED
├── normalize_lithostratigraphy.py    # PROPOSED
├── validate_boundary_version.py      # PROPOSED
├── validate_geometry_crs_scale.py    # PROPOSED
├── validate_source_role.py           # PROPOSED
├── validate_cross_lane_ownership.py  # PROPOSED
├── validate_public_safe_geometry.py  # PROPOSED
├── route_quarantine.py               # PROPOSED
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/geology/bedrock_units.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted lifecycle homes under `data/work/geology/`, `data/quarantine/geology/`, `data/processed/geology/`, `data/catalog/domain/geology/`, `data/triplets/geology/`, `data/published/layers/geology/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/geology/bedrock_units/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Raw source capture | `data/raw/geology/<source_id>/<run_id>/` | Immutable source-edge capture with descriptor and receipt. |
| Work candidate | `data/work/geology/<run_id>/` | Candidate only. |
| Quarantine record | `data/quarantine/geology/<reason>/<run_id>/` | Failed, restricted, unresolved, or unsafe material. |
| Processed bedrock record | `data/processed/geology/<dataset_id>/<version>/` | Only after validation and governed promotion. |
| Catalog/triplet handoff | `data/catalog/domain/geology/`, `data/triplets/geology/` | Projection only; not publication. |
| Receipt | `data/receipts/pipeline/geology/bedrock_units/<run_id>.yml` or accepted receipt home | Records inputs, units, boundaries, transforms, checks, outputs. |
| Evidence proof | `data/proofs/evidence_bundle/` or accepted proof home | Required for claim-bearing records. |
| Release handoff | `release/candidates/geology/` | Reviewable, release-gated output only. |

[⬆ Back to top](#top)

---

## 11. Minimal bedrock-unit candidate record

The final schema is not defined here. This example shows the minimum information a Geology bedrock-unit candidate should preserve.

```yaml
schema_version: kfm.geology_bedrock_unit_candidate.v1
candidate_id: geology_bedrock_<source_id>_<unit_code>_<boundary_version>_<hash>
pipeline_id: domains.geology.bedrock_units
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: <GeologicUnit|Lithology|StratigraphicInterval|GeologyBoundaryVersion|StructureFeature>
source:
  source_id: <source_id>
  source_role: <observed|authority|interpretation|model|aggregate|generated_context|synthetic>
  source_product: <bedrock_geology_map|geologic_map|boundary_version|derivative|other>
  lifecycle_ref: data/raw/geology/<source_id>/<run_id>/
  input_hash: sha256:<hash>
  rights_state: needs_review
unit_identity:
  native_unit_code: null
  native_unit_label: null
  formal_unit_name: null
  rank: <group|formation|member|bed|unknown>
  lithology_terms: []
  geologic_age: null
boundary:
  boundary_version_id: null
  geometry_ref: null
  crs: null
  compilation_scale: null
  source_vintage: null
  public_safe_transform_ref: null
relations:
  contacts: []
  structure_refs: []
  stratigraphic_interval_refs: []
  cross_section_refs: []
policy:
  outcome: ABSTAIN
  reason_code: SOURCE_DESCRIPTOR_UNIT_BOUNDARY_POLICY_OR_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
anti_collapse:
  bedrock_unit_is_surficial_unit: false
  bedrock_unit_is_soil_mapunit: false
  bedrock_context_is_hazard_risk: false
  stratigraphic_correlation_is_map_fact: false
  generated_summary_is_evidence: false
outputs:
  candidate_record: data/work/geology/run_YYYYMMDDThhmmssZ/bedrock_unit_candidate.yml
  receipt: data/receipts/pipeline/geology/bedrock_units/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until source activation, bedrock-units spec, evidence, policy, sensitivity, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/geology/bedrock_units/
├── test_no_network_dry_run.py              # PROPOSED
├── test_source_descriptor_required.py      # PROPOSED
├── test_map_unit_identity_required.py      # PROPOSED
├── test_boundary_version_required.py       # PROPOSED
├── test_source_role_preserved.py           # PROPOSED
├── test_bedrock_not_surficial_unit.py      # PROPOSED
├── test_bedrock_not_soil_mapunit.py        # PROPOSED
├── test_correlation_not_map_fact.py        # PROPOSED
├── test_geometry_crs_scale_required.py     # PROPOSED
├── test_public_safe_transform_required.py  # PROPOSED
├── test_evidence_gap_abstains.py           # PROPOSED
├── test_quarantine_on_schema_failure.py    # PROPOSED
├── test_receipt_hashes.py                  # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, source descriptors are required, map-unit identity and boundary versions are preserved, bedrock units do not become surficial/soil/hazard/resource truth, public-safe transforms are required for release-facing outputs, receipts are deterministic, and no run writes directly to public UI, public API, catalog store, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Geology bedrock-units pipelines may prepare candidates and handoff packages. They do not publish.

Required chain:

```text
admitted bedrock source capture
  -> bedrock-unit work candidate
  -> validation report
  -> policy decision
  -> EvidenceBundle closure
  -> processed GeologicUnit / GeologyBoundaryVersion record
  -> catalog / triplet candidate
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, restricted, stale, conflicted, and quarantined bedrock runs remain auditable;
- receipts preserve source refs, map-unit refs, lithostratigraphic refs, boundary-version refs, transform refs, evidence refs, source-role refs, policy outcomes, and failure reasons;
- processed versions are produced by governed promotion, not hidden overwrite;
- downstream artifacts are invalidated if source refs, map-unit refs, boundary-version refs, public-safe transform refs, EvidenceBundle refs, policy refs, source-role refs, correction refs, or rollback refs drift;
- release rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/geology/bedrock_units/README.md` file;
- identifies this directory as a nested executable Geology bedrock-units sublane;
- prevents connector, source-profile, schema, contract, policy, fixture, test, data, proof, catalog, graph, public API, UI, cross-domain truth, and release authority from being placed here;
- preserves `GeologicUnit`, `Lithology`, `StratigraphicInterval`, `GeologicAge`, `StructureFeature`, `GeologyBoundaryVersion`, map-unit identity, boundary versions, source roles, cross-lane ownership, public-safe geometry, evidence, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- blocks bedrock-unit-as-surficial-unit, bedrock-unit-as-soil-mapunit, bedrock-context-as-hazard-risk, correlation-as-map-fact, generated-summary-as-evidence, and direct publication writes;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has source-descriptor coverage, synthetic/generalized no-network fixtures, schema-backed candidates, contract conformance, map-unit/boundary/source-role/evidence/policy/no-direct-publish tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `GEOL-BEDROCK-001` | Should bedrock-unit execution remain one sublane, or split by source family such as KGS bedrock maps, USGS NGMDB/GeMS, county maps, and derived boundary versions? | NEEDS VERIFICATION / ADR |
| `GEOL-BEDROCK-002` | Which source-edge jobs own KGS/USGS bedrock source retrieval before this sublane reads lifecycle inputs? | NEEDS VERIFICATION |
| `GEOL-BEDROCK-003` | Which schema owns `GeologicUnit`, `Lithology`, `StratigraphicInterval`, `GeologyBoundaryVersion`, and quarantine reasons? | NEEDS VERIFICATION |
| `GEOL-BEDROCK-004` | Which first-wave source is approved for fixture-only dry runs: KGS bedrock map, USGS NGMDB/GeMS, county map extracts, or synthetic units? | NEEDS VERIFICATION |
| `GEOL-BEDROCK-005` | Which CI job owns Geology bedrock-unit invariant tests? | UNKNOWN |
| `GEOL-BEDROCK-006` | What public-safe generalization, scale, and attribute include-list levels are allowed for released bedrock map layers? | NEEDS VERIFICATION |
| `GEOL-BEDROCK-007` | Which receipt type owns boundary simplification, projection, source-vintage reconciliation, and unit-symbol normalization? | PROPOSED / NEEDS ADR |

---

## Maintainer note

Start with synthetic/generalized fixture-only dry runs and negative tests. Do not add live source fetching, source-profile editing, schema authority, policy authority, direct catalog writes, public ungated layers, release-manifest writes, or generated geology summaries until source roles, map-unit identity, boundary versions, EvidenceBundle closure, public-safe transforms, release review, and rollback are proven.
