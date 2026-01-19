---
title: "🗺️ Roadmap — Kansas Frontier Matrix (KFM)"
path: "docs/roadmap/README.md"
version: "v0.1.0"
last_updated: "2026-01-19"
status: "living"
doc_kind: "Roadmap"
markdown_protocol_version: "v13"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
---

# 🗺️ KFM Roadmap (Living Document)

![status](https://img.shields.io/badge/status-living-brightgreen)
![pipeline](https://img.shields.io/badge/pipeline-contract--first%20%7C%20deterministic-blue)
![evidence](https://img.shields.io/badge/evidence-STAC%20%7C%20DCAT%20%7C%20PROV-purple)
![ai](https://img.shields.io/badge/AI-Focus%20Mode%20%2B%20Citations-orange)
![ui](https://img.shields.io/badge/UI-MapLibre%20%2B%20Timeline%20%2B%20Story%20Nodes-teal)

> **KFM is not just a database or a map** — it’s a *dynamic, interactive knowledge network* that turns maps, datasets, documents, and models into an auditable, queryable, mappable system.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi) [oai_citation:1‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🧭 Quick Navigation

- [North Star](#-north-star)
- [Non-negotiables](#-non-negotiables)
- [Roadmap at a glance](#-roadmap-at-a-glance)
- [Milestones](#-milestones)
- [Epic backlog](#-epic-backlog)
- [Definition of Done](#-definition-of-done)
- [Issue & label conventions](#-issue--label-conventions)
- [Source library](#-source-library)

---

## 🔭 North Star

KFM’s “north star” is a system that lets people:
- **Discover** trustworthy sources (maps, datasets, docs, imagery) with rich metadata,
- **Connect** them into an evidence graph with provenance (who/what/when/why),
- **Explore** them through map + time + narrative,
- **Ask** focused questions via AI *without hallucinating*, always grounding answers in evidence.  [oai_citation:2‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:3‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

KFM is explicitly built to support reproducible research workflows (e.g., notebooks that can be launched for analysis), and should remain **open, auditable, and extensible**.  [oai_citation:4‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

---

## 🧱 Non-negotiables

### 1) Contract-first + deterministic pipeline ✅
We treat schemas, profiles, and API contracts as **first-class artifacts**, and we design ETL to be **deterministic, idempotent, and auditable**.  [oai_citation:5‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj) [oai_citation:6‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### 2) Canonical pipeline ordering rule 🧬
The system is designed around the pipeline ordering rule:

> **ETL → STAC/DCAT/PROV → Neo4j → APIs → React/Map UI → Story Nodes → Focus Mode**  [oai_citation:7‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### 3) Evidence-first “no mystery nodes” 🔎
KFM relies on an evidence triplet (**STAC + DCAT + PROV**) and requires that the knowledge graph be built from governed metadata + provenance (no untraceable entities).  [oai_citation:8‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

### 4) Policy gates “fail closed” 🚦
Every PR must pass automated checks (schema validation, metadata completeness, license presence, sensitivity classification, provenance completeness). AI outputs must include citations — **fail closed** if requirements aren’t met.  [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

Policy enforcement is expected to be automated via a **Policy Pack** (e.g., OPA/Rego + Conftest) to enforce citation + governance constraints consistently.  [oai_citation:10‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

### 5) AI answers must be sourced (or refuse) 🤖📌
Focus Mode must **always cite sources**, show what it used, and refuse or flag uncertainty when evidence is missing.  [oai_citation:11‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

### 6) Sensitive data handling + CARE 🪶
KFM plans for handling culturally sensitive or protected location data via redaction/generalization, sensitivity tagging, and Indigenous data sovereignty alignment (CARE).  [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

### 7) Privacy-preserving analytics (where needed) 🔐
We treat inference risk seriously: methods like k-anonymity, l-diversity, t-closeness, query auditing, and differential privacy are relevant for protecting sensitive datasets and outputs.  [oai_citation:13‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)

---

## 🗺️ Roadmap at a glance

> This roadmap is **sequenced**, not date-promised. We move forward by “milestone exits” (Definition of Done), not by optimism.

| Horizon | What “done” looks like | Highlights |
|---|---|---|
| **NOW** 🧱 | v13 baseline pipeline + governance | Contracts, policy pack, ingestion gate, STAC/DCAT/PROV validation, Map+Timeline MVP skeleton |
| **NEXT** 🗺️ | KFM usable for real “Map + Time + Story” journeys | Map Timeline slider MVP, Story Nodes workflow, graph-backed search |
| **SOON** 🤖 | Focus Mode v1 is safe + helpful | Retrieval + citations + audit panel + refusal mode |
| **LATER** 📦🌐 | Offline & federation | Offline Packs, GeoParquet+PMTiles packaging, multi-region federation patterns |
| **MOONSHOTS** 🌌 | 4D digital twin / time-travel narratives | Planet-scale, time-aware digital twins and immersive 4D experiences.  [oai_citation:14‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC) |

---

## 🏗️ Milestones

### M0 — Foundations: contracts, CI, docs, and governance 🧱
**Goal:** Make the repo “policy-gradable” so nothing ungoverned slips in.

**Key deliverables**
- [ ] Adopt v13 contract-first documentation + schema discipline.  [oai_citation:15‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- [ ] Policy Pack in CI (OPA/Rego + Conftest style checks) enforcing citations + governance.  [oai_citation:16‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- [ ] Automated Policy Gates enabled (fail-closed): schema + license + sensitivity + provenance + citation rules.  [oai_citation:17‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- [ ] Standard doc templates with Definition of Done checklists (front-matter complete, claims cited, etc.).  [oai_citation:18‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)
- [ ] “Living docs” workflow: docs updated with code changes; periodic doc audits.  [oai_citation:19‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

**Exit criteria**
- CI blocks merges that violate policy gates.
- Templates exist for: roadmap, runbook, data intake SOP, domain module spec, Story Node spec.
- Doc + schema changes are reviewed like code.

---

### M1 — Evidence ingestion v1: the gate that creates trust 📥
**Goal:** Ingest data + docs in a way that is deterministic, governed, and provenance-complete.

**Key deliverables**
- [ ] Implement ingestion gate steps (checksum, schema sanity, CRS/bounds checks, license presence, sensitivity classification, provenance stub).  [oai_citation:20‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- [ ] Deterministic ETL runs (idempotent jobs, stable outputs for same inputs).  [oai_citation:21‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- [ ] STAC/DCAT/PROV validation in CI (metadata-as-code).  [oai_citation:22‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- [ ] PROV is mandatory for publishing/merging governed data.  [oai_citation:23‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- [ ] Document ingestion foundation (OCR/NLP extraction + entity linking) with human-in-the-loop review (“AI steward”).  [oai_citation:24‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

**Exit criteria**
- A dataset + its STAC/DCAT/PROV can be added end-to-end via PR, passing CI.
- Every ingested artifact can be traced by checksum and provenance record.

---

### M2 — Evidence graph v1: Neo4j as the “connective tissue” 🕸️
**Goal:** Build a graph that mirrors the evidence catalogs, not a hand-wavy knowledge base.

**Key deliverables**
- [ ] Neo4j graph schema + ingest from STAC/DCAT/PROV (“no mystery nodes”).  [oai_citation:25‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- [ ] Entity resolution + stable IDs across nodes (doc/feature/dataset/source).  [oai_citation:26‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- [ ] Search index for discovery (e.g., full-text + embeddings) integrated with graph retrieval.  [oai_citation:27‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- [ ] Provenance-aware traversal helpers (e.g., “show chain of evidence”).  [oai_citation:28‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

**Exit criteria**
- Given a map layer or story node, the system can show its source datasets, license, and PROV lineage.

---

### M3 — Map + Timeline MVP: “the product becomes real” 🗺️⏳
**Goal:** Deliver the core interaction: **Map + Time + Layers + Search**.

**UI scope areas (from UI overview)**
- Map canvas, timeline slider, layer panel, search, story mode, focus mode hooks.  [oai_citation:29‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

**Key deliverables**
- [ ] Implement Map Timeline slider MVP (backend date filtering + MapLibre timeline sync).  [oai_citation:30‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- [ ] Layer registry + render pipeline (vector/raster + metadata-driven).  [oai_citation:31‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)
- [ ] Basic story viewing (Story Nodes read-only), anchored to place/time/layers.  [oai_citation:32‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- [ ] Mobile/responsive baseline (phone-first map interactions where possible).  [oai_citation:33‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

**Exit criteria**
- A user can select a time range and see map layers update, and open a story node tied to that time/place.

---

### M4 — Story Nodes v1: narrative as a first-class, governed artifact 🧾
**Goal:** Make narratives trustworthy: stories are versioned, cited, and traceable to evidence.

**Key deliverables**
- [ ] Story Node schema + template + DoD checklist (front-matter, citations, sensitivity labels).  [oai_citation:34‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)
- [ ] UI: Story mode reader with citations panel + provenance panel.  [oai_citation:35‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
- [ ] Example “community story” showing citizen contributions (with governance).  [oai_citation:36‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

**Exit criteria**
- A story node can be validated in CI and displayed in the UI with evidence links.

---

### M5 — Focus Mode v1: safe AI with citations + audit 🔎🤖
**Goal:** AI that accelerates discovery **without making things up**.

**Key deliverables**
- [ ] Focus Mode pipeline: parse → retrieve → LLM → governance_check → answer (with citations).  [oai_citation:37‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- [ ] Hard requirement: every answer cites sources; refusal mode if not derivable.  [oai_citation:38‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- [ ] XAI / Audit panel showing retrieved evidence and reasoning trace.  [oai_citation:39‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- [ ] Policy enforcement for AI (OPA-style rules + tests for citations and sensitive outputs).  [oai_citation:40‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

**Exit criteria**
- Any AI-generated claim links to a source artifact or explicitly flags uncertainty/refusal.

---

### M6 — Performance + packaging + offline 📦⚡
**Goal:** Make KFM fast at scale, and usable in low-connectivity contexts.

**Key deliverables**
- [ ] Standard “GeoParquet + PMTiles” packaging pattern with STAC/DCAT records.  [oai_citation:41‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)
- [ ] Offline Pack feature: download region/time bundle for offline usage.  [oai_citation:42‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- [ ] Raster pipeline optimization: COG + pre-tiling + cached tiles.  [oai_citation:43‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-BJN3xmP44EHc9NRCccCn4H)

**Exit criteria**
- “Offline Pack” can be generated and used to load a map+timeline session without internet.

---

### M7 — Federation + multi-region 🌐
**Goal:** Enable a federation of regions (Kansas-first, but not Kansas-only).

**Key deliverables**
- [ ] Shared schemas + identifiers + ontologies across regions.  [oai_citation:44‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- [ ] Federation mechanism: central hub harvests DCAT; state-prefix IDs; cross-region PROV references.  [oai_citation:45‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- [ ] Configurable UI + minimal Kansas hardcoding (“federation-ready”).  [oai_citation:46‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

**Exit criteria**
- Two catalogs (Kansas + another region) can be discovered and searched in a unified UI.

---

### M8 — 3D / AR / 4D digital twin (research track) 🛰️🕶️
**Goal:** Explore immersive “time-travel” mapping and 4D narratives (place + time + change).

**Why this exists**
- Digital twins are trending toward **4D**: time-aware experiences capturing change over time.  [oai_citation:47‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)

**Key deliverables**
- [ ] 3D toggle and/or AR overlays consuming the same evidence APIs.  [oai_citation:48‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- [ ] Prototype “time travel” narrative: Story Nodes + timeline + imagery overlays.  [oai_citation:49‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)
- [ ] Research protocols documented using scientific method templates (reproducible experiments).  [oai_citation:50‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

**Exit criteria**
- A demo proves the interaction model, with documented experiment protocol + results.

---

## 🧩 Epic backlog

<details>
<summary><strong>📥 Data intake & evidence catalogs</strong></summary>

- [ ] STAC collections for every geospatial dataset; DCAT for discoverability; PROV for lineage.  [oai_citation:51‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- [ ] Bulk ingestion UI (drag/drop) with OCR + entity extraction + link suggestions.  [oai_citation:52‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- [ ] “No mystery nodes” enforcement: every graph entity must tie to a governed artifact.  [oai_citation:53‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

</details>

<details>
<summary><strong>🕸️ Graph, search, and provenance</strong></summary>

- [ ] Neo4j schema module system (domain expansions via governed ontologies).  [oai_citation:54‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- [ ] Provenance explorer UI: evidence chain visualization.  [oai_citation:55‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- [ ] Search improvements: hybrid full-text + embedding + graph neighborhoods.  [oai_citation:56‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

</details>

<details>
<summary><strong>🗺️ UI: Map, timeline, story</strong></summary>

- [ ] Map Timeline slider MVP shipped.  [oai_citation:57‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- [ ] Story Node authoring workflow (template + UI editor).  [oai_citation:58‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)
- [ ] Accessibility + keyboard navigation + clear layering patterns (UI “musts”).  [oai_citation:59‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

</details>

<details>
<summary><strong>🤖 AI Focus Mode</strong></summary>

- [ ] Governance check layer required for all AI outputs.  [oai_citation:60‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- [ ] “Refuse if unsourced” guardrail.  [oai_citation:61‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- [ ] Audit panel standard (evidence used, provenance, uncertainty).  [oai_citation:62‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

</details>

<details>
<summary><strong>📦 Performance, packaging, offline</strong></summary>

- [ ] Standard packaging: GeoParquet + PMTiles + STAC/DCAT records.  [oai_citation:63‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)
- [ ] Offline Pack bundler + verifier.  [oai_citation:64‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- [ ] Tile caching + vector/raster performance baseline (WebGL where useful).  [oai_citation:65‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)

</details>

<details>
<summary><strong>🔒 Security, privacy, ethics</strong></summary>

- [ ] Sensitivity + CARE labels in front matter; review workflows for restricted data.  [oai_citation:66‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)
- [ ] Query auditing + inference control where applicable.  [oai_citation:67‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)

</details>

<details>
<summary><strong>🌐 Federation + community</strong></summary>

- [ ] Multi-region federation patterns (ID prefixes, harvested catalogs).  [oai_citation:68‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- [ ] Governance board + glossary + community contributor pathways.  [oai_citation:69‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

</details>

---

## ✅ Definition of Done

> We treat documentation + metadata like code: **front-matter valid, claims cited, policy gates pass**.  [oai_citation:70‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz) [oai_citation:71‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

### DoD — for a milestone
- [ ] Pipeline artifacts exist (schemas/profiles/contracts) and are versioned.
- [ ] CI enforces policy gates (fail closed).
- [ ] Ingested artifacts have license + sensitivity + PROV lineage.
- [ ] UI can render the intended slice (map/time/story) without manual DB edits.
- [ ] If AI is involved: citations + refusal mode + audit panel are implemented.

### DoD — for a Story Node (narrative)
- [ ] YAML front-matter includes sensitivity/CARE labels.
- [ ] Every factual claim is backed by evidence link(s).
- [ ] Citations render into UI evidence panel.
- [ ] Review approvals include any required data steward review.

---

## 🏷️ Issue & label conventions

### Recommended labels
- **type:** `type:feature`, `type:bug`, `type:policy`, `type:data`, `type:docs`, `type:research`
- **area:** `area:intake`, `area:catalog`, `area:graph`, `area:api`, `area:ui`, `area:ai`, `area:security`, `area:federation`
- **priority:** `p0`, `p1`, `p2`
- **risk:** `risk:privacy`, `risk:licensing`, `risk:performance`, `risk:governance`

### Issue template (copy/paste)
```md
## 🎯 Goal
What outcome do we want?

## 📦 Deliverables
- [ ] ...

## 🔎 Evidence & Contracts
- STAC/DCAT/PROV impact:
- Schema/contracts changed:
- Policy gates required:

## ✅ Acceptance Criteria
- [ ] ...

## 🔗 Dependencies
- #issue
- doc link

## 🧨 Risks
- ...
```

---

## 📚 Source library

> These are the roadmap’s **inputs**. If a file is a **PDF Portfolio**, we should extract/unpack it into individually indexable docs (roadmap item).  [oai_citation:72‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)

### Core KFM system docs
- 🧠 **AI System Overview** — Focus Mode, citations, auditability, governance checks.  [oai_citation:73‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- 🧩 **Comprehensive Architecture, Features, and Design** — platform design, policy gates, federation, UX direction.  [oai_citation:74‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- 🗺️ **Comprehensive UI System Overview** — UI module map (map/timeline/layers/story/focus).  [oai_citation:75‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
- 📥 **Data Intake – Technical & Design Guide** — canonical pipeline ordering, ingestion gates, evidence triplet, PROV requirements.  [oai_citation:76‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- 🧱 **Comprehensive Technical Documentation** — end-to-end platform concepts (knowledge network, remote sensing, performance, governance).  [oai_citation:77‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)
- 🌟 **Latest Ideas & Future Proposals** — offline packs, tiling strategy (GeoParquet/PMTiles), timeline MVP ideas.  [oai_citation:78‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)
- 💡 **Innovative Concepts to Evolve KFM** — digital twin / 4D direction, immersive futures.  [oai_citation:79‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  [oai_citation:80‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)
- 🧭 **Open-Source Geospatial Historical Mapping Hub Design** — ingestion-to-UI design including COG/tiles/OCR and Map UI approach.  [oai_citation:81‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- 🧾 **MARKDOWN_GUIDE v13** — contract-first & deterministic documentation + pipeline rules.  [oai_citation:82‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### Research + reference packs (to unpack/index)
- 🤖 **AI Concepts & more (PDF Portfolio)** — AI learning/reference pack (needs extraction).  [oai_citation:83‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)
- 🌍 **Maps / GoogleMaps / VirtualWorlds / WebGL (PDF Portfolio)** — mapping + virtual worlds reference pack (needs extraction).  [oai_citation:84‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)
- 🧰 **Various programming languages & resources (PDF Portfolio)** — language/tool reference pack (needs extraction).  [oai_citation:85‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)
- 🗄️ **Data Management / Theories / Architectures / Bayesian (PDF Portfolio)** — data architecture reference pack (needs extraction).  [oai_citation:86‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)

### Embedded / extracted books and guides already indexed
- 📘 **Python Geospatial Analysis Cookbook** — Folium/Leaflet/WebGL/tiles patterns and recipes.  [oai_citation:87‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)
- 🔐 **Data Mining Concepts & Applications** — inference control, query auditing, privacy techniques.  [oai_citation:88‡KFM- python-geospatial-analysis-cookbook-over-60-recipes-to-work-with-topology-overlays-indoor-routing-and-web-application-analysis-with-python.pdf](file-service://file-2gpiGDZS8iw6EdxGswEdHp)
- ✍️ **Comprehensive Markdown Guide** — templates, governance front-matter, DoD checklists.  [oai_citation:89‡Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx](file-service://file-J6rFRcp4ExCCeCdTevQjxz)
- 🧪 **Scientific Method / Research / Master Coder Protocol** — living documentation + reproducible experiment practices.  [oai_citation:90‡Scientific Method _ Research _ Master Coder Protocol Documentation.pdf](file-service://file-HTpax4QbDgguDwxwwyiS32)

---

## 📌 One last rule (to keep us honest)

If it can’t pass the gates (contracts ✅, provenance ✅, sensitivity ✅, citations ✅), **it doesn’t ship**.  [oai_citation:91‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)