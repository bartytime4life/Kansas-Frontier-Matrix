---
title: "🧩 KFM v11 — Accessible UI Patterns and Components Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"
backward_compatibility: "Aligned with v10.x → v11.x accessibility pattern contract"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../releases/v11.2.3/a11y-patterns-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-patterns-v3.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

doc_kind: "Index"
intent: "a11y-patterns-index"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"

sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM Accessibility Council"
risk_category: "Low"
redaction_required: false

provenance_chain:
  - "docs/accessibility/patterns/README.md@v10.2.3"

ontology_alignment:
  schema_org: "CreativeWork"
  cidoc: "E29 Design or Procedure"
  prov_o: "prov:Plan"

json_schema_ref: "../../../schemas/json/a11y-patterns-index.schema.json"
shape_schema_ref: "../../../schemas/shacl/a11y-patterns-index-shape.ttl"

doc_uuid: "urn:kfm:doc:a11y-patterns-index-v11.2.3"
semantic_document_id: "kfm-doc-a11y-patterns-index"
event_source_id: "ledger:docs/accessibility/patterns/README.md"
immutability_status: "version-pinned"

ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "removing FAIR+CARE requirements"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
classification: "Accessibility · UI Patterns"
jurisdiction: "United States · Kansas"
role: "a11y-patterns-root-index"
lifecycle_stage: "stable"
ttl_policy: "Quarterly review"
sunset_policy: "Superseded upon next a11y-patterns index update"
---

<div align="center">

# 🧩 **KFM v11 — Accessible UI Patterns and Components Index**  
`docs/accessibility/patterns/README.md`

**Purpose**  
Canonical index of **all accessibility patterns** used across the Kansas Frontier Matrix (KFM):  
web UI, geospatial tools, dashboards, archives, science workflows, and governance portals.  

Patterns are **WCAG 2.1 AA** and **FAIR+CARE** aligned, with reproducible validation, telemetry,  
and provenance hooks.

</div>

---

## 📘 Overview

This directory provides **ready-to-use accessibility patterns** for KFM, covering:

- Core web components (buttons, dialogs, forms, tables, media, alerts)  
- Geospatial and temporal interfaces (map controls, wayfinding, telemetry, navigation)  
- Scientific and domain-specific modules (hydrology, hazards, climate, air quality, soil, ecology, space)  
- Governance and archival systems (legal records, licensing, documentation, preservation)  
- Communication & educational layers (exhibits, narratives, Focus Mode, dashboards)

Each pattern specifies:

- **ARIA semantics** and landmark regions  
- **Keyboard interactions** and focus behavior  
- **Contrast and motion rules**  
- **Consent, ethics, and provenance cues**  
- **FAIR+CARE metadata expectations**

---

## 🗂️ Directory Layout (Emoji-Prefix Standard)

~~~text
docs/accessibility/patterns/
├── 📄 README.md
├── 📄 alerts.md
├── 📄 buttons.md
├── 📄 charts.md
├── 📄 dialogs.md
├── 📄 forms.md
├── 📄 tooltips.md
├── 📄 map-controls.md
├── 📄 media.md
├── 📄 navigation.md
├── 📄 tables.md
├── 📄 color-contrast.md
├── 📄 navigation-waypoints.md
├── 📄 historical-trails.md
├── 📄 parks-conservation.md
├── 📄 forestry-landcover.md
├── 📄 agroforestry-biomass.md
├── 📄 soil-health.md
├── 📄 prairie-restoration.md
├── 📄 biodiversity-habitats.md
├── 📄 wildlife-tracking.md
├── 📄 avian-ornithology.md
├── 📄 pollinators-ecosystem-services.md
├── 📄 microbiology-ecosystem-health.md
├── 📄 genetics-bioinformatics.md
├── 📄 biochemistry-environmental-chemistry.md
├── 📄 laboratory-methods.md
├── 📄 instrumentation-sensors.md
├── 📄 field-sensors-drone.md
├── 📄 telemetry-streams.md
├── 📄 network-infrastructure.md
├── 📄 api-exchange.md
├── 📄 computing-interface.md
├── 📄 data-infrastructure.md
├── 📄 archival-records.md
├── 📄 data-processing-automation.md
├── 📄 data-integration-validation.md
├── 📄 data-synchronization-versioning.md
├── 📄 branding-communication.md
├── 📄 focus-mode.md
├── 📄 cultural-ethics.md
├── 📄 localization.md
├── 📄 chat-interaction.md
├── 📄 narratives.md
├── 📄 legal-archives.md
├── 📄 exhibits.md
├── 📄 education.md
├── 📄 wayfinding.md
├── 📄 testing-validation.md
├── 📄 design-tokens.md
├── 📄 data-visualization-controls.md
├── 📄 system-controls.md
├── 📄 automation-telemetry.md
├── 📄 ai-explainability.md
├── 📄 environmental-dashboards.md
├── 📄 agriculture-resources.md
├── 📄 hydrology-water.md
├── 📄 hazards-emergency.md
├── 📄 climate-weather.md
├── 📄 air-quality.md
├── 📄 earth-systems.md
├── 📄 minerals-energy.md
├── 📄 infrastructure-utilities.md
├── 📄 urban-planning.md
├── 📄 transportation-mobility.md
├── 📄 vehicle-logistics.md
├── 📄 freight-corridors.md
├── 📄 rail-transit.md
├── 📄 aviation-airspace.md
├── 📄 space-remote-sensing.md
├── 📄 astronomy-spaceweather.md
├── 📄 cosmology-deepspace.md
└── 📄 planetarium-3d.md
~~~

