---
title: "docs/data — Data Documentation & Catalog Mapping Index"
path: "docs/data/README.md"
version: "v1.1.0"
last_updated: "2026-01-19"
status: "active"
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

doc_uuid: "urn:kfm:doc:docs:data:readme:v1.1.0"
semantic_document_id: "kfm-docs-data-readme-v1.1.0"
event_source_id: "ledger:kfm:doc:docs:data:readme:v1.1.0"
commit_sha: "<ci:git-sha>"
supersedes:
  - "urn:kfm:doc:docs:data:readme:v1.0.0"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

[![Doc](https://img.shields.io/badge/docs-data%2FREADME.md-blue)](#docsdata--data-documentation--catalog-mapping-index)
[![Status](https://img.shields.io/badge/status-active-success)](#)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-enforced-brightgreen)](#-faircare--governance)
[![Catalog](https://img.shields.io/badge/catalog-STAC%2FDCAT%2FPROV%20v11.0.0-6f42c1)](#-stac-dcat--prov-alignment)
[![License](https://img.shields.io/badge/license-CC--BY--4.0-lightgrey)](#)

# docs/data — Data Documentation & Catalog Mapping Index

> 🧭 **This folder is the governed “contract surface” for KFM data.**  
> It documents **how** domain packs map into **STAC/DCAT/PROV**, how they bind into the **Graph**, how they’re exposed via **contract-first APIs**, and how they stay citeable in **UI → Story Nodes → Focus Mode**.

---

## 🚀 TL;DR

- ✅ `docs/data/**` explains **what a dataset is**, **how it’s governed**, and **how it maps** into KFM catalogs & runtime.
- ❌ `docs/data/**` must **not** contain raw/intermediate/processed outputs or authoritative catalog JSON.
- 📦 **Authoritative outputs live in `data/**`**: raw/work/processed + STAC/DCAT/PROV + graph fixtures.
- 🧠 **AI outputs are treated as data artifacts**: they need **citations**, **provenance**, and **policy compliance**.
- 🔒 Governance is enforced as **policy-as-code** (CI + runtime checks), and defaults to **fail-closed**.

---

## 🔗 Quick Navigation

### “Start here” docs
- 🧭 Master guide (preferred): `docs/MASTER_GUIDE_v13.md`
- 🧭 Master guide (legacy): `docs/MASTER_GUIDE_v12.md`
- 📘 Glossary: `docs/glossary.md`
- 🧩 Repo redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`

### Templates
- 🧾 Universal governed doc: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- 🧠 Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- 🧷 API contract extension template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` *(if present)*
- 🧾 Changelog entry template: `docs/templates/TEMPLATE__CHANGELOG_ENTRY.md` *(if present)*

### Canonical data + catalog outputs
- 🗃️ Data lifecycle overview: `data/README.md`
- 🧱 Raw / work / processed: `data/raw/` • `data/work/` • `data/processed/`
- 🛰️ STAC: `data/stac/collections/` + `data/stac/items/`
- 🏷️ DCAT: `data/catalog/dcat/`
- 🧬 PROV: `data/prov/`

### Governance & policy
- ⚖ Governance root: `docs/governance/ROOT_GOVERNANCE.md`
- 🧭 Sovereignty: `docs/governance/SOVEREIGNTY.md`
- 🧠 Ethics: `docs/governance/ETHICS.md`
- 🧯 Policy Pack (OPA/Rego): `api/scripts/policy/README.md` *(if present)*

---

## 🧱 Non‑Negotiables (KFM invariants)

> 🛑 If any of these are violated, treat it as a **bug**, not a “style preference”.

1. **Pipeline ordering is canonical**  
   **Raw sources → ETL/normalize → STAC → DCAT → PROV → Graph → API → UI → Story Nodes → Focus Mode**
2. **No UI → Neo4j direct reads**  
   UI consumes **contracted APIs only** (REST/GraphQL boundaries), so governance rules can be enforced centrally.
3. **No “mystery layers”**  
   Every visible UI layer must trace to **STAC/DCAT/PROV** + stable IDs (aka “the map behind the map”).
4. **Provenance-first publishing**  
   Nothing is promoted for Graph/API/UI without at least **stub PROV + catalog presence**.
5. **Fail-closed governance**  
   Missing provenance, broken links, missing license metadata, or potential secret/sensitive leakage **must block** promotion/merge.

---

## 📌 Scope

| In Scope ✅ | Out of Scope ❌ |
|---|---|
| Governed domain documentation & “rules of the road” | Implementing ETL jobs or API endpoints (belongs in runtime code) |
| Mapping docs / crosswalks for STAC/DCAT/PROV | Authoritative STAC/DCAT/PROV JSON outputs (belong in `data/`) |
| Provenance expectations & review gates | Replacing global governance policy (belongs in `docs/governance/`) |
| Making narrative citeability resolvable via IDs | Writing Story Nodes themselves (belongs in `docs/reports/story_nodes/`) |

### Audience 👥
- **Primary:** Data contributors, catalog maintainers, governance reviewers
- **Secondary:** Graph/API/UI contributors who need stable identifiers + provenance guarantees
- **Tertiary:** Story Node authors + Focus Mode curators who need resolvable citations

---

## 🗂️ What goes where

### ✅ What belongs in `docs/data/`
- Domain “identity” docs: what it is, why it exists, license posture, governance posture
- Mapping docs: how domain assets become STAC/DCAT/PROV and how IDs are assigned
- Provenance expectations: what must be captured; what redactions/generalizations occur
- Downstream requirements: how API/UI/Story Nodes/Focus Mode should cite the domain

### ❌ What must NOT be in `docs/data/`
- Raw inputs, workbench artifacts, processed outputs → **`data/**`**
- Authoritative STAC/DCAT/PROV JSON → **`data/stac/**`, `data/catalog/dcat/**`, `data/prov/**`**
- Executable pipeline code → **`api/**`, `pipelines/**`, or repo-defined code roots**
- Secrets, credentials, access tokens, PII → **never commit**

---

## 🧭 Repo layout note (v13 vs legacy)

KFM documentation describes a **v13 layout** where backend runtime lives under `api/**`. Older docs may reference `src/**`.

Use this rule:
- ✅ If both exist, treat **v13 paths as authoritative**
- ✅ If only one exists, follow the repo reality — but keep links stable in docs

| Concern | v13+ (preferred) | Legacy (if present) |
|---|---|---|
| Backend APIs + contracts | `api/` + `api/contracts/` | `src/server/` + `src/server/contracts/` |
| Pipelines | `pipelines/` or `api/src/.../pipelines/` | `src/pipelines/` |
| Graph ingest code | `api/src/.../graph/` | `src/graph/` |
| UI | `web/` | `web/` |

---

## 🧰 Expected directory pattern (docs + data)

> 🧩 Keep **one canonical location per domain** for mapping docs. Link to it; don’t duplicate.

~~~text
📁 docs/
├── 📁 data/
│   ├── 📄 README.md   👈 (this file)
│   ├── 📁 historical/
│   │   └── 📁 land-treaties/
│   │       └── 📄 README.md
│   ├── 📁 air-quality/
│   │   └── 📄 README.md
│   └── 📁 soils/
│       └── 📁 sda/
│           └── 📄 README.md
│
📁 data/
├── 📁 raw/          👈 immutable-ish source captures + checksums
├── 📁 work/         👈 scratch + sims sandbox (NOT official)
├── 📁 processed/    👈 publishable outputs (official)
├── 📁 stac/
│   ├── 📁 collections/
│   └── 📁 items/
├── 📁 catalog/
│   └── 📁 dcat/
├── 📁 prov/
└── 📁 graph/
    ├── 📁 csv/
    ├── 📁 cypher/
    └── 📄 README.md
~~~

---

## 🗺️ Canonical pipeline ordering (reference)

> **Non-negotiable pipeline ordering:**  
> **Raw Sources → ETL/Normalize → STAC → DCAT → PROV → Graph → API → UI → Story Nodes → Focus Mode**

~~~mermaid
flowchart LR
  RS["Upstream / Raw Sources"] --> ETL["ETL + normalization<br/>pipelines"]
  ETL --> RAW["data/raw/"]
  ETL --> WORK["data/work/"]
  ETL --> PROC["data/processed/"]

  PROC --> STAC["data/stac/<br/>collections + items"]
  PROC --> DCAT["data/catalog/dcat/"]
  ETL --> PROV["data/prov/"]

  DOCS["docs/data/<br/>domain docs + mapping specs"] -. "documents + constrains" .-> STAC
  DOCS -. "documents + constrains" .-> DCAT
  DOCS -. "documents + constrains" .-> PROV

  STAC --> GRAPH["data/graph/ + graph ingest"]
  PROV --> GRAPH
  GRAPH --> API["API layer<br/>(contract-first)"]
  API --> UI["web UI<br/>(MapLibre/3D/etc)"]
  UI --> SN["Story Nodes<br/>(docs/reports/story_nodes/)"]
  SN --> FM["Focus Mode<br/>(evidence-linked context)"]
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

### ✅ KFM “alignment policy”
For anything intended to be discoverable, citeable, or UI-visible, KFM expects:

- **STAC**: “what assets exist, where/when they apply, how to fetch them”
- **DCAT**: “what dataset is this at a catalog level, what are the distributions, access rights”
- **PROV**: “how it was produced, from what, by whom/what, under what parameters”

### 🔗 Cross-layer linkage expectations
A healthy KFM data product should allow you to walk this chain:

**UI layer → API response → graph entity → STAC item/collection → DCAT dataset → PROV bundle → raw sources**

> 🧠 Design intent: **graph nodes reference catalogs**, rather than duplicating heavy payloads.

---

## 📦 Domain pack requirements (minimum)

Every domain should publish (or explicitly justify why it cannot publish) the following artifacts:

### 1) Domain README (governed narrative)
Location:
- Preferred: `docs/data/<domain>/README.md`  
- If a domain chooses co-location under `data/<domain>/`, then `docs/data/` must link to it and treat it as canonical.

Minimum sections:
- 🎯 **What it is** (domain definition + intended uses)
- 🧾 **Sources & licenses** (or link to `data/<domain>/governance/SOURCES_AND_LICENSES.md`)
- 🧬 **Provenance model** (what activities/entities are captured; what redactions happen)
- 🛰️ **STAC model** (what is a collection vs item; assets; geometry/time semantics)
- 🏷️ **DCAT model** (dataset identity, distributions, access rights)
- 🧩 **Graph bindings** (what nodes/edges are created and how IDs are referenced)
- 🧱 **API contract expectations** (endpoints/queries needed by UI & Focus Mode)
- 🗺️ **UI layer requirements** (time slider support, legends, popups, zoom rules)
- 🔒 **Sensitivity & sovereignty handling** (CARE label; generalized/public vs restricted)

### 2) Catalog outputs (authoritative)
- STAC collection(s) and item(s): `data/stac/**`
- DCAT dataset record(s): `data/catalog/dcat/**`
- PROV bundle(s): `data/prov/**`

### 3) Schema + contract references
- Schemas in: `schemas/**`
- Data contract examples (if present): `docs/data/contracts/examples/README.md`

---

## 🧾 Data contracts & schemas (contract-first 🔒)

KFM is contract-first by design:
- **Schemas** define what “valid data” means.
- **Contracts** define what “valid product behavior” means (metadata fields, IDs, access rules, etc.).
- **Policies** enforce both (CI + runtime).

> ✅ Domain docs in `docs/data/**` must describe **which schemas apply** and **where validations occur**.

Recommended doc links (if present):
- `schemas/README.md`
- `docs/standards/` *(profiles + protocols)*
- `api/contracts/` *(API boundary contracts)*

---

## 🧠 AI outputs & narratives are first-class data objects

KFM treats AI-derived artifacts (summaries, extracted entities, narrative drafts, Q&A answers) as **data objects**, meaning:

- They must be **labeled** as AI-generated when applicable
- They must include **citations** (no source → no answer)
- They should be representable in **PROV** (prov:Activity + prov:Agent + prov:Entity)
- They should be governed by the same **policy pack** checks as human-authored outputs

> 🧯 Rule of thumb: if it can influence a decision or appear in UI, it must be **traceable**.

---

## ⏱ Real-time (streaming) data: “many small datasets” model

Real-time layers (sensor feeds, GTFS-RT transit, gauges, alerts) are supported without breaking provenance rules:

- Streaming observations can be modeled as **STAC Items** emitted repeatedly over time
- A corresponding **DCAT Dataset** describes the feed as a whole
- **PROV** must exist at least as a stub or rolling bundle so the UI isn’t displaying unaudited data
- APIs enforce classification & omissions (e.g., sensitive stations hidden from public)

✅ docs/data responsibilities for streaming domains:
- Define **update cadence**, **time semantics**, **retention**, and **how citations resolve**
- Define **how “latest reading” queries work** (API endpoints / query patterns)
- Define what is considered **official** vs **provisional**

---

## 🧪 Simulations & modeling workflows (sandbox → promote)

Simulations are powerful — and dangerous without guardrails.

Recommended KFM posture:
- Run sims in **workbench**: `data/work/sims/` ✅
- Promote vetted outputs into **official data**: `data/processed/` ✅
- Never point UI/Graph directly at `data/work/sims/` outputs ❌

Minimum promotion checklist (for docs/data to require & link):
- ✅ Stable IDs assigned
- ✅ STAC/DCAT/PROV created
- ✅ Inputs pinned (hashes / versions)
- ✅ Parameters pinned (manifest)
- ✅ Environment pinned (container/lockfile)
- ✅ Seeds recorded (if stochastic)
- ✅ Verification & validation notes documented
- ✅ Uncertainty / sensitivity deliverables (if applicable)
- ✅ Governance review completed (sensitivity/sovereignty)

---

## 🔒 Sensitivity, privacy & redaction

KFM governance is not optional; it’s an engineering constraint.

### Classification reminders
- **classification**: open vs restricted vs internal
- **sensitivity**: public vs sensitive (and sublabels such as cultural/sacred, security, privacy)
- **care_label**: use when domains intersect with sovereignty-controlled knowledge

### Common redaction patterns (document in domain modules)
- 📍 **Coordinate fuzzing / aggregation** (especially for culturally sensitive sites)
- 🧮 **k-anonymity / l-diversity / t-closeness** patterns (for tabular sensitive attributes)
- 🔎 **Query auditing / inference control** (deny queries that enable re-identification)
- 🗺️ **Zoom-gated geometry generalization** (public layers at coarse zoom only)

> 🧠 docs/data should describe *what was generalized* and ensure PROV records capture the redaction activity.

---

## ⚖ FAIR+CARE & Governance

### Review gates (examples)
Governance review is typically required when:
- Introducing a new dataset source
- Changing classification/sensitivity
- Publishing derived datasets from sensitive/restricted inputs
- Adding a new UI layer that could reveal sensitive locations by interaction/zoom
- Promoting simulations from `work/` to `processed/`

### Policy-as-code enforcement (high level)
If the repo includes the Policy Pack:
- Policies are versioned (OPA/Rego + Conftest)
- CI must fail on missing provenance, broken links, missing license metadata, or secret/sensitive leakage
- Policies may be grouped with stable IDs (e.g., Catalogs/Provenance/Sovereignty/Security)
- Time-bound waivers (if allowed) must be explicit and documented

---

## 🧪 Validation & CI/CD (recommended)

> 🧯 Tooling commands vary by repo — treat this as **requirements**, not hard-coded CLI.

Minimum checks to expect:
- ✅ Markdown protocol validation (front-matter + required sections)
- ✅ Link/reference checks (avoid orphan pointers)
- ✅ Schema validation (domain schemas + catalog schemas)
- ✅ STAC/DCAT/PROV validation (in canonical locations)
- ✅ Secret scanning + sensitive pattern checks
- ✅ Policy Pack (OPA/Rego) compliance checks (CI + optionally runtime)
- ✅ Determinism checks for pipelines (idempotent runs)
- ✅ Provenance completeness checks (PROV bundle existence + linkage)

---

## 🧭 Domain index (curated entry points)

> 🧩 Add domains here when they meet baseline “publishable” requirements.

### Historical
- 🏛️ Land Treaties: `docs/data/historical/land-treaties/README.md`

### Environment
- 🌫️ Air Quality: `docs/data/air-quality/README.md`
- 🌱 Soils (SDA): `docs/data/soils/sda/README.md`

### Real-time (examples / planned)
- 🚍 Transit (GTFS-RT): `docs/data/transit/README.md` *(planned)*
- 🌊 River Gauges: `docs/data/hydrology/river-gauges/README.md` *(planned)*

---

## ✅ Definition of Done (this README)

- [x] Front-matter complete + protocol-aligned
- [x] Clearly distinguishes **docs** vs **data outputs** vs **runtime code**
- [x] Includes v13 catalog structure (`data/stac/collections` + `data/stac/items`)
- [x] Includes streaming + simulation governance expectations
- [x] Explicit governance/CARE/sovereignty constraints
- [x] Footer refs present (do not remove)

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---:|---|---|
| v1.1.0 | 2026-01-19 | Upgraded to align with v13 repo layout, policy-as-code governance, streaming/simulation workflows, and “AI outputs as data objects” expectations | (you + ChatGPT) |
| v1.0.0 | 2025-12-27 | Initial `docs/data/` README establishing purpose, placement rules, and mapping responsibilities | (you) |

---

## Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Master guide (preferred): `docs/MASTER_GUIDE_v13.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
---