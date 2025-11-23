---
title: "📦 KFM v11 — Hazards Refresh Resources (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/autonomous/hazards-refresh/resources/README.md"
version: "v11.0.0"
last_updated: "2025-11-22"
review_cycle: "Daily · Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.0.0/telemetry/autonomous-hazards-refresh.json"
telemetry_schema: "../../../../../schemas/telemetry/autonomous-hazards-refresh-v1.json"
governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
data_contract_ref: "../../../../../docs/contracts/data-contract-v3.json"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Resource Module"
semantic_document_id: "kfm-autonomous-hazards-refresh-resources-v11"
doc_uuid: "urn:kfm:pipelines:autonomous:hazards-refresh:resources:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 📦 **Hazards Refresh Resources Module (v11)**  
`src/pipelines/autonomous/hazards-refresh/resources/README.md`

**Purpose:**  
Document the configuration, schemas, provider definitions, and checksum manifests used by the  
**Autonomous Hazards Refresh pipeline**.  
These resources supply the metadata backbone for stale-detection, ingestion, STAC-generation,  
and graph-sync accuracy under KFM v11.

</div>

---

# 📘 Overview

This module contains all **static resources** required by the **hazards-refresh** autonomous DAG:

- Provider registry (hazard data sources)  
- Hazard schema (`hazards_v1.schema.json`)  
- Checksum manifest (integrity guarantee for STAC assets)  
- Event taxonomy references  
- Temporal + spatial domain configurations  
- Versioning and licensing metadata  

All resources MUST follow:

- **KFM-MDP v11**  
- **MCP-DL v6.3** (documentation-first)  
- **STAC 1.0 + KFM v11 STAC Geo Extensions**  
- **CRS Standard v11**  
- **Hazards Schema v1**  
- **PROV-O lineage completeness**  
- **DCAT 3.0 dataset semantics**

---

# 🗂 Directory Layout (v11)

```text
src/pipelines/autonomous/hazards-refresh/resources/
│
├── README.md                               # This file (v11)
│
├── providers.yaml                           # Hazard data providers + STAC/default metadata
│
├── schema/
│   └── hazards_v1.schema.json               # Required hazard event schema for normalization + STAC validation
│
└── checksums/
    └── manifest.json                        # SHA-256 manifest for all hazard STAC assets
```

---

# 🌐 providers.yaml (Purpose & Requirements)

Defines **every hazard data provider** used by the autonomous pipeline.

Required fields:

- `id` — provider unique key  
- `kind` — `csv_http | json_http | geojson_http | rss | custom`  
- `url` — remote feed  
- `etag_header` / `last_modified_header` — for stale detection  
- `stac:`  
  - collection ID  
  - provider roles  
  - license  
  - dataset provenance fields  

### Example (valid v11 block)

```yaml
providers:
  - id: "noaa.storm_events"
    kind: "csv_http"
    url: "https://example.noaa.gov/stormevents/ks/latest.csv"
    etag_header: "ETag"
    time_header: "Last-Modified"
    stac:
      collection: "kfm-hazards-statewide"
      license: "CC0-1.0"
      providers:
        - name: "NOAA"
          roles: ["producer"]
```

---

# 📑 hazards_v1.schema.json (Schema Requirements)

Defines the **canonical hazards event schema** used during normalization + STAC Item creation.

Required fields:

- `EVENT_ID`
- `HAZARD_TYPE`  
- `START_TIME`, `END_TIME`  
- `LAT`, `LON` (EPSG:4326 only)  
- `COUNTY_FIPS`  
- `SEVERITY`, `INJURIES`, `FATALITIES`, `DAMAGE_USD`  

MUST support:

- JSON Schema draft 2020-12  
- Temporal fields convertible to OWL-Time intervals  
- Spatial fields convertible to GeoSPARQL WKT  
- Mapped directly into STAC hazards extensions  

---

# 🔐 checksums/manifest.json (Integrity Contract)

Tracks:

- SHA-256 for all assets referenced in hazards STAC Items  
- Per-provider latest observed hash  
- Timestamp of last verification  
- Optional multihash entries for compatibility with KFM-STAC v11  

CI SHALL:

- Compare PR-modified STAC Items against this manifest  
- Block changes when checksums mismatch (unless governance policy authorizes updates)

---

# 🔍 How These Resources Are Used in the DAG

Used by nodes:

- **detect_stale.py**  
  - Reads provider etags, timestamps  
- **fetch_sources.py**  
  - Uses provider URLs + headers  
- **normalize_events.py**  
  - Validates against hazards_v1 schema  
- **build_stac_items.py**  
  - Injects provider metadata into STAC Items  
- **validate_checksums.py**  
  - Reads SHA-256 manifest  
- **stac_validate.py**  
  - Applies schema + STAC v11 validation  

All resources MUST be **read-only** during DAG execution except where governance explicitly allows updates (e.g., checksum manifest rotation).

---

# 📘 Governance & FAIR+CARE Alignment

This module MUST follow:

- **FAIR principles** (machine-readable, versioned, accessible, discoverable)  
- **CARE principles** (ethical stewardship of hazard + impact data)  
- **Data Contract v3** for physical units, schema guarantees, and lineage provenance  

---

# 🕰 Version History

- **v11.0.0 (2025-11-22)** — Initial KFM v11 compliant Resources module for Hazards Refresh.

---

<div align="center">

**Kansas Frontier Matrix — Hazards Refresh Resources (v11)**  
*Reliable · Declarative · Provenance-Driven*

</div>

---

### 🔗 Footer  
[⬅ Back to Hazards Refresh](../README.md) · [🧩 Nodes](../nodes/README.md) · [🧰 Autonomous Utils](../../utils/README.md) · [🏛 Governance](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

