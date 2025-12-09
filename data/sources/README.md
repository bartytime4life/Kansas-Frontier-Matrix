---
title: "📚 Kansas Frontier Matrix — Data Sources Layer (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/sources/README.md"

version: "v11.2.3"
last_updated: "2025-12-09"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:data-sources-readme:v11.2.3"
semantic_document_id: "kfm-doc-data-sources-layer"
event_source_id: "ledger:data/sources/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../releases/v11.2.3/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/data-sources-v11.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.5"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Guide"
intent: "data-sources-layer"
role: "source-registry"
category: "Data · Sources · Provenance · FAIR+CARE"

fair_category: "F1-A1-I1-R1"
care_label: "Variable — Provider & Dataset Dependent"
sensitivity: "Mixed"
sensitivity_level: "Dataset-level"
risk_category: "Dataset-level"
indigenous_rights_flag: "Dataset-level"
redaction_required: false
data_steward: "KFM FAIR+CARE Council"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

prov_profile: "PROV-O Plan + KFM Data Lineage Profile"
openlineage_profile: "OpenLineage v2.5 · Ingestion pipeline events"

provenance_chain:
  - "data/sources/README.md@v11.0.0"
  - "data/sources/README.md@v11.1.0"
  - "data/sources/README.md@v11.2.3"

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

machine_extractable: true
classification: "Public Document (describes source registry; referenced data may be sensitive)"
jurisdiction: "Kansas / United States"
accessibility_compliance: "WCAG 2.1 AA"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded upon next data-sources layer update"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
---

<div align="center">

# 📚 **Kansas Frontier Matrix — Data Sources Layer**  
`data/sources/README.md`

**Purpose**  
Define the **Data Sources Layer** for the Kansas Frontier Matrix (KFM): a governed registry of **upstream providers, catalogs, and agreements** that feeds the `data/raw/` and `data/work/` layers with traceable, licensed, FAIR+CARE-aligned inputs.

This layer does **not** store heavy data itself; instead it captures:

- Provider profiles & contact metadata  
- Upstream STAC/DCAT catalog references  
- Licensing & data-sharing agreements (summaries)  
- Ingestion configuration and scheduling hints  
- Provenance anchors used by PROV-O and OpenLineage  

It is the **“who/what/where/from”** of the KFM data system.

</div>

---

## 📘 Overview

The Sources layer answers:

- *Where did this dataset come from?*  
- *Under what license and conditions?*  
- *Who is the steward or authoritative provider?*  
- *Which upstream catalog or API should we re-query when refreshing?*

Conceptually:

- `data/raw/` contains **bytes** (immutable ingested data).  
- `data/sources/` contains **facts about those bytes** and how to re-obtain them.  

The layer is designed to:

- Support **reproducible ingestion** (same sources + same configs → same raw data).  
- Make **licensing and FAIR+CARE constraints explicit** at the very beginning of the pipeline.  
- Provide **graph-ready provenance** for all external data.  
- Centralize **provider-level relationships**, so a single provider change (e.g., new URL or license) can cascade safely.

---

## 🗂️ Directory Layout

The Sources layer is organized by *concept* rather than by domain:

```text
📁 data/sources/
├── 📄 README.md                     # This document (Data Sources Layer guide)
│
├── 📁 providers/                    # Provider profiles & contact metadata
│   ├── 🌊 noaa.json                 # NOAA profile (APIs, contact, license notes)
│   ├── 🗺️ usgs.json                 # USGS profile
│   ├── 🧪 kgs.json                  # Kansas Geological Survey profile
│   ├── 🏛️ nara.json                 # Archives / manuscript providers
│   ├── 🪶 tribal_partners.json      # Tribal/Indigenous stewards (metadata only; no sensitive detail)
│   └── 📁 custom/                   # Additional provider profiles (community, local archives, etc.)
│
├── 📁 catalogs/                     # Upstream catalog references (STAC/DCAT/API descriptors)
│   ├── 🛰️ noaa_stac.json           # STAC endpoints & collections for NOAA
│   ├── 🛰️ landsat_stac.json        # Landsat/USGS STAC entrypoints
│   ├── 🛰️ sentinel_stac.json       # Sentinel STAC entrypoints
│   ├── 🧾 dcat_upstream.jsonld      # External DCAT catalogs (e.g., data.gov, state portals)
│   └── 📁 custom/                   # Project-specific catalog configs (RDF/JSON/JSON-LD)
│
├── 📁 agreements/                   # Licensing & data-use agreements (summaries, not signed originals)
│   ├── 📄 noaa_license.md           # Summary of NOAA usage & attribution requirements
│   ├── 📄 usgs_license.md           # USGS license / usage conditions
│   ├── 📄 kgs_mou.md                # KGS MOU summary (non-sensitive)
│   ├── 📄 tribal_data_principles.md # High-level principles for Indigenous/tribal data partnerships
│   └── 📁 restricted/               # Redacted summaries for more sensitive agreements
│
└── 📁 ingestion/                    # Ingestion & harvest configuration
    ├── 🧩 pipelines.yml             # Mapping of source → ingest pipeline (IDs, frequencies)
    ├── 🧾 schedules.yml             # Cron-like hints for `kfm-auto-update.yml`
    ├── ⚙️ params/                   # Per-source parameter sets (e.g., bounding boxes, time ranges)
    └── 🧾 mapping/                  # Field/semantic mappings (upstream → KFM schemas)
```

