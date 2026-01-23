---
title: "🗂️ DCAT Dataset Links (Model Card)"
model_id: "<model_id>"
scope: "Datasets this model may reference/cite via DCAT (and cross-links to STAC + PROV)"
---

# 🧾 DCAT Dataset Links — `<model_id>`

![DCAT](https://img.shields.io/badge/metadata-DCAT-blue)
![STAC](https://img.shields.io/badge/geospatial-STAC-green)
![PROV](https://img.shields.io/badge/lineage-PROV--O-yellow)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-purple)

> According to the v13 KFM design docs, **pipeline ordering is absolute** (ETL → Catalogs → Graph → API → UI → Story Nodes → Focus Mode), and **nothing** should be consumed by later stages unless it has already passed through the earlier stages (including emitting STAC/DCAT/PROV + provenance). [oai_citation:0‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🔎 What this file is for

This file is the **link index** for DCAT dataset records that `<model_id>` is allowed to:
- ✅ **discover** (via catalog search / API),
- ✅ **cite** (Focus Mode / story answers),
- ✅ **retrieve** (via `dcat:distribution` access URLs),
- ✅ **audit** (via PROV lineage cross-links).

KFM’s governance assumes:
- **No citations → blocked** (policy gate), and
- **Provenance-first** publishing for anything surfaced in the graph/API/UI/Focus Mode.

---

## 🧭 Quick links

> Tip: this file lives at `mcp/model_cards/<model_id>/links/dcat_datasets.md`, so most repo links need `../../../../` to reach the repo root.

| Link | What it’s for |
|---|---|
| `../../../../data/catalogs/` | 📦 Canonical home for **DCAT** catalogs in v13-style docs [oai_citation:1‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) |
| `../../../../data/stac/` | 🗺️ Canonical home for **STAC** (collections/items) [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) |
| `../../../../data/prov/` | 🧬 Canonical home for **PROV** lineage docs [oai_citation:3‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) |
| `../../../../docs/standards/` | 📐 KFM profiles for STAC/DCAT/PROV (governed standards) [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) |
| `../../../../docs/guides/pipelines/` | ⚙️ How datasets are ingested + promoted via governed pipelines (no bypass) [oai_citation:5‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) |

> ⚠️ Some older docs refer to legacy paths like `data/catalog/` and `data/provenance/` for published metadata. [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
> If your repo still uses those, update the links below accordingly.

---

## 🧩 Legend

- 🟦 **DCAT** = dataset “contract” for discovery & access (`Dataset`, `Distribution`, license, publisher, etc.)
- 🟩 **STAC** = geospatial/temporal assets (collections/items, footprints, time ranges, asset links)
- 🟨 **PROV** = lineage (inputs → activities → outputs; agents; run IDs; reproducibility)
- 🔐 **Classification** = sensitivity / sovereignty constraints (FAIR+CARE-aligned)

---

## ✅ KFM invariants this index must preserve

### 1) Evidence triplet is required (STAC + DCAT + PROV)
KFM treats these as a linked “evidence stack,” written in version-controlled paths (DCAT in `data/catalogs/`, STAC in `data/stac/`, PROV in `data/prov/`). [oai_citation:7‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
Each artifact cross-references the others (e.g., DCAT distributions linking to STAC + PROV URLs). [oai_citation:8‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### 2) Catalog alignment is enforced
v13 alignment rules require each dataset to have:
- STAC (collection + items),
- DCAT dataset record with **minimal required** fields (title, description, license, publisher),
- PROV lineage record,
…and the IDs/links must align across the triplet. [oai_citation:9‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 3) “No mystery layers” + contract-first
KFM’s “contract-first” approach means datasets must satisfy metadata requirements before acceptance; this enables automatic attributions and citations and prevents unsourced layers from entering the official catalog. [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### 4) Sensitive data + CARE constraints must be encoded
KFM supports sensitivity-aware handling (redaction / generalization), and the docs explicitly call out CARE/Indigenous governance as a design constraint. [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
The “Innovative Concepts” research also recommends **cultural protocols / tiered access** patterns (e.g., restrictions and role-based access for sensitive heritage content). [oai_citation:12‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)

---

## 🧷 Dataset ID & link conventions

### Dataset ID convention
KFM uses stable, aligned dataset identifiers across STAC/DCAT/graph.

**Convention:** `kfm.<state>.<theme>.<name>.v#`  
**Example:** `kfm.ks.landcover.2000_2020.v1` [oai_citation:13‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### Where the links *usually* live (v13-style)
Use these as defaults (adjust if your repo uses legacy paths).

- 🟦 DCAT: `data/catalogs/dcat/<dataset_id>.{jsonld,ttl}`
- 🟩 STAC Collection: `data/stac/collections/<dataset_id>.json`
- 🟩 STAC Items: `data/stac/items/<dataset_id>/...`
- 🟨 PROV: `data/prov/<dataset_id>.{jsonld,prov.json}`

> v13 guidance also describes a DCAT home like `data/catalog/dcat/` (without the “s”), so treat the above as a repo-specific configuration knob. [oai_citation:14‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### DCAT distributions must be explicit
DCAT records should include `dcat:distribution` entries for:
- direct downloads (files),
- API endpoints,
- STAC catalog/collection URLs,
…and record media types / formats for each distribution. [oai_citation:15‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🌐 Runtime dataset discovery (API/UI hooks)

### Dataset API endpoints (server-side)
KFM’s API includes dataset listing and search endpoints such as:
- `GET /api/datasets`
- `GET /api/datasets/{id}`
- `GET /api/datasets/search?q=...` [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### UI Data Catalog expectations
The UI design includes a **Data Catalog UI** fed by DCAT + graph metadata, with filters by theme/time/region/publisher; search is driven by standardized metadata (DCAT/STAC).

---

## 📚 Registry: DCAT datasets for `<model_id>`

> [!IMPORTANT]
> This list should reflect **the exact DCAT dataset records** the model is allowed to cite.  
> If you want this to be fully accurate, **generate it from the DCAT directory** (see “Auto-generation” below) and keep the curated notes here.

### 🧱 Core dataset entries (seeded from project docs)

#### 1) `kfm.ks.landcover.2000_2020.v1` — Landcover (2000–2020)
- 🟦 DCAT: `../../../../data/catalogs/dcat/kfm.ks.landcover.2000_2020.v1.jsonld`  
- 🟩 STAC: `../../../../data/stac/collections/kfm.ks.landcover.2000_2020.v1.json`  
- 🟨 PROV: `../../../../data/prov/kfm.ks.landcover.2000_2020.v1.jsonld`  
- 📦 Distributions (expected):
  - STAC collection link (JSON)
  - Download (e.g., GeoTIFF/COG/GeoParquet)
  - API endpoint (if served) [oai_citation:17‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

#### 2) `<TBD dataset_id>` — “Kansas aerial imagery 1950s”
- 🟩 STAC motivation: STAC collections can describe imagery tiles with footprints and dates; KFM expects cross-links between STAC/DCAT/PROV for these assets. [oai_citation:18‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- 🧠 Why it matters for AI + UI: imagery tilesets are common sources for map overlays & evidence-backed narrative exports.

#### 3) `<TBD dataset_id>` — “USGS Real-time Water Data” (streaming)
- UI expects the layer legend to attribute sources using DCAT metadata (e.g., “Source: USGS NWIS”). [oai_citation:19‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- Focus Mode citations should point to the DCAT dataset record even for dynamic queries (with PROV logging of the specific reading used). [oai_citation:20‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

### 🛰️ Streaming / watcher-fed datasets

KFM’s architecture explicitly supports real-time watchers (e.g., GTFS-RT transit), generating STAC items continuously, **and** assigning a DCAT dataset entry for the feed so it’s governed like static data. [oai_citation:21‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

#### 4) `<TBD dataset_id>` — GTFS-RT transit feed watcher
- 🔁 Each poll/update becomes a STAC item; the feed itself is a DCAT dataset entry. [oai_citation:22‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- Proposed in “Latest Ideas & Future Proposals” as a roadmap item (real-time mapping that still stays cataloged). [oai_citation:23‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

### 🧪 Derived / modeled outputs (simulations, AI, analyses)

> [!NOTE]
> Simulation outputs **must be promoted** before the graph/API/UI can use them, and promotion includes emitting STAC/DCAT/PROV and stable IDs (no direct UI links to workbench outputs). [oai_citation:24‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

#### 5) `<TBD dataset_id>` — Offline “data pack” exports (curated subsets)
KFM proposes offline packs that include pre-curated datasets/tiles and a story; these are ideal DCAT distributions (downloadable bundle with explicit provenance). [oai_citation:25‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

---

## 📦 Advanced distribution patterns (OCI artifacts)

KFM’s “Additional Project Ideas” proposes treating large artifacts (PMTiles, GeoParquet, models, etc.) as **OCI artifacts** (ORAS + Cosign), and then referencing them from **STAC/DCAT** as a `distribution.oci` entry (registry/repo/tag/digest + files + media types). [oai_citation:26‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  
This supports reproducibility and verification (signed, content-addressed), and still keeps discovery in DCAT. [oai_citation:27‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

**If you adopt OCI distributions, add to each dataset entry:**
- 📦 OCI: `oci://<registry>/<repo>@<digest>` (plus file media types)
- 🔏 Signature verification: Cosign/Sigstore requirements (policy gate)

---

## 🧠 Thematic coverage hints (domain modules)

The v13 docs expect domain modules under `docs/data/<domain>/...` and encourage a consistent domain expansion pattern (examples include land treaties, air quality, soils). [oai_citation:28‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

Use these as buckets when auto-generating this file (group DCAT datasets by theme):
- 🪶 **Historical / Land Treaties** — `docs/data/historical/land-treaties/` [oai_citation:29‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- 🌫️ **Air Quality** — `docs/data/air-quality/` [oai_citation:30‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- 🧱 **Soils (SDA)** — `docs/data/soils/sda/` [oai_citation:31‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧷 Entry template (copy/paste)

<details>
<summary>📄 Click to expand dataset entry template</summary>

### `<dataset_id>` — `<Dataset Title>`
- 🟦 DCAT: `../../../../data/catalogs/dcat/<dataset_id>.jsonld`
- 🟩 STAC: `../../../../data/stac/collections/<dataset_id>.json`
- 🟨 PROV: `../../../../data/prov/<dataset_id>.jsonld`

**Distributions**
- 📦 Download: `<path or URL>`
- 🔌 API: `<endpoint>`
- 🗺️ STAC: `<collection URL/path>`

**Governance**
- 🔐 Classification: `<public|restricted|sensitive|...>`
- 🪶 Sovereignty notes (if applicable): `<CARE/TK labels / community authority / restrictions>`

**Notes**
- `<short notes, known caveats, validation rules, etc.>`

</details>

---

## 🤖 Model behavior expectations (when using these datasets)

- Focus Mode / narrative output should remain **evidence-first** and must cite cataloged sources (DCAT/STAC/PROV links), with “No unsourced narrative” enforced as a project invariant. [oai_citation:32‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  
- Any AI-generated text should be clearly identified and accompanied by provenance/confidence metadata in line with policy gates. [oai_citation:33‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- Pulse Threads / rapid narratives should still attach provenance metadata and reference dataset IDs in the graph (evidence manifests), keeping the same “drill-down to exact data” ethos. [oai_citation:34‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🔄 Auto-generation (recommended)

> [!TIP]
> The most reliable way to keep this file correct is to generate the dataset list from the DCAT directory and then maintain human notes on top.

Example (shell-only sketch):
```bash
# from repo root
find data -type f \( -path "data/catalogs/*" -o -path "data/catalog/*" \) \
  \( -name "*.jsonld" -o -name "*.ttl" \) \
  | sort
```

Then group by theme using DCAT fields (publisher/theme/keywords) as the UI expects.

---

## 📎 Source docs used (project files)

These are the project files that informed this index and its conventions:

- 📚 Data Intake pipeline & STAC/DCAT/PROV details:  [oai_citation:35‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- 🧠 AI policy gates & governance:  [oai_citation:36‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- 🖥️ UI catalog/search expectations:  [oai_citation:37‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
- 🧱 Architecture (cataloging, watchers):  [oai_citation:38‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- 🧪 “Pulse Ideas” / additional concepts (OCI artifacts, evidence manifests, conceptual nodes):  [oai_citation:39‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- 🌍 CARE / cultural protocol research and inclusive design patterns:  [oai_citation:40‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)

Other bundled “programming books / portfolios” present in the project (may need Adobe Reader to expand):
- 🧰 AI Concepts & more (PDF portfolio):  [oai_citation:41‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr) [oai_citation:42‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)
- 🗺️ Maps/GoogleMaps/Virtual Worlds/Geospatial WebGL (PDF portfolio):  [oai_citation:43‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6) [oai_citation:44‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)
- 🧑‍💻 Various programming languages & resources (PDF portfolio):  [oai_citation:45‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi) [oai_citation:46‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)
- 🧠 Data management theories & Bayesian methods (PDF portfolio):  [oai_citation:47‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

---

## ✅ TODOs for repo integration

- [ ] Replace `<TBD dataset_id>` entries with actual IDs from `data/catalogs/dcat/` (or `data/catalog/dcat/`) once the catalog files are present.
- [ ] Add a CI check that fails if any dataset listed here lacks corresponding STAC + PROV cross-links (alignment invariant). [oai_citation:48‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- [ ] Add a “Sensitive / sovereignty” badge/tag per dataset and ensure API/UI enforcement matches classification fields. [oai_citation:49‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
