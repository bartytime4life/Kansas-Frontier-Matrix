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
> As of **2026-05-20** the lane uses a **per-family folder** layout — each source family has its own folder with a `README.md` (see [`README.md`](./README.md) §8). The earlier flat `<family>.md` pages were reorganized into these folders.

## Family index — `directory-rules.md` §7.3 families

| Family | Status | Family page | Product pages |
|---|---|---|---|
| `usgs` | draft | [`usgs/README.md`](./usgs/README.md) | — *(PROPOSED)* |
| `fema` | draft | [`fema/README.md`](./fema/README.md) | — *(PROPOSED)* |
| `noaa` | draft | [`noaa/README.md`](./noaa/README.md) | — *(PROPOSED)* |
| `nrcs` | draft | [`nrcs/README.md`](./nrcs/README.md) | — *(PROPOSED)* |
| `kansas` | draft | [`kansas/README.md`](./kansas/README.md) | 8 — `ksgs`, `kdwp`, `khri`, `kansas-memory`, `kansas-state-archives`, `ksu-research-extension`, `ku-nhm`, `fhsu-sternberg` |
| `gbif` | draft | [`gbif/README.md`](./gbif/README.md) | — *(PROPOSED)* |
| `inaturalist` | draft | [`inaturalist/README.md`](./inaturalist/README.md) | — *(PROPOSED)* |
| `census` | draft | [`census/README.md`](./census/README.md) | — *(PROPOSED)* |
| `local_upload` | draft | [`local_upload/README.md`](./local_upload/README.md) | — *(PROPOSED)* |

## Additional families (beyond §7.3 — pending ADR)

These folders were created by the 2026-05-20 reorganization but are **not** part of `directory-rules.md` §7.3; see `OPEN-DSC-09`–`OPEN-DSC-12` in [`OPEN-QUESTIONS.md`](./OPEN-QUESTIONS.md).

| Family | Family page | Family | Family page |
|---|---|---|---|
| `ahgp` | [`ahgp/README.md`](./ahgp/README.md) | `loc` | [`loc/README.md`](./loc/README.md) |
| `blm` | [`blm/README.md`](./blm/README.md) | `manual_curation` | [`manual_curation/README.md`](./manual_curation/README.md) |
| `ebird` | [`ebird/README.md`](./ebird/README.md) | `natureserve` | [`natureserve/README.md`](./natureserve/README.md) |
| `eddmaps` | [`eddmaps/README.md`](./eddmaps/README.md) | `newspapers` | [`newspapers/README.md`](./newspapers/README.md) |
| `epa` | [`epa/README.md`](./epa/README.md) | `openstreetmap` | [`openstreetmap/README.md`](./openstreetmap/README.md) |
| `familysearch` | [`familysearch/README.md`](./familysearch/README.md) | `usfws_ecos` | [`usfws_ecos/README.md`](./usfws_ecos/README.md) |
| `ftdna` | [`ftdna/README.md`](./ftdna/README.md) | `idigbio` | [`idigbio/README.md`](./idigbio/README.md) |

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