**Normative rules:**

- **Provider profiles** (`providers/*.json`) are the **single source of truth** for a provider’s canonical name, URLs, and fundamental metadata.  
- Any ingestion config in `ingestion/` MUST reference providers via their profile IDs, not inline names.  
- Agreements documents in `agreements/`:
  - MAY include high-level terms and obligations,  
  - MUST NOT include confidential contractual details, signatures, or PII.

---

## 🌐 Provider Profiles

Provider profiles under `providers/` are **small, strongly typed JSON documents** that capture:

- Provider ID (e.g., `"noaa"`), official name, and description.  
- Primary and backup API/base URLs.  
- Contact email or URL for questions.  
- Declared license(s) and links to authoritative license text.  
- Default FAIR/CARE characteristics (e.g., public US federal data vs. community-governed data).  
- Jurisdiction & governance notes (e.g., tribally governed, US federal, etc.).

Example (abbreviated):

```json
{
  "id": "noaa",
  "name": "National Oceanic and Atmospheric Administration",
  "kind": "federal_agency",
  "homepage": "https://www.noaa.gov/",
  "apis": [
    {
      "id": "noaa-climate-data",
      "url": "https://www.ncei.noaa.gov/access/services/data/v1",
      "description": "NOAA Climate Data Online API"
    }
  ],
  "default_license": "U.S. Government Work",
  "fair_category": "F1-A1-I1-R1",
  "care_label": "Public · Low-Risk",
  "jurisdiction": "United States",
  "sovereignty_flag": false
}
```

Provider profiles are referenced by:

- `data/raw/` ingestion pipelines,  
- STAC/DCAT metadata (as `dct:creator`, `dct:publisher`, or `kfm:upstreamProvider`),  
- Graph nodes representing organizations or custodians.

---

## 🧾 Catalog References (STAC / DCAT / APIs)

Catalog descriptors under `catalogs/` describe **how to discover actual assets** at a given source:

- STAC entrypoints, root catalogs, and collection names.  
- DCAT catalogs and “landing pages” for external registries.  
- API endpoints that are catalog-like (even if not STAC/DCAT), including:
  - Parameterization (time ranges, bounding boxes, dataset IDs),  
  - Rate limits and pagination behavior.

Typical fields for STAC descriptors:

- `stac_root_url` — HTTP(S) URL of the root STAC catalog.  
- `collections` — list of important collection IDs.  
- `license_overrides` — any divergence from provider-level default license.  
- `default_spatial_filter` / `default_temporal_filter` — KFM’s typical fetch window for Kansas.

These descriptors allow ingestion scripts (e.g., `src/pipelines/ingest_stac.py`) to:

- Dynamically crawl new upstream items,  
- Filter by time/space,  
- Respect rate limits and provider guidance.

---

## 🤝 Agreements & Sovereignty

`agreements/` contains **human-readable summaries** of licensing and data-sharing terms:

- For public federal sources (e.g., NOAA/USGS), this often is a short explanation plus links to official terms.  
- For state, tribal, or local partners, it may summarize:
  - Data ownership and custodianship,  
  - Sharing and redistribution constraints,  
  - Required acknowledgements,  
  - Any “do not expose” rules for sensitive layers.

Cultural and Indigenous data:

- `tribal_data_principles.md` and related documents:
  - Distill key principles from the sovereignty policy and specific MOUs,  
  - Guide ingestion and downstream usage of culturally sensitive data in KFM.  
- Dataset-specific constraints are then reflected:
  - In STAC/DCAT metadata (CARE labels, `sovereignty_flag`),  
  - In Work/Processed layer flags and masking rules.

Sensitive details:

- The **actual legal documents** typically live outside the repo.  
- `agreements/restricted/` may contain **redacted** or high-level overviews when full details cannot be public.

---

## 🔄 Ingestion & Refresh Configuration

The `ingestion/` subdirectory defines **how upstream sources are harvested**:

- `pipelines.yml`
  - Maps provider IDs → pipeline IDs (e.g., `noaa-precip-v1` → `src/pipelines/hydro/noaa_precip.py`).  
  - Records expected **domain** (`hydrology`, `climate`, `hazards`, etc.) and **target** raw directory.

- `schedules.yml`
  - Provides hints for `kfm-auto-update.yml` on how often to refresh:
    - e.g., daily climate feeds; monthly archive updates; yearly static dataset checks.

