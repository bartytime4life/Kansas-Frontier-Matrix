<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-settlement-readme
title: pipeline_specs/settlement/ — Pipeline Specification Boundary
type: readme
version: v1.0
status: documentation-only; proposed-compatibility; read-only
owners: OWNER_TBD — pipeline-spec steward; domain steward; validation reviewer
created: 2026-06-13
updated: 2026-08-30
policy_label: public-metadata; compatibility-proposal; declarative-only; fail-closed
owning_root: pipeline_specs/
responsibility: document a proposed read-only mapping to pipeline_specs/settlements-infrastructure/ without creating parallel authority
truth_posture: CONFIRMED README-only boundary / PROPOSED target mapping / NEEDS VERIFICATION accepted registration and consumers
readme_profile: BOUNDARY_COMPACT
current_path: pipeline_specs/settlement/README.md
inherited_parent: pipeline_specs/README.md
scope_id: settlement
proposed_target: pipeline_specs/settlements-infrastructure/
target_status: PROPOSED_PENDING_REGISTRATION
related:
  - pipeline_specs/README.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - contracts/pipeline_spec_declaration.md
  - schemas/contracts/v1/pipeline_spec_declaration.schema.json
notes: ["Metadata is flat by contract; validation does not activate a source, pipeline, lifecycle write, release, or publication."]
[/KFM_META_BLOCK_V2] -->

# `pipeline_specs/settlement/` compatibility boundary

## Purpose and inherited parent

This lane inherits the declarative-only contract in [`pipeline_specs/`](../README.md). It preserves the legacy singular `settlement` path while [`pipeline_specs/settlements-infrastructure/`](../settlements-infrastructure/README.md) remains the proposed target recorded in the unresolved-alias register. The mapping is not yet an accepted canonical-path decision.

This is not a second writable authority. A path, README, merge, or reference to this lane never activates execution.

## Local owner and scope

- Scope ID: `kfm.pipeline_specs.compatibility.settlement`
- Local owner: `OWNER_TBD — Settlements/Infrastructure pipeline-spec steward`
- Governance reviewer: `OWNER_TBD — directory-governance reviewer`
- Boundary class: `proposed compatibility`
- Proposed target: `pipeline_specs/settlements-infrastructure/` (`NEEDS_VERIFICATION`)

## Belongs

- This compatibility notice.
- Proposed redirect or migration notes that point one way to `settlements-infrastructure/` without claiming accepted registration.
- A future retirement record after references and consumers are closed.

## Prohibited

- Pipeline declarations, schedules, source bindings, or resource envelopes.
- Executable acquisition, transformation, geocoding, or publication code.
- Contracts, schemas, policy, fixtures, tests, receipts, evidence, or release decisions.
- Any write that would make `settlement/` a parallel authority.
- Sensitive address, parcel, infrastructure, household, or living-person data.

## Inputs and outputs

| Direction | Allowed |
|---|---|
| Input | Verified legacy references requiring compatibility guidance |
| Output | A human-readable pointer to `pipeline_specs/settlements-infrastructure/` |
| Runtime effects | None |

Network access, lifecycle writes, source activation, promotion, release, and publication are `DENIED`.

## Exposure, mutation, and retention

- Exposure: repository documentation; it carries no public-data or operational authority.
- Mutation: read-only compatibility text. New declarations belong in the canonical target after review.
- Retention: keep only while a verified compatibility need exists.
- Sensitivity: exact addresses, ownership clues, protected infrastructure, and restricted operational details are prohibited.

## Current direct-child map

Verified 2026-08-30. Direct children only:

```text
settlement/
└── README.md  # read-only compatibility contract
```

## Declaration inventory

| Kind | Count | Status |
|---|---:|---|
| Pipeline YAML declarations | 0 | No active or inactive declarations live here |
| Schema-backed JSON profiles | 0 | None |

The removed `.gitkeep` was redundant because this README retains the directory.

## Validation

- Confirm the direct-child map matches the tracked tree.
- Confirm no YAML, JSON, executable, secret, sensitive payload, or generated output is added here.
- Confirm proposed migration guidance points only to `pipeline_specs/settlements-infrastructure/` and remains labeled unresolved.
- Run the repository documentation meta-block and link checks.
- Run the repository topology and path-alias validators.

## Related governed families

- Parent: [`pipeline_specs/README.md`](../README.md)
- Target: [`pipeline_specs/settlements-infrastructure/`](../settlements-infrastructure/README.md)
- Common declaration contract: [`contracts/pipeline_spec_declaration.md`](../../contracts/pipeline_spec_declaration.md)
- Common declaration schema: [`schemas/contracts/v1/pipeline_spec_declaration.schema.json`](../../schemas/contracts/v1/pipeline_spec_declaration.schema.json)
- Common fixtures: [`fixtures/contracts/v1/pipeline_spec_declaration/`](../../fixtures/contracts/v1/pipeline_spec_declaration/)
- Common tests: [`tests/validators/test_validate_pipeline_spec_declarations.py`](../../tests/validators/test_validate_pipeline_spec_declarations.py)
- Policy root: [`policy/`](../../policy/README.md)
- Settlement release compatibility family: [`release/candidates/settlement/`](../../release/candidates/settlement/README.md)
- Canonical release family: [`release/candidates/settlements-infrastructure/`](../../release/candidates/settlements-infrastructure/README.md)
- Accepted governance: [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) and [Directory Rules v2](../../docs/doctrine/directory-rules.md)

These links establish routing only. They do not establish activation, evidence closure, or release approval.

## Status and open verification

Status is `documentation-only proposed compatibility`. No pipeline declaration is active here, and this README does not accept the unresolved alias.

Open verification items:

- Name the owning steward.
- Record an accepted alias or canonical-path decision before treating the target as authoritative.
- Inventory repository and external consumers of the singular path.
- Record a retirement date and decision only after zero-consumer evidence exists.
- Decide whether a machine-readable alias is required; until then, `HOLD` rather than invent one.

## Review triggers and rollback

Re-review when canonical path policy, consumers, owners, validation, sensitivity, exposure, or the compatibility deadline changes; when an ADR changes; or when drift, correction, withdrawal, or rollback occurs.

Rollback this documentation change by reverting its commit. Rollback must not recreate `.gitkeep`, add declarations here, or restore two writable authorities. If a legacy consumer blocks retirement, preserve this pointer and open a governed path decision.
