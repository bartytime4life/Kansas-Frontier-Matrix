---
title: "🛰️ Kansas Frontier Matrix — Sentinel-1D Mission (SAR · C-Band · Commissioning Phase · Diamond⁹ Ω / Crown∞Ω)"
path: "data/stac/missions/sentinel-1d/README.md"

version: "v11.2.0"
last_updated: "2025-11-27"
release_stage: "Pre-Operational · Commissioning Phase"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Semiannual · EO Working Group · FAIR+CARE Council"

commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v11.2.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.0/stac-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/stac-sentinel1d-v11.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active · Ingestion Pending"
doc_kind: "Mission Directory"
intent: "stac-sentinel-1d-commissioning-namespace"
semantic_document_id: "kfm-stac-mission-sentinel-1d"
doc_uuid: "urn:kfm:data:stac:missions:sentinel-1d:v11.2.0"

fair_category: "FAIR-Aligned"
care_label: "CARE Screened (Radar Data Generally Non-Sensitive)"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"

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

# 🛰️ **Sentinel-1D Mission Directory**  
`data/stac/missions/sentinel-1d/`

**Purpose:**  
Define the **STAC namespace, directory scaffold, and integration model** for the **Sentinel-1D C-band SAR mission** within KFM during its **commissioning phase**, so that as soon as ESA public data becomes available, ingestion pipelines and downstream products can be activated without further structural changes.

</div>

---

## 📘 Overview

Sentinel-1D is the next-generation **C-band Synthetic Aperture Radar (SAR)** platform in the Copernicus Sentinel-1 constellation.

Key characteristics for KFM:

- **All-weather, day/night imaging** for Kansas and global targets.  
- **Interferometric stability (InSAR)** suitable for land subsidence, deformation, and infrastructure monitoring.  
- **Operational continuity** after Sentinel-1A/1B aging and gaps.  
- **Rapid hazard response** for flooding, landslides, ice dynamics, and other events that affect Kansas directly or indirectly.

In KFM, this mission directory:

- Establishes a **STAC-ready mission envelope** before full operational release.  
- Supports **UI previews and demos** using publicly released commissioning imagery.  
- Prepares **LangGraph v11 ingestion DAGs** and **OpenLineage** emission paths.

---

## 🗂️ Directory Layout

```text
📁 data/
└── 📁 stac/
    └── 📁 missions/
        └── 📁 sentinel-1d/
            ├── 📄 README.md              — This file (mission directory spec)
            ├── 📄 collection.json        — STAC Collection (commissioning-phase)
            ├── 📁 items/                 — STAC Items (commissioning + future operational)
            │   ├── 📁 commissioning/     — Browse pseudo-items (first images, ESA previews)
            │   └── 📁 operational/       — True SLC/GRD/ETAD-backed items (Q1–Q2 2026+)
            ├── 📁 metadata/              — Mission metadata (JSON-LD, DCAT, capabilities)
            │   ├── 📄 mission.jsonld
            │   ├── 📄 commissioning.json
            │   └── 📄 capabilities.json
            └── 📁 qa/                    — QA, validation, energy + carbon telemetry
                ├── 📄 stac-validate.log
                ├── 📄 energy.json
                └── 📄 carbon.json
```

This structure is **stable**: commissioning content is added now, operational items are added later without changing the hierarchy.

---

## 🧭 Context

Sentinel-1D is important to KFM because:

- SAR provides **cloud-agnostic coverage** of Kansas agricultural, hydrological, and infrastructure systems.  
- Interferometric capabilities support:
  - Groundwater-related subsidence studies.  
  - Levee, dam, and critical infrastructure monitoring.  
  - Long-term land deformation and hazard modeling.  
- Commissioning-phase previews allow:
  - Early UI integration and performance testing.  
  - STAC schema and metadata validation.  
  - Ingestion DAG dry-runs before operational data appears.

This directory is the **integration point** between global Sentinel-1D products and KFM’s regional focus.

---

## 🧱 STAC & Integration Model (v11.2)

### STAC Collection (`collection.json`)

The Sentinel-1D collection:

- Represents the mission in **commissioning status**.  
- Declares:
  - `"sar:frequency_band": "C"`  
  - `"platform": "Sentinel-1D"`  
  - Instrument metadata (e.g. SAR antenna, modes IW/EW).  
- Is compatible with:
  - **STAC v1.1.0** + KFM SAR extensions.  
  - KFM-STAC v11 profile for missions and acquisitions.

### Product Types (Pre-Registered)

These product types are **pre-wired** into KFM ingestion configurations:

