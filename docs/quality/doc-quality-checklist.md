<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/1d4c0e66-f094-4cc4-b9e0-23a31a531234
title: Documentation Quality Checklist
type: checklist
version: v1
status: draft
owners: kfm-core (TBD)
created: 2026-03-01
updated: 2026-03-01
policy_label: public
related:
  - ./README.md
  - ../README.md
tags: [kfm, quality, docs, checklist]
[/KFM_META_BLOCK_V2] -->

# Documentation Quality Checklist

Use this checklist before merging significant documentation updates.

## Structure and navigation

- [ ] File location is correct for the document type.
- [ ] Title reflects the scope and intent.
- [ ] Quick links / section anchors are present for long documents.
- [ ] References to sibling docs use valid relative links.

## Accuracy and governance alignment

- [ ] Claims align with current implementation or are clearly marked as proposed.
- [ ] Terms are consistent with the KFM glossary and governance language.
- [ ] Normative requirements are unambiguous and testable.
- [ ] Security/policy behavior is described as fail-closed when uncertain.

## Evidence and traceability

- [ ] User-facing claims include resolvable evidence links when required.
- [ ] Required artifacts and validators are explicitly named.
- [ ] Promotion/blocking criteria are documented where applicable.
- [ ] Exception paths include approval and time-bound requirements.

## Readability and maintenance

- [ ] Markdown renders cleanly (lists, tables, code fences).
- [ ] Long sections are broken into digestible subsections.
- [ ] “Back to top” / navigation helpers are present for long docs.
- [ ] Outdated TODOs or stale timestamps are removed or updated.

## Final pre-merge checks

- [ ] Local markdown lint/format checks pass.
- [ ] Link checks pass for changed files.
- [ ] Reviewer can identify what changed and why from the PR description.
