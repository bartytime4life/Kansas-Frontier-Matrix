---
title: "📨 Kansas Frontier Matrix — Event Model Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/architecture/event-models/examples/README.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/pipelines-event-model-examples-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 📨 **Kansas Frontier Matrix — Event Model Examples**  
`src/pipelines/architecture/event-models/examples/README.md`

**Purpose:**  
Provide **canonical, FAIR+CARE-compliant sample event envelopes** for all KFM pipeline categories.  
These examples demonstrate correct structure, required metadata, sovereignty annotations, checksum chains, and idempotency mechanics used throughout the system.

<img alt="Docs" src="https://img.shields.io/badge/Docs-MCP_v6.3-blue"/>
<img alt="License" src="https://img.shields.io/badge/License-MIT-green"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Certified-orange"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Examples-success"/>

</div>

---

## 📘 Overview

All KFM pipelines use **typed event envelopes** that initiate:

- Ingestion  
- ETL transformations  
- Raster/vector geoprocessing  
- Document NLP + OCR  
- Story Node generation  
- AI explainability workflows  
- STAC/DCAT metadata generation  
- Governance reviews  
- Publication and lineage emission  

This file contains **reference-grade examples** for each event type using all required metadata fields, CARE flags, sovereignty blocks, checksums, and PROV-O lineage stubs.

---

## 📁 Directory Layout

~~~~~text
src/pipelines/architecture/event-models/examples/
├── README.md              # This file
├── ingest.json            # Example ingestion event
├── etl.json               # Example ETL pipeline event
├── ai.json                # Example AI explainability event
├── metadata.json          # Example STAC/DCAT metadata event
├── storynode.json         # Example Story Node generator event
├── publish.json           # Example publication event
└── governance.json        # Example CARE/sovereignty review event
~~~~~

---

## 📨 Example — Ingestion Event

~~~~~json
{
  "event_id": "9b7439e1-2c8a-4d9c-bc66-c9bcdf06e4b2",
  "event_type": "ingest",
  "timestamp": "2025-11-13T18:22:11Z",
  "dataset_id": "noaa_storm_events_1950_2025",
  "version": "v10.3.1",
  "source_uri": "https://www.ncei.noaa.gov/storm-events/file_1950_2025.csv",
  "idempotency_key": "sha256:21dd2c...",
  "correlation_id": "45bdac52-07bf-4c78-8dab-c00d711dbf33",
  "pipeline": "storm_ingest",
  "care_label": "public",
  "parameters": {
    "format": "csv",
    "compression": "none"
  },
  "provenance": {
    "source_ids": ["noaa_archive_storms"],
    "source_checksums": ["sha256:aabb22..."],
    "tools": {
      "python": "3.11.5"
    }
  }
}
~~~~~

---

## 🧩 Example — ETL Event

~~~~~json
{
  "event_id": "bbf23d0c-0a92-4d6d-9c3c-cc21021f0703",
  "event_type": "etl",
  "timestamp": "2025-11-13T19:22:11Z",
  "dataset_id": "hydrology_flow_ks",
  "version": "v10.3.1",
  "source_uri": "s3://noaa-hydro/ks/2025/file.nc",
  "idempotency_key": "sha256:99ab33...",
  "correlation_id": "12e1fb7c-c0a5-4bcd-bf01-d0d33a1129e0",
  "pipeline": "hydrology_flow",
  "care_label": "public",
  "parameters": {
    "reprojection": "EPSG:4326",
    "window": "full"
  },
  "provenance": {
    "source_ids": ["noaa_hydro_archive"],
    "source_checksums": ["sha256:fefe22..."],
    "tools": {
      "python": "3.11.5",
      "gdal": "3.12.0"
    }
  }
}
~~~~~

---

## 🤖 Example — AI Explainability Event (Focus Mode v2.4)

~~~~~json
{
  "event_id": "f4b1a0db-95e9-47bd-98d8-cf0020f55343",
  "event_type": "ai",
  "timestamp": "2025-11-13T20:01:14Z",
  "dataset_id": "treaty_documents_1867",
  "version": "v10.3.1",
  "source_uri": "s3://kfm-archives/medicine_lodge/treaty_scan_1867.tif",
  "idempotency_key": "sha256:a8d32eff...",
  "correlation_id": "ab3c48c1-0af4-41cf-ae0e-e57b8c03457d",
  "pipeline": "focus_mode_ai",
  "care_label": "sensitive",
  "sovereignty": {
    "tribal_authority": "Kanza Nation",
    "review_status": "required",
    "masking": "h3_r7"
  },
  "parameters": {
    "model": "focus-transformer-v2.4",
    "explainability": true
  },
  "provenance": {
    "source_ids": ["treaty_scans_ks"],
    "source_checksums": ["sha256:5599aa..."],
    "tools": {
      "python": "3.11.5",
      "transformer": "v2.4.0"
    }
  }
}
~~~~~

