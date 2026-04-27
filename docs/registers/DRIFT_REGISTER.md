<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION/drift-register
title: Drift Register
type: register
version: v1
status: draft
owners: NEEDS_VERIFICATION
created: NEEDS_VERIFICATION
updated: 2026-04-27
policy_label: NEEDS_VERIFICATION
related: [README.md, AUTHORITY_LADDER.md, CANONICAL_LINEAGE_EXPLORATORY.md, VERIFICATION_BACKLOG.md]
tags: [kfm, registers, drift, contradictions, governance]
notes: [Initial drift register with starter entries and a template for ongoing conflict tracking.]
[/KFM_META_BLOCK_V2] -->

# Drift Register

Tracks contradictions, naming splits, overclaims, and authority ambiguity across documentation and implementation surfaces.

## Open drift items

| Drift ID | Date opened | Area | Conflict summary | Current truth | Risk if ignored | Owner | Next action |
|---|---|---|---|---|---|---|---|
| DRIFT-001 | 2026-04-27 | Register coverage | `docs/registers/README.md` listed four sibling register files that were missing from tree. | CONFIRMED | Maintainers cannot record authority/drift decisions consistently. | NEEDS_VERIFICATION | Closed by adding initial register files in this branch. |
| DRIFT-002 | 2026-04-27 | Metadata quality | Multiple register docs still contain `NEEDS_VERIFICATION` placeholders for owner/policy labels. | CONFIRMED | Ownership ambiguity delays review and escalation. | NEEDS_VERIFICATION | Resolve after CODEOWNERS/policy label confirmation. |

## Workflow

1. Add an entry for every meaningful contradiction or overclaim.
2. Link each entry to verification work in `VERIFICATION_BACKLOG.md`.
3. Close an entry only when evidence and review show convergence.

## Entry template

```markdown
| DRIFT-### | YYYY-MM-DD | <area> | <conflict summary> | <truth label> | <risk> | <owner> | <next action> |
```
