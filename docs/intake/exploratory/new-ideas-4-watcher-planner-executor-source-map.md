<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/new-ideas-4-watcher-planner-executor
title: New Ideas 4 — Watcher-Planner-Executor source map
type: exploratory-source-map
version: v1.0.0
status: proposed; source-adaptation; non-authoritative
created: 2026-08-07
updated: 2026-08-07
policy_label: internal; exploratory
related:
  - ../../../contracts/governance/agent_operation_envelope.md
  - ../../../schemas/contracts/v1/governance/agent_operation_envelope.schema.json
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [new-ideas, agents, watcher, planner, executor, source-map, intake]
[/KFM_META_BLOCK_V2] -->

# New Ideas 4 — Watcher-Planner-Executor source map

## Source boundary

| Field | Value |
|---|---|
| Source | `New Ideas 4.pdf` supplied in the authoring session |
| Source role | Exploratory design input; not repository or runtime authority |
| Current repository base | `main@14b9608addcf6cac80adaa0a836182f7a6e47806` |
| Placement authority | Accepted ADR-0029 and Directory Rules v2 |
| Implemented slice | Fixture-only `AgentOperationEnvelope` contract, schema, cases, validator, tests, read-only CI, and authoring receipt |
| Deferred live behavior | Source polling, external network calls, GitHub App credentials, check-run posting, branch mutation, PR mutation, signing, telemetry transport, release, deployment, publication |

## Adopted ideas

| Source idea | Repository adaptation | Reason |
|---|---|---|
| Separate Watcher, Planner, and Executor | Exact role matrix and role-specific input/output/capability ceilings | Prevents one automation profile from accumulating observation, planning, branch, merge, and publication authority. |
| Watcher is read-only | Watcher accepts a synthetic source snapshot and emits only facts/alerts | Preserves watcher-as-non-publisher doctrine. |
| Planner is deterministic | Pinned clock, commit seed, input hash, JCS/SHA-256 identity, no network | Supports replay and stable review. |
| Executor is PR-only | Ceiling allows unprotected feature-branch plus draft-PR writes; merge/protected/release/deploy/publish remain false | Preserves human and repository governance. |
| Idempotency key | Derived from role, subject, time window, commit seed, and input-bundle hash | Repeated identical operations converge on one identity. |
| Kill switch | Checked state holds Planner/Executor when engaged | Provides fail-closed containment without silencing read-only observation. |
| Validation gates | Ordered schema, policy, QA, and reproducibility declarations | Makes gate state explicit and finite. |
| Finite failure states | `READY`, `HOLD`, `DENY`, `ERROR` | Avoids implicit allow or ambiguous failure. |

## Path reconciliation

The source packet contains implementation-style paths under `src/`, top-level `plans/`, `prov/`, `telemetry/`, `sbom/`, and `artifacts/`. Those paths were not copied.

Directory Rules v2 routes the slice through existing responsibility roots:

- semantic meaning -> `contracts/governance/`;
- machine shape -> `schemas/contracts/v1/governance/`;
- synthetic inputs -> `fixtures/contracts/v1/governance/`;
- repository validator -> `tools/validators/governance/`;
- conformance proof -> `tests/validators/governance/`;
- platform orchestration -> `.github/workflows/`;
- source adaptation -> `docs/intake/exploratory/`;
- authoring provenance -> `data/receipts/generated/`.

This avoids the unresolved root `src/`, prevents new parallel authority, and keeps trust-bearing objects out of the transitional `artifacts/` root.

## Deferred or narrowed ideas

| Idea | Disposition | Verification needed before a later slice |
|---|---|---|
| HTTP ETag, ArcGIS change APIs, STAC diffs | Deferred | Source admission, rights, endpoint behavior, rate limits, connector ownership, fixture policy. |
| OpenLineage event POSTs | Deferred | Endpoint authority, authentication, network boundary, telemetry schema/profile, failure handling. |
| Sigstore/gitsign/Cosign attestations | Deferred | Accepted signing profile, OIDC audience, subject identity, registry, offline verification, rollback semantics. |
| GitHub App Check Runs and PR mutation | Deferred | App installation, exact permission matrix, ruleset coupling, concurrency, audit receipts, branch lifecycle, human review. |
| Energy/carbon gate | Narrowed to no implementation | Measurement authority, units, hardware attribution, SLO ownership, failure semantics. |
| Automatic publication after merge | Denied for this source adaptation | Merge is not promotion, release, deployment, or publication in KFM. |
| Executor opening a ready/non-draft PR | Denied in v1 | The current profile allows draft PR only. |
| Direct protected-branch or production-store writes | Denied | Violates the trust membrane and PR-first governance. |

## Acceptance boundary

The slice is complete when:

1. the schema is Draft 2020-12 valid;
2. each role's exact capability ceiling is enforced;
3. Planner/Executor hold under an engaged kill switch;
4. gate outcomes map deterministically to finite dispositions;
5. idempotency and envelope identities replay exactly;
6. protected-branch, merge, release, deployment, and publication overreach fail closed;
7. validation is deterministic and no-network;
8. the generated authoring receipt binds every non-self artifact.

## Non-effects

This source map and its implementation do not adopt the source packet as doctrine, create a live agent architecture, activate a source, install credentials, write a branch, open a pull request at runtime, merge, promote, release, deploy, publish, or authorize public use.
