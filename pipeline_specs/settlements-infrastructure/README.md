<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-settlements-infrastructure-readme
title: pipeline_specs/settlements-infrastructure/ — Pipeline Specification Boundary
type: readme
version: v1.0
status: proposed-inactive; repository-grounded
owners: OWNER_TBD — pipeline-spec steward; domain steward; validation reviewer
created: 2026-06-13
updated: 2026-08-30
policy_label: public-metadata; declarative-only; fail-closed; no-live-activation
owning_root: pipeline_specs/
responsibility: govern inactive declarative pipeline intent for the settlements-infrastructure scope
truth_posture: CONFIRMED inventory and fail-closed posture / PROPOSED declarations / NEEDS VERIFICATION activation prerequisites
readme_profile: BOUNDARY_COMPACT
current_path: pipeline_specs/settlements-infrastructure/README.md
inherited_parent: pipeline_specs/README.md
scope_id: settlements-infrastructure
related:
  - pipeline_specs/README.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - contracts/pipeline_spec_declaration.md
  - schemas/contracts/v1/pipeline_spec_declaration.schema.json
notes: ["Metadata is flat by contract; validation does not activate a source, pipeline, lifecycle write, release, or publication."]
[/KFM_META_BLOCK_V2] -->

# `pipeline_specs/settlements-infrastructure/` boundary

## Purpose and inherited parent

This lane inherits [`pipeline_specs/`](../README.md) and owns declarative run intent for settlement and infrastructure data processing. It may describe what a governed pipeline could consume or produce under named gates. Executable behavior belongs in [`pipelines/domains/settlements-infrastructure/`](../../pipelines/domains/settlements-infrastructure/README.md).

[`pipeline_specs/settlement/`](../settlement/README.md) is a read-only compatibility pointer, not a second writable authority.

Declaration presence never activates execution. Network access, lifecycle writes, source activation, promotion, release, and publication are `DENIED` for every current declaration.

## Local owner and scope

- Scope ID: `settlements-infrastructure`
- Local owner: `OWNER_TBD — Settlements/Infrastructure pipeline-spec steward`
- Required reviewers: source/rights, privacy, infrastructure sensitivity, evidence, policy, validation, and release stewards
- Boundary profile: `BOUNDARY_COMPACT`

## Belongs

- Schema-valid pipeline declarations for this domain.
- Declarative stage boundaries, inputs, outputs, resource envelopes, and required gates.
- References to admitted source descriptors and governed implementation, contract, schema, fixture, test, workflow, and release families.
- Explicit inactive, denial, rollback, correction, and supersession metadata.

## Prohibited

- Executable acquisition, transformation, geocoding, routing, or scheduling code.
- Credentials, source payloads, cached responses, generated products, or lifecycle instances.
- Exact living-person addresses, private household facts, protected-facility details, critical-infrastructure vulnerabilities, or access-control data.
- Claims that infrastructure status, occupancy, access, capacity, service availability, jurisdiction, or safety is current.
- Promotion or publication based on declaration presence, valid syntax, workflow success, or source recency alone.

## Inputs and outputs

| Direction | Governed posture |
|---|---|
| Inputs | References to admitted source descriptors, contracts, schemas, fixtures, implementations, and evidence; no embedded payloads |
| Candidate outputs | Lifecycle-state names and artifact-family references only |
| Writes | `false` for every current declaration |
| Runtime effects | None; all declarations are `PROPOSED_INACTIVE` and `DISABLED` |

Any later activation requires source admission, privacy and sensitivity review, schema and policy conformance, fixture-backed tests, evidence review, an activation record, and release authority.

## Exposure, mutation, and retention

- Exposure: internal repository declarations; downstream public use requires a separately approved, minimized release.
- Sensitivity: exact household and protected-infrastructure detail defaults to restricted or abstained treatment until reviewed.
- Mutation: pull-request review with stable IDs and deterministic hashes. Do not mutate an accepted identity in place.
- Retention: preserve proposal and supersession history needed for audit and rollback; payload retention belongs to governed data lanes.

## Current direct-child map

Verified 2026-08-30. Direct children only:

