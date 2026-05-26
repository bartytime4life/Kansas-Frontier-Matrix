<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid-pending>
title: Quick Geospatial QC Panel — specification
type: standard
version: v0.1
status: draft
owners: <pipeline-steward>, <domain-steward>  # PROPOSED placeholders; resolve before review
created: 2026-05-20
updated: 2026-05-20
policy_label: public
related:
  - docs/dashboards/README.md
  - docs/dashboards/operational/README.md
  - docs/dashboards/DASHBOARD_CATALOG.md
  - docs/dashboards/operational/COG_ZARR_REPRODUCIBILITY.md
  - docs/standards/GEOPARQUET.md
tags: [kfm, dashboards, operational, geospatial, qc, geometry, crs, topology]
notes:
  - "Source card: KFM-P31-FEAT-0017 (Quick Geospatial QC Panel) — UNCHANGED, active."
  - "Card self-check: UNKNOWN — repository implementation status remains unverified."
  - "This is a SPEC for a dashboard, not the running dashboard."
[/KFM_META_BLOCK_V2] -->

# Quick Geospatial QC Panel · `operational/GEOSPATIAL_QC_PANEL.md`

> Dashboard specification for the **Quick Geospatial QC Panel** (Atlas card
> `KFM-P31-FEAT-0017`). A fast, inspectable surface for geometry, CRS, and topology
> checks on geospatial outputs.

![Authority](https://img.shields.io/badge/authority-PROPOSED-orange)
![Status](https://img.shields.io/badge/status-draft-lightgrey)
![Category](https://img.shields.io/badge/category-operational-blueviolet)
![Source](https://img.shields.io/badge/source-KFM--P31--FEAT--0017-informational)
![Policy label](https://img.shields.io/badge/policy-public-brightgreen)

**Status:** draft · **Owners:** `<pipeline-steward>`, `<domain-steward>` (PROPOSED) · **Last reviewed:** 2026-05-20

---

> [!IMPORTANT]
> This is a *quick* QC panel — a fast first look, not the authoritative validator. A
> green QC panel does not admit data; the full `ValidationReport` does. The panel exists
> to catch obvious geometry/CRS/topology defects early.

---

## 1. Description

The Quick Geospatial QC Panel answers: **does this geospatial output look structurally
sane at a glance?** It surfaces fast checks — geometry validity, CRS correctness,
topology consistency, bounds plausibility — so a pipeline or domain steward can spot a
broken layer in seconds instead of waiting for a full validation pass.

## 2. Checks surfaced (PROPOSED)

| # | Check | Measures | Healthy posture (PROPOSED) | Negative state |
|---|---|---|---|---|
| 1 | Geometry validity | % of features with valid (OGC-simple) geometry. | 100%. | `GEOMETRY_INVALID` |
| 2 | CRS correctness | Declared CRS present and matches the expected projection. | Matches expected CRS. | `CRS_MISMATCH` |
| 3 | Topology consistency | Self-intersections, gaps, overlaps where not permitted. | None where not permitted. | `TOPOLOGY_ERROR` |
| 4 | Bounds plausibility | Geometry bounds fall within the expected extent (e.g., Kansas). | Within expected extent. | `BOUNDS_OUT_OF_RANGE` |
| 5 | Attribute completeness | Required attribute fields populated. | Required fields non-null. | `ATTRIBUTE_MISSING` |

## 3. Panels (PROPOSED)

- **Geometry validity** — pass rate + count of invalid features, with drill-down.
- **CRS** — declared vs. expected CRS, mismatches flagged.
- **Topology** — self-intersection / gap / overlap counts.
- **Bounds** — a small map thumbnail of the bounding box against the expected extent.
- **Attributes** — required-field completeness per layer.

## 4. Inputs

Mounted-repo paths NEEDS VERIFICATION.

- Geospatial outputs — vector/raster layers from the pipeline (`pipelines/`).
- `ValidationReport` — geometry/CRS/topology check outcomes, where already computed.
- Expected-extent metadata — per-domain bounding extents.
- Layer schemas — required attribute fields.

## 5. Files

| Path | Role | spec_hash |
|---|---|---|
| `docs/dashboards/operational/GEOSPATIAL_QC_PANEL.md` | This dashboard specification. | PROPOSED — pending JCS+SHA-256 |
| Running surface (PROPOSED) | `apps/review-console/` QC panel. | NEEDS VERIFICATION |

## 6. Ownership and review burden

- **Owning stewards (PROPOSED):** Pipeline steward (check plumbing), Domain steward
  (expected extent and attribute expectations for the layer's domain).
- **Review burden:** docs steward + the owning stewards. Resolve placeholders against
  Atlas v1.1 §24.7 before review.

## 7. Acceptance

- [ ] All five checks present; the panel is positioned as a *quick* look, not the validator.
- [ ] Owners named (no anonymous spec at v1).
- [ ] Link check passes; row present in [`DASHBOARD_CATALOG.md`](../DASHBOARD_CATALOG.md).
- [ ] Negative states use the Unified Doctrine §19 vocabulary.

## 8. Open questions

- [ ] **GQC-OQ-01** — Confirm the running surface and downgrade if unverified.
- [ ] **GQC-OQ-02** — Confirm the per-domain expected-extent source.
- [ ] **GQC-OQ-03** — Confirm `KFM-P31-FEAT-0017` implementation status against
      mounted-repo state (card self-check: UNKNOWN).

---

**Related docs:** [operational/README.md](README.md) · [dashboards/README.md](../README.md) · [DASHBOARD_CATALOG.md](../DASHBOARD_CATALOG.md) ·
[operational/COG_ZARR_REPRODUCIBILITY.md](COG_ZARR_REPRODUCIBILITY.md) ·
[standards/GEOPARQUET.md](../../standards/GEOPARQUET.md)

**Last updated:** 2026-05-20 · **Edition:** v0.1 (draft) · **Owners:** `<pipeline-steward>`, `<domain-steward>` (PROPOSED)
