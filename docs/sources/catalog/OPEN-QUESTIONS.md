<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-open-questions
title: Source catalog open questions
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

# Source catalog open questions

> Numbered register of unresolved questions (`OPEN-DSC-*`) for the source-catalog documentation lane.

**Status:** scaffold (PROPOSED)

Entries `OPEN-DSC-01` through `OPEN-DSC-08` are carried forward from [`README.md`](./README.md) §19. Entries `OPEN-DSC-09` through `OPEN-DSC-14` and `OPEN-DSC-NEW` are added by the scaffold, the 2026-05-20 reorganization, and the 2026-05-21 connector-derived family scaffold.

## Register

### OPEN-DSC-01 — lane existence
**Question:** Should `docs/sources/catalog/` exist as a docs subfolder, or should source-catalog narrative live in `docs/sources/<family>/` directly with no intermediate `catalog/` segment?
**Status:** PROPOSED.
**Resolution path:** per-root note in `docs/sources/README.md`, or ADR.

### OPEN-DSC-02 — per-family page layout
**Question:** Does the per-family page list live in this lane or in `docs/sources/README.md` as a flat index? The flat-vs-nested split observed earlier (flat `<family>.md` pages vs. `README.md` §8's nested folders) has been acted on.
**Status:** PARTIALLY RESOLVED — on 2026-05-20 the lane was reorganized into per-family folders (maintainer decision), implementing `README.md` §8. An ADR should still ratify the realized folder layout and settle the `docs/sources/README.md`-index vs. lane-index question.
**Resolution path:** ADR ratifying the realized folder layout.

### OPEN-DSC-03 — provenance namespace
**Question:** Is the KFM provenance namespace `kfm:` (KFM-global) or `ks-kfm:` (Kansas-scoped)? (Pass-10 C4-01.)
**Status:** UNKNOWN.
**Resolution path:** ADR pinning the namespace.

### OPEN-DSC-04 — promotion-state summary field
**Question:** Should STAC Collections carry a `kfm:promotion_state` summary field? (Pass-10 C4-02.)
**Status:** PROPOSED.
**Resolution path:** ADR, plus schema change in `schemas/contracts/v1/source/`.

### OPEN-DSC-05 — STAC vs DCAT disposition
**Question:** Canonical disposition between STAC and DCAT for spatiotemporal datasets that could go either way (Pass-10 C4-05). Related: does each product warrant its own STAC Collection or share one with sibling products?
**Status:** NEEDS VERIFICATION.
**Resolution path:** profile decision in [`PROFILES.md`](./PROFILES.md), plus verification against `data/catalog/`.

### OPEN-DSC-06 — kfm:care registry home
**Question:** Should `kfm:care` be proposed upstream to the STAC-extensions registry or kept KFM-local (Pass-10 C15-02)? Related: the canonical home for authored crosswalks — this lane vs. `docs/standards/`.
**Status:** UNKNOWN.
**Resolution path:** ADR.

### OPEN-DSC-07 — filename casing
**Question:** Filename casing for per-family pages — hyphens vs. underscores. See `directory-rules.md` §18 OPEN-DR-04.
**Status:** PROPOSED — resolved provisionally in [`NAMING.md`](./NAMING.md).
**Resolution path:** per-root note or ADR ratifying `NAMING.md`.

### OPEN-DSC-08 — repository implementation maturity
**Question:** Repository implementation maturity for everything described in this lane.
**Status:** PARTIALLY RESOLVED — a mounted repo was inspected in a Claude Code session on 2026-05-20; all sibling roots checked in §7.3 scope (connectors, data/catalog, data/registry/sources, schemas, policy, contracts, pipelines, docs/adr) were CONFIRMED-PRESENT. Per-product implementation maturity remains NEEDS VERIFICATION.
**Resolution path:** ongoing verification as products materialize.

### OPEN-DSC-09 — candidate families: federal agencies
**Question:** Should NASA, USDA, EPA, DOT, and BLM be promoted to `directory-rules.md` §7.3 families with full connector and registry treatment?
**Status:** DEFERRED — folders `blm/` and `epa/` were created in the 2026-05-20 reorganization ahead of ADR; folder existence does **not** constitute §7.3 promotion.
**Resolution path:** ADR per family, gated on a `connectors/<family>/` plus `data/registry/sources/<family>/` companion.

### OPEN-DSC-10 — candidate families: archival and genealogy
**Question:** Should the Library of Congress (LOC), FamilySearch, AHGP, and Newspapers be promoted to §7.3 families?
**Status:** DEFERRED — folders `loc/`, `familysearch/`, `ahgp/`, `newspapers/` were created in the 2026-05-20 reorganization ahead of ADR; folder existence does **not** constitute §7.3 promotion.
**Resolution path:** ADR per family; genealogy and archival sources additionally gated on CARE and sensitivity review.

### OPEN-DSC-11 — candidate families: citizen-science and sensors
**Question:** Should PurpleAir, eBird, and EDDMapS be promoted to §7.3 families?
**Status:** DEFERRED — folders `ebird/` and `eddmaps/` were created in the 2026-05-20 reorganization ahead of ADR; folder existence does **not** constitute §7.3 promotion.
**Resolution path:** ADR per family; eBird and EDDMapS additionally gated on sensitive-species redaction policy.

### OPEN-DSC-12 — candidate families: biodiversity collections and genomic
**Question:** Should iDigBio/Symbiota, NatureServe/USFWS, and direct-to-consumer (DTC) genomic sources be promoted to §7.3 families?
**Status:** DEFERRED — folders `idigbio/`, `natureserve/`, `usfws_ecos/`, `ftdna/` were created in the 2026-05-20 reorganization ahead of ADR; folder existence does **not** constitute §7.3 promotion.
**Resolution path:** ADR per family; genomic and rare-species sources gated deny-by-default per ADR-0010.

### OPEN-DSC-13 — folders without a clear family classification
**Question:** `openstreetmap/` and `manual_curation/` received folders in the 2026-05-20 reorganization but do not map cleanly to a source family — OpenStreetMap is a base-map source and Manual Curation describes a process rather than a source.
**Status:** OPEN — flagged by the 2026-05-20 reorganization.
**Resolution path:** maintainer decision, then ADR, relocation, or reclassification.

### OPEN-DSC-14 — connector-derived families (second wave)
**Question:** Should NASA, USDA, USDOT, OpenAQ, HIFLD, ISRIC, the U.S. Drought Monitor, and LANDFIRE be promoted to `directory-rules.md` §7.3 families?
**Status:** DEFERRED — folders `nasa/`, `usda/`, `usdot/`, `openaq/`, `hifld/`, `isric/`, `drought_monitor/`, `landfire/` were scaffolded on 2026-05-21 from the `connectors/` inventory ahead of ADR; folder existence does **not** constitute §7.3 promotion. Product descriptions are grounded in `docs/domains/*/SOURCE_REGISTRY.md` because the connector folders are empty stubs.
**Resolution path:** ADR per family, gated on a populated `connectors/<family>/` plus `data/registry/sources/<family>/` companion.

### OPEN-DSC-NEW — §15 README-contract field-order deviation
**Question:** The `_template/SOURCE_FAMILY_TEMPLATE.md` scaffold inserts a `## Directory tree` section between `## Outputs` and `## Validation`, deviating from the §15 README-contract field order in `directory-rules.md`.
**Status:** PROPOSED — flagged by this scaffold PR.
**Resolution path:** ADR to either (a) ratify the deviation lane-wide, or (b) relocate the directory-tree section to the lane-root `INDEX.md`.

## Related docs
- [`docs/sources/catalog/README.md`](./README.md) — lane root (§19 origin of `OPEN-DSC-01` through `OPEN-DSC-08`).
- [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) — placement authority, §18 OPEN-DR-04.

**Last reviewed:** 2026-05-20
