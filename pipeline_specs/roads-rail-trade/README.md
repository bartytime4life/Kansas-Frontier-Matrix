<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-roads-rail-trade-readme
title: pipeline_specs/roads-rail-trade/ — Pipeline Specification Boundary
type: readme
version: v1.0
status: proposed-inactive; repository-grounded
owners: OWNER_TBD — pipeline-spec steward; domain steward; validation reviewer
created: 2026-06-13
updated: 2026-08-30
policy_label: public-metadata; declarative-only; fail-closed; no-live-activation
owning_root: pipeline_specs/
responsibility: govern inactive declarative pipeline intent for the roads-rail-trade scope
truth_posture: CONFIRMED inventory and fail-closed posture / PROPOSED declarations / NEEDS VERIFICATION activation prerequisites
readme_profile: BOUNDARY_COMPACT
current_path: pipeline_specs/roads-rail-trade/README.md
inherited_parent: pipeline_specs/README.md
scope_id: roads-rail-trade
related:
  - pipeline_specs/README.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - contracts/pipeline_spec_declaration.md
  - schemas/contracts/v1/pipeline_spec_declaration.schema.json
notes: ["Metadata is flat by contract; validation does not activate a source, pipeline, lifecycle write, release, or publication."]
[/KFM_META_BLOCK_V2] -->

# `pipeline_specs/roads-rail-trade/` boundary

## Purpose and inherited parent

This lane inherits [`pipeline_specs/`](../README.md) and owns declarative run intent for roads, rail, historic routes, transportation feeds, and trade-route candidates. It may describe what a pipeline could consume or produce under named gates. Executable behavior belongs in [`pipelines/domains/roads-rail-trade/`](../../pipelines/domains/roads-rail-trade/README.md).

Declaration presence never activates execution. Network access, lifecycle writes, source activation, promotion, release, and publication are `DENIED` for every current declaration.

## Local owner and scope

- Scope ID: `roads-rail-trade`
- Local owner: `OWNER_TBD — Roads/Rail/Trade pipeline-spec steward`
- Required reviewers: source/rights, temporal, sensitivity, evidence, policy, validation, and release stewards
- Boundary profile: `BOUNDARY_COMPACT`

## Belongs

- Schema-valid pipeline declarations for this domain.
- Declarative stage boundaries, inputs, outputs, resource envelopes, and required gates.
- References to admitted source descriptors and governed implementation, contract, schema, fixture, test, workflow, and release families.
- Explicit inactive, hold, denial, rollback, correction, and supersession metadata.

## Prohibited

- Executable transformation, acquisition, routing, or scheduling code.
- Credentials, tokens, source payloads, cached responses, or generated products.
- Claims that a road, rail line, closure, restriction, crossing, historic route, or access right is current or operational.
- Navigation, dispatch, emergency-routing, railroad-operating, legal-access, or public-release authority.
- Promotion or publication based on declaration presence, valid syntax, workflow success, or source recency alone.

## Inputs and outputs

| Direction | Governed posture |
|---|---|
| Inputs | References to admitted source descriptors, contracts, schemas, fixtures, implementations, and evidence; no embedded payloads |
| Candidate outputs | Lifecycle-state names and artifact-family references only |
| Writes | `false` for every current declaration |
| Runtime effects | None; all declarations are `PROPOSED_INACTIVE` and `DISABLED` |

Any later activation requires separate source admission, schema and policy conformance, fixture-backed tests, evidence review, an activation record, and release authority.

## Exposure, mutation, and retention

- Exposure: internal repository declarations; downstream public use requires a separately approved release.
- Sensitivity: protect infrastructure, cultural-route, property-access, and security-relevant details; generalize or abstain where required.
- Mutation: pull-request review with stable IDs and deterministic hashes. Do not mutate an accepted identity in place.
- Retention: preserve proposal and supersession history needed for audit and rollback.

## Current direct-child map

Verified 2026-08-30. Direct children only:

```text
roads-rail-trade/
├── README.md             # this local boundary contract
├── catalog.yaml          # inactive CATALOG stage boundary
├── fra_gcis.yaml         # inactive FRA/GCIS pipeline candidate
├── historic_routes.yaml  # inactive historic-routes pipeline candidate
├── ingest.yaml           # inactive INGEST stage boundary
├── normalize.yaml        # inactive NORMALIZE stage boundary
├── publish.yaml          # inactive PUBLISH stage boundary
├── tiger_roads.yaml      # inactive TIGER roads pipeline candidate
├── validate.yaml         # inactive VALIDATE stage boundary
└── wzdx_v4.yaml          # inactive WZDx v4 pipeline candidate
```

