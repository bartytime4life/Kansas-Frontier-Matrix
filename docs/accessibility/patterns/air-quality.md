---
title: "🌤️ Kansas Frontier Matrix — Accessible Air Quality, Pollution, and Atmospheric Health Data Standards (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/air-quality.md"
version: "v10.4.1"
last_updated: "2025-11-16"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-air-quality-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.3"
status: "Active / Enforced"
doc_kind: "Pattern"
intent: "air-quality-a11y"
fair_category: "F1-A1-I1-R1"
care_label: "Public Health / Environmental"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "KFM Environmental Council · FAIR+CARE Council"
risk_category: "Medium"
redaction_required: false
provenance_chain:
  - "docs/accessibility/patterns/air-quality.md@v10.0.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  schema_org: "Dataset"
  cidoc: "E29 Design or Procedure"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/a11y-air-quality.schema.json"
shape_schema_ref: "../../../schemas/shacl/a11y-air-quality-shape.ttl"
doc_uuid: "urn:kfm:doc:a11y-air-quality-v10.4.1"
semantic_document_id: "kfm-doc-a11y-air-quality"
event_source_id: "ledger:docs/accessibility/patterns/air-quality.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative health risk claims"
  - "removing uncertainty or provenance fields"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Air Quality · Pollution · Atmospheric Health"
jurisdiction: "Kansas / United States"
role: "a11y-pattern-air-quality"
lifecycle_stage: "stable"
ttl_policy: "Quarterly review"
sunset_policy: "Superseded upon next air-quality pattern update"
---

<div align="center">

# 🌤️ **Kansas Frontier Matrix — Accessible Air Quality, Pollution, and Atmospheric Health Data Standards**  
`docs/accessibility/patterns/air-quality.md`

**Purpose:**  
Define accessibility, visual contrast, and ethical representation standards for **air quality indices (AQI)**, **pollution monitoring dashboards**, and **public health risk visualizations** across the Kansas Frontier Matrix (KFM).  
Ensure that air and atmospheric health datasets are **perceivable**, **culturally contextualized**, and **FAIR+CARE governed** for open and equitable environmental communication.

![Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![Status](https://img.shields.io/badge/Status-Active-success)

</div>

---

## 📘 Overview

Air quality and atmospheric health metrics in KFM (e.g., **PM₂.₅**, **PM₁₀**, **NO₂**, **O₃**, **SO₂**, **CO**, pollen indices, and smoke plumes) power:

- Environmental justice analyses  
- Public health warnings and advisories  
- Historical climate and pollution archives  
- Focus Mode explanations and Story Nodes  

This pattern ensures that:

- AQI visualizations remain **clear and navigable** for all users.  
- Risk messaging is **responsible and non-stigmatizing**.  
- Datasets communicate **uncertainty, source, and time context**.

---

## 🗂️ Directory Context

```text
docs/accessibility/
│
└── patterns/
    ├── air-quality.md           # This file
    ├── climate-weather.md
    ├── hazards-emergency.md
    └── environmental-dashboards.md
```

---

## 🧩 Air Quality Accessibility Principles

| Principle           | Description                                                                 | WCAG / FAIR+CARE Reference |
|---------------------|-----------------------------------------------------------------------------|----------------------------|
| Contrast Clarity    | AQI colors maintain ≥ 4.5:1 contrast; use patterns in legends if needed.    | WCAG 1.4.3                 |
| Semantic Indicators | Numeric AQI paired with plain-language categories (Good, Moderate, etc.).   | WCAG 1.1.1                 |
| Live Updates        | Dynamic AQI changes announced via `aria-live="polite"` (rate-limited).     | WCAG 4.1.3                 |
| Ethical Messaging   | Risk language is factual, non-alarmist, and culturally respectful.          | CARE E-1                   |
| Temporal Context    | Every chart shows clearly labeled timestamps and averaging intervals.       | FAIR F-2                   |
| Assistive Navigation| AQI widgets, graphs, and filters fully operable via keyboard & screen reader.| WCAG 2.1.1                |

---

## 🧭 Example Implementation (Air Quality Dashboard)

```html
<section aria-labelledby="air-dashboard-title" role="region">
  <h2 id="air-dashboard-title">Air Quality Index — Kansas Region</h2>

  <div role="status" aria-live="polite" id="aqi-status">
    Current AQI: 52 — Moderate (PM2.5 primary pollutant)
  </div>

  <figure role="group" aria-labelledby="aqi-figure-caption">
    <figcaption id="aqi-figure-caption">
      Daily Air Quality Trends (last 7 days, units: µg/m³)
    </figcaption>
    <canvas
      role="img"
      aria-label="Line chart of PM2.5 concentration by day with 7-day average 52 micrograms per cubic meter."
    ></canvas>
  </figure>

  <p role="note">
    Data sourced from EPA AirNow and Kansas Department of Health and Environment (KDHE).
  </p>
</section>
```

### Accessibility Features

- AQI values combine **numeric index**, **category name**, and **primary pollutant**.  
- Canvas-based chart uses `role="img"` with descriptive `aria-label` and `<figcaption>`.  
- Live updates broadcast via `aria-live="polite"` and are **debounced** to prevent AT overload.  

---

## 🎨 Design Tokens for Air Quality UIs

| Token              | Description                     | Example Value |
|--------------------|---------------------------------|---------------|
| `aqi.good`         | Good air quality color          | `#43A047`     |
| `aqi.moderate`     | Moderate condition color        | `#FFEB3B`     |
| `aqi.unhealthy`    | Unhealthy state color           | `#F57C00`     |
| `aqi.hazardous`    | Hazardous condition color       | `#B71C1C`     |
| `aqi.text.color`   | AQI numeric/label text          | `#212121`     |
| `aqi.focus.color`  | Focus outline for AQI widgets   | `#FFD54F`     |

> Palette must be tested against `color.background` in both **light** and **dark** modes.

---

## 🧾 FAIR+CARE Air Quality Metadata Schema

```json
{
  "data-origin": "EPA AirNow / KDHE",
  "data-license": "CC-BY 4.0",
  "data-ethics-reviewed": true,
  "data-sensitivity": "Public",
  "data-consent": true,
  "data-pollutants": ["PM2.5", "PM10", "O3"],
  "data-interval": "Hourly, 24-hour rolling averages",
  "data-provenance": "EPA SensorNet v2.1, KDHE atmospheric feed 2025-11-01T00:00Z",
  "data-uncertainty": "±3 µg/m³",
  "data-health-framework": "US EPA AQI Categories"
}
```

**Required**

- **Origin**, **license**, **sensitivity**, **consent**, **pollutant list**  
- Exposure **interval** and **uncertainty** fields  
- Clear indication of the health framework used (e.g., US EPA AQI)

---

## ⚙️ ARIA & Keyboard Interaction Matrix

| Key / Attribute    | Behavior                                       | Feedback                                |
|--------------------|------------------------------------------------|-----------------------------------------|
| `Tab`              | Move between AQI summary, filters, and chart   | Announces region + control name         |
| `Arrow Keys`       | Navigate along time series or discrete points  | Announces date, AQI, category, pollutant|
| `Enter`            | Toggle pollutant filters or open details       | “Filter applied: PM₂.₅ and O₃.”         |
| `Esc`              | Close any detail/overlay panels                | Returns focus to dashboard heading      |
| `aria-live="polite"` | Announce AQI updates                         | “AQI updated: 58 — Moderate, PM₂.₅.”    |

---

## 🧪 Validation Workflows

| Tool              | Scope                                      | Output                                         |
|-------------------|--------------------------------------------|------------------------------------------------|
| **axe-core**      | ARIA structure and landmark checks         | `a11y_air_quality.json`                       |
| **Lighthouse CI** | Contrast, keyboard, and motion auditing    | `lighthouse_air_quality.json`                 |
| **jest-axe**      | Component-level AQI widget testing         | `a11y_air_quality_components.json`            |
| **Faircare Script**| Ethics review (tone, equity, consent)     | `air_quality_audit.json`                      |

Validation must confirm:

- All color encodings have textual equivalents.  
- Risk language remains factual and non-stigmatizing.  
- Uncertainty, time interval, and provenance are exposed to the user.

---

## ⚖️ FAIR+CARE Integration

| Principle           | Implementation                                                                  |
|---------------------|----------------------------------------------------------------------------------|
| Collective Benefit  | AQI data used to support informed health and environmental decisions.           |
| Authority to Control| Agencies and communities may govern how local air-quality data is shown.        |
| Responsibility      | Transparent methodology, uncertainty, and update cadence disclosed.             |
| Ethics              | Visualizations avoid blaming communities; emphasize shared responsibility.      |

---

## 🕰️ Version History

| Version | Date       | Author              | Summary                                                                                          |
|--------:|------------|---------------------|--------------------------------------------------------------------------------------------------|
| v10.4.1 | 2025-11-16 | Accessibility Council | Upgraded to KFM-MDP v10.4.3; extended metadata schema, added clearer ethics rules and interaction matrix. |
| v10.0.0 | 2025-11-11 | FAIR+CARE Council   | Initial air quality pattern for KFM dashboards, with AQI semantics and FAIR+CARE framing.       |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Maintained under **Master Coder Protocol v6.3** · Verified by **FAIR+CARE Council**  
[⬅ Back to Accessibility Patterns Index](../README.md)

</div>