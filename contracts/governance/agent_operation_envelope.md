<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/agent-operation-envelope
title: AgentOperationEnvelope Contract
type: semantic-contract; governance; fixture-first
version: v1.0.0
status: proposed-inactive; no-network; non-mutating
owners: OWNER_TBD — governance steward · automation steward · policy steward · validation steward · repository-control steward
created: 2026-08-07
updated: 2026-08-07
policy_label: internal; fixture-only; no-authority
related:
  - ../../schemas/contracts/v1/governance/agent_operation_envelope.schema.json
  - ../../fixtures/contracts/v1/governance/agent_operation_envelope/
  - ../../tools/generators/agent_operation_envelope/
  - ../../tools/validators/governance/validate_agent_operation_envelope.py
  - ../../tests/validators/governance/test_agent_operation_envelope.py
  - ../../docs/intake/exploratory/new-ideas-4-watcher-planner-executor-source-map.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, governance, agents, watcher, planner, executor, idempotency, kill-switch, draft-pr, fixture-only]
notes:
  - "This contract adapts the Watcher-Planner-Executor separation from New Ideas 4.pdf to current KFM responsibility roots."
  - "It validates declarations only. It does not create an agent service, credential, branch, pull request, approval, merge, release, deployment, publication, or public-use authority."
[/KFM_META_BLOCK_V2] -->

# AgentOperationEnvelope Contract

> **Purpose.** Define one deterministic, fixture-only envelope that keeps Watcher, Planner, and Executor responsibilities separate and makes role overreach, kill-switch state, gate outcomes, idempotency, and PR-only executor limits machine-checkable.

## Status and authority boundary

| Field | Value |
|---|---|
| Contract status | `PROPOSED_INACTIVE` |
| Execution mode | `FIXTURE_ONLY_NO_EXTERNAL_EFFECT` |
| Network access | `FORBIDDEN` |
| Authority created | `NONE` |
| Current live agent or GitHub integration | None |
| Public-use posture | Denied |

A conforming record proves only that one synthetic operation declaration is internally consistent with this profile. It does not authenticate evidence, policy, review, attestation, GitHub permissions, branch protection, or a real runtime.

## Source-derived design

The *New Ideas 4* packet proposes three bounded roles:

1. **Watcher** — observes and emits immutable facts or alerts; never mutates code or data.
2. **Planner** — converts facts and policy inputs into deterministic plans, diff candidates, and validation evidence; never writes a branch or pull request.
3. **Executor** — consumes a validated plan and may be granted a narrow ceiling for feature-branch plus draft-PR writes; never writes a protected branch, merges, promotes, releases, deploys, or publishes.

The packet also requires deterministic seeds, idempotency keys, a central kill switch, fail-closed validation, and PR-first change delivery. This contract implements those ideas as a no-network conformance slice. Live source detection, OpenLineage transport, Sigstore signing, GitHub App credentials, and PR mutation remain separate future work.

## Directory Rules basis

Accepted ADR-0029 makes Directory Rules v2 the placement authority. The object is a governance declaration, so:

| Responsibility | Home |
|---|---|
| Semantic meaning | `contracts/governance/` |
| Machine shape | `schemas/contracts/v1/governance/` |
| Synthetic valid and invalid examples | `fixtures/contracts/v1/governance/` |
| Deterministic fixture construction | `tools/generators/agent_operation_envelope/` |
| Repository validation | `tools/validators/governance/` |
| Executable conformance proof | `tests/validators/governance/` |
| Read-only CI orchestration | `.github/workflows/` |
| Source adaptation and deferred ideas | `docs/intake/exploratory/` |
| AI authoring provenance | `data/receipts/generated/` |

No `src/`, `plans/`, `prov/`, `telemetry/`, `sbom/`, or `artifacts/` authority root is created. No existing contract, schema, policy, source, receipt, proof, release, or publication family is duplicated.

## Object meaning

An `AgentOperationEnvelope` binds these concerns without collapsing their authority:

- one actor role and component identity;
- one bounded operation kind and subject;
- one pinned window, commit_seed, input-bundle hash, and deterministic idempotency key;
- exact input and output kinds permitted for the role;
- four ordered gate declarations: schema, policy, quality assurance, and reproducibility;
- a checked kill-switch state;
- a role-specific capability ceiling and credential ceiling;
- a draft-PR target only for Executor;
- finite `READY`, `HOLD`, `DENY`, or `ERROR` disposition;
- all-false effective permissions and explicit non-effects.

### Capability ceiling is not permission

