---
title: "🌤️ KFM v11 — Accessible Air Quality, Pollution, and Atmospheric Health Data Standards (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/air-quality.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
backward_compatibility: "Aligned with v10.x → v11.x air-quality a11y pattern contract"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../releases/v11.2.3/a11y-air-quality-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-air-quality-v2.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

doc_kind: "Pattern"
intent: "air-quality-a11y"
fair_category: "F1-A1-I1-R1"
care_label: "Public Health · Environmental · Sovereignty-Aware"

sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "KFM Environmental Council · FAIR+CARE Council"
risk_category: "Medium"
redaction_required: false

provenance_chain:
  - "docs/accessibility/patterns/air-quality.md@v10.0.0"

ontology_alignment:
  schema_org: "Dataset"
  cidoc: "E29 Design or Procedure"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"

json_schema_ref: "../../../schemas/json/a11y-air-quality.schema.json"
shape_schema_ref: "../../../schemas/shacl/a11y-air-quality-shape.ttl"

doc_uuid: "urn:kfm:doc:a11y-air-quality-v11.2.3"
semantic_document_id: "kfm-doc-a11y-air-quality"
event_source_id: "ledger:docs/accessibility/patterns/air-quality.md"
immutability_status: "version-pinned"

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
accessibility_compliance: "WCAG 2.1 AA+"
classification: "Air Quality · Pollution · Atmospheric Health"
jurisdiction: "Kansas / United States"
role: "a11y-pattern-air-quality"
lifecycle_stage: "stable"
ttl_policy: "Quarterly review"
sunset_policy: "Superseded upon next air-quality pattern update"
---

<div align="center">

# 🌤️ **KFM v11 — Accessible Air Quality, Pollution, and Atmospheric Health Data Standards**  
`docs/accessibility/patterns/air-quality.md`

**Purpose**  
Define accessibility, visual contrast, and ethical representation standards for  
**air quality indices (AQI)**, **pollution monitoring dashboards**, and **public health risk visualizations**  
across the Kansas Frontier Matrix (KFM).  

Ensure that air and atmospheric health datasets are **perceivable**, **culturally contextualized**,  
and **FAIR+CARE governed** for open and equitable environmental communication.

</div>

---

## 📘 1. Overview

Air quality and atmospheric health metrics in KFM (e.g., **PM₂.₅**, **PM₁₀**, **NO₂**, **O₃**, **SO₂**, **CO**, pollen indices, smoke plumes) power:

- Environmental justice analyses  
- Public health warnings and advisories  
- Historical climate and air pollution archives  
- Focus Mode v3 explanations and Story Nodes  

This pattern ensures that:

- AQI visualizations are **clear, navigable, and screen-reader compatible**  
- Risk messaging is **responsible, non-stigmatizing, and culturally respectful**  
- Datasets communicate **uncertainty, source, and temporal context**  
- Indigenous and vulnerable communities are handled with **CARE**, sovereignty-aware framing, and masking where needed  

---

## 🗂️ 2. Directory Context (Emoji-Prefix Standard)

~~~text
docs/accessibility/
│
└── 📁 patterns/
    ├── 📄 air-quality.md               # This file
    ├── 📄 climate-weather.md
    ├── 📄 hazards-emergency.md
    ├── 📄 environmental-dashboards.md
    └── 📄 health-risk-communication.md (future)
~~~

---

## 🧩 3. Air Quality Accessibility Principles

| Principle               | Description                                                                 | WCAG / FAIR+CARE Reference |
|-------------------------|-----------------------------------------------------------------------------|----------------------------|
| **Contrast Clarity**    | AQI colors maintain ≥ 4.5:1 contrast; legends use high-contrast text.       | WCAG 1.4.3                 |
| **Semantic Indicators** | Numeric AQI paired with plain-language categories (“Good”, “Moderate”, etc.). | WCAG 1.1.1              |
| **Live Updates**        | Dynamic AQI changes announced via `aria-live="polite"` with rate limiting. | WCAG 4.1.3                 |
| **Ethical Messaging**   | Risk language is factual, non-alarmist, and culturally respectful.         | CARE E-1                   |
| **Temporal Context**    | Charts show clearly labeled timestamps and averaging intervals.            | FAIR F-2                   |
| **Assistive Navigation**| AQI widgets and filters fully operable via keyboard and screen readers.    | WCAG 2.1.1 / 2.4.3         |

---

## 🧭 4. Example Implementation (Air Quality Dashboard)

~~~html
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
      aria-label="Line chart of PM2.5 concentration by day with a 7-day average of 52 micrograms per cubic meter."
    ></canvas>
  </figure>

  <p role="note">
    Data sourced from EPA AirNow and Kansas Department of Health and Environment (KDHE).  
    Uncertainty: ±3 µg/m³. Health framework: US EPA AQI categories.
  </p>
</section>
~~~

### Accessibility & Content Features

