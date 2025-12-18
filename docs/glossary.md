import os, textwrap, datetime, pathlib, json, re
docs_dir = "/mnt/data/docs"
os.makedirs(docs_dir, exist_ok=True)

content = """---
title: "KFM Glossary"
path: "docs/glossary.md"
version: "v1.0.0"
last_updated: "2025-12-18"
status: "draft"
doc_kind: "Glossary"
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

doc_uuid: "urn:kfm:doc:glossary:v1.0.0"
semantic_document_id: "kfm-glossary-v1.0.0"
event_source_id: "ledger:kfm:doc:glossary:v1.0.0"
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

# KFM Glossary

## 📘 Overview

### Purpose
- Provide **canonical definitions** for common terms and acronyms used across KFM docs, pipelines, catalogs, graph, APIs, UI, and Story Nodes.
- Reduce ambiguity in governance reviews by standardizing terminology.

### Scope
| In Scope | Out of Scope |
|---|---|
| Definitions for KFM concepts, standards, and common geospatial/graph terms used in KFM docs | Full external standards documentation (STAC/DCAT/PROV specs themselves) |
| Project-specific terms (Focus Mode, Story Nodes, Extension Matrix, etc.) | New governance policy creation (refer to governance docs) |

### Audience
- Primary: contributors writing docs or implementing pipeline/graph/API/UI changes
- Secondary: reviewers validating provenance, sensitivity, and contract compliance

### Definitions (link to glossary)
- You are here: `docs/glossary.md`

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (canonical pipeline) | `docs/MASTER_GUIDE_v12.md` | Maintainers | Pipeline ordering + subsystem inventory |
| Governed templates | `docs/templates/` | Maintainers | Required structure for KFM docs |
| STAC/DCAT/PROV profiles | `KFM-STAC/DCAT/PROV v11.0.0` | Data/Catalog | Validation targets for catalogs |
| Ontology protocol | `KFM-ONTO v4.1.0` | Graph | Labels/relations + migration discipline |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Terms used across KFM docs are defined with minimal ambiguity
- [ ] New terms introduced in docs/pipelines/graph/api/design are added here
- [ ] Governance + CARE/sovereignty concepts are defined consistently

## 🗂️ Directory Layout

### This document
- `path`: `docs/glossary.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Docs | `docs/` | Governed documentation, templates, design notes |
| Data | `data/` | Raw/work/processed data + catalogs (STAC) |
| Pipelines | `src/pipelines/` + `docs/pipelines/` | ETL and catalog build docs |
| Graph | `src/graph/` + `docs/graph/` | Ontology, migrations, constraints |
| APIs | `src/server/` | REST/GraphQL contracts + services |
| Frontend | `web/` + `docs/design/` | React/Map UI, layer registry and UX docs |
| Telemetry | `docs/telemetry/` + `schemas/telemetry/` | Metrics/logs + schemas |
| Governance | `docs/governance/` | ROOT_GOVERNANCE, ETHICS, SOVEREIGNTY |

### Expected file tree for this sub-area
~~~text
📁 docs/
├─ 📄 glossary.md
├─ 📄 README.md
├─ 📄 ARCHITECTURE.md
├─ 📄 MASTER_GUIDE_v12.md
├─ 📁 🧩 templates/
└─ 📁 🧾 standards/
~~~

## 🧭 Context

### Background
KFM spans multiple technical layers (data → catalogs → graph → APIs → UI → narrative). A shared glossary keeps those layers interoperable and reduces “terminology drift” across contributions.

### Assumptions
- The glossary is a living document.
- Terms should be defined in a way that remains stable even as implementation details evolve.

### Constraints / invariants
- Use the canonical pipeline ordering language consistently:
  - ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode.
- Do not define new policy here; link to governance docs for rules.

### How to update this glossary
1. Add new terms when you introduce a new concept, acronym, schema field name, or subsystem name.
2. Prefer **project meanings** over textbook meanings if KFM uses a term in a specific way.
3. If a term is disputed or evolving, define it as a **working definition** and mark it `TBD` for governance review.

## 📚 Glossary (A–Z)

> Formatting convention used below:
> - **TERM (Acronym)** — definition. *(Notes / related terms)*

### A
- **A11y (Accessibility)** — practices that ensure UI and docs are usable by people with disabilities (keyboard navigation, contrast, ARIA labels, etc.).
- **API (Application Programming Interface)** — the contract boundary between clients (UI/tools) and KFM’s backend services. KFM’s UI should consume data via APIs or pre-built artifacts, not direct graph access.
- **Asset (STAC Asset)** — a file/resource referenced from a STAC Item (e.g., COG, GeoJSON, PDF, thumbnail). *(See: STAC Asset, STAC Item.)*
- **Audit panel** — a Focus Mode UI panel intended to show governance flags, provenance pointers, and redaction/generalization status. *(See: Focus Mode, Governance, Redaction.)*

### B
- **BBox (Bounding box)** — a rectangular spatial extent, typically `[west, south, east, north]`, used for spatial indexing and discovery. *(Often used in STAC.)*

### C
- **CARE Principles** — a framework emphasizing Collective Benefit, Authority to Control, Responsibility, and Ethics in Indigenous data governance. *(In KFM, CARE impacts sensitivity handling and generalization/redaction.)*
- **Catalog (KFM)** — the machine-readable inventory of data products and their metadata/lineage, primarily via STAC/DCAT/PROV.
- **Cesium** — a 3D geospatial rendering library used for 3D visualization in the UI. *(Often paired with MapLibre for 2D/3D.)*
- **CI/CD** — automation that validates, tests, and (optionally) deploys changes (schemas, docs, code). KFM expects validation gates for catalogs and contracts.
- **Classification** — a coarse access label for artifacts (e.g., `open`, `restricted`). *(Do not confuse with sensitivity; classification is an access policy category.)*
- **COG (Cloud Optimized GeoTIFF)** — a GeoTIFF formatted for HTTP range requests and efficient tiled access. *(Often a preferred raster asset type.)*
- **Contract test** — an automated test that ensures API payloads and schema expectations remain stable across changes.

### D
- **DCAT (Data Catalog Vocabulary)** — W3C vocabulary for describing datasets in catalogs; used in KFM for interoperable dataset descriptions. *(See: STAC, PROV-O.)*
- **Deterministic ETL** — ETL runs that produce the same outputs given the same inputs, versions, and configs (including fixed random seeds when applicable).
- **DVC (Data Version Control)** — tool often used to track large datasets and pipeline artifacts without committing large binaries directly to Git.

### E
- **Entity (PROV / Graph)** — a “thing” in provenance or the knowledge graph (e.g., dataset, map, place, event). *(In PROV: prov:Entity.)*
- **ETL (Extract, Transform, Load)** — pipeline stage that ingests raw sources, normalizes formats, and produces processed outputs plus lineage logs.

### F
- **FAIR Principles** — Findable, Accessible, Interoperable, Reusable; KFM’s cataloging and provenance practices support FAIR.
- **Focus Mode** — an interactive, topic-centric UI mode that freezes context (area/time/topic) and presents a consolidated dashboard with citations and governance signals. Focus Mode is provenance-only: nothing appears without a source; AI insights are opt-in and must show uncertainty. *(See: Story Node, Provenance, Uncertainty.)*

### G
- **GDAL** — geospatial data processing library/tooling (format conversion, reprojection, raster/vector operations).
- **Generalization** — reducing spatial or descriptive precision to protect sensitive entities while preserving analytical usefulness. *(Related: Redaction.)*
- **GeoJSON** — JSON format for representing vector geometries + properties.
- **GeoSPARQL** — OGC/W3C standard vocabulary/functions for geospatial querying in semantic systems (e.g., within-distance, intersects). *(KFM aligns geospatial semantics with GeoSPARQL concepts where applicable.)*
- **Graph (Knowledge graph)** — the semantic core linking entities (Place/Event/Dataset/etc.) and relationships, including provenance links.
- **GraphQL** — a query language/API style that can expose typed access to KFM graph-backed data through resolvers.
- **Governance** — the rules, review gates, and policies controlling how data is ingested, published, generalized/redacted, and narrated.

### H
- **H3** — hexagonal indexing system commonly used for spatial tiling/aggregation. *(May appear in pipeline or modeling extensions.)*
- **Hallucination (in KFM context)** — presenting narrative or claims without provenance-linked sources. Focus Mode forbids hallucinated/unsourced content.

### I
- **Item (STAC Item)** — a STAC object representing a single spatiotemporal “thing” (scene, tile, dataset slice) with assets and metadata. *(See: STAC.)*

### J
- **JSON-LD** — JSON for Linked Data; used to serialize graph-like semantics and align with W3C vocabularies like DCAT and PROV.

### K
- **KFM (Kansas Frontier Matrix)** — a geospatial-historical knowledge system with a governed end-to-end pipeline producing interactive maps and provenance-led narratives.
- **KFM-DCAT / KFM-PROV / KFM-STAC profiles** — KFM-specific validation profiles/version targets for DCAT, PROV, and STAC artifacts (schema rules, required fields).
- **KFM-MDP (Markdown protocol)** — KFM’s governed Markdown conventions (front-matter fields, required section structure, fence rules).
- **KFM-ONTO** — KFM’s ontology protocol/version (labels, relationships, constraints, migration discipline).
- **KFM-PPC (Pipeline contract)** — KFM’s pipeline ordering/contract version (non-negotiable stage ordering and subsystem expectations).

### L
- **Layer registry** — a UI configuration registry that lists available map layers, their sources, and access rules; used to prevent unauthorized or sensitive data exposure.
- **Lineage** — traceability describing how an artifact was produced from inputs and processes. *(See: PROV-O, Provenance.)*
- **LOD (Level of detail)** — technique to render large datasets efficiently by showing simpler representations at lower zoom levels.

### M
- **MapLibre** — open-source web mapping library used for 2D map rendering in KFM.
- **MCP (Master Coder Protocol)** — a reproducibility-oriented documentation and workflow discipline: explicit versions, clear methods, repeatable results, and traceable artifacts.
- **Metadata** — descriptive data about a dataset/artifact (title, description, license, extents, timestamps, provenance pointers, etc.).
- **Migration (Graph)** — a controlled change to the ontology or graph structure that preserves compatibility or upgrades data safely.

### N
- **Neo4j** — a graph database used for KFM’s semantic core and relationship queries.
- **NDVI (Normalized Difference Vegetation Index)** — remote sensing index used to estimate vegetation; may be used as a layer, feature, or anomaly signal in modeling workflows.

### O
- **Ontology** — formal definition of entity types, properties, and relationships; used to enforce consistency in the knowledge graph.
- **OpenAPI** — a specification for describing REST APIs; used to document and validate REST contracts.

### P
- **PROV-O (W3C Provenance Ontology)** — W3C ontology for representing provenance (entities, activities, agents, and relationships like “used” or “generated by”).
- **Provenance** — evidence-backed trace showing the origin, inputs, process, and responsible parties for an artifact or claim. In KFM, provenance is required for Focus Mode and Story Nodes.
- **prov:Activity** — a PROV construct representing a process (e.g., an ETL run) that uses inputs and generates outputs.
- **prov:Agent** — a PROV construct representing an actor (person, org, software) associated with an activity.
- **prov:Entity** — a PROV construct representing a produced/used artifact (dataset, file, document, etc.).
- **prov:used / prov:wasGeneratedBy / prov:generatedAtTime** — core PROV relations for inputs, generation activity, and timestamp.

### R
- **Raster** — gridded data (e.g., imagery, elevation). Often stored as GeoTIFF/COG.
- **Redaction** — removing or hiding sensitive information entirely (e.g., omitting coordinates). *(Related: Generalization.)*
- **Reproducibility** — ability to regenerate outputs from inputs with pinned versions/configs and recorded provenance.

### S
- **Schema validation** — automated checks that JSON/JSON-LD artifacts conform to required schemas/profiles (e.g., STAC/DCAT/PROV).
- **Sensitivity** — a label indicating potential harm if details are disclosed (e.g., protected sites). Sensitivity may require generalization or redaction.
- **Site dossier** — a UI/info bundle compiling datasets, documents, graph neighbors, and evidence related to a specific site/entity.
- **STAC (SpatioTemporal Asset Catalog)** — open specification for describing geospatial assets and collections using JSON. KFM uses STAC Collections/Items to package and discover processed assets.
- **STAC Collection** — a STAC object that groups items and defines shared metadata and spatial/temporal extents.
- **STAC Item** — a single catalog entry within a collection representing one spatiotemporal unit with assets.
- **STAC Asset** — a link/descriptor to an actual file/resource (raster, vector, document, thumbnail) within an item.
- **Story Node** — a versioned narrative artifact (structured markdown) that is machine-ingestible, linked to graph entities/datasets, and required to cite every factual claim. Story Nodes feed Focus Mode narratives.

### T
- **Telemetry** — logging and metrics collected to observe performance, security, and governance compliance (e.g., validation failures, redaction counts).
- **Tiling** — partitioning large spatial datasets into smaller pieces for fast rendering and retrieval (often used with WebGL maps).
- **Time slider** — UI control to filter layers and context by time.

### U
- **Uncertainty** — quantitative/qualitative indicator for confidence in model outputs or inferred claims. In KFM, AI-derived insights must be labeled and opt-in.
- **User overlay** — a user-provided dataset (e.g., custom GeoJSON, scanned map) ingested via a controlled ETL mechanism, typically sandboxed/unverified until reviewed.

### V
- **Validation gate** — a mandatory check in CI/CD (schemas, tests, docs lint) that must pass before changes are accepted.
- **Viewport** — the current visible map extent/zoom used to filter data requests and render decisions.

### W
- **WDE (World Discovery Engine)** — a referenced innovation/extension concept; in KFM context, WDE-related work typically implies new data products, graph entities, API extensions, and validation.
- **WebGL** — browser graphics API used for high-performance map rendering.
- **WKT (Well-Known Text)** — text format for geometries; commonly used in semantic/GeoSPARQL contexts.

## 🗺️ Diagrams
- Not required for this glossary. *(If future work adds term-dependency diagrams, place them here.)*

## 📦 Data & Metadata
- This document is a definitions catalog; it does not directly introduce new datasets.
- When adding a new dataset, ensure any new terminology or acronyms are added here.

## 🌐 STAC, DCAT & PROV Alignment
- This glossary supports consistent interpretation of STAC/DCAT/PROV artifacts but does not contain STAC/DCAT/PROV payloads itself.

## 🧠 Story Node & Focus Mode Integration
- Story Nodes and Focus Mode should link to this glossary for shared terminology.
- When writing Story Nodes, prefer terms defined here, especially for governance (sensitivity/redaction) and provenance (PROV-O) language.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (front-matter + required sections)
- [ ] Link check to referenced docs (as implemented in CI)

### Reproduction
~~~bash
# (Repo-specific commands may differ.)
# markdownlint docs/glossary.md
# linkcheck docs/glossary.md
~~~

## ⚖ FAIR+CARE & Governance

### Review gates
- If a term impacts governance (e.g., sensitivity categories, redaction rules), it should be reviewed by the governance owners referenced in front-matter.

### CARE / sovereignty considerations
- Ensure terms related to Indigenous data governance remain aligned to the sovereignty policy.
- Do not include sensitive site examples or specific protected coordinates in definitions.

### AI usage constraints
- This glossary can be summarized or indexed, but must not be used to invent policy or infer sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-18 | Initial glossary: core pipeline, cataloging, graph, API/UI, governance terms. | Bartytime |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
"""
file_path = os.path.join(docs_dir, "glossary.md")
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

file_path
