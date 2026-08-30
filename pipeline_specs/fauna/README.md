<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-fauna-readme
title: pipeline_specs/fauna/ — Pipeline Specification Boundary
type: readme
version: v1.0
status: proposed-inactive; repository-grounded
owners: OWNER_TBD — pipeline-spec steward; domain steward; validation reviewer
created: 2026-06-13
updated: 2026-08-30
policy_label: public-metadata; declarative-only; fail-closed; no-live-activation
owning_root: pipeline_specs/
responsibility: govern inactive declarative pipeline intent for the fauna scope
truth_posture: CONFIRMED inventory and fail-closed posture / PROPOSED declarations / NEEDS VERIFICATION activation prerequisites
readme_profile: BOUNDARY_COMPACT
current_path: pipeline_specs/fauna/README.md
inherited_parent: pipeline_specs/README.md
scope_id: fauna
related:
  - pipeline_specs/README.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - contracts/pipeline_spec_declaration.md
  - schemas/contracts/v1/pipeline_spec_declaration.schema.json
notes: ["Metadata is flat by contract; validation does not activate a source, pipeline, lifecycle write, release, or publication."]
[/KFM_META_BLOCK_V2] -->

# Fauna pipeline declarations

`pipeline_specs/fauna/` owns declarative Fauna run intent. It may describe candidate
stage boundaries and required gates. It does not own executable pipeline code,
source admission, wildlife truth, sensitivity decisions, lifecycle mutation, or release.

This is a Directory Rules v2 `BOUNDARY_COMPACT` contract adopted through
[`ADR-0029`](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md).
It inherits the root rules in [`pipeline_specs/README.md`](../README.md).

## Boundary posture

| Control | Required posture |
|---|---|
| Declaration status | `PROPOSED_INACTIVE` |
| Implementation status | `NOT_IMPLEMENTED` for every declaration in this lane |
| Source activation | `DENIED` |
| Network access | `DENIED` |
| Lifecycle writes | `DENIED` |
| Promotion | `DENIED` |
| Release | `DENIED` |
| Publication | `DENIED` |
| Rollback | `REVERT_DECLARATION_CHANGE` |

File presence, schema validity, merge state, or a named schedule does not activate a
declaration. Every consequential transition remains review-gated outside this lane.

## Purpose and ownership

This directory may hold closed `KfmPipelineSpecDeclaration` documents for the Fauna
domain. Each document records identity, candidate lifecycle edges, bindings, required
gates, non-effects, and deterministic hash material.

The pipeline-spec steward owns declaration shape and placement. The Fauna steward owns
domain intent. Source, rights, sensitivity, validation, evidence, policy, and release
stewards retain their separate authorities. Unassigned ownership fails closed.

## Belongs here

- inactive Fauna stage-boundary declarations;
- inactive Fauna pipeline candidates with explicit evidence bindings;
- references to accepted contracts, schemas, fixtures, tests, and workflows;
- candidate inputs and outputs that are explicitly non-writing;
- bounded reason codes, gate requirements, and rollback posture.

## Prohibited here

- Python, SQL, shell, connector, scheduler, or deployment implementation;
- credentials, private endpoints, live source payloads, or source activation flags;
- source-admission, taxonomy, rights, geoprivacy, policy, or release decisions;
- exact or reconstructable sensitive wildlife locations or identities;
- generated evidence claims, proof closure, catalog mutation, or publication state;
- a second writable declaration for the same responsibility.

## Direct-child map

Only direct children are shown; nested lanes define their own contracts.

```text
pipeline_specs/fauna/
├── README.md
├── catalog.yaml
├── ingest.yaml
├── normalize.yaml
├── publish.yaml
├── refresh.yaml
├── validate.yaml
└── watchers/
```

## Declaration inventory

All six declarations use `schema_version: 1.0.0`,
`object_type: KfmPipelineSpecDeclaration`, and `spec_version: 0.1.0`.

| File | `spec_id` | Kind | Stage | Status / implementation |
|---|---|---|---|---|
| `catalog.yaml` | `kfm.pipeline.fauna.catalog` | `STAGE_BOUNDARY` | `CATALOG` | `PROPOSED_INACTIVE` / `NOT_IMPLEMENTED` |
| `ingest.yaml` | `kfm.pipeline.fauna.ingest` | `STAGE_BOUNDARY` | `INGEST` | `PROPOSED_INACTIVE` / `NOT_IMPLEMENTED` |
| `normalize.yaml` | `kfm.pipeline.fauna.normalize` | `STAGE_BOUNDARY` | `NORMALIZE` | `PROPOSED_INACTIVE` / `NOT_IMPLEMENTED` |
| `publish.yaml` | `kfm.pipeline.fauna.publish` | `STAGE_BOUNDARY` | `PUBLISH` | `PROPOSED_INACTIVE` / `NOT_IMPLEMENTED` |
| `refresh.yaml` | `kfm.pipeline.fauna.refresh` | `PIPELINE_CANDIDATE` | `REFRESH` | `PROPOSED_INACTIVE` / `NOT_IMPLEMENTED` |
| `validate.yaml` | `kfm.pipeline.fauna.validate` | `STAGE_BOUNDARY` | `VALIDATE` | `PROPOSED_INACTIVE` / `NOT_IMPLEMENTED` |

