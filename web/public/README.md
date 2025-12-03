---
title: "🌐 KFM v11.2.3 — Web Public Assets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed collection of immutable public-facing assets (icons, images, fonts, PWA metadata) used across the KFM Web Application and FAIR+CARE dashboards."
path: "web/public/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Web · FAIR+CARE Council Oversight"
content_stability: "stable"
backward_compatibility: "v11.0.0 → v11.2.3 web-public-assets-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

doc_uuid: "urn:kfm:web-public-readme-v11.2.3"
semantic_document_id: "kfm-doc-web-public-v11.2.3"
event_source_id: "ledger:kfm:web:public:assets:readme:v11.2.3"

sbom_ref: "../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../releases/v11.2.3/manifest.zip"
telemetry_ref: "../releases/v11.2.3/web-public-telemetry.json"
telemetry_schema: "../schemas/telemetry/web-public-v4.json"
energy_schema: "../schemas/telemetry/energy-v2.json"
carbon_schema: "../schemas/telemetry/carbon-v2.json"

governance_ref: "../docs/standards/governance/ROOT-GOVERNANCE.md"
faircare_ref: "../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_ref: "../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT / CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Assets"
intent: "web-public-governance"
status: "Active / Enforced"

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

json_schema_ref: "../schemas/json/web-public-readme-v11.json"
shape_schema_ref: "../schemas/shacl/web-public-readme-v11.shape.ttl"

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
**KFM-MDP v11.2.3 formatting & metadata rules**.

</div>

---

## 📘 Overview

`web/public/` contains **static, cacheable, CDN-friendly assets** that must meet:

- ✔️ **Checksum integrity (SHA-256)**  
- ✔️ **Explicit licensing (MIT / CC-BY / CC0)**  
- ✔️ **Alt text & accessibility annotations**  
- ✔️ **FAIR+CARE sensitivity classification**  
- ✔️ **Provenance & ledger linkage (DCAT + PROV-O)**  
- ✔️ **Sovereignty constraints for sensitive imagery**  
- ✔️ **Sustainability telemetry (energy, carbon)**  

Static assets in this directory **enter the KFM public domain surface**, making correctness, ethics, and lineage mandatory.

---

## 🗂️ Directory Layout (v11.2.3 · Mixed-Mode Safe)

~~~text
web/public/
├── 📄 README.md                    # This document (governance & layout)
│
├── 🎨 icons/                       # SVG/Raster iconography
│   ├── 🧭 app/                     # App-wide icons (PWA, splash, home-screen)
│   ├── 🧱 ui/                      # UI icons (buttons, controls, navigation)
│   └── 🧾 metadata.json            # Icon registry: license, checksum, a11y tags, provenance
│
├── 🖼️ images/                      # Public imagery (governed by CARE rules)
│   ├── 🧩 ui/                      # UI-only images (non-sensitive, decorative + illustrative)
│   ├── 🗺️ maps/                    # Base maps, historic layer previews (generalized)
│   ├── 📊 data/                    # Data visual previews (graphs, thumbnails, diagrams)
│   ├── ⚖️ governance/              # CARE/provenance legend graphics & policy diagrams
│   ├── 📜 archive/                 # Historical images (requires provenance + context)
│   ├── 🪶 sovereignty/             # Cultural/Indigenous/sensitive images (strict governance)
│   └── 🧾 metadata.json            # Central registry for all image assets
│
├── 🔤 fonts/                       # Open-source fonts (WOFF2)
│   ├── <font-files>                # Inter, Source Serif, Atkinson Hyperlegible, etc.
│   └── 🧾 metadata.json            # Font licensing + checksum + usage notes
│
├── 📱 manifest.json                # PWA metadata (name, icons, theme, scope)
└── 🧾 metadata.json                # Root FAIR+CARE + provenance + sustainability registry
~~~

**Directory contract:**

- Every asset **MUST** be represented in the appropriate `metadata.json`.  
- No asset is considered **published** until:
  - It appears in `metadata.json` with checksum, license, FAIR+CARE block, and provenance.  
  - It passes the FAIR+CARE + sovereignty audit pipeline.  

---

## 🔀 Mixed-Mode Rule (v11.2.3)

- **`images/sovereignty/`**  
  - Treated as **SENSITIVE / Mixed-Risk**.  
  - Requires:
    - **CARE + sovereignty review**  
    - H3 generalization if spatial context is implied  
    - Indigenous-rights safeguards and contextual framing  

- **All other subdirectories**  
  - Treated as **GENERAL PUBLIC**, but still require:
    - FAIR+CARE review  
    - Checksum and explicit license  
    - Alt text / accessibility annotations (where applicable)  

No asset under `images/sovereignty/` may be:

- Used without explicit context in UI.  
- Embedded into third-party contexts without governance review.  

---

## 🧭 Governance & Publication Workflow (v11.2.3)

