<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-people-dna-land-readme
title: pipeline_specs/people-dna-land/ — Pipeline Specification Boundary
type: readme
version: v1.0
status: proposed-inactive; repository-grounded
owners: OWNER_TBD — pipeline-spec steward; domain steward; validation reviewer
created: 2026-06-13
updated: 2026-08-30
policy_label: public-metadata; restricted-domain; declarative-only; fail-closed; no-live-activation
owning_root: pipeline_specs/
responsibility: govern inactive declarative pipeline intent for the people-dna-land scope
truth_posture: CONFIRMED inventory and fail-closed posture / PROPOSED declarations / NEEDS VERIFICATION activation prerequisites
readme_profile: BOUNDARY_COMPACT
current_path: pipeline_specs/people-dna-land/README.md
inherited_parent: pipeline_specs/README.md
scope_id: people-dna-land
related:
  - pipeline_specs/README.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - contracts/pipeline_spec_declaration.md
  - schemas/contracts/v1/pipeline_spec_declaration.schema.json
notes: ["Metadata is flat by contract; validation does not activate a source, pipeline, lifecycle write, release, or publication."]
[/KFM_META_BLOCK_V2] -->

# People, DNA, and Land pipeline declarations

`pipeline_specs/people-dna-land/` is the canonical declarative run-intent lane
for People, Genealogy, DNA/Genomic, Consent, Revocation, and Land concerns. It
inherits the authority limits of the [pipeline specification root](../README.md)
and the accepted
[Directory Rules v2 decision](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md).

The local owner and CODEOWNERS review route is `@bartytime4life`. The scope ID
is `people-dna-land`. Privacy, consent, rights, community, domain, security, and
release reviewers must be identified before any activation proposal.

## Boundary contract

Belongs here:

- closed `KfmPipelineSpecDeclaration` documents for domain run intent;
- stage boundaries for ingest, normalize, validate, catalog, and publish;
- references to separately governed source descriptors, contracts, schemas,
  policies, implementations, fixtures, tests, and workflows;
- a child README where the land-ownership sensitivity boundary narrows this
  parent contract.

Prohibited here:

- executable code, connector behavior, credentials, schedules, or runtime state;
- source payloads, personal records, DNA/genomic material, evidence instances,
  receipts, proofs, title conclusions, or release decisions;
- a writable declaration under the `people/` compatibility lane;
- any assertion that identity, relationship, kinship, residence, ownership, or
  community membership is established merely because a pipeline ran;
- parallel contract, schema, policy, consent, promotion, or publication authority.

Individual-level DNA, identity, exact parcel or residence data, private
person-to-parcel joins, and vulnerable-community data fail closed. A public
record, consent reference, aggregation label, or path name is not sufficient
clearance for disclosure.

## Inputs and outputs

Permitted inputs are stable identifiers for reviewed source descriptors and
references to governed contract, schema, policy, implementation, fixture, test,
and workflow families. A declaration may name candidate lifecycle states; it
cannot admit a source, resolve an identity, grant consent, or approve a join.

The only outputs owned here are reviewed declaration documents. Candidate data
outputs are non-materialized intent until separately implemented and governed.
Executable transformations belong under `pipelines/`; data and evidence
instances belong under `data/`; release decisions remain outside this lane.

## Exposure, mutation, and retention

- Exposure: repository-visible metadata only. No direct or linkable sensitive
  data may enter declarations, examples, logs, issues, or review text.
- Mutation: human-reviewed Git changes only; no runtime writer is permitted.
- Retention: durable configuration history. Deletion, rename, split, or alias
  retirement requires a migration and consumer review.
- Capability posture: network access, source activation, lifecycle writes,
  promotion, release, and publication are `DENIED`.

Path presence never activates execution. Valid YAML, merge, scheduling syntax,
or a passing workflow cannot override those denials.

## Current direct children

Verified for this change; only direct children are shown.

```text
pipeline_specs/people-dna-land/
├── README.md          # this local boundary contract
├── catalog.yaml       # inactive CATALOG stage boundary
├── ingest.yaml        # inactive INGEST stage boundary
├── land-ownership/    # narrower sensitive sub-boundary
├── normalize.yaml     # inactive NORMALIZE stage boundary
├── publish.yaml       # inactive PUBLISH stage boundary
└── validate.yaml      # inactive VALIDATE stage boundary
```

## Declaration inventory

| Direct declarations | Object type | Profile kind | Status |
|---|---|---|---|
| `ingest.yaml`, `normalize.yaml`, `validate.yaml`, `catalog.yaml`, `publish.yaml` | `KfmPipelineSpecDeclaration` | `STAGE_BOUNDARY` | `PROPOSED_INACTIVE` |
| `land-ownership/` | no declaration; README boundary only | not applicable | not active |

All five stage declarations are `NOT_IMPLEMENTED`. The absence of an active
binding is deliberate and must not be inferred away.

## Validation

From the repository root, run:

```bash
python tools/validators/validate_pipeline_spec_declarations.py
python tools/validators/directory_governance/validate_repository_topology.py --repo-root . --format text
```

Validation must reject unknown fields, bad paths, hash drift, non-inactive
status, enabled network or writes, and any promotion, release, or publication
capability. Passing validation proves only declaration and placement conformance.

## Related authority families

- Common contract: [pipeline declaration semantics](../../contracts/pipeline_spec_declaration.md)
- Common schema: [pipeline declaration shape](../../schemas/contracts/v1/pipeline_spec_declaration.schema.json)
- Domain contracts: [People/DNA/Land contracts](../../contracts/domains/people-dna-land/README.md)
- Domain schemas: [People/DNA/Land schemas](../../schemas/contracts/v1/domains/people-dna-land/README.md)
- Policy: [domain policy](../../policy/domains/people-dna-land/README.md),
  [consent policy](../../policy/consent/people-dna-land/README.md), and
  [sensitivity policy](../../policy/sensitivity/people-dna-land/person_parcel_join.deny.rego)
- Fixtures: [synthetic People/DNA/Land fixtures](../../fixtures/domains/people-dna-land/README.md)
- Tests: [People/DNA/Land boundary tests](../../tests/domains/people-dna-land/README.md)
- Release families: [release contracts](../../contracts/release/README.md) and
  [release schemas](../../schemas/contracts/v1/release/README.md)

These families retain their own authority; this directory only references them.

## Status and open verification

The five declarations are structurally governed but remain
`PROPOSED_INACTIVE` and `NOT_IMPLEMENTED`. No admitted source, executable
consumer, production schedule, consent closure, lifecycle write, release
decision, or publication approval is claimed.

Before any activation proposal, verify named specialist reviewers, source rights,
living-person classification, consent and revocation propagation, genomic
minimization and retention, identity and temporal semantics, vulnerable-community
consultation, exact parcel/residence denial, public-safe transforms, negative
tests, receipts, correction, rollback, and independent release review.

## Review triggers and rollback

Re-review when ownership, schema, consumer, source role, consent model,
sensitivity, retention, exposure, child boundary, compatibility mapping,
workflow, or governing ADR changes; also review any request to change inactive
status or a denied capability.

Rollback is `REVERT_DECLARATION_CHANGE`: revert the declaration or README change,
preserve every execution and write/release denial, invalidate dependent candidate
evidence, and re-run declaration plus topology validation. Rollback never
reactivates a prior source, consent state, join, or published artifact.
