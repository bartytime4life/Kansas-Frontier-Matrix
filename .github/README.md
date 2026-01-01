# Kansas Frontier Matrix — `.github` (CI/CD + Community Health)

This directory is the project’s **GitHub control plane**: workflows, templates, and policies that keep the Kansas Frontier Matrix (KFM) pipeline reproducible, governed, and contributor-friendly.

> **KFM core idea:** KFM is a geospatial + historical knowledge system (“living atlas”) where *every derived artifact and narrative claim is traceable to versioned evidence* through a strict pipeline:  
> **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → API layer → Map UI → Story Nodes → Focus Mode**.

---

## What lives in `.github/`

Typical contents (some files may be added over time):

- `workflows/` — GitHub Actions pipelines (CI, scheduled data refresh, model training, deploy, telemetry, governance ledger sync).
- `ISSUE_TEMPLATE/` — issue templates for bugs, feature requests, data additions, Story Nodes, and governance reviews.
- `PULL_REQUEST_TEMPLATE.md` — PR checklist enforcing KFM invariants (contracts + provenance + governance).
- `CODEOWNERS` — routing for review (domain stewards, API/UI maintainers, governance reviewers).
- `SECURITY.md` — vulnerability reporting process.
- `dependabot.yml` (or Renovate config) — dependency update automation.

---

## Non‑negotiable invariants (the “hard gates”)

These invariants are the *system contracts* that CI must enforce (and reviewers must uphold):

- **Contract-first:** schemas and API contracts are first-class artifacts. Any breaking change requires explicit versioning and compatibility checks.


1. **Canonical pipeline ordering is absolute**  
   No stage may leapfrog upstream artifacts.  
   **ETL → Catalogs → Graph → API → UI → Story Nodes → Focus Mode**

2. **API boundary rule**  
   The UI must never query Neo4j directly. All reads go through the governed API.

3. **Provenance-first publishing**  
   Datasets and evidence artifacts must be registered in STAC/DCAT and traced in PROV **before** they can appear in graph/UI/narratives.

4. **Deterministic, idempotent ETL**  
   Same inputs + config ⇒ same outputs. Runs are logged and repeatable.

5. **Evidence-first narrative**  
   Story Nodes/Focus Mode contain **no unsourced claims**. AI outputs are treated as derived datasets with provenance and clear labeling.

6. **Sovereignty & classification propagation**  
   No derivative artifact can be “less restricted” than its inputs. Sensitive locations must be generalized/redacted where required.

---

## Data lifecycle (required staging + boundary artifacts)

KFM standardizes data movement so every artifact has an unambiguous “stage”:

- `data/raw/<domain>/` — immutable raw ingests (as received)
- `data/work/<domain>/` — intermediate transforms (rebuildable)
- `data/processed/<domain>/` — publish-ready outputs (versioned)

A dataset is not considered **published** until it also has the required *boundary artifacts*:

- **STAC** records → `data/stac/collections/` and `data/stac/items/`
- **DCAT** dataset entry → `data/catalog/dcat/`
- **PROV** lineage bundle → `data/prov/`

These boundary artifacts are what downstream stages (graph/API/UI/narrative) are allowed to consume.

---

## CI/CD philosophy (what workflows should do)

KFM treats GitHub Actions like a **governed assembly line**:

### 1) Pre-commit / lint phase
- Markdown front-matter validation
- YAML/JSON schema checks
- secrets scanning + policy checks

### 2) Build phase
- Reproducible environment build (Docker/Micromamba/lockfiles)
- Container image build for services (API, UI)

### 3) Test phase
- Unit + integration tests
- Data contract checks (schemas, metadata completeness)
- FAIR+CARE and sensitivity checks (including geospatial masking rules)

### 4) Deploy phase
- Controlled promotion to staging/production (environment protections, approvals)
- Optional DB migrations / graph ingest steps

### 5) Monitor phase
- Telemetry export (runtime performance, sustainability metrics where available)

### 6) Govern phase
- Write governance ledger entries (hashes, checks, timestamps)
- Attach artifacts (SBOM, signed manifests) to releases

---

## Contribution workflow (how to make changes that will merge)

### Before you open a PR
- Confirm your change respects the **pipeline ordering**.
- Identify what you are changing:
  - ETL code? ✅ update configs + tests + outputs
  - Data artifact? ✅ add STAC/DCAT/PROV boundary artifacts
  - Graph ingest? ✅ ensure graph references catalogs; add constraints/migrations
  - API contract? ✅ update OpenAPI/GraphQL contract, version if breaking
  - UI feature? ✅ consume only the governed API; add tests
  - Story Node? ✅ use the Story Node template; cite evidence artifacts

