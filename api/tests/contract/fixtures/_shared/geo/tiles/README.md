> According to a document from **2025-12-28**, KFM is **contract-first**, and CI runs **API contract tests** against **known inputs**. This directory provides **deterministic geo tile fixtures** for those tests. 🧪🗺️

# 🗺️ Geo Tiles — Shared Contract Fixtures

`🧪 contract-tests` `🧭 geo` `🧱 xyz-tiles` `📦 fixtures`

---

## 🎯 Purpose

This folder contains **small**, **stable**, **commit-friendly** map tiles used by **API contract tests** to validate tile-serving endpoints (and any supporting metadata endpoints).

Typical uses:
- ✅ Verify raster tile responses (`.png`, `.jpg`)
- ✅ Verify vector tile responses (`.pbf` / MVT)
- ✅ Verify “tile metadata” responses (e.g., TileJSON-style manifests), if your contract exposes them

> 💡 Goal: make geospatial contract tests **repeatable** and **fast** by using **known fixtures**, not live tile services.

---

## 🛰️ Background (why tiles exist in KFM)

KFM serves geospatial layers to the frontend in **web-friendly tiled forms**:
- **Raster imagery** can be hosted as a tile service (WMTS or an XYZ folder) and loaded by web/globe clients using a `.../{z}/{x}/{y}.png` URL template.
- **Vector layers** may be served as efficient **vector tiles** (e.g., MBTiles / `.pbf`) for client-side rendering.
- Time-aware layers can be driven by a **timeline** (changing the layer URL or parameters per time-slice).

This fixtures folder mirrors that reality — but in a **tiny**, test-oriented package. 📦

---

## 🧱 What belongs here

### ✅ Do include
- A **minimal** set of `{z}/{x}/{y}` tiles that your tests actually request
- “Golden” tiles for deterministic comparisons (bytes or stable hashes)
- Optional manifests for tile endpoints that return templates/metadata

### 🚫 Do not include
- Full tile pyramids (statewide / multiyear) — those are **data artifacts**, not test fixtures
- Anything sensitive (PII, restricted locations, protected layers)

---

## 📁 Recommended directory layout

> Adapt this layout to whatever your contract harness expects — the important part is being **explicit and consistent**.

```
📁 api/tests/contract/fixtures/_shared/geo/tiles/
├── 📄 README.md
├── 📁 raster/                       # XYZ raster tiles (PNG/JPEG)
│   └── 📁 <layer-or-dataset>/
│       └── 📁 {z}/{x}/
│           └── 🖼️ {y}.png
├── 📁 vector/                       # XYZ vector tiles (MVT / .pbf)
│   └── 📁 <layer-or-dataset>/
│       └── 📁 {z}/{x}/
│           └── 🧩 {y}.pbf
└── 📁 tilejson/                     # Optional manifests if your API exposes them
    └── 📄 <layer-or-dataset>.tilejson.json
```

---

## 🧭 Tile scheme expectations

| Concept | Expected value |
|---|---|
| Tiling scheme | **XYZ** (“Slippy Map”) |
| Path template | `/{z}/{x}/{y}.<ext>` |
| Origin | `(0,0)` is **upper-left** (northwest) at each zoom |
| Zoom `0` | A single tile covers the entire world |

> ⚠️ If your server/client uses **TMS**, it flips the Y axis compared to XYZ. Contract tests must be explicit about which scheme they validate.

---

## 🌍 Projection & coordinates

Tiles are intended for web map clients, so the “map-facing” output projection is typically **Web Mercator** (EPSG:3857), even if upstream data is stored/managed in WGS84 or other CRSs.

**Rule of thumb:** fixtures should match what the **API returns** and what the **frontend expects**, not necessarily what the raw source used. 🧭

---

## 🕰️ Time-sliced tiles (optional pattern)

If the API contract includes time-dependent tile endpoints, keep it deterministic by encoding time in the fixture path.

Examples (choose the convention your contract defines):

```txt
raster/ndvi/2025-03-01/{z}/{x}/{y}.png
vector/fields/1861/{z}/{x}/{y}.pbf
```

> ✅ Determinism tip: prefer time-in-path over “current time” defaults.

---

## 🧪 How contract tests typically use these fixtures

<details>
<summary><strong>Option A: Serve fixtures as static files (recommended)</strong> 📡</summary>

1. Mount this folder behind a test route (or a small fixture server).
2. Point contract tests at the real endpoint path.
3. Assert the contract:
   - status (`200`, `404`, etc.)
   - `Content-Type`
   - cache headers (if part of your contract)
   - deterministic body (exact bytes or stable digest)

Example API shapes (illustrative):

```txt
GET /api/tiles/raster/<layer>/{z}/{x}/{y}.png
GET /api/tiles/vector/<layer>/{z}/{x}/{y}.pbf
```

</details>

<details>
<summary><strong>Option B: Read expected fixtures directly from disk</strong> ⚡</summary>

If your harness supports it:
- Read expected bytes from this folder
- Compare against the API response body

This is fastest, but you’ll miss “routing/middleware” coverage that Option A exercises.

</details>

---

## ➕ Adding / updating a fixture set

Use this checklist to keep PRs clean and tests stable:

- [ ] Keep it **small**: only tiles your tests actually hit
- [ ] Confirm the endpoint’s **path template** matches the fixture’s `{z}/{x}/{y}` structure
- [ ] Ensure outputs are **deterministic** (avoid embedded timestamps / nondeterministic metadata)
- [ ] If time-dependent, encode the **time slice** in the folder name (or add a manifest)
- [ ] Validate nothing **sensitive** is included (fixtures must be safe to publish)

---

## 🧰 Troubleshooting

- **404 but you “have the file”**  
  → usually a path mismatch: layer name, extension, or `{z}/{x}/{y}` ordering

- **Tile appears flipped or offset**  
  → XYZ vs TMS mismatch (Y-axis inversion)

- **Vector tile renders “empty”**  
  → style/layer-name mismatch, or the contract is validating the wrong layer’s tiles

---

## 📚 Related KFM docs (for context)

- `docs/MASTER_GUIDE_v13.md` (contract-first + CI contract tests + governance gates)
- KFM technical docs (tile service patterns, vector tiles, time slider model)
- Open-source mapping hub design notes (MapLibre, TileJSON/MBTiles conventions)

---

