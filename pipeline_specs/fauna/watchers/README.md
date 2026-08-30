<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-fauna-watchers-readme
title: pipeline_specs/fauna/watchers/ — Pipeline Specification Boundary
type: readme
version: v1.0
status: proposed-inactive; placement-hold; repository-grounded
owners: OWNER_TBD — pipeline-spec steward; domain steward; validation reviewer
created: 2026-06-13
updated: 2026-08-30
policy_label: public-metadata; declarative-only; placement-review-required; fail-closed
owning_root: pipeline_specs/
responsibility: document the inactive fauna/watchers boundary while canonical placement remains on HOLD
truth_posture: CONFIRMED inventory and denial posture / PROPOSED boundary / NEEDS VERIFICATION canonical placement
readme_profile: BOUNDARY_COMPACT
current_path: pipeline_specs/fauna/watchers/README.md
inherited_parent: pipeline_specs/README.md
scope_id: fauna/watchers
related:
  - pipeline_specs/README.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - contracts/pipeline_spec_declaration.md
  - schemas/contracts/v1/pipeline_spec_declaration.schema.json
notes: ["Metadata is flat by contract; validation does not activate a source, pipeline, lifecycle write, release, or publication."]
[/KFM_META_BLOCK_V2] -->

# Fauna watcher declarations

`pipeline_specs/fauna/watchers/` is a reserved declarative boundary for possible Fauna
source-change watcher intent. Its placement is unresolved. It does not establish a
watcher profile, canonical target, schedule, source access, or execution path.

This is a Directory Rules v2 `BOUNDARY_COMPACT` contract adopted through
[`ADR-0029`](../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md).
It inherits [`pipeline_specs/fauna/README.md`](../README.md) and the
[`pipeline_specs/` root contract](../../README.md).

## Boundary posture

| Control | Required posture |
|---|---|
| Placement | `HOLD / PLACEMENT_REVIEW_REQUIRED` |
| Declaration inventory | none |
| Activation | `DENIED` |
| Network access | `DENIED` |
| Lifecycle writes | `DENIED` |
| Promotion | `DENIED` |
| Release | `DENIED` |
| Publication | `DENIED` |
| Sensitive detail | deny by default |

The directory name is not evidence of a selected topology. No shared or domain-local
watcher location is canonical until an explicit placement decision is accepted.
File presence does not activate execution or grant watcher authority.

## Purpose and ownership

If placement is accepted, this lane may hold closed `KfmPipelineSpecDeclaration`
documents that describe metadata-first checks and bounded review handoffs for admitted
Fauna sources. It may never hold executable watcher logic or source payloads.

The pipeline-spec steward owns declaration shape and placement. The watcher steward owns
comparison intent. The Fauna, source, rights, sensitivity, validation, evidence, policy,
and release stewards retain their separate authorities. Missing ownership fails closed.

## Belongs here only after placement approval

- inactive watcher declarations with `stage: WATCH`;
- admitted `SourceDescriptor` references, never embedded source records;
- metadata-only comparison signals and deterministic baseline references;
- bounded candidate outcomes such as `NO_ACTION`, `QUARANTINE`, or `WORK`;
- required gates, reason codes, non-effects, and rollback posture;
- links to accepted contracts, schemas, fixtures, tests, and workflows.

## Prohibited here

- unreviewed watcher declarations while placement remains on hold;
- HTTP clients, scraping code, connectors, schedulers, credentials, or private endpoints;
- fetched source data, cache state, comparison payloads, or lifecycle records;
- exact or reconstructable wildlife occurrences, sites, identifiers, or telemetry;
- source admission, taxonomy, rights, sensitivity, policy, evidence, or release decisions;
- catalog mutation, alerts represented as official truth, or public publication;
- duplicate writable profiles split between this lane and `pipeline_specs/watchers/`.

## Direct-child map

Only direct children are shown.

```text
pipeline_specs/fauna/watchers/
└── README.md
```

The removed `.gitkeep` was redundant because this README keeps the directory tracked.

## Declaration inventory

| File | `spec_id` | Stage | Status / implementation |
|---|---|---|---|
| None | None | None | `HOLD / PLACEMENT_REVIEW_REQUIRED` |

