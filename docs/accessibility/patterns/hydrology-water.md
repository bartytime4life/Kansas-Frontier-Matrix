---
title: "💧 Kansas Frontier Matrix — Accessible Hydrology, Water, and Drought Data Standards (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/hydrology-water.md"
version: "v10.4.1"
last_updated: "2025-11-16"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-hydrology-water-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.3"
status: "Active / Enforced"
doc_kind: "Pattern"
intent: "a11y-hydrology-water"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Medium-Risk"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "KFM Hydrology Working Group · FAIR+CARE Council"
risk_category: "Medium"
redaction_required: true
provenance_chain:
  - "docs/accessibility/patterns/hydrology-water.md@v10.0.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/a11y-hydrology-water.schema.json"
shape_schema_ref: "../../../schemas/shacl/a11y-hydrology-water-shape.ttl"
doc_uuid: "urn:kfm:doc:a11y-hydrology-water-v10.4.1"
semantic_document_id: "kfm-doc-a11y-hydrology-water"
event_source_id: "ledger:docs/accessibility/patterns/hydrology-water.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative hydrologic risk claims"
  - "alteration of historical records"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Public / Environmental Data"
jurisdiction: "Kansas / United States"
role: "a11y-pattern-hydrology-water"
lifecycle_stage: "stable"
ttl_policy: "Quarterly review"
sunset_policy: "Superseded upon next hydrology standard update"
---

<div align="center">

# 💧 **Kansas Frontier Matrix — Accessible Hydrology, Water, and Drought Data Standards**  
`docs/accessibility/patterns/hydrology-water.md`

**Purpose:**  
Establish accessibility, semantic, and ethical data standards for **hydrological datasets, drought/flood dashboards, and water resource models** within Kansas Frontier Matrix (KFM).  
Ensure that all water-related data — including streamflow, precipitation, drought indices, and groundwater levels — are **perceptually accessible**, **semantically transparent**, and **ethically governed** under **FAIR+CARE** principles.

