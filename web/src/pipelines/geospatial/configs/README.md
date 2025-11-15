---
title: "⚙️ Kansas Frontier Matrix — Geospatial Pipeline Configuration Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/src/pipelines/geospatial/configs/README.md"
version: "v10.4.0"
last_updated: "2025-11-15"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/web-pipelines-geospatial-configs-v1.json"
governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Configs Overview"
intent: "geospatial-pipeline-configs"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk (config-level only)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: "Conditional (for sovereignty masking configs)"
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
provenance_chain:
  - "web/src/pipelines/geospatial/configs/README.md@v10.3.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "CreativeWork"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"
  prov_o: "prov:Plan"
json_schema_ref: "../../../../../../schemas/json/web-pipelines-geospatial-configs.schema.json"
shape_schema_ref: "../../../../../../schemas/shacl/web-pipelines-geospatial-configs-shape.ttl"
doc_uuid: "urn:kfm:doc:web-pipelines-geospatial-configs-v10.4.0"
semantic_document_id: "kfm-doc-web-pipelines-geospatial-configs"
event_source_id: "ledger:web/src/pipelines/geospatial/configs/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Forbidden (configs must not be interpreted by AI)"
ai_transform_permissions:
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "summaries"
  - "speculative additions"
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public (config only)"
role: "configs-overview"
lifecycle_stage: "stable"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded on next geospatial pipeline config update"
---

<div align="center">

# ⚙️ **Kansas Frontier Matrix — Geospatial Pipeline Configuration Overview**  
`web/src/pipelines/geospatial/configs/README.md`

**Purpose:**  
Document the **configuration layer** used by the geospatial pipelines in the Kansas Frontier Matrix (KFM) Web Platform.  
These configs govern CRS normalization, masking parameters (H3), temporal slicing rules, spatial styling presets,  
Story Node overlay controls, and governance & sovereignty constraints—ensuring all geospatial flows remain  
deterministic, FAIR+CARE-aligned, and ethically governed.

</div>

---

# 📘 Overview

The **Geospatial Configuration Layer** defines **parameterized rules** used by pipeline modules:

- `loadFootprints.ts`  
- `applyTemporalFilters.ts`  
- `maskSensitiveGeometry.ts`  
- `geometryTransform.ts`  
- `mergeLayersForMap.ts`  
- `spatialTelemetry.ts`  

Configurations ensure that:

- Spatial operations behave consistently  
- CARE-required masking rules always apply  
- Temporal filters follow OWL-Time semantics  
- Maps render ethically and accessibly  
- Transform logic remains reproducible  
- Sovereignty boundaries remain protected  
- Telemetry outputs follow KFM schemas  

Configs represent **ethical, spatial, and computational constraints**, not business logic.

---

# 🧱 Directory Structure

~~~text
web/src/pipelines/geospatial/configs/
├── crs.config.ts                    # CRS normalization + transform rules
├── masking.config.ts                # CARE + sovereignty masking policies (H3 r7+)
├── temporal.config.ts               # Temporal slice/interval rules (OWL-Time)
├── merge.config.ts                  # Layer merge priorities + governance overlays
├── styling.config.ts                # MapLibre layer styling presets (accessible colors)
└── telemetry.config.ts              # Spatial telemetry event configuration
~~~

---

# 🧩 Configuration Modules

## 1. **CRS Configuration (`crs.config.ts`)**

Controls:

- Allowed input CRS  
- Required output CRS (EPSG:4326 baseline)  
- Datum transformation rules  
- Warnings for invalid transforms  
- Thresholds for geometry simplification  

Guarantees:

- Perfect predictability of coordinate normalization  
- No map-render jitter from poor CRS handling  

---

## 2. **Masking Configuration (`masking.config.ts`)**

Controls all CARE masking logic:

- H3 generalization (default: **r7**)  
- Masking behavior for:
  - Indigenous sovereignty locations  
  - Archaeological sites  
  - Sacred/culturally restricted geography  
- Blur/hex/centroid-replacement rules  
- Requirements for provenance metadata  

Guarantees:

- No unsafe coordinates are passed into UI  
- Masking is deterministic and reviewable  
- Masking metadata always accompanies output  

---

## 3. **Temporal Configuration (`temporal.config.ts`)**

Controls temporal slicing under OWL-Time:

- Timeline → geometry filtering rules  
- Handling of fuzzy or uncertain intervals  
- Intersection logic for Story Node footprints  
- Aggregation bins for deep-time/modern data  

Guarantees:

- Temporal consistency across:
  - Focus Mode  
  - Story Nodes  
  - Map layers  
  - STAC filters  

---

## 4. **Merge Configuration (`merge.config.ts`)**

Controls:

- Layer merge priority rules  
- Overlay transparency/opacity  
- Geometry conflict resolution  
- Provenance + CARE label overlay rules  
- Story Node footprint → STAC → governance compositing order  

Ensures:

- Unified map layers remain ethically correct  
- Provenance always visible  

---

## 5. **Styling Configuration (`styling.config.ts`)**

Contains accessible visual presets:

- MapLibre colors  
- CARE indicator colors  
- Sovereignty & mask overlays  
- Focus Mode halos  
- Story Node geometry outlines  
- COG footprint borders  

All palettes must be:

- **WCAG AA compliant**
- Consistent across light/dark themes  
- Approved by FAIR+CARE reviewers  

---

## 6. **Telemetry Configuration (`telemetry.config.ts`)**

Defines:

- Allowed spatial telemetry event types  
- Aggregation windows  
- Sustainability metadata rules  
- Spatial → narrative → A11y relationships  
- Governance metadata inclusion rules  

Ensures:

- Telemetry is non-PII  
- Events feed properly into `focus-telemetry.json`  
- Sustainability KPIs remain accurate  

---

# 🔐 FAIR+CARE & Governance Constraints

Configs must:

- Never weaken ethical rules  
- Support all masking requirements  
- Respect sovereignty and cultural rights  
- Prevent exposure of sensitive geographic data  
- Maintain provenance visibility  
- Enforce allowed AI behaviors  

Examples:

- Mask depth cannot be lowered below H3 r7  
- Sensitive datasets must always render in generalized form  
- No configuration may allow bypassing CARE controls  

---

# 🧪 Testing Expectations

Each config file must include:

- **Unit tests** verifying allowed parameter ranges  
- **Integration tests** confirming correct pipeline interpretation  
- **Governance tests** checking CARE metadata propagation  
- **A11y color contrast tests** for styling configs  
- **Telemetry schema tests**  

Tests exist under:

~~~text
tests/unit/web/pipelines/geospatial/configs/**
tests/integration/web/pipelines/geospatial/configs/**
~~~

---

# 🕰 Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v10.4.0 | 2025-11-15 | Full KFM-MDP v10.4 configuration overview added |
| v10.3.2 | 2025-11-14 | Added sovereignty masking + styling rules |
| v10.3.1 | 2025-11-13 | Initial config module structure |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
FAIR+CARE Certified · Public Document · Version-Pinned  
Validated under MCP-DL v6.3 and KFM-MDP v10.4  

</div>