| Mode | Product | KFM Code            | Notes                             |
|------|---------|---------------------|-----------------------------------|
| IW   | SLC     | S1D_IW_SLC__1SDV    | Interferometric wide-swath SLC    |
| IW   | GRD     | S1D_IW_GRDH_1SDV    | Default Kansas-region ingest GRD  |
| EW   | GRD     | S1D_EW_GRDM_1SDH    | Wide-area hazard monitoring GRD   |
| ETAD | AUX     | S1D_ETAD_AX         | Timing + attitude ancillary data  |

These codes are used to map incoming ESA SAFE metadata into **KFM STAC Items** and **graph entities**.

### KFM Integration Layers

1. **STAC Layer**  
   - `collection.json` → Sentinel-1D mission scope.  
   - `items/commissioning/*` → pseudo-items using commissioning preview imagery.  
   - `items/operational/*` → true SAFE-derived SLC/GRD/ETAD STAC items once public.

2. **LangGraph v11 Ingestion**  
   - DAG already defined, initially disabled.  
   - Steps:  
     - SAFE → intermediate GeoTIFF → cloud-optimized SAR tiles.  
     - Generation of derived metadata and STAC Items.  
   - All runs emit OpenLineage v2.5 events for:
     - Provenance  
     - Performance metrics  
     - Energy/carbon telemetry hooks.

3. **Graph Nodes (Neo4j)**  
   Sentinel-1D data maps into these primary entity types:

   - `SatelliteMission` (Sentinel-1D mission node)  
   - `Acquisition` (individual SAR scenes)  
   - `RadarMode` (IW/EW, polarization, look direction)  
   - `DerivedProduct` (processed hazard layers, coherence maps, etc.)  
   - `PlatformCapability` (e.g. revisit time, orbit characteristics)

These nodes connect to:

- `AreaOfInterest` (AOIs in Kansas)  
- `HazardModel` (e.g., flood, subsidence, landslide)  
- `DatasetVersion` (versions of derived products)

---

## 🗺️ Commissioning Phase Content

The `items/commissioning/` folder is reserved for **commissioning-phase pseudo-items**, built from ESA’s early preview releases:

- Example geographic foci:
  - Bremen / Elbe Delta  
  - Wadden Sea  
  - Antarctic Peninsula  

These are:

- **Not SAFE-backed products** and carry explicit flags as such.  
- Used to:
  - Test MapLibre overlay rendering.  
  - Validate STAC schemas and EO/SAR extensions.  
  - Exercise LangGraph ingestion without relying on stable, long-term data.  
  - Demonstrate KFM’s UI capabilities.

Each pseudo-item:

- Includes accurate geometry, time, and basic mission metadata.  
- Explicitly marks its `kfm:commissioning_preview = true` to avoid confusion with operational data.

---

## 🌐 Future Operational Integration (Q1–Q2 2026)

When ESA begins public Sentinel-1D distribution:

1. ESA SAFE archives (SLC/GRD/ETAD) become accessible via Copernicus hubs.  
2. KFM’s ingestion pipelines:
   - Ingest SAFE → generate GTiff/COG representations.  
   - Create STAC Items in `items/operational/`.  
   - Attach full provenance (OpenLineage + PROV).  
3. Commissioning pseudo-items are:
   - Retained for history (but clearly marked as previews), or  
   - Moved into a dedicated `items/commissioning/legacy/` subfolder.  
4. Hazard and EO models:
   - Start consuming Sentinel-1D SAR products for:
     - Flood inundation mapping.  
     - Soil moisture proxies (with other datasets).  
     - Land subsidence and deformation.  
     - Ice and snow monitoring upstream of Kansas river systems.

---

## 🧪 Validation & QA

The `qa/` folder centralizes quality and sustainability telemetry:

- `stac-validate.log`  
  - Output of STAC validators against `collection.json` and `items/*`.  
  - Ensures conformance to STAC and KFM-STAC profiles.

- `energy.json` / `carbon.json`  
  - Capture energy and carbon estimates for:
    - Ingestion  
    - Reprocessing  
    - Re-indexing operations  
  - Intended to align with **ISO 50001** and **ISO 14064** guidance.

These files enable:

- CI pipelines to fail fast on invalid STAC changes.  
- Governance to review SAR ingestion cost and efficiency over time.

---

## 🧭 Version History

| Version  | Date       | Summary                                                                 |
|---------:|------------|-------------------------------------------------------------------------|
| v11.2.0  | 2025-11-27 | Initial Sentinel-1D mission directory; commissioning-phase STAC scaffold and integration model defined. |

---

<div align="center">

**Kansas Frontier Matrix — Sentinel-1D Mission Directory**  
Pre-operational SAR integration for a future-proof KFM hazard and EO stack.

© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[⬅ Back to STAC Missions](../README.md) ·  
[⚖ Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
