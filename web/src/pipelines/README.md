---
title: "🚀 Kansas Frontier Matrix — Web Pipelines & Dataflow Orchestration (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/pipelines/README.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Continuous / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/web-pipelines-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🚀 **Kansas Frontier Matrix — Web Pipelines & Dataflow Orchestration**  
`web/src/pipelines/README.md`

**Purpose:**  
Define the **client-side dataflow pipelines** that orchestrate data retrieval, transformation, normalization, caching, telemetry emission, and governance checks for the Kansas Frontier Matrix (KFM) web platform.  
These pipelines unify **Focus Mode**, **STAC/DCAT**, **Neo4j**, **timeline**, and **layer** data into a coherent, reactive, FAIR+CARE-certified interface.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Pipeline%20Compliant-orange)]()  
[![Status](https://img.shields.io/badge/Status-Stable-success)]()  
[![License](https://img.shields.io/badge/License-MIT-green)]()

</div>

---

## 📘 Overview

The **Web Pipelines Layer** centralizes all multi-step client logic involving:

- Data aggregation from **STAC**, **DCAT**, **GraphQL**, **REST**, and **Focus Mode** APIs  
- Provenance & JSON-LD enrichment for UI components  
- CARE-aware redaction and governance checks  
- Client-side telemetry insertion (WebVitals, ethics, sustainability, navigation events)  
- Result caching & consistency rules for React components  
- Reactive timelines & synchronized map/timeline/focus updates  

These pipelines sit above `services/` and below React `hooks/`, forming the glue that links:

**Data → Semantics → Governance → UI → Telemetry.**

---

## 🗂️ Directory Layout (Pipeline Layer)

~~~~~text
web/src/pipelines/
├── README.md                     # This file
│
├── focusPipeline.ts              # Multi-stage Focus Mode assembly
├── stacPipeline.ts               # Multi-stage dataset/layer pipeline
├── entityPipeline.ts             # Unifies GraphQL entity lookups w/ lineage
├── timelinePipeline.ts           # Derived temporal aggregations + predictions
├── layerPipeline.ts              # Layer activation, presets, redaction logic
└── metadata.json                 # Pipeline-level governance + telemetry metadata
~~~~~

> **Note:** All pipeline outputs MUST go through `schemaGuards.ts` (utils) before reaching UI components.

---

## 🧩 Pipeline Architecture (Indented Mermaid)

~~~~~mermaid
flowchart TD
  A["Services Layer<br/>REST · GraphQL · STAC · DCAT"]
    --> B["Pipelines<br/>(focus · entity · stac · timeline · layers)"]
  B --> C["Enrichment<br/>JSON-LD · Provenance · CARE Flags"]
  C --> D["Validation<br/>schemaGuards.ts"]
  D --> E["Hooks<br/>(useFocus · useStac · useTimeline · useLayers)"]
  E --> F["UI Components<br/>MapView · Timeline · FocusPanel · StoryNode"]
  F --> G["Telemetry<br/>WebVitals · Ethics · A11y · Energy"]
~~~~~

---

## 🧠 Pipeline Definitions

### 1. **focusPipeline.ts**  
Orchestrates all steps for Focus Mode v2.4.

**Stages:**
- Fetch entity + subgraph (GraphQL)  
- Fetch STAC/DCAT metadata tied to entity  
- Merge JSON-LD provenance  
- Add explainability metadata  
- Insert CARE flags (sovereignty, sensitivity, restrictions)  
- Emit telemetry (AI depth, ethics events, latency, energy)  
- Validate with `schemaGuards.ts`  

**Consumers:**  
`useFocus` → `FocusPanel`, `MapView`, `TimelineView`  

---

### 2. **stacPipeline.ts**  
Normalizes STAC Items/Collections for use across map, timeline, and story nodes.

**Stages:**
- STAC search  
- Collection → Item flattening  
- Asset inspection (raster, vector, COG, NetCDF)  
- Build layer metadata + attribution  
- CARE-aware spatial masking  
- Version history detection  
- Validate with `schemaGuards.ts`  

**Consumers:**  
`useStac`, layer controls, legend systems  

---

### 3. **entityPipeline.ts**  
Combines GraphQL entity outputs with dataset provenance and relations.

**Stages:**
- Fetch entity node  
- Load related events, places, documents, datasets  
- Build unified entity descriptor with lineage & CARE flags  
- Validate with `schemaGuards.ts`  

**Consumers:**  
Entity drawers, Focus Mode, Story Nodes  

---

### 4. **timelinePipeline.ts**  
Derives denormalized temporal aggregates for UI.

**Stages:**
- Fetch events/stories/datasets with temporal extents  
- Build time buckets (annual, decadal, event clustering)  
- Merge predictive time bands (2030–2100 scenario rasters)  
- CARE-temporal redaction (historical sensitive events)  
- Validate with `schemaGuards.ts`  

**Consumers:**  
`TimelineView`, Focus Mode, predictive overlays  

---

### 5. **layerPipeline.ts**  
Applies semantic + governance transformations to map layers.

**Stages:**
- Load layer groups (hydrology, climate, hazards, treaties, ecology, archaeology)  
- Apply CARE governance (mask sites, obfuscate geom detail)  
- Resolve style tokens (tokens.css)  
- Tailwind class merging for legends  
- Validate output  

**Consumers:**  
MapView, LayerSwitcher, Legend systems  

---

## 🔐 FAIR+CARE Governance Integration

All pipelines must:

- Enforce `care_label` rules (public, sensitive, restricted)  
- Obey sovereignty restrictions  
- Mask coordinates for heritage/archaeology as required  
- Always output provenance fields:
  - `lineage`
  - `provenance`
  - `source_ids`
  - `ledger_refs`

Governance references for all pipelines resolved from:

```
../../../docs/reports/audit/web-governance-ledger.json
```

---

## 📡 Telemetry & Sustainability

All pipelines integrate `telemetryService.ts`:

- WebVitals (LCP, FID, CLS, TTFB)  
- Ethics events (CARE gating, masking triggers)  
- Focus reasoning depth  
- Dataset/layer usage  
- Estimated energy + CO₂e (UI action models)

Telemetry stored in:

```
../../../releases/v10.3.0/focus-telemetry.json
```

---

## ⚙️ Pipeline Validation

| Contract | Validator |
|----------|-----------|
| DTOs | `schemaGuards.ts` (strict) |
| Provenance | `provenance.ts` |
| A11y | CI accessibility scan |
| Ethics | CARE-flag enforcement tests |
| Security | CodeQL + Trivy |
| Telemetry | telemetry-export.yml |

Any pipeline violating MCP rules fails the build.

---

## 🧾 Example Pipeline Metadata Record (v10.3.1)

~~~~~json
{
  "id": "web_pipelines_v10.3.1",
  "pipelines": [
    "focusPipeline.ts",
    "stacPipeline.ts",
    "timelinePipeline.ts",
    "entityPipeline.ts",
    "layerPipeline.ts"
  ],
  "fairstatus": "certified",
  "a11y_compliant": true,
  "telemetry_linked": true,
  "checksum_verified": true,
  "ethics_gates_passed": true,
  "timestamp": "2025-11-13T17:44:00Z",
  "governance_ref": "docs/reports/audit/web-governance-ledger.json"
}
~~~~~

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---------|--------|---------|---------|
| v10.3.1 | 2025-11-13 | Web Architecture Team | Introduced pipeline layer; aligned with Focus v2.4, telemetry v3, and ethics-driven transformations. |

---

<div align="center">

**Kansas Frontier Matrix — Web Pipelines**  
Reactive Dataflow × FAIR+CARE × Provenance × Explainable AI  
© 2025 Kansas Frontier Matrix — MIT License  

[Back to Services](../services/README.md) · [Back to Source Index](../README.md)

</div>

