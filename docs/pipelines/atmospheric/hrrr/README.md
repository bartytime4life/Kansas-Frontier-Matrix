---
title: "🌤️ Kansas Frontier Matrix — HRRR Atmospheric Pipelines Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/atmospheric/hrrr/README.md"
version: "v11.2.4"
last_updated: "2025-12-08"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
doc_kind: "Pipeline Domain Index"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256-or-null>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../releases/v11.2.4/atmo-hrrr-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/atmo-hrrr-domain-v1.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.5"
ontology_protocol_version: "KFM-OP v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "atmo.hrrr"
  applies_to:
    - "etl"
    - "streaming-ingest"
    - "windowing"
    - "stac"
    - "graph"
    - "story-nodes"
    - "telemetry"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk (atmospheric fields; masking for sensitive joins)"
classification: "Public / Internal (governed pipelines)"
sensitivity_level: "Low–Medium"
public_exposure_risk: "Low"
risk_category: "Environmental Modelling / Atmospheric Data"
indigenous_rights_flag: true
redaction_required: true

doc_uuid: "urn:kfm:doc:pipelines:atmospheric:hrrr:index:v11.2.4"
semantic_document_id: "kfm-pipelines-atmospheric-hrrr-index"
event_source_id: "ledger:docs/pipelines/atmospheric/hrrr/README.md"
machine_extractable: true
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified atmospheric claims"
  - "governance-override"
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
ttl_policy: "24 months"
sunset_policy: "Superseded upon next HRRR domain reorganization"
---

<div align="center">

# 🌤️ **Kansas Frontier Matrix — HRRR Atmospheric Pipelines Index**  
`docs/pipelines/atmospheric/hrrr/README.md`

**Purpose**  
Serve as the **governed index** for all **HRRR-related pipelines, patterns, and tests** in the Kansas Frontier Matrix (KFM), including Zarr windowing, subsetting, catalog integration, and graph ingestion.

</div>

---

## 🗂️ Directory Layout

```text
KansasFrontierMatrix/
├── 📁 docs/
│   └── 📁 pipelines/
│       └── 📁 atmospheric/
│           └── 📁 hrrr/
│               ├── 📄 README.md                      # ← This file (HRRR pipelines index)
│               └── 📁 windowing/
│                   ├── 📄 README.md                  # HRRR Zarr windowing & subsetting pattern
│                   ├── 📁 examples/
│                   │   ├── 📄 bbox-basic.md          # Example bbox windowing run
│                   │   ├── 📄 polygon-windowing.md   # Polygon-based AOI windowing
│                   │   └── 📄 stac-subset-example.json
│                   └── 📁 tests/
│                       ├── 📄 test-windowing-shapes.py
│                       ├── 📄 test-stac-provenance.py
│                       └── 📁 fixtures/              # Test data & configs
├── 📁 src/
│   └── 📁 pipelines/
│       └── 📁 atmospheric/
│           └── 📁 hrrr/
│               ├── 📄 __init__.py
│               ├── 📁 windowing/
│               │   ├── 📄 run_window.py              # Main windowing entrypoint
│               │   ├── 📄 run_state.py               # Idempotency & run-state keys
│               │   ├── 📄 stac_emit.py               # STAC processing:subset emitter
│               │   └── 📄 config.py                  # Dataset/version/selector config
│               └── 📁 (future submodules)            # e.g., regridding, fused fields
└── 📁 data/
    ├── 📁 run_state/
    │   └── 📁 hrrr_window/
    │       └── 📄 <sha256>.json                      # Run-state & stats bundle
    └── 📁 atmospheric/
        └── 📁 hrrr/
            ├── 📁 zarr_index/                        # Optional Zarr index metadata
            └── 📁 subsets/                           # Materialized HRRR subsets
```

---

## 📘 Overview

The **HRRR Atmospheric Pipelines** cover ingest, windowing, and subsetting of **NOAA HRRR** forecast products for use inside KFM’s:

- Deterministic ETL pipelines,  
- STAC/DCAT catalogs,  
- Neo4j atmospheric graph nodes,  
- Focus Mode & Story Nodes that depend on high-resolution atmospheric fields.

This index:

- Anchors HRRR-specific pattern docs (e.g., the **HRRR Zarr Windowing & Subsetting Pattern**).  
- Connects code (`src/pipelines/atmospheric/hrrr/**`) to documentation (`docs/pipelines/atmospheric/hrrr/**`).  
- Provides a consistent home for tests, fixtures, and telemetry relevant to HRRR pipelines.

---

## 🧭 Context

HRRR is a **high-resolution, frequently-updated** atmospheric model. In KFM it is:

- A key driver of **hydrology**, **ecology**, and **risk** narratives,  
- Often used in combination with **NEXRAD**, **USGS gauges**, and **soil datasets**,  
- A major consumer of storage and compute, requiring **careful windowing** and **telemetry**.

