---
title: "🦋 Kansas Frontier Matrix — Accessible Biodiversity, Species, and Habitat Monitoring Standards (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/accessibility/patterns/biodiversity-habitats.md"
version: "v10.0.0"
last_updated: "2025-11-11"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/a11y-biodiversity-habitats-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🦋 **Kansas Frontier Matrix — Accessible Biodiversity, Species, and Habitat Monitoring Standards**
`docs/accessibility/patterns/biodiversity-habitats.md`

**Purpose:**  
Define accessibility and FAIR+CARE compliance standards for **biodiversity**, **species distribution**, and **habitat monitoring datasets** in the Kansas Frontier Matrix (KFM).  
Ensure ecological datasets, imagery, and dashboards used for tracking species recovery, migration, and conservation are **perceptible**, **transparent**, and **ethically contextualized** for research and public engagement.

![Badge Docs](https://img.shields.io/badge/Docs-MCP_v6.3-blue)
![Badge FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)
![Badge License](https://img.shields.io/badge/License-CC--BY%204.0-green)
![Badge Status](https://img.shields.io/badge/Status-Active-success)

</div>

---

## 📘 Overview

Biodiversity monitoring within KFM integrates **species occurrence records**, **habitat maps**, and **environmental DNA (eDNA)** data across Kansas ecosystems.  
This standard guarantees that **data visualization**, **map interaction**, and **scientific interpretation** follow **WCAG 2.1 AA**, **GBIF accessibility**, and **FAIR+CARE ethical transparency**.

---

## 🧩 Accessibility & Species Data Principles

| Principle | Description | Standard Reference |
|------------|--------------|--------------------|
| **Semantic Identification** | All species names use accessible taxonomic and vernacular labels. | WCAG 1.3.1 / GBIF |
| **Color & Texture Differentiation** | Habitat polygons color- and pattern-coded for contrast compliance. | WCAG 1.4.1 |
| **Keyboard Operability** | Map filters and species tables accessible via keyboard. | WCAG 2.1.1 |
| **Metadata Provenance** | Observations timestamped, georeferenced, and sourced transparently. | FAIR F-2 |
| **Consent for Sensitive Species** | Threatened or sacred species locations masked until authorized. | CARE A-2 |
| **Plain Language Summaries** | Ecological status described using readable, non-technical language. | WCAG 3.1.5 |

---

## 🧭 Example Implementation (Biodiversity Dashboard)

```html
<section aria-labelledby="biodiversity-dashboard-title" role="region">
  <h2 id="biodiversity-dashboard-title">Kansas Biodiversity & Habitat Monitoring Dashboard</h2>

  <div role="application" aria-roledescription="Biodiversity map viewer">
    <button aria-label="Toggle bird species data">🕊️ Bird Species</button>
    <button aria-label="Toggle pollinator habitats">🐝 Pollinators</button>
    <button aria-label="Toggle threatened species records">⚠️ Threatened Species</button>
  </div>

  <div id="biodiversity-status" role="status" aria-live="polite">
    Displaying: Pollinator habitats (2020–2025) · Species: Monarch Butterfly (Danaus plexippus) — Status: Vulnerable.
  </div>

  <p role="note">
    Data compiled from GBIF, Kansas Biological Survey, USFWS, and FAIR+CARE-certified community science partners.
  </p>
</section>
```

**Implementation Guidance**
- Use `aria-roledescription="Biodiversity map viewer"` for assistive clarity.  
- Announce species common and scientific names in plain text.  
- Live regions broadcast key statistics such as conservation status.  
- Sensitive data automatically masked per FAIR+CARE consent metadata.

---

## 🎨 Design Tokens for Biodiversity Visualization

| Token | Description | Example Value |
|--------|--------------|----------------|
| `biodiversity.bg.color` | Map background | `#E0F7FA` |
| `biodiversity.habitat.color` | Habitat polygon fill | `#4CAF50` |
| `biodiversity.species.color` | Marker color for species | `#FFC107` |
| `biodiversity.alert.color` | Threatened species alert | `#E53935` |
| `biodiversity.focus.color` | Focus outline | `#FFD54F` |
| `biodiversity.text.color` | Label text | `#212121` |

---

## 🧾 FAIR+CARE Biodiversity Metadata Schema

| Field | Description | Example |
|--------|--------------|----------|
| `data-origin` | Custodian or aggregator | “GBIF / KBS / USFWS” |
| `data-license` | License | “CC-BY 4.0” |
| `data-consent` | Consent flag for sensitive data | `true` |
| `data-ethics-reviewed` | FAIR+CARE ethics audit result | `true` |
| `data-provenance` | Data lineage | “GBIF occurrence dataset, verified 2025-08-12” |
| `data-sensitivity` | Access level | “Restricted / Threatened Species” |
| `data-vernacular` | Common name reference | “Monarch Butterfly” |

**Example JSON:**
```json
{
  "data-origin": "GBIF / KBS / USFWS",
  "data-license": "CC-BY 4.0",
  "data-consent": true,
  "data-ethics-reviewed": true,
  "data-provenance": "GBIF occurrence dataset, verified 2025-08-12",
  "data-sensitivity": "Restricted / Threatened Species",
  "data-vernacular": "Monarch Butterfly"
}
```

---

## ⚙️ Keyboard & ARIA Behavior Matrix

| Key | Function | Feedback |
|------|-----------|----------|
| `Tab` | Move between layers and legend filters | Sequential order |
| `Enter` | Activate or deactivate layer | “Threatened species layer enabled.” |
| `Arrow Keys` | Navigate between habitats | Announces habitat name and area |
| `Space` | Pause updates or animations | “Auto-refresh paused.” |
| `aria-live="polite"` | Announces dataset updates | “Bird dataset refreshed, 12 new observations.” |

---

## 🧪 Validation Workflows

| Tool | Scope | Output |
|-------|--------|--------|
| **axe-core** | Accessibility validation for ARIA and focus management | `reports/self-validation/web/a11y_biodiversity.json` |
| **Lighthouse CI** | Contrast and performance | `reports/ui/lighthouse_biodiversity.json` |
| **jest-axe** | Component-level UI compliance | `reports/ui/a11y_biodiversity_components.json` |
| **Faircare Ethics Script** | Checks consent and cultural protection rules | `reports/faircare/biodiversity_ethics.json` |

---

## ⚖️ FAIR+CARE Integration

| Principle | Implementation |
|------------|----------------|
| **Collective Benefit** | Encourages shared ecological stewardship and citizen science. |
| **Authority to Control** | Custodians and communities authorize publication of sensitive data. |
| **Responsibility** | Provenance and consent metadata required for each observation. |
| **Ethics** | Depictions of species avoid anthropocentric or exploitative framing. |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|----------|------|---------|----------|
| v10.0.0 | 2025-11-11 | FAIR+CARE Council | Created accessible biodiversity and habitat monitoring standard including ARIA schema, consent masking, and FAIR+CARE metadata. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — CC-BY 4.0**  
Developed under **Master Coder Protocol v6.3** · Verified by **FAIR+CARE Council**  
[⬅ Back to Accessibility Index](README.md)

</div>
