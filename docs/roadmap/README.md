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

> **KFM is not just a database or a map** — it’s a *dynamic, interactive knowledge network* that turns maps, datasets, documents, and models into an auditable, queryable, mappable system. :contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}

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
- **Ask** focused questions via AI *without hallucinating*, always grounding answers in evidence. :contentReference[oaicite:2]{index=2}:contentReference[oaicite:3]{index=3}

KFM is explicitly built to support reproducible research workflows (e.g., notebooks that can be launched for analysis), and should remain **open, auditable, and extensible**. :contentReference[oaicite:4]{index=4}

---

## 🧱 Non-negotiables

### 1) Contract-first + deterministic pipeline ✅
We treat schemas, profiles, and API contracts as **first-class artifacts**, and we design ETL to be **deterministic, idempotent, and auditable**. :contentReference[oaicite:5]{index=5}:contentReference[oaicite:6]{index=6}

### 2) Canonical pipeline ordering rule 🧬
The system is designed around the pipeline ordering rule:

> **ETL → STAC/DCAT/PROV → Neo4j → APIs → React/Map UI → Story Nodes → Focus Mode** :contentReference[oaicite:7]{index=7}

### 3) Evidence-first “no mystery nodes” 🔎
KFM relies on an evidence triplet (**STAC + DCAT + PROV**) and requires that the knowledge graph be built from governed metadata + provenance (no untraceable entities). :contentReference[oaicite:8]{index=8}

### 4) Policy gates “fail closed” 🚦
Every PR must pass automated checks (schema validation, metadata completeness, license presence, sensitivity classification, provenance completeness). AI outputs must include citations — **fail closed** if requirements aren’t met. :contentReference[oaicite:9]{index=9}

Policy enforcement is expected to be automated via a **Policy Pack** (e.g., OPA/Rego + Conftest) to enforce citation + governance constraints consistently. :contentReference[oaicite:10]{index=10}

### 5) AI answers must be sourced (or refuse) 🤖📌
Focus Mode must **always cite sources**, show what it used, and refuse or flag uncertainty when evidence is missing. :contentReference[oaicite:11]{index=11}

### 6) Sensitive data handling + CARE 🪶
KFM plans for handling culturally sensitive or protected location data via redaction/generalization, sensitivity tagging, and Indigenous data sovereignty alignment (CARE). :contentReference[oaicite:12]{index=12}

### 7) Privacy-preserving analytics (where needed) 🔐
We treat inference risk seriously: methods like k-anonymity, l-diversity, t-closeness, query auditing, and differential privacy are relevant for protecting sensitive datasets and outputs. :contentReference[oaicite:13]{index=13}

---

## 🗺️ Roadmap at a glance

> This roadmap is **sequenced**, not date-promised. We move forward by “milestone exits” (Definition of Done), not by optimism.

| Horizon | What “done” looks like | Highlights |
|---|---|---|
| **NOW** 🧱 | v13 baseline pipeline + governance | Contracts, policy pack, ingestion gate, STAC/DCAT/PROV validation, Map+Timeline MVP skeleton |
| **NEXT** 🗺️ | KFM usable for real “Map + Time + Story” journeys | Map Timeline slider MVP, Story Nodes workflow, graph-backed search |
| **SOON** 🤖 | Focus Mode v1 is safe + helpful | Retrieval + citations + audit panel + refusal mode |
| **LATER** 📦🌐 | Offline & federation | Offline Packs, GeoParquet+PMTiles packaging, multi-region federation patterns |
| **MOONSHOTS** 🌌 | 4D digital twin / time-travel narratives | Planet-scale, time-aware digital twins and immersive 4D experiences. :contentReference[oaicite:14]{index=14} |

---

## 🏗️ Milestones

### M0 — Foundations: contracts, CI, docs, and governance 🧱
**Goal:** Make the repo “policy-gradable” so nothing ungoverned slips in.

**Key deliverables**
- [ ] Adopt v13 contract-first documentation + schema discipline. :contentReference[oaicite:15]{index=15}
- [ ] Policy Pack in CI (OPA/Rego + Conftest style checks) enforcing citations + governance. :contentReference[oaicite:16]{index=16}
- [ ] Automated Policy Gates enabled (fail-closed): schema + license + sensitivity + provenance + citation rules. :contentReference[oaicite:17]{index=17}
- [ ] Standard doc templates with Definition of Done checklists (front-matter complete, claims cited, etc.). :contentReference[oaicite:18]{index=18}
- [ ] “Living docs” workflow: docs updated with code changes; periodic doc audits. :contentReference[oaicite:19]{index=19}

