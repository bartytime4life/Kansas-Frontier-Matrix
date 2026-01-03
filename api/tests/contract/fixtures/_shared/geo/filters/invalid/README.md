# 🚫 Invalid Geo Filter Fixtures

![contract-tests](https://img.shields.io/badge/tests-contract-1f6feb?style=flat-square)
![geo-filters](https://img.shields.io/badge/geo-filters-0b7285?style=flat-square)
![negative-cases](https://img.shields.io/badge/fixtures-invalid-dc2626?style=flat-square)
![shared](https://img.shields.io/badge/scope-_shared-6b7280?style=flat-square)

> **Purpose:** shared **negative** fixtures for geospatial filter inputs (🗺️➡️🚫).  
> These are consumed by **API contract tests** to guarantee the API rejects malformed/unsafe geo filters **deterministically** and with a **stable error shape**.

---

## 📍 You are here

```
api/tests/contract/fixtures/_shared/geo/filters/invalid/
```

These fixtures are:

- **`_shared`** ✅ reusable across endpoints (endpoint-agnostic)
- **`geo/filters`** ✅ only about *input validation* / *contract enforcement* for spatial filters
- **`invalid`** ✅ must be rejected by the API contract (usually 4xx) — never “soft accepted”

---

## 🧠 Why this folder exists

Geo filters are a high-leverage surface area:

- They drive **spatial queries** (potentially expensive) ⛏️
- They can be a vector for **DoS-style inputs** (e.g., huge polygons) 🧨
- They must be validated **at the API boundary** (contract-first) so the UI/clients can rely on consistent behavior 🔒

**Contract tests + fixtures** make “what must be rejected” explicit and repeatable.

---

## 🗺️ What counts as a “geo filter” (conceptually)

Exact parameter names vary by endpoint/contract, but geo filters typically look like one (or more) of:

- **BBox-style filter** (minLon, minLat, maxLon, maxLat)
- **Geometry / intersects-style filter** (GeoJSON geometry or Feature)
- **Point + radius / distance** style filter
- **AOI polygon** (often GeoJSON Polygon/MultiPolygon)

✅ Always validate against the **actual API contract** (OpenAPI / GraphQL / JSON Schema) used by the server.

---

## ✅ What “good invalid fixtures” look like

### 1) Deterministic (no data dependency)
A fixture should fail **before** any dependency on:
- database contents
- external services
- “current” time
- environment-specific configuration

If the fixture sometimes passes depending on data, it doesn’t belong here.

### 2) One failure reason per fixture
Design each fixture to violate **one** rule, cleanly:
- type mismatch
- malformed structure
- out-of-range coordinate
- invalid geometry
- unsupported CRS
- exceeds max vertices/size limit

This keeps failures surgical and makes regressions obvious.

### 3) Minimal & readable
Prefer the **smallest** input that triggers the intended validation failure:
- fewer coordinates
- smaller JSON payloads
- short strings
- tiny AOIs (unless testing max size limits)

### 4) Safe data only (🛡️ sovereignty + sensitive locations)
Even in test fixtures:
- ❌ no real addresses
- ❌ no precise coordinates for sensitive sites
- ❌ no PII
- ✅ use synthetic / generic coordinates (e.g., 0/0, simple rectangles, clearly fake points)

---

## 🧪 Expected API behavior for invalid geo filters

Your fixture should assert whatever the **contract** says, but the intent is always:

- **Reject** the request (4xx)
- Return a **stable error envelope** (shape + keys)
- Include a **machine-readable** signal (error code / type) + a human message
- Prefer returning **field-level pointers** (e.g., `"bbox"`, `"geometry"`, `"intersects"`) when the contract supports it

> ⚠️ Important: don’t “lock in” framework quirks (like a specific validation library message) unless the contract explicitly defines it.

---

## 🧰 Common invalid categories to cover

Use these as a checklist when expanding coverage:

### 📦 Type & shape errors
- bbox is string/object instead of array
- geometry is array instead of object
- numbers provided as `"12.34"` strings (if contract requires numeric)

### 📍 Coordinate range errors
- latitude outside `[-90, 90]`
- longitude outside `[-180, 180]`
- radius/distance negative or zero (if disallowed)

### 🧭 Ordering / semantic errors
- bbox has min > max
- bbox uses lat/lon swapped (when contract requires lon/lat)
- missing required fields (e.g., geometry missing `"type"` or `"coordinates"`)

### 🧩 Invalid GeoJSON
- Polygon ring not closed
- Polygon has too few points
- self-intersection (if validator checks)
- invalid “type” string

### 🧨 Size / complexity guardrails
- excessive vertices
- deeply nested coordinates
- payload exceeds max size (if enforced)

---

## 🏷️ Naming conventions (recommended)

Follow existing patterns in this repo (if present). If you’re introducing new fixtures, prefer:

```
<filter>__<reason>.<ext>
```

Examples (illustrative):
- `bbox__too_few_values.json`
- `bbox__min_greater_than_max.json`
- `geometry__not_geojson_object.json`
- `geometry__polygon_ring_not_closed.json`
- `radius__negative.json`

✅ Keep names *searchable* and *specific*.

---

## ➕ Adding a new invalid fixture

1) **Start from the contract** 📜  
   Find the geo filter definition in the API contract (commonly under something like `src/server/contracts/`).

2) **Pick one rule to break** 🎯  
   Ensure the fixture fails for *that* reason — not a different earlier validation error.

3) **Create the fixture file in this folder** 📄  
   Keep it minimal, synthetic, and endpoint-agnostic.

4) **Assert the contract-defined error** 🧪  
   Update/ensure the contract test harness expects the right:
   - status code
   - error envelope shape
   - stable code/type/pointer (if defined)

5) **Avoid coupling to unstable text** 🧊  
   Prefer matching stable keys/codes over full string messages, unless message text is contractually fixed.

---

## 🧾 Fixture “shape” (example only)

> The **actual** fixture schema is defined by the contract test harness in this repo.  
> Use this only as a conceptual example of what a self-describing fixture *might* contain.

```json
{
  "case": "bbox__min_greater_than_max",
  "request": {
    "query": {
      "bbox": [10, 0, -10, 1]
    }
  },
  "expect": {
    "status": 400,
    "error_code": "GEO_FILTER_INVALID",
    "field": "bbox"
  }
}
```

---

## 🚦What NOT to put here

Put these elsewhere (endpoint-specific fixtures), not in `_shared`:

- “Geo filters not allowed on endpoint X”
- “Geo filter conflicts with endpoint X business rules”
- “Valid geo filter but returns no results” (that’s data-dependent)
- anything requiring special dataset seeding to reproduce

---

## 🔗 Related (internal)

- 📘 `docs/MASTER_GUIDE_v13.md` (contract-first + API boundary expectations)
- 🧩 `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` (how to evolve the API contract safely)
- ⚖️ `docs/governance/ETHICS.md` + `docs/governance/SOVEREIGNTY.md` (sensitive locations / data rules)

---

## ✅ Quick checklist (PR-ready)

- [ ] Fixture fails **deterministically** (no DB/data dependency)
- [ ] Only **one** validation rule is violated
- [ ] Input uses **synthetic** coordinates (no sensitive locations)
- [ ] Expected error matches the **contract** (shape + stable code/type)
- [ ] Naming is clear: `<filter>__<reason>.<ext>`
- [ ] Contract tests updated/green ✅

