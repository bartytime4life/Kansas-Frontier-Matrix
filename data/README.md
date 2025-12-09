---
title: "📦 Kansas Frontier Matrix — Data Directory Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/README.md"

version: "v11.2.3"
last_updated: "2025-12-09"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:data-readme:v11.2.3"
semantic_document_id: "kfm-doc-data-root"
event_source_id: "ledger:data/README.md"
immutability_status: "version-pinned"

sbom_ref: "../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../releases/v11.2.3/manifest.zip"
telemetry_ref: "../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../schemas/telemetry/data-directory-v11.2.3.json"
energy_schema: "../schemas/telemetry/energy-v2.json"
carbon_schema: "../schemas/telemetry/carbon-v2.json"

governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.5"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Overview"
intent: "data-directory"
role: "repository-data-overview"
category: "Data · Metadata · FAIR+CARE"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "Mixed"
sensitivity_level: "Variable"
risk_category: "Low to Medium"
indigenous_rights_flag: false
redaction_required: false

machine_extractable: true
classification: "Public Document"
jurisdiction: "United States / Kansas"
accessibility_compliance: "WCAG 2.1 AA"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

prov_profile: "PROV-O Plan + KFM Data Lineage Profile"
openlineage_profile: "OpenLineage v2.5 · Data & ETL pipeline events"

provenance_chain:
  - "data/README.md@v11.0.0"
  - "data/README.md@v11.0.1"
  - "data/README.md@v11.2.2"
  - "data/README.md@v11.2.3"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "metadata-extraction"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-historical-claims"
  - "governance-override"
  - "hallucinated-datasets"
---

<div align="center">

# 📦 **Kansas Frontier Matrix — Data Directory Overview (v11.2.3)**  
`data/README.md`

**Purpose**  
Define the **canonical structure, lifecycle, and governance** of all datasets in the Kansas Frontier Matrix (KFM), from raw external sources to fully validated, cataloged, graph‑integrated, and Story‑Node‑ready products. This document ties the data layout directly to **STAC/DCAT catalogs, PROV‑O lineage, DVC/Git versioning, and KFM‑MDP v11.2.5**. 

