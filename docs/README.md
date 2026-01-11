---
id: DOC-DOCS-README
title: "docs/ — Kansas Frontier Matrix (KFM) Governed Documentation"
status: active
version: v1.1.0
last_updated: 2026-01-11
owners:
  - KFM Engineering
tags:
  - kfm
  - documentation
  - governance
  - standards
  - runbooks
  - story-nodes
  - focus-mode
---

<!--
📌 This README documents the *canonical governed documentation boundary* for KFM.
🗓️ Last updated: 2026-01-11
✅ Note: KFM’s v13 docs discipline assumes docs are validated (front‑matter + links + schemas) and treated as shippable system artifacts.
-->

# 📚 `docs/` — Kansas Frontier Matrix (KFM) Governed Documentation 📜🧭

![KFM](https://img.shields.io/badge/KFM-docs%2F%20canonical-1f6feb)
![README](https://img.shields.io/badge/README-v1.1.0-8957e5)
![Evidence](https://img.shields.io/badge/evidence--first-STAC%20%2B%20DCAT%20%2B%20PROV-0aa3a3)
![Contract-first](https://img.shields.io/badge/contract--first-schemas%20%2B%20API%20contracts-0aa3a3)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE%20%2B%20Sovereignty-2ea043)
![Accessibility](https://img.shields.io/badge/docs-accessible%20%2B%20scannable%20%2B%20citable-8250df)
![Security](https://img.shields.io/badge/security-no%20secrets%20%2B%20no%20side--channels-red)

> Canonical home for KFM’s **governed documentation**:  
> **architecture + standards + templates + runbooks + governance + story nodes** — written so that decisions are **auditable**, claims are **citable**, and change is **reviewable**.  
> This is where KFM stays explainable as it scales. 🧠🗺️

> [!IMPORTANT]
> **KFM’s non‑negotiable order (docs must reinforce it):**  
> **ETL → STAC/DCAT/PROV Catalogs → Graph → APIs → UI → Story Nodes → Focus Mode**  
> If a doc encourages bypassing the ordering (even as a “temporary shortcut”), it’s wrong.

---

## 🔗 Quick links
- 🧭 Repo overview: **[`../README.md`](../README.md)**
- 📦 Data + metadata boundary: **[`../data/README.md`](../data/README.md)**
- 🧪 MCP (methods + receipts): **[`../mcp/README.md`](../mcp/README.md)** *(if present)*
- 🧩 Executable code boundary: **[`../src/README.md`](../src/README.md)** *(if present)*
- 🧾 Pipelines boundary: **[`../src/pipelines/README.md`](../src/pipelines/README.md)** *(if present)*
- 🧪 Tests boundary: **[`../tests/README.md`](../tests/README.md)** *(if present)*
- 📓 Notebooks boundary: **[`../notebooks/README.md`](../notebooks/README.md)** *(if present)*
- 📐 Schemas registry: **[`../schemas/README.md`](../schemas/README.md)** *(if present)*
- 🌐 Web UI boundary: **[`../web/README.md`](../web/README.md)** *(if present)*
- 🤝 CI/CD + templates: **[`../.github/README.md`](../.github/README.md)** *(if present)*

---

## 🧭 Quick navigation
- [📘 Overview](#-overview)
- [🧾 Doc metadata](#-doc-metadata)
- [🧠 Core invariants](#-core-invariants)
- [📖 Glossary](#-glossary-kfm-terms-used-in-docs)
- [🗂️ What goes in `docs/`](#️-what-goes-in-docs)
- [🧱 Directory layout](#-directory-layout)
- [🏁 Golden paths](#-golden-paths-most-common-doc-workflows)
- [✅ Doc quality gates](#-doc-quality-gates-definition-of-done)
- [🧾 Evidence, citations, and provenance pointers](#-evidence-citations-and-provenance-pointers)
- [📚 Story Nodes and Focus Mode rules](#-story-nodes-and-focus-mode-rules)
- [🔒 Security, sovereignty, and sensitive info](#-security-sovereignty-and-sensitive-info)
- [🧪 Modeling and simulation documentation](#-modeling-and-simulation-documentation)
- [⚙️ Scaling and data management documentation](#️-scaling-and-data-management-documentation)
- [🎨 Visualization and UX documentation](#-visualization-and-ux-documentation)
- [📚 Project reference library influence map](#-project-reference-library-influence-map)
- [🕰️ Version history](#️-version-history)

---

## 🧾 Doc metadata

| Field | Value |
|---|---|
| Doc | `docs/README.md` |
| Status | Active ✅ |
| Last updated | **2026-01-11** |
| Audience | Contributors writing standards, runbooks, story nodes, ADRs, and governance policies |
| Prime directive | If it changes what people *believe* about the map/story/data, it must be **reviewable + citable + reversible** |
| Repo posture | **Evidence-first** + **Contract-first** + **Sovereignty-aware** |

---

## 📘 Overview

### ✅ Purpose
`docs/` exists so KFM remains:
- **understandable** (clear architecture + vocabulary)
- **governable** (policy and review gates are explicit)
- **auditable** (why a decision happened, and when)
- **evidence-first** (claims point to cataloged evidence)
- **humane** (transparent impacts, consent, dignity, and accountability)
- **change-friendly** (structured docs that evolve with requirements instead of becoming fossilized)

### 🚫 What `docs/` is not
- not a dumping ground for generated outputs *(those belong under `data/**` and catalogs)*
- not a substitute for contracts *(schemas and API contracts live under `schemas/**` and `src/server/**`)*
- not a place for secrets, tokens, credentials, internal hostnames, or private URLs 🚫

---

## 🧠 Core invariants

> [!IMPORTANT]
> **Docs are part of the system boundary.**  
> When a subsystem changes, docs should change **in the same PR** whenever feasible. Docs are “shipped,” not “updated later.”

```mermaid
flowchart LR
  A[🧪 ETL Pipelines] --> B[🗂️ STAC/DCAT/PROV Catalogs]
  B --> C[🕸️ Graph]
  C --> D[🛡️ APIs]
  D --> E[🖥️ UI]
  E --> F[📚 Story Nodes]
  F --> G[🎯 Focus Mode]
