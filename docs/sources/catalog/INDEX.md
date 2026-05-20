<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-index
title: Source catalog lane index
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

# Source catalog lane index

> Navigation index for the nine confirmed source families documented in the `docs/sources/catalog/` lane.

**Status:** scaffold (PROPOSED)

This index covers the nine source families enumerated in [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) §7.3. It is a navigation aid only — the lane root [`README.md`](./README.md) holds the authoritative scope statement, and per-family narrative currently lives in the flat `<family>.md` pages at the lane root.

> [!NOTE]
> The nested per-family folder layout (`<family>/README.md` plus product pages) sketched in [`README.md`](./README.md) §8 is **not yet built**. Whether the lane stays flat or migrates to nested folders is tracked as [`OPEN-DSC-02`](./OPEN-QUESTIONS.md).

## Family index

| Family | Status | Products documented | Last touched |
|---|---|---|---|
| `usgs` | PROPOSED scaffold | flat page `usgs.md`; nested product pages deferred | 2026-05-20 |
| `fema` | PROPOSED scaffold | flat page `fema.md`; nested product pages deferred | 2026-05-20 |
| `noaa` | PROPOSED scaffold | flat page `noaa.md`; nested product pages deferred | 2026-05-20 |
| `nrcs` | PROPOSED scaffold | flat page `nrcs.md`; nested product pages deferred | 2026-05-20 |
| `kansas` | PROPOSED scaffold | flat pages (multiple, e.g. `ksgs.md`, `kansas_memory.md`); nested product pages deferred | 2026-05-20 |
| `gbif` | PROPOSED scaffold | flat page `gbif.md`; nested product pages deferred | 2026-05-20 |
| `inaturalist` | PROPOSED scaffold | flat page `inaturalist.md`; nested product pages deferred | 2026-05-20 |
| `census` | PROPOSED scaffold | flat page `census.md`; nested product pages deferred | 2026-05-20 |
| `local_upload` | PROPOSED scaffold | flat page `local_upload.md`; nested product pages deferred | 2026-05-20 |

Source families beyond these nine are deferred — see [`OPEN-QUESTIONS.md`](./OPEN-QUESTIONS.md) entries `OPEN-DSC-09` through `OPEN-DSC-12`.

## Cross-cutting docs in this lane
- [`GLOSSARY.md`](./GLOSSARY.md) — term definitions.
- [`CROSSWALKS.md`](./CROSSWALKS.md) — cross-format mapping register.
- [`PROFILES.md`](./PROFILES.md) — KFM-STAC / DCAT / PROV profiles.
- [`IDENTITY.md`](./IDENTITY.md) — id and namespace conventions.
- [`NAMING.md`](./NAMING.md) — path and filename casing.
- [`RIGHTS-AND-SENSITIVITY-MAP.md`](./RIGHTS-AND-SENSITIVITY-MAP.md) — per-family rights summary.
- [`CARE-COMPLIANCE.md`](./CARE-COMPLIANCE.md) — CARE governance fields.
- [`COVERAGE-MATRIX.md`](./COVERAGE-MATRIX.md) — family × domain coverage.
- [`OPEN-QUESTIONS.md`](./OPEN-QUESTIONS.md) — `OPEN-DSC-*` register.
- [`CHANGELOG.md`](./CHANGELOG.md) — lane change history.

## Related docs
- [`docs/sources/catalog/README.md`](./README.md) — lane root and authoritative scope.
- [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) — placement authority (§7.3 family list).

**Last reviewed:** 2026-05-20
