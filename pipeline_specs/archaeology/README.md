<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-archaeology-readme
title: pipeline_specs/archaeology/ — Pipeline Specification Boundary
type: readme
version: v1.0
status: proposed-inactive; repository-grounded
owners: OWNER_TBD — pipeline-spec steward; domain steward; validation reviewer
created: 2026-06-13
updated: 2026-08-30
policy_label: public-metadata; restricted-domain; declarative-only; fail-closed; no-live-activation
owning_root: pipeline_specs/
responsibility: govern inactive declarative pipeline intent for the archaeology scope
truth_posture: CONFIRMED inventory and fail-closed posture / PROPOSED declarations / NEEDS VERIFICATION activation prerequisites
readme_profile: BOUNDARY_COMPACT
current_path: pipeline_specs/archaeology/README.md
inherited_parent: pipeline_specs/README.md
scope_id: archaeology
related:
  - pipeline_specs/README.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - contracts/pipeline_spec_declaration.md
  - schemas/contracts/v1/pipeline_spec_declaration.schema.json
notes: ["Metadata is flat by contract; validation does not activate a source, pipeline, lifecycle write, release, or publication."]
[/KFM_META_BLOCK_V2] -->

# Archaeology pipeline declarations

`pipeline_specs/archaeology/` is the declarative run-intent boundary for the
Archaeology domain. It inherits the authority limits of the
[pipeline specification root](../README.md) and the accepted
[Directory Rules v2 decision](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md).

The verified CODEOWNERS review route is `@bartytime4life`; local stewardship
remains `OWNER_TBD`. The scope ID is `archaeology`; cultural, rights-holder,
sensitivity, and release reviewers must be identified when a proposed
declaration seeks activation.

## Boundary contract

Belongs here:

- closed `KfmPipelineSpecDeclaration` documents for archaeology run intent;
- stage boundaries for ingest, normalize, validate, catalog, and publish;
- explicit compatibility aliases that point one way to a canonical declaration;
- references to separately governed contracts, schemas, policies, fixtures,
  tests, workflows, and source descriptors.

Prohibited here:

- executable pipeline or connector code, credentials, schedules, or runtime state;
- source payloads, evidence instances, receipts, proofs, or release decisions;
- exact site or heritage locations, reverse-engineerable geometry, collection
  security details, burial or human-remains locations, sacred knowledge, or
  culturally controlled content;
- any assertion that a candidate feature is a confirmed archaeological site;
- a second writable authority for contracts, schemas, policy, or publication.

Exact site and heritage locations are highly sensitive and fail closed. Path
placement, redaction text, or a passing validation check does not make them
public-safe or culturally authorized.

## Inputs and outputs

Permitted inputs are identifiers for reviewed source descriptors and references
to governed contract, schema, policy, implementation, fixture, test, and
workflow families. References describe prerequisites; they do not admit a
source or prove that the referenced control passed.

The only outputs owned here are reviewed declaration documents. Candidate
lifecycle outputs named by a declaration remain non-materialized intent.
Executable code belongs under `pipelines/`; lifecycle instances belong under
`data/`; release decisions belong to the release contract and decision
families.

## Exposure, mutation, and retention

- Exposure: repository-visible metadata only; no sensitive payload or precise
  location may enter a declaration, fixture example, log, or review body.
- Mutation: human-reviewed Git changes only. No runtime process may rewrite this
  lane.
- Retention: tracked as durable configuration history. Rename, alias retirement,
  or deletion requires a migration record and consumer review.
- Capability posture: network access, source activation, lifecycle writes,
  promotion, release, and publication are `DENIED`.

Path presence never activates execution. A valid file, merged change, schedule,
or workflow result cannot override these denials.

## Current direct children

Verified for this change; only direct children are shown.

```text
pipeline_specs/archaeology/
├── README.md              # this local boundary contract
├── catalog.spec.yaml      # compatibility alias -> catalog.yaml
├── catalog.yaml           # canonical CATALOG stage boundary
├── ingest.spec.yaml       # compatibility alias -> ingest.yaml
├── ingest.yaml            # canonical INGEST stage boundary
├── normalize.spec.yaml    # compatibility alias -> normalize.yaml
├── normalize.yaml         # canonical NORMALIZE stage boundary
├── publish.spec.yaml      # compatibility alias -> publish.yaml
├── publish.yaml           # canonical PUBLISH stage boundary
├── validate.spec.yaml     # compatibility alias -> validate.yaml
└── validate.yaml          # canonical VALIDATE stage boundary
```

## Declaration inventory

All ten YAML files use `object_type: KfmPipelineSpecDeclaration` and
`status: PROPOSED_INACTIVE`.

| Declaration set | Count | Profile kind | Canonical target |
|---|---:|---|---|
| `ingest.yaml`, `normalize.yaml`, `validate.yaml`, `catalog.yaml`, `publish.yaml` | 5 | `STAGE_BOUNDARY` | self |
| matching `*.spec.yaml` files | 5 | `COMPATIBILITY_ALIAS` | same-name `.yaml` |

The aliases are read-only routing declarations. They cannot diverge from or
replace their canonical targets, and neither set is implemented or active.

## Validation

From the repository root, run:

```bash
python tools/validators/validate_pipeline_spec_declarations.py
python tools/validators/directory_governance/validate_repository_topology.py --repo-root . --format text
```

Validation must reject unknown fields, bad relative paths, hash drift,
non-inactive status, an alias without an exact canonical target, enabled
network or writes, or any promotion, release, or publication capability.
Passing validation proves declaration conformance only.

## Related authority families

- Common contract: [pipeline declaration semantics](../../contracts/pipeline_spec_declaration.md)
- Common schema: [pipeline declaration shape](../../schemas/contracts/v1/pipeline_spec_declaration.schema.json)
- Domain contracts: [Archaeology contracts](../../contracts/domains/archaeology/README.md)
- Domain schemas: [Archaeology schemas](../../schemas/contracts/v1/domains/archaeology/README.md)
- Policy: [Archaeology policy](../../policy/domains/archaeology/README.md)
- Fixtures: [synthetic Archaeology fixtures](../../fixtures/domains/archaeology/README.md)
- Tests: [Archaeology boundary tests](../../tests/domains/archaeology/README.md)
- Release families: [release contracts](../../contracts/release/README.md) and
  [release schemas](../../schemas/contracts/v1/release/README.md)

These links do not transfer authority into `pipeline_specs/`.

## Status and open verification

The declarations are structurally governed but remain `PROPOSED_INACTIVE` and
`NOT_IMPLEMENTED`. No admitted source, active runtime binding, production
schedule, lifecycle write, release closure, or publication approval is claimed.

Before any activation proposal, verify named cultural and rights-holder review
authority, source rights and sovereignty, public-safe transforms, exact-location
denial across every output surface, executable consumer identity, fixtures,
negative tests, receipts, rollback, and independent release review.

## Review triggers and rollback

Re-review this boundary when ownership, schema, consumer, source role,
sensitivity, exposure, alias target, writer, workflow, or governing ADR changes;
also review any request to move a declaration out of `PROPOSED_INACTIVE`.

Rollback is `REVERT_DECLARATION_CHANGE`: revert the declaration or README change,
keep execution and all write/release capabilities denied, invalidate dependent
candidate evidence, and re-run declaration plus topology validation. Rollback
does not restore or authorize an earlier runtime state.
