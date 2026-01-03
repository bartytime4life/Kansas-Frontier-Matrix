---
title: "Fixture — Raster Tileset: <tileset_id>"
path: "api/tests/contract/fixtures/_shared/geo/tiles/raster/<tileset_id>/README.md"
version: "v0.1.0"
last_updated: "2026-01-03"
status: "active"
doc_kind: "Test Fixture"
owner: "KFM API (Geo)"
license: "TBD"
sensitivity: "public"
care_label: "Public"
markdown_protocol_version: "1.0"
---

# 🧩 Raster Tiles Fixture — `<tileset_id>`

![contract-tests](https://img.shields.io/badge/contract-tests-brightgreen)
![fixture](https://img.shields.io/badge/fixture-static%20tiles-blue)
![scheme](https://img.shields.io/badge/scheme-XYZ-informational)
![type](https://img.shields.io/badge/type-raster-orange)
![scope](https://img.shields.io/badge/scope-test%20only-lightgrey)

> ✅ This folder contains a **deterministic raster tile pyramid** used by **API contract tests**.  
> 🧪 It must stay **stable** unless you intentionally update the contract expectations.

---

## 📘 Overview

### Purpose 🎯
Provide a **known-good, offline, reproducible** raster tileset fixture that contract tests can use to validate:
- tile routing + path resolution (`{z}/{x}/{y}`),
- response behavior (200 vs 404),
- `Content-Type` correctness,
- byte-stable output (where applicable),
- regression safety when refactoring tile/geo code paths.

### Scope 🧭

| In Scope ✅ | Out of Scope ❌ |
|---|---|
| Minimal raster tile pyramid for tests | Production-grade basemap hosting |
| Deterministic, versioned test artifacts | Live upstream tile providers |
| Simple metadata documented here | Full styling pipelines / cartography work |

### Audience 👥
- **Primary:** Backend/API engineers maintaining geo tile endpoints & contract tests
- **Secondary:** QA / CI maintainers, platform engineers, geo pipeline contributors

### Definitions 📚
- **`tileset_id`**: The stable identifier for this tileset fixture. It should match whatever the API/test layer uses as the tileset key.
- **XYZ tiles**: “Slippy map” tile addressing with `{z}/{x}/{y}` (origin at top-left for `y`).
- **Tile pyramid**: A set of tiles across zoom levels (`z`) enabling progressive detail.

### Tileset Metadata 🧾 (fill this in)
| Field | Value |
|---|---|
| tileset_id | `<tileset_id>` |
| human_name | `TBD` |
| tile_scheme | `XYZ` |
| projection / CRS | `EPSG:3857` (recommended) / `TBD` |
| format | `png` / `webp` / `TBD` |
| tile_size_px | `256` (recommended) / `TBD` |
| min_zoom | `TBD` |
| max_zoom | `TBD` |
| bounds | `TBD` |
| nodata / background | `TBD` |
| source_artifact | `TBD` |
| generated_by | `TBD` |
| generated_on | `TBD` |
| license | `TBD` |
| attribution | `TBD` |

### Definition of Done ✅
- [ ] Tiles resolve correctly with the expected `{z}/{x}/{y}` paths
- [ ] Contract tests pass with **no network access**
- [ ] This README has **Purpose** + **Directory Layout** (required sections) 🧱
- [ ] Any non-synthetic source has a clear **license + attribution**
- [ ] No sensitive/regulated imagery or locations are included 🔒

---

## 🗂️ Directory Layout

### This folder 📁
`api/tests/contract/fixtures/_shared/geo/tiles/raster/<tileset_id>/`

### Expected contents (convention) 🧱

```text
📁 raster/
└── 📁 <tileset_id>/
    ├── 📄 README.md              # you are here ✅
    └── 📁 <z>/                   # zoom level folders (e.g., 0, 1, 2...)
        └── 📁 <x>/               # x tile index folders
            └── 🖼️ <y>.<ext>      # y tile images (png/webp)
```

> 📝 Note: Some implementations store tiles as `/<z>/<x>/<y>.<ext>` while others may include a prefix path segment.
> This fixture assumes “classic” XYZ folder layout unless your tests explicitly say otherwise.

---

## 🌐 Contract Expectations

These are the typical **contract invariants** this fixture is meant to support:

- ✅ **Deterministic lookup**: given the same `{z,x,y}`, the same bytes are returned.
- ✅ **Happy path**: existing tiles return `200`.
- ✅ **Missing tile**: non-existent tiles return `404` (or the project’s chosen “missing tile” behavior).
- ✅ **Correct headers**:
  - `Content-Type: image/png` for `.png`
  - `Content-Type: image/webp` for `.webp`
- ✅ **No external dependencies**: tests should not require a running tile server outside the test harness.

<details>
  <summary><strong>📌 Tip: Keep fixtures tiny</strong> (click to expand)</summary>

- Prefer **low zoom ranges** (e.g., `z=0..3`) unless a test explicitly needs more.
- Prefer a **small geographic footprint** to keep tile counts low.
- Avoid “heavy” imagery unless specifically required by the endpoint contract.

</details>

---

## 🧪 How Contract Tests Use This Fixture

While the exact wiring may vary, the intended pattern is:

1. Contract tests reference `<tileset_id>` (the tileset key).
2. The test harness maps that key to this folder.
3. Tile requests are resolved against the filesystem layout:
   - `.../<tileset_id>/{z}/{x}/{y}.<ext>`

### Example request shapes (illustrative)
```text
GET /api/geo/tiles/raster/<tileset_id>/<z>/<x>/<y>.png
GET /api/map/<layer>/<date>/<z>/<x>/<y>.png
```

> ⚠️ If your runtime uses **TMS** (flipped `y`) instead of XYZ, document it here and ensure fixtures match the server scheme.

---

## 🛠️ Adding or Updating a Raster Tileset

### Checklist 🧰
- [ ] Pick a **stable** `tileset_id` (avoid renaming once merged)
- [ ] Generate/export tiles into the `{z}/{x}/{y}` folder structure
- [ ] Keep zoom range minimal and deterministic
- [ ] Update the **Tileset Metadata** table in this README
- [ ] Run contract tests and confirm the expected `200/404` behavior
- [ ] Confirm licensing/attribution is safe for repository inclusion

### Guardrails 🚧
- ✅ Prefer **synthetic** or **project-owned** rasters for fixtures.
- ❌ Do not commit tiles derived from providers that prohibit redistribution.
- 🔒 Do not include sensitive or restricted location imagery.

---

## 🔁 Regenerating Tiles (Examples)

> These are **examples**. Use the project’s approved tooling and pin versions when possible to keep outputs reproducible.

<details>
  <summary><strong>🧱 Example: Generate XYZ tiles from a GeoTIFF (GDAL)</strong></summary>

```bash
# Example only — choose zoom range carefully
gdal2tiles.py \
  -z 0-3 \
  -w none \
  -r bilinear \
  source.tif \
  api/tests/contract/fixtures/_shared/geo/tiles/raster/<tileset_id>/
```

</details>

<details>
  <summary><strong>🧪 Example: Quick sanity check of tile presence</strong></summary>

```bash
# list a few tiles to ensure structure exists
find api/tests/contract/fixtures/_shared/geo/tiles/raster/<tileset_id> -maxdepth 4 -type f | head
```

</details>

---

## ✅ Validation Steps

### Local checks 🔍
- Confirm folder layout:
  - `/<tileset_id>/<z>/<x>/<y>.<ext>`
- Confirm at least one “known tile” exists at the zoom levels tests use.
- Confirm missing tiles behave as expected (usually `404`).

### Contract test run 🧪
Run the project’s contract test suite (or the geo/tiles subset) and ensure:
- tiles return expected status codes,
- headers match the format,
- snapshots (if any) match.

---

## 🔒 Governance & Safety Notes

- 🧭 **Principle:** test fixtures should never become a side-channel for sensitive data.
- 📜 **License:** all tiles must be redistributable under the repo’s policy (or replaced with synthetic data).
- 🧼 **Determinism:** if you regenerate tiles, do it via pinned tooling and document the inputs + versions.

---

## 🧾 Changelog

- `v0.1.0` — Initial README scaffold for raster tileset fixtures ✨