- `params/`
  - Contains YAML/JSON parameter sets per **source + pipeline + environment**:
    - Spatial extents (Kansas bounding boxes, HUCs),  
    - Temporal windows (e.g., last year, entire record),  
    - Filter values (e.g., particular stations or collections).

- `mapping/`
  - Defines field-level mappings from upstream schemas → KFM canonical schemas:
    - E.g., `PRCP` → `precip_mm`, `TMAX` → `temp_max_c`, etc.  
  - These mappings are referenced by ETL contracts in `docs/contracts/` and by Work layer transforms.

This folder is where **ingestion becomes config-driven** rather than ad-hoc scripts.

---

## 🧬 Provenance & Lineage Integration

Sources layer artifacts are primarily used to **anchor provenance**:

- Provider profiles → `prov:Agent` nodes.  
- Catalog descriptors → `prov:Entity` representing upstream catalogs.  
- Ingestion config → `prov:Plan` or `prov:Activity` templates.

During an ingestion run:

- The pipeline uses:
  - Provider profile → attaches as `prov:wasAttributedTo`,  
  - Catalog descriptor → attaches as `prov:wasDerivedFrom`,  
  - Ingestion params → hashed into a `config_fingerprint_sha256`.

- The resulting raw assets in `data/raw/`:
  - Carry references to:
    - Provider ID,  
    - Catalog descriptor version,  
    - Ingestion config fingerprint and timestamp.

Combined with OpenLineage events, this allows answering:

> *“Given this raw/processed dataset, exactly which upstream provider, catalog version, and parameters were used to fetch it?”*

---

## ⚖ FAIR+CARE & Sources

FAIR+CARE is **enforced from the sources layer forward**:

- Each provider profile encodes **default FAIR/CARE assumptions**:
  - Public federal open data vs. restricted community data,  
  - Baseline licenses vs. dataset-specific overrides.

- Agreements documents:
  - Clarify **reuse constraints** and **attribution requirements**.  
  - Inform STAC/DCAT metadata and API exposure rules.

- Ingestion configs for sensitive sources:
  - May include mandatory H3 generalization at or before Work layer,  
  - May prohibit including exact point locations in public products,  
  - May route new data through additional FAIR+CARE review before enabling any publication.

The Sources layer thus acts as the **first governance checkpoint** before bytes even land in `data/raw/`.

---

## 🧭 Contributor Workflow

When adding or updating a source:

1. **Create or update provider profile**
   - Add a JSON file under `providers/` (or update an existing one).  
   - Include: IDs, URLs, license, FAIR+CARE defaults, and governance notes.

2. **Add catalog descriptor(s)**
   - For STAC/DCAT/API-driven sources, create/extend files in `catalogs/`.  
   - Record any KFM-specific filtering rules.

3. **Add or refine agreement summaries**
   - Update `agreements/` with high-level license/MOU notes.  
   - Coordinate with governance/FAIR+CARE stewards for sensitive or Indigenous data.

4. **Wire ingestion configuration**
   - Map provider → pipeline in `ingestion/pipelines.yml`.  
   - Add schedules in `ingestion/schedules.yml`.  
   - Add parameter sets in `ingestion/params/` as needed.  
   - Update field mappings under `ingestion/mapping/`.

5. **Run checks (if available)**
   - Use local scripts or CI equivalents to ensure:
     - JSON schema validity for provider/catalog files,  
     - No obvious license or governance inconsistencies.

6. **Open a PR**
   - Describe:
     - New sources,  
     - Expected raw targets (`data/raw/**`),  
     - Governance/FAIR+CARE considerations.  
   - Expect review from:
     - Data architecture,  
     - FAIR+CARE Council / sovereignty stewards (when relevant).

---

## 🕰️ Version History

| Version | Date       | Author       | Summary                                                                                               |
|--------:|------------|--------------|-------------------------------------------------------------------------------------------------------|
| v11.2.3 | 2025-12-09 | `@kfm-data`  | Aligned with data/README & ARCHITECTURE; defined providers/catalogs/agreements/ingestion layout; clarified FAIR+CARE & provenance roles. |
| v11.1.0 | 2025-11-19 | `@kfm-data`  | Introduced structured provider profiles and ingestion configs; added FAIR+CARE-aware agreements area. |
| v11.0.0 | 2025-11-15 | `@kfm-data`  | Initial v11 data sources layer documentation; basic provider and catalog description structure.      |

---

<div align="center">

📚 **Kansas Frontier Matrix — Data Sources Layer (v11.2.3)**  
Source-First · FAIR+CARE-Governed · Provenance-Anchored  

[⬅️ Back to Data Overview](../README.md) ·  
[🗄️ Data System Architecture](../ARCHITECTURE.md) ·  
[🏗️ Repository Architecture](../../ARCHITECTURE.md) ·  
[⚖️ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>