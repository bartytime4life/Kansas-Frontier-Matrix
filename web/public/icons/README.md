---
title: "🎨 KFM v11.2.3 — Iconography System (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed icon library for the Kansas Frontier Matrix web ecosystem, including UI, data-domain, governance, and social icons."
path: "web/public/icons/README.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Web · FAIR+CARE Council Oversight"
content_stability: "stable"
backward_compatibility: "v9.7.0 → v11.2.3 iconography-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

doc_uuid: "urn:kfm:web-public-icons-readme-v11.2.3"
semantic_document_id: "kfm-doc-web-public-icons-v11.2.3"
event_source_id: "ledger:kfm:web:public:icons:readme:v11.2.3"

sbom_ref: "../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../releases/v11.2.3/web-public-telemetry.json"
telemetry_schema: "../../schemas/telemetry/web-public-icons-v1.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
faircare_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_ref: "../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT / CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Assets"
intent: "web-public-icons-governance"
status: "Active / Enforced"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Mixed-Risk"
sensitivity: "General"
sensitivity_level: "Medium"
indigenous_data_flag: false
public_benefit_level: "High"
risk_category: "Low"
redaction_required: false

ontology_alignment:
  schema_org: "ImageObject"
  cidoc: "E36 Visual Item"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../schemas/json/web-public-icons-readme-v11.json"
shape_schema_ref: "../../schemas/shacl/web-public-icons-readme-v11.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "12 Months"
sunset_policy: "Replaced upon next Iconography System protocol update"
---

<div align="center">

# 🎨 **Kansas Frontier Matrix — Iconography System**  
`web/public/icons/README.md`

**Purpose:**  
Define and govern the full **icon library** supporting the KFM web ecosystem.  
All icons are **FAIR+CARE-certified**, **WCAG 2.1 AA–aligned**, and **metadata-verified** under ISO 19115 and MCP v6.3, ensuring ethical visual communication and sustainability.

</div>

---

## 📘 Overview

The **KFM Iconography System** is the centralized design and governance hub for all icons used across:

- Web applications & dashboards  
- FAIR+CARE governance modules  
- Story Node and Focus Mode interfaces  
- Public-facing documentation and reports  

Each icon:

- Is **version-controlled** in git and registry metadata.  
- Has a **SHA-256 checksum** and SPDX-compatible license.  
- Is covered by **FAIR+CARE** and accessibility audits.  
- Contributes to **sustainability telemetry** (bytes, energy, CO₂).

This README is the icon-specific counterpart to:

- `web/public/README.md` (root public asset governance)  
- `web/public/images/README.md` (image governance)

---

## 🗂️ Directory Layout (v11.2.3)

~~~text
web/public/icons/
├── 📄 README.md                    # This document (icon governance & layout)
│
├── 🧭 app/                         # Application UI icons (alerts, nav, panels, timeline)
│   ├── …                           # Generic UI symbols
│   └── 🧾 metadata.json            # App icon registry (checksum, license, a11y, FAIR+CARE)
│
├── 📊 data/                        # Data-domain icons (climate, hydrology, hazards, land cover)
│   ├── …                           # Domain-specific glyphs
│   └── 🧾 metadata.json            # Data icon registry (domain + sensitivity tags)
│
├── 🎖️ badges/                      # FAIR+CARE, certification, status & governance badges
│   ├── …                           # Diamond⁹ Ω / Crown∞Ω, FAIR+CARE labels, etc.
│   └── 🧾 metadata.json            # Badge registry (usage constraints + licensing)
│
├── 🚩 flags/                       # Cultural / geopolitical flags (governed use)
│   ├── …                           # ISO-country or governance-approved flags
│   └── 🧾 metadata.json            # Flag registry (sovereignty + usage notes)
│
├── 🧱 system/                      # System / governance / OS-like interface icons
│   ├── …                           # Settings, governance, alert/status symbols
│   └── 🧾 metadata.json            # System icon registry
│
├── 🕰️ legacy/                      # Archived or retired icons (read-only)
│   ├── …                           # Deprecated designs kept for provenance
│   └── 🧾 metadata.json            # Legacy registry (immutability + lineage only)
│
└── 🧾 metadata.json                # Optional root roll-up index for all icons
~~~

**Directory contract:**

- Each category directory (`app/`, `data/`, `badges/`, `flags/`, `system/`, `legacy/`) must maintain its **own `metadata.json`**.  
- The optional root `metadata.json` must **not contradict** per-directory metadata.  
- No icon file may exist without a corresponding **metadata entry** in exactly one registry.

---

## 🔀 Icon Governance Workflow (v11.2.3)

~~~mermaid
flowchart TD
    A["Icon Creation / Update (SVG/WebP)"]
        --> B["Accessibility + FAIR+CARE Audit<br/>(WCAG · Ethics · Sensitivity)"]
    B --> C["Checksum + SPDX + Metadata Registration<br/>(metadata.json · JSON-LD)"]
    C --> D["Provenance & Ledger Sync<br/>(ISO 19115 · DCAT · PROV-O)"]
    D --> E["CI/CD Publish + SBOM / Manifest Integration"]
    E --> F["Immutable Delivery<br/>CDN · Cache-Control=31536000, immutable"]
~~~

**All stages are mandatory** before an icon becomes available for production use.

1. **Creation/Update**  
   - Icons are created by KFM-certified designers or imported from open, compliant libraries.  

2. **Accessibility + FAIR+CARE Audit**  
   - WCAG 2.1 contrast checks, color-blind safety, and semantics.  
   - Ethics & inclusivity review (no stereotypes, harmful imagery, or misuse of flags).

3. **Checksum + Metadata Registration**  
   - Compute **SHA-256** and register in `metadata.json`.  
   - Record license, provenance, FAIR+CARE status, and sustainability attributes.

