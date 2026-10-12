<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-soil-readme
title: pipeline_specs/soil/ — Pipeline Specification Boundary
type: readme
version: v1.0
status: proposed-inactive; repository-grounded
owners: OWNER_TBD — pipeline-spec steward; domain steward; validation reviewer
created: 2026-06-13
updated: 2026-08-30
policy_label: public-metadata; declarative-only; fail-closed; no-live-activation
owning_root: pipeline_specs/
responsibility: govern inactive declarative pipeline intent for the soil scope
truth_posture: CONFIRMED inventory and fail-closed posture / PROPOSED declarations / NEEDS VERIFICATION activation prerequisites
readme_profile: BOUNDARY_COMPACT
current_path: pipeline_specs/soil/README.md
inherited_parent: pipeline_specs/README.md
scope_id: soil
related:
  - pipeline_specs/README.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - contracts/pipeline_spec_declaration.md
  - schemas/contracts/v1/pipeline_spec_declaration.schema.json
notes: ["Metadata is flat by contract; validation does not activate a source, pipeline, lifecycle write, release, or publication."]
[/KFM_META_BLOCK_V2] -->

# Soil pipeline declaration boundary

`pipeline_specs/soil/` is the declarative Soil lane inherited from [`pipeline_specs/`](../README.md). It owns inactive pipeline and schema-specific profile declarations, not executable processing or soil truth.

Directory Rules v2 is adopted by [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md). This README applies its `BOUNDARY_COMPACT` profile.

> [!IMPORTANT]
> File presence does not activate execution. All declarations are `PROPOSED_INACTIVE`; network access, source activation, lifecycle writes, promotion, release, and publication remain `DENIED`.

> [!CAUTION]
> Static survey units, gridded derivatives, station observations, satellite estimates, pedon/profile evidence, and interpretations are not interchangeable. Each retains source role, spatial support, depth, time, uncertainty, and use limits. Parcel, operator, farm, or management joins require separate sensitivity and policy review.

## Owner and scope

- Local owners: pipeline-spec and Soil stewards; names remain `OWNER_TBD`.
- Scope ID: `kfm://scope/pipeline-specs/soil`.
- Local authority: inactive YAML stage declarations and established schema-specific JSON profiles.
- Inherited authority: lifecycle, evidence, public-boundary, correction, and rollback controls from the parent.

## Belongs / prohibited

Belongs here:

- inactive Soil stage boundaries;
- schema-backed support-type, time-caveat, materiality, and yearly-diff configuration profiles;
- explicit references, governance denials, canonical hashes, gates, and rollback metadata.

Prohibited here:

- executable ingestion, interpolation, classification, interpretation, modeling, or scheduling;
- credentials, raw observations, soil payloads, parcel or operator records, and runtime state;
- source admission, scientific or agronomic truth, policy, evidence, catalog, promotion, release, or publication authority;
- collapse of distinct support types, times, depths, methods, uncertainties, or source roles.

## Inputs and outputs

- Candidate inputs: admitted source captures and governed lifecycle references with explicit support, depth, time, method, and uncertainty.
- Candidate outputs: possible lifecycle or review candidates; inactive declarations write none.
- Permitted writers: reviewed repository changes only. Executable and lifecycle writers remain outside this boundary.
- Schema-specific profiles may constrain a verified consumer; they do not activate it.

## Exposure, mutation, and retention

- Exposure: public configuration metadata; examples must avoid sensitive property, person, operator, or exact-location joins.
- Mutation: support type, alias, time caveat, threshold, hash dimension, comparison, unit, or source-role changes require fixture-backed review.
- Retention: version-control history and explicit version / supersession lineage.
- Physical survey, observation, grid, model, interpretation, receipt, and release payload storage is prohibited.

## Current direct-child map

