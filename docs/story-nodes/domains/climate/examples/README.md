---
title: "🌦️ KFM v11.2.6 — Climate Story Node Examples (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/story-nodes/domains/climate/examples/README.md"
version: "v11.2.6"
last_updated: "2025-12-12"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Climate Systems Board · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Example Collection"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:doc:storynodes:domains:climate:examples:v11.2.6"
semantic_document_id: "kfm-storynodes-climate-examples-v11.2.6"
event_source_id: "ledger:docs/story-nodes/domains/climate/examples/README.md"
immutability_status: "version-pinned"

signature_ref: "../../../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.6/storynode-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/storynodes-v11.json"
schema_ref: "../../../../../schemas/json/story-node.schema.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"

intent: "kfm-climate-storynode-examples"
lifecycle_stage: "stable"

fair_category: "F1-A2-I2-R2"
care_label: "Environmental"
classification: "Public"
sensitivity: "Environmental event narratives (public-safe)"
sensitivity_level: "Low"
public_exposure_risk: "Low"

jurisdiction: "Kansas / United States"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "36 months"
sunset_policy: "Superseded by v12 climate example set"

metadata_profiles:
  - "PROV-O"
  - "FAIR+CARE"
  - "STAC (when assets present)"
  - "DCAT (when datasets referenced)"

provenance_chain:
  - "docs/story-nodes/domains/climate/examples/README.md@v11.2.2"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "timeline-generation"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "narrative-fabrication"
  - "governance-override"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
---

<div align="center">

# 🌦️ **Climate Story Node Examples (KFM v11.2.6)**  
### *Severe Weather · Heatwaves · Drought · Anomalies · Model Insights*  

`docs/story-nodes/domains/climate/examples/README.md`

**Purpose**  
Provide **public-safe**, **scientifically rigorous**, and **schema-valid** examples showing correct:
spacetime modeling, relations, provenance, and (when applicable) STAC/DCAT dataset integration for the climate domain.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Domain-Climate-brightgreen" />
<img src="https://img.shields.io/badge/Examples-Schema_Valid-informational" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 🗂️ Directory Layout

~~~text
📂 docs/
└── 📂 story-nodes/
    └── 📂 domains/
        └── 📂 climate/
            └── 📂 🧪 examples/
                ├── 📄 README.md                           # This file
                ├── 🌪️ hrrr-tornado-outbreak.json          # Severe weather example
                ├── 🌡️ heatwave-2022-kansas.json           # Heatwave / climate anomaly example
                └── 📄 ... (additional examples)           # Add more schema-valid examples
~~~

**Layout rules (normative)**  
- The ASCII connectors remain plain (`├──`, `│`, `└──`) for human scanability.  
- Directories use `📂` plus a semantic emoji (here: `🧪 examples/`).  
- Filenames MUST be kebab-case and descriptive (no internal IDs, no secrets, no personal data).

---

## 📘 Overview

All examples in this directory are:

- **public-safe**  
- **scientifically accurate** (with stated uncertainty)  
- **schema-validated** against `story-node.schema.json`  
- **provenance-complete** (sources and processing described)  
- **Focus Mode v3 compatible**  
- compatible with FAIR+CARE governance posture (environmental, low risk)

These files are intended to be copied as starting points when authoring new climate Story Nodes.

---

## 🧠 What These Examples Demonstrate

Each example Story Node illustrates:

- Correct **spacetime** modeling  
  - valid GeoJSON regions (public-safe scale)  
  - ISO-8601 time intervals with declared precision (`hour`, `day`, `month`, etc.)

- Clear separation of:
  - **observations** (measurements, reanalysis, radar/satellite products)
  - **model outputs** (forecast or derived layers)
  - **interpretation** (carefully scoped and evidence-grounded)
  - **uncertainty** (known limitations, resolution/coverage caveats)

- Proper climate terminology and units  
  - CF-style naming where appropriate  
  - explicit units on key values (and consistent conversions)

- Valid links (when applicable) to:
  - **STAC assets** (rasters, composites, derived layers)
  - **DCAT datasets**
  - **PROV-O lineage** (what was used, what was produced, and by whom)

- Climate-specific relations (when used), such as:
  - `about` (the primary event or phenomenon)
  - `references` (datasets, papers, reports)
  - `derived-from` (a product derived from an upstream dataset/model)
  - `analog-of` (historical analog events, when defensible)

---

## 🎯 Example Categories Included

### 🌪️ Severe Weather
Tornado outbreaks, derechos, high-wind episodes, mesoscale convective systems.

### 🌡️ Temperature Extremes
Heatwaves, cold spells, arctic intrusions, temperature anomalies.

### 💧 Hydroclimate Signals
Drought indicators, precipitation anomalies, flood precursors (public-safe scale).

### ☁️ Satellite & Model Driven
GOES composites, HRRR layers, ERA5 anomaly fields, blended products.

### 📈 Long-Term Trends
Multi-year summaries framed with uncertainty and without sensational attribution claims.

---

## 🚫 What Will Never Appear Here

- Personal data, individual identifiers, or property-targetable information  
- Sensitive infrastructure details (internal hostnames, restricted endpoints)  
- Unlicensed or proprietary datasets  
- Exaggerated or speculative attribution claims presented as certainty  
- Political or normative statements  
- “Hidden” precision (e.g., embedding fine coordinates in IDs, filenames, or relations)

**Scientific neutrality is mandatory.**

---

## 🧠 Story Node & Focus Mode Integration

Examples are authored to be safe for Focus Mode:

- timelines render from the declared temporal interval and precision
- map context uses public-safe geometries suitable for narrative exploration
- neighbor graph expansion relies on governed relation semantics (no free-form surprise edges)

Focus Mode MUST treat example nodes as:

- narrative + metadata objects with provenance,
- not authoritative “truth” beyond what sources and uncertainty support.

---

## 🧪 Validation Requirements

All example Story Nodes MUST:

- validate against `story-node.schema.json`
- use valid GeoJSON (if geometry is embedded)
- include complete provenance and source references
- avoid unsupported causal claims (especially for event attribution)
- use only approved relations for the domain
- keep geometry **public-safe** (appropriate aggregation scale for publication)

Recommended CI checks (if enabled in your pipeline):

- schema validation
- link checks (internal docs + dataset refs)
- unit sanity checks for key fields
- provenance completeness checks (minimum required fields)

---

## 🕰️ Version History

| Version | Date       | Summary                                                                 |
|--------:|------------|-------------------------------------------------------------------------|
| v11.2.6 | 2025-12-12 | Upgraded to KFM-MDP v11.2.6; improved directory layout formatting; tightened validation and safety language. |
| v11.2.2 | 2025-11-30 | Initial governed climate example set; aligned with templates.          |
| v11.2.1 | 2025-11-29 | Added tornado + heatwave draft examples (generalized).                 |

---

<div align="center">

🌦️ **Climate Story Node Examples (v11.2.6)**  
Public-Safe Climate Narratives · Schema-Valid Examples · Provenance-First

[⬅ Climate Domain](../README.md) ·
[📚 Story Nodes Root](../../README.md) ·
[📘 Docs Home](../../../../README.md) ·
[📏 Standards Index](../../../../standards/README.md) ·
[🛡 Governance Charter](../../../../standards/governance/ROOT-GOVERNANCE.md) ·
[🌿 FAIR+CARE Guide](../../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[🧾 Story Node Schema](../../../../../schemas/json/story-node.schema.json)

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
MCP-DL v6.3 · KFM-MDP v11.2.6 · Diamond⁹ Ω / Crown∞Ω

</div>
