<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/source-role-use-request
title: SourceRoleUseRequest Contract
type: semantic-contract
version: v1.0.0
status: draft; PROPOSED_INACTIVE; fixture-first
owners: OWNER_TBD — Source steward · Evidence steward · Policy steward · Validation steward
created: 2026-08-07
updated: 2026-08-07
policy_label: internal; source-role; anti-collapse; fail-closed; non-authoritative
owning_root: contracts/
responsibility: Define the meaning and authority boundary of one bounded request to reuse an admitted SourceDescriptor role in a downstream consumer without upgrading, erasing, or treating that role as claim truth, evidence closure, policy approval, release approval, or public permission.
related:
  - ../../schemas/contracts/v1/source/source_role_use_request.schema.json
  - ../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../fixtures/contracts/v1/source/source_role_use_request/base.json
  - ../../fixtures/contracts/v1/source/source_role_use_request/cases.json
  - ../../tools/validators/source_role/validate_source_role.py
  - ../../tests/validators/test_validate_source_role.py
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "This contract does not assign source roles. It checks whether a downstream request preserves the role and limits already declared by a SourceDescriptor."
  - "A PASS is a bounded compatibility result, not evidence, policy, review, source activation, release, publication, or public-use authority."
[/KFM_META_BLOCK_V2] -->

# SourceRoleUseRequest

> A deterministic, value-minimized request and assessment boundary for asking whether one admitted `SourceDescriptor` may support specified claim roles on a declared downstream surface without source-role collapse.

## Status and authority boundary

| Field | Value |
|---|---|
| Contract status | `PROPOSED_INACTIVE` |
| Execution mode | fixture-first, no-network |
| Vocabulary authority | Active `SourceDescriptor` schema and accepted source-role doctrine |
| Mutation authority | None |
| Source activation authority | None |
| Evidence or policy authority | None |
| Release/publication authority | None |

The object carries a complete SourceDescriptor snapshot plus one downstream-use request. The validator reads those bytes and returns a finite compatibility outcome. It never assigns a role, edits a descriptor, activates a source, fetches an endpoint, creates an EvidenceBundle, decides rights or sensitivity, approves review, releases, or publishes.

## Why this object exists

KFM already defines source role, authority rank, and admissibility limits in `SourceDescriptor`, but the repository's source-role validator lane was documentation-only. Downstream carriers—catalog records, graph edges, APIs, maps, exports, Focus Mode, embeddings, and AI answers—need a small executable boundary that prevents these common authority upgrades:

- modeled becomes observed;
- aggregate becomes per-place truth;
- candidate becomes verified;
- contextual becomes authoritative;
- corroborating becomes primary;
- fixture-only becomes public evidence;
- a renderer or AI response silently drops the admitted role or limitations.

The contract does not replace domain contracts. It is an anti-corruption boundary between admitted source posture and downstream consumers.

## Object shape

A `SourceRoleUseRequest` contains:

1. `profile` — fixed profile identifier;
2. `descriptor` — one complete SourceDescriptor snapshot validated against the active source descriptor schema;
3. `use` — identity, propagated role/rank, requested claim roles, consumer surface, exposure, support references, role-change posture, and explicit authority claims;
4. `permissions` — all consequential permissions fixed `false`;
5. `non_effects` — all mutation and authority effects fixed `false`.

### Deterministic identity

```text
request_id = "kfm:source-role-use:" +
  SHA-256(RFC8785-JCS({
    profile,
    descriptor,
    use_without_request_id
  }))
```

This binds the exact descriptor snapshot and exact requested use. Changing evidence references, exposure, requested claim roles, role-change lineage, or any descriptor field creates a different request identity.

## Finite outcomes

| Outcome | Exit | Meaning |
|---|---:|---|
| `PASS` | `0` | Role/rank are preserved; requested claims fit admitted limits; declared exposure has the required bounded support. |
| `ERROR` | `2` | Input, schema, ordering, identity, or internal state is malformed or contradictory. |
| `HOLD` | `3` | The request is well formed but awaits evidence, policy/review, release/rollback support, or a new governed descriptor after a role change. |
| `RESTRICT` | `4` | Use is compatible only in internal or steward-gated contexts because rights or sensitivity remain restrictive. |
| `ABSTAIN` | `5` | The source posture is too weak or uncertain for the requested claim role. |
| `DENY` | `6` | AI-inferred role, silent role/rank collapse, incompatible claim use, overclaim, denied rights, or public-surface leakage is present. |

Precedence is `ERROR > DENY > HOLD > RESTRICT > ABSTAIN > PASS`.

## Core rules

### Role and rank preservation

`use.propagated_source_role` and `use.propagated_authority_rank` must equal the admitted descriptor values. A correction, supersession, or retirement request with explicit lineage remains `HOLD`; it does not modify the descriptor. A silent change is `DENY`.

### Claim-role compatibility

Every requested claim role must be present in `descriptor.admissibility_limits.allowed_claim_roles` and absent from `prohibited_claim_roles`. The validator reads the accepted claim-role vocabulary from the active SourceDescriptor schema rather than defining a second vocabulary.

### Public exposure

A public request fails closed unless all of the following are true:

- rights are verified for use;
- the default sensitivity is public or low;
- `public_release.allowed` is true;
- review state is reviewed or approved;
- release state is released;
- evidence, policy decision, review, release manifest, correction, and rollback references are present;
- the role is not candidate-only or fixture-only.

These checks establish only bounded request compatibility. They do not authenticate any reference or authorize public release.

### No overclaim

All fields in `use.authority_claims` must remain false. Source-role metadata cannot be represented as claim truth, EvidenceBundle closure, policy approval, release approval, or public permission.

## Directory Rules basis

- `contracts/source/` owns object meaning;
- `schemas/contracts/v1/source/` owns machine shape;
- `tools/validators/source_role/` owns executable anti-collapse validation;
- `tools/validators/sources/` remains a compatibility shim only;
- `fixtures/contracts/v1/source/` owns synthetic cases;
- `tests/validators/` owns executable proof;
- `.github/workflows/` owns CI;
- `docs/intake/exploratory/` owns source adaptation;
- `data/receipts/generated/` owns AI authoring provenance.

No source registry, policy, evidence, receipt, proof, lifecycle, release, or public-runtime authority is created.

## Validation

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python -m pytest -q tests/validators/test_validate_source_role.py

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
  python tools/validators/source_role/validate_source_role.py --fixtures
```

## Rollback

Before merge, close the draft PR and abandon the feature branch. After a separately authorized merge, revert the feature commit. The slice is additive except for replacing one placeholder compatibility script, so no source deactivation, data migration, release withdrawal, or public correction is required.
