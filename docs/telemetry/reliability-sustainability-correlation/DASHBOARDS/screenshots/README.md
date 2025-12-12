---
title: "🖼️ Kansas Frontier Matrix — Dashboard Screenshots (Reliability × Sustainability) (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/screenshots/README.md"

version: "v11.2.6"
last_updated: "2025-12-12"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Autonomous"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"

signature_ref: "../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../../../releases/v11.2.6/reliability-sustainability-correlation-dashboards-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/reliability-sustainability-correlation-dashboards-v11.2.6.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Standard Index"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

scope:
  domain: "telemetry-dashboards-screenshots"
  applies_to:
    - "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/screenshots/**"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "Operational screenshots derived from aggregated telemetry (must remain non-sensitive)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by Dashboard Screenshots v12"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/screenshots/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "../../../../../schemas/json/kfm-markdown-protocol-v11.2.6.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/kfm-markdown-protocol-v11.2.6-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:telemetry:reliability-sustainability-correlation:dashboards:screenshots:index:v11.2.6"
semantic_document_id: "kfm-telemetry-rsc-dashboards-screenshots-index-v11.2.6"
event_source_id: "ledger:kfm:doc:telemetry:rsc:dashboards:screenshots:index:v11.2.6"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "a11y-adaptations"
  - "semantic-highlighting"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "narrative-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🗺️ Diagrams"
    - "🧠 Story Node & Focus Mode Integration"
    - "🧪 Validation & CI/CD"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "🧱 Architecture"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

test_profiles:
  - "markdown-lint"
  - "metadata-check"
  - "accessibility-check"
  - "provenance-check"
  - "footer-check"

ci_integration:
  workflow: ".github/workflows/docs-lint.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
  graph: "Semantics × Provenance × Spatial Intelligence"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
---

<div align="center">

# 🖼️ **KFM — Dashboard Screenshots (Reliability × Sustainability)**
`docs/telemetry/reliability-sustainability-correlation/DASHBOARDS/screenshots/README.md`

**Purpose**  
Maintain **reviewable, governance-safe screenshots** of correlation dashboards so PR reviewers can verify:
layout, labeling, units, and narrative safety — without needing live dashboard access.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/Dashboards-Screenshots-informational" />
<img src="https://img.shields.io/badge/Review-PR_First-orange" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 📘 Overview

This directory stores **static dashboard screenshots** used for:

- PR review and change tracking
- release evidence bundles
- governance and audit artifacts

Screenshots are **evidence**, not the source of truth. The source of truth remains:

- dashboard definitions (`../definitions/`)
- queries (`../queries/`)
- panel configs (`../panels/`)
- dashboard catalog (`../dashboards.catalog.json`)

**Non-negotiable rule**

Screenshots MUST remain **non-sensitive** and MUST NOT reveal restricted scopes, secrets, or sensitive coordinates.

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 telemetry/
    └── 📁 reliability-sustainability-correlation/
        └── 📁 DASHBOARDS/
            └── 📁 screenshots/
                ├── 📄 README.md
                ├── 🖼️ reliability_sustainability_overview__desktop.png
                ├── 🖼️ reliability_sustainability_overview__mobile.png
                ├── 🖼️ workflow_cost_hotspots__desktop.png
                ├── 🖼️ incident_waste_tracing__desktop.png
                └── 🖼️ panel_retry_storm_detector__desktop.png
~~~

**Naming convention (recommended)**

Use a stable, grep-friendly convention:

~~~text
<dashboard_or_panel_id>__<viewport>__<yyyy-mm-dd>.png
~~~

Where:

- `dashboard_or_panel_id` matches the ID in `../dashboards.catalog.json` or the panel filename
- `viewport` is one of: `desktop`, `mobile`, `wide`
- date reflects capture day (UTC)

If date is omitted, screenshots MUST be updated whenever the definition changes.

---

## 🧭 Context

Screenshots exist because governance review requires:

- deterministic evidence that can be preserved with the repo history
- visual validation of:
  - axis labels and units
  - legend semantics
  - severity coloring and labeling
  - safe wording (no “secure”, no causal claims unless supported)

Screenshots also reduce review friction:

