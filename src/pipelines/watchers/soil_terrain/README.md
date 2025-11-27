---
title: "🌾 KFM v11.2 — Soil & Terrain Watchers (gNATSGO + 3DEP · Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/watchers/soil_terrain/README.md"

version: "v11.2.2"
last_updated: "2025-11-27"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Semiannual · Pipelines Working Group · FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:pipelines:watchers:soil-terrain:v11.2.2"
semantic_document_id: "kfm-pipelines-watchers-soil-terrain"
event_source_id: "ledger:src/pipelines/watchers/soil_terrain/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/pipelines-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/watchers-soil-terrain-v11.2.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

status: "Active / Enforced"
doc_kind: "Pipeline README"
intent: "soil-terrain-watchers-governance"
category: "Pipelines · Watchers · Environmental Basemaps"

fair_category: "F1-A1-I1-R1"
care_label: "CARE: Collective Benefit · Authority to Control · Responsibility · Ethics"

data_domains:
  - "Soils · USDA NRCS gNATSGO"
  - "Terrain · USGS 3DEP 1/3-arc-second DEM"
  - "Hydrology-ready derivatives"

pipeline_tier: "Tier-1 Critical (Environmental Core)"
owner_group: "Environmental Pipelines Working Group"
approvers:
  - "FAIR+CARE Council"
  - "Reliability Engineering"
  - "Geo Standards Working Group"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
classification: "Public (Governed)"
jurisdiction: "Kansas / United States"

ttl_policy: "Semiannual Review"
sunset_policy: "Superseded by v12 Watcher Overhaul"
---

<div align="center">

# 🌾 **KFM v11.2 — Soil & Terrain Watchers**  
### gNATSGO Soils + USGS 3DEP Terrain  
`src/pipelines/watchers/soil_terrain/README.md`

**Purpose**  
Define the **auto-update watcher pipelines** responsible for detecting, validating, and triggering deterministic ETL refreshes for:  
- 🧪 **gNATSGO soils** (annual composites)  
- ⛰️ **USGS 3DEP DEM** (continuous → quarterly detection)  

These watchers ensure KFM’s environmental basemaps remain **accurate, reproducible, and governed**.

  
<!-- Badge Row (root-centered-badge-row) -->
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.2-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Certified-gold" />
<img src="https://img.shields.io/badge/OpenLineage-v2.5-informational" />
<img src="https://img.shields.io/badge/Metadata-STAC%20%2F%20DCAT%20%2F%20JSON--LD-lightgrey" />

</div>

---

## 📘 1. Scope

These watchers:

- Monitor authoritative sources  
- Detect upstream changes  
- Write WAL intents  
- Emit OpenLineage  
- Trigger deterministic ETL DAGs  
- Never promote directly  
- Never mutate production data  
- Guarantee provenance and FAIR+CARE compliance  

They serve as the **front door** to the environmental ETL ecosystem.

---

## 🗂️ 2. Directory Layout

```text
📁 src/
└── 📁 pipelines/
    └── 📁 watchers/
        └── 📁 soil_terrain/
            📄 README.md
            📄 gnatsgo_soils_watcher.py
            📄 usgs_3dep_terrain_watcher.py
            📁 config/
            │   📄 gnatsgo_soils_watcher.yaml
            │   📄 usgs_3dep_terrain_watcher.yaml
            │   📄 common-policies.yaml
            📁 state/
            │   📄 gnatsgo_soils.state.json
            │   📄 usgs_3dep_terrain.state.json
            📁 tests/
            │   📄 test_gnatsgo_soils_watcher.py
            │   📄 test_usgs_3dep_terrain_watcher.py
            │   📁 fixtures/
            │       📄 gnatsgo_metadata_sample.json
            │       📄 usgs_3dep_metadata_sample.json
            📁 docs/
                📄 watcher-design-notes.md
```

---

## 🔍 3. Watcher Behavior

### 3.1 gNATSGO Soil Watcher (Monthly)

- Runs monthly  
- Detects:
  - New ETag  
  - New Last-Modified  
  - Source checksum changes  
- On change:
  - WAL → `gnatsgo_full_refresh`
  - OpenLineage start event
  - ETL trigger: `pipelines.soils.gnatsgo_full_refresh`

### 3.2 3DEP Terrain Watcher (Quarterly)

- Runs quarterly  
- Detects:
  - Updated DEM tiles  
  - New collection releases  
  - STAC/DCAT modifications  
- On change:
  - WAL → `3dep_quarterly_refresh`
  - OpenLineage event  
  - ETL trigger: `pipelines.terrain.usgs_3dep_refresh`

---

## 🔁 4. ETL Contracts

Watchers **only enqueue**.  
ETL performs:

- Download + checksums  
- CRS + vertical datum corrections  
- Hydrology-ready derivations  
- COG + PMTiles generation  
- STAC/DCAT/JSON-LD creation  
- Provenance graph edges  
- Promotion gating

Context fields passed from watchers guarantee deterministic lineage.

---

## 🧱 5. WAL Model

Always WAL-first:

1. Write intent  
2. Persist state  
3. Emit OpenLineage  
4. Enqueue ETL  
5. Promotion happens in ETL, not watcher  

This ensures:

- Replay safety  
- Zero silent promotions  
- Perfect auditability  

---

## 📊 6. Telemetry

Watchers emit:

- Duration  
- Trigger reason  
- Error counters  
- Energy (Wh/J)  
- Carbon (gCO2e)  
- Retry counts  

Telemetry flows into:

```
releases/v11.2.2/pipelines-telemetry.json
```

---

## 🧬 7. Metadata Integration

Watchers provide ETL with:

- Release tags  
- Checksum signatures  
- Tile metadata  
- Timestamps  
- Provenance seeds (PROV-O)  
- Collection identifiers  

ETL produces STAC/DCAT/JSON-LD based on these seeds.

---

## 🧠 8. Focus Mode Integration

Watchers indirectly power Focus Mode:

- “Soil Basemap vYYYY”  
- “Terrain Basemap vYYYY-QN”  
- Change summaries for Story Nodes  
- Provenance-timebars

---

## 🕰 9. Version History

| Version | Date | Summary |
|--------:|------|---------|
| v11.2.2 | 2025-11-27 | Corrected footer, badges, canonical layout, telemetry alignment. |
| v11.2.0 | 2025-11-27 | Initial watcher specification. |

---

<div align="center">

## 🌾 **Kansas Frontier Matrix — Soil & Terrain Watchers (v11.2.2)**  
*Deterministic environmental basemaps · Reproducible ETL · FAIR+CARE aligned*

  
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.2-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Certified-gold" />
<img src="https://img.shields.io/badge/OpenLineage-v2.5-informational" />
<img src="https://img.shields.io/badge/Metadata-STAC%20%2F%20DCAT%20%2F%20JSON--LD-lightgrey" />

  
© 2025 Kansas Frontier Matrix — MIT License  
MCP-DL v6.3 · KFM-MDP v11.2.2 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω

  
[⬅ Back to Watchers Directory](../README.md) ·  
[⚖ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·  
[📘 KFM Documentation Home](../../../docs/README.md)

</div>
