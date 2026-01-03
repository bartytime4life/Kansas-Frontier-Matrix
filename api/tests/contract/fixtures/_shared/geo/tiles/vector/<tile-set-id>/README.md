# 🧱 Vector Tile Fixture — `<tile-set-id>` 🗺️

![fixture](https://img.shields.io/badge/fixture-vector_tiles-0a58ca)
![tests](https://img.shields.io/badge/used_by-contract_tests-6f42c1)
![format](https://img.shields.io/badge/format-MVT_(PBF)-1f883d)

> **TL;DR:** This folder is a **golden fixture** for the vector-tile tile-set **`<tile-set-id>`**.  
> Contract tests load these files and assert the API returns the **same bytes + headers** (as defined by the API contract).

---

## 📍 Where am I?

`api/tests/contract/fixtures/_shared/geo/tiles/vector/<tile-set-id>/`

This is the per-tile-set fixture directory under the shared Geo fixtures tree.

---

## 🎯 What this fixture is for

Vector tiles power interactive maps (fast pan/zoom + styled layers). This fixture exists so our **API contract tests** can validate that:

- ✅ the tile endpoint(s) for **`<tile-set-id>`** remain backward-compatible  
- ✅ response headers (content-type, caching, encoding) stay correct  
- ✅ the returned tile bytes remain deterministic for known `z/x/y` inputs  
- ✅ “missing tile” behavior is stable (404 vs 204 vs empty tile) *per contract*

---

## 🧾 Fixture metadata (fill this in)

| Field | Value |
|---|---|
| Tile-set id | `<tile-set-id>` |
| Human name | `<e.g., "Kansas Counties (simplified)">` |
| Geometry type(s) | `<Point / LineString / Polygon / Mixed>` |
| Layer names (MVT layers) | `<layer_1>, <layer_2>, ...` |
| Zoom range | `<minZoom>–<maxZoom>` |
| Tile scheme | `z/x/y` (Web Mercator) |
| Encoding on disk | `<raw .pbf/.mvt OR gzipped bytes>` |
| Expected `Content-Type` | `<e.g., application/vnd.mapbox-vector-tile>` |
| Expected `Content-Encoding` | `<e.g., gzip OR (none)>` |
| Source dataset | `<STAC/DCAT/PROV ref OR pipeline output ref>` |
| Generation method | `<pipeline script / command / job name>` |
| Generated at | `<YYYY-MM-DD>` |
| Notes | `<anything a maintainer needs to know>` |

---

## 📦 Expected contents

This folder should contain **only what contract tests need** to prove the API behavior for this tile-set.

Typical contents (yours may vary based on the harness):

```text
📦 <tile-set-id>/
├─ 📄 README.md              👈 you are here
├─ 📄 manifest.json          (optional) human/test harness metadata
└─ 🧩 tiles/
   └─ 🧭 {z}/
      └─ 🧭 {x}/
         └─ 🧊 {y}.pbf       (or .mvt, or .pbf.gz if you store wire-bytes gzipped)
```

### ✅ What belongs here
- A **small**, representative sample of tiles (enough to test styling, layer presence, feature counts, edge cases)
- Optional manifest/notes that help explain provenance and generation
- Optional “expected headers” file *if your contract harness supports it* (ex: `expected.headers.json`)

### 🚫 What does NOT belong here
- Huge tile pyramids (keep fixtures lightweight)
- Unlicensed or unclear-provenance data
- Anything that introduces non-determinism (timestamps, random IDs, unstable ordering) into the encoded output

---

## 🔌 How contract tests usually consume this (conceptual)

Contract tests typically do some variation of:

1. 🧭 Select a known request tuple: `(tileSetId, z, x, y)`
2. 📦 Load the corresponding fixture bytes from `tiles/{z}/{x}/{y}.*`
3. 🌐 Call the API endpoint under test
4. 🧾 Assert:
   - HTTP status code matches contract
   - `Content-Type` matches contract
   - `Content-Encoding` (if any) matches contract
   - body bytes match fixture bytes (**exact match**) or match a deterministic transform (**explicitly defined**)

> If you’re unsure where the route is defined: search the API contract definitions for **`<tile-set-id>`**.

---

## 🛠️ Adding or updating tiles (checklist)

### 1) Decide what you’re changing ✅
- 🧩 **Tiles changed** because dataset changed
- 🧪 **Tiles changed** because the encoder/tiler changed
- 🔌 **Contract changed** (headers/status/routing)

If the **contract** changes, make sure you’re also updating the contract definition and any versioning expectations (don’t “silently” break clients).

### 2) Keep fixtures minimal 🎒
- Prefer **a few tiles** across relevant zooms
- Include at least one tile that:
  - contains *multiple* features
  - exercises *every* intended layer
  - covers a boundary/edge case if relevant (tile border crossing, simplified geometry, etc.)

### 3) Preserve determinism 🧊
To avoid flaky contract tests:
- Use stable feature IDs (don’t rely on random IDs)
- Use stable attribute ordering where possible
- Keep a single canonical generation path (don’t regenerate with different tooling “just because”)

### 4) Validate locally 🧪
- Run the contract tests that reference this tile-set
- Confirm the API responses match your expected bytes/headers

---

## 🧯 Troubleshooting

### “My tile bytes don’t match, but visually it’s the same”
That’s common—vector tiles are binary and can change due to:
- different encoder versions
- different geometry simplification tolerances
- different feature ordering / IDs
- gzip on/off (wire bytes differ)

**Fix:** update the metadata above (generation method/tooling), and ensure the contract test expectation matches the contract (wire-bytes vs decoded equivalence).

### “Why not compare decoded features instead of bytes?”
Byte-for-byte fixtures are **stricter** and catch breaking changes earlier.  
If you want decoded comparisons, it must be an explicit contract decision (and usually requires a canonical decoding + normalization step).

---

## 🔗 Related (project) docs & concepts

- 📘 `/docs/MASTER_GUIDE_v13.md` — contract-first + determinism philosophy  
- 🧪 Contract tests — ensure API changes are compatible and deliberate  
- 🗺️ Map UI stack — vector tiles are foundational for interactive mapping

---

## ✅ Maintainer TODO (when creating a new tile-set fixture)

- [ ] Fill out the **Fixture metadata** table
- [ ] Add / update tiles in `tiles/{z}/{x}/{y}.*`
- [ ] Confirm contract tests pass for `<tile-set-id>`
- [ ] Ensure provenance/licensing is documented (even if briefly)

