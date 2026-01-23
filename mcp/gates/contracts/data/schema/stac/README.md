# 🛰️ STAC Schema Contract Gate (KFM)

![STAC](https://img.shields.io/badge/STAC-1.0.0-blue)
![Contract](https://img.shields.io/badge/data%20contract-schema%20%2B%20policy-0aa)
![Gates](https://img.shields.io/badge/policy%20as%20code-OPA%20%2B%20Conftest-brightgreen)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-purple)
![Provenance](https://img.shields.io/badge/provenance-STAC%20%2B%20DCAT%20%2B%20PROV-informational)

> [!IMPORTANT]
> In KFM, **STAC is not “nice metadata”** — it’s part of the **evidence-first trust boundary**. Every pipeline run should emit a **catalog triplet** (STAC + DCAT + PROV), and policy gates enforce that before anything is considered publishable. :contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}

---

## 🧭 What lives in this folder?

`mcp/gates/contracts/data/schema/stac/` defines the **STAC validation contract** used by KFM’s **policy gates** (CI + repo governance) to ensure:

- ✅ STAC **Items** and **Collections** are structurally valid
- ✅ KFM-required metadata extensions are present (`kfm:dataset_id`, `kfm:classification`, etc.)
- ✅ Spatial/temporal fields are well-formed (geometry/bbox/time range)
- ✅ STAC records remain **linkable** to the rest of the evidence stack (**DCAT + PROV**)
- ✅ Asset references are safe + consistent (formats, media types, optional checksums)
- ✅ Governance rules can “fail closed” (gate shuts, PR won’t merge) when requirements aren’t met :contentReference[oaicite:2]{index=2}:contentReference[oaicite:3]{index=3}

---

## 🧱 Where STAC fits in the KFM evidence pipeline

KFM’s intake philosophy treats raw data as immutable evidence and pushes all transformations downstream. A “publishable unit” includes boundary artifacts in open standards — at minimum **STAC/DCAT/PROV**. :contentReference[oaicite:4]{index=4}

A typical repo layout (simplified) looks like:

```text
🧠 mcp/
  🚧 gates/
    📜 contracts/
      🗂️ data/
        🧩 schema/
          🛰️ stac/        <-- you are here

🗃️ data/
  🧱 raw/                 (immutable evidence boundary)
  🧪 work/                (controlled transforms)
  ✅ processed/            (derived artifacts)
  🛰️ stac/
    🗂️ collections/
    🧷 items/
  📇 catalog/              (source-of-truth catalog layer)
  🧬 prov/                 (lineage bundles)
```

KFM uses STAC as a core descriptor of **what/where/when + where the files are**, and the catalog + API treat validated metadata as the source-of-truth for discovery and trust. :contentReference[oaicite:5]{index=5}:contentReference[oaicite:6]{index=6}

---

## 🗺️ Contract scope

### Objects covered
This gate targets the STAC objects KFM depends on most:

- **STAC Collection** (dataset-level envelope)
- **STAC Item** (time slice / observation / processed product variant)

> KFM also uses STAC-like cataloging patterns in its broader geospatial hub design. :contentReference[oaicite:7]{index=7}

### Why it matters (UI + AI)
- The UI is map-first, and time controls (timeline slider / temporal exploration) depend on consistent time metadata. :contentReference[oaicite:8]{index=8}:contentReference[oaicite:9]{index=9}
- Focus Mode **must cite sources** and integrates with map/time context; without stable STAC references, “evidence-backed answers” break. :contentReference[oaicite:10]{index=10}
- The knowledge graph import expects catalog-backed identifiers (no “mystery nodes”). :contentReference[oaicite:11]{index=11}

---

## 🧩 KFM STAC Profile (required extensions)

KFM extends STAC with mandatory fields to keep metadata stable, governable, and linkable:

- `kfm:dataset_id` — stable KFM dataset identifier  
- `kfm:classification` — data governance label (e.g., public/internal/…) :contentReference[oaicite:12]{index=12}

KFM describes itself as standards-first and explicitly calls out STAC/DCAT/PROV as core interoperability anchors. :contentReference[oaicite:13]{index=13}

> [!NOTE]
> The authoritative normative description is the project’s profile docs (e.g., `docs/standards/KFM_STAC_PROFILE.md`), and profiles are versioned alongside PROV conventions. :contentReference[oaicite:14]{index=14}

### Minimum STAC semantics KFM relies on
A STAC record should answer:
- **What** is this dataset/product?
- **Where/When** does it apply?
- **Where are the actual files?** (`assets[]` + links) :contentReference[oaicite:15]{index=15}

KFM also assumes:
- Geometry/bbox follow **WGS84** conventions. :contentReference[oaicite:16]{index=16}
- STAC is one of the core drivers for graph import + dataset discovery. :contentReference[oaicite:17]{index=17}

---

## 🔗 Cross-profile linking: STAC ↔ DCAT ↔ PROV

KFM is designed so that a dataset’s metadata is not a single file — it’s a **connected evidence bundle**.

At minimum, each publishable dataset should have:
- STAC collection + item(s)
- DCAT dataset record
- PROV lineage bundle :contentReference[oaicite:18]{index=18}:contentReference[oaicite:19]{index=19}

**Contract expectation (recommended pattern):**
- A STAC Item/Collection should include `links[]` that point to the corresponding DCAT + PROV artifacts (exact `rel` values are profile-defined).
- Provenance should remain queryable end-to-end (“which stories used this dataset?”, “what process produced this artifact?”). :contentReference[oaicite:20]{index=20}:contentReference[oaicite:21]{index=21}

---

## 📦 Assets & packaging patterns (COG / GeoParquet / PMTiles / OCI)

KFM pipelines commonly emit multiple “delivery shapes” for the same dataset:
- GeoParquet (analysis/queries)
- COG / imagery
- XYZ tiles / precomputed tilesets  
…and the system updates metadata (size/checksum/thumbnail/stats) as part of the pipeline. :contentReference[oaicite:22]{index=22}

### ✨ Optional: OCI artifact distribution (`distribution.oci`)
KFM proposals describe distributing data artifacts in OCI registries using **ORAS**, with integrity via **Cosign** signatures. :contentReference[oaicite:23]{index=23}

To make this discoverable from catalogs, KFM suggests storing OCI coordinates in STAC/DCAT as a `distribution.oci` entry (registry, repo, tag, digest, plus file list + media types). :contentReference[oaicite:24]{index=24}

<details>
  <summary><b>📦 OCI packaging notes (expand)</b></summary>

- ORAS can push multiple files (e.g., `*.pmtiles` + `*.geoparquet`) under one artifact reference, each with a distinct media type. :contentReference[oaicite:25]{index=25}
- Catalog metadata can reference immutable content by digest, improving reproducibility and rollback. :contentReference[oaicite:26]{index=26}
- A run manifest can be canonicalized and hashed (RFC 8785) to produce stable identifiers for audit + provenance linking. :contentReference[oaicite:27]{index=27}

</details>

---

## ✅ What the STAC gate should enforce

KFM’s architecture explicitly calls for **automated policy gates** that include schema validation and STAC/DCAT/PROV completeness checks (plus license + sensitivity + provenance completeness). :contentReference[oaicite:28]{index=28}

Below is the practical checklist this contract typically enforces.

### MUST (hard fail / “gate closed”)
- **Schema-valid STAC** for Item/Collection
- `kfm:dataset_id` present and stable :contentReference[oaicite:29]{index=29}
- `kfm:classification` present (governance label) :contentReference[oaicite:30]{index=30}
- Spatial footprint fields present & consistent (bbox/geometry), WGS84 conventions :contentReference[oaicite:31]{index=31}
- Temporal semantics present (datetime or start/end in extent/summaries; per profile)
- **License present** (policy gate example requirement) :contentReference[oaicite:32]{index=32}
- Links to the evidence bundle (DCAT + PROV), per KFM conventions :contentReference[oaicite:33]{index=33}

### SHOULD (strongly recommended; may be enforced for “published” datasets)
- Assets include `type` (media type), roles, and stable hrefs
- Checksums / file size / thumbnails included when available (pipelines often populate these) :contentReference[oaicite:34]{index=34}
- No orphaned graph references (“nothing goes into the graph without its catalog entry”) :contentReference[oaicite:35]{index=35}

### MAY (optional extensions)
- `distribution.oci` block for OCI-resident artifacts :contentReference[oaicite:36]{index=36}
- Run-manifest linkages (run_id, canonical_digest) for audit trails :contentReference[oaicite:37]{index=37}

---

## 🧪 Validation workflow

KFM’s docs describe validation as a first-class part of the pipeline: schema validation, spatial validation, and license checks, enforced by CI/policy. :contentReference[oaicite:38]{index=38}:contentReference[oaicite:39]{index=39}

### Local (developer) validation
- Run the repo’s catalog QA / validation tooling (e.g., `tools/validation/catalog_qa`) which updates + checks metadata and validates catalogs. :contentReference[oaicite:40]{index=40}
- Run policy tests (Conftest + OPA Rego) to ensure governance constraints pass. :contentReference[oaicite:41]{index=41}

> [!TIP]
> Treat metadata like code: validate early, validate often — CI should never be the first place you find out a STAC record is broken. (This mirrors KFM’s “treat data like code” ethos.) :contentReference[oaicite:42]{index=42}

---

## 🧾 Authoring checklist (quick wins)

When adding/updating a dataset:

1. 🗂️ Create/Update **STAC Collection** (dataset envelope)
2. 🧷 Create/Update **STAC Item(s)** for relevant time slices / products  
3. 🔐 Set `kfm:classification` correctly and ensure a license exists :contentReference[oaicite:43]{index=43}:contentReference[oaicite:44]{index=44}
4. 🔗 Add links to DCAT + PROV artifacts (evidence bundle) :contentReference[oaicite:45]{index=45}
5. 📦 Add assets for canonical deliverables (GeoParquet / PMTiles / COG, etc.) :contentReference[oaicite:46]{index=46}
6. ✅ Run validation tools + policy checks

---

## 🧰 Examples

> [!NOTE]
> These examples are intentionally minimal and use placeholder link rels/URIs. The **exact** required fields and `stac_extensions` IDs should match `docs/standards/KFM_STAC_PROFILE.md`. :contentReference[oaicite:47]{index=47}

### Example: STAC Collection (minimal + KFM fields)

```json
{
  "type": "Collection",
  "stac_version": "1.0.0",
  "id": "kfm.ks.example_dataset.v2026_01_23",
  "title": "Example Dataset (Kansas)",
  "description": "Example collection showing the KFM-required fields and cross-links.",
  "license": "CC-BY-4.0",
  "extent": {
    "spatial": { "bbox": [[-102.05, 36.99, -94.59, 40.00]] },
    "temporal": { "interval": [["1850-01-01T00:00:00Z", null]] }
  },
  "links": [
    { "rel": "root", "href": "/data/stac/catalog.json", "type": "application/json" },
    { "rel": "items", "href": "./items/", "type": "application/json" },

    { "rel": "describedby", "href": "/data/catalog/dcat/kfm.ks.example_dataset.json", "type": "application/json" },
    { "rel": "derived_from", "href": "/data/prov/kfm.ks.example_dataset.prov.jsonld", "type": "application/ld+json" }
  ],
  "assets": {
    "geoparquet": {
      "href": "/data/processed/example/example.parquet",
      "type": "application/vnd.geo+parquet",
      "roles": ["data"]
    },
    "pmtiles": {
      "href": "/data/processed/example/example.pmtiles",
      "type": "application/vnd.pmtiles",
      "roles": ["tiles"]
    }
  },

  "kfm:dataset_id": "ks-example-dataset",
  "kfm:classification": "public"
}
```

### Example: STAC Item (minimal Feature + assets)

```json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "kfm.ks.example_dataset.1900",
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [-102.05, 36.99], [-94.59, 36.99], [-94.59, 40.00], [-102.05, 40.00], [-102.05, 36.99]
    ]]
  },
  "bbox": [-102.05, 36.99, -94.59, 40.00],
  "properties": {
    "datetime": "1900-01-01T00:00:00Z",

    "kfm:dataset_id": "ks-example-dataset",
    "kfm:classification": "public"
  },
  "links": [
    { "rel": "collection", "href": "../collection.json", "type": "application/json" },

    { "rel": "describedby", "href": "/data/catalog/dcat/kfm.ks.example_dataset.json", "type": "application/json" },
    { "rel": "derived_from", "href": "/data/prov/kfm.ks.example_dataset.prov.jsonld", "type": "application/ld+json" }
  ],
  "assets": {
    "data": {
      "href": "/data/processed/example/example_1900.parquet",
      "type": "application/vnd.geo+parquet",
      "roles": ["data"]
    }
  }
}
```

### Example: Optional `distribution.oci` (concept)
If your deliverables live in an OCI registry, include an OCI distribution description in the STAC/DCAT record so it’s fetchable and verifiable. :contentReference[oaicite:48]{index=48}

```json
{
  "distribution.oci": {
    "registry": "ghcr.io",
    "repository": "myorg/kfm/example_dataset",
    "tag": "20260123",
    "digest": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "files": [
      { "path": "example.pmtiles", "mediaType": "application/vnd.pmtiles" },
      { "path": "example.parquet", "mediaType": "application/vnd.geo+parquet" }
    ]
  }
}
```

---

## 🧯 Common failure modes (and why the gate is strict)

- **Messy/inconsistent metadata** causes downstream analysis/UI/AI to mislead users — data quality and consistency checks are foundational. :contentReference[oaicite:49]{index=49}:contentReference[oaicite:50]{index=50}
- **Missing governance labels** risks accidental exposure of sensitive content; privacy-preserving controls and “deny unsafe queries” are core safety patterns. :contentReference[oaicite:51]{index=51}:contentReference[oaicite:52]{index=52}
- **Broken spatial/temporal semantics** break map zooming, time filtering, and narrative discovery (timeline slider relies on these fields). :contentReference[oaicite:53]{index=53}

---

## 🧾 Versioning & evolution rules

- KFM profiles (STAC/DCAT/PROV) are expected to be **explicitly versioned** and updated in standards docs. :contentReference[oaicite:54]{index=54}
- When you change the STAC contract:
  - 📌 Update profile docs (and bump version)
  - 🧪 Add fixtures (valid/invalid) for regression tests
  - ✅ Update Conftest policies if governance rules change :contentReference[oaicite:55]{index=55}

---

## 📚 Related docs & references

### Core KFM docs
- 📥 Data Intake philosophy + catalog triplet: STAC/DCAT/PROV :contentReference[oaicite:56]{index=56}
- 🧱 Architecture + policy gates (schema validation, completeness, license, classification, provenance) :contentReference[oaicite:57]{index=57}
- 🧰 Technical pipeline outputs + validation updates (checksums/thumbnails/stats) :contentReference[oaicite:58]{index=58}
- 🧠 AI system ethos: always cite sources; map/time context integration :contentReference[oaicite:59]{index=59}
- 🗺️ UI system overview (map-first + Focus Mode panel) :contentReference[oaicite:60]{index=60}:contentReference[oaicite:61]{index=61}
- 🧪 Innovative concepts (standards integration + profile discipline) :contentReference[oaicite:62]{index=62}

### MCP / governance / docs practices
- 🧬 MCP scientific rigor + repo layout including `data/stac/…` :contentReference[oaicite:63]{index=63}
- 📝 Markdown practices guide (formatting patterns used across MCP docs) :contentReference[oaicite:64]{index=64}
- 🧭 v13 Markdown guide flow + STAC/DCAT/PROV boundary artifacts :contentReference[oaicite:65]{index=65}

### Geospatial + data engineering references bundled in project
- 🧭 WGS84 transform recipe reference (helpful when validating geometry/bbox) :contentReference[oaicite:66]{index=66}
- 🔐 Data quality + privacy references that motivate strict gating (consistency/cleaning/privacy) :contentReference[oaicite:67]{index=67}:contentReference[oaicite:68]{index=68}

---

<details>
  <summary><b>📎 Source Trace: “use all project files” coverage (expand)</b></summary>

This README is grounded in the project’s uploaded documents, including:
- Evidence-first intake + catalog triplet (STAC/DCAT/PROV): :contentReference[oaicite:69]{index=69}
- STAC semantics (what/where/when/assets) + WGS84 + graph import dependency: :contentReference[oaicite:70]{index=70}
- Mandatory KFM STAC profile fields (`kfm:dataset_id`, `kfm:classification`): :contentReference[oaicite:71]{index=71}
- Automated policy gates (schema validation + completeness + license + classification + provenance): :contentReference[oaicite:72]{index=72}
- Conftest/OPA “gate closed” behavior + license requirement example: :contentReference[oaicite:73]{index=73}
- OCI + ORAS + Cosign + `distribution.oci` proposal: :contentReference[oaicite:74]{index=74}:contentReference[oaicite:75]{index=75}
- Timeline slider relying on STAC date fields: :contentReference[oaicite:76]{index=76}
- UI + AI dependency on stable, citable datasets: :contentReference[oaicite:77]{index=77}:contentReference[oaicite:78]{index=78}
- Project reference bundles included as PDF portfolios (open in Acrobat for full contents):  
  - AI concepts portfolio: :contentReference[oaicite:79]{index=79}  
  - Maps/WebGL/virtual worlds portfolio: :contentReference[oaicite:80]{index=80}  
  - Programming languages/resources portfolio: :contentReference[oaicite:81]{index=81}  
  - Data management & Bayesian methods portfolio: :contentReference[oaicite:82]{index=82}

</details>