[![KFM-MDP v11.2.5](https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.5-blue)](../docs/standards/kfm_markdown_protocol_v11.2.5.md)
[![FAIR+CARE](https://img.shields.io/badge/Data-FAIR%2BCARE-gold)](../docs/standards/faircare/FAIRCARE-GUIDE.md)
[![STAC/DCAT](https://img.shields.io/badge/Metadata-STAC_1.0.0_%7C_DCAT_3.0-informational)]()
[![Provenance](https://img.shields.io/badge/Lineage-PROV%E2%80%93O_%7C_OpenLineage-success)]()
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY_4.0-green)](../LICENSE)

</div>

---

## 📘 Overview

The `data/` directory is the **root of the KFM data plane**:

- Implements the repository‑wide lifecycle **raw → work → processed → releases** described in the canonical repo layout.  [oai_citation:0‡Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2.5".pdf](file-service://file-MM5cKccJmejjcqM7A3mUYq)  
- Anchors KFM’s **multi‑layered metadata strategy**:
  - Human‑readable READMEs and docs,
  - Machine‑readable STAC/DCAT catalogs,
  - PROV‑O lineage and OpenLineage execution traces.  [oai_citation:1‡Kansas Frontier Matrix Documentation.pdf](file-service://file-Kh5A494Gau4gS5ihmMLDuS)  
- Provides the source of truth for all **map layers, time‑sliced Story Nodes, Focus Mode narratives, and Neo4j graph facts**.
- Integrates with **Git + DVC/LFS** so that large rasters, vector tiles, and graph dumps are versioned without bloating the Git repo.  [oai_citation:2‡Kansas Frontier Matrix Documentation.pdf](file-service://file-Kh5A494Gau4gS5ihmMLDuS)  

Conceptually, `data/` is where:

- **External sources** are registered and frozen as raw assets (`sources/`, `raw/`),
- **ETL pipelines** normalize and enrich data (`work/`),
- **Analysis‑ready products** land (`processed/`),
- **Catalogs & provenance** expose them to the rest of the stack (`stac/`, `dcat/`, checksums, reports),
- CI/CD workflows enforce **schema, FAIR+CARE, sovereignty, and integrity** before anything ships to production.  [oai_citation:3‡Comprehensive CI_CD Guide for Software and Data Projects.pdf](file-service://file-DTBXPu2GMyqSAix4wesN9A)  

---

## 🗂️ Directory Layout

Canonical, emoji‑rich layout for `data/` (KFM‑MDP `immediate-one-branch-with-descriptions-and-emojis` profile).   

~~~text
📁 data/
├── 📄 README.md                      # This file (data directory overview & governance)
│
├── 📁 sources/                       # External dataset manifests & source metadata (STAC/DCAT-aligned)
│   ├── 📁 providers/                 # Provider profiles (KGS, USGS, NOAA, tribal partners, etc.)
│   ├── 📁 catalogs/                  # Upstream STAC/DCAT links & harvested descriptors
│   └── 📁 agreements/                # Licensing, MOUs, data-use agreements (non-sensitive summaries)
│
├── 📁 raw/                           # Unmodified source datasets (immutable; versioned via DVC/LFS)
│   ├── 📁 historic/                  # Scanned maps, manuscripts, diaries, archival scans
│   ├── 📁 environmental/             # NOAA, PRISM, Daymet, USGS, Mesonet, AQS, etc.
│   ├── 📁 cultural/                  # Tribal/Indigenous/heritage data (subject to sovereignty rules)
│   ├── 📁 geology/                   # DEMs, lithology, KGS datasets
│   └── 📁 admin/                     # Counties, municipalities, parcels, HUCs, etc.
│
├── 📁 work/                          # Normalized & enriched intermediates (pipeline workspace)
│   ├── 📁 tables/                    # Cleaned tabular data (CSV, Parquet)
│   ├── 📁 spatial/                   # GeoJSON, GPKG, intermediate rasters/COGs
│   └── 📁 metadata/                  # Pre-STAC/DCAT drafts, schema snapshots
│
├── 📁 processed/                     # Deterministic ETL outputs, analysis-ready
│   ├── 📁 hydrology/                 # Streamflow, flood history, watersheds, indices
│   ├── 📁 climate/                   # Climate normals, anomalies, extremes
│   ├── 📁 ecology/                   # Vegetation, biodiversity, habitat indices
│   ├── 📁 historical/                # Generalized historical event/layer datasets
│   └── 📁 hazards/                   # Tornado, drought, flood, wildfire, severe weather
│
├── 📁 stac/                          # STAC 1.x Items/Collections & catalog root (KFM-STAC v11)
│   ├── 📄 README.md                  # STAC catalog overview (profile, conventions)
│   ├── 🧾 catalog.json               # STAC root catalog
│   ├── 📁 missions/                  # EO missions (Landsat, Sentinel, NAIP, SWOT, etc.)
│   ├── 📁 hydrology/                 # Hydrology STAC Collections/Items
│   ├── 📁 climate/                   # Climate STAC domain
│   ├── 📁 hazards/                   # Hazards STAC domain
│   ├── 📁 landcover/                 # Land cover / land use Collections
│   └── 📁 tabular/                   # Tabular/non-spatial STAC items (CSV/Parquet)
│
├── 📁 dcat/                          # DCAT 3.0 catalogs (JSON-LD)
│   ├── 🧾 catalog.jsonld             # Root DCAT catalog (datasets + distributions)
│   └── 📁 datasets/                  # Individual DCAT dataset records (JSON-LD)
│
├── 📁 checksums/                     # SHA-256 lineage verification (Git/DVC-aligned)
│   ├── 🧾 raw/                       # Checksums for raw assets
│   ├── 🧾 processed/                 # Checksums for processed datasets
│   └── 🧾 stac/                      # Checksums for catalog JSONs
│
├── 📁 reports/                       # Validation, FAIR+CARE, and audit outputs
│   ├── 🧾 self-validation/           # Schema/STAC/DCAT/provenance & CARE reports
│   ├── 🧾 telemetry/                 # Data pipeline energy/carbon & performance telemetry
│   └── 🧾 audit/                     # Governance & external audit reports
│
├── 📁 archive/                       # Versioned snapshots & retired datasets (cold storage)
│   └── 📁 <year>/                    # Archived by year / major release
│
└── 📁 tmp/                           # Scratch space (ignored by CI; must not feed production)
~~~

**Normative rules (data/ level):**

- Any documented subdirectory under `data/` **MUST** have its own `README.md` describing purpose, ownership, and key files.  [oai_citation:4‡Kansas Frontier Matrix — Markdown Authoring Protocol (KFM-MDP) v11.2.5".pdf](file-service://file-MM5cKccJmejjcqM7A3mUYq)  
- New domain areas (e.g., `data/processed/<new-domain>/`) MUST:
  - Be added to this tree and to relevant catalogs (`stac/`, `dcat/`),
  - Be governed by FAIR+CARE and sovereignty rules before public exposure.  [oai_citation:5‡Kansas Frontier Matrix Documentation.pdf](file-service://file-Kh5A494Gau4gS5ihmMLDuS)  

---

## 📊 Data Lifecycle & Lineage

KFM’s data lifecycle is a **governed pipeline** that aligns with both MCP and data‑centric CI/CD practices.  [oai_citation:6‡Comprehensive CI_CD Guide for Software and Data Projects.pdf](file-service://file-DTBXPu2GMyqSAix4wesN9A)  

~~~mermaid
flowchart TD
  A["📁 sources/\nProvider manifests & upstream catalogs"]
    --> B["📁 raw/\nImmutable ingests (Git+DVC/LFS)"]

  B --> C["📁 work/\nCleaning · normalization · enrichment"]
  C --> D["📁 processed/\nDeterministic ETL outputs"]

  D --> E["📁 stac/\nSTAC Items & Collections"]
  D --> F["📁 dcat/\nDCAT Datasets & Distributions"]

  E --> G["📁 checksums/\nSHA-256 digests (raw/processed/stac)"]
  F --> G

  G --> H["📁 reports/self-validation/\nSchema · FAIR+CARE · provenance"]
  H --> I["📁 reports/telemetry/\nEnergy · carbon · dataops metrics"]
~~~

Key properties:

1. **Raw is immutable & reconstructable**  
   - `raw/` holds source files as‑received (or losslessly re‑encoded), with provenance recorded in `sources/` and DCAT/STAC metadata.  [oai_citation:7‡Kansas Frontier Matrix Documentation.pdf](file-service://file-Kh5A494Gau4gS5ihmMLDuS)  
   - Large assets are referenced via DVC/LFS, ensuring **data/code lockstep versioning** across Git commits and releases.  [oai_citation:8‡Kansas Frontier Matrix Documentation.pdf](file-service://file-Kh5A494Gau4gS5ihmMLDuS)  

2. **Work is transient but governed**  
   - `work/` contains intermediate artifacts used during ETL.  
   - Pipelines either clean up or DVC‑track these intermediates where they are needed for reproducibility.

3. **Processed is deterministic**  
   - `processed/` datasets are considered **production‑grade** and must be:
     - Generated by scripted, config‑driven pipelines,
     - Regenerable from `raw/` + configs + containerized environments,  
     - Tested via data validation checks (schema, value ranges, CRS, geometry validity).  [oai_citation:9‡Comprehensive CI_CD Guide for Software and Data Projects.pdf](file-service://file-DTBXPu2GMyqSAix4wesN9A)  

4. **Catalogs are the public metadata face**  
   - Every production dataset should appear as:
     - A STAC Item (and usually part of a STAC Collection), and
     - A DCAT Dataset with one or more Distributions.   

5. **Lineage is explicit and queryable**  
   - PROV‑O records and OpenLineage events relate raw → work → processed → catalogs as Entities and Activities with Agents (pipelines, maintainers).  [oai_citation:10‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  
   - Checksums and DVC state provide **tamper‑evident integrity** for every major artifact.  [oai_citation:11‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  

---

## 🧪 Validation & Compliance

Data cannot move from `raw/` into `processed/` and catalogs without passing a **stack of validation gates**, many of which are enforced in CI (e.g., `stac_validate.yml`, `dcat_validate.yml`, `data_pipeline.yml`).   

### 1. Schema & Structural Checks

- Field‑level schema validation (JSON Schema, SHACL, Great Expectations or equivalent) for:
  - Column names & types,
  - Allowed value ranges,
  - Missing value policies.  [oai_citation:12‡Comprehensive CI_CD Guide for Software and Data Projects.pdf](file-service://file-DTBXPu2GMyqSAix4wesN9A)  
- Geospatial validity:
  - `geometry` and `bbox` consistency,
  - Valid CRS (WGS84 / EPSG:4326 by default unless explicitly documented),
  - No invalid polygons or self‑intersections.  [oai_citation:13‡Comprehensive CI_CD Guide for Software and Data Projects.pdf](file-service://file-DTBXPu2GMyqSAix4wesN9A)  

### 2. FAIR+CARE & Sovereignty

- Datasets touching cultural heritage, Indigenous lands, or sensitive ecology:
  - MUST include **CARE labels**, sovereignty flags, and governance references in metadata.   
  - MUST be **generalized (e.g., H3)** or masked when public precision could pose risk.
- FAIR criteria:
  - **Findable** via STAC/DCAT and consistent identifiers,
  - **Accessible** via documented distributions or access notes,
  - **Interoperable** via standardized schemas and ontologies,
  - **Reusable** via clear licensing and provenance.  [oai_citation:14‡Kansas Frontier Matrix Documentation.pdf](file-service://file-Kh5A494Gau4gS5ihmMLDuS)  

### 3. Integrity & Provenance

- SHA‑256 checksums in `data/checksums/`:
  - Cross‑checked with release `manifest.zip` and `sbom.spdx.json`.  [oai_citation:15‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  
- DVC or equivalent ensures **historical versions** of large data remain retrievable per KFM/MCP reproducibility requirements.  [oai_citation:16‡Kansas Frontier Matrix Documentation.pdf](file-service://file-Kh5A494Gau4gS5ihmMLDuS)  

### 4. Sustainability & Telemetry

For significant ETL runs or bulk updates:

- Pipelines SHOULD record:
  - `energy_wh`, `carbon_gco2e`,
  - `records_processed`, `compute_time_s`.  [oai_citation:17‡Comprehensive CI_CD Guide for Software and Data Projects.pdf](file-service://file-DTBXPu2GMyqSAix4wesN9A)  
- Summaries are written under:
  - `data/reports/telemetry/`,
  - `releases/<version>/focus-telemetry.json`, referenced by this document’s `telemetry_ref`.

---

## 🧬 STAC / DCAT / PROV Integration

KFM’s data catalogs are intentionally **redundant but harmonized**: STAC, DCAT, and PROV‑O all describe the same assets from different angles.   

### STAC (SpatioTemporal Asset Catalog)

- `data/stac/` contains:
  - `catalog.json` as the STAC root,
  - Collections per domain (e.g., climate, hydrology, hazards),
  - Items pointing to **processed** assets (COGs, GeoJSON, Parquet, etc.).  [oai_citation:18‡OGC STAC Community Standard — Complete Overview (for KFM Integration).pdf](file-service://file-3Df7ewr7kx4gHofoTxybDg)  
- Validation via `stac-validate` composite action and workflow:
  - Ensures STAC spec compliance and KFM‑STAC profile rules (extensions, IDs, asset roles).
  - Stores validation reports in `data/reports/self-validation/`.  [oai_citation:19‡OGC STAC Community Standard — Complete Overview (for KFM Integration).pdf](file-service://file-3Df7ewr7kx4gHofoTxybDg)  

### DCAT (Data Catalog Vocabulary)

- `data/dcat/` holds:
  - `catalog.jsonld` (root DCAT catalog),
  - One JSON‑LD record per dataset under `datasets/`.  [oai_citation:20‡Data Catalog Vocabulary (DCAT) – Comprehensive Implementation Guide.pdf](file-service://file-GQAFs8RmTMXLbNtf2vDtE8)  
- DCAT records:
  - Mirror STAC `id` and `kfm_id` fields as `dct:identifier`,
  - Reference STAC assets as `dcat:distribution` entries,
  - Attach licensing and access constraints explicitly.

### PROV‑O & OpenLineage

- PROV‑O:
  - Each dataset is a `prov:Entity`,
  - ETL steps are `prov:Activity` instances,
  - People and automation agents are `prov:Agent`.  [oai_citation:21‡Comprehensive Guide to W3C PROV-O.pdf](file-service://file-M7Pfz7uE2cTVgom8q9d8B3)  
- OpenLineage:
  - CI/CD and ETL jobs emit run‑level events capturing inputs, outputs, and run metadata (including energy/carbon where available).
  - These events complement PROV‑O documents and allow time‑ordered reconstruction of pipeline runs.

Together, these layers ensure that **every layer, map tile, and Story Node is backed by verifiable, queryable lineage.**  [oai_citation:22‡Kansas Frontier Matrix Documentation.pdf](file-service://file-Kh5A494Gau4gS5ihmMLDuS)  

---

## 🧠 Contributor Guidance (Data)

When adding or modifying data in KFM:

1. **Pick the correct home**

   - New source?  
     - Add a manifest under `data/sources/` and place raw assets (or DVC pointers) under `data/raw/<domain>/`.
   - New intermediate transformation?  
     - Materialize into `data/work/` and document in pipeline configs.
   - New analysis‑ready layer?  
     - Land it in `data/processed/<domain>/` and plan STAC/DCAT entries.

2. **Register provenance**

   - Record:
     - Source URLs or archival references,
     - Processing notes (tools, parameters, uncertainty),  
     - Any generalization or masking applied.  [oai_citation:23‡Kansas Frontier Matrix Documentation.pdf](file-service://file-Kh5A494Gau4gS5ihmMLDuS)  
   - For large data, ensure DVC is configured and **linked to the same Git commit** as code changes.  [oai_citation:24‡Kansas Frontier Matrix Documentation.pdf](file-service://file-Kh5A494Gau4gS5ihmMLDuS)  

3. **Create or update catalog entries**

   - STAC:
     - Add or extend Collections under `data/stac/<domain>/`,
     - Create Items referencing `processed/` assets with correct `bbox`, `geometry`, `datetime`, and `assets`.  [oai_citation:25‡OGC STAC Community Standard — Complete Overview (for KFM Integration).pdf](file-service://file-3Df7ewr7kx4gHofoTxybDg)  
   - DCAT:
     - Add a Dataset record in `data/dcat/datasets/`,
     - Ensure distributions point to STAC assets or equivalent URLs.  [oai_citation:26‡Data Catalog Vocabulary (DCAT) – Comprehensive Implementation Guide.pdf](file-service://file-GQAFs8RmTMXLbNtf2vDtE8)  

4. **Respect FAIR+CARE & sovereignty**

   - Consult:
     - `../docs/standards/faircare/FAIRCARE-GUIDE.md`,
     - `../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`.  
   - For sensitive data:
     - Apply spatial generalization (e.g., H3) before committing,
     - Coordinate with FAIR+CARE stewards when in doubt.  [oai_citation:27‡Kansas Frontier Matrix Documentation.pdf](file-service://file-Kh5A494Gau4gS5ihmMLDuS)  

5. **Run validations locally (where possible)**

   Typical sequence (mirroring CI checks):

   ~~~bash
   # From repo root (examples; actual scripts may differ)
   python scripts/validate_pipelines.py
   bash .github/actions/stac-validate/entrypoint.sh data/stac
   bash .github/actions/dcat-validate/entrypoint.sh
   python scripts/run_faircare_checks.py
   python scripts/h3_masking_check.py
   ~~~

   See `.github/workflows/data_pipeline.yml`, `stac_validate.yml`, and `dcat_validate.yml` for the authoritative CI equivalents.

6. **Open a data issue or PR**

   - Use the data‑specific issue template (e.g., `data_issue.md` under `.github/ISSUE_TEMPLATE/`) to:
     - Describe the dataset and its purpose,
     - Provide provenance and licensing,
     - Flag any FAIR+CARE or sovereignty considerations.

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                                                         |
|--------:|------------|---------------------------------------------------------------------------------------------------------------------------------|
| v11.2.3 | 2025-12-09 | Aligned with KFM-MDP v11.2.5; expanded directory layout to match repo-wide standard; integrated STAC/DCAT/PROV & DVC semantics; updated telemetry schema and governance metadata. |
| v11.2.2 | 2025-11-27 | Canonical directory layout; telemetry/schema paths wired; FAIR+CARE and checksum governance hardened.                           |
| v11.0.1 | 2025-11-19 | Rewritten with v11 fence rules; GitHub-safe layout; aligned initial data architecture with v11 stack.                           |
| v11.0.0 | 2025-11-19 | Initial v11 dataset directory documentation and lifecycle definition.                                                          |

---

<div align="center">

📦 **Kansas Frontier Matrix — Data Directory Overview (v11.2.3)**  
Data‑First · FAIR+CARE‑Governed · Provenance‑Aware  

© 2025 Kansas Frontier Matrix — CC‑BY 4.0  
MCP‑DL v6.3 · KFM‑MDP v11.2.5 · KFM‑OP v11.0  

[⬅ Back to Repository Root](../README.md) ·  
[📚 Data & Catalog Standards](../docs/data/README.md) ·  
[⚖ Governance Charter](../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>