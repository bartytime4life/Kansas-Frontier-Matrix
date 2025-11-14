---
title: "📥 Kansas Frontier Matrix — Remote Sensing Ingestion Pipelines (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/remote-sensing/ingest/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/pipelines-remote-sensing-ingest-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📥 **Kansas Frontier Matrix — Remote Sensing Ingestion Pipelines**  
`src/pipelines/remote-sensing/ingest/README.md`

**Purpose:**  
Define the **canonical ingestion layer** for all remote-sensing pipelines in the Kansas Frontier Matrix (KFM).  
These ingestion modules perform **STAC polling**, **ETag-aware delta ingestion**, **batch collection**, **download orchestration**, **file normalization**, and **FAIR+CARE-governed staging** for Landsat, Sentinel-1/2, NAIP, MODIS/VIIRS, and hazard/index pipelines.

<img alt="Ingest" src="https://img.shields.io/badge/Ingestion-STAC_Driven-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Enforced-orange"/>
<img alt="Provenance" src="https://img.shields.io/badge/Provenance-Tracked-green"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Active-success"/>

</div>

---

## 📘 Overview

Ingestion pipelines form the **front door** of all remote-sensing processing in KFM.

These modules:

- Poll **STAC** and satellite-specific APIs  
- Respect **ETag / If-None-Match** to avoid unnecessary downloads  
- Write structured JSON/JSONL batches into standardized staging directories  
- Produce provenance, checksums, and telemetry logs  
- Activate preprocessing, overlap analysis, AI summarization, Neo4j publishing, and RDF export steps downstream  
- Enforce **FAIR+CARE governance** at the data-entry boundary  

All ingestion outputs MUST be:

- Deterministic  
- Versioned  
- Validated  
- CARE-compliant  
- Traceable via lineage  
- Telemetry-linked  

---

## 🗂️ Directory Layout

~~~~~text
src/pipelines/remote-sensing/ingest/
├── README.md                          # This file
│
├── landsatlook_ingest.py              # USGS LandsatLook STAC fetcher
├── sentinel2_ingest.py                # Sentinel-2 L2A ingestion
├── sentinel1_ingest.py                # Sentinel-1 GRD ingestion
├── naip_ingest.py                     # NAIP imagery harvest
├── modis_ingest.py                    # MODIS/VIIRS scene ingestion
│
└── schemas/
    ├── ingest.schema.json             # Required fields for ingest configs
    └── stac_batch.schema.json         # Schema for JSONL STAC batches
~~~~~

---

## 🧩 Ingestion Architecture (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Scheduled Polling<br/>GitHub Actions / Cron"] --> B["STAC / API Request<br/>ETag / If-None-Match"]
  B -->|304| Z["No Change<br/>Emit Telemetry"]
  B -->|200| C["Write Raw Batch<br/>data/stac/incoming/..."]
  C --> D["Validate Batch<br/>jsonschema + FAIR+CARE"]
  D -->|PASS| E["Trigger Preprocessing Layer"]
  D -->|FAIL| F["Quarantine Batch<br/>+ Open Governance Issue"]
~~~~~

---

## 🛰 Supported Ingestion Modules

### 1. **landsatlook_ingest.py**
- Queries USGS LandsatLook STAC Search  
- Filters by datetime, cloud cover, and Kansas AOI  
- Supports pagination via `links[].rel=="next"`  
- Writes JSONL files to:  

~~~~~text
data/stac/landsat/<YYYY>/<MM>/<DD>/items_*.jsonl
~~~~~

### 2. **sentinel2_ingest.py**
- Queries Sentinel-2 L2A STAC endpoints (AWS Element84, USGC)  
- Retrieves optical scenes for spectral index, burn-scar, and hazard pipelines  
- Accepts cloud-probability filters  

### 3. **sentinel1_ingest.py**
- SAR ingestion for flood-extents, soil-moisture proxies, winter hydrology  
- Supports GRD-specific filters (orbit direction, polarization)  

### 4. **naip_ingest.py**
- Ingests NAIP imagery via USDA endpoints  
- Maps footprints to Kansas counties  
- Normalizes metadata for downstream mosaicking  

### 5. **modis_ingest.py**
- Earthdata/MODIS/VIIRS ingestion  
- Provides temporal composites for drought pipelines and climate analyses  

---

## 📦 STAC Ingest Output Format

All ingestion modules produce **STAC JSONL batches** validating against:

~~~~~text
src/pipelines/remote-sensing/ingest/schemas/stac_batch.schema.json
~~~~~

Each line represents one STAC `Feature` object:

- `id`
- `collection`
- `datetime`
- `bbox`
- `geometry`
- `assets`
- `links`
- `properties` (normalized)

All ingested features MUST include:

- `kfm:ingest_time`  
- `kfm:ingest_version`  
- `kfm:source_endpoint`  
- `kfm:stacAssetHash` (sha256 of sorted asset HREFs)  

---

## 📎 Example Minimal Ingestion Payload

~~~~~json
{
  "collections": ["landsat-c2l2-sr"],
  "datetime": "2025-10-31T00:00:00Z/..",
  "limit": 250,
  "intersects": {
    "type": "Polygon",
    "coordinates": "… Kansas Boundary …"
  }
}
~~~~~

---

## 🔐 Governance Requirements

All ingestion output MUST:

- Include `care_label` from pipeline config  
- Flag any detections of sensitive AOIs  
- Apply masking/generalization when `care_label = sensitive/restricted`  
- Log governance metadata to:  

~~~~~text
../../../../../docs/reports/audit/data_provenance_ledger.json
~~~~~

- Fail CI if:
  - Sensitive AOIs are intersected without mandated masking  
  - Required provenance fields missing  
  - Schema validation fails  

---

## 📡 Telemetry Requirements

Each ingestion module must emit structured NDJSON:

~~~~~text
data/processed/telemetry/<pipeline>.ndjson
~~~~~

Tracked telemetry fields:

- `stage: "ingest"`  
- `items_polled`  
- `items_retained`  
- `items_deduped`  
- `etag_used`  
- `request_latency_ms`  
- `energy_wh`  
- `co2_g`  
- `care_violations`  
- `errors`  

Aggregated to:

~~~~~text
../../../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## 🧪 Local Run Pattern

~~~~~bash
python src/pipelines/remote-sensing/ingest/landsatlook_ingest.py \
  --config src/pipelines/remote-sensing/configs/landsatlook-stac-ingest.config.yaml
~~~~~

---

## 🕰️ Version History

| Version | Date       | Author | Summary |
|---------|------------|--------|---------|
| v10.3.1 | 2025-11-14 | Remote Sensing Team | Established ingestion module registry; aligned with FAIR+CARE, telemetry, STAC batch schema. |

---

<div align="center">

**Kansas Frontier Matrix — Remote Sensing Ingestion Layer**  
Reliable STAC Harvesting × FAIR+CARE × Deterministic ETL × Provenance Integrity  
© 2025 Kansas Frontier Matrix — MIT License  

</div>