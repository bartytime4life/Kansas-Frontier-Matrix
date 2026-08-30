<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-flora-watchers-readme
title: pipeline_specs/flora/watchers/ — Pipeline Specification Boundary
type: readme
version: v1.0
status: proposed-inactive; placement-hold; repository-grounded
owners: OWNER_TBD — pipeline-spec steward; domain steward; validation reviewer
created: 2026-06-13
updated: 2026-08-30
policy_label: public-metadata; declarative-only; placement-review-required; fail-closed
owning_root: pipeline_specs/
responsibility: document the inactive flora/watchers boundary while canonical placement remains on HOLD
truth_posture: CONFIRMED inventory and denial posture / PROPOSED boundary / NEEDS VERIFICATION canonical placement
readme_profile: BOUNDARY_COMPACT
current_path: pipeline_specs/flora/watchers/README.md
inherited_parent: pipeline_specs/README.md
scope_id: flora/watchers
related:
  - pipeline_specs/README.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - contracts/pipeline_spec_declaration.md
  - schemas/contracts/v1/pipeline_spec_declaration.schema.json
notes: ["Metadata is flat by contract; validation does not activate a source, pipeline, lifecycle write, release, or publication."]
[/KFM_META_BLOCK_V2] -->

# Flora watcher placement boundary

`pipeline_specs/flora/watchers/` inherits from the [Flora declaration boundary](../README.md). It documents an unresolved placement seam; it is not an implemented watcher lane.

Directory Rules v2 is adopted by [ADR-0029](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md). This README applies its `BOUNDARY_COMPACT` profile.

> [!IMPORTANT]
> Status is `HOLD / PLACEMENT_REVIEW_REQUIRED`. No canonical target is asserted among this directory, `pipeline_specs/flora/plants_drift_watcher.yaml`, and `pipeline_specs/watchers/plants_drift.yaml`.

> [!CAUTION]
> Watch metadata, diffs, logs, and notifications can reveal rare-plant locations, private collections, restricted endpoints, license-limited fields, or culturally sensitive knowledge. They fail closed under reconstruction risk.

## Owner and scope

- Local owners: pipeline-spec, Flora, watcher, source-rights, sensitivity, evidence, and release stewards; names remain `OWNER_TBD`.
- Scope ID: `kfm://scope/pipeline-specs/flora/watchers`.
- Local scope: placement documentation only until an accepted decision assigns authority.
- Inherited parent: `pipeline_specs/flora/`.

## Belongs / prohibited

Belongs here:

- this boundary contract;
- future declarations only after an accepted placement decision and migration plan.

Prohibited here:

- executable watcher code, schedules, credentials, endpoints, payloads, or runtime state;
- source admission, content truth, materiality, policy, evidence, promotion, release, or notification authority;
- mirrored or duplicate declarations that create parallel authority;
- exact or reconstructable sensitive Flora details.

## Inputs and outputs

- Current inputs: parent governance and repository placement evidence only.
- Current outputs: no pipeline or watcher outputs.
- Permitted writers: reviewed documentation changes while placement is on hold.
- Runtime, network, lifecycle, promotion, release, and publication writers are denied.

## Exposure, mutation, and retention

- Exposure: public boundary metadata only; no sensitive examples.
- Mutation: placement-affecting edits require Flora, watcher, and directory-governance review.
- Retention: version-control history until the seam is resolved by migration.
- `.gitkeep` is unnecessary because this README retains the directory.

## Current direct-child map

```text
pipeline_specs/flora/watchers/
└── README.md                       # Placement boundary; no declarations
```

## Declaration inventory

There are no declarations in this directory. Consequently, there is no active parser binding, source binding, schedule, or executable consumer here.

Related declarations outside this boundary are evidence of an unresolved seam, not authority:

| External path | Current posture |
|---|---|
| `pipeline_specs/flora/plants_drift_watcher.yaml` | `KfmPipelineSpecDeclaration`; `PROPOSED_INACTIVE`; `NOT_IMPLEMENTED`; placement `HOLD` |
| `pipeline_specs/watchers/plants_drift.yaml` | `KfmPipelineSpecDeclaration`; `PROPOSED_INACTIVE`; `NOT_IMPLEMENTED`; placement review required |

## Safety posture

- File presence does not activate execution.
- Network access and source activation remain `DENIED`.
- Lifecycle writes, promotion, release, publication, and public notification remain `DENIED`.
- A detected source change is not admission, domain truth, evidence closure, or release approval.

## Validation

Run the repository-wide declaration checks from the repository root:

```bash
python tools/validators/validate_pipeline_spec_declarations.py
python -m pytest tests/validators/test_validate_pipeline_spec_declarations.py -q
```

Also verify that no declaration is introduced here before the placement hold is resolved and that no parallel authority is created.

## Related authority families

- Common semantics: [`contracts/pipeline_spec_declaration.md`](../../../contracts/pipeline_spec_declaration.md)
- Common shape: [`schemas/contracts/v1/pipeline_spec_declaration.schema.json`](../../../schemas/contracts/v1/pipeline_spec_declaration.schema.json)
- Flora contracts / policy: `contracts/domains/flora/`, `policy/domains/flora/`
- Flora fixtures / tests: `fixtures/domains/flora/`, `tests/domains/flora/`
- Executable watchers: `pipelines/watchers/` or a verified domain consumer, subject to placement review
- Release candidates: `release/candidates/flora/`; this boundary cannot authorize them

## Status and open verification

- `HOLD / PLACEMENT_REVIEW_REQUIRED` remains the only safe placement outcome.
- Verify consumers, domain specificity, shared-watcher criteria, source ownership, rights, sensitivity, and migration dependencies.
- Record any canonical-target decision in accepted authority before moving or duplicating a declaration.
- Keep all candidate declarations `PROPOSED_INACTIVE` throughout review.

## Review triggers and rollback

Re-review when a watcher declaration, consumer, source, schedule, output, sensitivity posture, path, alias, or governing ADR changes.

Rollback is a reviewed revert of the bounded documentation or migration change. If a move creates ambiguity, restore the last single-authority layout, keep both candidates inactive, and escalate rather than selecting a target by convention.