There are no `KfmPipelineSpecDeclaration` files in this directory. Therefore there is
no `PROPOSED_INACTIVE` watcher here, no implementation binding, and no canonical target
to infer. A future declaration requires a separate reviewed placement decision.

## Candidate inputs and outputs

If this boundary is activated by a later governance decision, a watcher declaration may
describe candidate `SOURCE_SNAPSHOT` input and candidate `NO_ACTION`, `QUARANTINE`, or
`WORK` output. Those values are planning edges only:

- `lifecycle.writes_targets` must remain `false` until separately authorized;
- a metadata difference is not a source, content, or materiality decision;
- a candidate output is not RAW admission, evidence, catalog closure, or release;
- a watcher receipt is process memory, not proof of a Fauna claim.

## Wildlife sensitivity and exposure

Watch metadata must not reveal or enable reconstruction of exact animal occurrences,
nests, dens, roosts, hibernacula, spawning or breeding sites, telemetry, steward-only
records, private identities, or protected habitat joins. Logs, hashes, diff excerpts,
issue text, receipts, alerts, and generated summaries are all exposure surfaces.

A changed ETag, checksum, timestamp, version, manifest, or header does not establish that
a Fauna fact changed. Sensitive or ambiguous changes route to quarantine and human
review. Public-safe generalization must be decided by accepted policy outside this lane.

## Mutation and retention

This lane is immutable at runtime and retains only reviewed Git history. It stores no
source snapshots, fetched payloads, secrets, temporary state, receipts, proofs, or
published artifacts. Executable watchers and their runtime state belong under their
accepted implementation and data responsibility roots.

## Validation

From the repository root, run:

```bash
python tools/validators/validate_pipeline_spec_declarations.py
pytest -q tests/validators/test_validate_pipeline_spec_declarations.py
python tools/validators/directory_governance/validate_repository_topology.py
```

At present, validation must confirm this lane has no declaration and that documentation
does not imply activation. Future shape validation would not authorize network access,
source admission, lifecycle writes, promotion, release, or publication.

## Related authority families

- Declaration contract: [`contracts/pipeline_spec_declaration.md`](../../../contracts/pipeline_spec_declaration.md)
- Machine schema: [`schemas/contracts/v1/pipeline_spec_declaration.schema.json`](../../../schemas/contracts/v1/pipeline_spec_declaration.schema.json)
- Shared watcher specs: [`pipeline_specs/watchers/`](../../watchers/README.md)
- Executable watcher code: [`pipelines/watchers/`](../../../pipelines/watchers/README.md)
- Fauna implementation: [`pipelines/domains/fauna/`](../../../pipelines/domains/fauna/README.md)
- Fauna doctrine: [`docs/domains/fauna/`](../../../docs/domains/fauna/README.md)
- Policy: [`policy/domains/fauna/`](../../../policy/domains/fauna/README.md)
- Sensitivity policy: [`policy/sensitivity/fauna/`](../../../policy/sensitivity/fauna/README.md)
- Fixtures and tests: [`fixtures/domains/fauna/`](../../../fixtures/domains/fauna/README.md), [`tests/domains/fauna/`](../../../tests/domains/fauna/README.md)
- Release candidates: [`release/candidates/fauna/`](../../../release/candidates/fauna/README.md)

## Status and open verification

The README-only inventory is confirmed. Placement, ownership, parser/registry support,
consumer binding, admitted sources, cadence, rights, materiality vocabulary, sensitivity
controls, fixtures, tests, receipt handling, workflow wiring, and rollback remain open.

Resolve placement before adding a YAML declaration. The decision must state whether the
shared watcher lane, this domain-local lane, or another accepted boundary owns Fauna
watcher intent, and it must prevent duplicate writable authority.

## Review triggers and rollback

Review is required for any placement, declaration, source role, cadence, comparison
signal, lifecycle edge, sensitivity posture, binding, or ownership change. Any newly
reconstructable wildlife signal triggers sensitivity review and fail-closed handling.

Rollback means revert the declaration or documentation change, keep all execution and
network access disabled, and preserve the review record. Any already-created data or
release correction must be handled by its owning lifecycle or release authority.
