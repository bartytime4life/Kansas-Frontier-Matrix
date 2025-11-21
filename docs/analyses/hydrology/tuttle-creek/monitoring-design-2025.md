---
title: "🧪 Kansas Frontier Matrix — Tuttle Creek WID 2025 Monitoring & QA/QC Design"
path: "docs/analyses/hydrology/tuttle-creek/monitoring-design-2025.md"
version: "v11.0.0"
last_updated: "2025-11-21"
review_cycle: "Annual / Hydrology & Hazards Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/docs-analyses-hydrology-wid-monitoring-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Analysis"
intent: "hydrology-tuttle-creek-monitoring-design"
semantic_document_id: "kfm-analyses-hydrology-tuttle-creek-monitoring-2025"
doc_uuid: "urn:kfm:docs:analyses:hydrology:tuttle-creek:monitoring-design-2025:v11.0.0"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🧪 **Tuttle Creek WID 2025 — Monitoring & QA/QC Design**  
`docs/analyses/hydrology/tuttle-creek/monitoring-design-2025.md`

**Purpose:**  
Define the v11-compliant monitoring system, instrumentation network, QA/QC frameworks, and  
analytical protocols supporting the **2025 Water Injection Dredging (WID)** demonstration at Tuttle Creek  
Lake, enabling ETL → STAC → Neo4j → Focus Mode integration.

</div>

---

# 📘 Overview

This document provides the **technical monitoring design** for the 2025 Water Injection Dredging (WID)  
demonstration at **Tuttle Creek Lake**. The monitoring system is engineered to:

- Quantify **water-quality impacts**  
- Track **density-current behavior**  
- Protect downstream aquatic ecosystems  
- Generate **ETL-ready datasets**  
- Feed WID datasets into KFM’s **STAC catalog**, **CIDOC-CRM graph**, and **Story Node v3** narratives  

This design follows MCP-DL v6.3, FAIR+CARE ethics, and KFM’s deterministic hydrology standards.

---

# 🌊 1. Monitoring Objectives (Science & Compliance)

## 🎯 Primary goals

- Detect effects of WID-induced sediment resuspension.  
- Quantify downstream transport and attenuation of the density current.  
- Ensure compliance with DO, turbidity, and nutrient thresholds.  
- Provide high-frequency data for Focus Mode pattern detection.  
- Generate reproducible time-series for cross-year comparisons.

## 🧩 Key indicators

- **Turbidity (NTU)**  
- **Total Suspended Solids (TSS)**  
- **Dissolved Oxygen (DO)**  
- **Temperature profiles & stratification**  
- **Nutrients:** NH₄, NO₃, TN, TP  
- **Sediment granulometry**  
- **Biological indicators:** mussels, fish, macroinvertebrates  
- **Hydraulics:** gate flow, reservoir elevation, tailwater stage  

---

# 🛰️ 2. Spatial Monitoring Network

The Tuttle Creek WID 2025 monitoring network uses a **three-zone architecture**:

```text
Zone A — In-Reservoir (WID Operations Zone)
Zone B — Dam & Tailwater
Zone C — Big Blue River Downstream Corridor (0–15 miles)
```

## 🗺️ Zone A — Reservoir (WID Operating Area)

| Station | Purpose | Sensors | Frequency |
|--------:|---------|----------|-----------|
| A1 | Near-field turbidity plume tracking | Turbidity, DO, temperature | 1–5 min |
| A2 | Density current profile | Acoustic backscatter, ADCP | 1–5 min |
| A3 | Control station (background) | DO/Turbidity/Temperature | 15 min |

## 🏗️ Zone B — Dam & Tailwater

| Station | Purpose | Sensors | Frequency |
|--------:|---------|----------|-----------|
| B1 | Outlet monitoring | Turbidity, DO, nutrients | 1–5 min |
| B2 | Gate hydrodynamics | Flow, gate position, stage | 1–5 min |
| B3 | Biological transects | Macroinvertebrates, fish | Daily/episodic |

## 🌎 Zone C — Downstream River (0–15 miles)

| Station | Purpose | Sensors | Frequency |
|--------:|---------|----------|-----------|
| C1 | Near-field deposition zone | TSS, turbidity | 15 min |
| C2 | Mid-reach | DO, turbidity | 15 min |
| C3 | Far-reach recovery | DO, nutrients, fish community | Hourly/daily |

