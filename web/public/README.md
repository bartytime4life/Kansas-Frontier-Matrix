---
title: "🌐 Kansas Frontier Matrix — Web Public Assets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/README.md"
version: "v11.0.0"
last_updated: "2025-11-24"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

doc_uuid: "urn:kfm:web-public-readme-v11.0.0"
semantic_document_id: "kfm-doc-web-public"
doc_kind: "Assets"
intent: "web-public-governance"
status: "Active / Enforced"
lifecycle_stage: "stable"

sbom_ref: "../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/web-public-v4.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
faircare_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_ref: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT / CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Mixed-Risk"
sensitivity: "General"
sensitivity_level: "Medium"
indigenous_data_flag: true
public_benefit_level: "High"
risk_category: "Moderate"
redaction_required: true

ontology_alignment:
  schema_org: "MediaObject"
  cidoc: "E73 Information Object"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../schemas/json/web-public-readme-v11.json"
shape_schema_ref: "../../schemas/shacl/web-public-readme-v11.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "12 Months"
sunset_policy: "Replaced upon next Web Public Assets protocol update"
---

<div align="center">

# 🌐 **Kansas Frontier Matrix — Web Public Assets**  
`web/public/README.md`

Governed collection of **immutable public-facing assets** (icons, images, fonts, PWA metadata) used across the KFM Web Application and FAIR+CARE dashboards.

All assets strictly follow:

**FAIR+CARE**,  
**Sovereignty & cultural-sensitivity governance**,  
**WCAG 2.1 AA accessibility**,  
**ISO 19115 lineage**, and  
**KFM-MDP v11 formatting & metadata rules**.

</div>

---

## 📘 Overview

`web/public/` contains **static, cacheable, CDN-friendly assets** that must meet:

- ✔️ **Checksum integrity (SHA-256)**  
- ✔️ **Explicit licensing (MIT / CC-BY / CC0)**  
- ✔️ **Alt text & A11y annotations**  
- ✔️ **FAIR+CARE sensitivity classification**  
- ✔️ **Provenance & ledger linkage**  
- ✔️ **Sovereignty constraints for sensitive imagery**  
- ✔️ **Sustainability telemetry (energy, carbon)**  

Static assets in this directory **enter the KFM public domain surface**, making correctness, ethics, and lineage mandatory.

---

## 1. Directory Layout (v11 · Mixed Mode Safe)

~~~~text
web/public/
├── README.md                    # This document
│
├── icons/                       # SVG/Raster iconography
│   ├── app/                     # App-wide icons (PWA, splash, home-screen)
│   ├── ui/                      # UI icons (buttons, controls)
│   └── metadata.json            # Icon registry: license, checksum, a11y tags
│
├── images/                      # Public imagery (governed by CARE rules)
│   ├── ui/                      # UI-only images (non-sensitive)
│   ├── maps/                    # Base maps, historic layer previews
│   ├── data/                    # Data visual previews (graphs, thumbnails)
│   ├── governance/              # CARE/provenance legend graphics
│   ├── archive/                 # Historical images (requires provenance)
│   ├── sovereignty/             # Cultural/Indigenous/sensitive images (Strict)
│   └── metadata.json            # Central registry for all image assets
│
├── fonts/                       # Open-source fonts (WOFF2)
│   ├── <font-files>             # Inter, Source Serif, Atkinson Hyperlegible
│   └── metadata.json            # Font licensing + checksum registry
│
├── manifest.json                # PWA metadata (name, icons, theme)
└── metadata.json                # Root FAIR+CARE + provenance registry
~~~~

---

### Mixed Mode Rule (v11)

