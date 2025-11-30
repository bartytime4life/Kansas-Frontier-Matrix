```markdown
---
title: "🧠 Kansas Frontier Matrix — System Story Nodes Overview"
path: "docs/story-nodes/system/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council & Focus Mode Board"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/github-infra-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/storynodes-system-v1.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Index"
intent: "story-nodes-system-overview"
role: "focusmode-system-index"
category: "Story Nodes · Focus Mode · System Architecture"

classification: "Public Document"
sensitivity: "General (non-sensitive)"
sensitivity_level: "None"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false
indigenous_rights_flag: false

fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
data_steward: "KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/story-nodes/system/README.md@v11.2.0"
  - "docs/story-nodes/system/README.md@v11.0.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: false

json_schema_ref: "../../../schemas/json/storynodes-system-readme-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/storynodes-system-readme-v11-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "speculative-additions"
  - "governance-override"
  - "content-alteration"

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

# 🧠 **Kansas Frontier Matrix — System Story Nodes Overview**  
`docs/story-nodes/system/README.md`

**Purpose**  
Act as the **index and architectural guide** for **system-level Story Nodes** used by Focus Mode v3 to explain  
KFM’s **infrastructure, CI/CD behavior, governance, telemetry, and auto-update orchestration** (e.g., `kfm-auto-update.yml`).

System Story Nodes describe **how the system itself behaves over time** — not people or places — and are strictly governed.

</div>

---

## 📘 Overview

System Story Nodes are **machine- and human-readable narrative objects** that represent:

- CI/CD processes and pipeline states (e.g., auto-update, release, telemetry exports)  
- Governance events (e.g., policy changes, FAIR+CARE decisions)  
- Infrastructure health and reliability stories (e.g., error budgets, SLO status)  
- Operational rhythms (e.g., daily auto-refresh, weekly re-indexing, monthly archive loads)  

They are not end-user content; they are **system explainers** that help:

- Focus Mode narrate **what the platform is doing and why**  
- Maintainers see system history as a **timeline of governed events**  
- Governance bodies understand the **impact and reliability** of automation  

All System Story Nodes must:

- Use the **Story Node v3 schema**  
- Be grounded in **OpenLineage + telemetry data**  
- Respect FAIR+CARE & sovereignty constraints (even for system narratives)  

---

## 🗂️ Directory Layout

~~~text
docs/
└── 🧠 story-nodes/
    ├── 📄 README.md                    # Global Story Nodes overview (all domains)
    ├── 📂 system/                      # System-level Story Nodes (this directory)
    │   ├── 📄 README.md                # ← System Story Nodes index & architecture (this file)
    │   ├── 📄 kfm-auto-update.json     # Daily stage → prod auto-update Story Node
    │   ├── 📄 ci-health.json           # (planned) CI health + failure-rate narrative
    │   ├── 📄 releases-timeline.json   # (planned) Release cadence & quality history
    │   └── 📂 templates/               # Templates & patterns for system Story Nodes
    └── 📂 domains/                     # User-facing domain Story Nodes (history, hydro, soil, etc.)
        ├── 📂 history/
        ├── 📂 hydrology/
        ├── 📂 climate/
        └── 📂 archaeology/
~~~

Author rules:

- Every `system/*.json` file MUST validate against the Story Node v3 schema.  
- New system Story Nodes MUST be described in this README and referenced from the global Story Nodes README.  
- Any Story Node that references **sensitive layers** must explicitly describe masking/generalization behavior in its metadata.

---

## 🧱 Architecture

### What is a “System Story Node”?

A **System Story Node** is a Story Node whose primary focus is:

- A **KFM system process** (CI/CD run, auto-update, release, etc.), or  
- An **aggregate of system behavior** over time (e.g., “auto-update success rate over 6 months”).

System Story Nodes typically:

- Have `geometry = null` (no explicit geospatial footprint), or  
- Use a **high-level bounding geometry** (e.g., Kansas-wide or non-sensitive extents), and  
- Use `spacetime.when` to describe the **time interval** of system activity.

They link to:

- Workflows (`.github/workflows/*.yml`)  
- Architecture docs (`docs/architecture/**`)  
- Telemetry files (`releases/**/github-infra-telemetry.json`)  
- Releases (`releases/**`, tags `kfm-<ver>`)

---

## 🧠 Story Node & Focus Mode Integration

System Story Nodes are consumed by Focus Mode to:

- Provide **system timelines** — “When did auto-update first go live?”  
- Explain **governed behavior** — “Why did this promotion fail?”  
- Surface **meta-context** — “Is CI stable? Are FAIR+CARE checks noisy?”  
- Offer **narratives for maintainers and power users** in the UI.

Focus Mode uses system Story Nodes to:

- Generate infoboxes when the user focuses on:
  - `.github/workflows/**`
  - `data/releases/**`
  - `docs/architecture/**`
- Provide **“system health” overlays** alongside map and timeline views.

System narratives must:

- Be **strictly factual** and backed by telemetry/lineage.  
- Avoid speculation about human motives or cultural meaning.  
- Reference governance docs instead of embedding policy changes ad hoc.

---

## 📦 Data & Metadata

All system Story Nodes should:

- Use `@context` entries that align with:
  - Story Node v3  
  - KFM ontology context  
- Include:
  - `id` as a stable URN (`urn:kfm:story-node:system:...`)  
  - `version` for semantic-document tracking  
  - `spacetime.when` with OWL-Time-compatible instant/interval semantics  
  - `links.targets` pointing to:
    - workflows, docs, releases, telemetry artifacts  
  - `governance` block with FAIR+CARE and sovereignty references  

For example, see `docs/story-nodes/system/kfm-auto-update.json`:

- Represents daily auto-update runs as a story node  
- Links to:
  - `kfm-auto-update.yml`  
  - `github-infra-telemetry.json`  
  - Git tags `kfm-<ver>`  
- Summarizes risks, scope, and governance behavior.

---

## 🧱 Example: `kfm-auto-update.json` (System Auto-Update Node)

The `kfm-auto-update.json` Story Node:

- Describes **daily stage → prod promotion** governed by `.github/workflows/kfm-auto-update.yml`.  
- Highlights:
  - ingest & ingest validation in **stage**  
  - governed promotion to **prod**  
  - FAIR+CARE & H3 gates  
  - supply-chain (SBOM/SLSA) checks  
  - telemetry & OpenLineage emission  

When Focus Mode focuses on:

- `kfm-auto-update.yml`  
- `github-infra-telemetry.json`  
- A release tag created by `kfm-auto-update`  

it can surface a narrative explaining:

> “This layer/version was promoted by an automated, fully governed daily update pipeline,  
> which passed FAIR+CARE, sovereignty, security, and metadata checks at both stage and prod levels.”

---

## ⚖ FAIR+CARE & Governance

Even for system-level narratives, Story Nodes must:

- Clearly state the **scope** (system, not cultural/historical narrative).  
- Avoid attributing specific failures to individuals; focus on system behavior.  
- Respect confidentiality and not expose:
  - internal security details  
  - secret locations or credentials  
  - personally identifiable information  

System Story Nodes derived from telemetry must not:

- Embed raw logs with sensitive content.  
- Expose exact internal hostnames or secrets.  
- Present ethics decisions as if they were “absolute truth”; instead, reference policy docs.

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                 |
|--------:|------------|-----------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-28 | Created System Story Nodes index; documented kfm-auto-update node & Focus Mode wiring. |
| v11.2.0 | 2025-11-27 | Drafted system node patterns for CI/CD & telemetry narratives.                         |
| v11.0.0 | 2025-11-18 | Introduced the concept of system-level Story Nodes for KFM infrastructure.             |

---

<div align="center">

🧠 **Kansas Frontier Matrix — System Story Nodes Overview (v11.2.2)**  
System Narratives · Governed Timelines · Focus Mode Meta-Context  

[📘 Docs Root](../../README.md) · [🧠 Story Nodes Index](../README.md) · [🛡 Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md)

</div>
```

