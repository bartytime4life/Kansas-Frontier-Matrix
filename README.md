---
title: "🧭 Kansas Frontier Matrix (KFM) — Root README"
path: "README.md"
version: "v1.0.0-draft"
last_updated: "2025-12-31"
status: "draft"
doc_kind: "Guide"
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
care_label: "Public · Low-Risk"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"
doc_uuid: "urn:kfm:doc:root:readme:v1.0.0-draft"
semantic_document_id: "kfm-root-readme-v1.0.0-draft"
event_source_id: "ledger:kfm:doc:root:readme:v1.0.0-draft"
commit_sha: "<latest-commit-hash>"
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

# Kansas Frontier Matrix (KFM) 🗺️🌾

**Kansas Frontier Matrix** is an open-source **geospatial + historical knowledge system** — a “living atlas” of Kansas — built to ingest heterogeneous sources, publish governed metadata catalogs, build a semantically structured knowledge graph, and serve evidence through contracted APIs into a map-and-narrative UI.

If you’re here to **use** KFM: start with the docs.  
If you’re here to **contribute**: follow the pipeline. Every addition must be evidence-linked and provenance-traceable.

---

## 🧭 Start Here

**1) Read the Master Guide**
- `docs/MASTER_GUIDE_v13.md` — canonical pipeline, repo invariants, and v13 structure expectations.

**2) Follow the Markdown & Template rules**
- `docs/standards/KFM_MARKDOWN_FORMATTING_GUIDE.md` — required YAML front-matter, citation rules, and doc validation.

**3) Check governance before adding sensitive content**
- `docs/governance/ROOT_GOVERNANCE.md`
- `docs/governance/ETHICS.md`
- `docs/governance/SOVEREIGNTY.md`
- `docs/governance/REVIEW_GATES.md`

---

## 🚦 Non‑Negotiables

### 1) Canonical pipeline ordering (must not be bypassed)
**ETL → STAC/DCAT/PROV Catalogs → Neo4j Graph → APIs → Map UI → Story Nodes → Focus Mode**

### 2) Catalog gatekeeping
If an artifact does not have complete catalog metadata and pass validation, it **does not** enter the graph/UI.

### 3) API boundary is mandatory
The UI must never read the graph/database directly. The API layer is the contract boundary for security, provenance, and redaction.

### 4) Evidence-first narratives
Story content is governed. Factual claims must be resolvable to catalog IDs / document IDs.

---

## 🔁 Canonical Pipeline Overview

~~~mermaid
flowchart LR
  subgraph Data
    A["Raw Sources"] --> B["ETL + Normalization"]
    B --> C["STAC Items + Collections"]
    C --> D["DCAT Dataset Views"]
    C --> E["PROV Lineage Bundles"]
  end

  C --> G["Neo4j Graph (references catalogs)"]
  G --> H["API Layer (contracts + redaction)"]
  H --> I["Map UI — React · MapLibre · (optional) Cesium"]
  I --> J["Story Nodes (governed narratives)"]
  J --> K["Focus Mode (provenance-linked context bundle)"]
~~~

---

## 🗂️ Repository Map (Directory Layout)

This section describes the **intended v13 layout** and how KFM organizes work by lifecycle stage and subsystem boundary.

### Top-level directories (with emoji + purpose)

| Emoji | Path | What lives here |
|---:|---|---|
| 📦 | `data/` | Raw → work → processed data, plus catalogs (STAC/DCAT/PROV) |
| 🧾 | `docs/` | Canonical governed documentation (guides, designs, domain notes, reports) |
| 🧩 | `schemas/` | JSON Schemas for docs, catalogs, UI registry, telemetry, story nodes |
| 🧪 | `src/pipelines/` | ETL jobs & domain-specific transformations |
| 🧠 | `src/graph/` | Graph build code, ontology bindings, ingest scripts, constraints |
| 🔌 | `src/server/` | API services + contract definitions (OpenAPI/GraphQL where applicable) |
| 🖥️ | `web/` | Frontend app (React + MapLibre; optional Cesium integration) |
| 📰 | `docs/reports/story_nodes/` | Governed narratives (draft vs published) + story assets |
| 🧰 | `mcp/` | Methods & computational experiments (runs, notebooks, model cards) |
| ✅ | `tests/` | Unit & integration tests across subsystems |
| 🚀 | `releases/` | Versioned bundles (catalog snapshot, graph exports, UI manifests, SBOM) |

### Root files you should expect (and why they matter)

- 📘 `README.md` — you are here
- 🪪 `LICENSE` — project licensing
- 🧾 `CITATION.cff` — how to cite KFM
- 🤝 `CONTRIBUTING.md` — contribution rules & PR flow
- 🛡️ `SECURITY.md` — disclosure and security posture
- 🧑‍⚖️ `CODE_OF_CONDUCT.md` — community standards
- 🧱 `docker-compose.yml` — local dev stack (commonly includes API + Neo4j)
- 🧩 `.env.example` — example environment config
- 🛠️ `Makefile` — common local commands (run `make help` if present)
- 🤖 `.github/workflows/` — CI/CD: validation, tests, scheduled ingests, releases

### A compact tree view

