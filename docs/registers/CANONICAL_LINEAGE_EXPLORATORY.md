<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION/canonical-lineage-exploratory
title: Canonical / Lineage / Exploratory Register
type: register
version: v1
status: draft
owners: NEEDS_VERIFICATION
created: NEEDS_VERIFICATION
updated: 2026-04-27
policy_label: NEEDS_VERIFICATION
related: [README.md, AUTHORITY_LADDER.md, DRIFT_REGISTER.md, VERIFICATION_BACKLOG.md]
tags: [kfm, registers, canon, lineage, exploratory, classification]
notes: [Initial classification register scaffold; entries should be updated as directories are reviewed and ADRs are accepted.]
[/KFM_META_BLOCK_V2] -->

# Canonical / Lineage / Exploratory Register

Tracks documentation/source families by authority class so maintainers can classify before citing.

## Status classes

- **Canonical**: current governing source for a concern.
- **Lineage**: historical/superseded context worth preserving.
- **Exploratory**: useful but non-governing, non-proving material.
- **Reference**: external context not adopted as doctrine.
- **Superseded**: replaced by newer canonical source.

## Register entries

| Scope | Current class | Why | Promotion/demotion trigger | Owner |
|---|---|---|---|---|
| `policy/` rules + policy tests | Canonical | Defines allow/deny behavior and obligations. | ADR/policy update accepted and validated. | NEEDS_VERIFICATION |
| Versioned schemas/contracts | Canonical | Machine-checkable definitions for payloads and artifacts. | Schema-home decision or version supersession. | NEEDS_VERIFICATION |
| Accepted ADRs | Canonical | Governing decisions on boundaries and file homes. | Superseding ADR accepted. | NEEDS_VERIFICATION |
| `docs/` current standards/runbooks/architecture | Canonical | Human-governed doctrine and operating guidance. | Superseded by accepted ADR + doc update. | NEEDS_VERIFICATION |
| Historic manuals / old architecture packets | Lineage | Useful context but not current authority. | Explicit promotion via ADR + verification. | NEEDS_VERIFICATION |
| Intake ideas / exploratory packets | Exploratory | Candidate guidance lacking implementation proof. | Verified implementation + review + migration. | NEEDS_VERIFICATION |
| External standards and vendor references | Reference | Contextual technical input. | Explicit adoption into policy/schema/ADR. | NEEDS_VERIFICATION |
| Deprecated docs with successor path | Superseded | Kept for audit trail and traceability. | Removal only per retention policy. | NEEDS_VERIFICATION |

## Entry template

Use this snippet for new classifications:

```markdown
| <path or family> | <class> | <justification> | <promotion/demotion trigger> | <owner> |
```

## Rules

1. A file/family is not canonical unless there is a clear current owner and non-conflicting authority path.
2. Repetition across sources does not increase authority class.
3. Promotion from exploratory/lineage to canonical requires explicit evidence and review.
