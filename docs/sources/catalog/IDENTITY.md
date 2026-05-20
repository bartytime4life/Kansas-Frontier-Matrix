<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-identity
title: Source catalog identity and namespace conventions
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

# Source catalog identity and namespace conventions

> Collection-id, item-id, namespace, and promoteId conventions for KFM source-catalog entries.

**Status:** scaffold (PROPOSED)

## Collection-id pattern
- **PROPOSED pattern:** `kfm-<org>-<product>` — for example `kfm-noaa-storm-events`.
- `<org>` is the source family short code; `<product>` is the product slug in `lowercase-with-hyphens`.
- Whether each product gets its own STAC Collection or shares one with sibling products is unresolved — see [`OPEN-DSC-05`](./OPEN-QUESTIONS.md).

## Item-id determinism
- **PROPOSED:** item ids must be deterministic functions of source identity plus `spec_hash`, so that re-ingest of unchanged input yields the same id.
- The identity grammar for `spec_hash` and `run_id` is fixed by ADR-0013.

## Namespace pin
- The KFM provenance namespace prefix is **UNRESOLVED**: `kfm:` (KFM-global) vs. `ks-kfm:` (Kansas-scoped).
- Tracked as [`OPEN-DSC-03`](./OPEN-QUESTIONS.md). Scaffold pages in this lane use `kfm:` provisionally.

## Per-family promoteId convention
- **NEEDS VERIFICATION:** the `promoteId` convention (the stable per-feature key used by map tiles) per family has not been confirmed against `data/catalog/` artifacts in this session.

## Related docs
- [`docs/sources/catalog/PROFILES.md`](./PROFILES.md) — profile definitions.
- [`docs/sources/catalog/NAMING.md`](./NAMING.md) — path and filename casing.
- [`data/registry/sources/`](../../../data/registry/sources/) — authoritative source descriptors.

**Last reviewed:** 2026-05-20
