<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid-pending>
title: COG / Zarr Reproducibility Dashboard — specification
type: standard
version: v0.1
status: draft
owners: <pipeline-steward>  # PROPOSED placeholder; resolve before review
created: 2026-05-20
updated: 2026-05-20
policy_label: public
related:
  - docs/dashboards/README.md
  - docs/dashboards/operational/README.md
  - docs/dashboards/DASHBOARD_CATALOG.md
  - docs/standards/COG.md
  - docs/standards/GEOPARQUET.md
tags: [kfm, dashboards, operational, cog, zarr, raster, datacube, reproducibility]
notes:
  - "Source card: KFM-P31-FEAT-0016 (COG/Zarr Reproducibility Dashboard) — UNCHANGED, active."
  - "Card self-check: UNKNOWN — repository implementation status remains unverified."
  - "This is a SPEC for a dashboard, not the running dashboard."
[/KFM_META_BLOCK_V2] -->

# COG / Zarr Reproducibility Dashboard · `operational/COG_ZARR_REPRODUCIBILITY.md`

> Dashboard specification for the **COG / Zarr Reproducibility Dashboard** (Atlas card
> `KFM-P31-FEAT-0016`). Tracks whether raster and datacube artifacts can be rebuilt
> bit-identically: build container, tool versions, chained hashes, layout, verdict.

![Authority](https://img.shields.io/badge/authority-PROPOSED-orange)
![Status](https://img.shields.io/badge/status-draft-lightgrey)
![Category](https://img.shields.io/badge/category-operational-blueviolet)
![Source](https://img.shields.io/badge/source-KFM--P31--FEAT--0016-informational)
![Policy label](https://img.shields.io/badge/policy-public-brightgreen)

**Status:** draft · **Owners:** `<pipeline-steward>` (PROPOSED) · **Last reviewed:** 2026-05-20

---

> [!IMPORTANT]
> Reproducibility is a property of the *artifact build*, not of the dashboard. The
> verdict shown here is derived from chained hashes and recorded build inputs — the
> `RunReceipt` / build record is the proof.

---

## 1. Description

The COG / Zarr Reproducibility dashboard answers: **can each raster (COG) or datacube
(Zarr) artifact be rebuilt and produce a bit-identical result?** It surfaces the build
environment and a reproducibility verdict per artifact so the pipeline steward can catch
non-determinism (a GDAL upgrade, a numcodecs change, an unpinned container) before it
silently changes published data.

## 2. Metrics surfaced (PROPOSED)

| # | Metric | Measures | Healthy posture (PROPOSED) | Negative state |
|---|---|---|---|---|
| 1 | Build container identity | Whether the artifact records the exact build container digest. | Pinned digest recorded. | `BUILD_ENV_UNPINNED` |
| 2 | Tool versions | GDAL / numcodecs / driver versions used in the build. | Recorded and pinned. | `TOOL_VERSION_DRIFT` |
| 3 | Chained hashes | Input → intermediate → output hash chain integrity. | Chain verifies end to end. | `HASH_CHAIN_BROKEN` |
| 4 | Overview / block layout | Whether overviews and block/chunk layout match the standard. | Matches `COG.md` / Zarr profile. | `LAYOUT_NONCONFORMANT` |
| 5 | Reproducibility verdict | Rebuild produces a bit-identical artifact. | `REPRODUCIBLE`. | `NOT_REPRODUCIBLE` |

## 3. Panels (PROPOSED)

- **Build environment** — per-artifact container digest + tool versions; drift flagged.
- **Hash chain** — input/intermediate/output hash chain with a verify status.
- **Layout conformance** — overview levels and block/chunk layout vs. the standard.
- **Verdict board** — `REPRODUCIBLE` / `NOT_REPRODUCIBLE` per artifact, with cause.

## 4. Inputs

Mounted-repo paths NEEDS VERIFICATION.

- `RunReceipt` / build records — container digest, tool versions, input hashes.
- Artifact metadata — COG overview/block layout, Zarr chunk layout.
- Chained-hash manifests — input → intermediate → output integrity.
- Standards: [`COG.md`](../../standards/COG.md), Zarr/datacube profile.

## 5. Files

| Path | Role | spec_hash |
|---|---|---|
| `docs/dashboards/operational/COG_ZARR_REPRODUCIBILITY.md` | This dashboard specification. | PROPOSED — pending JCS+SHA-256 |
| Running surface (PROPOSED) | `apps/review-console/` reproducibility panel. | NEEDS VERIFICATION |

## 6. Ownership and review burden

- **Owning steward (PROPOSED):** Pipeline steward.
- **Review burden:** docs steward + pipeline steward. Resolve the placeholder against
  Atlas v1.1 §24.7 before review.

## 7. Acceptance

- [ ] All five metrics present; the verdict is derived from chained hashes, not asserted.
- [ ] Owner named (no anonymous spec at v1).
- [ ] Link check passes; row present in [`DASHBOARD_CATALOG.md`](../DASHBOARD_CATALOG.md).
- [ ] Negative states use the Unified Doctrine §19 vocabulary.

## 8. Open questions

- [ ] **CZR-OQ-01** — Confirm the running surface and downgrade if unverified.
- [ ] **CZR-OQ-02** — Confirm the canonical Zarr/datacube layout profile to check against.
- [ ] **CZR-OQ-03** — Confirm `KFM-P31-FEAT-0016` implementation status against
      mounted-repo state (card self-check: UNKNOWN).

---

**Related docs:** [operational/README.md](README.md) · [dashboards/README.md](../README.md) · [DASHBOARD_CATALOG.md](../DASHBOARD_CATALOG.md) ·
[standards/COG.md](../../standards/COG.md) · [standards/GEOPARQUET.md](../../standards/GEOPARQUET.md)

**Last updated:** 2026-05-20 · **Edition:** v0.1 (draft) · **Owners:** `<pipeline-steward>` (PROPOSED)
