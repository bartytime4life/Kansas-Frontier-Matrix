---
title: "📥 Kansas Frontier Matrix — Raw Data Layer (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/raw/README.md"

version: "v11.0.0"
last_updated: "2025-11-19"
release_stage: "Stable / Governed"
review_cycle: "Continuous · FAIR+CARE Council Oversight"
lifecycle: "Long-Term Support (LTS)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:data-raw-layer-v11.0.0"
semantic_document_id: "kfm-doc-data-raw-readme"
event_source_id: "ledger:data/raw/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.0.0/manifest.zip"
data_contract_ref: "../../docs/contracts/data-contract-v3.json"

telemetry_ref: "../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/data-raw-v11.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "Open Data Commons / FAIR+CARE License"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Domain Architecture"
intent: "raw-data-layer"
role: "raw-domain"
category: "Data · Raw · FAIR+CARE · Provenance"

fair_category: "F1-A1-I1-R1"
care_label: "Mixed — varies by source and domain"
sensitivity_level: "Dataset-dependent"
indigenous_rights_flag: "Dataset-dependent"
public_exposure_risk: "Dataset-dependent"
redaction_required: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Mixed"

ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../schemas/json/data-raw-readme-v11.schema.json"
shape_schema_ref: "../../schemas/shacl/data-raw-readme-v11-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "speculative"
  - "unverified historical claims"

machine_extractable: true
classification: "Public / Mixed Sensitivity"
jurisdiction: "Kansas / United States"
accessibility_compliance: "WCAG 2.1 AA"
ttl_policy: "Permanent"
sunset_policy: "Superseded upon next raw-layer architecture update"
---

<div align="center">

# 📥 Kansas Frontier Matrix — **Raw Data Layer**  
`data/raw/README.md`

**Purpose**  
Immutable repository of **unaltered, source-level datasets** collected from verified public, academic, tribal, and governmental providers.  

The Raw Data Layer is the **foundation of KFM**, enabling:

- Transparent ingestion pipelines  
- Strong provenance and checksum validation  
- FAIR+CARE pre-audits and governance tracking  
- Ethical and sovereign data handling from first contact  

</div>

---

## 1. 📘 Overview

The **Raw Data Layer** preserves all source datasets in their **original formats**, together with:

- 🌐 Source metadata (who / what / where / when / how)  
- ⚖️ FAIR+CARE pre-audit and licensing checks  
- 🔐 SHA-256 checksums and integrity manifests  
- 🧬 PROV-O and ISO 19115-compatible provenance  

Raw data is **never modified** — any cleaning or transformation occurs downstream in `data/staging/` and beyond.  

---

## 2. 🗂️ Directory Layout (GitHub-Safe)

~~~~text
data/raw/
├── README.md
│
├── climate/          ← NOAA, NIDIS, CPC; temperature / precip / drought
├── hazards/          ← FEMA, USGS, NOAA; floods / tornadoes / droughts
├── hydrology/        ← USGS streamflow, aquifer, watershed datasets
├── landcover/        ← MODIS/VIIRS, Landsat, NLCD; vegetation classification
├── tabular/          ← historical, census, administrative records
├── terrain/          ← DEMs, slope, elevation rasters
├── text/             ← OCR-scanned documents, archival texts, reports
└── metadata/         ← source provenance, checksums, data contracts, FAIR+CARE pre-audits
~~~~

Each domain subfolder may include its own `README.md` describing source conventions.

---

## 3. 🔄 Data Acquisition Workflow

~~~~mermaid
flowchart TD
    SRC["External Sources\n(NOAA · USGS · FEMA · NASA · Archives · Tribal/State)"]
      --> ING["Automated Ingestion\n(ETL jobs, scripts, or manual drops)"]

    ING --> PRE["FAIR+CARE Pre-Audit\n(ethics · licensing · sovereignty)"]
    PRE --> REG["Checksum & Provenance Registration\n(data/raw/metadata/*)"]
    REG --> PROMO["Promotion to Staging\n(data/staging/*)"]
~~~~

### 3.1 Steps

1. **Acquisition**  
   - Fetch via API/FTP/download/drive imports.  
   - Capture **license** and **terms of use** from source.  

2. **Verification**  
   - Verify vendor checksums and signatures where available.  
   - Compute internal SHA-256 checksums for all raw files.  

3. **FAIR+CARE Pre-Audit**  
   - Record sensitivity, licensing nuances, and consent or use restrictions.  
   - Tag Indigenous or culturally sensitive sources.  

4. **Registration**  
   - Write provenance entries in `data/raw/metadata/provenance.json`.  
   - Update governance ledger with acquisition events and reviewers.  

5. **Promotion**  
   - Copy unaltered files into `data/staging/` for normalization and ETL.  

---

## 4. 🧩 Example Source Metadata Record (JSON)

~~~~json
{
  "id": "noaa_temperature_1900_2025_raw",
  "domain": "climate",
  "source_url": "https://www.ncdc.noaa.gov/cdo-web/",
  "provider": "NOAA National Centers for Environmental Information",
  "license": "Public Domain",
  "records_fetched": 125480,
  "schema_version": "v3.1.0",
  "checksum_sha256": "sha256:aaf87123e5c16bcae094a9c71e2d93b09c29a38cf7d5b1e07c187a9127f84a53",
  "fetched_on": "2025-11-12T19:22:00Z",
  "validator": "@kfm-etl-ops",
  "faircare_preaudit": {
    "sensitivity": "none",
    "license_review": "ok",
    "community_flags": [],
    "consent_token": null
  },
  "governance_ref": "docs/reports/audit/data_provenance_ledger.json"
}
~~~~