`capability_ceiling` expresses the maximum shape a separately authorized runtime profile could request. The fixture has no credential and performs no effect. The separate `permissions  object is fixed to `false` for repository writes, lifecycle writes, canonical writes, merge, promotion, release, deployment, publication, and public use.

A valid Executor record may therefore declare this ceiling:

```text
feature branch write = true
draft PR write       = true
protected branch     = false
merge                = false
release/deploy       = false
publish               = false
```

That declaration is not a token, authorization decision, GitHub App installation, branch, commit, or pull request.

## Role matrix

| Role | Inputs required | Outputs allowed | Credential ceiling | Forbidden effects |
|---|---|---|---|---|
| `WATCHER` | `SOURCE_SNAPSHOT` | `FACTS`, optional `ALERTS` | `READ_ONLY` | Planning, branch/PR writes, protected writes, merge, release, deploy, publish |
| `PLANNER` | `WATCHER_FACTS`, `POLICY_BASELINE` | `PLAN`, `DIFF_CANDIDATE`, `VALIDATION_EVIDENCE` | `READ_ONLYP | Facts authority, branch/PR writes, protected writes, merge, release, deploy, publish |
| `EXECUTOR` | `PLAN`, `VALIDATION_EVIDENCE`, `ATTESTATION` | `DRAFT_PR_METADATA`, `EXECUTION_RECEIPT` | `FEATURE_BRANCH_AND_DRAFT_PR_ONLY` | Protected writes, merge, promotion, release, deploy, publish |

Input and output bindings are sorted, kind-unique, and content-hashed. Executor targets are fixed to protected `main` as the base, an unprotected `agent/...` head, and `draft: true`.

## Deterministic identity and replay

The profile uses the repository's RFC 8785 JCS plus SHA-256 implementation.

### Idempotency key

```text
idempotency_key = SHA-256(JCS({
  role,
  subject_ref,
  window,
  commit_seed,
  input_bundle_hash
}))
```

The same role, subject, window, seed, and input bundle therefore produce the same key.

### Envelope identity

`spec_hash` is SHA-256 over the complete envelope excluding `operation_id` and `spec_hash`. `operation_id` is:

```text
kfm:agent-operation:<spec_hash hexadecimal payload>
```

Changing role, inputs, outputs, gates, kill-switch state, target, disposition, or any boundary claim changes identity.

## Kill-switch semantics

The kill switch must be checked and cite a configuration reference.

- `ENGAGED` immediately holds `PLANNER` and `EXECUTOR` with `KILL_SWITCH_ENGAGED`.
- A read-only `WATCHER` may remain `READY` under this fixture profile, with an explicit reason that it is operating read-only during the switch.
- The fixture does not read or change a real configuration file.

## Gate and disposition semantics

Gates are stored in this exact order:

```text
SCHEMA -> POLICY -> QA -> REPRODUCIBILITY
```

Disposition is derived deterministically:

1. engaged kill switch for Planner or Executor -> `HOLD`;
2. any gate `ERROR` -> `ERROR`;
3. otherwise any gate `DENY` -> `DENY`;
4. otherwise any gate `HOLD` -> `HOLD`;
5. otherwise -> `READY`.

A valid record may therefore carry a non-ready disposition. Validation checks that the declared disposition and reason codes match the inputs; it does not convert a gate declaration into authority.

## Validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Shape, role boundary, ordered bindings, deterministic identity, idempotency, gates, kill switch, disposition, and non-effects agree. |
| `DENY` | The record is malformed, over-authoritative, role-confused, hash-invalid, non-deterministic, or internally contradictory. |
| `ERROR` | The candidate could not be read or parsed safely. |

A `PASS` does not execute the declared operation.

## Fixture profile

The compact fixture manifest drives a deterministic in-memory builder. The fixture suite contains:

- ready Watcher, Planner, and Executor declarations;
- a Planner held by the kill switch;
- an Executor denied by policy;
- an Executor with a finite gate error;
- negative role-overreach, protected-branch, missing-attestation, forbidden-output, idempotency, disposition, and ordering cases.

All values are synthetic. They are not Kansas facts, source snapshots, policy decisions, reviews, attestations, or GitHub authorization records.

## Validation

```bash
python tools/generators/agent_operation_envelope/build_agent_operation_envelope.py \
  --case valid-executor-ready

python -m unittest discover \
  --start-directory tests/validators/governance \
  --pattern 'test_agent_operation_envelope.py' \
  --verbose

python tools/validators/governance/validate_agent_operation_envelope.py \
  --fixtures
```

Single-file validation:

```bash
python tools/validators/governance/validate_agent_operation_envelope.py \
  --candidate path/to/candidate.json
```

## Trust boundary

This profile does not:

- call an AI model or preserve private chain-of-thought;
- fetch an upstream source or post OpenLineage telemetry;
- resolve or authenticate evidence;
- evaluate a real policy engine or authenticate a reviewer or attestation;
- obtain or use GitHub credentials;
- create a branch, commit, check run, issue, or pull request;
- write a protected branch or merge;
- create a receipt, proof, promotion, release, correction, deployment, publication, or public-use decision outside its synthetic fixture;
- mutate a repository, lifecycle store, database, object store, catalog, or public product.

## Rollback

The slice is additive and inactive. Before merge, close the draft pull request and delete its feature branch. After an authorized merge, revert the feature commit or merge commit. No source deactivation, data migration, lifecycle reprocessing, cache purge, release withdrawal, or public correction is required.
