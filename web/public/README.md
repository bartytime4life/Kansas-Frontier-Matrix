---
title: "🌐 Kansas Frontier Matrix — Web Public Assets (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/README.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/web-public-v2.json"
governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT / CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🌐 **Kansas Frontier Matrix — Web Public Assets**  
`web/public/README.md`

**Purpose:**  
Document the **public-facing static assets** for the KFM web application — icons, images, fonts, and PWA metadata — and define FAIR+CARE governance, accessibility, sustainability, and telemetry requirements for open publication under **Master Coder Protocol v6.3**.

<img alt="Docs · MCP" src="https://img.shields.io/badge/Docs-MCP_v6.3-blue" />
<img alt="License: MIT / CC-BY 4.0" src="https://img.shields.io/badge/License-MIT%20%2F%20CC--BY%204.0-green" />
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Certified-orange" />
<img alt="Status: Stable" src="https://img.shields.io/badge/Status-Stable-success" />

</div>


---

## 📘 Overview

This directory contains **immutable, cacheable** assets supporting the KFM UI, governance dashboards, and dataset visualizations.

All assets must be:

- **Licensed** (MIT/CC-BY or compatible)  
- **Checksum-verified** (SHA-256 recorded)  
- **Accessibility-audited** (alt text, ARIA roles, contrast)  
- **FAIR+CARE-governed** (no unreviewed culturally sensitive imagery)  

Metadata is linked to provenance ledgers and release telemetry to ensure **traceability, sustainability, and ethical reuse**.

---

## 🗂️ Directory Layout

    web/public/
    ├── README.md
    │
    ├── icons/                  # System, data, and app iconography (SVG/PNG)
    │   └── metadata.json       # Icon registry (license, checksum, a11y tags)
    │
    ├── images/                 # UI, maps, governance, and data visuals
    │   ├── ui/
    │   ├── maps/
    │   ├── data/
    │   ├── governance/
    │   ├── archive/
    │   └── metadata.json       # Image registry with FAIR+CARE annotations
    │
    ├── fonts/                  # Open-source fonts (WOFF2) + typography tokens
    ├── manifest.json           # PWA manifest (name, theme, icons, scope)
    └── metadata.json           # Root FAIR+CARE + provenance registry for assets

---

## 🧩 Governance & Publication Workflow

    flowchart TD
      A["Design / Data Viz Production"] --> B["Accessibility & FAIR+CARE Audit"]
      B --> C["Checksum + License + Metadata Registration"]
      C --> D["Provenance Ledger Sync (ISO 19115 / DCAT)"]
      D --> E["CI/CD Publish (Immutable, Cache-Control)"]

Workflow:

1. **Audit**  
   - Lighthouse + axe accessibility scans  
   - FAIR+CARE review (cultural sensitivity, representation, consent where required)

2. **Register**  
   - Compute SHA-256 checksum  
   - Assign SPDX-compatible license  
   - Add alt text and FAIR+CARE fields to `metadata.json`

3. **Ledger Sync**  
   - Append metadata summary to governance ledger:  
     `../../docs/reports/audit/web_public_assets.json`  
   - Optionally cross-link to DCAT metadata

4. **Publish**  
   - Deploy via CI/CD  
   - Set `Cache-Control: public, max-age=31536000, immutable`  
   - Reference assets in SBOM and release manifest

> 💡 **Tip:** Prefer SVG for vector assets, WebP/AVIF for photographs, and keep image weights low without sacrificing legibility.

---

## 🧾 Example Asset Metadata

    {
      "id": "web_public_assets_v10.3.1_map_kansas_1890",
      "category": "images/maps",
      "filename": "ks_topography_1890.png",
      "checksum_sha256": "ed92a2a3c4c6b1e0a71d57bfb78dfcbbd7",
      "license": "CC-BY-4.0",
      "alt_text": "Topographic map of Kansas circa 1890.",
      "fair_status": "certified",
      "a11y_reviewed": true,
      "sustainability_score": 98,
      "timestamp": "2025-11-13T18:55:00Z"
    }

**Required fields:**  

- `id`  
- `filename`  
- `checksum_sha256`  
- `license`  
- `alt_text`  

Optional fields include `languages`, `sensitive`, `source_uri`, `creator`, `care_notes`, `sustainability_score`.

---

## ⚙️ FAIR+CARE Governance Matrix

