<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-standards-markdown-work-protocol
title: KFM Markdown Work Protocol
type: standard
version: v1
status: draft
owners: NEEDS_VERIFICATION
created: 2026-04-28
updated: 2026-04-28
policy_label: NEEDS_VERIFICATION
related: [README.md, markdown-rules.md, ../README.md, ../../tools/ci/README.md]
tags: [kfm, standards, markdown, documentation, protocol]
notes: [Normative prose protocol; keep this synchronized with task-facing markdown-rules.md.]
[/KFM_META_BLOCK_V2] -->

# KFM Markdown Work Protocol

Normative protocol for authoring and reviewing Markdown in standards surfaces.

## Required posture

- Use explicit truth posture (`CONFIRMED`, `INFERRED`, `PROPOSED`, `UNKNOWN`, `NEEDS VERIFICATION`) when confidence matters.
- Prefer routing claims to executable evidence instead of implying enforcement.
- Preserve correction lineage; avoid silent deletions for materially reviewed content.

## Minimum structure

1. One H1 per file.
2. A metadata block.
3. Scope/boundary statement.
4. Clear non-goals for high-risk claims.

## Review expectations

- Validate links before merge.
- Identify downstream proof burden when adding normative requirements.
- Keep this protocol and `markdown-rules.md` aligned.
