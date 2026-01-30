# 🧰 Fixtures (`tools/fixtures/`)

![Scope](https://img.shields.io/badge/scope-tools%2Ffixtures-2b7cff)
![Purpose](https://img.shields.io/badge/purpose-tests%20%7C%20demos%20%7C%20CI-7a3df0)
![Data](https://img.shields.io/badge/data-provenance--first-00b894)
![Formats](https://img.shields.io/badge/formats-GeoJSON%20%7C%20JSON%20%7C%20CSV%20%7C%20Parquet-lightgrey)

> **Deterministic sample assets** used across the Kansas Matrix System / **KFM** stack for testing, demos, docs, and CI validation.  
> Goal: make it *easy* to reproduce bugs, validate pipelines, and exercise API/UI paths without pulling huge datasets. ✅

---

## 🧭 What fixtures are for (and why we’re picky)

KFM is built around a **provenance-first pipeline** (raw ➜ processed ➜ catalog/prov ➜ database ➜ API ➜ UI). Fixtures help us test each stage quickly and consistently, without requiring full-scale data downloads.

Fixtures are intentionally:
- **Small** (fast for CI 🏎️)
- **Stable** (IDs don’t “randomly” change)
- **Explainable** (every pack has a manifest + source/license notes)
- **Safe** (no sensitive data; governance-friendly 🔒)

---

## ✅ What belongs here

Typical fixture “packs” include:

- 🧪 **API test fixtures** (request payloads, expected responses, error cases)
- 🗺️ **Mini geospatial layers** (GeoJSON, tiny rasters-as-metadata, sample geometries)
- 🧾 **Metadata exemplars** (STAC / DCAT / PROV examples for validation)
- 🧱 **DB seed snippets** (PostGIS SQL seeds, Neo4j CSV/JSON seed inputs)
- 🛡️ **Policy test cases** (OPA/Rego inputs & expected allow/deny outcomes)
- 🧠 **AI/RAG mocks** (stubbed retrieval results / citations / deterministic “answers”)

---

## 🚫 What does **NOT** belong here

Please keep these out of `tools/fixtures/`:

- 🗃️ **Large binaries** (big rasters, COGs, model weights)  
  → use `data/` + DVC/LFS/remote pointers (or documented external references)
- ⚖️ **Unlicensed / unclear-license** data
- 🧑‍🤝‍🧑 **PII / sensitive community data** (CARE-first: treat as restricted)
- 🎲 “Random” data without a **manifest**, **source**, and **reason to exist**
- 🧨 Fixtures that silently change over time (breaks reproducibility)

---

## 🗂️ Suggested folder layout

This directory is organized as **fixture packs**: each pack is a self-contained mini-world.

```text
📁 tools/
  📁 fixtures/
    📄 README.md
    📁 _template/                 # copy this to start a new pack
      📄 README.md
      📄 manifest.json
      📄 checksums.sha256
      📁 data/
      📁 metadata/
      📁 expected/
    📁 kfm-minimal-parcels/       # example pack name
      📄 README.md
      📄 manifest.json
      📄 checksums.sha256
      📁 data/
      📁 metadata/
      📁 expected/
```

> 💡 **Rule of thumb:** if a pack can’t be understood by reading its `README.md` + `manifest.json`, it’s not ready.

---

## 🧾 Fixture Pack Contract (required)

Each fixture pack **must** include:

### 1) `README.md` 📄
Keep it short but complete:
- What it tests (service/pipeline/policy/UI)
- What’s inside (files + meanings)
- Source / provenance (even if synthetic)
- License / attribution
- Any “gotchas” (CRS assumptions, ordering constraints, etc.)

### 2) `manifest.json` 🧩
A machine-readable description of the pack.

**Recommended schema (feel free to extend):**
```json
{
  "id": "kfm-minimal-parcels",
  "version": "1.0.0",
  "description": "Tiny land-parcel + event link dataset for API + graph tests.",
  "intended_use": ["api-tests", "pipeline-smoke", "policy-tests"],
  "data_contract": {
    "crs": "EPSG:4326",
    "time_zone": "UTC",
    "id_stability": "stable"
  },
  "artifacts": [
    {
      "path": "data/parcels.geojson",
      "type": "geojson",
      "roles": ["processed"],
      "primary_keys": ["parcel_id"]
    },
    {
      "path": "metadata/stac-item.json",
      "type": "stac-item",
      "roles": ["catalog"]
    },
    {
      "path": "metadata/prov.json",
      "type": "prov",
      "roles": ["provenance"]
    }
  ],
  "license": {
    "spdx": "CC-BY-4.0",
    "notes": "Synthetic geometries; structure mirrors real pipeline output."
  },
  "maintainers": ["@your-handle"],
  "created": "2026-01-30"
}
```

### 3) `checksums.sha256` 🔐
A checksum list for pack stability (helps detect accidental changes).

Example:
```text
e3b0c44298fc1c149afbf4c8996fb924...  data/parcels.geojson
a54d88e06612d820bc3be72877c74f25...  metadata/stac-item.json
```

---

## 🌍 Geospatial conventions (KFM-friendly)

To keep fixtures interoperable across the stack:

- 🧭 **Default CRS:** `EPSG:4326` for GeoJSON unless a pack *explicitly* documents otherwise.
- 📏 If a projected CRS is required (analysis fixtures), document:
  - CRS string (EPSG code)
  - Units
  - Why it’s necessary
- 🧱 Keep geometries **tiny and valid**
  - Avoid self-intersections
  - Close rings
  - Ensure `FeatureCollection` is valid JSON

---

## 🧬 Metadata conventions (STAC / DCAT / PROV)

If a fixture represents a “dataset-like” artifact, include minimal-but-valid:
- 🗂️ **STAC** records describing the asset(s)
- 🧾 **DCAT** dataset entry (when relevant)
- 🧿 **PROV** lineage bundle (raw ➜ transform ➜ output)

> 🧠 The fixture goal is not to be “complete STAC,” but to be **valid enough** that our validators, loaders, and UI can exercise real paths.

---

## 🧰 Using fixtures

### 🧪 In tests
Fixtures should be usable by unit and integration tests without network access.

Common usage patterns:
- Load files by **relative path from repo root**
- Avoid hidden dependencies (no “download this first” steps)
- Keep test data deterministic (fixed timestamps if needed)

### 🧱 In pipelines
Fixture packs are ideal for:
- smoke testing pipeline stages (parse ➜ normalize ➜ write outputs)
- validating metadata generation and provenance stitching

### 🖥️ In UI demos
UI fixtures should be:
- visually meaningful (a few features, clear bounding box)
- fast to load (small JSON)
- consistent across runs (stable IDs)

---

## 🧷 Naming + versioning rules

- 📛 Pack names: `kebab-case` (e.g., `kfm-minimal-parcels`)
- 🔢 Pack versioning: SemVer in `manifest.json` (`1.0.0`, `1.1.0`, etc.)
- 🧊 Prefer **append-only** evolution:
  - breaking changes ⇒ new major version or new pack
- 🧾 If you change fixture meaning, update:
  - `manifest.json` version
  - `checksums.sha256`
  - pack `README.md` change notes

---

## ✅ PR checklist (fixtures)

Before submitting:
- [ ] Pack has `README.md`, `manifest.json`, and `checksums.sha256`
- [ ] All data is open-licensed or synthetic-with-notes
- [ ] No secrets / tokens / PII
- [ ] JSON/GeoJSON parses cleanly
- [ ] IDs are stable + documented
- [ ] Any STAC/DCAT/PROV examples are valid enough to pass validators (or clearly marked “intentionally invalid” for negative tests)

---

## 🔗 Related docs (jump points)

- 📚 Repo overview: `../../README.md`
- 🧪 API tests: `../../api/`
- 🗺️ Pipelines: `../../pipelines/`
- 🧾 Data catalog + provenance: `../../data/`
- 🛡️ Governance / policies: `../../policy/`
- 📖 Architecture + standards: `../../docs/`

---

## 🧱 Template pack starter

Need a quick start? Copy:

```text
tools/fixtures/_template/  ➜  tools/fixtures/<your-pack>/
```

Then edit:
- `README.md`
- `manifest.json`
- `checksums.sha256`

Happy testing 🧪✨