![Badge Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)
![Badge FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![Badge License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![Badge Status](https://img.shields.io/badge/Status-Stable-success)

</div>

---

## 📘 Overview

KFM integrates multi-decade and multi-century hydrological records to map:

- River flow variability and flood history  
- Precipitation cycles and anomalies  
- Aquifer depletion and recharge trends  
- Drought severity and recovery timelines  

This pattern applies to:

- Historical flow archives and reconstructed hydrology  
- Real-time hydrology feeds and drought monitors  
- Groundwater level monitoring dashboards  
- Scenario modeling and Focus Mode hydrology narratives  

Goals:

- **Accessibility:** Make water data usable with screen readers, keyboards, and alternative input devices.  
- **Traceability:** Preserve full provenance and context for all hydrologic datasets.  
- **Ethics:** Frame water scarcity and flood risk within environmental justice and community resilience contexts.

---

## 🗂️ Directory Context

```text
docs/accessibility/
│
├── README.md
├── testing-guide.md
├── tokens.md
└── patterns/
    ├── hydrology-water.md              # This file
    ├── telemetry-streams.md
    ├── instrumentation-sensors.md
    ├── minerals-energy.md
    ├── ...
```

---

## 🧩 Hydrology Accessibility Principles

| Principle                    | Description                                                  | WCAG / FAIR+CARE Reference |
|-----------------------------|--------------------------------------------------------------|----------------------------|
| Semantic Measurement Labels | Each unit labeled with `<abbr>` and ARIA descriptions.      | WCAG 1.3.1 / 3.1.3         |
| Data Provenance Clarity     | Include `data-origin`, `data-license`, timestamps, and methods. | FAIR F-2                 |
| Dynamic Updates             | Live feeds use `aria-live="polite"` for updates.            | WCAG 4.1.3                 |
| Color & Pattern Distinction | Flood / drought zones encoded by color **and** pattern.     | WCAG 1.4.1                 |
| Temporal Navigation         | Time sliders & controls fully keyboard-accessible.          | WCAG 2.1.1                 |
| Ethical Context             | Drought and scarcity framed within environmental justice.   | CARE E-2 / FAIR+CARE Ethics |

---

## 🧭 Example Implementation (Hydrology Dashboard Component)

~~~html
<section aria-labelledby="hydrology-title" role="region">
  <h2 id="hydrology-title">Kansas Hydrology Dashboard</h2>
  <p role="note">
    Real-time streamflow, groundwater, and precipitation conditions — FAIR+CARE validated hydrologic datasets.
  </p>

  <figure role="group" aria-labelledby="streamflow-caption">
    <canvas
      role="img"
      aria-label="Streamflow rates from 1950 to 2025 by decade for major Kansas rivers"
    ></canvas>
    <figcaption id="streamflow-caption">
      Streamflow rates by decade (cubic feet per second).
    </figcaption>
  </figure>

  <label for="timeslider">Select year:</label>
  <input
    type="range"
    id="timeslider"
    name="year"
    min="1950"
    max="2025"
    value="2020"
    aria-valuemin="1950"
    aria-valuemax="2025"
    aria-valuenow="2020"
    aria-label="Year slider for hydrology data"
  />

  <div role="status" aria-live="polite" id="data-status">
    Displaying data for 2020.
  </div>
</section>
~~~

### Implementation Notes

- Provide explicit measurement units (e.g., `cfs`, `mm`, `acre-ft`) in both text and ARIA labels.  
- Announce slider changes via `aria-live` when the user stops adjusting (debounced to avoid spam).  
- Ensure charts have descriptive captions and `role="img"` + `aria-label` for AT users.  
- Provide alternative tabular views or downloadable CSV/JSON for charts when possible.

---

## 🎨 Design Tokens for Hydrology UI

| Token                 | Description                         | Example Value |
|-----------------------|-------------------------------------|---------------|
| hydro.bg.color        | Background for hydrology panels     | #E3F2FD       |
| hydro.water.color     | Primary river/water tone            | #2196F3       |
| hydro.drought.color   | Drought overlay                     | #FFB74D       |
| hydro.flood.color     | Flood zone highlight                | #1565C0       |
| hydro.focus.color     | Focus ring color                    | #FFD54F       |
| hydro.alert.color     | Severe condition alert color        | #D32F2F       |

---

## 🧾 FAIR+CARE Hydrology Metadata Schema

| Field            | Description                          | Example                                                  |
|------------------|--------------------------------------|----------------------------------------------------------|
| data-origin      | Data custodian / monitoring agency   | "USGS / NOAA WaterWatch / KFM Hydrology Team"           |
| data-license     | Dataset license                      | "CC-BY 4.0"                                              |
| data-sensitivity | Data privacy & precision level       | "Low"                                                    |
| data-consent     | Consent for community display        | true                                                     |
| data-ethics-reviewed | FAIR+CARE validation flag        | true                                                     |
| data-provenance  | Short description of data lineage    | "USGS StreamGauge 06893000 (1949–2025) + KFM interpolation" |

### Example JSON

~~~json
{
  "data-origin": "USGS / NOAA WaterWatch",
  "data-license": "CC-BY 4.0",
  "data-sensitivity": "Low",
  "data-consent": true,
  "data-ethics-reviewed": true,
  "data-provenance": "Derived from USGS StreamGauge 06893000 (1949–2025)"
}
~~~

---

## ⚙️ Keyboard & ARIA Interaction Matrix

| Key / Attribute    | Action                                       | Accessibility Output                    |
|--------------------|----------------------------------------------|-----------------------------------------|
| Tab                | Moves between chart, slider, and summary     | Predictable, cyclical order             |
| Arrow Keys         | Adjusts year slider                          | Announces "Year set to YYYY" via status |
| Enter / Space      | Confirms toggle or button action             | Announces which dataset was updated     |
| Esc                | Cancels zoom or closes detail modal          | Returns focus to main hydrology heading |
| aria-live="polite" | Announces new data after updates             | "Data updated for 2023 streamflow."     |

---

## 🧪 Validation Workflows

| Tool            | Scope                                       | Output                                      |
|-----------------|---------------------------------------------|---------------------------------------------|
| axe-core        | Hydrology dashboard structure + ARIA roles  | a11y_hydrology.json                         |
| Lighthouse CI   | Motion control, focus state, color contrast | lighthouse_hydrology.json                   |
| jest-axe        | Component-level hydrology widget tests      | a11y_hydrology_components.json              |
| Faircare Script | Ethics/consent & environmental justice audit| hydrology_audit.json                        |

Validation confirms:

- Time sliders and charts are operable via keyboard only.  
- Live updates for hydrologic changes are informative but not overwhelming.  
- All human-relevant risk language (e.g., flood warnings) is precise, non-alarmist, and contextualized.

---

## ⚖️ FAIR+CARE Integration

| Principle           | Implementation                                                                    |
|---------------------|------------------------------------------------------------------------------------|
| Collective Benefit  | Hydrologic transparency supports shared water management and risk awareness.      |
| Authority to Control| Communities and agencies decide display of well locations, small systems, etc.    |
| Responsibility      | Each dataset linked to clearly documented provenance, method, and uncertainty.    |
| Ethics              | Communications emphasize resilience and adaptation, not fear or blame.            |

---

## 🕰️ Version History

| Version | Date       | Author             | Summary                                                                                         |
|--------:|------------|--------------------|-------------------------------------------------------------------------------------------------|
| v10.4.1 | 2025-11-16 | Accessibility Council | Upgraded to KFM-MDP v10.4.3; added extended metadata, clarified ARIA/time slider semantics, and ensured one-box-safe formatting. |
| v10.0.0 | 2025-11-11 | FAIR+CARE Council  | Introduced hydrology accessibility standard with semantic units, ARIA timeline navigation, and ethics metadata schema. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Developed under **Master Coder Protocol v6.3** · Verified by **FAIR+CARE Council**  
[⬅ Back to Accessibility Patterns Index](../README.md)

</div>