## Declaration inventory

| Declaration class | Files | Count | Status |
|---|---|---:|---|
| Stage boundaries | `ingest.yaml`, `normalize.yaml`, `validate.yaml`, `catalog.yaml`, `publish.yaml` | 5 | `PROPOSED_INACTIVE`; `NOT_IMPLEMENTED`; `DISABLED` |
| Pipeline candidates | `fra_gcis.yaml`, `historic_routes.yaml`, `tiger_roads.yaml`, `wzdx_v4.yaml` | 4 | `PROPOSED_INACTIVE`; `NOT_IMPLEMENTED`; `DISABLED` |
| Total YAML declarations | All rows above | 9 | No source, network, write, promotion, release, or publication authority |

The four candidate names are inventory, not proof of source admission, supported format, operational currency, or consumer binding.

## Validation

- Validate every YAML file against the [common declaration schema](../../schemas/contracts/v1/pipeline_spec_declaration.schema.json).
- Run [`tools/validators/validate_pipeline_spec_declarations.py`](../../tools/validators/validate_pipeline_spec_declarations.py) and its fixture-backed tests.
- Verify declared paths, references, stable IDs, deterministic hashes, inactive status, denial invariants, and unique identity.
- Run repository YAML, documentation meta-block/link, topology, secret, and policy checks.
- Treat missing references, schema drift, source-role collapse, network permission, lifecycle writes, or publication authority as failure.

## Related governed families

- Common contract: [`contracts/pipeline_spec_declaration.md`](../../contracts/pipeline_spec_declaration.md)
- Common schema: [`schemas/contracts/v1/pipeline_spec_declaration.schema.json`](../../schemas/contracts/v1/pipeline_spec_declaration.schema.json)
- Domain contract family: [`contracts/domains/roads-rail-trade/`](../../contracts/domains/roads-rail-trade/README.md)
- Domain schema family: [`schemas/contracts/v1/domains/roads-rail-trade/`](../../schemas/contracts/v1/domains/roads-rail-trade/README.md)
- Domain policy family: [`policy/domains/roads-rail-trade/`](../../policy/domains/roads-rail-trade/README.md)
- Common declaration fixtures: [`fixtures/contracts/v1/pipeline_spec_declaration/`](../../fixtures/contracts/v1/pipeline_spec_declaration/)
- Domain fixtures: [`fixtures/domains/roads-rail-trade/`](../../fixtures/domains/roads-rail-trade/README.md)
- Common declaration tests: [`tests/validators/test_validate_pipeline_spec_declarations.py`](../../tests/validators/test_validate_pipeline_spec_declarations.py)
- Domain tests: [`tests/domains/roads-rail-trade/`](../../tests/domains/roads-rail-trade/README.md)
- Release family: [`release/candidates/roads-rail-trade/`](../../release/candidates/roads-rail-trade/README.md)
- Domain guidance: [`docs/domains/roads-rail-trade/`](../../docs/domains/roads-rail-trade/README.md)
- Accepted governance: [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) and [Directory Rules v2](../../docs/doctrine/directory-rules.md)

## Status and open verification

Status: nine machine-readable declarations, all `PROPOSED_INACTIVE`; no active source, schedule, network path, writer, publisher, or release is established.

Open verification items:

- Name owners and reviewers.
- Admit and bind sources only through the source-governance process.
- Verify executable consumers and fixture-first conformance before any activation proposal.
- Resolve transport contract/schema compatibility placement without creating parallel authority.
- Establish temporal validity, rights, sensitivity, correction, and withdrawal controls for each candidate.

## Review triggers and rollback

Re-review when a declaration, source, consumer, owner, schema, policy, lifecycle target, exposure, sensitivity, workflow, or release family changes; when an ADR changes; or when drift, correction, withdrawal, or rollback occurs.

Rollback declaration changes by reverting the owning commit and re-running the validator. A rollback does not reactivate an older source or release. Consequential operational answers must defer to the appropriate current official authority.
