---
title: "🖼️ KFM v11.2.3 — Public Image Assets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed library of public-facing image assets (UI, maps, data viz, governance imagery) for the Kansas Frontier Matrix web ecosystem."
path: "web/public/images/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Web · FAIR+CARE Council Oversight"
content_stability: "stable"
backward_compatibility: "v9.7.0 → v11.2.3 web-public-images-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

doc_uuid: "urn:kfm:web-public-images-readme-v11.2.3"
semantic_document_id: "kfm-doc-web-public-images-v11.2.3"
event_source_id: "ledger:kfm:web:public:images:readme:v11.2.3"

sbom_ref: "../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../releases/v11.2.3/web-public-telemetry.json"
telemetry_schema: "../../schemas/telemetry/web-public-images-v1.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
faircare_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_ref: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT / CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Assets"
intent: "web-public-images-governance"
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
  schema_org: "ImageObject"
  cidoc: "E38 Image"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../schemas/json/web-public-images-readme-v11.json"
shape_schema_ref: "../../schemas/shacl/web-public-images-readme-v11.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "12 Months"
sunset_policy: "Replaced upon next Web Public Images protocol update"
---

<div align="center">

# 🖼️ **Kansas Frontier Matrix — Public Image Assets**  
`web/public/images/README.md`

**Purpose:**  
Define and govern **public-facing image assets** used throughout the KFM web ecosystem — including UI, data visualization, and governance communication imagery.  
All images are **FAIR+CARE-certified**, **ISO 19115-aligned**, and **WCAG 2.1 AA accessibility-validated**, and must conform to **KFM-MDP v11.2.3**.

</div>

---

## 📘 Overview

The **Public Image Assets Library** under `web/public/images/` contains all **open-licensed, traceable, and accessible images** powering KFM’s web presentation layer.

Each image:

- Has a **SHA-256 checksum** and SPDX-compatible license.  
- Is described by **JSON metadata** (ISO 19115 + FAIR+CARE blocks).  
- Includes **alt text** or documented justification if omitted.  
- Is subject to **sensitivity classification**, including Indigenous data & sovereignty safeguards.  
- Contributes to **sustainability telemetry** (bytes, energy, CO₂ estimates).

This README is the **image-specific supplement** to the root web public asset governance in:

- `web/public/README.md`

---

## 🗂️ Directory Layout (v11.2.3)

~~~text
web/public/images/
├── 📄 README.md                    # This document (image governance & layout)
│
├── 🧩 ui/                          # Interface elements and widget imagery
│   ├── …                           # Buttons, headers, hero images, decorative vectors
│   └── 🧾 metadata.json            # UI image registry (license, checksum, alt text, FAIR+CARE)
│
├── 📊 data/                        # Dataset visualization and preview imagery
│   ├── …                           # Thumbnails, charts, diagrams, Story Node previews
│   └── 🧾 metadata.json            # Data visualization image registry
│
├── 🗺️ maps/                        # Cartographic and topographic imagery
│   ├── …                           # Generalized rasters, hillshades, historic previews
│   └── 🧾 metadata.json            # Map image registry (provenance-heavy)
│
├── ⚖️ governance/                  # FAIR+CARE, governance, audit visuals
│   ├── …                           # Legend graphics, governance diagrams, badges
│   └── 🧾 metadata.json            # Governance imagery registry
│
├── 📜 archive/                     # Legacy / retired imagery kept for provenance
│   ├── …                           # Decommissioned assets (never used in new UI)
│   └── 🧾 metadata.json            # Archive registry (immutability + lineage only)
│
└── 🧾 metadata.json                # Root roll-up index for all image assets (optional)
~~~

**Directory contract:**

- Each **subdirectory** (`ui/`, `data/`, `maps/`, `governance/`, `archive/`) must maintain its **own `metadata.json`**.  
- An optional top-level `metadata.json` may roll up all entries, but **MUST NOT** contradict subdirectory metadata.  
- No image file may be present without a corresponding, validated **metadata entry**.

---

## 🔀 Image Lifecycle Workflow (v11.2.3)

~~~mermaid
flowchart TD
    A["Image Created or Imported"] --> B["FAIR+CARE + Accessibility Review<br/>(A11y · Ethics · Sensitivity)"]
    B --> C["Checksum + SPDX + Metadata Generation<br/>(metadata.json · JSON-LD)"]
    C --> D["Governance Ledger Registration<br/>(ISO 19115 · DCAT · PROV-O)"]
    D --> E["Sustainability Estimation<br/>(Bytes · Energy · CO₂e)"]
    E --> F["Publication<br/>web/public/images/ + Immutable CDN"]
~~~

**Stages (all required):**

1. **Creation / Import**  
   - Images originate from verified, open datasets or KFM design workflows.  

2. **FAIR+CARE + A11y Audit**  
   - Check for **WCAG 2.1 AA** color contrast and textual equivalents.  
   - Review for **cultural sensitivity**, Indigenous data concerns, and potential harm.  

3. **Checksum + Metadata**  
   - Compute **SHA-256**; register SPDX license and attribution.  
   - Capture provenance (source URI, digitizer, processing steps).  

4. **Ledger Registration**  
   - Register in the governance ledger (DCAT + PROV-O + FAIR+CARE status).  

5. **Sustainability Estimation & Publication**  
   - Estimate per-asset bytes → energy/CO₂; log to telemetry.  
   - Publish to `web/public/images/` with long-lived immutable caching.

---

## 🧾 Example Image Metadata Record (v11 Schema)

