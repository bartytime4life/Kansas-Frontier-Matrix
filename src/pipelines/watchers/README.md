---
title: "👁️ KFM v11.2 — Watcher Pipelines Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/watchers/README.md"

version: "v11.2.2"
last_updated: "2025-11-27"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Semiannual · Pipelines Working Group · FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<sha256-prev>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:pipelines:watchers:index:v11.2.2"
semantic_document_id: "kfm-watchers-index"
event_source_id: "ledger:src/pipelines/watchers/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/pipelines-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/watchers-index-v11.2.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

status: "Active / Enforced"
doc_kind: "Pipeline README"
intent: "watchers-index"
category: "Pipelines · Automation · Environmental & Data Integrity Watchers"

fair_category: "F1-A1-I1-R1"
care_label: "CARE · Collective Benefit · Responsible Stewardship"
classification: "Public (Governed)"
jurisdiction: "Kansas / United States"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "Annual Review"
sunset_policy: "Superseded by Watchers Index v12"
---

<div align="center">

# 👁️ **KFM v11.2 — Watcher Pipelines Index**  
`src/pipelines/watchers/README.md`

**Purpose**  
Serve as the **authoritative index** for all automatic **watcher pipelines** used in the Kansas Frontier Matrix.  
Watchers detect upstream dataset changes, log WAL intents, emit OpenLineage, and trigger deterministic ETL processes — providing **early-warning, automatic-refresh capability** with full **provenance, reproducibility, governance, and FAIR+CARE compliance**.

  
<!-- Badge Row (root-centered-badge-row) -->
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.2-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Certified-gold" />
<img src="https://img.shields.io/badge/OpenLineage-v2.5-informational" />
<img src="https://img.shields.io/badge/Automation-Watchers_Enabled-lightgrey" />

</div>

---

## 📘 1. Overview

Watcher pipelines are **Tier-1 automation agents** responsible for:

- Detecting **upstream dataset releases**, modifications, or metadata drift  
- Enforcing **WAL-first reliability patterns**  
- Emitting **OpenLineage** run events  
- Triggering **deterministic ETL DAGs** (never performing ETL directly)  
- Maintaining **versioned basemap consistency**  
- Ensuring **FAIR+CARE-aligned governance**  
- Supporting **Focus Mode v3** and Story Node timeline narratives  

Watchers guarantee KFM remains **fresh, reproducible, and audit-friendly** without manual intervention.

---

## 🗂️ 2. Directory Layout (Canonical)

```text
📁 src/
└── 📁 pipelines/
    └── 📁 watchers/
        📄 README.md                       — ← This file
        📁 soil_terrain/                   — gNATSGO soils + USGS 3DEP DEM watcher suite
        📁 climate/                        — HRRR, NDFD, PRISM, Daymet watcher suite
        📁 hydrology/                      — Streamflow, reservoir levels, WID/USGS watchers
        📁 hazards/                        — Severe weather, wildfire, drought watchers
        📁 imagery/                        — NAIP, Sentinel-2, Landsat repository watchers
        📁 metadata/                       — Source registry, provider metadata drift watchers
        📁 contracts/                      — Watchers enforcing STAC/DCAT/data-contract release drift
        📁 tests/                          — Consolidated watcher-level integration tests
```

Each subdirectory contains:

- **watcher python modules**  
- **config files** (yaml)  
- **state directories** (ETags, timestamps, checksums, release IDs)  
- **unit + integration tests**  
- Optional **design notes**

---

## 🔍 3. Responsibilities of All Watchers

All watchers MUST:

### ✔ 3.1 Follow WAL-First Reliability  
- Write an immutable **intent record**  
- Then fire OpenLineage  
- Then enqueue ETL DAG  
- Never modify production assets directly  

### ✔ 3.2 Perform Lightweight Detection Only  
- Watchers = **metadata inspectors**, not processors  
- ETL performs all transformation & publication  

### ✔ 3.3 Enforce Governance  
- No promotion without:
  - ETL success  
  - Schema checks  
  - FAIR+CARE checks  
  - Provenance completeness  
  - STAC/DCAT validation  

### ✔ 3.4 Emit Telemetry  
- Duration  
- Error codes  
- Energy / carbon  
- Trigger reason  
- Drift classification  

### ✔ 3.5 Maintain State  
- ETag or modified-date  
- Source checksum  
- Last promoted version  
- Notes for replay or regression  

