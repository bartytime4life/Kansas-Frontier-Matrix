---
title: "🌫️ Air Quality — Ingestion"
path: "data/air-quality/ingestion/README.md"

version: "v0.1.0"
last_updated: "2025-12-16"
release_stage: "Draft"
lifecycle: "Active"
review_cycle: "Quarterly · Data Steward Review"
content_stability: "evolving"

status: "Draft"
doc_kind: "README"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"

indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Review on major pipeline changes"

commit_sha: "<latest-commit-hash>"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

ontology_alignment:
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"
  owl_time: "ProperInterval"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/standards/kfm_markdown_protocol_v11.2.6.md@v11.2.6"

doc_uuid: "urn:kfm:doc:data:air-quality:ingestion:readme:v0.1.0"
semantic_document_id: "kfm-data-air-quality-ingestion-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:air-quality:ingestion:readme:v0.1.0"
doc_integrity_checksum: "<sha256>"

story_node_refs: []
immutability_status: "mutable"

ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "metadata-extraction"
  - "layout-normalization"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
---

<div align="center">

# 🌫️ **Air Quality — Ingestion**
`data/air-quality/ingestion/README.md`

**Purpose**  
Define the **ingestion contract** for the Air Quality domain in KFM: where inputs come from, where artifacts land, what metadata/provenance must be emitted, and what validations are required so downstream **STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes** remain consistent.

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/Domain-Air%20Quality-blue" />
<img src="https://img.shields.io/badge/Pipeline-ETL%20%2F%20Ingestion-blueviolet" />
<img src="https://img.shields.io/badge/Status-Draft-lightgrey" />

</div>

---

## 📘 Overview

This directory documents **how Air Quality data enters the KFM system**.

### What this README covers

- **Ingestion scope (ETL stage):** acquire/land raw Air Quality data, normalize into a KFM-friendly shape, and emit **metadata + provenance** needed for cataloging and downstream loading.
- **Artifacts and placement:** what belongs in `data/raw/`, `data/processed/`, `data/stac/`, `data/checksums/`, `data/reports/`, and `mcp/runs/`.
- **Contracts:** minimum metadata/provenance expectations so the KFM catalogs and graph loaders can operate without “orphan” assets.

### What this README does not cover

- Source-specific implementation details (API keys, credentials, vendor SDKs). Those belong in secure runtime configuration, never committed.
- Graph schema/ontology changes. If new concepts are needed, they require schema/ontology review (do not invent terms ad hoc).

### Outcomes expected from a correct ingestion run

1. **Raw landing** of upstream assets (stored in the repo’s raw tier, typically DVC/LFS-managed).
2. **Checksums** for raw and processed assets.
3. **Processed, analysis-ready artifacts** under the processed tier.
4. **Catalog metadata** suitable for STAC/DCAT publication and discoverability.
5. **Lineage/provenance** (PROV) that links sources → activities → outputs with a stable run ID.
6. **Validation reports** committed (or referenced) so CI and reviewers can verify integrity.

---

## 🗂️ Directory Layout

> Directory trees must be fenced as `~~~text` and use consistent branch glyphs and emojis.

~~~text
📁 data/                                      — Project data root (see `data/ARCHITECTURE.md`)
├── 📄 ARCHITECTURE.md                        — Canonical data placement rules (raw/processed/stac/etc.)
├── 📄 README.md                              — Data overview and indices
├── 📁 air-quality/                           — Air Quality domain workspace (this domain)
│   └── 📁 ingestion/                         — Ingestion contract + manifests (this directory)
│       ├── 📄 README.md                      — This file (ingestion expectations + runbook)
│       ├── 📁 manifests/                     — Source + run manifests (repo-tracked, no secrets)
│       ├── 📁 configs/                       — Config templates (env-agnostic; secrets excluded)
│       └── 📁 notes/                         — Mapping notes, edge cases, change rationale
├── 📁 raw/                                   — Raw landing zone (large files; may be DVC/LFS managed)
│   └── 📁 air-quality/                       — Raw Air Quality pulls (partitioned by source/time)
├── 📁 processed/                             — Curated/normalized outputs (analysis-ready)
│   └── 📁 air-quality/                       — Processed Air Quality products
├── 📁 stac/                                  — STAC catalogs/collections/items for assets
│   └── 📁 air-quality/                       — STAC artifacts for Air Quality assets
├── 📁 checksums/                             — Hash manifests for raw/processed assets
│   └── 📁 air-quality/                       — Checksums for Air Quality artifacts
└── 📁 reports/                               — QA/validation outputs for CI and review
    └── 📁 air-quality/                       — Air Quality QA reports (schema, STAC, DCAT, etc.)
