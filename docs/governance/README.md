---
title: "KFM Governance — README"
path: "docs/governance/README.md"
version: "v1.1.0"
last_updated: "2026-01-12"
status: "draft"
doc_kind: "README"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:governance:readme:v1.1.0"
semantic_document_id: "kfm-governance-readme-v1.1.0"
event_source_id: "ledger:kfm:doc:governance:readme:v1.1.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:d3934b6937763c14acaf7b68e795a27c2f22aa58f678b3c3af3ebf24358e2b87"
---

# KFM Governance — README 🧱🌾

![Status](https://img.shields.io/badge/status-draft-yellow)
![License](https://img.shields.io/badge/license-CC--BY--4.0-blue)
![FAIR%2BCARE](https://img.shields.io/badge/FAIR%2BCARE-governed-brightgreen)
![Jurisdiction](https://img.shields.io/badge/jurisdiction-US--KS-lightgrey)
![KFM--MDP](https://img.shields.io/badge/KFM--MDP-v11.2.6-purple)

> [!IMPORTANT]
> **This README is an index + process guide.** Canonical policy text lives in:
> - `docs/governance/ROOT_GOVERNANCE.md`
> - `docs/governance/ETHICS.md`
> - `docs/governance/SOVEREIGNTY.md`
>
> Keep this file **link-heavy** and **definition-light**. (No new policy definitions here.)

## 🔗 Quick links

- 🧭 Master Guide (latest): `docs/MASTER_GUIDE_v13.md`:contentReference[oaicite:0]{index=0}
- 🧱 Root Governance (canonical): `docs/governance/ROOT_GOVERNANCE.md`:contentReference[oaicite:1]{index=1}
- ⚖️ Ethics: `docs/governance/ETHICS.md`:contentReference[oaicite:2]{index=2}
- 🪶 Sovereignty: `docs/governance/SOVEREIGNTY.md`:contentReference[oaicite:3]{index=3}
- 🧩 Templates: `docs/templates/`:contentReference[oaicite:4]{index=4}
- 🏗️ Architecture docs: `docs/architecture/`:contentReference[oaicite:5]{index=5}
- 🔐 Security docs: `docs/security/` + `SECURITY.md`
- 🧪 Methods / SOPs (MCP): `mcp/`:contentReference[oaicite:7]{index=7}

---

## 📘 Overview

### Purpose

This directory is the **canonical home for project-wide governance** in KFM. It exists to:

- define **FAIR+CARE-aligned** governance rules that apply across the pipeline,
- document **review gates** and change-control expectations for sensitive or high-impact modifications,
- ensure KFM stays **architecture-synced** (no bypassing contracts, provenance, or access policy),
- provide a single starting point for contributors who need to understand **what requires governance review** and how approvals are tracked.

KFM’s Master Guide describes the platform as a governed “living atlas” where catalogs (STAC/DCAT/PROV) precede the graph, APIs, UI, and narrative—so every claim can trace to evidence.:contentReference[oaicite:8]{index=8}:contentReference[oaicite:9]{index=9}

### Scope

| In Scope ✅ | Out of Scope ❌ |
|---|---|
| Project-wide governance policies and their change-control expectations | Domain-specific governance (belongs under `data/<domain>/governance/`) |
| Ethics and sovereignty policy references and review triggers | Writing new policy text without an approved governance process |
| Review gates and exception logging mechanisms | Implementing ETL/API/UI code (belongs under `src/**` or `web/**`) |
| Classification/sensitivity invariants that must hold across the pipeline | Legal advice or jurisdiction-specific requirements beyond what is explicitly governed in-repo |

### Audience

- **Primary:** maintainers, governance reviewers/owners, DataOps, security reviewers
- **Secondary:** contributors adding/modifying datasets, schemas, graph mappings, APIs, UI layers, or Story Nodes

### Definitions (KFM-aligned)

- Link: `docs/glossary.md`

Core terms (non-exhaustive):

- **Catalogs**: STAC (assets), DCAT (dataset/distribution discovery), PROV (lineage).:contentReference[oaicite:11]{index=11}
- **Contract artifact**: machine-validated schema/spec defining an interface (JSON Schema, OpenAPI, GraphQL SDL, UI registry, etc.).:contentReference[oaicite:12]{index=12}
- **Evidence artifact**: derived data product registered in catalogs (STAC/DCAT) with PROV lineage **before** being used in UI or narrative.:contentReference[oaicite:13]{index=13}
- **Story Node**: governed narrative artifact; machine-ingestible and provenance-linked (claims/media reference sources in catalogs).:contentReference[oaicite:14]{index=14}
- **Focus Mode**: interactive experience that presents Story Nodes in context using provenance-linked content; AI suggestions must be labeled and constrained by evidence.:contentReference[oaicite:15]{index=15}
- **Governance gate**: review + CI validation step required before merge/release.
- **Sensitivity / classification**: governance labels that control redaction/generalization and distribution. (Canonical taxonomies live in `ROOT_GOVERNANCE.md`.)

### Key artifacts (what this README points to)

| Artifact | Path / Identifier | Expected owner | Notes |
|---|---|---|---|
| This README | `docs/governance/README.md` | Repo maintainers | Index + process guidance |
| Root governance policy | `docs/governance/ROOT_GOVERNANCE.md` | Governance owners | Canonical labels, approvals, exceptions |
| Ethics policy | `docs/governance/ETHICS.md` | Governance owners | AI/ML transparency + bias + disclosure requirements |
| Sovereignty policy | `docs/governance/SOVEREIGNTY.md` | Governance owners | Indigenous data sovereignty + culturally sensitive handling |
| Master Guide v13 (draft) | `docs/MASTER_GUIDE_v13.md` | KFM maintainers | Canonical pipeline ordering + invariants:contentReference[oaicite:16]{index=16} |
| Templates | `docs/templates/` | KFM maintainers | Required doc structures + front-matter:contentReference[oaicite:17]{index=17} |
| Architecture blueprints | `docs/architecture/` | KFM maintainers | v13 blueprint + future stages:contentReference[oaicite:18]{index=18} |
| Methods / SOPs (MCP) | `mcp/` | Maintainers + reviewers | Internal wiki: procedures, model cards, experiments:contentReference[oaicite:19]{index=19}:contentReference[oaicite:20]{index=20} |
| Security guidance | `docs/security/` + `SECURITY.md` | Security reviewers | Threat model/runbooks recommended |
| CI policy pack (planned) | `tools/validation/policy/` | Governance owners + DevOps | OPA/Rego + Conftest “policy gate” proposal:contentReference[oaicite:22]{index=22} |

### Definition of done (for this document)

- [ ] Front-matter complete + valid (required keys present)
- [ ] Links resolve to canonical governance documents (no dead pointers)
- [ ] Directory layout reflects **current repo** + **v13 target** without contradiction:contentReference[oaicite:23]{index=23}
- [ ] Review-gate guidance is consistent with the canonical pipeline ordering (no “skip the API boundary”):contentReference[oaicite:24]{index=24}
- [ ] Describes how governance affects Story Nodes / Focus Mode (provenance-linked narrative rule)
- [ ] CI expectations cover minimum gates + policy enforcement hooks (where adopted)
- [ ] Footer refs present and point to canonical docs (do not remove)

---

## 🗂️ Directory Layout

> [!NOTE]
> KFM has both a **current/observed** layout (v12-era folders like `api/`, `pipelines/`) and a **v13 target** layout that consolidates subsystems into canonical homes (e.g., `src/server/`, `src/pipelines/`, `schemas/`, `releases/`).:contentReference[oaicite:25]{index=25}:contentReference[oaicite:26]{index=26}

### Current/observed repo anchors (as documented)

- `api/` — back-end API service (FastAPI):contentReference[oaicite:27]{index=27}
- `web/` — front-end UI (React/MapLibre/Cesium):contentReference[oaicite:28]{index=28}
- `data/` — datasets + catalogs (STAC/DCAT/PROV outputs):contentReference[oaicite:29]{index=29}
- `pipelines/` — ingestion + processing workflows
- `tools/` — validation, utilities, QA scripts
- `notebooks/` — exploratory analysis + prototyping
- `mcp/` — Methods, Controls & Processes (SOPs, ethics guidelines, runbooks):contentReference[oaicite:33]{index=33}
- `docs/` — canonical documentation with subfolders including `architecture/`, `specs/`, `security/`, `standards/`, `governance/`

### v13 target layout (canonical homes per subsystem)

Per the Master Guide v13 draft, the repo consolidates into one canonical home per subsystem and adds missing roots like `schemas/`, `releases/`, `data/prov/`, and `data/catalog/dcat/`.:contentReference[oaicite:35]{index=35}:contentReference[oaicite:36]{index=36}

#### Expected v13 file tree (illustrative)

~~~text
📦 repo-root/
├── 📁 data/                          # raw/work/processed + catalog outputs
│   ├── 📁 raw/
│   ├── 📁 work/
│   ├── 📁 processed/
│   ├── 📁 catalog/
│   │   ├── 📁 stac/
│   │   └── 📁 dcat/
│   └── 📁 prov/
├── 📁 docs/
│   ├── 📁 governance/                # 👈 you are here
│   ├── 📁 templates/
│   ├── 📁 architecture/
│   ├── 📁 specs/
│   ├── 📁 security/
│   ├── 📁 standards/
│   └── 📁 reports/
│       └── 📁 story_nodes/
│           ├── 📁 draft/
│           └── 📁 published/
├── 📁 schemas/                       # JSON Schemas (STAC/DCAT/PROV/story/ui/telemetry)
├── 📁 src/
│   ├── 📁 pipelines/                 # ETL jobs
│   ├── 📁 graph/                     # graph build/ingest
│   └── 📁 server/                    # API boundary + contracts
├── 📁 web/                           # UI
├── 📁 mcp/                           # methods + experiments + model cards
└── 📁 tools/                         # validation + automation
~~~

---

## 🧭 Context

### Background: why governance exists

KFM is designed as a governed geospatial + historical knowledge system that:

- ingests heterogeneous sources,
- publishes metadata catalogs (STAC/DCAT/PROV),
- builds a Neo4j knowledge graph,
- serves evidence via contracted APIs into a map-and-narrative UI.:contentReference[oaicite:37]{index=37}

The architecture emphasizes modular layers (API, UI, pipelines, knowledge graph) and explicit contracts between them (clean architecture / separation of concerns).:contentReference[oaicite:38]{index=38}

### The canonical pipeline (non-negotiable ordering)

> **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**:contentReference[oaicite:39]{index=39}

This ordering is the core governance constraint: **no stage may bypass a prior stage’s contracts or outputs**.:contentReference[oaicite:40]{index=40}

### Constraints / invariants (must not regress)

- ✅ **API boundary is mandatory:** UI must not read Neo4j directly; all access flows through contracted APIs (authorization + redaction).:contentReference[oaicite:41]{index=41}
- ✅ **Contract-first:** schemas + API specs are first-class artifacts; implementations must honor them.:contentReference[oaicite:42]{index=42}:contentReference[oaicite:43]{index=43}
- ✅ **Evidence-first:** catalogs + PROV lineage exist **before** narrative interpretation is published.:contentReference[oaicite:44]{index=44}
- ✅ **No unsourced narrative:** Story Nodes must be provenance-linked (claims/media reference cataloged sources).:contentReference[oaicite:45]{index=45}
- ✅ **Restricted-location protection:** if data can reveal protected locations, redaction/generalization is required and must be enforceable at API/UI layers (see sovereignty policy).:contentReference[oaicite:46]{index=46}
- ✅ **Focus Mode is advisory-only:** it should summarize/interpret KFM evidence with citations and avoid speculation beyond available data.:contentReference[oaicite:47]{index=47}

---

## 🧑‍⚖️ Governance model (who reviews what)

> [!TIP]
> The roadmap calls out “governance maturity” work: SOPs, contributor guide expansion, and potentially an advisory board/steering committee as KFM grows and federates with other states/projects.:contentReference[oaicite:48]{index=48}

### Minimum reviewer roles (recommended)

| Role | Reviews | Typical triggers |
|---|---|---|
| **Maintainers** | All PRs (baseline) | Any change |
| **Ethics reviewers** | AI/ML, narrative generation, bias/disclosure | Focus Mode changes; AI summaries; model outputs used in narrative:contentReference[oaicite:49]{index=49} |
| **Sovereignty reviewers** | Indigenous/culturally sensitive data + restricted locations | Datasets affecting sensitive areas; precision changes; new story content:contentReference[oaicite:50]{index=50} |
| **Security reviewers** | authN/authZ, data exposure, supply chain | New endpoints; downloads; CI signing/attestations:contentReference[oaicite:51]{index=51} |
| **Domain stewards** | domain-specific ETL & interpretations | New domain modules; schema mapping changes |

> If a formal RACI table exists, link it here (preferred: `docs/governance/RACI.md`). If not, add it via governance process.

---

## 🚦 Review gates & governance triggers

### Governance decision flow (PR → gates → review)

~~~mermaid
flowchart TD
  A["Change proposed (PR)"] --> B["Run CI gates (contracts + policy checks)"]
  B --> C{"Governance trigger hit?"}
  C -- "No" --> D["Standard review + merge (maintainers)"]
  C -- "Yes" --> E["Request governance review (ethics / sovereignty / security)"]
  E --> F["Address findings + record approvals"]
  F --> D
  D --> G["Release / publish (if applicable)"]
  G --> H["Audit trail (PROV + telemetry)"]
~~~

### Trigger examples (guidance)

These are *examples*; the canonical list should live in a dedicated gate registry (recommended: `docs/governance/REVIEW_GATES.md`).

- **Sensitive/culturally protected datasets** → sovereignty review.:contentReference[oaicite:52]{index=52}
- **Any AI/ML component generating summaries/narrative** → ethics review (transparency + bias + disclosure).:contentReference[oaicite:53]{index=53}
- **AuthN/AuthZ, new public endpoints, downloads** → security review.:contentReference[oaicite:54]{index=54}
- **Schema/contract changes** (`schemas/**`, API specs) → contract gate + versioning review.:contentReference[oaicite:55]{index=55}
- **Story Node publication** (`docs/reports/story_nodes/published/**`) → narrative review + evidence check.:contentReference[oaicite:56]{index=56}:contentReference[oaicite:57]{index=57}

### Recording approvals (minimum)

- Approvals are recorded in **PR review history** at minimum.
- If/when a governed registry exists (e.g., `docs/governance/approvals.yaml`), link it here.

---

## 🧾 Exceptions & waivers (time-bounded)

> [!CAUTION]
> **Guidance:** treat exceptions as **rare**, **explicit**, and **expiring**. Canonical exception rules (if any) belong in `ROOT_GOVERNANCE.md`.

Recommended (if adopted):

- Registry: `docs/governance/exceptions.yaml`
- Each entry includes: scope, reason, approver(s), expiry, mitigations, and follow-up issue.

---

## ⚙️ Validation & CI/CD

### Baseline CI gates (minimum expectations)

KFM’s roadmap proposes combining fast automated checks with “lane” validators, then promoting via signed PRs to keep changes reproducible and auditable.:contentReference[oaicite:58]{index=58}

Minimum gates (baseline):

- [ ] **Markdown protocol validation** (front-matter + link integrity + templates)
- [ ] **Contract validation** (JSON Schemas + API specs):contentReference[oaicite:59]{index=59}
- [ ] **Catalog validation** (STAC/DCAT/PROV shape + cross-links):contentReference[oaicite:60]{index=60}
- [ ] **Graph integrity checks** (constraints + ingest invariants)
- [ ] **Policy gate** (OPA/Rego + Conftest) for governance rules (planned):contentReference[oaicite:61]{index=61}
- [ ] **Security scanning** (secrets, dependency/SBOM, basic vuln scans)
- [ ] **Sovereignty scanning** (restricted precision / sensitive-area heuristics, if applicable)

### Detect → Validate → Promote (recommended workflow)

The roadmap describes a pipeline that detects changes (checksums/events), validates with policy + lane validators, then opens a **Sigstore-signed PR** for promotion, emitting OpenLineage events for auditability.:contentReference[oaicite:62]{index=62}

> [!NOTE]
> **Automation is allowed, but governance still applies.** KFM’s roadmap describes an agent framework (Watcher → Planner → Executor) that proposes changes and opens PRs, but keeps a **kill-switch**, avoids scope creep, and does **not** replace human review/approval.:contentReference[oaicite:63]{index=63}

~~~mermaid
flowchart LR
  A["Detect changes (ETags / repo events)"] --> B["Validate (schema + policy + lanes)"]
  B --> C{"All checks pass?"}
  C -- "No" --> D["Fail + report (checks + artifacts)"]
  C -- "Yes" --> E["Open PR (promotion)"]
  E --> F["Sign PR/commit (Sigstore)"]
  F --> G["Emit OpenLineage + store audit artifacts"]
~~~

### DevOps provenance (PR → PROV)

KFM proposes mapping GitHub PR events into W3C PROV-O (PR as Activity, commits as Entities, contributors/reviewers as Agents) so development history is queryable lineage in Neo4j.:contentReference[oaicite:64]{index=64}

### Telemetry signals (if applicable)

The roadmap proposes treating telemetry as QA output, including health checks for OpenTelemetry traces and energy/carbon reporting.:contentReference[oaicite:65]{index=65}

| Signal | Source | Where recorded |
|---|---|---|
| CI gate results | GitHub Actions | CI logs + artifacts |
| Policy gate results | Conftest/OPA | CI artifacts + PR checks |
| Lineage events | OpenLineage | Observability server / logs:contentReference[oaicite:66]{index=66} |
| Redaction notices | UI/Focus Mode | Telemetry event(s) like `focus_mode_redaction_notice_shown`:contentReference[oaicite:67]{index=67} |
| Energy/carbon | CI telemetry | CI artifacts / observability:contentReference[oaicite:68]{index=68} |

### Reproduction (placeholders — wire to repo scripts)

~~~bash
# Markdown protocol checks
# e.g., tools/validation/markdown_lint.py  (TBD)

# Contract checks (schemas + API)
# e.g., tools/validation/schema_check.py   (TBD)

# Catalog checks (STAC/DCAT/PROV)
# e.g., tools/validation/catalog_qa/       (TBD)

# Policy gate (OPA/Conftest)
# conftest test . -p tools/validation/policy  (if adopted)

# Lane validators (spatial QA, graph checks)
# e.g., tools/validation/spatial_lane.py   (TBD)
# e.g., tools/validation/graph_lane.py     (TBD)
~~~

---

## 🧠 Story Nodes & Focus Mode integration

### Where Story Nodes live (v13)

- Drafts: `docs/reports/story_nodes/draft/`
- Published: `docs/reports/story_nodes/published/`:contentReference[oaicite:69]{index=69}:contentReference[oaicite:70]{index=70}

### What a Story Node is (implementation note)

KFM’s documentation describes Story Nodes as a narrative sequence: each node has narrative text (often with images/citations) plus a map-view configuration; the UI orchestrates nodes into a guided “living atlas” experience.:contentReference[oaicite:71]{index=71}

### Provenance-linked narrative rule (hard requirement)

- Story Nodes must ensure every factual claim can trace to a dataset/record/asset identifier in catalogs.
- If a Story Node depends on restricted inputs, it must inherit the appropriate classification and must not be published as open.

### Focus Mode expectations

- Focus Mode should surface **provenance-linked context only** (narrative + citations + governance flags).:contentReference[oaicite:72]{index=72}
- If data is withheld/generalized (restricted precision), emit an audit/telemetry signal (example: `focus_mode_redaction_notice_shown`).:contentReference[oaicite:73]{index=73}
- Focus Mode is designed to interpret KFM content with citations and avoid speculation beyond what KFM contains.:contentReference[oaicite:74]{index=74}

---

## 📦 Data & metadata governance

### Standards & formats (project posture)

KFM emphasizes open standards: vector outputs as **GeoJSON**, raster outputs as **Cloud-Optimized GeoTIFF (COG)**, with preference for **WGS84**, plus STAC records, PROV lineage, and DCAT feeds for discovery.:contentReference[oaicite:75]{index=75}

### API posture (for governance)

The audit describes an API-first design with REST documented by OpenAPI and a GraphQL endpoint for flexible retrieval—governance must ensure these interfaces enforce classification/redaction rules.:contentReference[oaicite:76]{index=76}

### Required metadata fields (governed docs)

All governed docs (including governance docs) should include in front-matter:

- identifiers: `doc_uuid`, `semantic_document_id`, `event_source_id`, `commit_sha`
- governance labels: `sensitivity`, `classification`, `jurisdiction`, `fair_category`, `care_label`
- references: `governance_ref`, `ethics_ref`, `sovereignty_policy`
- AI constraints: `ai_transform_permissions`, `ai_transform_prohibited`
- integrity fields: `doc_integrity_checksum`

### Evidence artifacts (models, analyses, derived products)

When contributing models/analytics outputs, treat outputs as **evidence artifacts**:

- capture inputs, parameters, code version, and outputs in PROV,
- register outputs in catalogs (STAC/DCAT),
- only then allow narratives/UI to cite them.:contentReference[oaicite:77]{index=77}:contentReference[oaicite:78]{index=78}

---

## 🧬 Ontology & knowledge graph governance

KFM’s semantic layer is implemented as a **Neo4j** knowledge graph that links people, places, events, and datasets, and is designed to align with standard ontologies (e.g., **CIDOC-CRM** for history, **GeoSPARQL** for geospatial, **OWL-Time** for temporal).:contentReference[oaicite:79]{index=79}

Governance expectations:

- Ontology mappings and graph constraints are treated as **contract artifacts** (schema-controlled, versioned).:contentReference[oaicite:80]{index=80}
- Changes to ontology bindings, entity resolution rules, or graph ingest constraints trigger **governance review** (risk: downstream narrative/API behavior changes).
- Graph analytics outputs (clusters, centrality, anomaly flags) are treated as **evidence artifacts** and must be cataloged + provenance-linked before being surfaced in UI or Story Nodes.:contentReference[oaicite:81]{index=81}:contentReference[oaicite:82]{index=82}

## 🔐 Security & supply-chain governance (high level)

- Follow `SECURITY.md` + `docs/security/` for reporting/handling vulnerabilities.
- The roadmap proposes supply-chain rigor (SBOMs + SLSA-style attestations) and Sigstore signing for automated PRs/releases.:contentReference[oaicite:84]{index=84}:contentReference[oaicite:85]{index=85}
- No secrets/PII in repo. Never commit credentials (even in examples).

---

## 📚 Reference library governance (project files)

> [!NOTE]
> KFM’s documentation explicitly distinguishes the project’s own MIT-licensed code/docs from **third‑party reference PDFs**, which retain their original licenses and are not automatically “MIT.”

Recommended handling:

- Store third-party references under a clear root (e.g., `docs/library/` or `docs/references/`)
- Add a lightweight manifest (e.g., `docs/library/README.md`) capturing: title, source, license/terms, and why it’s included
- Prefer linking to official sources when redistribution is not permitted

<details>
<summary>📖 Included reference files (as currently present in the project workspace)</summary>

### 🛰️ Geospatial, remote sensing, cartography

- `python-geospatial-analysis-cookbook.pdf`
- `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`
- `making-maps-a-visual-guide-to-map-design-for-gis.pdf`
- `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf`
- `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf`

### 🗺️ Web mapping & visualization

- `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`
- `responsive-web-design-with-html5-and-css3.pdf`

### 📊 Statistics, data science, ML

- `regression-analysis-with-python.pdf`
- `Regression analysis using Python - slides-linear-regression.pdf`
- `think-bayes-bayesian-statistics-in-python.pdf`
- `Understanding Statistics & Experimental Design.pdf`
- `graphical-data-analysis-with-r.pdf`
- `Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf`

### 🧠 Modeling, simulation, optimization, graphs

- `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`
- `Generalized Topology Optimization for Structural Design.pdf`
- `Spectral Geometry of Graphs.pdf`
- `Scalable Data Management for Future Hardware.pdf`
- `Data Spaces.pdf`
- `Principles of Biological Autonomy - book_9780262381833.pdf`

### ⚖️ Ethics, law, human-centered tech

- `Introduction to Digital Humanism.pdf`
- `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf`

### 🛡️ Security & systems

- `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`
- `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf`
- `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf`
- `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf`

### 🧰 Programming compendiums (collections)

- `A programming Books.pdf`
- `B-C programming Books.pdf`
- `D-E programming Books.pdf`
- `F-H programming Books.pdf`
- `I-L programming Books.pdf`
- `M-N programming Books.pdf`
- `O-R programming Books.pdf`
- `S-T programming Books.pdf`
- `U-X programming Books.pdf`

### 🧾 KFM core docs (project-authored)

- `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx`
- `🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx`
- `Audit of the Kansas Frontier Matrix (KFM) Repository.pdf`
- `Kansas Frontier Matrix Design Document.pdf`
- `Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf`
- `MARKDOWN_GUIDE_v13.md.gdoc`
- `Comprehensive Markdown Guide - KFM_MARKDOWN_GUIDE_v13.docx`
- `Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx`

</details>

---

## 🕰️ Version history

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.1.0 | 2026-01-12 | Aligned README with Master Guide v13 draft (canonical homes, story_nodes workflow); confirmed repo anchors (mcp/docs/security/standards); expanded CI gates + policy-pack roadmap references | TBD |
| v1.0.0 | 2025-12-27 | Initial governance README scaffold | TBD |

---

## Footer refs (do not remove)

- Master Guide: `docs/MASTER_GUIDE_v13.md`:contentReference[oaicite:87]{index=87}
- Templates: `docs/templates/`:contentReference[oaicite:88]{index=88}
- Architecture: `docs/architecture/`:contentReference[oaicite:89]{index=89}
- Governance: `docs/governance/ROOT_GOVERNANCE.md`:contentReference[oaicite:90]{index=90}
- Ethics: `docs/governance/ETHICS.md`:contentReference[oaicite:91]{index=91}
- Sovereignty: `docs/governance/SOVEREIGNTY.md`:contentReference[oaicite:92]{index=92}