```text
pipeline_specs/soil/
├── README.md                              # This boundary contract
├── catalog.yaml                           # Inactive CATALOG boundary
├── ingest.yaml                            # Inactive INGEST boundary
├── normalize.yaml                         # Inactive NORMALIZE boundary
├── promotion_materiality_profile.v1.json  # Inactive promotion materiality profile
├── publish.yaml                           # Inactive PUBLISH boundary
├── ssurgo_yearly_diff_profile.v1.json     # Inactive yearly-diff profile
├── support_type_alias_map.v1.json         # Inactive support-type aliases
├── support_type_profile.v1.json           # Inactive support-type profile
├── time_caveat_profile.v1.json            # Inactive time-caveat profile
└── validate.yaml                          # Inactive VALIDATE boundary
```

## Declaration inventory

| Declaration | Kind / object type | Status | Implementation posture |
|---|---|---|---|
| `ingest.yaml` | `STAGE_BOUNDARY / INGEST` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `normalize.yaml` | `STAGE_BOUNDARY / NORMALIZE` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `validate.yaml` | `STAGE_BOUNDARY / VALIDATE` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `catalog.yaml` | `STAGE_BOUNDARY / CATALOG` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `publish.yaml` | `STAGE_BOUNDARY / PUBLISH` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `promotion_materiality_profile.v1.json` | `SoilPromotionMaterialityProfile` | `PROPOSED_INACTIVE` | Schema-specific profile |
| `ssurgo_yearly_diff_profile.v1.json` | `SoilYearlyDiffProfile` | `PROPOSED_INACTIVE` | Schema-specific profile |
| `support_type_alias_map.v1.json` | `SoilSupportTypeAliasMap` | `PROPOSED_INACTIVE` | Schema-specific alias map |
| `support_type_profile.v1.json` | `SoilSupportTypeProfile` | `PROPOSED_INACTIVE` | Schema-specific profile |
| `time_caveat_profile.v1.json` | `SoilTimeCaveatProfile` | `PROPOSED_INACTIVE` | Schema-specific profile |

All five YAML files use `KfmPipelineSpecDeclaration`. The five JSON objects retain their established schema, validator, fixture, and canonicalization families; they are not silently converted.

## Safety posture

- A support-type alias cannot erase the canonical support type or source role.
- A yearly diff or materiality threshold is a review signal, not evidence closure, promotion, or release.
- Time caveats remain attached through transformations and public representations.
- File presence, schema validity, or hash validity activates nothing and grants no agronomic or management authority.

## Validation

Run the common YAML declaration checks plus the established Soil profile validators/tests:

```bash
python tools/validators/validate_pipeline_spec_declarations.py
python -m pytest tests/validators/test_validate_pipeline_spec_declarations.py -q
```

Profile validation must additionally verify each schema, deterministic hash where required, exact fixture polarity, canonical alias behavior, units and bounds, governance denials, and negative cases for support-type or temporal collapse.

## Related authority families

- Common YAML semantics: [`contracts/pipeline_spec_declaration.md`](../../contracts/pipeline_spec_declaration.md)
- Common YAML shape: [`schemas/contracts/v1/pipeline_spec_declaration.schema.json`](../../schemas/contracts/v1/pipeline_spec_declaration.schema.json)
- Soil contracts / policy: `contracts/domains/soil/`, `policy/domains/soil/`
- Soil fixtures / tests: `fixtures/domains/soil/`, `tests/domains/soil/`
- Executable consumers: `pipelines/domains/soil/`
- Release candidates: `release/candidates/soil/`; declarations confer no release authority

## Status and open verification

- Status: repository-grounded, declarative-only, and inactive.
- Verify named owners, admitted source roles, rights, support-type and time vocabularies, depth and unit handling, uncertainty, schema/validator coverage, and hash reproducibility.
- Verify alias mapping is one-way and cannot create parallel semantic authority.
- Verify each implementation, fixture, test, workflow, evidence, and release reference before any status change.

## Review triggers and rollback

Re-review on owner, source, support type, alias, unit, depth, time, uncertainty, threshold, hash dimension, consumer, schema, workflow, exposure, correction, or governing ADR change.

Rollback is a reviewed revert to the last validated declarations and hashes. Retain inactivity, restore every denial, invalidate affected candidates, quarantine derived outputs, and preserve correction lineage outside this directory.
