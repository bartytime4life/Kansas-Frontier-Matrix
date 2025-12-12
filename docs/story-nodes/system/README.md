---
title: "🧠 Kansas Frontier Matrix — System Story Nodes Overview"
path: "docs/story-nodes/system/README.md"

version: "v11.2.6"
last_updated: "2025-12-12"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council & Focus Mode Board"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../releases/v11.2.6/signature.sig"
attestation_ref: "../../../releases/v11.2.6/slsa-attestation.json"
sbom_ref: "../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.6/manifest.zip"

telemetry_ref: "../../../releases/v11.2.6/github-infra-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/storynodes-system-v1.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Index"
intent: "story-nodes-system-overview"
role: "focusmode-system-index"
category: "Story Nodes · Focus Mode · System Architecture"

classification: "Public"
sensitivity: "General (non-sensitive)"
sensitivity_level: "None"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false
indigenous_rights_flag: false

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
data_steward: "KFM FAIR+CARE Council"

doc_uuid: "urn:kfm:doc:story-nodes:system:index:v11.2.6"
semantic_document_id: "kfm-story-nodes-system-index-v11.2.6"
event_source_id: "ledger:kfm:doc:story-nodes:system:index:v11.2.6"
immutability_status: "version-pinned"

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
  - "docs/story-nodes/system/README.md@v11.2.2"
  - "docs/story-nodes/system/README.md@v11.2.0"
  - "docs/story-nodes/system/README.md@v11.0.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: false

json_schema_ref: "../../../schemas/json/storynodes-system-readme-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/storynodes-system-readme-v11-shape.ttl"

diagram_profiles:
  - "mermaid-flowchart-v1"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
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
  - "schema-lint"
  - "metadata-check"
  - "diagram-check"
  - "provenance-check"
  - "footer-check"

ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"
---

<div align="center">

# 🧠 **Kansas Frontier Matrix — System Story Nodes Overview**  
`docs/story-nodes/system/README.md`

**Purpose**  
Serve as the **index and architectural guide** for **system-level Story Nodes** used by Focus Mode to explain  
KFM’s **automation behavior over time** — CI/CD runs, governance gates, reliability status, and telemetry/lineage outputs — in a strictly governed, non-speculative format.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/Story%20Nodes-System%20Index-informational" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Enforced-brightgreen" />

</div>

---

## 📘 Overview

System Story Nodes are **machine- and human-readable narrative objects** that represent **platform behavior** (not people or places). They are designed for Focus Mode to answer questions like:

- “What automation promoted this release or dataset?”
- “Why did a pipeline gate fail, and what evidence supports that?”
- “How has CI reliability or governance noise changed over time?”
- “Which workflows generated these artifacts, and what lineage/telemetry backs them?”

System Story Nodes typically describe:

- CI/CD processes and pipeline states (auto-update, release promotion, lint/validation gates)  
- Governance events (policy changes, FAIR+CARE decisions, approvals/waivers)  
- Infrastructure health stories (SLO status, error budgets, regression signals)  
- Operational rhythms (daily refreshes, weekly re-indexing, scheduled audits)

**Non-negotiable constraint:** system narratives MUST be **strictly factual** and **backed by telemetry/lineage**, with links to authoritative artifacts. No motive attribution. No invented causes.

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 story-nodes/
    ├── 📄 README.md                          # Global Story Nodes overview (all domains)
    ├── 📁 system/                            # System-level Story Nodes (this directory)
    │   ├── 📄 README.md                      # ← System Story Nodes index (this file)
    │   ├── 🧾 kfm-auto-update.json           # Daily stage → prod promotion Story Node (example)
    │   ├── 🧾 ci-health.json                 # (planned) CI health + failure-rate narrative
    │   ├── 🧾 releases-timeline.json         # (planned) Release cadence & quality history
    │   └── 📁 templates/                     # Templates & patterns for system Story Nodes
    └── 📁 domains/                           # User-facing domain Story Nodes (history, hydro, soil, etc.)
        ├── 📁 history/
        ├── 📁 hydrology/
        ├── 📁 climate/
        └── 📁 archaeology/
