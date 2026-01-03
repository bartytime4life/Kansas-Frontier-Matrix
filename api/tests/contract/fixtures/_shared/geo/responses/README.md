# 🌍 Geo Contract Response Fixtures

![Contract Tests](https://img.shields.io/badge/tests-contract-blue)
![Scope](https://img.shields.io/badge/scope-_shared%2Fgeo%2Fresponses-informational)
![Format](https://img.shields.io/badge/format-GeoJSON%20%2F%20JSON-brightgreen)
![Stability](https://img.shields.io/badge/contract-backwards--compatible-success)
![Policy](https://img.shields.io/badge/data-redaction%20aware-yellow)

📁 **Path:** `api/tests/contract/fixtures/_shared/geo/responses/`

Shared (“golden”) **response-body fixtures** for Geo/GIS endpoints used by **API contract tests**.  
If a contract test needs an expected GeoJSON/JSON output that’s reusable across multiple endpoints or test suites, it belongs here ✅

---

## 🧭 What’s in this folder

These fixtures represent **known-good API response bodies** for geospatial outputs, typically including:

- ✅ GeoJSON `FeatureCollection` / `Feature` responses  
- ✅ Common “empty” cases (e.g., empty feature collections)  
- ✅ Common error shapes **only if** they’re shared across geo endpoints  
- ✅ Canonical metadata wrappers that multiple geo endpoints return

> ⚠️ **This folder is `_shared`**  
> If your fixture is *endpoint-specific* (or tied to a unique query/route), put it in that endpoint’s fixture directory instead of here.

---

## 🚫 What should NOT be here

- ❌ Sensitive / restricted coordinates (see **🔒 Sensitivity & redaction**)  
- ❌ Huge geometries (megabytes of polygon rings) — simplify or use a minimal test geometry  
- ❌ Volatile fields (timestamps, random IDs, request IDs) unless stabilized  
- ❌ Fixtures that only one endpoint/test ever uses (not “shared”)

---

## 🧱 Conventions

### 📄 File extensions

| Type | Use when | Extension |
|---|---|---|
| GeoJSON body | The body is pure GeoJSON | `.geojson` |
| JSON body | The body is JSON (maybe wraps GeoJSON) | `.json` |

### 🏷️ Naming (recommended)

Keep names **kebab-case**, and encode the scenario:

- `featurecollection-empty.geojson`
- `featurecollection-single-point.geojson`
- `featurecollection-multipolygon-minimal.geojson`
- `error-400-invalid-bbox.json`
- `error-404-not-found.json`

If the API has multiple “shapes” for the same endpoint, include the variant:

- `featurecollection-empty__with-metadata.json`
- `featurecollection-empty__bare.geojson`

> 💡 Tip: Prefer adding a **new** fixture for a new variant over mutating an older fixture that other tests rely on.

---

## 🗺️ GeoJSON rules (please follow)

### ✅ Coordinate reference expectations
- Assume GeoJSON coordinates are **WGS84 / EPSG:4326** unless your contract explicitly states otherwise.
- Enforce **(lon, lat)** ordering in coordinates.
- Keep coordinates within valid ranges:
  - longitude: `[-180, 180]`
  - latitude: `[-90, 90]`

### ✅ Geometry sanity
- Use **valid** geometries (closed polygon rings, no self-intersections when avoidable).
- Keep a “minimal but meaningful” geometry:
  - a point
  - a tiny polygon
  - a small linestring  
  rather than production-scale boundaries.

---

## 🧼 Determinism & normalization

Contract fixtures are only useful if they’re stable. When generating or editing fixtures:

- **Sort / stabilize ordering**  
  - stable feature ordering (e.g., by `id`)
  - stable property ordering (or canonical JSON formatting)
- **Freeze volatility**  
  - replace timestamps with fixed values
  - avoid random UUIDs unless seeded and stable
- **Prefer minimal precision**
  - keep float precision consistent (avoid noisy “1.234567890123” unless required by the contract)
- **No environment leakage**
  - no hostnames, temp paths, stack traces, internal IPs, etc.

> 🧩 Contract tests should fail only on **meaningful** contract changes—not on formatting noise.

---

## 🔒 Sensitivity & redaction

Geo fixtures can accidentally leak sensitive locations. Before committing:

- ✅ Use **synthetic** or **generalized** coordinates for any sensitive context  
- ✅ Prefer “toy” geometries that still validate the contract  
- ✅ If a fixture might be sensitive, **don’t store it here** — redesign the test case to avoid sensitive coordinates entirely

If the project uses classification/sensitivity tags, ensure tests and fixtures respect them end-to-end.

---

## ➕ Adding a new shared response fixture

### 1) Start with the contract 📜
- Add/update the API contract (OpenAPI/GraphQL schema) **first**, then fixtures.

### 2) Generate the response deterministically 🧪
- Use a deterministic dataset, deterministic seeds, and fixed clocks where relevant.

### 3) Sanitize + normalize 🧽
- Remove volatility (timestamps/IDs) or freeze it.
- Ensure GeoJSON is WGS84 and valid.

### 4) Validate ✅
- Run the contract tests.
- Ensure the fixture is reusable (i.e., not coupled to one-off behavior).

---

## ✅ Definition of Done (Fixture PR)

- [ ] Fixture is **shared** (used by multiple tests) and belongs in `_shared/`
- [ ] Response body matches the **current API contract**
- [ ] GeoJSON is WGS84, **(lon, lat)**, and geometry is valid
- [ ] No sensitive coordinates or restricted data
- [ ] Output is deterministic (no timestamps/randomness/noise)
- [ ] Contract tests pass locally + in CI

---

## 🧰 Example fixture (minimal GeoJSON)

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": "example-point-001",
      "properties": {
        "name": "Example Point",
        "source": "fixture"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [-96.0, 38.5]
      }
    }
  ]
}
```

---

## 🔗 Related docs & places to look

- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` (contract-first workflow)
- `src/server/contracts/` (canonical API contract home, if present)
- `docs/governance/` (sensitivity, redaction, review gates)
- `api/tests/contract/` (test harness + non-shared fixtures)

---

<details>
<summary>🗂️ Example directory layout (illustrative)</summary>

```text
api/tests/contract/fixtures/_shared/geo/
├─ requests/
│  └─ README.md
└─ responses/
   ├─ README.md  ← you are here
   ├─ featurecollection-empty.geojson
   ├─ featurecollection-single-point.geojson
   └─ error-400-invalid-bbox.json
```

</details>

