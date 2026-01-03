# 🧪 Fixtures — `GET /v1/layers` ✅ (Happy Path)

![Contract Tests](https://img.shields.io/badge/contract-tests-blue)
![Endpoint](https://img.shields.io/badge/GET-%2Fv1%2Flayers-brightgreen)
![Scenario](https://img.shields.io/badge/scenario-happy%20path-success)

This folder contains **deterministic fixtures** for the contract test case:

> **`GET /v1/layers`** → returns the **layer catalog** the UI uses to populate layer/timeline controls 🗺️⏳

---

## 🎯 Goal

Lock down the **externally observable behavior** of `/v1/layers` so downstream consumers (UI, tools, integrations) can rely on:

- ✅ status code & headers  
- ✅ response body *shape* (schema)  
- ✅ response body *meaning* (stable IDs + stable semantics)

This is contract-first territory: changes here should be intentional, reviewable, and versioned. 🔒

---

## 🧭 What “Layers” mean in KFM

A **layer** is a toggle-able geospatial dataset (raster or vector) that the platform can render and/or query over time.

Typical examples include:
- 🗺️ historical topographic map layers  
- 🧾 cadastral / land ownership boundaries  
- 🏔️ terrain products (DEM / hillshade / slope)  
- 🌊 hydrology + wetlands + lakes  
- 🌾 land cover / vegetation comparisons  
- 🏘️ settlements + forts + trails + rail expansion  

---

## 📦 What lives in `fixtures/`

📁 `api/tests/contract/cases/GET__v1_layers__happy_path/fixtures/`

| File / Folder | Purpose 🧩 | Notes |
|---|---|---|
| 📄 `README.md` | This guide | Keep it current |
| 📄 `request.*` | Canonical request snapshot | For GETs: mostly path, query params, headers |
| 📄 `response.200.*` | Expected **200 OK** output | Body + (optionally) headers |
| 📁 `seed/` or `stubs/` | Optional deterministic backing data | Only if the harness needs it |

> If your harness uses different filenames: **keep the intent the same**, update the table, and stay consistent across cases.

---

## ✅ Fixture rules (keep contract tests boring)

### 1) Deterministic output 🔁
- Sort the returned layer list by a stable key (usually `id` or `slug`).
- Avoid volatile fields (timestamps, random UUIDs, hostnames that change per env).
- Prefer stable URLs (or predictable templates) over env-specific absolute links.

### 2) Minimal but representative 🧪
Keep the happy-path fixture small, but make sure it exercises the contract:
- at least **one raster-style** layer
- at least **one vector-style** layer
- at least **one time-aware** layer *(if the API supports temporal extents)*

### 3) Provenance / attribution is required 🧾
KFM is evidence-first. Each layer record should include enough attribution/provenance
for the UI to show “where this came from” without inventing it.

Practical guidance:
- include a human-readable attribution/source label
- include stable references to catalog records when available (STAC/DCAT/PROV identifiers or links)

### 4) Don’t leak 🔐
Fixtures must **never** contain:
- secrets / tokens / API keys
- internal-only endpoints
- sensitive coordinates or restricted datasets (unless redaction rules are explicitly under test)

---

## 🔄 Updating fixtures (when `/v1/layers` changes)

1. **Update the OpenAPI contract** (the source of truth).  
2. Regenerate or edit fixtures to match the contract:
   - `response.200.*`
   - `request.*` *(if query params/headers changed)*
3. Re-run contract tests locally + in CI.  
4. If the change is breaking:
   - **don’t silently change** `/v1/...`
   - introduce `/v2/...` (or a version negotiation strategy) and keep `/v1` stable until sunset

---

## 🧷 Naming convention (why this folder name looks wild)

Case folders follow a readable pattern:

`<METHOD>__<path>__<scenario>`

Example:
- `GET__v1_layers__happy_path`

This keeps contract suites grep-friendly and avoids OS path issues. 📎

---

## 🧰 Quick PR checklist

- [ ] Fixture response validates against the OpenAPI schema for `/v1/layers`
- [ ] Layer list ordering is deterministic
- [ ] IDs are stable (no random UUIDs)
- [ ] Provenance/attribution is present per layer
- [ ] No secrets, no env-specific hostnames, no volatile timestamps

---

## 🧩 Optional: conceptual response shape (illustrative)

<details>
<summary>Click to expand (⚠️ illustrative only — follow the OpenAPI contract)</summary>

```json
[
  {
    "id": "string",
    "title": "string",
    "type": "raster|vector",
    "extent": { "bbox": [minX, minY, maxX, maxY] },
    "time": { "start": "YYYY-MM-DD", "end": "YYYY-MM-DD" },
    "provenance": {
      "source": "string",
      "stac_item": "string",
      "dcat_dataset": "string",
      "prov_bundle": "string"
    }
  }
]
```

</details>

---

## 🔗 Related docs

- 📘 Master guide: `../../../../../../docs/MASTER_GUIDE_v13.md`
- 🧾 Metadata profiles (STAC/DCAT/PROV): `../../../../../../docs/standards/`
- 🧩 API contracts (OpenAPI): `../../../../../../src/server/contracts/`

> Tip: If you’re adding new layers, ensure the **catalog metadata exists first** (STAC/DCAT/PROV), then expose via API. 🧠➡️🗺️

