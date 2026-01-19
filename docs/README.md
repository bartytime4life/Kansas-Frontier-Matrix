---
title: "📚 `docs/` — Kansas Frontier Matrix (KFM) Governed Documentation 📜🧭"
path: "docs/README.md"
version: "v1.3.1"
last_updated: "2026-01-19"
status: "active"
doc_kind: "Directory README"
license: "CC-BY-4.0"

# Protocols (repo defaults)
markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

# Governance & provenance posture
fair_category: "FAIR+CARE"
care_label: "Public"
sensitivity: "public"
classification: "open"
owner: "KFM Engineering"
governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
review_cycle: "quarterly"

# Canonical references (expected)
canonical_master_guide: "docs/MASTER_GUIDE_v13.md"
canonical_glossary: "docs/glossary.md"
canonical_library_index: "docs/library/README.md"
canonical_story_nodes_root: "docs/reports/story_nodes/"
---

<a id="top"></a>

# 📚 `docs/` — Kansas Frontier Matrix (KFM) Governed Documentation 📜🧭

![KFM](https://img.shields.io/badge/KFM-docs%2F%20canonical-1f6feb)
![KFM-MDP](https://img.shields.io/badge/KFM--MDP-v11.2.6-8957e5)
![Version](https://img.shields.io/badge/version-v1.3.1-8957e5)
![Updated](https://img.shields.io/badge/updated-2026--01--19-2ea043)
![Evidence](https://img.shields.io/badge/evidence--first-STAC%20%2B%20DCAT%20%2B%20PROV-0aa3a3)
![Contract-first](https://img.shields.io/badge/contract--first-schemas%20%2B%20API%20contracts-0aa3a3)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE%20%2B%20Sovereignty-2ea043)
![Policy](https://img.shields.io/badge/policy--pack-OPA%20%2B%20conftest%20gates-ff8c00)
![Accessibility](https://img.shields.io/badge/docs-accessible%20%2B%20scannable%20%2B%20citable-8250df)
![License](https://img.shields.io/badge/license-CC--BY--4.0-blue)
![Security](https://img.shields.io/badge/security-no%20secrets%20%2B%20no%20side--channels-red)

> Canonical home for KFM’s **governed documentation**:  
> **architecture + standards + guides + templates + runbooks + governance + story nodes** — written so decisions are **auditable**, claims are **citable**, and change is **reviewable**.  
> Docs are part of the system boundary: if it changes what people *believe* about the map/story/data, it must be **reviewable + citable + reversible**.

> [!IMPORTANT]
> **KFM’s non-negotiable order (docs must reinforce it):**  
> **ETL → STAC/DCAT/PROV Catalogs → Graph → APIs → UI → Story Nodes → Focus Mode**  
> If a doc encourages bypassing the ordering (even as a “temporary shortcut”), it’s wrong.

---

## 🔗 Quick links
- 🧭 Repo overview: **[`../README.md`](../README.md)**
- 📘 Master system map: **[`./MASTER_GUIDE_v13.md`](./MASTER_GUIDE_v13.md)** *(canonical architecture + repo shape)*
- 🏛️ Governance charter: **[`./governance/ROOT_GOVERNANCE.md`](./governance/ROOT_GOVERNANCE.md)**
- 🧭 Ethics: **[`./governance/ETHICS.md`](./governance/ETHICS.md)**
- 🧬 Sovereignty policy: **[`./governance/SOVEREIGNTY.md`](./governance/SOVEREIGNTY.md)**
- ✅ Review gates: **[`./governance/REVIEW_GATES.md`](./governance/REVIEW_GATES.md)** *(if present)*

**Doc-making helpers**
- 🧾 Universal doc template: **[`./templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`](./templates/TEMPLATE__KFM_UNIVERSAL_DOC.md)** *(if present)*
- 📚 Story Node template: **[`./templates/TEMPLATE__STORY_NODE_V3.md`](./templates/TEMPLATE__STORY_NODE_V3.md)** *(if present)*
- 🛡️ API contract extension template: **[`./templates/TEMPLATE__API_CONTRACT_EXTENSION.md`](./templates/TEMPLATE__API_CONTRACT_EXTENSION.md)** *(if present)*
- ✍️ Markdown work protocol: **[`./standards/KFM_MARKDOWN_WORK_PROTOCOL.md`](./standards/KFM_MARKDOWN_WORK_PROTOCOL.md)** *(if present)*

**System boundaries**
- 📦 Data + metadata boundary: **[`../data/README.md`](../data/README.md)**
- 🧬 Provenance runs/receipts (MCP): **[`../mcp/README.md`](../mcp/README.md)** *(if present)*
- 📐 Schemas registry: **[`../schemas/README.md`](../schemas/README.md)** *(if present)*
- 🧪 Pipelines boundary: **[`../src/pipelines/README.md`](../src/pipelines/README.md)** *(if present)*
- 🕸️ Graph build boundary: **[`../src/graph/README.md`](../src/graph/README.md)** *(if present)*
- 🛡️ API boundary: **[`../src/server/README.md`](../src/server/README.md)** *(if present)*
- 🔐 Policy Pack (CI gates): **[`../api/scripts/policy/README.md`](../api/scripts/policy/README.md)** *(if present)*
- 🌐 Web UI boundary: **[`../web/README.md`](../web/README.md)** *(if present)*
- 🧪 Tests boundary: **[`../tests/README.md`](../tests/README.md)** *(if present)*
- 🧰 Tools boundary: **[`../tools/README.md`](../tools/README.md)** *(if present)*
- 🧾 Releases boundary: **[`../releases/README.md`](../releases/README.md)** *(if present)*

**Guides (cross-cutting “how-to”)**
- 📥 Ingestion guide: **[`./guides/pipelines/ingestion-guide.md`](./guides/pipelines/ingestion-guide.md)** *(if present)*
- 🤖 AI pipeline cookiecutter: **[`./guides/pipelines/kfm-ai-pipeline-cookiecutter.md`](./guides/pipelines/kfm-ai-pipeline-cookiecutter.md)** *(if present)*
- ⚖ FAIR+CARE oversight: **[`./guides/governance/faircare-oversight.md`](./guides/governance/faircare-oversight.md)** *(if present)*

---

## 🧭 Quick navigation
- [📘 Overview](#-overview)
- [🧾 Doc metadata](#-doc-metadata)
- [🧠 Core invariants](#-core-invariants)
- [🧫 Data lifecycle and artifact locations](#-data-lifecycle-and-artifact-locations)
- [📖 Glossary](#-glossary-kfm-terms-used-in-docs)
- [🗂️ What goes in `docs/`](#-what-goes-in-docs)
- [🧱 Directory layout](#-directory-layout)
- [🏁 Golden paths](#-golden-paths-most-common-doc-workflows)
- [✅ Doc quality gates](#-doc-quality-gates-definition-of-done)
- [🧾 Evidence, citations, and provenance pointers](#-evidence-citations-and-provenance-pointers)
- [📚 Story Nodes and Focus Mode rules](#-story-nodes-and-focus-mode-rules)
- [🔒 Security, sovereignty, and sensitive info](#-security-sovereignty-and-sensitive-info)
- [🧪 Modeling, simulation, and inference documentation](#-modeling-simulation-and-inference-documentation)
- [🤖 Machine learning and AI documentation](#-machine-learning-and-ai-documentation)
- [⚙️ Scaling and data management documentation](#-scaling-and-data-management-documentation)
- [🕸️ Graph and ontology documentation](#-graph-and-ontology-documentation)
- [🎨 Visualization and UX documentation](#-visualization-and-ux-documentation)
- [📚 Project reference library influence map](#-project-reference-library-influence-map)
- [📚 Library intake policy](#-library-intake-policy-license-aware)
- [🕰️ Version history](#-version-history)

---

## 🧾 Doc metadata

| Field | Value |
|---|---|
| Doc | `docs/README.md` |
| Status | Active ✅ |
| Version | **v1.3.1** |
| Last updated | **2026-01-19** |
| Audience | Contributors writing standards, guides, runbooks, Story Nodes, ADRs, and governance policies |
| Prime directive | If it changes what people *believe* about the map/story/data, it must be **reviewable + citable + reversible** |
| Repo posture | **Evidence-first** + **Contract-first** + **Sovereignty-aware** + **License-aware** + **Append-only publishing mindset** |

> [!NOTE]
> The YAML front-matter is authoritative for protocol versions and governance posture.  
> This table is a human-friendly snapshot.

---

## 📘 Overview

### ✅ Purpose
`docs/` exists so KFM remains:
- **understandable** (clear architecture + vocabulary)
- **governable** (policy and review gates are explicit)
- **auditable** (why a decision happened, and when)
- **evidence-first** (claims point to cataloged evidence)
- **contract-first** (schemas + API contracts define reality; docs explain it)
- **humane** (transparent impacts, consent, dignity, and accountability) ❤️
- **change-friendly** (structured docs that evolve instead of fossilizing) 🔁
- **license-aware** (meaning + metadata must respect legal/ethical constraints) 🪪

### 🚫 What `docs/` is not
- not a dumping ground for generated outputs *(those belong under `data/**` and catalogs)*
- not a substitute for contracts *(schemas and API contracts define behavior)*
- not a place for secrets, tokens, credentials, internal hostnames, or private URLs 🚫
- not a “shadow API” (docs explain; contracts enforce)

---

## 🧠 Core invariants

> [!IMPORTANT]
> **Docs are part of the system boundary.**  
> When a subsystem changes, docs should change **in the same PR** whenever feasible.

```mermaid
flowchart LR
  A[🧪 ETL Pipelines] --> B[🗂️ STAC/DCAT/PROV Catalogs]
  B --> C[🕸️ Graph]
  C --> D[🛡️ APIs]
  D --> E[🖥️ UI]
  E --> F[📚 Story Nodes]
  F --> G[🎯 Focus Mode]