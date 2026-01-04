# 🧪 API Test Fixtures (Golden Data) 🧰

![fixtures](https://img.shields.io/badge/tests-fixtures-blue)
![deterministic](https://img.shields.io/badge/goal-deterministic-success)
![safe](https://img.shields.io/badge/rules-no%20secrets%20%2F%20no%20PII-critical)

Welcome to the **fixture vault** for the API test suite. Fixtures are **small, deterministic, reviewable inputs/outputs** used to keep tests stable, fast, and meaningful.

---

## 🎯 What belongs in `fixtures/`

Use fixtures for anything that should be **repeatable** across machines + CI runs:

- **📨 HTTP requests** (sample payloads your endpoints accept)
- **📬 HTTP responses** (“golden” outputs for contract tests / snapshot-style assertions)
- **🗺️ Geospatial samples** (tiny GeoJSON, bbox/tiles metadata, minimal feature sets)
- **🧠 Graph samples** (small graph datasets to validate constraints/invariants)
- **📦 Catalog metadata samples** (tiny STAC/DCAT/PROV JSON-LD examples)
- **🛰️ Remote-sensing derived samples** (small clipped outputs, summaries, timeseries snippets)

> Rule of thumb: **If it helps prevent a flaky test, it belongs here.**  
> If it’s big, sensitive, or “real production data” → it does **not** belong here.

---

## 🧱 Fixture principles (non‑negotiable)

### 1) ✅ Deterministic by design
- No “now()” timestamps, random IDs, UUIDs, or non-seeded randomness.
- Sort arrays where ordering isn’t meaningful.
- Normalize floats (rounding) when output precision is not contractually guaranteed.

### 2) 🔒 Safe + governed
- **Never** commit secrets: tokens, API keys, cookies, connection strings, signed URLs.
- **Never** commit PII or sensitive coordinates.
- If a fixture references a sensitive place, **generalize** (region/bbox) or use synthetic geometry.

### 3) 🧩 Contract-first
Fixtures should align with the API contract:
- Payloads validate against the endpoint schema.
- Responses validate against the contract and remain stable unless the contract changes.

### 4) 🪶 Keep fixtures tiny
- Prefer **minimal** GeoJSON: a handful of features (or even 1 feature) with realistic properties.
- Prefer **summaries** over raw rasters (e.g., precomputed stats instead of full imagery).
- If you *must* store binary, keep it tiny and documented (and consider alternatives first).

---

## 🗂️ Suggested directory layout

> Add folders as needed—keep names boring and obvious 😄

```text
📁 api/src/tests/fixtures/
├── 📁 http/
│   ├── 📁 requests/                 # request bodies, query param examples
│   └── 📁 responses/                # golden outputs for assertions
├── 📁 geo/
│   ├── 📁 geojson/                  # FeatureCollection / Feature samples
│   ├── 📁 tiles/                    # tilejson / style snippets (tiny)
│   └── 📁 projections/              # CRS / reproject edge cases
├── 📁 graph/
│   ├── 📁 cypher/                   # seed scripts (small!)
│   └── 📁 json/                     # node/edge exports for tests
├── 📁 catalogs/
│   ├── 📁 stac/                     # sample Item/Collection JSON
│   ├── 📁 dcat/                     # sample dataset/distribution JSON-LD
│   └── 📁 prov/                     # sample lineage JSON(-LD)
├── 📁 remote-sensing/
│   ├── 📁 summaries/                # zonal stats, timeseries samples
│   └── 📁 derived/                  # clipped outputs (very small)
└── 📄 README.md
```

---

## 🏷️ Naming conventions

Keep fixture filenames descriptive and grep-friendly:

### ✅ Recommended patterns
- **HTTP request**:  
  `http__<route>__<case>.request.json`
- **HTTP response**:  
  `http__<route>__<case>.response.json`
- **GeoJSON**:  
  `geo__<layer>__<case>.geojson`
- **Graph**:  
  `graph__<topic>__<case>.cypher` or `graph__<topic>__<case>.json`

### Examples
- `http__v1_fields_search__minimal.request.json`
- `http__v1_fields_search__ok.response.json`
- `geo__counties__bbox_small.geojson`
- `graph__locations__valid_minimal.cypher`

---

## 🧼 Sanitization checklist (before committing)

- [ ] Removed **secrets** (tokens/keys/cookies)
- [ ] Removed **PII** (names/emails/phones/user IDs not explicitly synthetic)
- [ ] Generalized or replaced **sensitive coordinates**
- [ ] Replaced any “real” IDs with **fixed, fake** IDs (`00000000-0000-...`)
- [ ] Confirmed file size is reasonable (try to keep fixtures **KB**, not **MB**)

---

## 🧪 How fixtures are typically used

### Unit tests
- Use fixtures to feed pure functions: parsers, validators, mappers, reducers.

### Integration / contract tests
- Use fixtures to:
  - seed a minimal dataset (or mock adapters)
  - call endpoints
  - assert on response shape + key values (golden files)

### Regression tests
- When fixing a bug, add:
  - **one failing input fixture**
  - **one expected output fixture**
  - a test that locks the behavior in

---

## ➕ Adding a new fixture (quick recipe)

1. **Pick the smallest representative case** (minimal but realistic).
2. **Name it clearly** using the conventions above.
3. **Add/extend the test** to load the fixture and assert deterministically.
4. **Run tests locally** and ensure no snapshot churn.
5. **Commit** with a message like:  
   `test(fixtures): add <route> <case> request/response`

---

## 🚫 Common anti-patterns (please don’t)

- ❌ “Real” production payload dumps
- ❌ Fixtures that include dynamic dates/timestamps
- ❌ Huge rasters, giant GeoJSON, or full DB dumps
- ❌ Anything that would fail a security/PII scan

---

## ✅ When fixtures are *not* the answer
If you need full pipeline or large dataset validation, fixtures belong in the **data pipeline/canonical data areas**, not in API test fixtures. Keep this folder focused on **test determinism** and **contract safety**.

---

## 🙌 Contributing notes
If you’re unsure where a fixture should live, choose the location that best matches the boundary it tests:
- API behavior → `http/`
- Spatial geometry correctness → `geo/`
- Ontology / graph invariants → `graph/`
- Metadata contract validation → `catalogs/`
- EO-derived behavior → `remote-sensing/`