- AQI values **combine numeric index, category label, and primary pollutant**.  
- Canvas-based charts use `role="img"` plus descriptive `aria-label` and `<figcaption>`.  
- Live updates use `aria-live="polite"` and are **debounced** to avoid overwhelming assistive tech.  
- Risk descriptions focus on recommended actions (“limit outdoor activity”) rather than blame or speculation.  

---

## 🎨 5. Design Tokens for Air Quality UIs

| Token              | Description                        | Example Value |
|--------------------|------------------------------------|---------------|
| `aqi.good`         | Good air quality color             | `#43A047`     |
| `aqi.moderate`     | Moderate condition color           | `#FFEB3B`     |
| `aqi.unhealthy`    | Unhealthy state color              | `#F57C00`     |
| `aqi.hazardous`    | Hazardous condition color          | `#B71C1C`     |
| `aqi.text.color`   | AQI numeric/label text color       | `#212121`     |
| `aqi.focus.color`  | Focus outline for AQI widgets      | `#FFD54F`     |

Design tokens MUST:

- Comply with **WCAG contrast** rules in light and dark themes.  
- Be defined in `web/src/theme/tokens.json`.  
- Be validated by the `color-contrast.yml` workflow.

---

## 🧾 6. FAIR+CARE Air Quality Metadata Schema (Example)

~~~json
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
~~~

Required:

- Origin, license, sensitivity, consent  
- Pollutants measured, collection interval, and uncertainty  
- Named health framework (e.g., “US EPA AQI”)  

Optional EJ/sovereignty extensions:

- `environmental-justice-zone`: `"Yes"` / `"No"`  
- `tribal-land-mask-applied`: `true`  

---

## ⚙️ 7. ARIA & Keyboard Interaction Matrix

| Key / Attribute      | Behavior                                           | Feedback Example                                   |
|----------------------|----------------------------------------------------|----------------------------------------------------|
| `Tab`                | Move between AQI summary, filters, chart, and map | “Filter: PM2.5 and O3 selected.”                  |
| Arrow keys           | Navigate points on accessible charts/maps         | “Nov 2: AQI 68 — Moderate, PM2.5 primary pollutant.” |
| `Enter` / `Space`    | Toggle pollutant filters or open AQI details      | “County-level AQI details expanded.”              |
| `Esc`                | Close dialogs/overlays                            | “Detail view closed. Returning to AQI summary.”   |
| `aria-live="polite"` | Announce AQI updates                              | “AQI updated: 58 — Moderate, PM2.5.”              |

ARIA patterns MUST be validated with NVDA, VoiceOver, and TalkBack.

---

## 🧪 8. Validation Workflows

| Tool / Workflow       | Scope                                         | Output                                 |
|-----------------------|-----------------------------------------------|----------------------------------------|
| **axe-core**          | Landmark, ARIA, and contrast validation       | `a11y_air_quality.json`                |
| **Lighthouse CI**     | Keyboard flows, performance, visual contrast  | `lighthouse_air_quality.json`          |
| **jest-axe**          | Component-level AQI widget a11y               | `a11y_air_quality_components.json`     |
| **faircare-air-audit**| Tone, EJ framing, consent & sensitivity checks| `air_quality_audit.json`               |

Validation MUST confirm:

- No **color-only** signaling of risk categories  
- Risk descriptions are evidence-based and non-stigmatizing  
- Uncertainty, intervals, and provenance are visible and accessible  

---

## ⚖️ 9. FAIR+CARE Integration

| Principle             | Implementation                                                                      |
|-----------------------|--------------------------------------------------------------------------------------|
| **Collective Benefit**| AQI data is used for public-good decisions (health advisories, EJ monitoring).      |
| **Authority to Control** | Agencies & communities can govern how local AQI data is aggregated or shared.  |
| **Responsibility**    | Visualizations clearly describe methodology, time windows, and uncertainty.         |
| **Ethics**            | Messaging avoids blaming communities and clearly distinguishes modeled vs observed. |

---

## 🕰️ 10. Version History

| Version | Date       | Author                | Summary                                                                                           |
|--------:|------------|-----------------------|---------------------------------------------------------------------------------------------------|
| v11.2.3 | 2025-11-29 | Accessibility Council | Upgraded to v11.2.3; telemetry v2; emoji directory layout; clarified uncertainty & EJ/sensitivity handling. |
| v10.4.1 | 2025-11-16 | Accessibility Council | Updated to KFM-MDP v10.4.3; extended metadata schema; added ethics rules and interaction matrix. |
| v10.0.0 | 2025-11-11 | FAIR+CARE Council     | Initial air quality accessibility pattern for KFM dashboards with AQI semantics.                  |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Maintained under **Master Coder Protocol v6.3** · Verified by **FAIR+CARE Council**  

[⬅ Back to Accessibility Patterns Index](../README.md) · [🌡 Climate & Weather](climate-weather.md) · [🚨 Hazards & Emergency](hazards-emergency.md)

</div>