> Related: see `docs/accessibility/checklists/README.md` for implementer checklists  
> and `docs/accessibility/README.md` for the global accessibility index.

---

## 🧩 Pattern Foundations

| Category                 | Principle                      | Description                                                                  |
|--------------------------|--------------------------------|------------------------------------------------------------------------------|
| **Keyboard Operability** | Navigable without a mouse      | Tab, Shift+Tab, Enter, Space, Arrow keys, Esc                               |
| **Screen Reader Semantics** | Clear roles & labels       | WAI-ARIA 1.2 landmarks, roles, states, names & descriptions                 |
| **Focus Visibility**     | Persistent, high-contrast outline | ≥ 3:1 focus indicator, no outline suppression                            |
| **Motion Sensitivity**   | Respect user motion prefs      | Honors `prefers-reduced-motion`; no flashing > 3 Hz                         |
| **Color Independence**   | Redundant cues                 | Never color-only signals; use text, icons, shape, pattern                   |
| **Consent & Ethics**     | FAIR+CARE cues                 | Gated layers, consent indicators, sensitivity flags, heritage protections   |
| **Provenance**           | Traceable lineage              | STAC/DCAT references, model cards, telemetry, governance ledger entries     |

---

## 🧾 Required Metadata (All Patterns)

Every pattern’s example MUST support **governance-aware metadata**:

| Field                 | Purpose                 | Example                                             |
|-----------------------|-------------------------|-----------------------------------------------------|
| `data-origin`         | Source or custodian     | `"USGS / KFM SensorNet"`                           |
| `data-license`        | Reuse license           | `"CC-BY 4.0"`                                      |
| `data-consent`        | Consent status          | `true`                                             |
| `data-ethics-reviewed`| FAIR+CARE audit flag    | `true`                                             |
| `data-provenance`     | Lineage summary         | `"Derived 2025-11-11 from NOAA feed"`              |
| `data-sensitivity`    | Access class            | `"Public"`, `"Restricted"`, `"Heritage"`           |

Domain-specific patterns MAY extend with:

- `data-units`  
- `data-uncertainty`  
- `location-generalization`  
- `indigenous-consent-reference`  

---

## 🧾 Validation & Automation

| Workflow                      | Scope                                      | Output                                              |
|-------------------------------|--------------------------------------------|-----------------------------------------------------|
| `accessibility_scan.yml`      | axe-core + Lighthouse over web UIs         | `reports/self-validation/web/a11y_summary.json`     |
| `storybook-a11y.yml`          | Component-level patterns via jest-axe      | `reports/ui/a11y_component_audits.json`             |
| `color-contrast.yml`          | Palette & token contrast validation        | `reports/ui/color-contrast.json`                    |
| `faircare-visual-audit.yml`   | Imagery, tone, consent & ethics metadata   | `reports/faircare/visual-validation.json`           |

All pattern changes MUST pass these workflows before merging.

---

## 🧩 Pattern Integration Map

~~~mermaid
flowchart LR
  A["Patterns (this directory)"]
  B["Components (web/src/components)"]
  C["Pages & Views"]
  D["Workflows & Dashboards"]
  E["Reports, Story Nodes & Focus Mode"]

  A --> B
  B --> C
  C --> D
  D --> E
~~~

Patterns → Components → Pages → Workflows → Narrative layers must preserve:

- Keyboard operability  
- ARIA semantics  
- FAIR+CARE metadata  
- Telemetry hooks  

---

## 🧠 References

- WAI-ARIA Authoring Practices 1.2  
- WCAG 2.1 Quick Reference  
- Deque axe-core & jest-axe integration guides  
- FAIR+CARE Governance Charter (`../../standards/governance/ROOT-GOVERNANCE.md`)  
- KFM Markdown Structural & Formatting Rules (`../../standards/markdown_rules.md`)  

---

## 🕰️ Version History

| Version | Date       | Author                     | Summary                                                                                  |
|--------:|------------|---------------------------|------------------------------------------------------------------------------------------|
| v11.2.3 | 2025-11-29 | KFM Accessibility Council | Upgraded to v11.2.3; emoji-prefix directory layout; telemetry v2; integrated with updated governance artifacts. |
| v10.4.1 | 2025-11-16 | KFM Accessibility Council | Upgraded to KFM-MDP v10.4.3; extended YAML metadata; clarified validation workflows.    |
| v10.2.3 | 2025-11-11 | KFM A11y Guild            | Rebuild: expanded directory layout; alignment with MCP-DL v6.3 and Platinum v7.1.       |
| v10.0.0 | 2025-11-10 | A11y & FAIR+CARE Council  | Initial consolidated index; core UI patterns and validation pipelines.                  |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
**FAIR+CARE Certified · MCP-DL v6.3 · Diamond⁹ Ω / Crown∞Ω**

[⬅ Back to Accessibility Index](../README.md) · [🎨 Tokens](../tokens.md) · [🛡 Governance](../../standards/governance/ROOT-GOVERNANCE.md)

</div>