**Exit criteria**
- CI blocks merges that violate policy gates.
- Templates exist for: roadmap, runbook, data intake SOP, domain module spec, Story Node spec.
- Doc + schema changes are reviewed like code.

---

### M1 — Evidence ingestion v1: the gate that creates trust 📥
**Goal:** Ingest data + docs in a way that is deterministic, governed, and provenance-complete.

**Key deliverables**
- [ ] Implement ingestion gate steps (checksum, schema sanity, CRS/bounds checks, license presence, sensitivity classification, provenance stub). :contentReference[oaicite:20]{index=20}
- [ ] Deterministic ETL runs (idempotent jobs, stable outputs for same inputs). :contentReference[oaicite:21]{index=21}
- [ ] STAC/DCAT/PROV validation in CI (metadata-as-code). :contentReference[oaicite:22]{index=22}
- [ ] PROV is mandatory for publishing/merging governed data. :contentReference[oaicite:23]{index=23}
- [ ] Document ingestion foundation (OCR/NLP extraction + entity linking) with human-in-the-loop review (“AI steward”). :contentReference[oaicite:24]{index=24}

**Exit criteria**
- A dataset + its STAC/DCAT/PROV can be added end-to-end via PR, passing CI.
- Every ingested artifact can be traced by checksum and provenance record.

---

### M2 — Evidence graph v1: Neo4j as the “connective tissue” 🕸️
**Goal:** Build a graph that mirrors the evidence catalogs, not a hand-wavy knowledge base.

**Key deliverables**
- [ ] Neo4j graph schema + ingest from STAC/DCAT/PROV (“no mystery nodes”). :contentReference[oaicite:25]{index=25}
- [ ] Entity resolution + stable IDs across nodes (doc/feature/dataset/source). :contentReference[oaicite:26]{index=26}
- [ ] Search index for discovery (e.g., full-text + embeddings) integrated with graph retrieval. :contentReference[oaicite:27]{index=27}
- [ ] Provenance-aware traversal helpers (e.g., “show chain of evidence”). :contentReference[oaicite:28]{index=28}

**Exit criteria**
- Given a map layer or story node, the system can show its source datasets, license, and PROV lineage.

---

### M3 — Map + Timeline MVP: “the product becomes real” 🗺️⏳
**Goal:** Deliver the core interaction: **Map + Time + Layers + Search**.

**UI scope areas (from UI overview)**
- Map canvas, timeline slider, layer panel, search, story mode, focus mode hooks. :contentReference[oaicite:29]{index=29}

**Key deliverables**
- [ ] Implement Map Timeline slider MVP (backend date filtering + MapLibre timeline sync). :contentReference[oaicite:30]{index=30}
- [ ] Layer registry + render pipeline (vector/raster + metadata-driven). :contentReference[oaicite:31]{index=31}
- [ ] Basic story viewing (Story Nodes read-only), anchored to place/time/layers. :contentReference[oaicite:32]{index=32}
- [ ] Mobile/responsive baseline (phone-first map interactions where possible). :contentReference[oaicite:33]{index=33}

**Exit criteria**
- A user can select a time range and see map layers update, and open a story node tied to that time/place.

---

### M4 — Story Nodes v1: narrative as a first-class, governed artifact 🧾
**Goal:** Make narratives trustworthy: stories are versioned, cited, and traceable to evidence.

**Key deliverables**
- [ ] Story Node schema + template + DoD checklist (front-matter, citations, sensitivity labels). :contentReference[oaicite:34]{index=34}
- [ ] UI: Story mode reader with citations panel + provenance panel. :contentReference[oaicite:35]{index=35}
- [ ] Example “community story” showing citizen contributions (with governance). :contentReference[oaicite:36]{index=36}

**Exit criteria**
- A story node can be validated in CI and displayed in the UI with evidence links.

---

### M5 — Focus Mode v1: safe AI with citations + audit 🔎🤖
**Goal:** AI that accelerates discovery **without making things up**.

**Key deliverables**
- [ ] Focus Mode pipeline: parse → retrieve → LLM → governance_check → answer (with citations). :contentReference[oaicite:37]{index=37}
- [ ] Hard requirement: every answer cites sources; refusal mode if not derivable. :contentReference[oaicite:38]{index=38}
- [ ] XAI / Audit panel showing retrieved evidence and reasoning trace. :contentReference[oaicite:39]{index=39}
- [ ] Policy enforcement for AI (OPA-style rules + tests for citations and sensitive outputs). :contentReference[oaicite:40]{index=40}