~~~

### Placement rules (non-negotiable)

- **Do not commit large data files** into `data/air-quality/ingestion/`.  
  This folder is for **documentation + manifests + config templates**.
- **Raw payloads** land in `data/raw/air-quality/…`.
- **Derived/normalized outputs** land in `data/processed/air-quality/…`.
- **Catalog metadata** (STAC) lands in `data/stac/air-quality/…`.
- **Checksums** land in `data/checksums/air-quality/…`.
- **Validation outputs** land in `data/reports/air-quality/…`.
- **Run logs + provenance bundles** land in `mcp/runs/<run_id>/…` (or `mcp/experiments/…` when exploratory).

---

## 🧭 Context

KFM is designed to treat data ingestion as a **governed, reproducible pipeline**, where every dataset and transformation can be traced through:

- **Human-readable documentation** (this README and related runbooks)
- **Machine-readable catalogs** (STAC/DCAT)
- **Machine-readable lineage** (PROV)

Air Quality ingestion specifically supports KFM’s broader platform goals of integrating **ecological change and real-time/environmental data** into the historical + spatial storytelling stack.

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[Upstream Air Quality Source] --> B[Ingestion Activity (ETL)]
  B --> C[data/raw/air-quality/…]
  B --> D[Validate + Normalize]
  D --> E[data/processed/air-quality/…]
  D --> F[data/checksums/air-quality/…]
  D --> G[data/reports/air-quality/…]
  D --> H[data/stac/air-quality/…]
  D --> I[PROV bundle in mcp/runs/<run_id>/…]
  H --> J[Catalog Layer (STAC/DCAT)]
  E --> K[Graph Loaders]
  K --> L[Neo4j Graph]
  L --> M[APIs]
  M --> N[React/MapLibre UI]
  N --> O[Story Nodes / Focus Mode]
~~~

### Provenance framing (conceptual)

- **PROV Entity:** a raw file, a processed table, a derived raster, a STAC Item JSON
- **PROV Activity:** a specific ingestion run (identified by `run_id`)
- **PROV Agent:** the pipeline (and, when applicable, the maintainer approving the run)

---

## 🧱 Architecture

### Pipeline stage placement

This README governs **ETL/Ingestion** responsibilities only:

1. **ETL →** acquire + normalize + validate assets and metadata  
2. **STAC/DCAT/PROV →** publish machine-readable description + lineage  
3. **Graph →** load curated outputs into Neo4j (via loaders, not via UI)  
4. **APIs →** expose query services  
5. **UI →** consumes APIs (frontend must not read the graph directly)  
6. **Story Nodes/Focus Mode →** narrative layers consume cataloged evidence, not guesses

### Contract boundaries

- Ingestion **MUST NOT** introduce new graph ontology terms without governance review.
- Ingestion **MUST NOT** bypass API boundaries for UI needs.
- Ingestion **MUST** preserve stable IDs/keys so downstream merges/dedup are deterministic.

---

## 📦 Data & Metadata

### Ingestion inputs (expected)

1. **Source manifest** describing what to fetch, legal constraints, cadence, and coverage.
2. **Runtime configuration** (credentials, tokens, endpoints) provided securely at runtime.
3. Optional: **previous run state** to support incremental pulls.

#### Source manifest template (repo-tracked, no secrets)

Store provider/source definitions as JSON in one of:
- `data/air-quality/ingestion/manifests/` (domain-local), and/or
- the repo’s shared source registry (if present in your implementation).

~~~json
{
  "source_id": "air-quality__<provider>__<product>",
  "title": "<human-readable name>",
  "description": "<what this source provides>",
  "license": "<license id or text>",
  "publisher": "<org>",
  "access": {
    "method": "download|api|bulk",
    "base_url": "<public url>",
    "auth": "none|runtime-secret"
  },
  "coverage": {
    "spatial": "<bbox or reference>",
    "temporal": "<start/end or 'ongoing'>",
    "cadence": "hourly|daily|monthly|ad_hoc"
  },
  "expected_artifacts": [
    {
      "artifact_kind": "raw",
      "format": "csv|json|geotiff|other",
      "partitioning": "by_date|by_station|by_tile|other"
    }
  ]
}
~~~

