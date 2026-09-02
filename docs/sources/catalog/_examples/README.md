<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-examples-readme
title: Source catalog examples
type: readme
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

# Source catalog examples

> Illustrative-only example payloads for the source-catalog lane. NOT authoritative.

**Status:** scaffold (PROPOSED)

> [!WARNING]
> Every file in `_examples/` is **illustrative only**. These payloads are minimal hand-written sketches with placeholder digests (`sha256:<placeholder>`) and placeholder identifiers. They are **not** validated against `schemas/contracts/v1/source/` and must never be treated as authoritative or copied into real catalog artifacts.

## Files

| File | Shows |
|---|---|
| [`stac-item-example.json`](./stac-item-example.json) | Minimal STAC 1.1 Item with a `kfm:provenance` block and a `file:checksum` asset. |
| [`dcat-distribution-example.json`](./dcat-distribution-example.json) | Minimal DCAT distribution with `kfm:provenance` and `kfm:care` blocks. |
| [`prov-o-graph-example.json`](./prov-o-graph-example.json) | Minimal PROV-O graph linking a run activity, an evidence entity, and a catalog entity. |

## Conventions
- Each file carries a top-level `_note` field marking it illustrative-only. JSON cannot carry an HTML-comment KFM Meta Block, so `_note` serves as its provenance marker.
- All digests are the literal placeholder `sha256:<placeholder>` — no realistic-looking digests are fabricated.
- All identifiers contain `PLACEHOLDER` or `<placeholder>`.

## Related docs
- [`docs/sources/catalog/PROFILES.md`](../PROFILES.md) — the profiles these examples sketch.
- [`docs/sources/catalog/_template/SOURCE_PRODUCT_TEMPLATE.md`](../_template/SOURCE_PRODUCT_TEMPLATE.md) — references `stac-item-example.json`.
- [`schemas/contracts/v1/source/`](../../../../schemas/contracts/v1/source/) — authoritative machine shapes.

**Last reviewed:** 2026-05-20