### PR checklist (copy/paste into PR description)
- [ ] Pipeline ordering respected (no bypasses)
- [ ] New/changed dataset includes **STAC + DCAT + PROV**
- [ ] Deterministic rerun verified (same input/config ⇒ same output)
- [ ] Governance tags applied (FAIR+CARE, sensitivity, care_label)
- [ ] Tests updated/added and passing
- [ ] Docs updated and follow the Markdown work protocol (front-matter + DoD checklist)

---

## Documentation rules (especially for governed narrative)

All governed docs should use **YAML front-matter** and (when applicable) include fields like:
- `doc_kind`, `status`, `license`
- governance references (`governance_ref`, `ethics_ref`)
- FAIR/CARE and sensitivity labels (`fair_category`, `care_label`, `classification`, `sensitivity`)
- integrity fields (`commit_sha`, checksum)

**Definition of Done (for any governed doc)**
- [ ] Front-matter complete & valid
- [ ] All required sections present
- [ ] All factual claims have citations / evidence links
- [ ] Markdown lint passed, links validated
- [ ] Reviewed by a peer/maintainer (and governance reviewer if sensitive)

---

## Local development expectations (high level)

The stack is designed to be runnable via containers:
- Neo4j (graph store)
- API service (FastAPI + REST/GraphQL)
- Web UI (React + MapLibre)

Configuration and secrets should come from environment variables and **never** be committed.

---

## Project Reference Library (these docs drive design decisions)

These project files are considered **authoritative references** for implementation patterns, research methods, and standards used across KFM:

### Core KFM design, repo governance, and authoring
- *Kansas Frontier Matrix System.docx*
- *Inside and Out of GitHub_ A Deep Guide for the Kansas Frontier Matrix.docx*
- *Comprehensive Markdown Guide_ Syntax, Extensions, and Best Practices.docx*
- *MARKDOWN_GUIDE_v13.md.gdoc*
- *Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf*

### DevOps / shell / collaboration
- *Command Line Kung Fu_ Bash Scripting Tricks, Linux Shell Programming Tips, and Bash One-liners - Command_Line_Kung_Fu_Bash_Scripting_Tricks,_Linux_Shell_Program.pdf*

### Architecture / software design / programming languages
- *clean-architectures-in-python.pdf*
- *implementing-programming-languages-an-introduction-to-compilers-and-interpreters.pdf*

### Data platforms & databases
- *Scalable Data Management for Future Hardware.pdf*
- *PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf*
- *MySQL Notes for Professionals - MySQLNotesForProfessionals.pdf*

### AI / ML foundations
- *AI Foundations of Computational Agents 3rd Ed.pdf*
- *Artificial-neural-networks-an-introduction.pdf*
- *deep-learning-in-python-prerequisites.pdf*
- *Data Mining Concepts & applictions.pdf*
- *Data Science &-  Machine Learning (Mathematical & Statistical Methods).pdf*

### Statistics / experimental design / Bayesian methods
- *Understanding Statistics & Experimental Design.pdf*
- *regression-analysis-with-python.pdf*
- *Bayesian computational methods.pdf*
- *graphical-data-analysis-with-r.pdf*
- *Statistics Done Wrong - Alex_Reinhart-Statistics_Done_Wrong-EN.pdf*

### Scientific modeling & simulation
- *Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf*
- *Generalized Topology Optimization for Structural Design.pdf*

### Graph theory (useful for knowledge graph work)
- *Spectral Geometry of Graphs.pdf*

### Geospatial, mapping, and remote sensing
- *Geographic Information System Basics - geographic-information-system-basics.pdf*
- *geoprocessing-with-python.pdf*
- *python-geospatial-analysis-cookbook.pdf*
- *making-maps-a-visual-guide-to-map-design-for-gis.pdf*
- *Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf*
- *Google Earth Engine Applications.pdf*

### Web UI / cartography / 3D graphics
- *responsive-web-design-with-html5-and-css3.pdf*
- *Node.js Notes for Professionals - NodeJSNotesForProfessionals.pdf*
- *Google Maps API Succinctly - google_maps_api_succinctly.pdf*
- *google-maps-javascript-api-cookbook.pdf*
- *webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf*
- *Computer Graphics using JAVA 2D & 3D.pdf*

---

## Where to go next
- Start with the **Master Guide** (v13) for canonical directory layout + contracts.
- Use issue/PR templates to route reviews to the right owners.
- Keep changes small, evidence-linked, and easy to reproduce.

