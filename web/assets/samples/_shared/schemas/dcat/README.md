# 🧾 DCAT Schemas (Shared Web Samples)

![DCAT](https://img.shields.io/badge/standard-DCAT%20(v2)-2b6cb0)
![JSON-LD](https://img.shields.io/badge/format-JSON--LD-475569)
![JSON%20Schema](https://img.shields.io/badge/validation-JSON%20Schema-16a34a)
![KFM](https://img.shields.io/badge/project-KFM-7c3aed)
![Web%20Samples](https://img.shields.io/badge/scope-web%20sample%20assets-f97316)

> 📌 **Purpose:** Shared **DCAT shapes** (JSON Schema + JSON-LD examples) used by the **web app** sample fixtures and UI tooling.
>
> 🧠 **Mental model:** **DCAT = “dataset discovery layer”** (what the dataset *is*, who publishes it, how to access it).  
> For geospatial detail, we typically point outward to **STAC** via distributions. For lineage, we point outward to **PROV**.

---

## 🧭 Where you are

```txt
web/assets/samples/_shared/schemas/dcat/   ✅ you are here
```

> [!NOTE]
> This folder is **for web samples** (fixtures, demos, UI docs).  
> The **canonical** schema/profile source of truth should live under `schemas/dcat/` (repo root), and generated catalog outputs live under `data/catalog/dcat/`.

---

## 🗺️ How DCAT fits in the KFM pipeline

```mermaid
flowchart LR
  A[ETL / ingest] --> B[Catalogs: STAC + DCAT + PROV]
  B --> C[Graph build (Neo4j)]
  C --> D[API layer (contracts + redaction)]
  D --> E[Web UI (React + MapLibre)]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
```

---

## 🧩 What belongs in this folder

Keep this folder **small, stable, and UI-friendly**. Typical contents include:

- 🧱 **JSON Schemas** for the *KFM-shaped* DCAT objects the UI needs (dataset cards, search results, detail panels)
- 🧪 **Sample JSON-LD fixtures** representing *valid* DCAT datasets/distributions for demos & tests
- 🧷 (Optional) **Contexts / prefix maps** used by sample JSON-LD

> [!TIP]
> If you need something “real,” reference the generated catalog outputs under `data/catalog/dcat/` (and fetch via the API boundary in the running system). This folder is for **samples**, not publication.

---

## ✅ KFM DCAT baseline rules (what the UI should assume)

### 1) A “discoverable dataset” must have the basics
At minimum, a dataset entry should carry:

- 🏷️ `title`
- 📝 `description`
- ⚖️ `license`
- 🧷 `keywords` (or equivalent discoverability tags)
- 🔗 `distribution` links (to STAC and/or downloadable resources)

### 2) Distributions are the bridge to assets
In KFM, DCAT is the **catalog view**; distributions should “point to where the data actually lives,” typically:

- 🗺️ a **STAC Item/Collection** for geospatial assets, **and/or**
- 📦 a stable download location for processed artifacts (e.g., GeoParquet, COG, CSV, etc.)

### 3) Sensitivity & access must be representable
The UI should be able to determine:

- 🔒 whether the dataset is **public**, **restricted**, or **redacted**
- 🧭 how to label or hide content based on classification/access rules

> [!IMPORTANT]
> Don’t hard-code access-bypassing sample links into UI features that would circumvent governance. Samples should model the **same boundary assumptions** as production (API-mediated access).

### 4) IDs should be stable and versioned
Use stable, descriptive IDs (and keep versions explicit) so UI caches, graph references, and story citations don’t drift.

---

## 🧪 Using these schemas in the web app

Common uses:

- ✅ Validate fixture files during dev/test (so sample data doesn’t rot)
- 🧱 Drive UI components (dataset cards, metadata panels) against a known shape
- 🔁 Keep UI expectations aligned with schema changes (contract-first)

**Example (Ajv-style validation)**

```js
// Example only — adapt paths/names to match your repo layout.
import Ajv from "ajv";
import addFormats from "ajv-formats";

import dcatDatasetSchema from "./dcat.dataset.schema.json";
import sampleDataset from "./samples/dataset.sample.json";

const ajv = new Ajv({ allErrors: true, strict: false });
addFormats(ajv);

const validate = ajv.compile(dcatDatasetSchema);
const ok = validate(sampleDataset);

if (!ok) {
  console.error("❌ DCAT sample failed schema validation:", validate.errors);
  process.exitCode = 1;
} else {
  console.log("✅ DCAT sample is valid");
}
```

---

## 📦 Example DCAT Dataset (JSON-LD)

<details>
  <summary><strong>👀 Click to expand sample</strong></summary>

```json
{
  "@context": {
    "dcat": "http://www.w3.org/ns/dcat#",
    "dct": "http://purl.org/dc/terms/",
    "prov": "http://www.w3.org/ns/prov#",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@type": "dcat:Dataset",
  "dct:identifier": "kfm.ks.landcover.2000_2020.v1",
  "dct:title": "Kansas Landcover (2000–2020)",
  "dct:description": "Annual landcover classifications for Kansas, harmonized for map + analysis use.",
  "dct:license": "https://creativecommons.org/licenses/by/4.0/",
  "dcat:keyword": ["kansas", "landcover", "remote-sensing"],
  "dcat:distribution": [
    {
      "@type": "dcat:Distribution",
      "dct:title": "STAC Item (primary geospatial asset)",
      "dcat:accessURL": "https://example.org/stac/collections/landcover/items/kfm.ks.landcover.2000_2020.v1",
      "dcat:mediaType": "application/geo+json"
    },
    {
      "@type": "dcat:Distribution",
      "dct:title": "Processed download (GeoParquet)",
      "dcat:downloadURL": "https://example.org/data/processed/landcover/kfm.ks.landcover.2000_2020.v1.geoparquet",
      "dcat:mediaType": "application/geoparquet"
    }
  ],
  "dct:provenance": "https://example.org/prov/runs/2026-01-01T00-00-00Z.jsonld"
}
```

</details>

---

## 🔁 Update checklist (keep samples aligned)

When you change anything DCAT-shaped:

- [ ] Update canonical schema/profile (`schemas/dcat/` and the DCAT profile doc, if applicable)
- [ ] Update/regen these web sample schemas & fixtures
- [ ] Run schema validation in tests/CI so drift is caught early
- [ ] Ensure distributions still link correctly (STAC or stable download)
- [ ] Ensure access/sensitivity semantics still render correctly in UI

---

## 🔗 Related docs & specs

### 🧠 KFM internal (repo paths)
- `docs/standards/KFM_DCAT_PROFILE.md` — KFM DCAT profile (required fields & extensions)
- `schemas/dcat/` — canonical DCAT JSON Schemas
- `data/catalog/dcat/` — generated DCAT outputs (JSON-LD)
- `data/stac/` — STAC collections/items (asset catalog)
- `data/prov/` — provenance bundles (lineage)

### 🌐 External standards
- W3C DCAT: https://www.w3.org/TR/vocab-dcat-2/
- W3C PROV-O: https://www.w3.org/TR/prov-o/

---

<p align="right"><a href="#-dcat-schemas-shared-web-samples">⬆️ Back to top</a></p>
