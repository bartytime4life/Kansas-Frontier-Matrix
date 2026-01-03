<!--
📍 Path: api/tests/contract/fixtures/_shared/geo/geojson/README.md
-->

# 🌍 Shared GeoJSON Fixtures (API Contract Tests)

![GeoJSON](https://img.shields.io/badge/format-GeoJSON-2ea44f)
![Contract Tests](https://img.shields.io/badge/tests-contract-0ea5e9)
![CRS](https://img.shields.io/badge/CRS-EPSG%3A4326%20(WGS84)-7c3aed)
![Safety](https://img.shields.io/badge/fixtures-no%20PII%20%2F%20no%20secrets-orange)

These files are the **canonical, reusable GeoJSON payloads** used across **KFM API contract tests** to keep geospatial request/response shapes consistent, deterministic, and backwards-compatible. ✅

> 📌 **Rule of thumb:** if a contract test needs GeoJSON, **use a fixture from here** (or add one here) instead of embedding large inline JSON in a test file.

---

## 🗂️ Where this folder sits

```text
📁 api/                                   🧩 Backend workspace (API + tests)
└─ 📁 tests/                               🧪 Automated test suite root
   └─ 📁 contract/                          📜 Contract/spec conformance tests
      └─ 📁 fixtures/                       📦 Test inputs + expected outputs (snapshots)
         └─ 📁 _shared/                     ♻️ Reusable fixtures shared across many cases
            └─ 📁 geo/                      🗺️ Geospatial shared fixtures (multiple formats)
               └─ 📁 geojson/               🌍 GeoJSON fixtures (canonical shapes + edge cases)
                  ├─ 📄 README.md           📘 Rules, conventions, and usage for this folder
                  └─ 📄 *.geojson           🧱 Shared GeoJSON samples (Feature / FeatureCollection)
```

---

## 🎯 What belongs in this folder

### ✅ Valid fixtures
Small, realistic GeoJSON objects representing shapes the API commonly **accepts** or **returns**, typically:
- `Feature` (single object)
- `FeatureCollection` (multiple objects)

Examples of “good” fixtures:
- a simple point feature (geocode / marker)
- a linestring route (routing / path)
- a polygon AOI (area of interest / boundary)
- multi-geometries + holes (edge cases)

### 🧨 Negative/invalid fixtures (optional but encouraged)
When you want contract tests to ensure **we reject bad GeoJSON** with good error messages.

**Convention suggestion (pick one and be consistent):**
- prefix with `invalid__...geojson`, or
- put them in an `invalid/` subfolder

---

## 🧭 Principles this folder supports

- **Contract-first** 🧾: fixtures represent stable “known inputs/outputs” that help lock down the API boundary.
- **Deterministic** 🔁: fixtures must not depend on randomness, timestamps, or environment.
- **Minimal but representative** 🎛️: keep data small, but include the required fields and realistic structure.

---

## ✅ GeoJSON fixture rules for KFM

### 1) CRS + coordinate order (non-negotiable)
- **CRS:** EPSG:4326 (WGS84)
- **Coordinate order:** `[longitude, latitude]` (optional third value: `altitude`)

> ⚠️ Common footgun: exporting EPSG:3857 (Web Mercator) coordinates into `.geojson` and then wondering why it looks “shifted” in viewers/tests. Only do this if the fixture is **explicitly intended** to be invalid/compat-coverage.

### 2) Keep fixtures small & stable
- Prefer small geometries (a few vertices) unless the test is explicitly about large payload handling.
- Round floats to a consistent precision (suggestion: **≤ 6 decimal places**) to avoid noisy diffs.
- Avoid ordering churn:
  - keep feature ordering stable in a `FeatureCollection`
  - keep `properties` keys stable where possible

### 3) Properties should be “contract-relevant”
`properties` should be:
- ✅ **minimal**
- ✅ **stable**
- ✅ **representative** of what the API expects/returns (required keys present)
- 🚫 not full production dumps with extra noise

### 4) Don’t embed sensitive content
Fixtures live in git history forever and will be processed by CI and tooling.
- 🚫 No secrets (keys/tokens)
- 🚫 No personal data
- ⚠️ Avoid precise sensitive/protected locations — use generalized geometry

---

## 🧪 How to use these fixtures in tests

<details>
<summary><strong>Node / TypeScript</strong> (read fixture from repo path)</summary>

```ts
import fs from "node:fs";
import path from "node:path";

const fixturePath = path.resolve(
  process.cwd(),
  "api/tests/contract/fixtures/_shared/geo/geojson/__fixture__.geojson"
);

const geojson = JSON.parse(fs.readFileSync(fixturePath, "utf8"));

// Example assertions (adjust to your contract expectations)
expect(geojson.type).toMatch(/^(Feature|FeatureCollection)$/);
```
</details>

<details>
<summary><strong>Python</strong> (read fixture from repo path)</summary>

```py
import json
from pathlib import Path

fixture_path = Path.cwd() / "api/tests/contract/fixtures/_shared/geo/geojson/__fixture__.geojson"
geojson = json.loads(fixture_path.read_text(encoding="utf-8"))

assert geojson["type"] in {"Feature", "FeatureCollection"}
```
</details>

---

## 🧰 Creating a new fixture (recommended workflow)

1. **Start from real output** (or a realistic sample aligned with the API contract).
2. **Transform to EPSG:4326** *before* exporting GeoJSON.
3. **Minimize**: keep only what the contract test needs.
4. **Add or update a contract test** to use the fixture.
5. **Register it in the catalog table** below (so others can find/reuse it).

<details>
<summary><strong>Example: PostGIS → GeoJSON geometry (EPSG:4326)</strong></summary>

```sql
-- NOTE: ST_AsGeoJSON returns geometry only; wrap into Feature/FeatureCollection in your app/test helper if needed.
SELECT ST_AsGeoJSON(ST_Transform(geom, 4326)) AS geom_geojson
FROM your_table
WHERE id = :id;
```
</details>

---

## 📚 Fixture catalog (keep this updated ✍️)

> Add one row per fixture so future tests can reuse existing files instead of duplicating GeoJSON.

| File | GeoJSON type | Used by | Notes |
|---|---|---|---|
| `__fixture__.geojson` | `Feature` / `FeatureCollection` | `…` | Replace this placeholder with real fixtures |
| `…` | `…` | `…` | `…` |

---

## 🔍 Quick validation checklist

- [ ] Valid JSON (parses cleanly)
- [ ] Valid GeoJSON `type`
- [ ] WGS84-looking coordinate bounds (roughly `lon: -180..180`, `lat: -90..90`)
- [ ] Polygon rings are closed (first coordinate == last coordinate)
- [ ] No secrets / PII / sensitive coordinates included
- [ ] If this fixture is an edge case: the test name explains **why it exists** ✅

<details>
<summary><strong>Optional: tiny “bounds sanity” snippet (Python)</strong></summary>

```py
def looks_like_wgs84(lon: float, lat: float) -> bool:
    return -180.0 <= lon <= 180.0 and -90.0 <= lat <= 90.0
```
</details>

---

## 🔄 Changing an existing fixture (⚠️ treat as a contract change)

If you modify a fixture, you are effectively changing a **contract example**.

✅ Prefer:
- add a new fixture + update tests

🚫 Avoid:
- rewriting an existing fixture “just because” (unless the contract changed intentionally and the versioning story is clear)

---

## ❓FAQ

<details>
<summary><strong>Why does my GeoJSON look “wrong” in QGIS / viewers?</strong></summary>

Most often: you exported in EPSG:3857 but the viewer assumed EPSG:4326. Re-export in EPSG:4326 and try again.
</details>

