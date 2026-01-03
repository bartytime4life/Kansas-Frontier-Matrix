# ✅ Geo Filters — Valid Contract Fixtures 🌍

> **Purpose:** This folder contains **shared, schema-valid** geospatial filter fixtures used by the **API contract tests**.  
> Think of these files as **canonical “known-good” examples** that must keep passing as the API evolves.

---

## 📍 Where you are

```text
📁 api/tests/contract/fixtures/_shared/geo/filters/
└── ✅ valid/
    └── 📄 README.md  ← you are here
```

**Why `_shared/`?**  
These fixtures are intended to be **endpoint-agnostic** and **reused** across multiple contract suites.

---

## 🧪 What “valid” means here

A fixture in this directory MUST:

- ✅ Pass the **contract schema** for geo filters
- ✅ Use **well-formed geometry** (when geometry is involved)
- ✅ Be **deterministic** (no timestamps, randomness, env-dependent content)
- ✅ Be **portable** (works on CI, local, and across DB backends if applicable)
- ✅ Represent **realistic query shapes** (small bbox, polygon, etc.)

> **If you need something to fail validation**, it belongs in the sibling `invalid/` fixtures folder (not here).

---

## 🧩 How these fixtures are typically used

Most contract tests follow the same pattern:

1. Load a fixture from `.../_shared/geo/filters/valid/*.json`
2. Inject it into an API request (query params, JSON body, or filter DSL)
3. Assert the server **accepts** it (2xx) and returns a response matching the contract

### Example integration patterns (illustrative)

<details>
  <summary><strong>📦 JSON body filter payload (common pattern)</strong></summary>

```json
{
  "filters": {
    "geo": {
      "...fixture contents here": true
    }
  }
}
```

</details>

<details>
  <summary><strong>🧵 Query param filter (common pattern)</strong></summary>

```text
GET /search?bbox=-96.90,38.90,-96.80,39.00
```

</details>

> ⚠️ The exact insertion point depends on the endpoint contract.  
> The fixture itself should remain **generic** and **reusable**.

---

## 🌐 Geo fixture rules (keep these consistent)

### 1) Coordinate reference + axis order 🧭

- Use **WGS84 / EPSG:4326**
- Use **[longitude, latitude]** order (GeoJSON convention)

✅ Good: `[-96.85, 39.00]`  
❌ Bad: `[39.00, -96.85]`

---

### 2) Bounding boxes 📦

If a fixture represents a bounding box, keep it unambiguous:

- Format: `[minLon, minLat, maxLon, maxLat]`
- Ensure: `minLon < maxLon` and `minLat < maxLat`
- Keep values in valid ranges:
  - `lon ∈ [-180, 180]`
  - `lat ∈ [-90, 90]`

---

### 3) GeoJSON geometry 🧱

If a fixture uses GeoJSON:

- `type` must be a valid GeoJSON geometry type (`Point`, `Polygon`, `MultiPolygon`, etc.)
- `Polygon` rings must be **closed** (first coordinate == last coordinate)
- Avoid self-intersections unless you’re deliberately testing server-side repair logic
- Keep geometry **small and readable** unless you are explicitly testing complexity limits

---

### 4) “Shared fixture” etiquette 🤝

Because these fixtures are reused:

- ✅ Keep them **minimal** (only the fields needed to represent the geo filter)
- ✅ Keep them **named for intent**, not for endpoint specifics
- ❌ Don’t embed endpoint-only keys, auth context, IDs, or dataset assumptions
- ❌ Don’t rely on “this bbox must return X records” (that’s an integration/data test, not contract)

---

## 🧰 Fixture design checklist

| Check | Rule | Why it matters |
|------:|------|----------------|
| ✅ | Deterministic values | Stable tests across CI + time |
| ✅ | Minimal payload | Easier diffs + fewer breaking changes |
| ✅ | Human-readable coordinates | Faster debugging |
| ✅ | Explicit edge-cases (when needed) | Prevent regressions in geo handling |
| ✅ | No “magic data” assumptions | Contract tests shouldn’t depend on seeded DB contents |

---

## 🗂️ Recommended fixture categories

When expanding coverage, aim to include a few **distinct** shapes:

- 📦 **Small bbox** (tight area)
- 🗺️ **Large bbox** (state-wide / region-wide)
- 📍 **Point** geometry (if supported)
- 🔺 **Simple polygon** (rectangle-ish)
- 🧩 **MultiPolygon** (if supported)
- 🧨 **Edge-case valid** (near bounds, but still valid)

> Tip: Add *edge-case valid* fixtures slowly and intentionally.  
> They’re great for resilience, but can expose backend quirks if DB libraries differ.

---

## 🧾 Example “valid” fixture shapes (templates)

> These are **templates** to guide authorship.  
> Keep actual fixture keys aligned with the contract schema in this repo.

<details>
  <summary><strong>📦 BBOX template</strong></summary>

```json
{
  "bbox": [-96.90, 38.90, -96.80, 39.00]
}
```

</details>

<details>
  <summary><strong>🧱 GeoJSON Polygon template</strong></summary>

```json
{
  "intersects": {
    "type": "Polygon",
    "coordinates": [
      [
        [-96.90, 38.90],
        [-96.80, 38.90],
        [-96.80, 39.00],
        [-96.90, 39.00],
        [-96.90, 38.90]
      ]
    ]
  }
}
```

</details>

---

## ➕ Adding a new fixture (safe workflow)

1. **Copy** the closest existing fixture and modify it (avoid creating from scratch unless needed)
2. Keep the file:
   - ✅ small
   - ✅ readable
   - ✅ intention-revealing
3. Add a short note to this README under “Fixture Index” (below)
4. Run the contract test suite and ensure it passes

---

## 🧾 Fixture Index (keep updated) 📌

> Update this table whenever you add/remove a fixture in this folder.

| Fixture file | Shape | Notes |
|---|---:|---|
| _(add me)_ | 📦 / 🧱 | What behavior does this represent? |

---

## 🧯 Troubleshooting (common geo mistakes)

- **Tests fail schema validation**
  - Check required keys + exact key names
- **Server rejects “valid” GeoJSON**
  - Verify polygon ring closure
  - Verify coordinate order `[lon, lat]`
- **BBox rejected**
  - Ensure `[minLon, minLat, maxLon, maxLat]` ordering and min < max
- **Flaky tests**
  - Remove dependencies on live data or record counts; assert schema + status instead

---

## 🔗 Related folders

- `../invalid/` — intentionally invalid geo filter fixtures ❌  
- `../../` — shared geo fixtures (other categories) 🌍

---