**Exit criteria**
- Any AI-generated claim links to a source artifact or explicitly flags uncertainty/refusal.

---

### M6 — Performance + packaging + offline 📦⚡
**Goal:** Make KFM fast at scale, and usable in low-connectivity contexts.

**Key deliverables**
- [ ] Standard “GeoParquet + PMTiles” packaging pattern with STAC/DCAT records. :contentReference[oaicite:41]{index=41}
- [ ] Offline Pack feature: download region/time bundle for offline usage. :contentReference[oaicite:42]{index=42}
- [ ] Raster pipeline optimization: COG + pre-tiling + cached tiles. :contentReference[oaicite:43]{index=43}

**Exit criteria**
- “Offline Pack” can be generated and used to load a map+timeline session without internet.

---

### M7 — Federation + multi-region 🌐
**Goal:** Enable a federation of regions (Kansas-first, but not Kansas-only).

**Key deliverables**
- [ ] Shared schemas + identifiers + ontologies across regions. :contentReference[oaicite:44]{index=44}
- [ ] Federation mechanism: central hub harvests DCAT; state-prefix IDs; cross-region PROV references. :contentReference[oaicite:45]{index=45}
- [ ] Configurable UI + minimal Kansas hardcoding (“federation-ready”). :contentReference[oaicite:46]{index=46}

**Exit criteria**
- Two catalogs (Kansas + another region) can be discovered and searched in a unified UI.

---

### M8 — 3D / AR / 4D digital twin (research track) 🛰️🕶️
**Goal:** Explore immersive “time-travel” mapping and 4D narratives (place + time + change).

**Why this exists**
- Digital twins are trending toward **4D**: time-aware experiences capturing change over time. :contentReference[oaicite:47]{index=47}

**Key deliverables**
- [ ] 3D toggle and/or AR overlays consuming the same evidence APIs. :contentReference[oaicite:48]{index=48}
- [ ] Prototype “time travel” narrative: Story Nodes + timeline + imagery overlays. :contentReference[oaicite:49]{index=49}
- [ ] Research protocols documented using scientific method templates (reproducible experiments). :contentReference[oaicite:50]{index=50}

**Exit criteria**
- A demo proves the interaction model, with documented experiment protocol + results.

---

## 🧩 Epic backlog

<details>
<summary><strong>📥 Data intake & evidence catalogs</strong></summary>

- [ ] STAC collections for every geospatial dataset; DCAT for discoverability; PROV for lineage. :contentReference[oaicite:51]{index=51}
- [ ] Bulk ingestion UI (drag/drop) with OCR + entity extraction + link suggestions. :contentReference[oaicite:52]{index=52}
- [ ] “No mystery nodes” enforcement: every graph entity must tie to a governed artifact. :contentReference[oaicite:53]{index=53}

</details>

<details>
<summary><strong>🕸️ Graph, search, and provenance</strong></summary>

- [ ] Neo4j schema module system (domain expansions via governed ontologies). :contentReference[oaicite:54]{index=54}
- [ ] Provenance explorer UI: evidence chain visualization. :contentReference[oaicite:55]{index=55}
- [ ] Search improvements: hybrid full-text + embedding + graph neighborhoods. :contentReference[oaicite:56]{index=56}

</details>

<details>
<summary><strong>🗺️ UI: Map, timeline, story</strong></summary>

- [ ] Map Timeline slider MVP shipped. :contentReference[oaicite:57]{index=57}
- [ ] Story Node authoring workflow (template + UI editor). :contentReference[oaicite:58]{index=58}
- [ ] Accessibility + keyboard navigation + clear layering patterns (UI “musts”). :contentReference[oaicite:59]{index=59}

</details>

<details>
<summary><strong>🤖 AI Focus Mode</strong></summary>

- [ ] Governance check layer required for all AI outputs. :contentReference[oaicite:60]{index=60}
- [ ] “Refuse if unsourced” guardrail. :contentReference[oaicite:61]{index=61}
- [ ] Audit panel standard (evidence used, provenance, uncertainty). :contentReference[oaicite:62]{index=62}

</details>

<details>
<summary><strong>📦 Performance, packaging, offline</strong></summary>

