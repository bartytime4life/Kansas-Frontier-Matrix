<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-people-readme
title: pipeline_specs/people/ — Pipeline Specification Boundary
type: readme
version: v1.0
status: documentation-only; proposed-compatibility; read-only
owners: OWNER_TBD — pipeline-spec steward; domain steward; validation reviewer
created: 2026-06-13
updated: 2026-08-30
policy_label: public-metadata; compatibility-proposal; declarative-only; fail-closed
owning_root: pipeline_specs/
responsibility: document a proposed read-only mapping to pipeline_specs/people-dna-land/ without creating parallel authority
truth_posture: CONFIRMED README-only boundary / PROPOSED target mapping / NEEDS VERIFICATION accepted registration and consumers
readme_profile: BOUNDARY_COMPACT
current_path: pipeline_specs/people/README.md
inherited_parent: pipeline_specs/README.md
scope_id: people
proposed_target: pipeline_specs/people-dna-land/
target_status: PROPOSED_PENDING_REGISTRATION
related:
  - pipeline_specs/README.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - contracts/pipeline_spec_declaration.md
  - schemas/contracts/v1/pipeline_spec_declaration.schema.json
notes: ["Metadata is flat by contract; validation does not activate a source, pipeline, lifecycle write, release, or publication."]
[/KFM_META_BLOCK_V2] -->

# People compatibility boundary

`pipeline_specs/people/` is maintained as a documentation-only compatibility
boundary directed to [People, DNA, and Land](../people-dna-land/README.md). The
mapping is a fail-closed working posture pending accepted register evidence; it
does not itself settle canonical identity. This lane inherits the authority
limits of the [pipeline specification root](../README.md) and the accepted
[Directory Rules v2 decision](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md).

The verified CODEOWNERS review route is `@bartytime4life`; local stewardship
remains `OWNER_TBD`. The local scope ID is `people`; the proposed compatibility
target scope is `people-dna-land`, subject to accepted alias registration.

## Boundary contract

Belongs here:

- this README and temporary human-readable migration guidance;
- explicit references that direct consumers to `pipeline_specs/people-dna-land/`;
- verified consumer and retirement evidence when compatibility work is reviewed.

Prohibited here:

- YAML, JSON, schedules, run graphs, or any other machine declaration;
- executable code, connectors, credentials, source payloads, runtime state,
  evidence instances, receipts, proofs, or release decisions;
- direct edits that duplicate, override, or diverge from the canonical lane;
- a fallback write path when the canonical lane rejects a change;
- sensitive People, DNA, identity, residence, parcel, or community data.

This path must not become a second writable authority. Under the proposed
mapping, consumers needing run intent resolve to the `people-dna-land`
declaration set.
Individual-level DNA, identity, exact parcel/residence, and vulnerable-community
data fail closed across both paths.

## Inputs and outputs

Permitted inputs are the proposed target lane identity, verified legacy-consumer
references, and migration evidence. The only output is documentation that maps
the compatibility name to its proposed target.

This lane emits no declaration, run, lifecycle object, receipt, proof, release
candidate, or published artifact. It cannot admit a source, schedule execution,
resolve identity, grant consent, approve a join, or authorize disclosure.

## Exposure, mutation, and retention

- Exposure: repository-visible compatibility documentation only; no sensitive
  payload or identifying example belongs here.
- Mutation: human-reviewed documentation changes only. Machine writers and
  declaration edits are prohibited.
- Retention: keep only while verified consumers require the alias; retirement
  requires consumer closure and migration evidence.
- Capability posture: network access, source activation, lifecycle writes,
  promotion, release, and publication are `DENIED`.

Path presence never activates execution. A consumer reference, link, merge,
valid target declaration, or passing workflow cannot override these denials.

## Current direct children

Verified for this change; only direct children are shown.

```text
pipeline_specs/people/
├── .gitkeep     # retained zero-byte topology marker; no authority
└── README.md    # documentation-only compatibility mapping
```

The retained `.gitkeep` is a compatibility marker only. It does not register or
accept the proposed mapping and grants no declaration or execution authority.

## Declaration inventory

| Direct declarations | Object type | Proposed compatibility target | Status |
|---:|---|---|---|
| 0 | none permitted | `pipeline_specs/people-dna-land/` | documentation-only |

The proposed target contains five `KfmPipelineSpecDeclaration` stage
boundaries, each with `status: PROPOSED_INACTIVE`. This README does not proxy or
activate them and is not itself a `COMPATIBILITY_ALIAS` machine declaration.

## Validation

From the repository root, run:

```bash
python tools/validators/validate_pipeline_spec_declarations.py
python tools/validators/directory_governance/validate_repository_topology.py --repo-root . --format text
```

Review must also confirm that this directory remains README-only. Validation
must fail if a machine declaration appears here or if a consumer treats the path
as writable authority. Passing checks proves compatibility placement only.

## Related authority families

- Canonical lane: [People/DNA/Land declarations](../people-dna-land/README.md)
- Common contract: [pipeline declaration semantics](../../contracts/pipeline_spec_declaration.md)
- Common schema: [pipeline declaration shape](../../schemas/contracts/v1/pipeline_spec_declaration.schema.json)
- Domain contracts: [People/DNA/Land contracts](../../contracts/domains/people-dna-land/README.md)
- Domain schemas: [People/DNA/Land schemas](../../schemas/contracts/v1/domains/people-dna-land/README.md)
- Policy: [domain policy](../../policy/domains/people-dna-land/README.md),
  [consent policy](../../policy/consent/people-dna-land/README.md), and
  [sensitivity policy](../../policy/sensitivity/people-dna-land/person_parcel_join.deny.rego)
- Fixtures: [synthetic domain fixtures](../../fixtures/domains/people-dna-land/README.md)
- Tests: [domain boundary tests](../../tests/domains/people-dna-land/README.md)
- Release families: [release contracts](../../contracts/release/README.md) and
  [release schemas](../../schemas/contracts/v1/release/README.md)

These families belong to the canonical domain and retain their own authority.

## Status and open verification

This lane is README-only and has zero declarations. No active source, runtime
binding, schedule, lifecycle write, consent decision, release, or publication is
claimed here or by reference.

Verify the complete set of legacy consumers, their one-way resolution behavior,
whether an accepted alias register entry exists or must be created, absence of
writes and generated mirrors, owner-approved retirement criteria, and tests
that prevent parallel authority.
Until that evidence closes, retain this narrow documentation boundary.

## Review triggers and rollback

Re-review when a consumer is added or removed; when canonical naming, alias
registration, ownership, sensitivity, exposure, or the governing ADR changes;
or when any file other than this README is proposed here.

Rollback is to revert the documentation or migration change, preserve this lane
as read-only, keep all execution and write/release capabilities denied, and
re-run declaration plus topology validation. Never roll back by copying canonical
declarations into this path.
