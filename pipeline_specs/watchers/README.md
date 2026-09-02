<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-watchers-readme
title: pipeline_specs/watchers/ — Pipeline Specification Boundary
type: readme
version: v1.0
status: proposed-inactive; repository-grounded
owners: OWNER_TBD — pipeline-spec steward; domain steward; validation reviewer
created: 2026-06-13
updated: 2026-08-30
policy_label: public-metadata; declarative-only; fail-closed; no-live-activation
owning_root: pipeline_specs/
responsibility: govern inactive declarative pipeline intent for the watchers scope
truth_posture: CONFIRMED inventory and fail-closed posture / PROPOSED declarations / NEEDS VERIFICATION activation prerequisites
readme_profile: BOUNDARY_COMPACT
current_path: pipeline_specs/watchers/README.md
inherited_parent: pipeline_specs/README.md
scope_id: watchers
related:
  - pipeline_specs/README.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - contracts/pipeline_spec_declaration.md
  - schemas/contracts/v1/pipeline_spec_declaration.schema.json
notes: ["Metadata is flat by contract; validation does not activate a source, pipeline, lifecycle write, release, or publication."]
[/KFM_META_BLOCK_V2] -->

# `pipeline_specs/watchers/` boundary

## Purpose and inherited parent

This cross-domain lane inherits [`pipeline_specs/`](../README.md). It may hold declarative watcher intent or gate profiles only when one domain lane cannot uniquely own them. Executable watcher behavior belongs under [`pipelines/`](../../pipelines/README.md) or [`tools/`](../../tools/README.md), according to its responsibility.

A watcher may identify a candidate change for governed review. It cannot admit a source, certify domain truth, approve promotion, rewrite catalog authority, publish, or issue a public alert.

File presence never activates execution. Network access, lifecycle writes, source activation, promotion, release, and publication are `DENIED` for the current declarations and profiles.

## Local owner and scope

- Scope ID: `shared-watchers`
- Local owner: `OWNER_TBD — shared watcher pipeline-spec steward`
- Required reviewers: affected domain, source/rights, sensitivity, security, evidence, policy, validation, and release stewards
- Boundary profile: `BOUNDARY_COMPACT`
- Placement rule: use this lane only after a path decision demonstrates cross-domain ownership.

## Belongs

- Schema-valid, inactive shared watcher declarations.
- Cross-domain watcher gate profiles with stable identity and deterministic hashes.
- References to admitted sources, finite outcomes, fixtures, validators, evidence, and policies.
- Explicit hold, denial, correction, supersession, and rollback metadata.

## Prohibited

- Executable fetch, comparison, transformation, scheduling, or notification code.
- Credentials, endpoints containing secrets, source payloads, cached responses, or unrestricted diffs.
- Source admission, lifecycle promotion, catalog mutation, release approval, publication, or public-alert authority.
- Domain-specific declarations placed here merely for naming symmetry.
- Logs or summaries exposing rare species, archaeology, living persons, DNA, protected infrastructure, or restricted source terms.

## Inputs and outputs

| Direction | Governed posture |
|---|---|
| Inputs | References to admitted source metadata, prior snapshots, schemas, policies, and public-safe fixtures |
| Candidate outputs | Finite `NO_ACTION`, `WORK`, or `QUARANTINE` intent and receipt-family references; no current writes |
| Writes | `false` for the YAML declaration; JSON profiles grant no execution authority |
| Runtime effects | None; all three machine-readable files are inactive |

A changed checksum, ETag, timestamp, schema, or payload size is a review signal, not proof that domain truth changed or publication is warranted.

## Exposure, mutation, and retention

- Exposure: internal declarations and profiles only; no direct public or notification path.
- Sensitivity: comparison output must be minimized; restricted details default to `QUARANTINE` or abstention.
- Mutation: pull-request review with stable IDs and deterministic hashes. Do not rewrite accepted evidence or profile identity.
- Retention: keep proposal/supersession history; store runtime snapshots, diffs, receipts, and evidence in their governed data families.

## Current direct-child map

Verified 2026-08-30. Direct children only:

```text
watchers/
├── README.md                    # this local boundary contract
├── plants_drift.yaml            # inactive candidate; placement is on hold
├── soil_ssurgo_gnatsgo.json     # fixture-only soil watcher specification
└── watcher_gate_profile.v1.json # inactive shared gate threshold profile
```

## Declaration and profile inventory