~~~text
Kansas-Frontier-Matrix/
├─ README.md
├─ LICENSE
├─ CITATION.cff
├─ CONTRIBUTING.md
├─ CODE_OF_CONDUCT.md
├─ SECURITY.md
├─ docker-compose.yml
├─ .env.example
├─ Makefile
├─ .github/
│  └─ workflows/
├─ data/
│  ├─ raw/
│  ├─ work/
│  ├─ processed/
│  ├─ stac/
│  ├─ catalog/
│  │  └─ dcat/
│  └─ prov/
├─ schemas/
├─ docs/
│  ├─ MASTER_GUIDE_v13.md
│  ├─ templates/
│  ├─ standards/
│  ├─ architecture/
│  ├─ governance/
│  └─ reports/
│     └─ story_nodes/
│        ├─ draft/
│        └─ published/
├─ src/
│  ├─ pipelines/
│  ├─ graph/
│  └─ server/
├─ web/
├─ mcp/
├─ tests/
└─ releases/
~~~

---

## 🏁 Getting Started (Readers & Contributors)

### If you’re exploring (no code)
1. Browse `docs/MASTER_GUIDE_v13.md`
2. Browse `docs/architecture/` (system blueprint, ADRs)
3. Browse `docs/reports/story_nodes/published/` (public narrative content)
4. Browse `data/catalog/dcat/` and `data/stac/` (what data exists + where it came from)

### If you’re developing (typical local flow)
> Exact commands vary by module and are governed by the repo’s Makefile/scripts. Prefer `make help` and the Master Guide.

~~~bash
# 1) Configure environment
cp .env.example .env

# 2) Bring up local stack (if docker-compose.yml is present)
docker compose up -d

# 3) Discover available commands (if Makefile is present)
make help
~~~

---

## ➕ Adding a Dataset (Canonical Path)

When you add a dataset, you are adding **evidence**. Evidence must travel through the full pipeline.

### Step 0 — Choose / create a domain
- Example domains: `treaties`, `trails`, `forts`, `railroads`, `floods`, `prairie`, etc.
- Keep domain work isolated to avoid cross-contamination.

### Step 1 — Ingest raw source material
- Put originals in: `data/raw/<domain>/`
- Treat raw as immutable.

### Step 2 — ETL / normalization (domain pipelines)
- Implement or extend ETL under: `src/pipelines/<domain>/`
- Write intermediates to: `data/work/<domain>/`
- Write publishable outputs to: `data/processed/<domain>/`

### Step 3 — Publish catalogs (required boundary artifacts)
For every dataset/evidence artifact you publish, you must create:

- 🗺️ **STAC** records: `data/stac/…`  
- 🧾 **DCAT** entry: `data/catalog/dcat/…`  
- 🔍 **PROV** lineage: `data/prov/…`  

### Step 4 — Graph integration (references catalogs)
- Graph nodes should reference **catalog IDs** (STAC/DCAT/PROV), not duplicate large payloads.
- Prefer exports to `data/graph/csv/` (if present) and ingest scripts under `src/graph/`.

### Step 5 — API exposure
- Add/extend endpoints under `src/server/`
- Update the API contract docs/specs and ensure redaction + provenance checks are enforced.

### Step 6 — UI integration (registry-driven)
- UI reads from APIs, not the graph.
- Register new layers/features (typically in a UI registry schema/manifest) so they appear in the map UI.

---

## 📰 Story Nodes (Narratives with Evidence)

Story Nodes are governed narrative documents that bind **context** to **evidence**.

**Where they live**
- Drafts: `docs/reports/story_nodes/draft/`
- Published: `docs/reports/story_nodes/published/`

**Key rules**
- Use the Story Node template (v3) from `docs/templates/`
- Every factual claim must cite an evidence identifier (dataset ID, document ID, PROV entity, etc.)
- Stories must not publish unless all citations resolve (no “citation needed” gaps)

---

## 🧠 AI / ML & Derived Data

AI is allowed in KFM only when it produces **auditable, cataloged derived datasets**.

If you generate an AI-derived artifact (OCR corpus, model output layer, classification raster, predicted route, etc.), it must:
1. Be stored in `data/processed/...`
2. Have STAC/DCAT/PROV records like any other dataset
3. Record model identity, run parameters, and timestamps in PROV
4. Carry uncertainty semantics (define what “confidence” means for that product)
5. Never infer or reconstruct sensitive locations or private attributes

---

## 🧑‍⚖️ Governance, Ethics, and Sovereignty

KFM treats governance as a first-class system component:
- Tag and label sensitivity honestly
- Follow review gates for culturally sensitive or high-risk content
- Respect sovereignty and community stewardship expectations

If you’re uncertain about sensitivity classification, default to caution and route through governance review.

---

## ✅ Contributing

1. Read `CONTRIBUTING.md`
2. Follow the Master Guide + Markdown Guide
3. Keep changes pipeline-aligned (ETL → Catalog → Graph → API → UI → Story → Focus)
4. Run validations/tests locally where available
5. Submit PRs with clear provenance notes and any required governance flags

---

## 📌 License & Citation

- **Code license:** see `LICENSE`
- **Data licensing:** declared per dataset in DCAT/STAC metadata (do not assume a global data license)
- **How to cite KFM:** see `CITATION.cff`

---

## 🕰️ Version History

| Version | Date | Summary of Changes | Author |
|---|---|---|---|
| v1.0.0-draft | 2025-12-31 | Rebuilt root README to align with Master Guide v13 pipeline, directory layout, and governed-document standards. | AI-assisted draft (human review required) |
---
