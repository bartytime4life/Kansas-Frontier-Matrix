<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-hydrology-readme
title: pipeline_specs/hydrology/ — Pipeline Specification Boundary
type: readme
version: v1.0
status: proposed-inactive; repository-grounded
owners: OWNER_TBD — pipeline-spec steward; domain steward; validation reviewer
created: 2026-06-13
updated: 2026-08-30
policy_label: public-metadata; declarative-only; fail-closed; no-live-activation
owning_root: pipeline_specs/
responsibility: govern inactive declarative pipeline intent for the hydrology scope
truth_posture: CONFIRMED inventory and fail-closed posture / PROPOSED declarations / NEEDS VERIFICATION activation prerequisites
readme_profile: BOUNDARY_COMPACT
current_path: pipeline_specs/hydrology/README.md
inherited_parent: pipeline_specs/README.md
scope_id: hydrology
related:
  - pipeline_specs/README.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - contracts/pipeline_spec_declaration.md
  - schemas/contracts/v1/pipeline_spec_declaration.schema.json
notes: ["Metadata is flat by contract; validation does not activate a source, pipeline, lifecycle write, release, or publication."]
[/KFM_META_BLOCK_V2] -->

# Hydrology pipeline declaration boundary

`pipeline_specs/hydrology/` is the declarative Hydrology lane inherited from [`pipeline_specs/`](../README.md). It records inactive run-graph proposals and one bounded fixture-first implementation binding.

Directory Rules v2 is adopted by [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md). This README applies its `BOUNDARY_COMPACT` profile.

> [!IMPORTANT]
> File presence does not activate execution. Every declaration is `PROPOSED_INACTIVE`; network access, source activation, lifecycle writes, promotion, release, and publication remain `DENIED`. WBD fixture execution writes no lifecycle target.

> [!CAUTION]
> A watershed boundary is context, not observed flow. A gauge value is source-, unit-, datum-, station-, and time-bound. Flood-hazard layers do not establish current inundation or replace official determinations, warnings, engineering, water-quality, or safety guidance.

## Owner and scope

- Local owners: pipeline-spec and Hydrology stewards; names remain `OWNER_TBD`.
- Scope ID: `kfm://scope/pipeline-specs/hydrology`.
- Local authority: inactive declarations, implementation bindings, candidate lifecycle edges, required gates, and rollback metadata.
- Inherited authority: lifecycle, evidence, public-boundary, correction, and rollback controls from the parent.

## Belongs / prohibited

Belongs here:

- Hydrology stage boundaries, source candidates, compatibility declarations, and fixture-first bindings;
- references to admitted sources, semantic contracts, schemas, fixtures, tests, workflows, and gates;
- explicit disabled or fixture-only execution posture and non-effects.

Prohibited here:

- live network orchestration, executable transformations, schedules, payloads, credentials, or runtime state;
- claims of current water level, discharge, flood, drought, water quality, jurisdiction, or public safety;
- source admission, policy, evidence, catalog, promotion, release, or publication authority;
- parallel NHDPlus or WBD authority without an explicit target and reviewed migration.

## Inputs and outputs

- Candidate inputs: source-capture candidates, fixture packages, and governed lifecycle references.
- Candidate outputs: possible `RAW`, `WORK`, `QUARANTINE`, `PROCESSED`, catalog, or release candidates; declarations write none.
- WBD fixture-only output may be emitted to stdout or an explicit new file for tests; `writes_targets: false` remains mandatory.
- Permitted writers: reviewed repository changes and bounded test output only; no lifecycle or public writer is authorized.

## Exposure, mutation, and retention

- Exposure: public configuration metadata and synthetic or bounded fixtures only.
- Mutation: source, feature identity, CRS, datum, unit, station, time, geometry, placement, or lifecycle changes require review.
- Retention: version-control history and reviewed supersession / compatibility lineage.
- Physical hydrology observations, boundaries, regulated records, and operational feeds do not belong here.

## Current direct-child map

```text
pipeline_specs/hydrology/
├── README.md                       # This boundary contract
├── catalog.yaml                    # Inactive CATALOG boundary
├── ingest.yaml                     # Inactive INGEST boundary
├── ingest_nfhl.yaml                # Inactive NFHL ingest candidate
├── ingest_nhdplus_hr.yaml          # Inactive NHDPlus ingest; placement HOLD
├── ingest_usgs_nwis.yaml           # Inactive NWIS ingest candidate
├── ingest_wbd.yaml                 # Inactive compatibility alias to WBD HUC12
├── nfhl_context.yaml               # Inactive NFHL context derivation
├── nhdplus_hr_ingest.yaml          # Inactive NHDPlus ingest; placement HOLD
├── normalize.yaml                  # Inactive NORMALIZE boundary
├── publish.yaml                    # Inactive PUBLISH boundary
├── usgs_water_observations.yaml    # Inactive observations derivation
├── validate.yaml                   # Inactive VALIDATE boundary
└── wbd_huc12_ingest.yaml           # Inactive fixture-first binding
```

