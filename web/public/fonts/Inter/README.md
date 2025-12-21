---
title: "🔤 Kansas Frontier Matrix — Inter Typeface Family (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "web/public/fonts/Inter/README.md"
version: "v9.7.0"
last_updated: "2025-11-05"
status: "stable"
doc_kind: "Guide"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/governance/ETHICS.md"
sovereignty_policy: "../../../../docs/standards/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:web-public-fonts:inter:v9.7.0"
semantic_document_id: "kfm-web-public-fonts-inter-v9.7.0"
event_source_id: "ledger:kfm:doc:web-public-fonts:inter:v9.7.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

<div align="center">

# 🔤 **Kansas Frontier Matrix — Inter Typeface Family — Diamond⁹ Ω / Crown∞Ω Ultimate Certified**
`web/public/fonts/Inter/README.md`

**Purpose:** Provide the official, governed **Inter** typeface used across KFM web UI, documentation, and visualization.  
This registry documents **accessibility (WCAG 2.1 AA)**, **open licensing (SIL OFL 1.1)**, and **provenance/telemetry hooks** under **MCP-DL v6.3**.

[![Docs · MCP](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../../docs/README.md)
[![License: SIL OFL 1.1](https://img.shields.io/badge/License-SIL%20OFL%201.1-green)](https://scripts.sil.org/OFL)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../../../../docs/standards/faircare.md)
![Status: Stable](https://img.shields.io/badge/Status-Stable-success)

</div>

---

## 📘 Overview

### Purpose
- Provide a **self-hosted, reproducible** Inter font bundle (WOFF2) for KFM web interfaces.
- Define the **governance controls** for licensing, integrity (checksums), and accessibility expectations.
- Anchor the font assets to **release artifacts** (manifest/SBOM) and **telemetry schema** references.

### Scope

| In Scope | Out of Scope |
|---|---|
| Inter WOFF2 assets in `web/public/fonts/Inter/` | CDN-hosted font delivery (third-party) |
| `metadata.json` structure expectations (license, checksums, coverage) | Full typography system tokens for the entire UI |
| Linkage to release artifacts (SBOM/manifest/telemetry export) | End-user privacy policy text (belongs in governance/security docs) |
| Usage guidance for UI + docs + visualization | Branding decisions outside this repository |

### Audience
- Primary: Web/UI maintainers, design system maintainers, release engineering.
- Secondary: Accessibility reviewers, governance reviewers, telemetry maintainers.

### Definitions
- Glossary (canonical): `docs/glossary.md`
- Terms used here:
  - **WOFF2**: Compressed web font format used for delivery/caching.
  - **SIL OFL 1.1**: Open Font License governing redistribution/modification of the font assets.
  - **WCAG 2.1 AA**: Accessibility baseline for text legibility and presentation.
  - **SBOM**: Software Bill of Materials (release artifact inventory).
  - **Manifest**: Release build manifest anchoring reproducibility and file identities.
  - **Telemetry schema**: JSON schema validating observability events for font loading/rendering.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Inter font assets | `web/public/fonts/Inter/*.woff2` | @kfm-design | Self-hosted WOFF2 family |
| Font metadata | `web/public/fonts/Inter/metadata.json` | @kfm-design | License + SHA-256 checksums + coverage |
| Fonts index | `web/public/fonts/README.md` | @kfm-web | Directory-level index + conventions |
| Release SBOM | `../../../../releases/v9.7.0/sbom.spdx.json` | @kfm-release | Release-time inventory linkage |
| Release manifest | `../../../../releases/v9.7.0/manifest.zip` | @kfm-release | Provenance anchor for this release |
| Telemetry export | `../../../../releases/v9.7.0/focus-telemetry.json` | @kfm-sustainability | Observability snapshot (build/runtime) |
| Telemetry schema | `../../../../schemas/telemetry/web-public-fonts-inter-v1.json` | @kfm-telemetry | Contract for font telemetry events |
| Governance root | `../../../../docs/standards/governance/ROOT-GOVERNANCE.md` | @kfm-governance | Review triggers + policy constraints |

### Review cycle
- Annual / Accessibility & Branding Review

### Definition of done
- [ ] Front-matter complete + valid
- [ ] All internal links resolve (no broken relative references)
- [ ] All font assets listed in **Directory Layout** exist
- [ ] `metadata.json` includes license + SHA-256 checksums for each shipped WOFF2
- [ ] Release manifest + SBOM references are updated for this version (if packaging changed)
- [ ] Telemetry schema reference is current and stable for this version
- [ ] Governance + CARE/sovereignty considerations explicitly stated

---

## 🗂️ Directory Layout

### This document
- `path`: `web/public/fonts/Inter/README.md`

### On-disk layout (expected)

~~~text
📁 web/
└── 📁 public/
    └── 📁 fonts/
        └── 📁 Inter/
            ├── 📄 README.md
            ├── 📄 metadata.json
            ├── 🔤 Inter-Regular.woff2
            ├── 🔤 Inter-Medium.woff2
            ├── 🔤 Inter-SemiBold.woff2
            ├── 🔤 Inter-Bold.woff2
            └── 🔤 Inter-Italic.woff2
~~~

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Web frontend | `web/` | React/Map UI + static public assets |
| Public fonts | `web/public/fonts/` | Self-hosted font assets + family registries |
| Telemetry schemas | `schemas/telemetry/` | JSON Schemas for observability contracts |
| Release artifacts | `releases/` | Manifests, SBOM, telemetry exports (versioned) |
| Governance standards | `docs/standards/governance/` | Root governance + ethics + sovereignty policies |
| Documentation | `docs/` | System guides and standards index |

---

## 🧭 Context

### Why this is governed
Inter is a UI-critical dependency: it impacts readability, layout stability, and accessibility across:
- UI body text and controls
- Narrative/story panels (including Focus Mode presentation)
- Data visualization labels and annotations

### Security + sensitivity
- Font binaries are static and **should not contain PII**.
- Telemetry (if collected) must remain **performance-only** (e.g., load timings, cache status) and must not log user content.
- Any telemetry emitted must validate against the referenced telemetry schema.

### Key invariants
- **Self-hosted + WOFF2**: reduce dependency drift and improve caching.
- **Checksum lineage**: shipped files must match SHA-256 in `metadata.json` and release artifacts.
- **Accessibility-first**: typography must remain legible under zoom, OS scaling, and high-contrast modes.
- **No hidden leakage**: fonts must not introduce external network calls (e.g., remote font CDNs) unless explicitly governed elsewhere.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Source (verified upstream)"] --> B["A11y review (WCAG 2.1 AA expectations)"]
  B --> C["Build/prepare WOFF2 assets (subset if applicable)"]
  C --> D["SHA-256 checksums + metadata.json update"]
  D --> E["Release linkage: manifest + SBOM"]
  E --> F["Deploy as public asset (web/public)"]
  F --> G["Telemetry export (load/render metrics)"]
  G --> H["Schema validation (web-public-fonts-inter-v1)"]
~~~

---

## 🧩 Implementation

### Acquisition & updates (governed workflow)
1. Obtain Inter only from **verified open sources** consistent with **SIL OFL 1.1**.
2. Ensure WOFF2 assets reflect the supported weights:
   - Regular
   - Medium
   - SemiBold
   - Bold
   - Italic
3. Compute SHA-256 for each `.woff2` and record in `metadata.json`.
4. Ensure release packaging includes these files in:
   - `releases/<version>/manifest.zip`
   - `releases/<version>/sbom.spdx.json`
5. Validate telemetry events (if present) against:
   - `schemas/telemetry/web-public-fonts-inter-v1.json`

### CSS integration (reference pattern)
Use self-hosted assets via `/fonts/Inter/...` paths.

~~~css
/* Inter — self-hosted (public assets) */
@font-face {
  font-family: "Inter";
  font-style: normal;
  font-weight: 400;
  src: url("/fonts/Inter/Inter-Regular.woff2") format("woff2");
  font-display: swap;
}

@font-face {
  font-family: "Inter";
  font-style: normal;
  font-weight: 500;
  src: url("/fonts/Inter/Inter-Medium.woff2") format("woff2");
  font-display: swap;
}

@font-face {
  font-family: "Inter";
  font-style: normal;
  font-weight: 600;
  src: url("/fonts/Inter/Inter-SemiBold.woff2") format("woff2");
  font-display: swap;
}

@font-face {
  font-family: "Inter";
  font-style: normal;
  font-weight: 700;
  src: url("/fonts/Inter/Inter-Bold.woff2") format("woff2");
  font-display: swap;
}

@font-face {
  font-family: "Inter";
  font-style: italic;
  font-weight: 400;
  src: url("/fonts/Inter/Inter-Italic.woff2") format("woff2");
  font-display: swap;
}

/* KFM convention: single source of truth token */
:root {
  --kfm-font-sans: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif;
}

body {
  font-family: var(--kfm-font-sans);
}
~~~

---

## 🔌 Contracts & Interfaces

| Contract | Purpose | Artifact / Reference |
|---|---|---|
| Asset integrity | Prevent drift and ensure reproducibility | `metadata.json` SHA-256 + release manifest/SBOM |
| Accessibility | Maintain readable UI across sizes and zoom | WCAG 2.1 AA expectations; a11y review outputs |
| Delivery/performance | Avoid layout shifts and slow text rendering | WOFF2 + `font-display: swap` |
| Telemetry | Observe performance without leaking content | `schemas/telemetry/web-public-fonts-inter-v1.json` |
| Governance | Ensure licensing and ethical constraints are documented | `docs/standards/governance/*` |

---

## 📦 Data & Metadata

### metadata.json expectations
`metadata.json` is the canonical local registry for:
- Family + supported weights
- License identifier
- SHA-256 checksums per file
- Optional fields for telemetry-derived performance metrics (where governed)

### Example metadata structure (illustrative)

~~~json
{
  "id": "inter_v9.7.0",
  "family": "Inter",
  "weights": ["Regular", "Medium", "SemiBold", "Bold", "Italic"],
  "license": "SIL Open Font License 1.1",
  "wcag": "2.1 AA",
  "fairstatus": "certified",
  "checksum_sha256": {
    "Inter-Regular.woff2": "b3c2eaabde42...02e74",
    "Inter-Medium.woff2": "TBD",
    "Inter-SemiBold.woff2": "TBD",
    "Inter-Bold.woff2": "e91d7f0c9a7a...a1f9c",
    "Inter-Italic.woff2": "TBD"
  },
  "energy_score": 99.2,
  "timestamp": "2025-11-05T19:25:00Z"
}
~~~

### Release linkage
For the v9.7.0 release line, this registry references:
- SBOM: `../../../../releases/v9.7.0/sbom.spdx.json`
- Manifest: `../../../../releases/v9.7.0/manifest.zip`
- Telemetry export: `../../../../releases/v9.7.0/focus-telemetry.json`

---

## 🧠 Story Node & Focus Mode Integration

Inter is the primary UI font used when rendering:
- Story Nodes (narrative panels, citations, callouts)
- Focus Mode UI (context bundles + provenance-linked content panels)
- Evidence panels and UI annotations

Typography is part of the UX trust surface:
- Legibility supports careful reading of citations and provenance references.
- Accessibility behavior (zoom/scaling) supports inclusive access to public historical content.

---

## 🧪 Validation & CI/CD

### Minimum gates (v12-ready alignment)
- Markdown protocol validation
- JSON schema validation (telemetry schema, where applicable)
- UI asset integrity checks (file existence + checksum match)
- Accessibility checks (text scaling, contrast policy adherence where applicable)
- Security/sovereignty scanning gates (where applicable)

### Practical validation checklist for this directory
- [ ] All `.woff2` files exist and load from `/fonts/Inter/...`
- [ ] `metadata.json` checksums match actual binaries
- [ ] No external font CDN calls are required to render Inter
- [ ] `font-display: swap` used in font-face declarations
- [ ] Telemetry events (if emitted) validate against `web-public-fonts-inter-v1`

---

## ⚖ FAIR+CARE & Governance

### FAIR+CARE governance matrix (operational interpretation)

| Principle | Implementation | Oversight |
|---|---|---|
| Findable | Indexed by family/weight/checksum in `metadata.json` | @kfm-data |
| Accessible | WOFF2 delivery; swap strategy; zoom compatible | @kfm-accessibility |
| Interoperable | SPDX-friendly license labeling + stable identifiers | @kfm-architecture |
| Reusable | SIL OFL 1.1 permits redistribution & modification | @kfm-design |
| Collective Benefit | Inclusive typography for public science & education | @faircare-council |
| Authority to Control | Annual review of a11y + governance references | @kfm-governance |
| Responsibility | Telemetry + manifest/SBOM track performance + drift | @kfm-sustainability |
| Ethics | Neutral, respectful typographic defaults | @kfm-ethics |

### Sustainability targets (track via telemetry)
| Metric | Target | Source of truth |
|---|---:|---|
| Avg. file size | ≤ 130 KB | Build/release metrics |
| Render energy | ≤ 0.02 Wh | Telemetry export |
| Carbon output | ≤ 0.02 gCO₂e | Telemetry export / CI pipeline |
| Hosting | 100% RE100 | Infrastructure governance |

---

## 🔤 Usage Guidelines

| Weight | Purpose | Example selectors | Notes |
|---|---|---|---|
| Regular | Body text | `p`, `li`, `.body` | Minimum 16px; responsive scaling |
| Medium | UI labels & nav | `label`, `nav a`, `.btn` | Improve contrast at small sizes |
| SemiBold | Subheads | `h4`, `h5` | Use weight for hierarchy, not color alone |
| Bold | Section titles | `h1`, `h2`, `.alert-title` | Reserve for structure, not decoration |
| Italic | Citations/emphasis | `em`, `cite` | Avoid color-only emphasis |

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---|---|---|
| v9.7.0 | 2025-11-05 | KFM Core Team | Aligned telemetry schema v1, governance contracts, WCAG expectations, usage guidance. |
| v9.6.0 | 2025-11-04 | KFM Core Team | Added energy footprint and checksum lineage expectations. |
| v9.5.0 | 2025-11-02 | KFM Core Team | Integrated automatic a11y scoring + FAIR+CARE review hooks. |
| v9.3.2 | 2025-10-28 | KFM Core Team | Established official Inter typeface registry for KFM UI. |

---

## 📎 Appendices

### A. Quick links
- Back to Fonts Index: `../README.md`
- Docs Index: `../../../../docs/README.md`
- Governance root: `../../../../docs/standards/governance/ROOT-GOVERNANCE.md`
- Telemetry schema: `../../../../schemas/telemetry/web-public-fonts-inter-v1.json`

### B. License note
- Font assets: SIL Open Font License 1.1 (see license badge link).
- This document: CC-BY-4.0 (see front-matter).

---

<div align="center">

**© 2025 Kansas Frontier Matrix — SIL OFL 1.1 / CC-BY 4.0**  
Maintained under **MCP-DL v6.3** · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  
`web/public/fonts/Inter/README.md`

</div>