### Ingestion outputs (minimum required)

Each ingestion run should produce:

- **Raw assets** (exact upstream payloads)
- **Normalized/processed outputs** suitable for analytics and/or mapping
- **STAC artifacts** (Collections/Items/Assets describing the above)
- **Checksums** for any file that is referenced by STAC or loaders
- **Run provenance** bundle with a stable `run_id`
- **Validation reports** sufficient for CI/review

#### Run manifest template

~~~json
{
  "run_id": "run-<YYYYMMDD>-<hhmm>-<short-hash>",
  "started_at": "<ISO8601>",
  "ended_at": "<ISO8601>",
  "pipeline_ref": "src/pipelines/<pipeline-name>@<commit>",
  "source_manifest_ref": "data/air-quality/ingestion/manifests/<source>.json",
  "inputs": [
    { "path": "data/raw/air-quality/…", "checksum_ref": "data/checksums/air-quality/…"}
  ],
  "outputs": [
    { "path": "data/processed/air-quality/…", "checksum_ref": "data/checksums/air-quality/…"}
  ],
  "stac_refs": [
    "data/stac/air-quality/…"
  ],
  "reports": [
    "data/reports/air-quality/…"
  ],
  "prov_bundle": "mcp/runs/<run_id>/prov.ttl"
}
~~~

### Recommended canonical fields for point observations

If the ingested Air Quality product is point-based (stations/sensors/monitors), the processed “observation” table SHOULD support, at minimum:

| Field | Required | Notes |
|---|---:|---|
| `observation_id` | ✅ | Stable ID, deterministic where possible (avoid random UUIDs) |
| `observed_at` | ✅ | ISO-8601 timestamp (UTC preferred) |
| `geometry` or `lat`/`lon` | ✅ | Point location; follow masking rules if sensitive |
| `parameter` | ✅ | Metric/pollutant name/code (define controlled vocab in domain notes) |
| `value` | ✅ | Numeric value |
| `unit` | ✅ | Unit string/code; document conversions |
| `qc_flag` | ⛔/✅ | Required if upstream provides QA flags; preserve upstream meaning |
| `source_id` | ✅ | Matches `source_manifest.source_id` |
| `ingest_run_id` | ✅ | Links to run manifest + PROV activity |

If you ingest gridded surfaces/rasters, document the grid specification (resolution, CRS, temporal aggregation) in `data/air-quality/ingestion/notes/`.

---

## 🌐 STAC, DCAT & PROV Alignment

This section describes how Air Quality ingestion outputs should map into the KFM catalog + provenance layers.

### Mapping overview

| Artifact | STAC | DCAT | PROV |
|---|---|---|---|
| Raw file(s) | STAC Item Asset (role: `raw`) or referenced via processing notes | `dcat:Distribution` (download URL + format) | `prov:Entity` |
| Processed dataset | STAC Item Asset (role: `data`) and/or Collection | `dcat:Dataset` + `dcat:Distribution` | `prov:Entity` |
| Ingestion run | N/A (tracked outside STAC) | N/A | `prov:Activity` |
| Pipeline maintainer/system | N/A | `dct:publisher` or `dct:creator` | `prov:Agent` |
| Validation report | Optional STAC Asset (role: `qa`) | Optional Distribution | `prov:Entity` derived from outputs |

### STAC notes for Air Quality assets

- Use STAC Collections to group a coherent Air Quality product (by source + product type).
- Use STAC Items to represent spatiotemporal slices (per day/hour/station/year), depending on the asset granularity.
- Assets should include stable roles such as `raw`, `data`, `qa`, and `metadata` (as applicable).

#### Minimal STAC Item skeleton (illustrative)

~~~json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "air-quality__<product>__<time-slice>__<region-or-station>",
  "properties": {
    "datetime": "<ISO8601>"
  },
  "geometry": { "type": "Point", "coordinates": [<lon>, <lat>] },
  "bbox": [<minLon>, <minLat>, <maxLon>, <maxLat>],
  "assets": {
    "data": {
      "href": "../../../data/processed/air-quality/…",
      "type": "text/csv",
      "roles": ["data"],
      "title": "Processed Air Quality Observations"
    },
    "raw": {
      "href": "../../../data/raw/air-quality/…",
      "roles": ["raw"],
      "title": "Upstream Raw Payload"
    }
  },
  "links": [
    { "rel": "collection", "href": "../collection.json" }
  ]
}
~~~