~~~mermaid
flowchart TD
    A["Asset Creation<br/>(Design · Archive Import · Data Viz)"]
        --> B["FAIR+CARE + Sovereignty Audit<br/>(Ethics · A11y · Sensitivity)"]

    B --> C["Checksum + License + Metadata Registration<br/>(metadata.json · SPDX · JSON-LD)"]

    C --> D["Governance Ledger Sync<br/>(ISO 19115 · DCAT · PROV-O Ledger Entry)"]

    D --> E["Telemetry Export<br/>(Energy · CO₂e · Access Counts)"]

    E --> F["Publication<br/>Immutable CDN · Cache-Control=31536000, immutable"]
~~~

**All five stages are mandatory** before an asset becomes publicly accessible.

CI must verify that:

- Every asset in `icons/`, `images/`, `fonts/` appears in **exactly one** `metadata.json`.  
- Every `metadata.json` entry has:
  - Valid checksum  
  - Valid license string  
  - FAIR+CARE block  
  - Provenance + sustainability block  

---

## 🧾 Example Asset Metadata (v11 Schema)

~~~json
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
~~~

**Minimum required fields per asset:**

- Stable `id` + `path`  
- `checksum_sha256`  
- `license` (SPDX-compatible string)  
- `alt_text` (or explicit `"alt_text": null` with justification)  
- `category`  
- `sensitivity`  
- `faircare` block  
- `provenance` block  
- `sustainability` block  

---

## 📊 FAIR+CARE Governance Matrix (v11.2.3)

| Principle                 | Enforcement                                      | Owner                |
|---------------------------|--------------------------------------------------|----------------------|
| **Findable**             | IDs, checksums, JSON-LD metadata                 | @kfm-data            |
| **Accessible**           | Alt text, semantic labeling, WCAG 2.1 AA         | @kfm-accessibility   |
| **Interoperable**        | ISO 19115, DCAT 3.0, PROV-O                      | @kfm-architecture    |
| **Reusable**             | MIT/CC-BY licenses + provenance                  | @kfm-design          |
| **Collective Benefit**   | Non-extractive public imagery                    | @faircare-council    |
| **Authority to Control** | Sovereignty checks for sensitive content         | @kfm-governance      |
| **Responsibility**       | Ethical representation; contextual warnings      | @kfm-ethics          |

Assets under `images/sovereignty/` are subject to **strongest control** across all matrix dimensions.

---

## 🌱 Sustainability Targets (v11.2.3)

| Metric            | Target         | Verified By       |
|-------------------|----------------|-------------------|
| Max image weight  | ≤ 350 KB       | Build pipeline    |
| Energy / view     | ≤ 0.035 Wh     | Telemetry         |
| CO₂ / view        | ≤ 0.045 g      | Telemetry         |
| Renewable hosting | 100% (RE100)   | Infra audit       |
| A11y score        | ≥ 98           | A11y CI           |

Assets exceeding thresholds must:

- Be **recompressed** or redesigned, or  
- Be explicitly whitelisted with justification and governance sign-off.

---

## 📡 Telemetry Sink Paths (v11.2.3)

Public asset telemetry and audit outputs are written to:

~~~text
../releases/v11.2.3/web-public-telemetry.json
../docs/reports/telemetry/web_public_assets.json
../docs/reports/audit/web_public_assets_ledger.json
~~~

These files capture:

- Aggregate access counts (non-identifying)  
- Energy and CO₂ estimates per asset category  
- Governance/audit events (additions, deprecations, redactions)

Telemetry must never include:

- User-level identifiers  
- Raw IPs, user agents, or location hints beyond coarse region (if any)

---

## 🧪 CI & Validation Expectations

CI jobs (indicative):

- `web-public-metadata-validate.yml`  
- `web-public-a11y-check.yml`  
- `web-public-sustainability-check.yml`  

CI MUST:

- Fail if an asset exists without a corresponding `metadata.json` entry.  
- Fail if checksums do not match actual file content.  
- Warn or fail when:
  - Image size budgets are violated.  
  - Alt text is missing or low-quality.  
  - FAIR+CARE or sovereignty flags are inconsistent with placement.

---

## 🕰️ Version History

| Version  | Date       | Summary                                                                                   |
|----------|------------|-------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Aligned with KFM-MDP v11.2.3; updated paths, telemetry references, governance language, and sustainability targets; clarified Mixed-Mode rules. |
| v11.0.0  | 2025-11-24 | Full upgrade to KFM-MDP v11; added sovereignty rules, Mixed-Mode classification, energy/carbon v2 fields, new directory tree. |
| v10.3.1  | 2025-11-13 | Aligned with telemetry v2 and FAIR+CARE v10.                                             |
| v10.2.2  | 2025-11-12 | Added JSON-LD and checksum enforcement.                                                   |

---

<div align="center">

**© 2025 Kansas Frontier Matrix · MIT / CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
Machine-Extractable · Version-Pinned  

[⬅ Back to Web Overview](../README.md) · [⬅ Governance Charter](../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>