---
title: "KFM Reference Library — External Standards & Guides"
path: "docs/reference/REFERENCE_LIBRARY.md"
version: "v0.1.0"
last_updated: "2025-12-19"
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
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:reference-library:v0.1.0"
semantic_document_id: "kfm-reference-library-v0.1.0"
event_source_id: "ledger:kfm:doc:reference-library:v0.1.0"
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

# KFM Reference Library — External Standards & Guides

## 📘 Overview

### Purpose
- Maintain a curated, version-aware set of external standards and authoritative documentation to use as **reference files** for KFM development.
- Keep KFM architecture aligned to the canonical pipeline ordering (**ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**) and prevent “spec drift.”

### Scope
| In Scope | Out of Scope |
|---|---|
| Normative standards (STAC/DCAT/PROV/OGC/W3C/IETF), API specs (OpenAPI/GraphQL), core tool manuals (Neo4j, GDAL, Tika), and governance baselines (FAIR/CARE, OWASP, WCAG). | Vendor-specific marketing docs, unlicensed scans, or duplicated copies of content already governed inside `docs/`. |

### Audience
- Primary: Pipeline engineers, catalog/metadata owners, API/Frontend engineers
- Secondary: Data curators, historians/research partners, governance reviewers

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: STAC, DCAT, PROV-O/PROV-DM, GeoJSON, OGC API Features, JSON-LD, MapLibre, 3D Tiles

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| KFM Master Guide | `docs/MASTER_GUIDE_v12.md` | Docs owner | Canonical pipeline ordering |
| Universal governed-doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs owner | Formatting + front-matter rules |
| Story node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Story owner | Narrative requirements |
| Reference library (this doc) | `docs/reference/REFERENCE_LIBRARY.md` | Docs owner | Curated list + capture rules |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Each reference has a stable link, a version/date, and a rationale tied to pipeline stages
- [ ] Any vendored PDFs have license notes recorded (or are link-only if unclear)
- [ ] Governance + CARE/sovereignty considerations explicitly stated for sensitive materials

## 🗂️ Directory Layout

### This document
- `path`: `docs/reference/REFERENCE_LIBRARY.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Documentation | `docs/` | Canonical governed docs |
| Reference index | `docs/reference/` | This library + optional local snapshots |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Generated STAC/DCAT/PROV artifacts |
| Graph | `src/graph/` | Ontology bindings + ingestion |
| APIs | `src/api/` | REST/GraphQL service layer |
| UI | `src/web/` or `web/` | React + MapLibre/Cesium clients |

### Expected file tree for this sub-area
~~~text
📁 docs/
├── 📁 reference/
│   ├── 📄 REFERENCE_LIBRARY.md
│   └── 📁 external/
│       ├── 📁 standards/
│       ├── 📁 tooling/
│       ├── 📁 governance/
│       ├── 📁 sources/
│       └── 📄 LICENSE_NOTES.md
~~~

## 🧭 Context

### Background
KFM integrates geospatial + historical data and relies on a governed pipeline and strong metadata/provenance standards. A reference library reduces ambiguity across ETL, catalog generation, graph modeling, API contracts, map UI, and story node production.

### Assumptions
- **Link-first** policy: prefer stable links to authoritative sources.
- **Vendor with care**: only store PDF snapshots in-repo if license permits; otherwise keep links + capture date.
- Some references may need periodic refresh (security/accessibility, changing APIs).

### Constraints / invariants
- The canonical ordering **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode** is preserved.
- UI never reads Neo4j directly; it consumes API contracts only.
- Do not infer or disclose sensitive locations from restricted sources.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Which references should be vendored as PDFs vs link-only? | Docs owner | TBD |
| Do we require a “reference refresh” cadence (quarterly/annual)? | Governance owner | TBD |
| Should we pin specific versions (e.g., OpenAPI 3.1.x) in API contracts? | API owner | TBD |

### Future extensions
- Add a `docs/reference/REFRESH_LOG.md` capturing when each reference was reviewed.
- Add a script that checks link health (CI) for link-only references.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/MapLibre UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

## 📦 Data & Metadata

### Reference selection criteria
- **Authoritative**: primary standards body / official docs preferred
- **Stable**: versioned specs or clearly dated docs
- **Relevant**: maps to at least one pipeline stage
- **Governable**: capture license/terms if vendoring; otherwise link-only

### P0 — Standards & contracts (implement against these)
| Topic | Reference | Primary stage(s) | Capture |
|---|---|---|---|
| STAC core | STAC Spec — `https://stacspec.org/en` | Catalog | Link-only or PDF snapshot |
| STAC API | OGC STAC API CS — `https://www.ogc.org/standard/stacapi/` | Catalog/API | Link-only or PDF snapshot |
| STAC versioning | STAC Versioning extension — `https://github.com/stac-extensions/version` | Catalog/PROV | Link-only |
| DCAT 3 | W3C DCAT v3 — `https://www.w3.org/TR/vocab-dcat-3/` | Catalog | Link-only or PDF snapshot |
| PROV-O | W3C PROV-O — `https://www.w3.org/TR/prov-o/` | PROV/Graph | Link-only or PDF snapshot |
| PROV-DM | W3C PROV-DM — `https://www.w3.org/TR/prov-dm/` | PROV | Link-only |
| PROV-JSON | W3C PROV-JSON — `https://www.w3.org/Submission/prov-json/` | PROV | Link-only |
| GeoJSON | RFC 7946 — `https://www.rfc-editor.org/rfc/rfc7946` | API/UI | Link-only |
| OGC API Features | OGC API - Features — `https://ogcapi.ogc.org/features/` | API/UI | Link-only |
| OpenAPI | OpenAPI Spec — `https://spec.openapis.org/oas/latest.html` | API | Link-only |
| JSON Schema | JSON Schema — `https://json-schema.org/specification` | API/Catalog | Link-only |
| GraphQL | GraphQL Spec — `https://spec.graphql.org/` | API | Link-only |
| JSON-LD | W3C JSON-LD 1.1 — `https://www.w3.org/TR/json-ld11/` | DCAT/PROV | Link-only |
| DCMI terms | DCMI Terms — `https://www.dublincore.org/specifications/dublin-core/dcmi-terms/` | Metadata | Link-only |