---

## 5. ⚖️ FAIR+CARE Source Governance Matrix

| Principle            | Implementation                                                     | Oversight              |
|----------------------|--------------------------------------------------------------------|------------------------|
| 🧭 **Findable**      | STAC/DCAT index of raw sources in `data/raw/metadata/` (JSON-LD). | `@kfm-data`            |
| 🔓 **Accessible**    | Original licensing preserved; access notes stored verbatim.        | `@kfm-accessibility`   |
| 🔗 **Interoperable** | Native formats (CSV, GeoTIFF, NetCDF, JSON) with metadata crosswalks. | `@kfm-architecture` |
| 🔁 **Reusable**      | Complete source notes, schema refs, license & consent.             | `@kfm-design`          |
| 🤝 **Collective Benefit** | Supports transparent, equitable science & planning.          | `@faircare-council`    |
| 🛡️ **Authority**     | Council validates ethics, attribution, and consent where needed.   | `@kfm-governance`      |
| 📋 **Responsibility**| Ingestion logs + checksums recorded & reviewed.                    | `@kfm-security`        |
| 🧠 **Ethics**        | Restricted or sensitive content quarantined and flagged.           | `@kfm-ethics`          |

Governance logs:

~~~~text
docs/reports/audit/data_provenance_ledger.json
docs/reports/fair/data_care_assessment.json
~~~~

---

## 6. 🔐 Data Integrity Verification

### 6.1 Checksum Records

Checksums for raw files are stored in:

~~~~text
data/raw/metadata/checksums.json
data/checksums/manifest.json
~~~~

Each entry includes:

- `file` — relative path to raw file  
- `checksum_sha256` — `sha256-...` format  
- `validated` — boolean  
- `verified_on` — timestamp  
- `source_ref` — human-readable description of upstream source  

### 6.2 Provenance Logging

Source-level provenance stored in:

~~~~text
data/raw/metadata/provenance.json
~~~~

And mirrored into:

~~~~text
docs/reports/audit/data_provenance_ledger.json
~~~~

---

## 7. 🧠 Raw Layer’s Role in the Data System

The raw layer is the **trust anchor** for:

- All ETL pipelines under `src/pipelines/**`  
- All processed data in `data/processed/**`  
- All archived data in `data/archive/**`  
- All Story Nodes and Focus Mode narratives  

Rules:

- ✅ Raw files are not edited in-place  
- ✅ Transformations only happen in `staging/`, `processed/`, etc.  
- ✅ Any re-ingestion of updated source files is logged as a **new acquisition event**  

---

## 8. ♻️ Retention & Preservation Policy

| Category         | Retention | Policy                                      |
|------------------|----------:|---------------------------------------------|
| Raw Data Files   | Permanent | Immutable archival for provenance & audits  |
| Source Metadata  | Permanent | ISO 19115 / FAIR+CARE governance retention  |
| Checksum Records | Permanent | Integrity evidence for every release        |
| FAIR+CARE Pre-Audits | 5 years | Pre-ingestion ethics & licensing records |
| Ingestion Logs   | 365 days  | Rotated per governance and infra policy     |

Retention automation defined in:

~~~~text
data/raw/metadata/raw_data_retention.yml
~~~~

---

## 9. 🌱 Sustainability Practices (Raw Ingestion)

Sustainability metrics for ingestion include:

- Energy consumption per ingestion job (`energy_wh`)  
- Carbon-equivalent emissions (`carbon_gCO2e`)  
- Ingestion throughput (files/time, bytes/time)  

Telemetry for raw ingestion flows into:

~~~~text
releases/v11.0.0/focus-telemetry.json
docs/reports/telemetry/data-raw-v11.json
~~~~

Practices:

- Prefer batching downloads to reduce overhead  
- Use renewable-powered compute where available  
- Minimize redundant fetches from upstream sources  

---

## 10. 🧾 Internal Use Citation

~~~~text
Kansas Frontier Matrix (2025). Raw Data Layer (v11.0.0).
Immutable FAIR+CARE-aligned repository for unaltered source datasets from NOAA,
USGS, FEMA, NASA, KDHE, and public/archival providers. Implements checksum
validation, ISO 19115 provenance logs, and open data ethics under MCP-DL v6.3
and KFM-MDP v11.0.
~~~~

---

## 11. 🕰 Version History

| Version | Date       | Summary                                                                                                         |
|--------:|------------|-----------------------------------------------------------------------------------------------------------------|
| v11.0.0 | 2025-11-19 | Full v11 upgrade: telemetry v4, FAIR+CARE pre-audits v11, ontology mapping, sustainability and governance v11. |
| v10.2.2 | 2025-11-12 | Streaming STAC hooks, telemetry v2, expanded pre-audit fields (consent tokens, sensitivity flags).            |
| v10.0.0 | 2025-11-09 | Streaming STAC baseline, telemetry schema references, lifecycle policy clarified.                              |
| v9.7.0  | 2025-11-06 | Governance & retention clarifications; improved metadata patterns.                                             |

<div align="center">

**Kansas Frontier Matrix — Raw Data Layer**  
📥 Open Data Integrity · ⚖️ FAIR+CARE Governance · 🧬 Provenance Accountability  

[⬅️ Back to Data Index](../README.md) ·  
[📐 Data Architecture](../ARCHITECTURE.md) ·  
[⚖️ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>