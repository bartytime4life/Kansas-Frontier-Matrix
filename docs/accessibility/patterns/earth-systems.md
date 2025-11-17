---
title: "🌍 Kansas Frontier Matrix — Accessible Earth Systems, Soil, and Geophysical Data Standards (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/earth-systems.md"
version: "v10.4.1"
last_updated: "2025-11-16"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-earth-systems-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.3"
status: "Active / Enforced"
doc_kind: "Pattern"
intent: "accessible-earth-systems"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium-Risk"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "KFM Accessibility Council · KGS · NRCS · FAIR+CARE Council"
risk_category: "Medium"
redaction_required: true
provenance_chain:
  - "docs/accessibility/patterns/earth-systems.md@v10.0.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  schema_org: "Dataset"
  cidoc: "E26 Physical Feature"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/a11y-earth-systems.schema.json"
shape_schema_ref: "../../../schemas/shacl/a11y-earth-systems-shape.ttl"
doc_uuid: "urn:kfm:doc:a11y-earth-systems-v10.4.1"
semantic_document_id: "kfm-doc-a11y-earth-systems"
event_source_id: "ledger:docs/accessibility/patterns/earth-systems.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "speculative geologic claims"
  - "removal of cultural-consent warnings"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Earth Systems / Geoscience"
jurisdiction: "Kansas / United States"
role: "a11y-pattern-earth"
lifecycle_stage: "stable"
ttl_policy: "Quarterly review"
sunset_policy: "Superseded upon next earth-systems update"
---

<div align="center">

# 🌍 **Kansas Frontier Matrix — Accessible Earth Systems, Soil, and Geophysical Data Standards**  
`docs/accessibility/patterns/earth-systems.md`

**Purpose:**  
Define accessibility, visualization, and **FAIR+CARE-governed** data-ethics protocols for **soil**, **geology**, **fault systems**, **seismic activity**, and **subsurface datasets** within the Kansas Frontier Matrix (KFM).  
Ensure Earth data layers are **accessible**, **semantically annotated**, **machine- and human-readable**, and **culturally respectful**, especially where geology intersects with tribal lands or heritage territories.

![Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![Status](https://img.shields.io/badge/Status-Active-success)

</div>

---

## 📘 Overview

Earth system datasets within KFM integrate:

- Soil horizons, texture, and moisture  
- Lithology, bedrock, mineral content  
- Seismic faults, event logs, and hazard layers  
- Geophysical surveys, borehole archives, magnetics/gravimetry  
- Time-variant subsurface models  

These standards ensure that both **historical archives** and **modern sensor-driven datasets** are:

- **WCAG compliant**  
- **Cognitively accessible**  
- **FAIR+CARE certified**  
- **Governance-traceable**  
- **Fully keyboard operable**  

---

## 🗂️ Directory Context

```text
docs/accessibility/
│
└── patterns/
    ├── earth-systems.md    # This document
    ├── hydrology-water.md
    ├── soil-health.md
    ├── minerals-energy.md
    └── geology/
```

---

## 🧩 Accessibility & Geophysical Data Principles

| Principle | Description | Standard Reference |
|----------|-------------|-------------------|
| **Semantic Layers** | Each layer uses explicit ARIA labeling + metadata. | WCAG 1.3.1 / ISO 19157 |
| **3D Scene Accessibility** | Geological 3D viewers support arrow-key panning + tab-traversable UI. | WCAG 2.1.1 |
| **Color & Pattern Encoding** | Geologic units use color + hatch patterns for colorblind safety. | WCAG 1.4.1 |
| **Cultural Consent** | Sensitive tribal geology masked unless explicitly approved. | CARE A-2 |
| **Measurement Readability** | All units wrapped in `<abbr>` with readable expansions. | WCAG 3.1.3 |
| **Provenance Transparency** | Subsurface data includes sampling dates, borehole IDs, and custodians. | FAIR F-2 |

---

## 🧭 Example Implementation (Soil + Subsurface Layers)

```html
<section aria-labelledby="earth-systems-title" role="region" data-fair-consent="approved">
  <h2 id="earth-systems-title">Kansas Soil & Subsurface Geology Map</h2>
  <p role="note">
    Interactive map showing soil composition and depth strata. FAIR+CARE reviewed for cultural and environmental sensitivity.
  </p>

  <div id="geology-map" role="application" aria-roledescription="Geologic map viewer">
    <button aria-label="Toggle Soil Layer (0–1m depth)">Soil Layer</button>
    <button aria-label="Toggle Subsurface Layer (1–5m depth)">Subsurface Layer</button>
    <button aria-label="Toggle Seismic Faults">Seismic Faults</button>
  </div>

  <p role="contentinfo">
    Data derived from USDA NRCS, USGS Earth Explorer, and Kansas Geological Survey archives.
  </p>
</section>
```

**Accessibility Notes**

- Soil and rock units must include **non-color visual differentiation**.  
- Fault lines require **≥4.5:1 contrast** and text descriptors.  
- Seismic markers grouped logically for screen reader traversal.

---

## 🎨 Design Tokens for Geophysical Visualization

| Token | Description | Example Value |
|--------|--------------|----------------|
| `earth.bg.color` | Map background | `#ECEFF1` |
| `earth.soil.color` | Soil unit tone | `#A1887F` |
| `earth.rock.color` | Lithology / bedrock | `#5D4037` |
| `earth.fault.color` | Active fault highlight | `#E53935` |
| `earth.seismic.color` | Seismic event marker | `#4FC3F7` |
| `earth.focus.color` | Keyboard focus ring | `#FFD54F` |

---

## 🧾 FAIR+CARE Earth Systems Metadata Schema

```json
{
  "data-origin": "USGS / KGS / USDA NRCS",
  "data-license": "CC-BY 4.0",
  "data-consent": true,
  "data-ethics-reviewed": true,
  "data-provenance": "Kansas Geological Survey borehole archive 1955–2020",
  "data-sensitivity": "Restricted"
}
```

**Metadata Must Include**

- Source + dataset lineage  
- Sampling methodology  
- Resolution (spatial + temporal)  
- Accuracy + uncertainty  
- Custodian + access class  
- Cultural consent flags

---

## ⚙️ Keyboard & ARIA Interaction Matrix

| Key | Function | Behavior |
|-----|----------|----------|
| `Tab` | Move between controls | Predictable traversal |
| `Arrow Keys` | Pan / rotate geology scene | “Panned east 10km.” |
| `Enter` | Toggle layers | Confirms via polite live region |
| `Esc` | Exit map focus | Restores previous focus |
| `aria-live="polite"` | Announce layer changes | “Subsurface layer enabled.” |

---

## 🧪 Validation Workflows

| Tool | Scope | Output |
|-------|--------|--------|
| **axe-core** | ARIA + semantic labeling checks | `a11y_earth_systems.json` |
| **Lighthouse CI** | 3D scene focus + keyboard nav | `lighthouse_earth_systems.json` |
| **jest-axe** | Component-level tests | `a11y_earth_components.json` |
| **Faircare Audit** | Consent + cultural sensitivity validation | `earth_systems_audit.json` |

---

## ⚖️ FAIR+CARE Integration

| Principle | Implementation |
|----------|----------------|
| Collective Benefit | Supports environmental literacy and stewardship. |
| Authority to Control | Custodians approve geological visibility. |
| Responsibility | Full provenance stored in governance ledger. |
| Ethics | Geology near cultural areas masked unless explicitly released. |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|--------:|------|--------|---------|
| v10.4.1 | 2025-11-16 | Accessibility Council | Brought into full KFM-MDP v10.4.3 compliance; added metadata, consent flags, upgraded structure + tokens. |
| v10.0.0 | 2025-11-11 | FAIR+CARE Council | Initial Earth Systems Accessibility Pattern. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
FAIR+CARE Council · Master Coder Protocol v6.3  
[⬅ Back to Accessibility Patterns Index](../README.md)

</div>