~~~

**Directory rules (normative)**

- Every `docs/story-nodes/system/*.json` MUST validate against the Story Node schema used by KFM v11.  
- Each new system Story Node MUST be:
  - listed here, and
  - cross-linked from `docs/story-nodes/README.md`.  
- System nodes SHOULD be non-spatial (`geometry: null`) unless a **non-sensitive** bounding extent is required.

---

## 🧭 Context

System Story Nodes exist to make KFM’s automation **inspectable and governable**.

They sit inside the canonical KFM pipeline as **meta-narratives**:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j → API → UI → Story Nodes → Focus Mode

System Story Nodes are where Focus Mode learns:

- which workflow ran,
- what it validated,
- which artifacts it generated,
- and what governance policies applied at the time.

They rely on evidence sources like:

- CI artifacts and summaries (lint reports, validation reports, security checks)  
- OpenLineage / PROV-style lineage exports  
- release manifests + signatures (SBOM/SLSA where applicable)  
- aggregated telemetry snapshots (`github-infra-telemetry.json`, `focus-telemetry.json`)

---

## 🗺️ Diagrams

The diagram below shows the **safe ingestion pattern** for system narratives.

~~~mermaid
flowchart LR
    A["Workflow run (CI/CD, ETL, audit)"] --> B["Telemetry + Lineage (PROV/OpenLineage)"]
    B --> C["System Story Node (governed JSON)"]
    C --> D["Focus Mode system context"]
    D --> E["Dashboards and governance review"]
~~~

Diagram rule: keep labels simple and quoted to avoid Mermaid parse failures in GitHub renderers.

---

## 🧠 Story Node & Focus Mode Integration

System Story Nodes are consumed by Focus Mode to:

- Provide **system timelines** (e.g., “auto-update success rate over 90 days”)  
- Explain **governed behavior** (e.g., “promotion blocked by sovereignty gate”)  
- Surface **meta-context** for maintainers (e.g., “docs-lint failures increased after rule change”)  
- Offer **evidence links** (telemetry snapshots, reports, manifests)

Focus Mode may generate UI overlays for:

- `.github/workflows/**` (what this workflow does, what it emitted, what failed)  
- `releases/**` (how a release was produced and validated)  
- `docs/standards/**` (what rules were in force when a decision was made)

**Hard constraints (normative)**

- MUST be factual, evidence-linked, and reproducible.  
- MUST NOT speculate, invent causes, or “explain” failures without artifacts.  
- MUST NOT embed secrets, internal hostnames, or raw logs with sensitive content.

---

## 🧪 Validation & CI/CD

System Story Nodes are CI-enforced.

Minimum checks (typical):

- `schema-lint`: validate Story Node JSON against the correct schema  
- `metadata-check`: ensure stable IDs, timestamps, and required governance refs exist  
- `provenance-check`: node references a commit/release/telemetry artifact when required  
- `markdown-lint` + `footer-check`: applies to this README and any template docs

System nodes that fail validation are **non-governed outputs** and MUST NOT be treated as production narrative sources.

---

## 📦 Data & Metadata

### 1. Identity and naming

System Story Nodes SHOULD use stable URNs:

- `urn:kfm:story-node:system:<topic>:<run_id_or_interval>`

And SHOULD record:

- `id` (URN)  
- `title`, `summary`  
- `version` (node version, not repo release)  
- `spacetime.when` (instant or interval)  
- `links.targets[]` (workflows, reports, manifests, telemetry)  
- `governance` block pointing to:
  - `governance_ref`
  - `ethics_ref`
  - `sovereignty_policy` (even if non-applicable, it should be explicit)

### 2. Evidence-first linking

A system narrative is only as trustworthy as its links. Each system node SHOULD link to:

- the workflow definition(s) that executed  
- the telemetry snapshot(s) used  
- the report artifact(s) being summarized  
- release manifests (if describing a release)  
- signatures/attestations where present

---

## 🌐 STAC, DCAT & PROV Alignment

System narratives are often non-spatial, but still catalogable.

### DCAT

- Model system nodes as documentation datasets:
  - `dct:title` = `title`
  - `dct:identifier` = `id`
  - `dct:modified` = node timestamp/end time
  - `dct:license` = `license`
- Attach artifacts as `dcat:Distribution` entries (reports, telemetry JSON, manifests)

### STAC

- Represent a system node as a STAC Item in a `kfm-story-nodes` Collection:
  - `id` = stable identifier (or a derived slug)
  - `properties.datetime` = node timestamp
  - `geometry: null` (typical)
  - `assets` include:
    - `story-node` (the JSON itself)
    - `telemetry` (linked telemetry snapshot)
    - `reports` (linked validation artifacts)

### PROV-O

Treat a system node as a `prov:Entity` describing/deriving from:

- a `prov:Activity` (workflow run)
- that `prov:used` inputs (schemas/configs/datasets)
- and `prov:generated` outputs (reports/telemetry/manifests)

This supports queries like:
- “Which workflow run generated the evidence summarized by this system node?”

---

## 🧱 Architecture

System Story Nodes are an interface boundary between:

- **Operational reality** (workflows, telemetry, lineage)
- and **human explanation** (Focus Mode narratives)

Recommended module boundaries:

- `.github/workflows/*` orchestrates jobs  
- `scripts/` and `tools/` emit telemetry + lineage  
- `releases/<ver>/` stores immutable snapshots (telemetry, manifests, SBOMs)  
- `docs/story-nodes/system/*.json` stores the governed narrative objects  
- Focus Mode consumes nodes but does not rewrite or “repair” them

Design rule: system Story Nodes SHOULD summarize, link, and contextualize — never replace the evidence.

---

## ⚖ FAIR+CARE & Governance

Even system-level narratives must uphold FAIR+CARE:

- **Findable**: stable IDs and predictable paths  
- **Accessible**: public-safe summaries and links (no secrets)  
- **Interoperable**: PROV/DCAT/STAC-aligned metadata where applicable  
- **Reusable**: clear versioning, provenance, and licensing

Governance enforcement notes:

- Any waiver or exception (e.g., allowing a release despite a non-critical failure) MUST be:
  - documented in the governance ledger, and
  - referenced by the system Story Node rather than “explained away” inside the node.

---

## 🕰️ Version History

| Version     | Date       | Summary                                                                 |
|------------:|-----------:|-------------------------------------------------------------------------|
| **v11.2.6** | 2025-12-12 | Upgraded to KFM‑MDP v11.2.6; normalized directory tree style; added diagrams + STAC/DCAT/PROV alignment; tightened transform permissions; strengthened evidence-first requirements. |
| v11.2.2     | 2025-11-28 | Created System Story Nodes index; documented system node patterns.      |
| v11.2.0     | 2025-11-27 | Drafted system node scaffolding for CI/CD & telemetry narratives.       |
| v11.0.0     | 2025-11-18 | Introduced concept of system-level Story Nodes for KFM infrastructure.  |

---

<div align="center">

🧠 **Kansas Frontier Matrix — System Story Nodes Overview (v11.2.6)**  
System Narratives · Governed Timelines · Evidence-Linked Focus Mode Context  

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governance%20Aligned-gold" />
<img src="https://img.shields.io/badge/Lineage-PROV%20%2F%20OpenLineage-informational" />

[📘 Docs Root](../../README.md) ·
[🧠 Story Nodes Index](../README.md) ·
[📑 Markdown Protocol v11.2.6](../../standards/kfm_markdown_protocol_v11.2.6.md) ·
[🛡 Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md) ·
[⚖ FAIR+CARE Guide](../../standards/faircare/FAIRCARE-GUIDE.md)

</div>