| Principle              | Implementation                                                                     | Steward              |
|------------------------|-------------------------------------------------------------------------------------|----------------------|
| **Findable**           | Asset registries searchable by ID, checksum, and category; JSON-LD export capable. | @kfm-data            |
| **Accessible**         | Alt text, ARIA roles, keyboard-visible focus for icon links.                       | @kfm-accessibility   |
| **Interoperable**      | Metadata uses ISO 19115 + DCAT patterns; JSON-LD contexts supported.               | @kfm-architecture    |
| **Reusable**           | MIT/CC-BY licensing; provenance and license stored in registries.                  | @kfm-design          |
| **Collective Benefit** | Assets curated for public education and open research, not extractive use.         | @faircare-council    |
| **Authority to Control** | Council review for culturally sensitive or heritage-related imagery.             | @kfm-governance      |
| **Responsibility**     | Contributors ensure inclusive, non-stereotyped, non-harmful representations.       | @kfm-ethics          |

---

## 🔁 Compliance & CI/CD Integration

| Workflow                 | Function                                        | Artifact                                                            |
|--------------------------|-------------------------------------------------|---------------------------------------------------------------------|
| `docs-lint.yml`          | Validate Markdown/front-matter consistency      | `docs/reports/self-validation/docs/lint_summary.json`              |
| `build-and-deploy.yml`   | Bundle + publish web assets                     | `../../releases/v10.3.0/manifest.zip`                              |
| `telemetry-export.yml`   | Aggregate sustainability & asset metrics        | `../../releases/v10.3.0/focus-telemetry.json`                      |
| `accessibility_scan.yml` | Lighthouse/axe A11y scan per release            | `docs/reports/self-validation/web/a11y_summary.json`               |

Rules:

- CI/CD **rejects** any asset missing **checksum**, **license**, or **alt text**.  
- A11y thresholds are enforced; failing runs block release.  
- Asset metadata is merged into release-level telemetry and governance reports.

---

## 🌱 Sustainability & Performance Targets

| Metric              | Target               | Verified By             |
|---------------------|----------------------|-------------------------|
| Avg. Image Weight   | ≤ 400 KB             | Build metrics           |
| Render Energy       | ≤ 0.04 Wh per view   | Telemetry estimates     |
| Carbon Output       | ≤ 0.05 gCO₂e per view| Telemetry / infra data  |
| Renewable Hosting   | ≥ 100% RE-backed     | Infra audit             |
| Lighthouse Perf     | ≥ 95                 | `accessibility_scan.yml`|

Assets are optimized for:

- Efficient network transfer  
- Minimal CPU/GPU overhead  
- High visual clarity at common resolutions  

---

## 🧮 Telemetry & Provenance

Asset usage and quality are reflected in telemetry:

- **Usage counts** (by route/context)  
- **Bytes served** and estimated energy/carbon  
- **A11y scores** for image/icon usage  
- **Governance flags** (e.g., use of restricted imagery is prohibited)

Telemetry sinks:

- `../../docs/reports/telemetry/build_metrics.json`  
- `../../docs/reports/audit/web_public_assets.json`  
- `../../releases/v10.3.0/focus-telemetry.json` (aggregated)

Example telemetry snippet:

    {
      "asset_id": "map_kansas_1930",
      "bytes": 355432,
      "energy_wh": 0.031,
      "co2_g": 0.047,
      "a11y_score": 98,
      "timestamp": "2025-11-13T18:00:00Z"
    }

---

## 🕰️ Version History

| Version  | Date       | Author            | Summary                                                                 |
|----------|------------|-------------------|-------------------------------------------------------------------------|
| v10.3.1  | 2025-11-13 | Web Assets Team   | Upgraded to v10.3 telemetry, tightened FAIR+CARE + sustainability rules, aligned paths. |
| v10.2.2  | 2025-11-12 | Web Assets Team   | JSON-LD export, performance/energy targets, immutable cache policy, CI gates for alt/lic/checksum. |
| v10.0.0  | 2025-11-09 | Web Assets Team   | Sustainability telemetry, ISO/DCAT support, Lighthouse A11y integration. |
| v9.7.0   | 2025-11-05 | KFM Core Team     | Metadata registries, telemetry schema v1, a11y requirements.            |
| v9.6.0   | 2025-11-04 | KFM Core Team     | Added sustainability metrics & checksum traceability.                   |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT / CC-BY 4.0**  
Maintained under **Master Coder Protocol v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
[Back to Web Overview](../README.md) · [Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>