<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-naming
title: Source catalog naming conventions
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

# Source catalog naming conventions

> Decision register for path and filename casing within the `docs/sources/catalog/` lane.

**Status:** scaffold (PROPOSED)

This register records the casing conventions for the lane. It **resolves [`OPEN-DSC-07`](./OPEN-QUESTIONS.md) as PROPOSED** — ratification by a per-root note or an ADR is still required.

## Casing decision register

| Path class | Convention | Example |
|---|---|---|
| Family folders | `lowercase_with_underscores` | `local_upload/` |
| Product pages | `lowercase-with-hyphens.md` | `storm-events.md` |
| Lane-root governance docs | `UPPERCASE-WITH-HYPHENS.md` | `RIGHTS-AND-SENSITIVITY-MAP.md` |
| Hidden support folders | underscore prefix | `_template/`, `_examples/` |

## Notes
- The convention above is **locked** for this lane and must not vary page-to-page.
- The existing flat per-family pages at the lane root (`usgs.md`, `fema.md`, and others) predate this register; reconciling them with the family-folder convention is part of [`OPEN-DSC-02`](./OPEN-QUESTIONS.md).
- `OPEN-DSC-07` corresponds to `directory-rules.md` §18 OPEN-DR-04, which covers the same casing question lane-wide.

## Related docs
- [`docs/sources/catalog/IDENTITY.md`](./IDENTITY.md) — id and namespace conventions.
- [`docs/sources/catalog/OPEN-QUESTIONS.md`](./OPEN-QUESTIONS.md) — `OPEN-DSC-07`, `OPEN-DSC-02`.
- [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) — placement authority.

**Last reviewed:** 2026-05-20
