<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION/authority-ladder
title: Authority Ladder
type: standard
version: v1
status: draft
owners: NEEDS_VERIFICATION
created: NEEDS_VERIFICATION
updated: 2026-04-27
policy_label: NEEDS_VERIFICATION
related: [README.md, CANONICAL_LINEAGE_EXPLORATORY.md, DRIFT_REGISTER.md, VERIFICATION_BACKLOG.md, ../README.md, ../../README.md]
tags: [kfm, registers, authority, governance, doctrine]
notes: [Initial register stub expanded into a working authority ladder; owner, policy label, and enforcement integration require verification in active branch.]
[/KFM_META_BLOCK_V2] -->

# Authority Ladder

Defines how to resolve conflicts between KFM materials and evidence classes.

## Ladder (highest to lowest)

1. **Safety/legal/policy hard-stops** in `policy/` and approved governance doctrine.
2. **Versioned machine contracts and schemas** in canonical schema homes.
3. **ADR decisions** marked accepted/current and not superseded.
4. **Current canonical documentation** under `docs/`.
5. **Implementation evidence** (tests, fixtures, generated receipts, proofs, release manifests).
6. **Lineage docs** (historical manuals and superseded guidance).
7. **Exploratory material** (idea packets, drafts, analysis notes).
8. **External references** (papers, standards, vendor docs) when not explicitly adopted.

> If two sources conflict, the higher rung wins unless an accepted ADR explicitly redefines scope.

## Conflict resolution protocol

1. Record the conflict in `DRIFT_REGISTER.md`.
2. Mark each competing claim with a truth label (`CONFIRMED`, `PROPOSED`, `UNKNOWN`, `CONFLICTED`).
3. Open/update a `VERIFICATION_BACKLOG.md` item for required evidence.
4. If authority order itself is ambiguous, raise an ADR.
5. Only promote state once evidence is attached and reviewed.

## Allowed citations by claim type

| Claim type | Minimum authority class |
|---|---|
| "Policy requires/forbids X" | Policy rule + fixture/test evidence |
| "Schema/contract defines X" | Canonical schema/contract file |
| "Architecture intends X" | Current architecture doc or accepted ADR |
| "System currently does X" | Runtime/test/release evidence |
| "Historical/manual states X" | Lineage source with non-authoritative marker |

## Anti-patterns

- Treating repeated prose as stronger than machine-validated evidence.
- Letting generated artifacts silently override doctrine without ADR/policy update.
- Using exploratory notes as implementation proof.
- Using external references as implicit policy.
