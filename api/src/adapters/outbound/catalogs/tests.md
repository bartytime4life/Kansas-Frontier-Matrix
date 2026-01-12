# 🧪 Catalog Outbound Adapter — Test Strategy (`api/src/adapters/outbound/catalogs/tests.md`)

![Contract-First](https://img.shields.io/badge/contract--first-OpenAPI%20%7C%20Schemas%20%7C%20Profiles-2ea44f)
![Metadata](https://img.shields.io/badge/metadata-STAC%20%7C%20DCAT%20%7C%20PROV-blue)
![Determinism](https://img.shields.io/badge/invariant-deterministic%20outputs-orange)

> KFM treats catalog artifacts as **boundary contracts**: STAC/DCAT/PROV outputs must be **machine-validated** and are required before downstream stages consume the data.  [oai_citation:0‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
> KFM’s published datasets are described with **STAC**, indexed in **DCAT**, and accompanied by **PROV** lineage metadata.  [oai_citation:1‡Audit of the Kansas Frontier Matrix (KFM) Repository.pdf](file-service://file-1RwSrWXaDb5fnJ5gZX5kS3)

---

## 🎯 Purpose

This document defines **what to test** and **how to test** the outbound *catalogs* adapter(s) responsible for exporting KFM domain objects into:

- 🗺️ **STAC** Items + Collections (JSON)
- 🧾 **DCAT** Catalog/Dataset/Distribution (JSON-LD)
- 🧬 **PROV-O** provenance bundles (JSON-LD)

These artifacts are the “**boundary artifacts**” required at publication time and must land in canonical locations (per repo conventions).  [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 📦 What lives in this folder (conceptually)

```text
api/src/adapters/outbound/catalogs/
  ├─ stac/        # render internal Dataset/Asset ➜ STAC Item/Collection
  ├─ dcat/        # render internal Dataset ➜ DCAT Dataset + Distributions (JSON-LD)
  ├─ prov/        # render pipeline lineage ➜ PROV bundle (JSON-LD)
  ├─ writers/     # filesystem/S3 writers, URL builders, link policies
  └─ tests.md     # (this) test strategy + cases
```

> If your implementation combines these, that’s fine—the tests still apply.

---

## ✅ Core invariants (the “do not break” rules)

### 1) Machine-valid metadata (schemas + profiles)
All emitted STAC/DCAT/PROV must be **machine-validated**; no dataset is “published” without valid metadata.  [oai_citation:3‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

**Test implication:** every “happy path” test ends with `validate(output, schema + profile)`.

---

### 2) Cross-artifact linkage correctness
- DCAT **Distribution** entries must link to STAC and/or the actual resource endpoints (download/tiles/etc.).  [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  [oai_citation:5‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- PROV must connect inputs → activities → outputs end-to-end (raw → intermediate → processed).  [oai_citation:6‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

**Test implication:** verify hyperlinks and IDs form a consistent graph across artifacts.

---

### 3) Deterministic outputs
Pipelines (and therefore their catalog artifacts) must be deterministic/replayable given the same inputs.  [oai_citation:7‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

**Test implication:** snapshot/golden-file tests must not depend on wall-clock time, random UUIDs, or unordered maps/sets.

---

### 4) Canonical output locations (when writing)
Catalog outputs must land in the canonical folders:
- `data/stac/collections/` and `data/stac/items/`
- `data/catalog/dcat/`
- `data/prov/`  [oai_citation:8‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

**Test implication:** integration tests confirm exact paths, naming, and that files are written atomically.

---

## 🧱 Test layers (recommended pyramid)

### A) Unit tests (pure transformations) 🧩
**Goal:** Given an internal model, produce correct JSON structures.

**Examples**
- `Dataset ➜ StacItem` (bbox/geometry/time/links/assets)
- `Dataset ➜ StacCollection` (extent/license/providers)
- `Dataset ➜ DcatDataset` (title/description/keywords/spatial/temporal/distributions)
- `Lineage ➜ ProvBundle` (entities/activities/agents)

**Assertions**
- Required fields present
- Optional fields handled correctly
- No forbidden/internal fields leaked (e.g., internal DB IDs)

---

### B) Schema & profile validation tests 🧾✅
**Goal:** Validate output against *the same schemas/profiles* used by CI and publication gates.  [oai_citation:9‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

**Implementation hint**
- Use `jsonschema` for STAC JSON
- Use JSON-LD expansion + SHACL (or equivalent) for DCAT/PROV if you have shapes; otherwise validate structural JSON schema + required predicates

---

### C) Golden/snapshot tests (semantic stability) 📸
**Goal:** Prevent accidental breaking changes to public-facing metadata.

**Rules**
- Canonicalize JSON (sorted keys, stable arrays, normalized decimals)
- Freeze time (`Clock`/`NowProvider`)
- Stable IDs (seeded UUID generator or deterministic ID function)

**When to update snapshots**
- Only when a deliberate versioned change occurs and is documented in release notes/versioning.  [oai_citation:10‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

### D) Cross-artifact contract tests 🔗
**Goal:** Validate that STAC/DCAT/PROV agree with each other.

**Examples**
- DCAT distribution `downloadURL`/`accessURL` matches STAC `links` or asset hrefs
- STAC item `id` and PROV output entity identifier correlate
- PROV activity references pipeline run/config identifiers (if your system includes them)  [oai_citation:11‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

### E) Integration tests (writers + storage) 📁☁️
**Goal:** Validate writing behavior to local FS or object storage.

**Examples**
- Writes are **atomic** (write temp → rename)
- Re-running export overwrites deterministically or creates versioned outputs (as designed)
- Directory layout is correct (canonical folders)  [oai_citation:12‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧪 Test matrix (minimum recommended)

| Area | Test name | Type | What it proves |
|------|-----------|------|----------------|
| STAC Item | `stac_item__minimal_vector__valid` | unit+schema | basic required STAC item fields + schema pass |
| STAC Item | `stac_item__cog_raster__assets_and_roles` | unit+schema | raster asset fields + roles + href correctness |
| STAC Collection | `stac_collection__extent_license_links` | unit+schema | extent/links/license consistency |
| DCAT Dataset | `dcat__dataset__distributions_link_to_stac` | contract | DCAT distributions reference STAC/real resources  [oai_citation:13‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) |
| PROV Bundle | `prov__end_to_end_chain__raw_to_processed` | contract | lineage connects raw → work → processed  [oai_citation:14‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) |
| Determinism | `export__same_input_same_output__byte_equal` | snapshot | stable ordering, stable times, stable IDs  [oai_citation:15‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) |
| Paths | `writer__outputs_to_canonical_locations` | integration | correct `data/stac`, `data/catalog/dcat`, `data/prov`  [oai_citation:16‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) |
| Errors | `validation__rejects_missing_required_fields` | negative | publication gate blocks invalid metadata  [oai_citation:17‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) |

---

## 🧰 Fixtures (golden test data)

Create fixtures that represent *real KFM usage patterns*:

### 1) Minimal Vector Dataset
- GeoJSON vector layer
- Known bbox + geometry
- One asset (download) + one “service” URL (tiles/features)

### 2) COG Raster Dataset
KFM emphasizes COG for raster publishing, so ensure raster assets are represented correctly.  [oai_citation:18‡Audit of the Kansas Frontier Matrix (KFM) Repository.pdf](file-service://file-1RwSrWXaDb5fnJ5gZX5kS3)

### 3) “Live feed” observation dataset (optional but valuable)
KFM proposals explicitly mention producing STAC Items for real-time observations and a DCAT dataset entry per feed.  [oai_citation:19‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx](file-service://file-QrXwct2pX9kFpqgjtBiijR)  
This is a great regression fixture for “rapidly changing but still valid” metadata.

---

## 🧷 Canonicalization rules (to avoid flaky tests)

To satisfy determinism requirements, enforce:

- **Stable JSON ordering:** sort keys; sort arrays where order is not semantically meaningful
- **Stable IDs:** derive from content (`hash(dataset_id + asset_path)`) or use seeded UUIDs
- **Stable time:** inject `NowProvider` and set fixed timestamps in tests
- **Stable floats:** normalize precision for bbox/coords when feasible

> Goal: given the same inputs, output should match exactly (or differences are explicitly logged and explained).  [oai_citation:20‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧾 Suggested test helpers (pseudo-code)

### Python-style (pytest)
```python
def test_stac_item__minimal_vector__valid(schema_registry, now_fixed):
    dataset = fixtures.minimal_vector_dataset(now=now_fixed)
    item = stac_renderer.to_item(dataset)

    jsonschema_validate(item, schema_registry.stac_item)
    assert item["type"] == "Feature"
    assert item["id"] == dataset.public_id
    assert "assets" in item and len(item["assets"]) >= 1
```

### TypeScript-style (vitest/jest)
```ts
it("dcat__dataset__distributions_link_to_stac", () => {
  const dataset = fixtures.minimalVectorDataset({ now: FIXED_NOW });
  const stac = stacRenderer.toItem(dataset);
  const dcat = dcatRenderer.toDataset(dataset, { stacHref: stac.links.find(l => l.rel === "self")?.href });

  expect(validateJsonLd(dcat)).toBe(true);
  expect(dcat.distribution[0].accessURL).toContain("/stac/");
});
```

---

## 🚦CI gating (recommended)

Run these checks on every PR touching catalogs:

1. ✅ Unit tests (fast)
2. ✅ Schema/profile validation (STAC/DCAT/PROV)  [oai_citation:21‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
3. ✅ Snapshot tests (golden outputs)
4. ✅ Integration tests (writers + canonical paths)  [oai_citation:22‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

If schema validation fails, the PR should be blocked—catalog validity is a first-order system contract.  [oai_citation:23‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧯 Troubleshooting guide

### “Snapshot changed but nothing meaningful changed”
- Did field ordering change? Add canonicalization.
- Did timestamps change? Inject/freeze `NowProvider`.
- Did IDs change? Switch to deterministic IDs in tests.
- Did floating precision differ? Normalize float formatting.

### “Schema passes but downstream breaks”
Add or extend **cross-artifact contract tests**:
- Verify DCAT distributions resolve to STAC/resources  [oai_citation:24‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- Verify PROV references the same outputs that STAC/DCAT describe  [oai_citation:25‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🔭 Future-proofing (without breaking contracts)

- When adding new metadata fields, prefer **profile extensions** over ad-hoc keys.  [oai_citation:26‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- If you must change public output shape, treat it like an API contract break: version it, document it, snapshot it.  [oai_citation:27‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🔗 Related docs (in-repo)

- `schemas/` — JSON Schemas & profiles for STAC/DCAT/PROV (contract artifacts)  [oai_citation:28‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- `api/contracts/` — API contracts (OpenAPI/GraphQL) and their contract tests (neighbor discipline)  [oai_citation:29‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- `data/stac/`, `data/catalog/dcat/`, `data/prov/` — canonical output locations  [oai_citation:30‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
