<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-changelog
title: Source catalog changelog
type: register
version: v0.1
status: draft
owners: <PLACEHOLDER — Docs steward + Source steward>
created: 2026-05-20
updated: 2026-05-20
policy_label: public
related:
  - docs/sources/catalog/README.md
  - docs/doctrine/directory-rules.md
tags: [kfm, docs, sources, catalog]
notes:
  - "PROPOSED scaffold; sibling-link presence verified in Claude Code session."
[/KFM_META_BLOCK_V2] -->

# Source catalog changelog

> Change history for the `docs/sources/catalog/` documentation lane.

**Status:** scaffold (PROPOSED)

This changelog follows *Keep a Changelog* conventions. Dates are UTC.

## [Unreleased]

- Scaffold initial lane structure — cross-cutting governance docs, templates, and illustrative example payloads — PROPOSED in this PR.
- Reorganize 30 flat per-source pages into 23 per-family folders (9 `directory-rules.md` §7.3 families plus 14 additional families); add `kansas/README.md`; depth-correct relative links in all moved files.
- Known follow-up: 24 pre-existing broken links (authoring bugs predating the reorganization) were preserved unchanged and reported for a separate fix.

## Related docs
- [`docs/sources/catalog/README.md`](./README.md) — lane root.
- [`docs/sources/catalog/INDEX.md`](./INDEX.md) — family index.

**Last reviewed:** 2026-05-20