4. **Provenance & Ledger Sync**  
   - Record icon set changes in governance ledgers and audits.  

5. **CI/CD Publish + Immutable Delivery**  
   - Include in SBOM and manifests.  
   - Deployed via immutable, long-lived caching.

---

## 🧾 Example Icon Registry Metadata Record

> Registry-level example (not per-icon, but per-set summary).

~~~json
{
  "id": "icon_registry_v11.2.3",
  "categories": ["app", "data", "system", "social", "badges", "flags"],
  "total_icons": 428,
  "fairstatus": "certified",
  "wcag": "2.1 AA",
  "checksum_sha256": "3fe6a4b2c991df3c46e8a5e1d7a92f8f9e1d3b76c81b70af53b8f2f4e36d4172",
  "sustainability": {
    "avg_bytes": 31240,
    "energy_score": 98.9,
    "carbon_output_gco2e": 0.05
  },
  "timestamp": "2025-12-03T19:45:00Z"
}
~~~

**Per-icon metadata** (in category-level `metadata.json`) must include at least:

- `id`, `path`, `category`, `checksum_sha256`  
- `license` (SPDX string), `aria_label` or descriptive `title` (if applicable)  
- `sensitivity` and `faircare` block  
- `provenance` block (source, designer, lineage)  
- `sustainability` block (bytes, estimated energy/CO₂)  
- `timestamp`

---

## 🧠 FAIR+CARE Governance Matrix (Iconography)

| Principle               | Implementation                                              | Oversight            |
|-------------------------|------------------------------------------------------------|----------------------|
| **Findable**           | Indexed by checksum, ID, and category in `metadata.json`.  | @kfm-data            |
| **Accessible**         | Alt-text/ARIA/`<title>` tags; WCAG 2.1 AA contrast checks. | @kfm-accessibility   |
| **Interoperable**      | ISO 19115, DCAT, PROV-O, FAIR+CARE metadata blocks.        | @kfm-architecture    |
| **Reusable**           | CC-BY / MIT licenses, clear attribution paths.             | @kfm-design          |
| **Collective Benefit** | Culturally sensitive, inclusive iconography.               | @faircare-council    |
| **Authority to Control** | FAIR+CARE Council & governance review for new sets.      | @kfm-governance      |
| **Responsibility**     | Designers & engineers maintain lineage & audit trails.      | @kfm-sustainability  |
| **Ethics**             | Screening for neutrality, avoiding stereotypes/appropriation. | @kfm-ethics       |

Icons involving **flags** or culturally specific symbols require:

- Additional sovereignty review.  
- Explicit usage notes in `flags/metadata.json`.

---

## ♿ Accessibility Standards (Icons)

- Minimum **3:1** contrast for secondary icons; **4.5:1** for primary and status icons.  
- Every interactive icon must have:
  - A **semantic role** (via ARIA or context)  
  - A descriptive **label** (e.g., `aria-label`, `<title>` in SVG).  

- No critical information may be conveyed **solely by color**; icons must:
  - Use shape, outline, or pattern to differentiate states (e.g., error vs warning).  

- Icons should **not embed text** inside the graphic when text can be rendered separately, to ensure screen readers can access it.

---

## 🌱 Sustainability Metrics (Icon Layer)

| Metric             | Target       | Verified By          |
|--------------------|-------------|----------------------|
| Average icon size  | ≤ 60 KB     | CI metrics           |
| Render energy/view | ≤ 0.02 Wh   | Telemetry            |
| CO₂ / view         | ≤ 0.03 g    | Telemetry            |
| Renewable hosting  | 100% RE100  | @kfm-infrastructure  |
| FAIR+CARE coverage | 100%        | @faircare-council    |

Telemetry (icons + other public assets) is aggregated in:

- `../../releases/v11.2.3/web-public-telemetry.json`

Budget exceptions (e.g., complex badges or legacy social icons):

- Must be explicitly documented in metadata (e.g., `"waiver_reason"`).  
- Must be reviewed periodically for redesign or optimization.

---

## ⚙️ Validation Contracts & CI

Typical CI workflows (names illustrative):

- `web-public-icons-metadata-validate.yml`  
- `web-public-icons-a11y-check.yml`  
- `web-public-icons-sustainability-check.yml`  

CI MUST:

- Fail if icon files exist without matching metadata entries.  
- Fail on checksum mismatch or missing/invalid license.  
- Warn or fail when:
  - Accessibility requirements are not met (contrast, labels).  
  - Sustainability thresholds are exceeded without waiver.  
  - FAIR+CARE flags or sovereignty notes conflict with category placement.

Audit artifacts (indicative):

- `../../docs/reports/audit/web_public_icons_ledger.json`  

---

## 🕰️ Version History

| Version  | Date       | Author         | Summary                                                                 |
|----------|------------|----------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | KFM Core Team  | Aligned Iconography System with KFM-MDP v11.2.3; updated telemetry paths, governance refs, accessibility & sustainability targets; harmonized with `web/public/` and `web/public/images/`. |
| v9.7.0   | 2025-11-05 | KFM Core Team  | Upgraded telemetry schema v1, metadata contracts, CI/CD integration.    |
| v9.6.0   | 2025-11-04 | KFM Core Team  | Introduced automated checksum + provenance registration for icons.      |
| v9.5.0   | 2025-11-02 | KFM Core Team  | Added new governance + social icons; expanded FAIR+CARE checks.         |
| v9.3.2   | 2025-10-28 | KFM Core Team  | Established FAIR+CARE iconography registry baseline.                    |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT / CC-BY 4.0**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
Machine-Extractable · Version-Pinned  

[⬅ Back to Web Public Assets](../README.md) · [⬅ Back to Web Overview](../../README.md) · [📜 Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>