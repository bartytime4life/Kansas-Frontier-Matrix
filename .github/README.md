# Kansas Frontier Matrix (KFM)

_Evidence-first geospatial knowledge hub for Kansas — maps, data, narratives, and AI assistance with provenance (“the map behind the map”)._

## 📘 Overview

### What KFM is
Kansas Frontier Matrix (KFM) is an **open-source, evidence-first** geospatial knowledge and modeling platform that fuses historical archives, GIS data, remote sensing, simulations, and AI-assisted research into a cohesive, governed system.

### Mission
Make Kansas’s “spatial truth” — from archival maps to live sensor feeds — **searchable, mappable, auditable, and modelable for everyone**.

### What this file is
This is the README for the repo’s `.github/` layer: CI workflows, security/compliance policies, and merge gates that enforce KFM’s provenance-first operating contract.

### Non-negotiables
- **Provenance & transparency:** nothing in KFM is a black box. Every dataset, map layer, and AI output must be traceable to its source and processing steps.
- **Layer separation:** UI does not query databases directly; access is mediated by the API boundary and policy enforcement.
- **Governance at boundaries:** every transition (raw → processed → catalogs → databases → APIs → UI/AI) is validated.
- **Human-centered & ethical:** Focus Mode is advisory-only and evidence-backed; it does not execute autonomous actions.
- **FAIR + CARE + Indigenous Data Sovereignty:** openness where appropriate; controlled access, consent, and context where required.

### Start here
- Repo overview: [`../README.md`](../README.md)
- KFM documentation entrypoint: [`../docs/MASTER_GUIDE_v13.md`](../docs/MASTER_GUIDE_v13.md)
- Architecture overview: [`../docs/architecture/system_overview.md`](../docs/architecture/system_overview.md)
- FAIR+CARE standard: [`../docs/standards/faircare.md`](../docs/standards/faircare.md)

## 🗂️ Directory Layout

### What lives in `.github/`
`.github/` typically contains:
- `.github/workflows/` — GitHub Actions workflows (tests, schema validation, governance gates)
- `.github/SECURITY.md` — security policy (if used)
- `.github/ISSUE_TEMPLATE/` — issue/PR templates (if used)
- `.github/CODEOWNERS` — review routing (if used)

### Canonical repo top-levels (expected)
| Area | Path | What lives here |
| --- | --- | --- |
| CI / governance automation | `.github/` | Workflows, policy docs, security/compliance files |
| Data domains | `data/` | Raw, working, processed artifacts + catalogs (STAC/DCAT/PROV) |
| Documentation | `docs/` | Governed docs (guides, designs, domain notes) |
| Templates | `docs/templates/` | Governed doc templates (universal, story node, API) |
| Architecture docs | `docs/architecture/` | System design docs, blueprints, ADRs |
| Story nodes | `docs/reports/story_nodes/` | Governed narrative content (draft vs published) |
| Schemas | `schemas/` | JSON Schemas for STAC/DCAT/PROV/story nodes/UI/telemetry |
| Pipelines | `src/pipelines/` | ETL jobs & transformations (domain-specific) |
| Graph | `src/graph/` | Graph build/ontology bindings/ingest scripts/constraints |
| API boundary | `src/server/` | API implementation + API contracts + policy integration |
| UI | `web/` | Frontend app (React, MapLibre/Cesium components) |
| Methods & experiments | `mcp/` | Runs, notebooks, model cards (reproducibility artifacts) |
| Tests | `tests/` | Unit + integration tests |
| Tools | `tools/` | Validators, utility scripts, DevOps helpers |
| Releases | `releases/` | Versioned release artifacts (data bundles, manifests, SBOM) |

### Data domain structure (expected)
Each data domain typically follows:
- `data/<domain>/raw/` — immutable source artifacts (read-only)
- `data/<domain>/work/` — intermediate outputs
- `data/<domain>/processed/` — publishable processed outputs
- `data/<domain>/README.md` — domain runbook, sources, notes

> Note: large binaries may live outside Git (cloud storage, Git LFS, checksummed external references). The folder structure still matters for reproducibility in dev/prod.

## 🗺️ Diagrams

### KFM “truth path” (end-to-end)
```mermaid
flowchart TD
  A[Raw Sources] --> B[ETL + Normalization]
  B --> C[(Processed Data)]
  C --> D[STAC + DCAT + PROV Artifacts]
  D --> E[(PostGIS / Neo4j / Search Index)]
  E --> F[API Boundary (FastAPI + OPA)]
  F --> G[Web UI (React + MapLibre/Cesium)]
  G --> H[Story Nodes]
  H --> I[Focus Mode (Evidence-backed AI)]
  I --> G
```