- reviewers can verify layout changes without running the full dashboard stack
- regressions become obvious in diffs

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A["Dashboard change in PR"] --> B["Render dashboard"]
  B --> C["Capture screenshot"]
  C --> D["Commit screenshot"]
  D --> E["Reviewer checks"]
  E --> F["Merge and publish"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

Screenshots may be referenced as **supporting assets** for Story Nodes such as:

- `urn:kfm:story-node:telemetry:dashboard:rsc:<release_id>`
- `urn:kfm:story-node:telemetry:incident:waste:<incident_id>`

Focus Mode MAY:

- link to the screenshot as “visual evidence”
- summarize what the dashboard is intended to show (based on the dashboard spec)

Focus Mode MUST NOT:

- treat screenshots as authoritative data
- infer causality or policy from a chart image alone

---

## 🧪 Validation & CI/CD

### 1. Required checks

- `docs-lint.yml` MUST validate this README (structure, links, footer rules).
- If screenshot validation is implemented, it SHOULD check:
  - allowed file extensions: `png`, `webp`
  - max file size (repo policy)
  - naming convention compliance (warn or fail per policy)

### 2. When screenshots are required

A PR SHOULD include updated screenshots when it changes:

- dashboard layout, panels, units, or labels
- correlation thresholds or severity semantics
- any text shown directly on charts (titles, legends, annotations)

---

## 📦 Data & Metadata

Screenshots are treated as **release evidence artifacts**.

Recommended minimal metadata captured per screenshot (in PR description or release notes):

- dashboard ID
- commit SHA
- environment (dev/staging/prod)
- time window (e.g., last 7 days)
- aggregation level (workflow, job, run)

If a manifest is later introduced, it MUST be governance-safe and must not embed sensitive identifiers.

---

## 🌐 STAC, DCAT & PROV Alignment

- **DCAT**
  - Screenshots can be modeled as `dcat:Distribution` assets for the dashboard pack dataset.
  - Media type: `image/png` (or `image/webp`).

- **PROV-O**
  - Each screenshot is a `prov:Entity`.
  - Capture is a `prov:Activity` that:
    - `prov:used` the dashboard definition and query revision
    - `prov:wasAssociatedWith` a CI agent or maintainer

STAC representation is optional; if used, treat screenshots as non-spatial assets with `geometry: null`.

---

## 🧱 Architecture

Screenshots sit in the dashboard layer as **review artifacts**:

- definitions and queries remain primary
- screenshots provide human validation and historical diffing

Screenshots MUST never become a dependency for runtime systems.

---

## ⚖ FAIR+CARE & Governance

### Governance constraints (normative)

Screenshots MUST NOT include:

- secrets, tokens, credentials, or URLs with embedded credentials
- PII or individual-level identifiers
- restricted coordinates or culturally sensitive locations
- internal-only hostnames or infrastructure identifiers (unless policy explicitly allows)

If a screenshot accidentally captures a sensitive element:

- remove it from git history per repo governance procedure
- replace it with a redacted or re-captured image
- record the event in the appropriate governance log, if required by policy

---

## 🕰️ Version History

| Version | Date       | Author           | Summary                                                                 |
|--------:|------------|------------------|-------------------------------------------------------------------------|
| v11.2.6 | 2025-12-12 | `@kfm-telemetry` | Established screenshot directory rules, naming guidance, and governance constraints under KFM-MDP v11.2.6. |
| v11.2.4 | 2025-12-06 | `@kfm-telemetry` | Prior baseline (superseded by v11.2.6).                                 |

---

<div align="center">

🖼️ **KFM — Dashboard Screenshots (Reliability × Sustainability) (v11.2.6)**  
PR Evidence · Governance-Safe Visuals · Deterministic Review

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Aligned-gold" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />

[⬅ Dashboards](../README.md) ·
[⬅ Correlation Module](../../README.md) ·
[⬅ Telemetry Index](../../../README.md) ·
[🧾 Specs](../../specs/README.md) ·
[🧪 Validators](../../validators/README.md) ·
[📦 Reports](../../reports/README.md) ·
[⚙ Workflows Index](../../../../workflows/README.md) ·
[⚙ Telemetry Export Workflow](../../../../workflows/telemetry-export.yml.md) ·
[📘 Docs Root](../../../../README.md) ·
[📘 Markdown Protocol](../../../../standards/kfm_markdown_protocol_v11.2.6.md) ·
[⚖ Governance Charter](../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[⚡ Energy Schema](../../../../../schemas/telemetry/energy-v2.json) ·
[🌿 Carbon Schema](../../../../../schemas/telemetry/carbon-v2.json)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω

</div>