~~~json
{
  "id": "kfm_public_img_kansas_topo_1890_v11",
  "path": "maps/ks_topography_1890.webp",
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
    "lineage": ["scan", "color-correct", "optimize", "webp-compress"]
  },
  "sustainability": {
    "bytes": 244815,
    "energy_wh": 0.028,
    "co2_g": 0.041
  },
  "wcag": {
    "compliant": true,
    "standard": "2.1 AA",
    "notes": "Alt text present; no text embedded in image."
  },
  "timestamp": "2025-11-24T17:21:00Z"
}
~~~

**Minimum required fields per image:**

- `id`, `path`, `checksum_sha256`, `license`, `category`, `sensitivity`  
- `alt_text` (or explicit justification for omission)  
- `faircare` block  
- `provenance` block  
- `sustainability` block  
- `timestamp`

---

## 🧠 FAIR+CARE Governance Matrix (Image-Specific)

| Principle               | Implementation                                             | Oversight              |
|-------------------------|-----------------------------------------------------------|------------------------|
| **Findable**           | IDs, checksums, JSON-LD metadata in `metadata.json`       | @kfm-data              |
| **Accessible**         | Alt text, WCAG 2.1 AA, semantic roles                     | @kfm-accessibility     |
| **Interoperable**      | ISO 19115, DCAT, PROV-O alignment                         | @kfm-architecture      |
| **Reusable**           | MIT/CC-BY licenses, clear attribution requirements        | @kfm-design            |
| **Collective Benefit** | Non-extractive, non-harmful public imagery                | @faircare-council      |
| **Authority to Control** | Sovereignty, Indigenous data rules for sensitive content | @kfm-governance        |
| **Responsibility**     | Designers and engineers maintain provenance & checksums   | @kfm-sustainability    |
| **Ethics**             | Respectful representation of people, cultures, landscapes | @kfm-ethics            |

Images involving **Indigenous sites or cultural materials** must also:

- Reference `sovereignty_ref`.  
- Be tagged with `indigenous_data_flag: true` in metadata.  
- Undergo enhanced review before publication.

---

## 🖼️ Image Categories & Standards

| Directory       | Description                                 | Typical Format     | FAIR+CARE Status |
|-----------------|---------------------------------------------|--------------------|------------------|
| `ui/`           | Backgrounds, headers, widget visuals        | SVG / PNG / WebP   | Certified        |
| `data/`         | Dataset previews and visualization exports  | PNG / WebP / SVG   | Certified        |
| `maps/`         | Cartographic and topographic imagery        | WebP / PNG / GeoTIFF (derived) | Certified (Generalized) |
| `governance/`   | Audit, certification, FAIR+CARE visuals     | SVG / PNG          | Certified        |
| `archive/`      | Deprecated imagery retained for lineage     | Various            | Archived (Read-only) |

Assets in `archive/`:

- Must **not** be used in new UI work.  
- Remain available solely for provenance and audit.

---

## ⚖️ Retention & Provenance Policy

| Record Type        | Retention        | Policy                                            |
|--------------------|------------------|---------------------------------------------------|
| Active Images      | Continuous       | Versioned and replaceable under FAIR+CARE rules   |
| Image Metadata     | Permanent        | Ledger-backed, PROV-O/JSON-LD preserved          |
| Archived Assets    | Permanent        | Immutable checksum lineage                        |
| Audit Reports      | ≥ 365 Days       | Reviewed annually by FAIR+CARE Council           |

Audit outputs (indicative):

- `../../docs/reports/audit/web_public_images_ledger.json`  
- `../../docs/reports/audit/web_public_assets.json`

---

## 🌱 Sustainability Metrics (Image Layer)

| Metric              | Target       | Verified By          |
|---------------------|-------------|----------------------|
| Average file size   | ≤ 500 KB    | @kfm-design          |
| Render energy/view  | ≤ 0.04 Wh   | @kfm-sustainability  |
| CO₂ / view          | ≤ 0.06 g    | @kfm-sustainability  |
| Renewable hosting   | 100% (RE100) | @kfm-infrastructure |
| FAIR+CARE coverage  | 100%        | @faircare-council    |

Telemetry captured in:

- `../../releases/v11.2.3/web-public-telemetry.json`

Large or high-impact images (e.g., hero backgrounds) must:

- Be explicitly justified in metadata.  
- Be subject to **extra compression** and **progressive loading** strategies.

---

## 🧪 Validation & CI Contracts

CI workflows (names illustrative):

- `web-public-images-metadata-validate.yml`  
- `web-public-images-a11y-check.yml`  
- `web-public-images-sustainability-check.yml`  

CI MUST:

- Fail if any image exists without a matching metadata entry.  
- Fail on checksum mismatch or missing/invalid license.  
- Warn or fail when:
  - Alt text fails quality checks.  
  - Size/energy/carbon budgets are exceeded without justification.  
  - FAIR+CARE or sovereignty flags conflict with directory placement.

---

## 🕰️ Version History

| Version  | Date       | Author        | Summary                                                                 |
|----------|------------|---------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | KFM Core Team | Aligned with KFM-MDP v11.2.3; updated telemetry paths, governance refs, sustainability targets, and Mixed-Mode rules; harmonized with `web/public/README.md`. |
| v9.7.0   | 2025-11-05 | KFM Core Team | Upgraded with telemetry schema and ISO alignment for image metadata.    |
| v9.6.0   | 2025-11-04 | KFM Core Team | Added sustainability registry and checksum governance for images.       |
| v9.5.0   | 2025-11-02 | KFM Core Team | Expanded FAIR+CARE validation and accessibility scoring.                |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT / CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
Machine-Extractable · Version-Pinned  

[⬅ Back to Web Public Assets](../README.md) · [⬅ Back to Web Overview](../../README.md) · [📜 Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>