- **images/sovereignty/**  
  - Treated as **SENSITIVE**  
  - Requires **CARE + sovereignty review**, H3-generalization if spatial, and Indigenous-rights safeguards.  

- **All other subdirectories**  
  - Treated as **GENERAL PUBLIC**  
  - Still require FAIR+CARE review, checksum, license, and alt text.

---

## 3. Governance & Publication Workflow (v11)

~~~~mermaid
flowchart TD
    A["Asset Creation<br/>(Design / Archive Import / Data Viz)"]
        --> B["FAIR+CARE + Sovereignty Audit<br/>(Ethics · A11y · Sensitivity)"]

    B --> C["Checksum + License + Metadata Registration<br/>(metadata.json · SPDX · JSON-LD)"]

    C --> D["Governance Ledger Sync<br/>(ISO 19115 · DCAT · PROV-O Ledger Entry)"]

    D --> E["Telemetry Export<br/>(Energy · CO₂e · Access Counts)"]

    E --> F["Publication<br/>Immutable CDN · Cache-Control=31536000,immutable"]
~~~~

**All five stages are mandatory** before an asset becomes publicly accessible.

---

## 4. Example Asset Metadata (v11 Schema)

~~~~json
{
  "id": "kfm_public_img_kansas_topo_1890_v11",
  "path": "images/maps/ks_topography_1890.webp",
  "checksum_sha256": "8dbcd91aef7c0b32298e243c93e07aee9d5e4b3219d2...",
  "license": "CC-BY-4.0",
  "alt_text": "Topographic map of Kansas published circa 1890.",
  "category": "maps",
  "sensitivity": "general",
  "faircare": {
    "fair_status": "certified",
    "care_label": "Public",
    "sovereignty_notes": null
  },
  "provenance": {
    "source_uri": "https://www.loc.gov/...",
    "digitized_by": "KFM Archives",
    "lineage": ["scan", "optimize", "webp-compress"]
  },
  "sustainability": {
    "bytes": 244815,
    "energy_wh": 0.028,
    "co2_g": 0.041
  },
  "timestamp": "2025-11-24T17:21:00Z"
}
~~~~

---

## 5. FAIR+CARE Governance Matrix (v11)

| Principle | Enforcement | Owner |
|----------|-------------|-------|
| **Findable** | IDs, checksums, JSON-LD metadata | @kfm-data |
| **Accessible** | Alt text, semantic labeling, WCAG AA | @kfm-accessibility |
| **Interoperable** | ISO 19115, DCAT 3.0, PROV-O | @kfm-architecture |
| **Reusable** | MIT/CC-BY licenses + provenance | @kfm-design |
| **Collective Benefit** | Non-extractive public imagery | @faircare-council |
| **Authority to Control** | Sovereignty checks for sensitive content | @kfm-governance |
| **Responsibility** | Ethical representation; contextual warnings | @kfm-ethics |

---

## 6. Sustainability Targets (v11)

| Metric | Target | Verified By |
|--------|--------|--------------|
| Max image weight | ≤ 350 KB | Build pipeline |
| Energy/view | ≤ 0.035 Wh | Telemetry |
| CO₂/view | ≤ 0.045 g | Telemetry |
| Renewable hosting | 100% (RE100) | Infra audit |
| A11y score | ≥ 98 | A11y CI |

---

## 7. Telemetry Sink Paths

~~~~text
../../releases/v11.0.0/focus-telemetry.json
../../docs/reports/telemetry/web_public_assets.json
../../docs/reports/audit/web_public_assets_ledger.json
~~~~

---

## 8. Version History

| Version | Date | Summary |
|--------:|-------|---------|
| **v11.0.0** | 2025-11-24 | Full upgrade to KFM-MDP v11; added sovereignty rules, Mixed-Mode classification, energy/carbon v2 fields, new directory tree. |
| v10.3.1 | 2025-11-13 | Previous version aligned with telemetry v2 and FAIR+CARE v10. |
| v10.2.2 | 2025-11-12 | Added JSON-LD and checksum enforcement. |

---

<div align="center">

© 2025 Kansas Frontier Matrix · MIT / CC-BY 4.0  
FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  
Machine-Extractable · Version-Pinned  

[Back to Web Overview](../README.md) · [Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>