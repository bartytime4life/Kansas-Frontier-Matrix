---
title: "Kansas Frontier Matrix – Historical Data Domain"
path: "data/historical/README.md"
version: "v11.2.6"
last_updated: "2025-12-11"

doc_kind: "data-domain-index"
lifecycle: "active"
release_stage: "stable"
owner_team: "kfm-data-historical"
contact: "data-historical@kfm.example.org"

domain: "historical"
domain_scope:
  spatial: "Kansas and immediately adjacent regions"
  temporal: "Pre-contact through present, with emphasis on historical-period change"
  includes:
    - "historical events and periods"
    - "land tenure, treaties, and jurisdictional change"
    - "historic infrastructure and land use"
    - "demography and administrative units"
    - "historic maps, atlases, registers, and newspapers"
  excludes:
    - "purely modern sensor streams (see data/sensing)"
    - "purely ecological baselines (see data/ecology)"

markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
catalog_profile:
  stac: "KFM-STAC v11"
  dcat: "KFM-DCAT v11"
  prov: "KFM-PROV v11"

fair_label: "FAIR: F1-A1-I1-R1"
care_label: "CARE-aware: historical and Indigenous content"
sensitivity_default: "assess-per-dataset"

telemetry_ref: "../../mcp/telemetry/data-historical-domain.json"
governance_refs:
  data_governance: "../../docs/standards/governance/DATA-GOVERNANCE.md"
  indigenous_data: "../../docs/standards/governance/INDIGENOUS-DATA-GUIDE.md"
  security_policy: "../../docs/standards/security/SECURITY-POLICY.md"

doc_id: "urn:kfm:doc:data-historical-readme:v11.2.6"
previous_version: "v11.2.5"
change_request: "CR-HIST-001"
---

# Historical Data Domain (data/historical)

## 1. Purpose and role in the KFM pipeline

This README is the **entry point** for everything under `data/historical/`. It describes how historical data is expected to flow through the standard Kansas Frontier Matrix pipeline:

Deterministic ETL  
→ STAC / DCAT / PROV catalogs  
→ Neo4j graph  
→ API layer  
→ React / MapLibre / Cesium frontends  
→ Story Nodes and Focus Mode.

Every new dataset or subdirectory under `data/historical/` must:

- Declare how it fits into this pipeline.
- Provide STAC, DCAT, and PROV metadata.
- Integrate with the historical section of the Neo4j graph using the KFM-OP ontology.
- Respect FAIR+CARE principles and relevant sovereignty and sensitivity rules.

This document is intentionally generic; specific datasets and subdomains add their own README files, which **must reference this one** as their parent domain spec.

---

## 2. Directory layout and subdomains

The historical domain is organized by **theme** rather than by source. This section defines the target layout; some directories may be planned but not yet present.

~~~text
data/
  historical/
    README.md                     # This file – domain index and governance
    land-tenure/                  # Treaties, jurisdiction, land allocations (existing/planned)
      README.md
      raw/                        # As-ingested source materials
      work/                       # Normalized / intermediate
      processed/                  # Ready-for-catalog and graph ingestion
      stac/                       # STAC Collections and Items
        collections/
        items/
      dcat-prov/                  # DCAT dataset descriptions and PROV bundles
        dcat/
        prov/
    events/                       # Historical events, periods, and timelines (planned)
      README.md
    infrastructure/               # Rail, roads, canals, utilities, etc. (planned)
      README.md
    demography/                   # Census extracts, population time series (planned)
      README.md
    maps-atlases/                 # Historic maps, atlases, plats (planned)
      README.md
    newspapers-gazetteers/        # Indexes to newspapers, gazetteers (planned)
      README.md
    oral-histories/               # Historical oral history with special protections (planned)
      README.md
~~~

Conventions:

- Each thematic subdirectory must have its own `README.md` aligned with KFM-MDP v11.2.6.
- The `raw / work / processed` pattern is mandatory where ETL is involved.
- STAC / DCAT / PROV folders are required for any dataset that is published beyond private scratch use.

If a dataset does not yet fit this structure, it should live in a clearly marked temporary area (e.g. `data/historical/_staging`) with an issue tracking the work to bring it into compliance.

---

## 3. Expected data types and examples (non-exhaustive)

This domain includes, but is not limited to, the following categories of data. The examples are **types**, not specific datasets:

- **Land tenure and jurisdiction**
  - Historical county and township boundaries.
  - Administrative regions (territories, reservations, municipalities) over time.
  - Records of boundary changes, annexations, and reclassifications.
- **Treaties and legal-historical instruments**
  - Spatial representations of jurisdictional effects where modeling is appropriate and lawful.
  - Structured representations of articles, effective dates, and parties.
- **Historical events and periods**
  - Dated events with spatial extents (points, lines, polygons).
  - Named periods with time spans and associated places.
- **Infrastructure and land use**
  - Historic transportation networks (rail, roads, trails).
  - Major public works with known construction and decommission dates.
- **Demography**
  - Aggregated census units, population counts, and demographic indicators.
- **Maps and atlases**
  - Georeferenced historic map sheets and atlases.
  - Vectorized features derived from those sources where allowed.
- **Newspapers and gazetteers**
  - Indexes of articles and notices with place and time references (not full text reproduction).
- **Oral histories**
  - Time-anchored narratives, usually with non-public detail and stronger sovereignty constraints.

Each concrete dataset must document its own scope, methods, and limitations.

---

## 4. ETL expectations (Deterministic and config-driven)

Historical ETL logic lives under `src/pipelines/historical/` and must be:

- **Deterministic**  
  - No hidden randomness; any stochastic step must set and record a seed.
- **Config-driven**  
  - Config files under `configs/historical/` describe sources, transformations, CRS, time handling, and sensitivity rules.
- **Layered**  
  - ETL outputs map to `raw → work → processed` in this directory tree.

Minimum expectations for any ETL touching `data/historical`:

- A config file (e.g. `configs/historical/<theme>-etl.yaml`).
- A reproducible run command documented in the dataset-level README (e.g. `make etl-historical-<theme>`).
- A log of the most recent runs under `mcp/experiments/historical/`.
- Clear, stable identifiers in outputs so STAC / DCAT / PROV and the graph can reference them.

---

## 5. Catalogs: STAC, DCAT, and PROV

Every dataset under `data/historical/` that is exposed to the graph or APIs must have:

### 5.1 STAC

- At least one **STAC Collection** per thematic grouping or series.
- One or more **STAC Items** per spatiotemporally distinct asset (e.g., a specific boundary realization, a map sheet, an event layer).
- Conformance to the KFM STAC profile, including:
  - `id`, `title`, `description`, `license`, `providers`, `extent`, and `keywords`.
  - Spatial and temporal extent expressed in EPSG:4326 and ISO-8601.
  - Properties for:
    - Sensitivity flags.
    - Relevant governance or sovereignty tags where required.

### 5.2 DCAT

- One **DCAT dataset description** per dataset.
- DCAT must describe:
  - Title, description, publisher/maintainer.
  - Spatial and temporal coverage.
  - License and access level.
  - Contact and usage notes.
- DCAT files for historical datasets are written to  
  `data/historical/<theme>/dcat-prov/dcat/`.

### 5.3 PROV

- One or more **PROV bundles** per ETL or curation flow.
- Each bundle identifies:
  - **Entities**: source files, intermediate layers, final products.
  - **Activities**: ETL runs, manual curation steps, quality review.
  - **Agents**: individuals, teams, automated systems.
- PROV files are written to  
  `data/historical/<theme>/dcat-prov/prov/` and must be valid JSON-LD.

---

## 6. Graph integration (Neo4j)

Historical data is integrated into the KFM Neo4j graph via ingestion code in `src/graph/historical/`. The exact labels and relationships are defined in the KFM-OP ontology and associated schema files, but the following general patterns apply:

- Nodes (examples of **types**, not a full schema):
  - `:HistoricalEvent`, `:Period`, `:Place`, `:AdministrativeUnit`
  - `:BoundaryVersion`, `:Dataset`, `:SourceDocument`
- Relationships (examples):
  - `(:HistoricalEvent)-[:OCCURRED_IN]->(:Place)`
  - `(:BoundaryVersion)-[:VALID_DURING]->(:Period)`
  - `(:Dataset)-[:DERIVES_FROM]->(:SourceDocument)`
  - `(:Dataset)-[:IMPLEMENTS]->(:Specification)` for formally defined models.

Any new graph integration must:

- Use stable identifiers derived from STAC / DCAT IDs, not ad-hoc strings.
- Declare its schema in the appropriate ontology or schema file before ingestion runs in CI.
- Include tests under `src/graph/historical/tests/` that exercise typical queries used by APIs and Story Nodes.

If a historical dataset is **not** intended for graph ingestion, that must be stated explicitly in the dataset README, along with the reason.

---

## 7. Story Nodes and Focus Mode

Historical data often drives Story Nodes and Focus Mode views. For each major dataset or grouping, authors should plan for at least one Story Node that:

- Has a stable ID and lives under `docs/story/historical/`.
- Clearly separates:
  - **Facts** supported directly by data (with references to STAC/DCAT/graph).
  - **Interpretation** (reasoned narrative).
  - **Speculation** (clearly labeled as such, or omitted).
- Records:
  - Spatial extent (bbox or named places).
  - Temporal extent (start / end dates).
  - Links to:
    - Relevant STAC Collections or Items.
    - DCAT datasets.
    - Graph entities (e.g., key places, events, boundaries).

This README does not define Story Node content, but any Story Node in the historical domain should reference this file to document its data dependencies and constraints.

---

## 8. FAIR, CARE, sovereignty, and sensitivity

Historical data for Kansas can include:

- Information about Indigenous nations and communities.
- Locations of cemeteries, burial sites, and sacred or sensitive places.
- Records of conflict, displacement, or other traumatic events.

For this reason:

- **FAIR** principles must be followed in terms of metadata, formats, and provenance.
- **CARE** and related sovereignty principles must be applied, especially when:
  - Publishing spatial detail for sensitive locations.
  - Representing historical narratives that affect living communities.
  - Handling oral histories and community-held knowledge.

Concrete requirements for this domain:

- Each dataset must declare:
  - Its sensitivity level and access policy.
  - Whether it includes content related to Indigenous communities, and if so, how authority and governance are handled.
- Where necessary, public layers must:
  - Generalize, buffer, or omit precise geometries.
  - Provide metadata-only entries when full data cannot be made open.
- Governance decisions must be documented and linked from:
  - The dataset-level README.
  - The DCAT record (`rights`, `accessLevel`, and related fields).

If there is uncertainty about how to handle a dataset, the default is **conservative**: treat it as sensitive and seek guidance via the governance process before publication.

---

## 9. CI, validation, and quality gates

Changes under `data/historical/` are subject to the normal KFM CI pipelines. At minimum, historical datasets must pass:

- **Markdown checks** for this README and sub-READMEs.
- **Schema checks** for:
  - STAC Collections and Items.
  - DCAT datasets.
  - PROV bundles.
- **Data integrity checks**:
  - Checksums where defined (e.g., `data/checksums/`).
  - CRS and geometry validity for spatial layers.
- **Graph integration tests** for any dataset that is ingested.
- **Governance checks**:
  - Presence of required metadata fields for sensitivity and rights.
  - No disallowed fields or accidental exposure of sensitive coordinates where they must be generalized.

No dataset in this domain is to be considered **production-ready** until it clears these gates.

---

## 10. Next steps and typical follow-up work

When adding or modifying historical data, typical next steps are:

1. Create or update the subdomain README (e.g., `data/historical/land-tenure/README.md`) referencing this document.
2. Define ETL configs under `configs/historical/`.
3. Implement or update ETL code under `src/pipelines/historical/`.
4. Generate and validate STAC / DCAT / PROV metadata.
5. Wire up graph ingestion and tests under `src/graph/historical/`.
6. Update or create Story Nodes under `docs/story/historical/` if appropriate.
7. Ensure CI passes and governance approvals are recorded.

Each of these steps should be tracked by issues or pull requests referencing this README.

---

## 11. Version history

- **v11.2.6 (2025-12-11)**  
  - Rewritten domain README to be concise and pipeline-focused.  
  - Clarified directory layout as a target structure and marked several subdomains as planned.  
  - Strengthened explicit ties to ETL configs, STAC/DCAT/PROV, Neo4j, and Story Nodes.  
  - Made FAIR/CARE, sovereignty, and sensitivity handling explicit but dataset-agnostic.

---

Back links:

- Data index: `data/README.md`  
- Architecture overview: `docs/architecture/README.md`  
- Data governance: `docs/standards/governance/DATA-GOVERNANCE.md`