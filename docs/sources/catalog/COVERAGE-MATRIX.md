<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-coverage-matrix
title: Source catalog coverage matrix
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

# Source catalog coverage matrix

> Family × domain documentation coverage for the source-catalog lane.

**Status:** scaffold (PROPOSED)

Each cell records whether the source-catalog lane documents a family's contribution to a domain: `documented` · `partial` · `not-yet`. **Every cell is `not-yet` in this scaffold PR** — no per-family product pages have been authored in the nested layout.

The domain axis is the set of subdirectories under [`data/catalog/domain/`](../../../data/catalog/domain/) (CONFIRMED 2026-05-20). The family axis is the nine families of `directory-rules.md` §7.3.

## Matrix

| Domain \ Family | usgs | fema | noaa | nrcs | kansas | gbif | inaturalist | census | local_upload |
|---|---|---|---|---|---|---|---|---|---|
| agriculture | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet |
| archaeology | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet |
| atmosphere | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet |
| fauna | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet |
| flora | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet |
| geology | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet |
| habitat | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet |
| hazards | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet |
| hydrology | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet |
| people | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet |
| people-dna-land | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet |
| roads-rail-trade | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet |
| settlement | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet |
| settlements-infrastructure | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet |
| soil | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet | not-yet |

> [!NOTE]
> The domain axis lists every subdirectory present under `data/catalog/domain/` as of 2026-05-20. Some entries (`settlement` vs. `settlements-infrastructure`, `people` vs. `people-dna-land`) may be in-flux naming — confirm the canonical domain taxonomy against `data/catalog/domain/README.md`.

## Related docs
- [`docs/sources/catalog/INDEX.md`](./INDEX.md) — family index.
- [`data/catalog/domain/`](../../../data/catalog/domain/) — domain projections (domain axis source).
- [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) — placement authority.

**Last reviewed:** 2026-05-20
