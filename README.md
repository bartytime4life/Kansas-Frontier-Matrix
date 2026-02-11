# Kansas Frontier Matrix (KFM) 🧭🗺️  
**Provenance-first geospatial knowledge + storytelling platform for Kansas (“the map behind the map”).**

![Status](https://img.shields.io/badge/status-draft-blue)
![Governance](https://img.shields.io/badge/governance-FAIR%2BCARE-informational)
![Provenance](https://img.shields.io/badge/provenance-first-brightgreen)
![Policy](https://img.shields.io/badge/policy-OPA%20(Rego)-orange)
![Docs](https://img.shields.io/badge/docs-governed%20Markdown-purple)

> [!IMPORTANT]
> **Trust membrane / governance invariant:** the **UI never directly touches the databases**. All access is mediated by the **backend API** and its validation + policy enforcement layers. [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## What is KFM?

The **Kansas Frontier Matrix (KFM)** is a **full-stack geospatial information system** designed to integrate historical + spatial data about Kansas into **interactive maps, timelines, and narrative “Story Nodes”**, with an integrated, governed AI assistant (“Focus Mode”). [oai_citation:1‡Kansas Frontier Matrix (KFM) Comprehensive Guide.pdf](sediment://file_000000004530722f96d93b826296d578) [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

KFM is explicitly described as a **pipeline → catalog → database → API → UI** system that turns raw files into **trustworthy, explorable knowledge**, where every layer/story/answer remains traceable back to sources (“the map behind the map”). [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## Key capabilities

- **Interactive mapping + timeline exploration** with narrative Story Nodes. [oai_citation:4‡Kansas Frontier Matrix (KFM) Comprehensive Guide.pdf](sediment://file_000000004530722f96d93b826296d578)
- **Provenance-first by design:** maps/stories/AI answers are intended to be backed by versioned data + citations. [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- **Governed AI (“Focus Mode”):** constrained by policy to support ethical + factual responses (not an ungoverned chatbot). [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- **Clean architecture + strict boundaries** (domain/use-case/interface/infrastructure layers). [oai_citation:7‡Kansas Frontier Matrix (KFM) Comprehensive Guide.pdf](sediment://file_000000004530722f96d93b826296d578)
- **FAIR + CARE alignment** (findable/interoperable + community ethics and sovereignty). [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:9‡Kansas Frontier Matrix (KFM) Comprehensive Guide.pdf](sediment://file_000000004530722f96d93b826296d578)

---

## Architecture at a glance

### Core components (as described in project docs)

| Layer / Component | Expected responsibility |
|---|---|
| Data pipelines | Ingest + process datasets; attach metadata + lineage |
| Catalogs | Treat catalogs (e.g., **STAC/DCAT/PROV**) as canonical interfaces between pipeline outputs and runtime services [oai_citation:10‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) |
| Storage | **PostgreSQL + PostGIS** for geospatial-relational data; **Neo4j** for the knowledge graph; **Elasticsearch/OpenSearch** for full-text/vector search [oai_citation:11‡Kansas Frontier Matrix (KFM) Comprehensive Guide.pdf](sediment://file_000000004530722f96d93b826296d578) |
| API | **FastAPI** providing unified REST (and GraphQL) services [oai_citation:12‡Kansas Frontier Matrix (KFM) Comprehensive Guide.pdf](sediment://file_000000004530722f96d93b826296d578) |
| UI | **React (JS/TS)** + **MapLibre GL** for interactive maps, timeline, layer controls, Story Node reading, Focus Mode UI [oai_citation:13‡Kansas Frontier Matrix (KFM) Comprehensive Guide.pdf](sediment://file_000000004530722f96d93b826296d578) |
| Policy enforcement | OPA/Rego policy-as-code expected in CI and runtime gating (deny/sanitize sensitive outputs) [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) |

### Data + governance flow (conceptual)

```mermaid
flowchart LR
  A[Raw sources] --> B[Ingest & transform pipelines]
  B --> C[Catalogs: STAC / DCAT / PROV]
  C --> D[(PostGIS)]
  C --> E[(Neo4j)]
  C --> F[(Search: OpenSearch/Elastic)]
  D --> G[Governed API (FastAPI REST/GraphQL)]
  E --> G
  F --> G
  G --> H[Web UI (React + MapLibre)]
  G --> I[Focus Mode (Governed AI)]
  P[OPA policies (policy/)] --> G
  P --> CI[CI policy + schema validation]
```

> [!NOTE]
> Some elements above are presented in the docs as design/blueprint expectations. Validate exact service names and ports in your checked-out repo if they differ. (If something is unknown, mark it **“(not confirmed in repo)”**.) [oai_citation:15‡KFM Markdown Guide.docx.pdf](sediment://file_000000007d1c71f5827af1abdbf2b2fa)

---

## Quickstart (local development via Docker Compose)

### Prerequisites
- Docker + Docker Compose (v2 recommended)

### Steps

```bash
cp .env.example .env
docker compose up --build
```

Open:
- UI: `http://localhost:3000`  
- API docs (Swagger): `http://localhost:8000/docs`  
- Neo4j Browser: `http://localhost:7474`  (not confirmed in repo, but referenced in docs)

> [!TIP]
> If you change core dependencies or base images, rebuild with `--build`. If ports are in use, adjust `.env` or Compose port mappings.

---

## Repository layout

> [!NOTE]
> The project docs describe KFM as a monorepo containing **data/**, **docs/**, **src/**, **web/**, etc. If your actual repo differs, update this section to match what `tree -L 2` shows.

```text
.
├── data/
│   ├── raw/
│   ├── work/
│   ├── processed/
│   ├── catalog/
│   └── provenance/
├── docs/
│   ├── 00-front-matter/
│   ├── 01-architecture/
│   ├── 02-data/
│   ├── 03-governance/
│   ├── 04-api/
│   ├── 05-ui/
│   ├── 06-focus_mode/
│   ├── 07-story_nodes/
│   ├── standards/
│   └── templates/
├── mcp/
├── schemas/
├── src/
│   ├── api/
│   ├── backend/
│   ├── pipelines/
│   └── shared/
├── tests/
├── tools/
├── web/
├── releases/
├── README.md
├── LICENSE
├── CITATION.cff
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── docker-compose.yml
└── .env.example
```

---

## Data domains and example sources (inventory)

KFM’s data inventory materials include examples such as:

| Domain | Example sources mentioned in project materials |
|---|---|
| Biodiversity / species | GBIF, iNaturalist, eButterfly, state extension resources |
| Birds | eBird, Kansas Ornithological Society |
| Climate / weather | NOAA (NCEI), Kansas Mesonet, NASA POWER |
| Demographics | US Census, IPUMS NHGIS |
| Agriculture | USDA NASS QuickStats, Kansas Dept. of Agriculture |

> [!IMPORTANT]
> Treat these as **examples** from the inventory docs. Each dataset must be ingested through the governed pipeline and cataloged with required provenance metadata before it is considered usable in KFM’s runtime services. [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## Story Nodes and Focus Mode

**Story Nodes** are governed narrative Markdown documents that tie evidence + context together for the UI (and for Focus Mode to render citations/attribution). The Story Node template expects:  
- short, neutral paragraphs,  
- citations per factual sentence,  
- an entity index and relationships,  
- explicit listing of the Story Node file path + referenced dataset IDs + graph node IDs. [oai_citation:17‡KFM Markdown Guide.docx.pdf](sediment://file_000000007d1c71f5827af1abdbf2b2fa)

### Templates you should use (governed)
- `docs/templates/TEMPLATE__STORY_NODE_V3.md` [oai_citation:18‡KFM Markdown Guide.docx.pdf](sediment://file_000000007d1c71f5827af1abdbf2b2fa)
- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` [oai_citation:19‡KFM Markdown Guide.docx.pdf](sediment://file_000000007d1c71f5827af1abdbf2b2fa)
- `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` [oai_citation:20‡KFM Markdown Guide.docx.pdf](sediment://file_000000007d1c71f5827af1abdbf2b2fa)
- `docs/standards/KFM_CHATGPT_WORK_PROTOCOL.md` [oai_citation:21‡KFM Markdown Guide.docx.pdf](sediment://file_000000007d1c71f5827af1abdbf2b2fa)
- Governance docs: `docs/governance/ROOT_GOVERNANCE.md`, `ETHICS.md`, `SOVEREIGNTY.md` [oai_citation:22‡KFM Markdown Guide.docx.pdf](sediment://file_000000007d1c71f5827af1abdbf2b2fa)

> [!NOTE]
> Story Node placement may vary. A docs source notes that as of v13, Story Nodes are expected under a `docs/reports/<topic>/story_nodes/` hierarchy **(not confirmed in repo)**. [oai_citation:23‡KFM Markdown Guide.docx.pdf](sediment://file_000000007d1c71f5827af1abdbf2b2fa)

---

## Documentation governance (Definition of Done)

For any governed doc (including Story Nodes) to be merge-ready, the docs require at least:

- [ ] Required template structure and headings (order matters) [oai_citation:24‡KFM Markdown Guide.docx.pdf](sediment://file_000000007d1c71f5827af1abdbf2b2fa)  
- [ ] **Provenance for all substantive claims** (no claim stands without evidence) [oai_citation:25‡KFM Markdown Guide.docx.pdf](sediment://file_000000007d1c71f5827af1abdbf2b2fa)  
- [ ] Governance tags + sensitivity handling (redact/generalize sensitive locations; flag for review) [oai_citation:26‡KFM Markdown Guide.docx.pdf](sediment://file_000000007d1c71f5827af1abdbf2b2fa)  
- [ ] Advanced Markdown used appropriately (tables, Mermaid, callouts, details, etc.) [oai_citation:27‡KFM Markdown Guide.docx.pdf](sediment://file_000000007d1c71f5827af1abdbf2b2fa)  
- [ ] CI validation passes (markdown lint, structure/schema validation, link checks, sensitivity/accessibility scans) [oai_citation:28‡KFM Markdown Guide.docx.pdf](sediment://file_000000007d1c71f5827af1abdbf2b2fa)

---

## Policy enforcement (OPA / Rego)

The blueprint describes policy-as-code patterns where:
- CI can fail on missing provenance artifacts (e.g., missing PROV), or disallowed content patterns.
- Runtime requests (including AI answers) can be allowed/denied/sanitized based on policy decisions.  
- `policy/` is treated as the policy source of truth. [oai_citation:29‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

> [!TIP]
> The blueprint also suggests contributors can run policy checks locally using tools like Conftest **(exact commands not confirmed in repo)**. [oai_citation:30‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## Contributing

1. Read `CONTRIBUTING.md` (and the docs standards under `docs/standards/`).  
2. Use templates first (`docs/templates/`).  
3. Keep the **trust membrane** intact: no direct DB access from UI; backend logic should respect repository interfaces and clean architecture boundaries. [oai_citation:31‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:32‡Kansas Frontier Matrix (KFM) Comprehensive Guide.pdf](sediment://file_000000004530722f96d93b826296d578)
4. Ensure your change passes the documentation Definition of Done checklist (above).

---

## License and citation

- License information should be confirmed in `LICENSE` (and any doc licensing conventions in doc front-matter).  
- If present, use `CITATION.cff` when citing KFM in academic or public work (not confirmed in repo beyond documented repo layout expectations).

---

## See also (recommended reading order)

- `docs/MASTER_GUIDE_v13.md` (canonical structure + governance gates) [oai_citation:33‡KFM Markdown Guide.docx.pdf](sediment://file_000000007d1c71f5827af1abdbf2b2fa)  
- `docs/01-architecture/` (system architecture + trust membrane)  
- `docs/03-governance/` (FAIR+CARE, sovereignty, ethics)  
- `docs/07-story_nodes/` (Story Node guidance and examples)  
- `docs/06-focus_mode/` (Focus Mode behavior + auditing + citations)

---

### Maintainers: README reality-check checklist

- [ ] Confirm actual directory layout matches the tree above; update if needed.  
- [ ] Confirm local ports and URLs in `docker-compose.yml`.  
- [ ] Confirm whether GraphQL is enabled and what endpoint path is used.  
- [ ] Confirm doc canonical paths (Story Nodes location, templates).  
- [ ] Confirm license(s) for code vs docs/story nodes.