## Declaration inventory

| Declaration | Kind / stage | Status | Implementation |
|---|---|---|---|
| `ingest.yaml` | `STAGE_BOUNDARY / INGEST` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `normalize.yaml` | `STAGE_BOUNDARY / NORMALIZE` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `validate.yaml` | `STAGE_BOUNDARY / VALIDATE` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `catalog.yaml` | `STAGE_BOUNDARY / CATALOG` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `publish.yaml` | `STAGE_BOUNDARY / PUBLISH` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `ingest_nfhl.yaml` | `PIPELINE_CANDIDATE / INGEST` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `ingest_usgs_nwis.yaml` | `PIPELINE_CANDIDATE / INGEST` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `nfhl_context.yaml` | `PIPELINE_CANDIDATE / DERIVE` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `usgs_water_observations.yaml` | `PIPELINE_CANDIDATE / DERIVE` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED` |
| `ingest_nhdplus_hr.yaml` | `PIPELINE_CANDIDATE / INGEST` | `PROPOSED_INACTIVE`; `HOLD` | `NOT_IMPLEMENTED` |
| `nhdplus_hr_ingest.yaml` | `PIPELINE_CANDIDATE / INGEST` | `PROPOSED_INACTIVE`; `HOLD` | `NOT_IMPLEMENTED` |
| `ingest_wbd.yaml` | `COMPATIBILITY_ALIAS / INGEST` | `PROPOSED_INACTIVE` | `NOT_IMPLEMENTED`; target `wbd_huc12_ingest.yaml` |
| `wbd_huc12_ingest.yaml` | `PIPELINE_CANDIDATE / INGEST` | `PROPOSED_INACTIVE` | `IMPLEMENTED_FIXTURE_FIRST` |

All thirteen YAML files use `KfmPipelineSpecDeclaration`. `IMPLEMENTED_FIXTURE_FIRST` means deterministic no-network test behavior only; it does not mean live readiness.

## WBD fixture-first boundary

The WBD binding may reference its producer, source descriptor, contracts, schemas, fixture package, tests, and dedicated workflow. It must retain:

- `execution.mode: FIXTURE_ONLY` and `network_access: DENIED`;
- `source_activation`, `lifecycle_write`, `promotion`, `release`, and `publication` as `DENIED`;
- `lifecycle.writes_targets: false`;
- deterministic valid/invalid fixture behavior and no live WBD request.

## Validation

```bash
python tools/validators/validate_pipeline_spec_declarations.py
python -m pytest tests/validators/test_validate_pipeline_spec_declarations.py -q
python -m pytest tests/pipelines/domains/hydrology/test_wbd_huc12_ingest_candidate.py tests/validators/domains/hydrology/wbd_huc12_material_change/test_validate_wbd_huc12_material_change.py -q --strict-config --strict-markers
```

Passing tests do not activate the source, schedule a run, write lifecycle data, or authorize publication.

## Related authority families

- Common semantics: [`contracts/pipeline_spec_declaration.md`](../../contracts/pipeline_spec_declaration.md)
- Common shape: [`schemas/contracts/v1/pipeline_spec_declaration.schema.json`](../../schemas/contracts/v1/pipeline_spec_declaration.schema.json)
- Hydrology contracts / policy: `contracts/domains/hydrology/`, `policy/domains/hydrology/`
- Hydrology fixtures / tests: `fixtures/domains/hydrology/`, `tests/domains/hydrology/`
- Executable consumers: `pipelines/domains/hydrology/`
- Release candidates: `release/candidates/hydrology/`; declarations confer no release authority

## Status and open verification

- Status: repository-grounded and inactive; one fixture-first implementation binding exists.
- `HOLD / PLACEMENT_REVIEW_REQUIRED`: resolve `ingest_nhdplus_hr.yaml` versus `nhdplus_hr_ingest.yaml` without inventing a canonical target here.
- Verify named owners, source admission, rights, units, datums, temporal semantics, geometry lineage, sensitivity, and public-safe representation.
- Verify all fixture-first bindings and the WBD compatibility alias before any path or status change.

## Review triggers and rollback

Re-review on owner, source, consumer, station, unit, datum, time, geometry, CRS, placement, alias, execution mode, lifecycle, schema, workflow, correction, or governing ADR change.

Rollback is a reviewed revert. Keep declarations inactive, restore every denial, disable or revert fixture bindings, quarantine candidate outputs, and route any public correction through evidence and release authority rather than this directory.
