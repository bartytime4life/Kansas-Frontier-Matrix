---
title: "🦋 Kansas Frontier Matrix — Accessible Biodiversity, Species, and Habitat Monitoring Standards (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/biodiversity-habitats.md"
version: "v10.4.1"
last_updated: "2025-11-16"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.0/manifest.zip"
telemetry_ref: "../../../releases/v10.4.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-biodiversity-habitats-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.3"
status: "Active / Enforced"
doc_kind: "Pattern"
intent: "biodiversity-habitats-a11y"
fair_category: "F1-A1-I1-R1"
care_label: "Ecological / Cultural-Sensitive"
sensitivity_level: "High"
public_exposure_risk: "Medium"
indigenous_rights_flag: true
data_steward: "KFM Biodiversity Working Group · FAIR+CARE Council"
risk_category: "Medium"
redaction_required: true
provenance_chain:
  - "docs/accessibility/patterns/biodiversity-habitats.md@v10.0.0"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  schema_org: "Dataset"
  cidoc: "E26 Physical Feature"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
json_schema_ref: "../../../schemas/json/a11y-biodiversity-habitats.schema.json"
shape_schema_ref: "../../../schemas/shacl/a11y-biodiversity-habitats-shape.ttl"
doc_uuid: "urn:kfm:doc:a11y-biodiversity-habitats-v10.4.1"
semantic_document_id: "kfm-doc-a11y-biodiversity-habitats"
event_source_id: "ledger:docs/accessibility/patterns/biodiversity-habitats.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative species status changes"
  - "exposing precise locations of sensitive species"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Biodiversity / Habitat Monitoring"
jurisdiction: "Kansas / Tribal Nations / United States"
role: "a11y-pattern-biodiversity-habitats"
lifecycle_stage: "stable"
ttl_policy: "Quarterly review"
sunset_policy: "Superseded upon next biodiversity pattern update"
---

<div align="center">

# 🦋 **Kansas Frontier Matrix — Accessible Biodiversity, Species, and Habitat Monitoring Standards**  
`docs/accessibility/patterns/biodiversity-habitats.md`

**Purpose:**  
Define accessibility and FAIR+CARE compliance standards for **biodiversity**, **species distribution**, and **habitat monitoring datasets** in the Kansas Frontier Matrix (KFM).  
Ensure ecological datasets, imagery, and dashboards used for tracking species recovery, migration, and conservation are **perceptible**, **transparent**, and **ethically contextualized** for research, policy, and public engagement.

![Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![Status](https://img.shields.io/badge/Status-Active-success)

</div>

---

## 📘 Overview

Biodiversity monitoring within KFM integrates:

- Species occurrence records (GBIF, museum records, community science)  
- Habitat suitability and landcover maps  
- Environmental DNA (eDNA) and microbiome indicators  
- Conservation status & IUCN–aligned risk categories  
- Indigenous ecological knowledge, where consented  

This standard ensures that biodiversity content is:

- Accessible for screen readers and keyboard-only users  
- Culturally and ecologically **non-harmful** (no location leakage for sensitive species)  
- Bound to **FAIR+CARE provenance and consent metadata**  

---

## 🗂️ Directory Context

```text
docs/accessibility/
│
└── patterns/
    ├── biodiversity-habitats.md     # This file
    ├── soil-health.md
    ├── wildlife-tracking.md
    ├── pollinators-ecosystem-services.md
    └── ...
```

---

## 🧩 Accessibility & Species Data Principles

| Principle                 | Description                                                                 | Reference              |
|---------------------------|-----------------------------------------------------------------------------|------------------------|
| Semantic Identification   | Species labeled with common + scientific names, readable by AT.            | WCAG 1.3.1 / GBIF      |
| Color & Texture Diff.     | Habitat types distinguished using color + patterns, not color alone.        | WCAG 1.4.1             |
| Keyboard Operability      | Map controls, filters, and tables fully keyboard-accessible.                | WCAG 2.1.1             |
| Metadata Provenance       | Observations timestamped, georeferenced, and sourced with lineage.          | FAIR F-2               |
| Consent for Sensitive Species | Threatened or sacred species masked/generalized by default.            | CARE A-2               |
| Plain-Language Summaries  | Ecological status explained in non-technical, contextual language.          | WCAG 3.1.5             |

---

## 🧭 Example Implementation (Biodiversity Dashboard)

```html
<section aria-labelledby="biodiversity-dashboard-title" role="region">
  <h2 id="biodiversity-dashboard-title">
    Kansas Biodiversity & Habitat Monitoring Dashboard
  </h2>

  <div role="application" aria-roledescription="Biodiversity map viewer">
    <button aria-label="Toggle bird species data">🕊️ Bird Species</button>
    <button aria-label="Toggle pollinator habitats">🐝 Pollinators</button>
    <button aria-label="Toggle threatened species records">⚠️ Threatened Species</button>
  </div>

  <div id="biodiversity-status" role="status" aria-live="polite">
    Displaying: Pollinator habitats (2020–2025) · Species: Monarch Butterfly
    (<i>Danaus plexippus</i>) — Status: Vulnerable.
  </div>

  <p role="note">
    Data compiled from GBIF, Kansas Biological Survey, USFWS, community science projects, and FAIR+CARE-certified partners.
  </p>
</section>
```

### Implementation Guidance

- Use `aria-roledescription="Biodiversity map viewer"` for clear semantics.  
- Announce both **vernacular** and **scientific names**.  
- Show conservation status and whether precise locations are masked.  

---

## 🎨 Design Tokens for Biodiversity Visualizations

| Token                          | Description                     | Example Value |
|--------------------------------|---------------------------------|---------------|
| `biodiversity.bg.color`        | Map background                  | `#E0F7FA`     |
| `biodiversity.habitat.color`   | Habitat polygon fill            | `#4CAF50`     |
| `biodiversity.species.color`   | Species occurrences markers     | `#FFC107`     |
| `biodiversity.alert.color`     | Threatened species alerts       | `#E53935`     |
| `biodiversity.focus.color`     | Focus outline                   | `#FFD54F`     |
| `biodiversity.text.color`      | Labels and legend text          | `#212121`     |

---

## 🧾 FAIR+CARE Biodiversity Metadata Schema

```json
{
  "data-origin": "GBIF / KBS / USFWS",
  "data-license": "CC-BY 4.0",
  "data-consent": true,
  "data-ethics-reviewed": true,
  "data-provenance": "GBIF occurrence dataset, verified 2025-08-12",
  "data-sensitivity": "Restricted / Threatened Species",
  "data-vernacular": "Monarch Butterfly",
  "data-taxonomy": "Danaus plexippus",
  "location-generalization": "H3 r7"
}
```

**Key Requirements**

- Species records must carry **provenance, taxonomic authority, and sensitivity**.  
- `location-generalization` required for threatened or sacred species.  

---

## ⚙️ Keyboard & ARIA Behavior Matrix

| Key / Attribute    | Function                                   | Feedback                                  |
|--------------------|--------------------------------------------|-------------------------------------------|
| `Tab`              | Move between layers, filters, and legend   | Announces control label                   |
| `Enter`            | Toggle habitat/species layer               | “Threatened species layer enabled.”       |
| `Arrow Keys`       | Navigate between habitat polygons/markers  | Announces habitat name + species count    |
| `Space`            | Pause auto-refresh or animation            | “Auto-refresh paused.”                    |
| `aria-live="polite"` | Announce dataset updates                 | “Bird dataset refreshed; 12 new records.” |

---

## 🧪 Validation Workflows

| Tool              | Scope                                       | Output                                  |
|-------------------|----------------------------------------------|-----------------------------------------|
| **axe-core**      | ARIA semantics & focus paths                 | `a11y_biodiversity.json`                |
| **Lighthouse CI** | Contrast, performance, keyboard flows        | `lighthouse_biodiversity.json`          |
| **jest-axe**      | React/map component-level tests              | `a11y_biodiversity_components.json`     |
| **Faircare Script** | Consent masks & sensitive-location checks  | `biodiversity_ethics.json`              |

Validation must confirm:

- No direct coordinates shown for sensitive or sacred species.  
- All interactive habitat layers and filters are keyboard-accessible.  
- Legends and labels use tokenized palettes and accessible contrast.

---

## ⚖️ FAIR+CARE Integration

| Principle           | Implementation                                                                 |
|---------------------|---------------------------------------------------------------------------------|
| Collective Benefit  | Biodiversity data supports shared conservation and learning.                    |
| Authority to Control| Tribes, agencies, and landowners control sensitive species visibility.         |
| Responsibility      | Every species dataset carries lineage, sensitivity, and consent metadata.      |
| Ethics              | Map and narrative avoid sensationalism, exploitation, or blame.                |

---

## 🕰️ Version History

| Version | Date       | Author               | Summary                                                                                       |
|--------:|------------|----------------------|-----------------------------------------------------------------------------------------------|
| v10.4.1 | 2025-11-16 | Accessibility Council| Updated for KFM-MDP v10.4.3; added extended YAML metadata, location generalization semantics, and ethics checks. |
| v10.0.0 | 2025-11-11 | FAIR+CARE Council    | Initial biodiversity & habitat monitoring accessibility pattern with FAIR+CARE metadata mask rules. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
Developed under **Master Coder Protocol v6.3** · Verified by **FAIR+CARE Council**  
[⬅ Back to Accessibility Patterns Index](../README.md)

</div>