## 📦 Data

### Content-only Markdown policy
KFM Markdown is **content-only**. Do **not** embed metadata in YAML “front matter” blocks; metadata belongs in structured sidecar JSON and in the platform catalogs (STAC/DCAT/PROV).

### Minimum publishable dataset package
A dataset is “KFM-ready” when it has:
1. **Raw source(s)** recorded in `data/<domain>/raw/` (and/or a fetch script that lands there)
2. **Pipeline code** in `src/pipelines/<domain>/` producing deterministic outputs
3. **Processed outputs** in `data/<domain>/processed/`
4. **STAC** collection + items (for geospatial assets) under `data/stac/`
5. **DCAT** dataset record (JSON-LD) under `data/catalog/dcat/` (title, description, license, spatial/temporal coverage, keywords, distributions)
6. **PROV** lineage record under `data/prov/` linking raw → steps → outputs → agents
7. **Graph integration** (when applicable) so the dataset is discoverable and connected
8. **Tests + validators** proving schemas and constraints still pass

### Adding a new dataset (workflow)
1. Place sources into `data/<domain>/raw/` (or add a fetch step that lands there).
2. Add/extend a pipeline under `src/pipelines/<domain>/`.
3. Emit outputs to `data/<domain>/work/` and `data/<domain>/processed/`.
4. Generate/refresh STAC/DCAT/PROV artifacts.
5. Update graph build/export if the dataset adds entities/relationships.
6. Add/update docs (`docs/`) and run validations/tests before opening a PR.

### Story nodes: narrative + map + evidence
Story nodes are governed narrative objects that connect:
- `story.md` — narrative text with citations
- `story.json` — structured metadata
- `script.json` — map/animation instructions (optional)
- `assets/` — supporting images/media

Treat story nodes like first-class artifacts: versioned, reviewed, and linked back to datasets + provenance.

## 📜 Governance

### FAIR + CARE + Indigenous Data Sovereignty
KFM follows FAIR principles **and** CARE principles:
- **Collective Benefit**
- **Authority to Control**
- **Responsibility**
- **Ethics**

Indigenous Data Sovereignty means Indigenous peoples have a say in how data about them or their lands are used and shared. Sensitive cultural knowledge may require protections (rights flags in metadata, warning/context labels, restricted map zoom, aggregation requirements, or access controls).

### Focus Mode (AI) guardrails
Focus Mode is **not** an ungoverned chatbot. Guardrails include:
- **Prompt Gate** input filtering/sanitization against prompt injection, disallowed content, and privacy-violating requests
- **Evidence retrieval first:** graph/spatial/text retrieval produces an evidence bundle that the model must cite
- **Citations enforced:** every AI-derived sentence must be traceable; automated checks verify citation patterns
- **Sandboxed operation:** no unapproved tools; no direct internet/filesystem access; least privilege by default
- **Local-first models:** LLM runs on KFM infrastructure (privacy, sovereignty, offline deployments)

### CI / merge gates (what belongs in `.github/workflows/`)
KFM’s CI is expected to fail the build if any of the following break:
- Markdown structure and required headings (template compliance)
- Broken internal links
- Schema validation (STAC/DCAT/PROV/story-node schemas)
- Graph integrity constraints (ontology, relationships, forbidden cycles, etc.)
- Pipeline reproducibility checks (deterministic outputs, checksums where applicable)
- API contract tests (OpenAPI/GraphQL schema consistency)
- Security scans (dependency/container vulnerabilities)
- Secrets detection
- PII / sensitive location checks (especially for protected cultural sites and private individuals)
- Classification rules (outputs can’t be less sensitive than inputs)

### Governance review triggers (request explicit review)
Escalate for governance review when a change introduces or modifies:
- New public dataset releases, especially with human/tribal/community data
- New narrative claims, story nodes, or AI narrative features
- Data classification/sensitivity levels or access-control rules
- New data sources with unclear licensing, consent, or provenance
- Policy logic (OPA rules), Prompt Gate rules, or citation enforcement rules

## 📚 References (Optional)
- `docs/MASTER_GUIDE_v13.md`
- `MARKDOWN_GUIDE_v13.md` (governed Markdown rules)
- KFM architecture/system overview docs under `docs/architecture/`
- FAIR+CARE standard under `docs/standards/`
- STAC/DCAT/PROV schemas under `schemas/`

## 🕰️ Version History
| Version | Date (YYYY-MM-DD) | Author | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-02-08 | KFM Maintainers | Initial `.github/README.md` aligned to KFM architecture + governance docs |