KFM’s HRRR handling must:

- Be **deterministic and replayable**,  
- Avoid over-fetching or arbitrary slicing,  
- Emit enough metadata to reconstruct every window,  
- Integrate cleanly with **Event-Time watermarking** and **event-driven ingest** patterns.

---

## 🧱 Architecture (HRRR Domain)

The HRRR domain is structured around:

1. **Ingest & Indexing** (future expansion)  
   - Cataloging HRRR Zarr stores and versions,  
   - Maintaining `zarr_index` metadata to support cheap subsets.

2. **Windowing & Subsetting**  
   - Defined by the **HRRR Zarr Windowing & Subsetting Pattern**:
     - Config-driven, deterministic Zarr windows,  
     - Run-state keys ensuring idempotency,  
     - STAC `processing:subset` metadata.

3. **Higher-level Products** (future expansion)  
   - Regridded fields, fused HRRR + radar composites, metrics for Story Nodes, etc.

This index primarily documents (2) today, but is the place where (1) and (3) will be wired in as they become governed patterns.

---

## 📦 Data & Metadata

HRRR domain outputs must:

- Live under `data/atmospheric/hrrr/**`, with clear separation between:
  - Index structures (`zarr_index/`),  
  - Materialized subsets (`subsets/`),  
  - Run-state (`data/run_state/hrrr_window/`).  

- Be cataloged via STAC Collections and Items, using the **processing subset** metadata defined in:
  - `docs/pipelines/atmospheric/hrrr/windowing/README.md`.

All HRRR subsets must carry:

- `dataset_version`, `source_store`, `forecast_hour`,  
- Selector type/value (bbox or polygon),  
- Variables list, shapes, chunk structure, estimated bytes,  
- Provenance info: software versions, selectors, and run-state key.

---

## 🧪 Validation & CI/CD

HRRR pipelines are subject to:

- **Windowing pattern tests**:
  - `test-windowing-shapes.py` — verifying shapes and spatial extents,  
  - `test-stac-provenance.py` — verifying STAC `processing:subset` block and run-state linkage.

- **Reliability tests** (from the global suite):
  - Replayability and WAL recovery for HRRR streams (e.g., `test_replay_hrrr_stream.py`).  
  - Deterministic behavior under load.

- **Telemetry checks**:
  - Conformance to `hrrr-windowing-v2.json` telemetry schema,  
  - Energy/carbon reporting for HRRR windowing runs.

Any new HRRR pipeline or pattern must:

- Add or update tests under `docs/pipelines/atmospheric/hrrr/windowing/tests/` and `src/tests/reliability/**`.  
- Ensure `telemetry_ref` includes HRRR domain metrics for energy and reliability dashboards.

---

## 🧠 Story Nodes & Focus Mode Integration

HRRR subsets are frequently used in narratives about:

- Severe storms and high-impact weather,  
- Heat waves, drought, and extreme precipitation,  
- Air quality and ecological responses,  
- Interactions with hydrology and energy infrastructures.

For Story Nodes:

- HRRR layers referenced by narratives must link to:
  - Specific STAC Items or dataset versions that were windowed using this pattern,  
  - Graph nodes representing the derived HRRR windows.

- Focus Mode should rely on:
  - Time-scoped HRRR windows (forecast_hour intervals),  
  - Spatially-limited subsets (e.g., Kansas or basins),  
  - Telemetry + provenance showing:
    - How subsets were derived,  
    - When they were last updated,  
    - How they intersect with other domains (e.g., hydrology basins).

This index is the jumping-off point for any new HRRR-driven narratives or views intended for Focus Mode.

---

## 🕰️ Version History

| Version | Date       | Notes                                                                 |
|--------:|------------|-----------------------------------------------------------------------|
| v11.2.4 | 2025-12-08 | Initial governed HRRR pipelines index; aligned with Zarr windowing pattern and KFM-MDP v11.2.5. |

---

## 🛡️ Governance Footer

This document is governed by:

- **Atmospheric Working Group**  
- **FAIR+CARE Council**  
- **KFM Documentation & Pipeline Standards**

All modifications MUST:

- Maintain `markdown_protocol_version` alignment,  
- Update `doc_integrity_checksum`, `commit_sha`, and `previous_version_hash`,  
- Pass **docs-lint**, **schema-lint**, and **telemetry-lint** checks in CI.

Energy & carbon telemetry for HRRR pipelines:

- Is attached via `telemetry_ref`, following `energy_schema` and `carbon_schema`,  
- MUST be recorded for all production windowing runs to support sustainability SLOs.

<div align="center">

🌪️ **Kansas Frontier Matrix — HRRR Atmospheric Pipelines**  

[📘 Docs Root](../../../README.md) ·  
[🌤️ Atmospheric Pipelines Index](../README.md) ·  
[⚖️ Root Governance](../../standards/governance/ROOT-GOVERNANCE.md)

</div>
