<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION/verification-backlog
title: Verification Backlog
type: register
version: v1
status: draft
owners: NEEDS_VERIFICATION
created: NEEDS_VERIFICATION
updated: 2026-04-27
policy_label: NEEDS_VERIFICATION
related: [README.md, AUTHORITY_LADDER.md, CANONICAL_LINEAGE_EXPLORATORY.md, DRIFT_REGISTER.md]
tags: [kfm, registers, verification, evidence, backlog]
notes: [Initial evidence backlog for register hardening; convert placeholders to concrete owners, labels, and checks as evidence is collected.]
[/KFM_META_BLOCK_V2] -->

# Verification Backlog

Defines concrete evidence required before upgrading register claims from `PROPOSED` or `UNKNOWN` to `CONFIRMED`.

## Active backlog

| Backlog ID | Date opened | Claim to verify | Evidence required | Status | Owner | Linked drift |
|---|---|---|---|---|---|---|
| VB-001 | 2026-04-27 | Register ownership is known and enforceable. | Confirm owning team in `.github/CODEOWNERS` and replace placeholders in all `docs/registers/*.md`. | OPEN | NEEDS_VERIFICATION | DRIFT-002 |
| VB-002 | 2026-04-27 | Policy label for register docs is settled. | Identify approved policy label source and update metadata blocks consistently. | OPEN | NEEDS_VERIFICATION | DRIFT-002 |
| VB-003 | 2026-04-27 | Register maintenance checks are part of CI or documented local workflow. | Add/verify command(s) or workflow step that checks register links/placeholders. | OPEN | NEEDS_VERIFICATION | DRIFT-001 |

## Completion criteria

An item can be closed when all conditions are met:

1. Evidence is linked to a concrete file, command output, or workflow run.
2. A reviewer acknowledges the evidence in PR review or ADR notes.
3. Related drift items are updated to `resolved` or narrowed.

## Entry template

```markdown
| VB-### | YYYY-MM-DD | <claim> | <required evidence> | OPEN\|IN_PROGRESS\|DONE | <owner> | <drift id or n/a> |
```