---

## 📚 Example — Metadata (STAC/DCAT) Event

~~~~~json
{
  "event_id": "d1ad20fc-2c87-4e41-aa98-ccdf09ab0dd8",
  "event_type": "metadata",
  "timestamp": "2025-11-13T21:08:00Z",
  "dataset_id": "ks_landcover_2020",
  "version": "v10.3.1",
  "source_uri": "s3://kfm-data/landcover/ks_2020.parquet",
  "idempotency_key": "sha256:ffa322...",
  "correlation_id": "6ef2a880-e93e-4c54-8351-4744bd623d49",
  "pipeline": "landcover_metadata",
  "care_label": "public",
  "parameters": {},
  "provenance": {
    "source_ids": ["us_landcover_archive"],
    "source_checksums": ["sha256:1010aa..."],
    "tools": {
      "python": "3.11.5"
    }
  }
}
~~~~~

---

## 🗺️ Example — Story Node Creation Event

~~~~~json
{
  "event_id": "7c097c92-8c17-464c-9ed6-b21f4d27f620",
  "event_type": "storynode",
  "timestamp": "2025-11-13T21:55:33Z",
  "dataset_id": "medicine_lodge_treaty_story",
  "version": "v10.3.1",
  "source_uri": "s3://kfm-stories/treaties/medicine_lodge/story_inputs.json",
  "idempotency_key": "sha256:a1a1e2c...",
  "correlation_id": "11fa9723-d33d-4cd9-a3e2-8a559b1c180e",
  "pipeline": "storynode_generator",
  "care_label": "sensitive",
  "provenance": {
    "source_ids": ["treaty_documents_1867"],
    "source_checksums": ["sha256:aaeebb..."],
    "tools": {
      "python": "3.11.5",
      "spaCy": "3.7.3"
    }
  }
}
~~~~~

---

## 📤 Example — Publication Event

~~~~~json
{
  "event_id": "ef12342d-b6bb-4747-ad6e-cb4f76bf8a6a",
  "event_type": "publish",
  "timestamp": "2025-11-13T22:33:19Z",
  "dataset_id": "ks_hydrology_flow_2025",
  "version": "v10.3.1",
  "source_uri": "s3://kfm/processed/hydrology/ks_2025/",
  "idempotency_key": "sha256:ff3312...",
  "correlation_id": "df141f8c-2fe2-49e5-ae2a-12f3c00aa782",
  "pipeline": "hydrology_publish",
  "care_label": "public",
  "provenance": {
    "source_ids": ["noaa_stations_ks", "usgs_streamflow_ks"],
    "source_checksums": [
      "sha256:abc111...",
      "sha256:def222..."
    ]
  }
}
~~~~~

---

## ⚖️ Example — Governance Review Event

~~~~~json
{
  "event_id": "b331ce90-0e48-4a06-bbdf-5f5d9dcac11a",
  "event_type": "governance",
  "timestamp": "2025-11-13T23:18:55Z",
  "dataset_id": "ks_archaeology_sensitive",
  "version": "v10.3.1",
  "source_uri": "s3://tribal-archives/ks_sensitive.geojson",
  "idempotency_key": "sha256:ac44e55...",
  "correlation_id": "9ed015db-589c-4fb4-afc1-e091f7a1a26a",
  "pipeline": "care_review",
  "care_label": "restricted",
  "sovereignty": {
    "tribal_authority": "Prairie Band Potawatomi Nation",
    "review_status": "required",
    "masking": "h3_r7"
  },
  "provenance": {
    "source_ids": ["tribal_archive_ks_2025"],
    "source_checksums": ["sha256:aa5599..."]
  }
}
~~~~~

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|--------|---------|
| v10.3.1 | 2025-11-13 | Pipeline Architecture Team | Added full suite of event envelope examples across ingestion, ETL, AI, metadata, Story Node, publication, and governance pipelines. |

---

<div align="center">

**Kansas Frontier Matrix — Event Model Examples**  
Deterministic Events × FAIR+CARE × Provenance × Governance  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Event Models](../README.md)

</div>
