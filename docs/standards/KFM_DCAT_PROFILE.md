---
title: "KFM Standard — DCAT Profile"
path: "docs/standards/KFM_DCAT_PROFILE.md"
version: "v11.0.0"
last_updated: "2025-12-19"
status: "draft"
doc_kind: "Standard"
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

doc_uuid: "urn:kfm:doc:standards:dcat-profile:v11.0.0"
semantic_document_id: "kfm-standard-dcat-profile-v11.0.0"
event_source_id: "ledger:kfm:doc:standards:dcat-profile:v11.0.0"
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

# KFM Standard — DCAT Profile

**Profile ID:** `KFM-DCAT v11.0.0`

## 📘 Overview

### Purpose
- Define how KFM publishes dataset and service metadata using DCAT, including:
  - repository placement and file layout under `data/catalog/dcat/`
  - minimum required fields and recommended controlled values
  - mapping between STAC Collections and DCAT Datasets and Distributions
  - linkage to PROV provenance bundles under `data/prov/`
- Serve as a contract for any pipeline step that emits or consumes DCAT records:
  - catalog builder
  - graph ingest
  - API metadata exposure
  - external catalog export

### Scope
| In scope | Out of scope |
|---|---|
| DCAT Dataset and Distribution records for KFM datasets | Full RDF and Linked Data tutorial |
| DCAT Catalog record for the repository or deployment | API endpoint definitions and payload schemas |
| DCAT DataService records for KFM APIs | Graph ontology design |
| Mapping rules from STAC and PROV into DCAT | UI rendering and UX requirements |

### Audience
- Primary: Data engineers, catalog maintainers
- Secondary: Graph ingestion maintainers, API developers, documentation authors

### Definitions
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **DCAT**: Data Catalog Vocabulary for describing datasets and services
  - **Dataset**: A logical dataset exposed by KFM
  - **Distribution**: A concrete access method for a dataset
  - **Catalog**: A collection of datasets
  - **DataService**: An API or service that provides access to data
  - **STAC Collection and Item**: Metadata for geospatial and temporal assets
  - **PROV bundle**: Provenance record capturing activities, agents, and entities

### Key artifacts
| Artifact | Path or identifier | Notes |
|---|---|---|
| DCAT profile | `docs/standards/KFM_DCAT_PROFILE.md` | Governs KFM-DCAT constraints |
| DCAT dataset records | `data/catalog/dcat/` | One record per dataset |
| STAC collections and items | `data/stac/collections/`, `data/stac/items/` | Primary for geospatial and temporal assets |
| PROV bundles | `data/prov/` | Required for auditability and lineage |

### Definition of done
- [ ] Front-matter complete and valid
- [ ] Placement and naming conventions are explicit for `data/catalog/dcat/`
- [ ] MUST, SHOULD, MAY constraints are listed
- [ ] STAC, DCAT, PROV linkage rules are defined
- [ ] Sensitivity and classification handling is stated
- [ ] Validation steps are listed and repeatable

## 🗂️ Directory Layout

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw, work, processed data per domain |
| DCAT catalogs | `data/catalog/dcat/` | DCAT dataset and service records |
| STAC catalogs | `data/stac/` | STAC collections and items |
| PROV lineage | `data/prov/` | Provenance bundles |
| Documentation | `docs/` | Governed docs and domain docs |
| Pipelines | `src/pipelines/` | ETL and catalog emitters |
| Schemas | `schemas/` | JSON Schemas or SHACL shapes if adopted |

### Expected file tree for this sub-area
~~~text
📁 docs/
└── 📁 standards/
    └── 📄 KFM_DCAT_PROFILE.md

📁 data/
├── 📁 stac/
│   ├── 📁 collections/
│   │   └── 📄 <collection_id>.json
│   └── 📁 items/
│       └── 📄 <item_id>.json
├── 📁 catalog/
│   └── 📁 dcat/
│       ├── 📄 catalog.jsonld
│       ├── 📁 datasets/
│       │   └── 📄 <dataset_id>.jsonld
│       └── 📁 services/
│           └── 📄 <service_id>.jsonld
└── 📁 prov/
    └── 📁 <run_id>/
        └── 📄 bundle.jsonld
~~~

## 🧭 Context