### DCAT notes for Air Quality datasets

- Use DCAT to describe the **dataset-level identity** (publisher, license, themes, spatial/temporal coverage).
- Use `dcat:distribution` for concrete downloadables (raw dumps, processed packages).
- If Air Quality is exposed as an API service, model it as `dcat:DataService` linked from the dataset.

### PROV notes for Air Quality ingestion

- Represent ingestion runs as `prov:Activity`.
- Represent raw/processed files and emitted STAC metadata as `prov:Entity`.
- Link `prov:used` (inputs) and `prov:wasGeneratedBy` (outputs), and include agent attribution.

#### Minimal PROV (Turtle) skeleton (illustrative)

~~~turtle
@prefix prov: <http://www.w3.org/ns/prov#> .

<urn:kfm:run:<run_id>> a prov:Activity ;
  prov:used <urn:kfm:entity:air-quality:raw:<raw_asset_id>> ;
  prov:generated <urn:kfm:entity:air-quality:processed:<processed_asset_id>> ;
  prov:wasAssociatedWith <urn:kfm:agent:pipeline:air-quality-ingestion> .

<urn:kfm:entity:air-quality:raw:<raw_asset_id>> a prov:Entity .
<urn:kfm:entity:air-quality:processed:<processed_asset_id>> a prov:Entity ;
  prov:wasDerivedFrom <urn:kfm:entity:air-quality:raw:<raw_asset_id>> .

<urn:kfm:agent:pipeline:air-quality-ingestion> a prov:Agent .
~~~

---

## 🧪 Validation & CI/CD

### Minimum validation set (run-time)

1. **Checksum generation/verification**
   - Every raw and processed artifact referenced by STAC or loaders must have a checksum entry.
2. **Schema validation for processed outputs**
   - Validate expected fields (time, geometry, parameter/value/unit).
3. **STAC validation**
   - Validate Collections/Items/Assets (schema + links + required fields).
4. **DCAT validation (if DCAT records are emitted)**
   - Validate dataset/distribution completeness and required fields.
5. **PROV sanity checks**
   - Ensure each run has a single `prov:Activity` and all referenced entities resolve.

### Where validators live

Prefer repo-owned validators (when present), typically under:
- `tools/validation/` (data + metadata validators)
- CI workflows under `.github/workflows/`

### CI expectations for this README

- Approved H2 headings only
- Directory tree fenced as `~~~text`
- Version history present
- Governance links present in footer

---

## 🧠 Story Node & Focus Mode Integration

Air Quality ingestion enables Story Nodes and Focus Mode only when evidence is traceable.

### Evidence requirements (for narrative use)

- Every map layer or chart used in a Story Node must link back to:
  - A **processed artifact** (or API distribution)
  - A **STAC record**
  - A **run provenance bundle** (PROV + run manifest)

### Safety constraints

- Do not fabricate relationships between datasets (“X derived from Y”) unless the PROV record explicitly encodes it.
- Do not override governance constraints (e.g., coordinate masking) in the name of narrative clarity.

---

## ⚖ FAIR+CARE & Governance

### Licensing and attribution

- Every source manifest MUST document the source license and publisher.
- If a source imposes downstream constraints (redistribution, attribution wording), capture it in the manifest and in the dataset-level catalog record.

### Sensitivity and masking

- Default to KFM’s masking rules when location precision could expose sensitive sites.
- If Indigenous data sovereignty or culturally sensitive contexts are implicated, follow:
  - `governance_ref`
  - `ethics_ref`
  - `sovereignty_policy`

### Human review triggers

Escalate to maintainers / governance review when:

- A new source has unclear licensing
- A dataset includes sensitive locations or restricted disclosures
- You need new ontology terms or graph relationships

---

## 🕰️ Version History

| Version | Date | Change | Author | Notes |
|---|---|---|---|---|
| v0.1.0 | 2025-12-16 | Initial Air Quality ingestion README (contract + layout + validation expectations) | Drafted for KFM | Human review recommended before “enforced” status |

---

<div align="center">

[📚 Docs Home](../../../docs/README.md) •
[🗃️ Data Home](../../README.md) •
[🏛️ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md) •
[⚖ FAIR+CARE Guidelines](../../../docs/standards/faircare/FAIRCARE-GUIDE.md) •
[🪶 Indigenous Data Protection](../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

</div>
