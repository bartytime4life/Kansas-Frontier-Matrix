<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/encyclopedia/chapters/04-operating-law
title: "Operating law in daily work"
type: planning-reference
version: v1.0
status: draft; repository-grounded; non-authoritative; placement-hold
owners: ["@bartytime4life via CODEOWNERS; domain review remains pending"]
created: 2026-10-08
created_note: Metadata records substantive draft authorship; the existing path predates this edition.
updated: 2026-10-08
policy_label: public; planning-reference
owning_root: docs/
responsibility: "Explain operating law in daily work and route readers to the owning KFM sources."
truth_posture: PROPOSED guidance; repository-grounded draft at ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe; not ADR acceptance, source admission, release or publication.
related:
  - docs/encyclopedia/INDEX.md
  - docs/KFM-encyclopedia.md
[/KFM_META_BLOCK_V2] -->

# Operating law in daily work

Evidence snapshot: `main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe`. Draft reference; formal lane acceptance remains pending.

The [Directory Rules](../../doctrine/directory-rules.md) and accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) define responsibility boundaries. This chapter explains how to apply them; it does not amend them.

## Route changes by responsibility

| You are changing | Owning surface | Review question |
|---|---|---|
| Human explanation | `docs/` | Does every material claim have support? |
| Semantic meaning | `contracts/` | Are identity, units and edge cases explicit? |
| Machine shape | `schemas/` | Are valid and invalid inputs distinguished? |
| Admissibility | `policy/` | Which evaluator and authority make the decision? |
| Executable behavior | `tools/`, `packages/`, `pipelines/`, `apps/` | Is the real behavior tested? |
| Lifecycle and accountability data | Governed `data/` lanes | Is identity and lineage preserved? |
| Release decision | `release/` and its governed records | Is the exact candidate approved? |

## Before editing

Inspect repository identity, branch, commit and dirty state. Preserve unfinished work. Compare proposed paths with their existing responsibility, readers and writers. An existing filename does not prove that its content or placement is accepted. For structural changes, follow the accepted decision process rather than deriving authority from this chapter.

## Before reporting success

Name the actual action and its evidence: a file was authored, a test passed, a PR merged, a version deployed, or a reviewer accepted a candidate. Those are distinct events. Record the scope and exact version for each. An author can prepare review material without becoming its independent reviewer.

If documentation conflicts with implementation, retain the conflict and identify the source that owns the fact. Avoid silently rewriting immutable receipts, historic snapshots or accepted decision bytes. Use a correction or successor where required.

The [truth-posture guide](../../doctrine/truth-posture.md), [lifecycle law](../../doctrine/lifecycle-law.md), and [trust membrane](../../doctrine/trust-membrane.md) supply the detailed rules behind these daily checks.

[Chapter index](../INDEX.md) · [Reader guide](01-cover.md)