---

## 📡 4. Watcher Categories

### 🌾 4.1 Soil & Terrain Watchers  
Location: `soil_terrain/`  
Covers:
- gNATSGO (annual composites)  
- 3DEP 1/3-arc-sec DEM (terrain basemap + hydrology derivatives)

### 🌦️ 4.2 Climate & Atmospheric Watchers  
Location: `climate/`  
Covers:
- PRISM  
- HRRR  
- NDFD  
- Daymet  
- NOAA Climate Normals  
- NCEI time-series feeds

### 🌊 4.3 Hydrology Watchers  
Location: `hydrology/`  
Covers:
- USGS NWIS  
- Reservoir water-surface elevations  
- Flood data, WID dredging, turbidity sensors  
- River deltas, reservoir sedimentation

### ⚠️ 4.4 Hazards Watchers  
Location: `hazards/`  
Covers:
- Tornado, hail, and storm-path feeds  
- Wildfire risk layers  
- County-level hazard bulletins  
- Drought monitors

### 🛰️ 4.5 Imagery & Remote Sensing Watchers  
Location: `imagery/`  
Covers:
- NAIP  
- Landsat collections  
- Sentinel-2  
- SWOT & other EO missions  
- High-resolution imagery STAC updates

### 🧩 4.6 Metadata & Contract Compliance Watchers  
Location: `metadata/`, `contracts/`  
Covers:
- Provider metadata drift  
- STAC Collection updates  
- DCAT catalog drift  
- Schema changes to external datasets  
- Data contract violations

---

## 🔁 5. Watcher → ETL → Promotion Lifecycle

```text
Watcher detects change
        ↓
Write-Ahead Log (WAL) intent
        ↓
OpenLineage emitted (STARTED)
        ↓
Enqueue ETL DAG
        ↓
ETL performs ingest + harmonization + STAC/DCAT
        ↓
Validation → QA → FAIR+CARE governance
        ↓
Promotion + update of watcher state file
```

This ensures **zero ambiguity** in what triggered each dataset refresh.

---

## 📊 6. Telemetry Model (v11.2.2)

All watchers emit at least:

- `kfm.watcher.<domain>.triggered`  
- `kfm.watcher.<domain>.duration_ms`  
- `kfm.watcher.error_count`  
- `kfm.watcher.energy.j`  
- `kfm.watcher.carbon.gco2e`  
- OpenLineage events referencing:
  - dataset_id  
  - source_id  
  - trigger_reason  
  - state_before  
  - state_after  

Telemetry stored under:

```
releases/v11.2.2/pipelines-telemetry.json
```

---

## 🧠 7. Focus Mode & Story Node Integration

Watcher-triggered refreshes feed Focus Mode narrative contexts:

- “**Kansas Basemap Update**”  
- “**Soil Refresh vYYYY**”  
- “**Terrain Mosaic Update vYYYY-QN**”  
- “**Climate Drift Event Detected**”  
- “**Water Surface Changed: Reservoir X**”  

Story Nodes read:

- release timestamps  
- spatial extents  
- lineage metadata  
- delta summaries  

---

## 🧭 8. Related Documents

- `src/pipelines/reliability/README.md`  
- `docs/standards/geo/README.md`  
- `docs/standards/geo/soil-source-comparison.md`  
- `docs/standards/governance/ROOT-GOVERNANCE.md`  
- `docs/standards/faircare/FAIRCARE-GUIDE.md`  

---

## 🕰 9. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-27 | Initial v11.2.2 unified watcher index; added canonical footer, badges, directory layout, governance alignment. |

---

<div align="center">

## 👁️ **Kansas Frontier Matrix — Watcher Pipelines Index (v11.2.2)**  
*Automation for environmental truth · Reliable · Governed · FAIR+CARE aligned*

  
<!-- Badge Row -->
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.2-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Certified-gold" />
<img src="https://img.shields.io/badge/OpenLineage-v2.5-informational" />
<img src="https://img.shields.io/badge/Watchers-Automated-lightgrey" />

  
© 2025 Kansas Frontier Matrix — MIT License  
MCP-DL v6.3 · KFM-MDP v11.2.2 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to Pipelines](../README.md) ·  
[⚖ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·  
[📘 KFM Documentation Home](../../../docs/README.md)

</div>