| File | Object/class | Status | Authority |
|---|---|---|---|
| `plants_drift.yaml` | Pipeline candidate | `PROPOSED_INACTIVE`; `NOT_IMPLEMENTED`; `DISABLED` | None |
| `soil_ssurgo_gnatsgo.json` | `SoilWatcherSpec` | `PROPOSED_INACTIVE`; `FIXTURE_ONLY`; network denied | None |
| `watcher_gate_profile.v1.json` | `WatcherGateProfile` | `PROPOSED_INACTIVE` | Threshold fixture/profile only |

The YAML candidate overlaps in subject with [`pipeline_specs/flora/plants_drift_watcher.yaml`](../flora/plants_drift_watcher.yaml). Its outcome is `HOLD` with reason `PLACEMENT_REVIEW_REQUIRED`. This README does not assert which path is canonical and does not convert either file into an alias.

## Validation

- Validate `plants_drift.yaml` against the [common declaration schema](../../schemas/contracts/v1/pipeline_spec_declaration.schema.json).
- Run [`tools/validators/validate_pipeline_spec_declarations.py`](../../tools/validators/validate_pipeline_spec_declarations.py) and its fixture-backed tests.
- Validate `soil_ssurgo_gnatsgo.json` with [`validate_soil_watcher_spec.py`](../../tools/validators/domains/soil/watcher_spec/validate_soil_watcher_spec.py).
- Validate the watcher gate profile through the [watcher gate packet validator](../../tools/validators/watchers/validate_watcher_gate_packet.py) and schema.
- Run repository JSON/YAML, documentation meta-block/link, topology, secret, sensitivity, and policy checks.
- Treat missing references, hash drift, non-finite outcomes, network permission, lifecycle writes, sensitive-detail leakage, or publication authority as failure.

## Related governed families

- Common declaration contract: [`contracts/pipeline_spec_declaration.md`](../../contracts/pipeline_spec_declaration.md)
- Common declaration schema: [`schemas/contracts/v1/pipeline_spec_declaration.schema.json`](../../schemas/contracts/v1/pipeline_spec_declaration.schema.json)
- Common declaration fixtures: [`fixtures/contracts/v1/pipeline_spec_declaration/`](../../fixtures/contracts/v1/pipeline_spec_declaration/)
- Common declaration tests: [`tests/validators/test_validate_pipeline_spec_declarations.py`](../../tests/validators/test_validate_pipeline_spec_declarations.py)
- Watcher packet contract: [`contracts/watchers/watcher_gate_packet.md`](../../contracts/watchers/watcher_gate_packet.md)
- Watcher profile schema: [`schemas/contracts/v1/watchers/watcher_gate_profile.schema.json`](../../schemas/contracts/v1/watchers/watcher_gate_profile.schema.json)
- Soil watcher contract: [`contracts/domains/soil/soil_watcher_spec.md`](../../contracts/domains/soil/soil_watcher_spec.md)
- Soil watcher schema: [`schemas/contracts/v1/domains/soil/soil_watcher_spec.schema.json`](../../schemas/contracts/v1/domains/soil/soil_watcher_spec.schema.json)
- Soil watcher policy: [`policy/domains/soil/watcher_spec.rego`](../../policy/domains/soil/watcher_spec.rego)
- Soil watcher fixtures: [`fixtures/domains/soil/watcher_spec/`](../../fixtures/domains/soil/watcher_spec/README.md)
- Soil watcher tests: [`tests/validators/domains/soil/watcher_spec/`](../../tests/validators/domains/soil/watcher_spec/test_validate_soil_watcher_spec.py)
- Release families: [`release/candidates/flora/`](../../release/candidates/flora/README.md) and [`release/candidates/soil/`](../../release/candidates/soil/README.md)
- Accepted governance: [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) and [Directory Rules v2](../../docs/doctrine/directory-rules.md)

## Status and open verification

Status: one inactive YAML candidate and two inactive schema-backed JSON profiles. No active source, schedule, network path, writer, notifier, publisher, or release is established.

Open verification items:

- Name the shared watcher owner and domain reviewers.
- Resolve plants-drift placement with an evidence-backed path decision; remain on `HOLD` until then.
- Verify active consumers, if any, and bind only admitted sources.
- Define minimized receipt and notification boundaries before any activation proposal.
- Establish correction, supersession, withdrawal, and release review for each profile family.

## Review triggers and rollback

Re-review when placement, a declaration/profile, source, consumer, owner, schema, policy, finite outcome, sensitivity, exposure, workflow, or release family changes; when an ADR changes; or when drift, security, correction, withdrawal, or rollback occurs.

Rollback changes by reverting the owning commit and re-running the applicable validators. A rollback does not reactivate an older source, watcher, notification, or release. If placement remains ambiguous, preserve both identities as inactive evidence and keep the outcome `HOLD`; do not create parallel writable authorities.