No declaration is an activation record or executable plan. Empty implementation,
fixture, test, workflow, and source-descriptor bindings are unresolved dependencies,
not permission to proceed.

## Inputs and outputs

Declared lifecycle edges are candidates only:

| Stage | Candidate inputs | Candidate outputs |
|---|---|---|
| `INGEST` | `SOURCE_CAPTURE_CANDIDATE` | `QUARANTINE`, `RAW` |
| `NORMALIZE` | `QUARANTINE`, `RAW` | `QUARANTINE`, `WORK` |
| `VALIDATE` | `QUARANTINE`, `WORK` | `PROCESSED`, `QUARANTINE` |
| `CATALOG` | `PROCESSED` | `CATALOG` |
| `PUBLISH` | `CATALOG`, `PROCESSED`, `PROOF`, `RELEASE_DECISION` | `PUBLISHED` |
| `REFRESH` | `SOURCE_CAPTURE_CANDIDATE` | `NO_ACTION`, `QUARANTINE`, `RAW` |

`lifecycle.writes_targets` remains `false`. A candidate output does not create a
lifecycle object, close evidence, or confer publication authority.

## Exposure, mutation, and retention

Repository-visible declarations may expose public-safe metadata only. Exact animal
occurrences, nests, dens, roosts, hibernacula, spawning or breeding sites, telemetry,
steward-controlled records, private identities, and joinable location clues are
deny-by-default. Logs, receipts, diffs, issues, and generated summaries must not make
restricted information reconstructable.

This lane is immutable at runtime. It retains reviewed declaration history through Git;
it stores no fetched payloads, derived records, secrets, temporary artifacts, or release
outputs. Correction and withdrawal happen in their owning lifecycle and release lanes.

## Validation

From the repository root, run:

```bash
python tools/validators/validate_pipeline_spec_declarations.py
pytest -q tests/validators/test_validate_pipeline_spec_declarations.py
python tools/validators/directory_governance/validate_repository_topology.py
```

Validation proves shape and repository consistency only. It does not prove source
admission, factual correctness, sensitivity clearance, evidence closure, or release.

## Related authority families

- Declaration contract: [`contracts/pipeline_spec_declaration.md`](../../contracts/pipeline_spec_declaration.md)
- Machine schema: [`schemas/contracts/v1/pipeline_spec_declaration.schema.json`](../../schemas/contracts/v1/pipeline_spec_declaration.schema.json)
- Executable Fauna code: [`pipelines/domains/fauna/`](../../pipelines/domains/fauna/README.md)
- Domain doctrine: [`docs/domains/fauna/`](../../docs/domains/fauna/README.md)
- Policy: [`policy/domains/fauna/`](../../policy/domains/fauna/README.md)
- Sensitivity policy: [`policy/sensitivity/fauna/`](../../policy/sensitivity/fauna/README.md)
- Fixtures and tests: [`fixtures/domains/fauna/`](../../fixtures/domains/fauna/README.md), [`tests/domains/fauna/`](../../tests/domains/fauna/README.md)
- Release candidates: [`release/candidates/fauna/`](../../release/candidates/fauna/README.md)

## Status and open verification

The directory and six-file inventory are confirmed. Every declaration remains
`PROPOSED_INACTIVE` and `NOT_IMPLEMENTED`. Before any activation proposal, verify an
accepted parser and registry, explicit consumer binding, admitted source descriptors,
rights, taxonomy authority, sensitivity policy, deterministic fixtures, executable
tests, evidence and receipt handling, rollback, ownership, and separate release review.

The nested `watchers/` placement is `HOLD / PLACEMENT_REVIEW_REQUIRED`; this contract
does not invent a canonical target or imply that a Fauna watcher profile exists.

## Review triggers and rollback

Review is required for any schema version, lifecycle edge, binding, gate, source role,
sensitivity posture, path, ownership, or status change. Wildlife disclosure risk or a
new reconstructable join is a mandatory sensitivity review trigger.

Rollback means revert the declaration change, keep execution disabled, preserve the
review record, and route any already-created data correction or withdrawal through its
own authority. Reverting this file never substitutes for lifecycle or release rollback.