---

# 🔧 3. Instrumentation Specifications

## 🧭 Sensor Suite

- **YSI EXO2 Multiparameter Sondes**  
  - DO (optical), temperature, conductivity, pH, turbidity  
- **ADCP (Teledyne)**  
  - Density current mapping  
- **Laser In-Situ Sediment Monitors (LISST)**  
  - Particle-size & concentration  
- **Isco Samplers**  
  - Discrete samples for lab analysis  
- **HOBO / NexSens loggers**  
  - Redundant DO & turbidity

## 🏢 Calibration & QA/QC Cycles

- Pre-deployment calibration per manufacturer SOPs  
- Drift tests every **48 hours** during active WID operations  
- Duplicate sampling at **10%** of sites  
- Reference standard checks:

  - Formazin turbidity standards  
  - Winkler DO titration for sensor validation  
  - Certified nutrient standards for autosamplers

- Chain-of-custody tracking for discrete laboratory samples  

---

# 🧪 4. Laboratory Analyses

All discrete samples processed at accredited labs:

| Parameter | Method | Standard |
|----------|--------|---------|
| TSS | Gravimetric | EPA 160.2 |
| TP, TN | Colorimetric digestion | EPA 365.1 |
| NO₃, NH₄ | Ion chromatography | EPA 300 |
| Metals | ICP-MS | EPA 200.8 |
| Granulometry | Laser diffraction | ASTM D4221 |

Deliverables:

- CSV datasets (processed)  
- QA/QC summary sheets  
- STAC Items reflecting time, place, parameter type  

---

# 🚨 5. Trigger Levels & Mitigation

## 📉 Action thresholds

- **DO < 5 mg/L** → Increase monitoring, adjust WID track, potential pause.  
- **Turbidity exceedances** (per State standards) → Modify jet flow or halt operations.  
- **TSS spikes** → Assess plume confinement & density-current trajectory.

## 🛑 Shutdown conditions

- Massive DO sag affecting aquatic life.  
- Persistent turbidity above regulatory limits.  
- Rapid adverse biological indicators.

All triggers logged via PROV-O `prov:wasInformedBy` → Sensor Dataset → WID Event.

---

# 🛰 6. STAC Integration

Monitoring results should be cataloged under:

```text
data/stac/hydrology/tuttle-creek/
└── wid-2025-monitoring/
    ├── turbidity-a1.json
    ├── do-b1.json
    ├── tss-c1.json
    ├── adcp-density-current.json
    └── nutrients-b1.json
```

Each STAC Item MUST include:

- Geometry (point)  
- Date/time range  
- Parameter type  
- Instrument ID  
- Provider (USACE/KWO)  
- QA/QC notes  
- Link to raw + processed files  

---

# 🕸 7. Neo4j / CIDOC-CRM Mapping

Core entities:

- `E7 Activity: WID_Monitoring_2025`  
- `E53 Place`: reservoir, dam, downstream stations  
- `E73 InformationObject`: sensor datasets  
- `E29 DesignOrProcedure`: this monitoring plan  
- `E30 Measurement`: individual parameter readings  
- `geo:hasGeometry`: station coordinates  
- `time:hasTime`: timestamps  
- `prov:wasGeneratedBy`: sensor → dataset → WID activity  

Relationships enable Focus Mode to:

- Plot time-series  
- Compare parameter behavior pre/during/post WID  
- Trace monitoring design provenance  

---

# 📖 8. Story Node Narrative (Mini)

> **“Watching the Water During WID”**  
>  
> When Water Injection Dredging began at Tuttle Creek in 2025, the water became a laboratory.  
> Sensors hung in the reservoir, the dam tailwater, and miles downstream. Every minute, they sent  
> turbidity, oxygen, and nutrient readings through the system. Biologists surveyed fish, hydrologists  
> checked gate flows, and ADCP beams traced the dense near-bottom plume.  
>  
> The monitoring network was the safety net—ensuring engineers could push the experiment  
> without pushing the ecosystem too far.

---

# 🕰 Version History

- **v11.0.0 (2025-11-21):** Initial v11-compliant monitoring design specification.

---

[⬅️ Back to Tuttle Creek Index](README.md) • [🏠 KFM v11 Master Guide](../../../reference/kfm_v11_master_documentation.md) • [📂 Data Index](../../../data/README.md)

