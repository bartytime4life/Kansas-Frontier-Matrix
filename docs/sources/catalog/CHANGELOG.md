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
- Fix 13 genuine broken links (the `openstreetmap` footer depth bug and a miscased governance link); 11 deliberate author-labelled PROPOSED forward-references left as-is.
- Scaffold 84 per-product pages across 22 families — one page per dataset documented in each family's README — instantiated from `_template/SOURCE_PRODUCT_TEMPLATE.md`.
- Scaffold 8 connector-derived source families (`nasa`, `usda`, `usdot`, `openaq`, `hifld`, `isric`, `drought_monitor`, `landfire`) with 19 product pages, and add 12 product pages to `kansas`, `usgs`, and `noaa` — descriptions grounded in `docs/domains/*/SOURCE_REGISTRY.md`; tracked as `OPEN-DSC-14`.

## Related docs
- [`docs/sources/catalog/README.md`](./README.md) — lane root.
- [`docs/sources/catalog/INDEX.md`](./INDEX.md) — family index.

**Last reviewed:** 2026-05-20