### P1 — Map + media delivery references
| Topic | Reference | Primary stage(s) | Capture |
|---|---|---|---|
| Map styling | MapLibre style spec — `https://maplibre.org/maplibre-style-spec/` | UI | Link-only |
| Vector tiles | Vector Tiles spec — `https://github.com/mapbox/vector-tile-spec` | UI/API | Link-only |
| 3D tiles | OGC 3D Tiles CS — `https://www.ogc.org/standard/3dtiles/` | UI | Link-only |
| IIIF | IIIF Presentation API — `https://iiif.io/api/presentation/3.0/` | ETL/UI | Link-only |

### P1 — Data formats for scalable geospatial delivery
| Topic | Reference | Primary stage(s) | Capture |
|---|---|---|---|
| Cloud Optimized GeoTIFF | COG overview — `https://www.cogeo.org/` | ETL/API | Link-only |
| GeoParquet | GeoParquet spec — `https://geoparquet.org/` | ETL/Analytics | Link-only |

### P2 — Tooling manuals (implementation)
| Tool | Reference | Primary stage(s) | Capture |
|---|---|---|---|
| Neo4j Cypher | Cypher Manual — `https://neo4j.com/docs/cypher-manual/` | Graph | Link-only |
| Neo4j GDS | Graph Data Science docs — `https://neo4j.com/docs/graph-data-science/` | Graph | Link-only |
| Neo4j APOC | APOC docs — `https://neo4j.com/docs/apoc/` | Graph | Link-only |
| GDAL | GDAL docs — `https://gdal.org/` | ETL | Link-only |
| Apache Tika | Tika docs — `https://tika.apache.org/` | ETL | Link-only |
| Tesseract | Tesseract docs — `https://tesseract-ocr.github.io/` | ETL | Link-only |

### P0/P1 — Governance, accessibility, security
| Topic | Reference | Primary stage(s) | Capture |
|---|---|---|---|
| FAIR | FAIR Principles — `https://www.go-fair.org/fair-principles/` | Governance | Link-only |
| CARE | CARE Principles — `https://www.gida-global.org/care` | Governance | Link-only |
| OWASP API | API Security Top 10 — `https://owasp.org/www-project-api-security/` | API | Link-only |
| WCAG | WCAG 2.2 — `https://www.w3.org/TR/WCAG22/` | UI | Link-only |

### P2 — Source data APIs (if used by KFM ETL)
| Source | Reference | Primary stage(s) | Capture |
|---|---|---|---|
| Chronicling America | loc.gov API docs — `https://libraryofcongress.github.io/data-exploration/` | ETL | Link-only |
| NASA FIRMS | FIRMS API Mapkey — `https://firms.modaps.eosdis.nasa.gov/api/` | ETL | Link-only |
| USGS Earthquakes | FDSN event service — `https://earthquake.usgs.gov/fdsnws/event/1/` | ETL | Link-only |
| GBIF | GBIF API — `https://www.gbif.org/developer/summary` | ETL | Link-only |

## 📌 Versioning & update policy
- Record “capture date” whenever a reference is snapped to PDF.
- Prefer versioned URLs (W3C TR, RFCs, version tags) whenever available.
- If a reference is known to change frequently (security/accessibility/data APIs), review annually or when a breaking change is detected.

---
