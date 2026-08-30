<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-air-readme
title: pipeline_specs/air/ — Pipeline Specification Boundary
type: readme
version: v1.0
status: documentation-only; proposed-compatibility; read-only
owners: OWNER_TBD — pipeline-spec steward; domain steward; validation reviewer
created: 2026-06-13
updated: 2026-08-30
policy_label: public-metadata; compatibility-proposal; declarative-only; fail-closed
owning_root: pipeline_specs/
responsibility: document a proposed read-only mapping to pipeline_specs/atmosphere/ without creating parallel authority
truth_posture: CONFIRMED README-only boundary / PROPOSED target mapping / NEEDS VERIFICATION accepted registration and consumers
readme_profile: BOUNDARY_COMPACT
current_path: pipeline_specs/air/README.md
inherited_parent: pipeline_specs/README.md
scope_id: air
proposed_target: pipeline_specs/atmosphere/
target_status: PROPOSED_PENDING_REGISTRATION
related:
  - pipeline_specs/README.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - contracts/pipeline_spec_declaration.md
  - schemas/contracts/v1/pipeline_spec_declaration.schema.json
notes: ["Metadata is flat by contract; validation does not activate a source, pipeline, lifecycle write, release, or publication."]
[/KFM_META_BLOCK_V2] -->

# `pipeline_specs/air/` compatibility boundary

## Purpose and inherited parent

This lane inherits the declarative-only contract in [`pipeline_specs/`](../README.md). It preserves the legacy `air` path while [`pipeline_specs/atmosphere/`](../atmosphere/README.md) remains the proposed target recorded in the unresolved-alias register. The mapping is not yet an accepted canonical-path decision.

This is not a second writable authority. A file path, README, merge, or reference to this lane never activates execution.

## Local owner and scope

- Scope ID: `kfm.pipeline_specs.compatibility.air`
- Local owner: `OWNER_TBD — Atmosphere/Air pipeline-spec steward`
- Governance reviewer: `OWNER_TBD — directory-governance reviewer`
- Boundary class: `proposed compatibility`
- Proposed target: `pipeline_specs/atmosphere/` (`NEEDS_VERIFICATION`)

## Belongs

- This compatibility notice.
- Proposed redirect or migration notes that point one way to `atmosphere/` without claiming accepted registration.
- A future retirement record after all consumers and references are checked.

## Prohibited

- Pipeline declarations, schedules, source bindings, or resource envelopes.
- Executable acquisition or transformation code.
- Contracts, schemas, policy, fixtures, tests, receipts, evidence, or release decisions.
- Any write that would make `air/` a parallel authority.
- Secrets, credentials, source payloads, or generated outputs.

## Inputs and outputs

| Direction | Allowed |
|---|---|
| Input | Verified legacy references requiring compatibility guidance |
| Output | A human-readable pointer to `pipeline_specs/atmosphere/` |
| Runtime effects | None |

Network access, lifecycle writes, source activation, promotion, release, and publication are `DENIED`.

## Exposure, mutation, and retention

- Exposure: repository documentation; it carries no public data authority.
- Mutation: read-only compatibility text. New declarations belong in the canonical target after review.
- Retention: keep only while a verified compatibility need exists.
- Sensitivity: do not place source endpoints, credentials, restricted observations, or operational detail here.

## Current direct-child map

Verified 2026-08-30. Direct children only:

```text
air/
├── .gitkeep   # retained zero-byte topology marker; no authority
└── README.md  # read-only compatibility contract
```

## Declaration inventory

| Kind | Count | Status |
|---|---:|---|
| Pipeline YAML declarations | 0 | No active or inactive declarations live here |
| Schema-backed JSON profiles | 0 | None |

The retained `.gitkeep` is a compatibility marker only. It is not a declaration,
registry entry, activation signal, or writable authority.

## Validation

- Confirm the direct-child map matches the tracked tree.
- Confirm no YAML, JSON, executable, secret, or generated payload is added here.
- Confirm all proposed migration guidance points to `pipeline_specs/atmosphere/` and remains labeled unresolved.
- Run the repository documentation meta-block and link checks.
- Run the repository topology and path-alias validators.

## Related governed families

- Parent: [`pipeline_specs/README.md`](../README.md)
- Target: [`pipeline_specs/atmosphere/`](../atmosphere/README.md)
- Common declaration contract: [`contracts/pipeline_spec_declaration.md`](../../contracts/pipeline_spec_declaration.md)
- Common declaration schema: [`schemas/contracts/v1/pipeline_spec_declaration.schema.json`](../../schemas/contracts/v1/pipeline_spec_declaration.schema.json)
- Common fixtures: [`fixtures/contracts/v1/pipeline_spec_declaration/`](../../fixtures/contracts/v1/pipeline_spec_declaration/)
- Common tests: [`tests/validators/test_validate_pipeline_spec_declarations.py`](../../tests/validators/test_validate_pipeline_spec_declarations.py)
- Policy root: [`policy/`](../../policy/README.md)
- Atmosphere release family: [`release/candidates/atmosphere/`](../../release/candidates/atmosphere/README.md)
- Accepted governance: [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) and [Directory Rules v2](../../docs/doctrine/directory-rules.md)

These links identify responsibility boundaries; they do not prove that a release, fixture set, or implementation is active.

## Status and open verification

Status is `documentation-only proposed compatibility`. No pipeline declaration is active here, and this README does not accept the unresolved alias.

Open verification items:

- Name the owning steward.
- Record an accepted alias or canonical-path decision before treating the target as authoritative.
- Inventory repository and external consumers of the legacy path.
- Record a retirement date and decision only after zero-consumer evidence exists.
- Decide whether a machine-readable alias is required; until then, `HOLD` rather than invent one.

## Review triggers and rollback

Re-review when canonical path policy, consumers, owners, validation, exposure, or the compatibility deadline changes; when an ADR changes; or when drift, correction, withdrawal, or rollback occurs.

Rollback this documentation change by reverting its commit. Rollback must not add declarations here or restore two writable authorities. If a legacy consumer blocks retirement, preserve this pointer and open a governed path decision.
