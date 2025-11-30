---
title: "🧠 Kansas Frontier Matrix — Story Nodes Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/story-nodes/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council & Focus Mode Board"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../releases/v11.2.2/github-infra-telemetry.json"
telemetry_schema: "../../schemas/telemetry/storynodes-v3.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Index"
intent: "story-nodes-overview"
role: "story-nodes-index"
category: "Story Nodes · Focus Mode · Semantic Narrative System"

classification: "Public Document"
sensitivity: "General (non-sensitive)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:Feature"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/story-nodes/README.md@v11.2.1"
  - "docs/story-nodes/README.md@v11.0.0"
  - "docs/story-nodes/README.md@v10.4.0"
provenance_requirements:
  versions_required: true
  newest_first: true

json_schema_ref: "../../schemas/json/storynodes-readme-v11.schema.json"
shape_schema_ref: "../../schemas/shacl/storynodes-readme-v11-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "diagram-extraction"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "governance-override"
  - "content-alteration"
  - "speculative-additions"

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

# 🧠 **Kansas Frontier Matrix — Story Nodes Overview**  
`docs/story-nodes/README.md`

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue "Master Coder Protocol v6.3")]() ·
[![Story Nodes v3](https://img.shields.io/badge/Story%20Nodes-v3-informational "Story Node Schema v3")]() ·
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold "FAIR+CARE Compliant")]() ·
[![WCAG AA+](https://img.shields.io/badge/Accessibility-WCAG_2.1_AA%2B-blueviolet "WCAG 2.1 AA+")]() ·
[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen "Status: Active & Enforced")]()

**Purpose**  
Provide the **top-level index and architectural guide** for all **Story Nodes** in the Kansas Frontier Matrix (KFM) v11.2.2.  
Story Nodes form the **semantic narrative layer** used by **Focus Mode v3** to connect text, space, time, data, and governance.

</div>

---

## 🗂️ Directory Layout

~~~text
docs/
└── 📂 story-nodes/
    ├── 📄 README.md                       # Global Story Nodes overview (this file)
    ├── 📂 system/                         # System-level Story Nodes (CI/CD, infra, governance)
    │   ├── 📄 README.md                   # System Story Nodes index
    │   ├── 📄 kfm-auto-update.json        # Daily stage→prod auto-update narrative
    │   ├── 📄 ci-health.json              # (planned) CI stability and SLO/SLA narrative
    │   ├── 📄 releases-timeline.json      # (planned) Release cadence & quality history
    │   └── 📂 templates/                  # Templates for new system Story Nodes
    │       ├── 📄 system-node-template.json
    │       └── 📄 README.md
    └── 📂 domains/                        # Domain-specific storytelling (data & history)
        ├── 📂 history/                    # Historical/cultural narratives (governed)
        │   └── 📄 README.md
        ├── 📂 hydrology/                  # Hydrology & water resources narratives
        │   └── 📄 README.md
        ├── 📂 climate/                    # Climate & atmospheric narratives
        │   └── 📄 README.md
        └── 📂 archaeology/                # Archaeology & heritage narratives (highly governed)
            └── 📄 README.md
~~~

**Layout rules**

- 📂 is used **only** for directories; 📄 is used **only** for files.  
- No emojis appear inside the ASCII connectors themselves.  
- Every directory above MUST maintain a `README.md` that documents its local Story Node collections.

---

## 📘 Overview

Story Nodes are **structured narrative objects** that describe:

- **What**: a phenomenon, process, event, dataset family, or system behavior.  
- **Where**: a place or region (geometry or generalized H3 index).  
- **When**: an instant or interval in time (OWL-Time compatible).  
- **Who/Which**: entities involved (places, agents, datasets, workflows).  
- **How/Why**: explanatory narrative grounded in data, provenance, and governance.

They are used by Focus Mode to generate contextual, data-backed narratives and system explainers across KFM.

Typical Story Node fields (JSON):

- `id`, `version`, `label`  
- `spacetime.geometry`, `spacetime.when`  
- `narrative.summary`, `narrative.details`, `narrative.risk_summary`  
- `links.targets`, `links.datasets`, `links.environments`  
- `governance` (CARE, sovereignty, masking rules)  
- `telemetry_refs` (for system nodes)

---

## 🧭 Context

Story Nodes sit at the intersection of:

- **Ontology** (KFM-OP v11): CIDOC-CRM, GeoSPARQL, OWL-Time, PROV-O mappings.  
- **Catalogs**: STAC for assets, DCAT for datasets, JSON-LD contexts.  
- **CI/CD & Telemetry**: OpenLineage + OpenTelemetry outputs.  
- **Focus Mode v3**: UI layer that consumes Story Nodes to build narrative experiences.

This README anchors Story Nodes as a **first-class, governed artifact** of the monorepo, equal in importance to datasets and pipelines.

---

## 🧠 Story Node & Focus Mode Integration

Focus Mode v3 treats Story Nodes as:

- **Narrative primitives** (small, linkable units of explanation).  
- **Semantic waypoints** tying together:
  - map views  
  - timelines  
  - dataset detail panels  
  - CI/CD and system health views.

### Story Node Consumption

When a user focuses on:

- a place (county, river, watershed, trail)  
- a dataset (STAC collection or DCAT dataset)  
- a system object (workflow, release, telemetry bundle)

Focus Mode:

1. Finds Story Nodes whose `links` or `targets` include that entity.  
2. Renders summaries and details in a Focus panel.  
3. Optionally builds multi-node timelines and comparisons.

### System vs Domain Story Nodes

- **System Story Nodes (system/)**  
  - Explain CI/CD runs, auto-updates, release practices, telemetry evolution, governance events.  
  - Example: `kfm-auto-update.json` describes the daily auto-update orchestrator.

- **Domain Story Nodes (domains/)**  
  - Explain real-world phenomena (floods, droughts, climate episodes, archaeological landscapes).  
  - Highly governed, particularly in archaeology and history folders.

---

## 📦 Data & Metadata

Story Nodes are:

- **JSON documents** that validate against a **Story Node v3 JSON Schema** (`schemas/json/story-node-v3.schema.json` in the monorepo).  
- **PROV-O aware**, referencing workflows, datasets, and releases as `prov:Entity`/`prov:Activity`.  
- **STAC/DCAT-aware**, referencing catalog entries instead of hard-coded URLs.

For each Story Node, authors should:

1. Ensure all referenced datasets exist in STAC/DCAT catalogs.  
2. Link to workflows via their `.github/workflows/*.yml` identifiers.  
3. Include any relevant telemetry references (e.g., CI/CD or auto-update metrics).  
4. Provide stable, versioned URNs (`urn:kfm:story-node:...`) for `id`.

---

## ⚖ FAIR+CARE & Governance

All Story Nodes—especially domain and historical/cultural nodes—are subject to:

- **FAIR**:
  - Machine-readable JSON.  
  - Stable identifiers.  
  - Clear licensing & provenance.

- **CARE**:
  - Protection of Indigenous and community knowledge.  
  - Use of **H3 generalization** for sensitive sites.  
  - Compliance with `INDIGENOUS-DATA-PROTECTION.md`.  
  - Avoidance of speculative or sensationalized narratives.

System nodes (in `system/`) avoid human subjects and cultural interpretation but still carry FAIR+CARE metadata for consistency.

Sensitive nodes may require:

- Additional review by FAIR+CARE Council and relevant community partners.  
- Restricted publication or partial redaction in public builds.

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                          |
|--------:|------------|--------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Rebuilt to mirror KFM-MDP v11.2.2 formatting; added badge row; moved directory layout near top; fixed emoji discipline. |
| v11.2.1 | 2025-11-27 | Interim reorganization of system vs domain Story Node directories.                               |
| v11.0.0 | 2025-11-20 | Initial Story Nodes README defining roles and basic directory structure.                         |

---

<div align="center">

🧠 **Kansas Frontier Matrix — Story Nodes Overview (v11.2.2)**  
Semantic Narratives · Temporal Intelligence · FAIR+CARE-Governed  

[📘 Docs Root](../README.md) · [🧠 System Story Nodes](system/README.md) · [⚖ Governance](../standards/governance/ROOT-GOVERNANCE.md)

</div>