```text
settlements-infrastructure/
├── README.md      # this local boundary contract
├── catalog.yaml   # inactive CATALOG stage boundary
├── ingest.yaml    # inactive INGEST stage boundary
├── normalize.yaml # inactive NORMALIZE stage boundary
├── publish.yaml   # inactive PUBLISH stage boundary
└── validate.yaml  # inactive VALIDATE stage boundary
```

## Declaration inventory

| Declaration class | Files | Count | Status |
|---|---|---:|---|
| Stage boundaries | `ingest.yaml`, `normalize.yaml`, `validate.yaml`, `catalog.yaml`, `publish.yaml` | 5 | `PROPOSED_INACTIVE`; `NOT_IMPLEMENTED`; `DISABLED` |
| Pipeline candidates | None | 0 | No candidate-specific declarations are present |
| Total YAML declarations | All rows above | 5 | No source, network, write, promotion, release, or publication authority |

The stage boundaries are inventory and interface candidates; they do not prove source admission, implementation, scheduling, consumer binding, or safe exposure.

## Validation

- Validate every YAML file against the [common declaration schema](../../schemas/contracts/v1/pipeline_spec_declaration.schema.json).
- Run [`tools/validators/validate_pipeline_spec_declarations.py`](../../tools/validators/validate_pipeline_spec_declarations.py) and its fixture-backed tests.
- Verify declared paths, references, stable IDs, deterministic hashes, inactive status, denial invariants, and unique identity.
- Run repository YAML, documentation meta-block/link, topology, secret, privacy, and policy checks.
- Treat missing references, schema drift, source-role collapse, network permission, lifecycle writes, sensitive-detail exposure, or publication authority as failure.

## Related governed families

- Common contract: [`contracts/pipeline_spec_declaration.md`](../../contracts/pipeline_spec_declaration.md)
- Common schema: [`schemas/contracts/v1/pipeline_spec_declaration.schema.json`](../../schemas/contracts/v1/pipeline_spec_declaration.schema.json)
- Domain contract family: [`contracts/domains/settlements-infrastructure/`](../../contracts/domains/settlements-infrastructure/README.md)
- Domain schema family: [`schemas/contracts/v1/domains/settlements-infrastructure/`](../../schemas/contracts/v1/domains/settlements-infrastructure/README.md)
- Domain policy family: [`policy/domains/settlements-infrastructure/`](../../policy/domains/settlements-infrastructure/README.md)
- Common declaration fixtures: [`fixtures/contracts/v1/pipeline_spec_declaration/`](../../fixtures/contracts/v1/pipeline_spec_declaration/)
- Domain fixtures: [`fixtures/domains/settlements-infrastructure/`](../../fixtures/domains/settlements-infrastructure/README.md)
- Common declaration tests: [`tests/validators/test_validate_pipeline_spec_declarations.py`](../../tests/validators/test_validate_pipeline_spec_declarations.py)
- Domain tests: [`tests/domains/settlements-infrastructure/`](../../tests/domains/settlements-infrastructure/README.md)
- Release family: [`release/candidates/settlements-infrastructure/`](../../release/candidates/settlements-infrastructure/README.md)
- Domain guidance: [`docs/domains/settlements-infrastructure/`](../../docs/domains/settlements-infrastructure/README.md)
- Accepted governance: [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) and [Directory Rules v2](../../docs/doctrine/directory-rules.md)

## Status and open verification

Status: five machine-readable stage-boundary declarations, all `PROPOSED_INACTIVE`; no active source, schedule, network path, writer, publisher, or release is established.

Open verification items:

- Name owners and reviewers.
- Admit and bind sources only through the source-governance process.
- Verify executable consumers and fixture-first conformance before any activation proposal.
- Inventory users of the singular compatibility path and define its exit criteria.
- Establish privacy, sensitivity, correction, withdrawal, and public-generalization controls.

## Review triggers and rollback

Re-review when a declaration, source, consumer, owner, schema, policy, lifecycle target, privacy rule, exposure, sensitivity, compatibility consumer, workflow, or release family changes; when an ADR changes; or when drift, correction, withdrawal, or rollback occurs.

Rollback declaration changes by reverting the owning commit and re-running the validator. A rollback does not reactivate an older source or release and must not restore `pipeline_specs/settlement/` as a writable authority.
