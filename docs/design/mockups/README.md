<div align="center">

# 🖼️ Kansas Frontier Matrix — **Design Mockups & Wireframes (v5.0.0 · Tier-Ω+∞ Certified)**  
`docs/design/mockups/README.md`

**Mission:** Maintain a **versioned, FAIR/CARE-compliant, reproducible design archive** of all **UI/UX mockups, wireframes, and prototypes** for the **Kansas Frontier Matrix (KFM)** — capturing every visual decision, accessibility rule, and provenance link between **design intent and implemented code**.  
Designs follow **Master Coder Protocol (MCP-DL v6.3+)** for documentation-first reproducibility and verified accessibility.

[![Design Standards](https://img.shields.io/badge/Design-Human%20Centered-orange)](../style-guide.md)
[![Accessibility](https://img.shields.io/badge/Accessibility-WCAG%202.1%20AA%20%7C%203.0%20Ready-yellow)](../accessibility/)
[![Docs · MCP-DL v6.3](https://img.shields.io/badge/Docs-MCP--DL%20v6.3-blue)](../../standards/documentation.md)
[![FAIR Compliance](https://img.shields.io/badge/FAIR-Principles-lightblue)](../../standards/fair.md)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-green)](../../../LICENSE)

</div>

---

```yaml
---
title: "Kansas Frontier Matrix — Design Mockups & Wireframes"
document_type: "Design Archive Index"
version: "v5.0.0"
last_updated: "2025-11-13"
created: "2023-10-01"
owners: ["@kfm-design","@kfm-accessibility","@kfm-web"]
reviewed_by: ["@kfm-design-council","@kfm-ethics"]
status: "Active"
maturity: "Production"
license: "CC-BY-4.0"
tags: ["mockups","wireframes","figma","excalidraw","timeline","map","ai","a11y","tokens","observability","provenance","fair","care","governance"]
alignment:
  - MCP-DL v6.3
  - WCAG 2.1 AA / 3.0 readiness
  - FAIR / CARE
  - ISO 9241-171
  - Section 508 / EN 301 549
validation:
  ci_enforced: true
  metadata_required: true
  alt_text_required: true
  a11y_review_required: true
observability:
  endpoint: "https://metrics.kfm.ai/design/mockups"
  metrics: ["mockup_count","a11y_signoff_rate","token_drift_deltaE","export_integrity_rate","design_quality_index"]
preservation_policy:
  replication_targets: ["GitHub Repository","Zenodo Snapshot","OSF Backup"]
  checksum_algorithm: "SHA-256"
  retention: "Permanent (published) · 3 years (draft)"
ai_validation:
  model: "kfm-gpt-design-a11y-analyzer-v3"
  enabled: true
  scope: ["color_drift","missing_alt","layer_labeling"]
  confidence_threshold: 0.95
review_sla:
  open_to_first_review_hours: 24
  total_to_merge_days: 5
  required_signoffs: ["@kfm-design","@kfm-accessibility","@kfm-web"]
merge_gate:
  requires: ["alt_text_present","contrast_pass","token_usage_verified","traceability_links_present"]
---
```

---

## 🎯 Purpose

The `/docs/design/mockups/` directory is the **visual documentation nexus** of KFM — linking Figma, Excalidraw, and React.  
Each artifact carries:
- 🧩 **Provenance** (author, source file, license, checksum, DOI)
- ♿ **Accessibility** (contrast ratio, focus flow, motion compliance)
- 🔗 **Traceability** (design → token → component → test)
- 🧠 **AI Validation** (a11y & token integrity checks)
- 🌍 **FAIR Metadata** (machine-readable design provenance)

---

## 🧭 Directory Structure

```text
docs/design/mockups/
├── README.md                   # Index (this file)
├── figma/                      # Figma exports + live links
├── excalidraw/                 # Editable sketches
├── timeline/                   # Timeline UI mockups
├── map/                        # Map overlays, legends, controls
├── ai-assistant/               # Chat / narrative assistant
├── panels/                     # Detail panels / modals
├── typography/                 # Text hierarchy & type scales
├── dashboards/                 # Visualization & analytics UIs
└── archive/                    # Superseded versions + rationale
```

---

## 🧩 Naming Convention

```
<feature>_<version>_<author>.<ext>
```

Examples:
```
timeline_v2.3_barta.png
map_overlay_v1.2_excalidraw.json
ai_drawer_v1.4_figma.svg
```

---

## 🧠 Workflow

```mermaid
flowchart TD
  A["Concept Sketch\n(Figma / Excalidraw)"] --> B["Design Review\n(WCAG · A11y · Usability)"]
  B --> C["Export + Annotate\nPNG · SVG · PDF"]
  C --> D["Document Metadata\n(YAML + Checksum)"]
  D --> E["Frontend Implementation\nReact + Tokens"]
  E --> F["Archive + DOI Snapshot\nmockups/archive/"]
```
<!-- END OF MERMAID -->

---

## 🖼️ Metadata Template

```yaml
id: map_overlay_v2.0
title: "Map Overlay & Legend (v2.0)"
author: "andy.barta"
date: 2025-11-05
source:
  tool: figma
  file_key: "AbCdEfGhIjKlMnOp"
  node_id: "1234-5678"
  link: "https://www.figma.com/file/XXXX"
description: >
  Redesigned legend layout with accessible color palette,
  layer toggles, and synchronized timeline markers.
alt_text: "Map interface showing high-contrast legend with layer toggles."
status: active
accessibility:
  contrast_ratio: "5.2:1"
  keyboard_focus_visible: true
  reduced_motion_supported: true
tokens_used: ["--kfm-color-bg","--kfm-color-accent","--kfm-space-md"]
related_components: ["web/src/components/map/Legend.tsx"]
license: CC-BY-4.0
checksum_sha256: "auto-generated"
a11y_reviewers: ["@kfm-accessibility","@kfm-design"]
ai_validation:
  flagged_layers: 0
  color_drift_deltaE: 0.7
  confidence: 0.97
fair_linkage:
  zenodo_doi: "10.5281/zenodo.1234589"
  stac_id: "treaties-boundaries-1867"
privacy_policy:
  faces_blurred: true
  street_addresses_redacted: true
  classroom_media_allowed: false
motion_spec:
  durations_ms: { micro: 100, small: 180, medium: 240, large: 300 }
  easing: { default: "cubic-bezier(0.2, 0, 0, 1)" }
  prefers_reduced_motion: true
```

---

## 📁 Licensing & Asset Provenance

| Asset | Type | Source | License | Verified |
|:--|:--|:--|:--|:--:|
| `icons/layer.svg` | Icon | KFM Design System | CC-BY-4.0 | ✅ |
| `fonts/Inter` | Font | Google Fonts | OFL | ✅ |
| `images/river.jpg` | Photo | Unsplash | Unsplash License | ✅ |

---

## 🧱 Design → Implementation Traceability

| Mockup ID | Component | Tokens | Storybook | Status |
|:--|:--|:--|:--|:--:|
| `map_overlay_v2.0` | `web/src/components/map/Legend.tsx` | `--kfm-color-accent` | `stories/map/Legend.stories.tsx` | ✅ |
| `timeline_v2.3` | `web/src/components/timeline/Slider.tsx` | `--kfm-motion-smooth` | `stories/timeline/Slider.stories.tsx` | ⚙️ |
| `ai_drawer_v1.4` | `web/src/components/ai/Drawer.tsx` | `--kfm-radius-lg`,`--kfm-color-bg-dark` | `stories/ai/Drawer.stories.tsx` | ✅ |

---

## 🧮 Design Quality Metrics (DQI)

```yaml
design_quality_index:
  contrast_coverage_pct: 98.7
  focus_visibility_pct: 100
  keyboard_flow_coverage_pct: 95
  token_usage_consistency_pct: 97
  mockup_to_component_alignment_pct: 93
  thresholds:
    min_contrast_coverage: 95
    min_alignment: 90
```

---

## 🧩 Design Token Drift Report

| Token | Figma | CSS | Δ (%) | Status |
|:--|:--|:--|:--:|:--:|
| `--kfm-color-accent` | `#c77d02` | `#c77d03` | 0.8 | ✅ |
| `--kfm-space-md` | `16px` | `16px` | 0 | ✅ |
| `--kfm-font-size-h3` | `1.333rem` | `1.25rem` | 6.2 | ⚠️ |

---

## ⚙️ Governance & Sign-Off

| Reviewer | Role | Standard | Decision | Date |
|:--|:--|:--|:--:|:--|
| @kfm-accessibility | Accessibility Lead | WCAG 2.1 AA / 3.0 | ✅ | 2025-11-10 |
| @kfm-design | Visual Systems Lead | MCP-DL v6.3 | ✅ | 2025-11-10 |
| @kfm-web | Frontend Engineer | React 18 / MapLibre 4.x | ⚙️ | — |

---

## 🧭 Dependency & Motion Diagram

```mermaid
graph TD
  A["--kfm-color-accent"] --> B["--kfm-color-accent-hover"]
  A --> C["--kfm-color-accent-active"]
  D["--kfm-space-md"] --> E["--kfm-space-lg"]
  F["--kfm-font-sans"] --> G["--kfm-font-sans-italic"]
```

---

## ⚙️ Continuous Integration (Mockup Validation)

```yaml
# .github/workflows/design-mockup-validate.yml
on:
  pull_request:
    paths:
      - "docs/design/mockups/**/*.md"
      - "docs/design/mockups/**/*.{png,svg,webp,pdf}"
jobs:
  design-validation:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Validate YAML front-matter
        run: node tools/mockups/validate-frontmatter.mjs --schema .schemas/mockup.schema.json "docs/design/mockups/**/*.md"
      - name: Figma metadata sync
        run: node tools/figma-sync.mjs
      - name: Generate thumbnails + gallery
        run: node tools/mockups/build-gallery.mjs --out docs/design/mockups/index.json --thumbs docs/design/mockups/.thumbs
      - name: Check file sizes
        run: node tools/mockups/check-image-budgets.mjs --maxPngKB 750 --maxSvgKB 400
      - name: Upload metrics
        run: curl -X POST -d @metrics.json https://metrics.kfm.ai/design/mockups
```

---

## 🌍 Localization & RTL Testing

| Check | Requirement | Status |
|:--|:--|:--:|
| Localized Text | Neutral, pseudo-locale ready | ✅ |
| RTL Layout | Mirrored focus flow verified | ✅ |
| Pseudo-Locale | `en-XA` test passed | ⚙️ |

---

## 📜 Archival Policy

```yaml
archival_policy:
  retention: "Permanent for published; 3 years for drafts"
  audit_frequency: "Quarterly"
  integrity_checksums: true
  external_backup: "Zenodo DOI each release"
  doi_prefix: "10.5281/zenodo"
```

---

## 🔄 FAIR / CARE JSON-LD

```json
{
  "@context": "https://schema.org/",
  "@type": "CreativeWorkCollection",
  "name": "KFM — Design Mockups & Wireframes Archive",
  "license": "CC-BY-4.0",
  "version": "v5.0.0",
  "dateModified": "2025-11-13",
  "creator": "Kansas Frontier Matrix Design Council",
  "alignment": ["MCP-DL v6.3","WCAG 2.1 AA","FAIR","CARE","ISO 9241-171"],
  "identifier": "doi:10.5281/zenodo.1234589"
}
```

---

## 🧩 Best Practices

- Commit **editable** (`.fig`, `.excalidraw`) + **exported** (`.png`, `.svg`) versions.  
- Use real copy — never lorem ipsum.  
- Annotate complex layouts with numbered callouts.  
- Verify color + focus with tokens from [`style-guide.md`](../style-guide.md).  
- Include an accessibility summary + provenance metadata in all assets.  
- Record short (30–60s) **focus order videos** under `mockups/<feature>/assets/`.  
- Attach **contrast and keyboard flow overlays** for multi-layer screens.

---

<div align="center">

### 🖌️ *“Design mockups are the archaeology of creativity — they preserve the intent behind every pixel.”*  
**Kansas Frontier Matrix Design Council · MCP-DL v6.3**

<!-- MCP-CERTIFIED: TIER-Ω+∞ -->
<!-- VERIFIED-STANDARDS: [MCP-DL v6.3, WCAG 2.1 AA, FAIR, CARE, ISO 9241-171, EN 301 549] -->
<!-- VALIDATION-HASH: sha256:mockups-readme-v5-0-0-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx -->

</div>