- [ ] Standard packaging: GeoParquet + PMTiles + STAC/DCAT records. :contentReference[oaicite:63]{index=63}
- [ ] Offline Pack bundler + verifier. :contentReference[oaicite:64]{index=64}
- [ ] Tile caching + vector/raster performance baseline (WebGL where useful). :contentReference[oaicite:65]{index=65}

</details>

<details>
<summary><strong>🔒 Security, privacy, ethics</strong></summary>

- [ ] Sensitivity + CARE labels in front matter; review workflows for restricted data. :contentReference[oaicite:66]{index=66}
- [ ] Query auditing + inference control where applicable. :contentReference[oaicite:67]{index=67}

</details>

<details>
<summary><strong>🌐 Federation + community</strong></summary>

- [ ] Multi-region federation patterns (ID prefixes, harvested catalogs). :contentReference[oaicite:68]{index=68}
- [ ] Governance board + glossary + community contributor pathways. :contentReference[oaicite:69]{index=69}

</details>

---

## ✅ Definition of Done

> We treat documentation + metadata like code: **front-matter valid, claims cited, policy gates pass**. :contentReference[oaicite:70]{index=70}:contentReference[oaicite:71]{index=71}

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

> These are the roadmap’s **inputs**. If a file is a **PDF Portfolio**, we should extract/unpack it into individually indexable docs (roadmap item). :contentReference[oaicite:72]{index=72}

### Core KFM system docs
- 🧠 **AI System Overview** — Focus Mode, citations, auditability, governance checks. :contentReference[oaicite:73]{index=73}
- 🧩 **Comprehensive Architecture, Features, and Design** — platform design, policy gates, federation, UX direction. :contentReference[oaicite:74]{index=74}
- 🗺️ **Comprehensive UI System Overview** — UI module map (map/timeline/layers/story/focus). :contentReference[oaicite:75]{index=75}
- 📥 **Data Intake – Technical & Design Guide** — canonical pipeline ordering, ingestion gates, evidence triplet, PROV requirements. :contentReference[oaicite:76]{index=76}
- 🧱 **Comprehensive Technical Documentation** — end-to-end platform concepts (knowledge network, remote sensing, performance, governance). :contentReference[oaicite:77]{index=77}
- 🌟 **Latest Ideas & Future Proposals** — offline packs, tiling strategy (GeoParquet/PMTiles), timeline MVP ideas. :contentReference[oaicite:78]{index=78}
- 💡 **Innovative Concepts to Evolve KFM** — digital twin / 4D direction, immersive futures. :contentReference[oaicite:79]{index=79} :contentReference[oaicite:80]{index=80}
- 🧭 **Open-Source Geospatial Historical Mapping Hub Design** — ingestion-to-UI design including COG/tiles/OCR and Map UI approach. :contentReference[oaicite:81]{index=81}
- 🧾 **MARKDOWN_GUIDE v13** — contract-first & deterministic documentation + pipeline rules. :contentReference[oaicite:82]{index=82}

### Research + reference packs (to unpack/index)
- 🤖 **AI Concepts & more (PDF Portfolio)** — AI learning/reference pack (needs extraction). :contentReference[oaicite:83]{index=83}
- 🌍 **Maps / GoogleMaps / VirtualWorlds / WebGL (PDF Portfolio)** — mapping + virtual worlds reference pack (needs extraction). :contentReference[oaicite:84]{index=84}
- 🧰 **Various programming languages & resources (PDF Portfolio)** — language/tool reference pack (needs extraction). :contentReference[oaicite:85]{index=85}
- 🗄️ **Data Management / Theories / Architectures / Bayesian (PDF Portfolio)** — data architecture reference pack (needs extraction). :contentReference[oaicite:86]{index=86}

### Embedded / extracted books and guides already indexed
- 📘 **Python Geospatial Analysis Cookbook** — Folium/Leaflet/WebGL/tiles patterns and recipes. :contentReference[oaicite:87]{index=87}
- 🔐 **Data Mining Concepts & Applications** — inference control, query auditing, privacy techniques. :contentReference[oaicite:88]{index=88}
- ✍️ **Comprehensive Markdown Guide** — templates, governance front-matter, DoD checklists. :contentReference[oaicite:89]{index=89}
- 🧪 **Scientific Method / Research / Master Coder Protocol** — living documentation + reproducible experiment practices. :contentReference[oaicite:90]{index=90}

---

## 📌 One last rule (to keep us honest)

If it can’t pass the gates (contracts ✅, provenance ✅, sensitivity ✅, citations ✅), **it doesn’t ship**. :contentReference[oaicite:91]{index=91}