### Background
KFM standardizes metadata before graph ingest. After ETL, outputs are packaged as STAC items and collections, DCAT dataset records, and PROV provenance bundles. DCAT records make datasets discoverable and provide a dataset-level grouping layer that can point to STAC assets and other files.

### Assumptions
- STAC is used for geospatial or temporal assets.
- For non-geospatial datasets or logical groupings, KFM creates DCAT dataset records stored in `data/catalog/dcat/`.
- Every new dataset publication includes:
  - a STAC catalog entry when applicable
  - a DCAT dataset description
  - a PROV activity describing how the dataset was produced

### Constraints and invariants
- Canonical pipeline ordering is preserved: ETL → STAC/DCAT/PROV catalogs → Graph → APIs → UI → Story Nodes → Focus Mode.
- ETL and catalog generation are deterministic, reproducible, and idempotent.
- Classification tags and sensitivity labels in metadata control what can be exposed publicly. Sensitive locations may require generalization.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Canonical serialization: JSON-LD only, or JSON-LD plus Turtle | TBD | TBD |
| Do we maintain a single `catalog.jsonld` root, or only per-dataset files | TBD | TBD |
| Do we adopt SHACL shapes for constraints, JSON Schema, or both | TBD | TBD |
| Controlled vocabularies for themes, keywords, and access rights | TBD | TBD |

### Future extensions
- Add SHACL constraints for KFM-DCAT under `schemas/dcat/`
- Add catalog integrity CI checks for broken links and required terms
- Add DCAT-AP export if required by external portals

## 🗺️ Diagrams

### System dataflow
~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### DCAT object model for KFM minimal profile
~~~mermaid
flowchart TB
  Catalog[dcat:Catalog] -->|dcat:dataset| Dataset[dcat:Dataset]
  Dataset -->|dcat:distribution| Dist[dcat:Distribution]
  Service[dcat:DataService] -->|dcat:servesDataset| Dataset
  Dataset -->|dct:provenance or prov:wasGeneratedBy| Prov[PROV bundle]
  Dataset -->|dct:relation or dcat:landingPage| STAC[STAC Collection or Items]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Location | Notes |
|---|---|---|---|
| STAC collections and items | JSON | `data/stac/collections/`, `data/stac/items/` | Source for extents and license when applicable |
| PROV bundles | JSON-LD | `data/prov/<run_id>/bundle.jsonld` | Provides lineage for reproducibility |
| Domain documentation | Markdown | `docs/data/<domain>/` | Describes dataset intent and constraints |
| Data artifacts | mixed | `data/<domain>/` | Files pointed to by DCAT distributions |

### Outputs
| Output | Format | Location | Notes |
|---|---|---|---|
| DCAT datasets | JSON-LD preferred | `data/catalog/dcat/datasets/<dataset_id>.jsonld` | One per dataset |
| DCAT services | JSON-LD preferred | `data/catalog/dcat/services/<service_id>.jsonld` | Optional |
| DCAT catalog | JSON-LD preferred | `data/catalog/dcat/catalog.jsonld` | Optional root entry |

### Sensitivity and redaction
- Every DCAT Dataset record MUST carry enough access metadata to enforce public or restricted exposure.
- If any distribution refers to sensitive locations, the DCAT record SHOULD:
  - expose only generalized spatial bounds, or
  - omit spatial extents entirely in public mode and rely on restricted channels.

### Quality signals
- Required terms present and non-empty where required
- All distributions resolve to real files or reachable endpoints
- PROV linkage exists and references a recorded run or activity
- License is present and matches an allowed identifier
- Version traceability exists for updated datasets

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Geospatial and temporal assets are represented as STAC Items.
- STAC Items are grouped into STAC Collections.
- STAC JSON resides under:
  - `data/stac/collections/`
  - `data/stac/items/`

### DCAT

#### KFM-DCAT principle
DCAT is KFM’s dataset-level discovery and interoperability layer. DCAT dataset records are stored under `data/catalog/dcat/` and may describe logical datasets that point to component STAC assets and other files.

#### Normative language
- MUST: required for every published dataset
- SHOULD: required unless a documented exception exists
- MAY: optional

#### KFM-DCAT minimum required terms for datasets
Each `dcat:Dataset` record MUST include:

1) Identity and description
- `dct:identifier` as a stable, unique identifier
- `dct:title`
- `dct:description`

2) Rights and governance
- `dct:license`
- `dct:accessRights` using a controlled value or documented equivalent

3) Access
- at least one `dcat:distribution`

4) Provenance linkage
- one of:
  - `dct:provenance` pointing to a PROV bundle file, or
  - `prov:wasGeneratedBy` pointing to an Activity IRI

Each `dcat:Dataset` record SHOULD include:
- `dct:issued` and `dct:modified`
- `dcat:keyword` with at least one keyword
- `dct:spatial` and `dct:temporal` when applicable

#### KFM-DCAT minimum required terms for distributions
Each `dcat:Distribution` MUST include:
- `dct:format`
- one of:
  - `dcat:accessURL`
  - `dcat:downloadURL`

Each `dcat:Distribution` SHOULD include:
- `dct:license` when distribution-specific
- `dct:conformsTo` when a schema or standard applies

#### Dataset identifier conventions
- A dataset identifier MUST be stable across rebuilds for the same semantic dataset.
- Preferred pattern for new datasets:
  - `urn:kfm:dataset:<domain>:<dataset_slug>:v<semver>`
- File naming SHOULD mirror the identifier in a filesystem-safe way:
  - `<domain>__<dataset_slug>__v<semver>.jsonld`

#### Mapping STAC collections to DCAT datasets
When a STAC Collection exists, KFM SHOULD map:

| STAC Collection field | DCAT field | Notes |
|---|---|---|
| `id` | `dct:identifier` | Use STAC id as seed |
| `title` | `dct:title` | Human-readable |
| `description` | `dct:description` | Human-readable |
| `license` | `dct:license` | Carry through |
| `extent.spatial` | `dct:spatial` | Generalize if sensitive |
| `extent.temporal` | `dct:temporal` | Interval if available |
| `keywords` | `dcat:keyword` | Carry through if present |

#### Linking DCAT datasets to STAC assets
A DCAT Dataset representing a grouping of STAC assets SHOULD:
- include a Distribution whose `dcat:accessURL` points to the relevant STAC Collection JSON, and or
- include `dct:relation` entries pointing to key STAC Items or Collections

#### KFM DataService records
When KFM exposes an API endpoint that serves a dataset, represent it as `dcat:DataService` with:
- `dcat:endpointURL`
- `dcat:servesDataset` pointing to the dataset identifier
- `dct:conformsTo` pointing to the API contract identifier if available

#### Access rights controlled values
KFM SHOULD standardize `dct:accessRights` values:
- `public`
- `restricted`
- `embargoed`
- `internal`

### PROV-O
- `prov:wasDerivedFrom` links datasets and distributions to source entities
- `prov:wasGeneratedBy` links outputs to pipeline activities
- Activities and agents SHOULD be identifiable and time-stamped

## 🔁 Versioning
- Dataset versions SHOULD link to predecessors and successors.
- PROV records MUST allow tracing inputs → transformations → outputs.
- Graph ingestion SHOULD mirror dataset version relationships so UI and APIs can expose evolution over time.

## Appendix Example minimal JSON-LD dataset record
~~~json
{
  "@context": {
    "dcat": "http://www.w3.org/ns/dcat#",
    "dct": "http://purl.org/dc/terms/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@type": "dcat:Dataset",
  "dct:identifier": "urn:kfm:dataset:example:demo:v1.0.0",
  "dct:title": "Demo Dataset",
  "dct:description": "Illustrative DCAT Dataset record for the KFM-DCAT profile.",
  "dct:license": "CC-BY-4.0",
  "dct:accessRights": "public",
  "dcat:keyword": ["kansas", "history", "demo"],
  "dcat:distribution": [
    {
      "@type": "dcat:Distribution",
      "dct:format": "application/json",
      "dcat:accessURL": "data/stac/collections/demo.json"
    }
  ],
  "dct:provenance": "data/prov/2025-01-01_demo_run/bundle.jsonld"
}
~~~

## Appendix External references
~~~text
DCAT v3 (W3C): https://www.w3.org/TR/vocab-dcat-3/
PROV-O (W3C): https://www.w3.org/TR/prov-o/
STAC: https://stacspec.org/
~~~

