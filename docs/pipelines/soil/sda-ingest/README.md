---
title: "🧱 KFM v11.2.4 — SDA Soils Ingestion Pattern (Deterministic Chunked Pulls for Kansas SSURGO)"
path: "docs/pipelines/soil/sda-ingest/README.md"
version: "v11.2.4"
last_updated: "2025-12-06"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Soil Systems · FAIR+CARE Oversight"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x ingestion-contract compatible"
status: "Active / Enforced"

doc_kind: "Pattern"
intent: "soil-sda-ingest-pattern"
role: "soils-ingestion-contract"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "soils"
  applies_to:
    - "etl"
    - "stac"
    - "graph"
    - "api"
    - "provenance"
    - "telemetry"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "Low"
public_exposure_risk: "Low"
classification: "Public / Open Data (USDA-NRCS SDA)"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: false
risk_category: "Soils Ingestion"
redaction_required: false

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-commit-hash>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
telemetry_ref: "releases/v11.2.4/pipelines-soil-telemetry.json"
telemetry_schema: "schemas/telemetry/pipelines-soil-sda-v1.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/pipelines/soil/sda-ingest/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-pipelines-soil-sda-ingest-pattern-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-soil-sda-ingest-pattern-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:pipelines:soil:sda-ingest:pattern:v11.2.4"
semantic_document_id: "kfm-pipelines-soil-sda-ingest-pattern-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:soil:sda-ingest:pattern:v11.2.4"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-historical-claims"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🧭 Context"
    - "🧱 Architecture"
    - "📦 Data & Metadata"
    - "🧪 Validation & CI/CD"
    - "🗂️ Directory Layout"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"

diagram_profiles:
  - "mermaid-flowchart-v1"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "provenance-check"
  - "footer-check"
  - "accessibility-check"
  - "pattern-contract-check"

ci_integration:
  workflow: ".github/workflows/soil-sda-ingest-ci.yaml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Deterministic ETL × Open Soils Data × Sustainable Intelligence"
  architecture: "Chunked SDA Pulls · STAC/DCAT/PROV Ready"
  analysis: "Evidence-Led · Drift-Aware · FAIR+CARE Grounded"
  data-spec: "SSURGO/SDM × KFM Ontology"
  telemetry: "Soil Pipelines · Energy/Carbon · Reliability"
  graph: "Soil Units · Components · Place-Aware"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"

badge_profiles:
  - "root-centered-badge-row"

requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true

deprecated_fields: []
---

<div align="center">

# 🧱 **KFM v11.2.4 — SDA Soils Ingestion Pattern**  
**Deterministic Chunked Pulls for Kansas SSURGO via USDA Soil Data Access (SDA)**  
`docs/pipelines/soil/sda-ingest/README.md`

**Purpose:**  
Standardize a **deterministic, chunked ingestion pattern** for Kansas SSURGO/SDM soils from USDA SDA into KFM’s STAC/DCAT/PROV catalogs, Neo4j graph, and API layer — with WAL-safe resumes, geometry validation, drift detection, and full telemetry.

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode.

</div>

---

## 📘 Overview

This pattern defines how KFM ingests SSURGO/SDM soils data from **USDA Soil Data Access (SDA)** for Kansas:

- Deterministic, **chunked tabular + spatial** pulls from SDA.  
- Explicit handling of **SDA result size caps** (no silent truncation).  
- STAC/DCAT/PROV-ready snapshots for each run.  
- Canonical Neo4j graph mapping for soils entities and relationships.  
- Energy/carbon/reliability telemetry suitable for Autonomy Matrix and lineage audits.

Use this pattern for **any soils pipeline** that fetches data from SDA (R/`soilDB`, Python client, or direct HTTP) before publishing into KFM’s canonical STAC + graph layers.

---

## 🧭 Context

### SDA Within KFM

USDA Soil Data Access (SDA) is the authoritative service for SSURGO/SDM soils data. Within KFM:

- SDA is treated as an **external authoritative source**.  
- Ingested data is normalized into KFM’s:
  - **Data lake** (raw + processed).  
  - **STAC/DCAT catalogs** for discoverability.  
  - **Neo4j graph** for soils relationships and Story Node linkage.  

### Endpoint Types

KFM recognizes three SDA access modes:

- **Tabular REST**  
  - Endpoint: SDA `Tabular/post.rest` (HTTP POST).  
  - Payload: T-SQL query (`text/sql` or equivalent).  
  - Output: JSON with tabular results.

- **Spatial via tabular**  
  - Tables with geometry (e.g., `mupolygongeo`) expose WKT/WKB geometries to be normalized by KFM.

- **Spatial via WFS/WMS**  
  - Used for tiles / visualization; canonical storage & STAC come from tabular pulls, not WFS/WMS.

All KFM SDA ingestion must:

- Pin the exact endpoint base URL and API variant in **config**, not code.  
- Log the **T-SQL templates + parameter sets** in PROV.  
- Validate result sizes against SDA caps.

### Hard Limits (Pattern Assumptions)

The pattern assumes (and enforces):

- **≤ 100,000 rows per SDA query**.  
- **≤ ~32 MB JSON** per response.

These are treated as governed constraints:

- Hitting limits → **pipeline error** (not silent truncation).  
- Exceeding thresholds → chunk size must be reduced and rerun under **WAL-safe** logic.

---

## 🧱 Architecture

### Chunking Strategy (Deterministic & Resumable)

#### Chunk Identification

Standard chunk key options:

- Primary: `areasymbol` (all Kansas soil survey areas).  
- Alternative: `mukey` ranges or `cokey` ranges for finer control.

Pattern:

1. **Discover chunk universe** deterministically:  
   - Single SDA query lists all `areasymbol` for Kansas.  
   - Sort ascending; store manifest in `data/raw/soil/sda/chunk-manifests/`.  
2. Treat the manifest as **data**, not code:  
   - Versioned, checksummed, PROV-tracked.  
   - Used identically across re-runs and environments.

#### Tabular Query Templates

All SQL queries are **templates** parameterized by chunk key(s).

Example (components):

~~~text
SELECT c.*
FROM component c
JOIN mapunit mu ON c.mukey = mu.mukey
WHERE mu.areasymbol IN (@areasymbol_list);
~~~

Example (polygons):

~~~text
SELECT mu.mukey,
       mu.musym,
       mu.muname,
       mpg.WKT
FROM mupolygongeo AS mpg
JOIN mapunit AS mu
  ON mpg.mukey = mu.mukey
WHERE mu.areasymbol = @areasymbol;
~~~

Rules:

- The template ID is versioned and recorded in telemetry/PROV.  
- Changing the SQL template requires a **pipeline + dataset version bump**.  
- Chunk binding (e.g., `@areasymbol_list`) is deterministic and fully logged.

### WAL, Idempotency, and Resumes

For each chunk:

1. Log a WAL entry with:  
   - Chunk ID(s).  
   - SQL template ID + parameter set.  
   - Attempt number.  
2. Execute SDA POST; capture:  
   - HTTP status.  
   - Row count.  
   - Response size (bytes).  
3. Write raw JSON to `data/raw/soil/sda/tabular/…` with deterministic filenames:
   - Based on `chunk_id`, `query_kind`, `attempt`.  
4. On success:  
   - Mark chunk as **COMPLETE** in WAL.  
5. On failure:  
   - Apply bounded retry policy (e.g., deterministic retry loop pattern).  
   - Accept only **full**, validated results; no partial success.

Re-running the pipeline with the same configuration:

- Skips already-completed chunks (per WAL).  
- Reuses WAL state without corrupting history.  
- Produces identical processed outputs for identical SDA responses.

### Geometry & CRS Validation

All spatial outputs must be normalized to **EPSG:4326** for canonical KFM storage.

For each geometry:

- Ensure CRS is known and logged:
  - If table is in another CRS (e.g., Web Mercator), reproject to EPSG:4326.  
- Validate topology:
  - No self-intersections (within tolerance).  
  - Positive area (where applicable).  
- Enforce Kansas AOI clip:
  - Polygons must intersect the Kansas AOI geometry.  
  - Optional buffer for cross-border units.

Failure handling:

- **Hard failures** (run-level):  
  - Unknown CRS.  
  - Invalid WKT/WKB parse.  
  - > configurable fraction of geometries failing topology checks.  
- **Soft failures** (record-level):  
  - Individual geometry issues under threshold, logged in a **geometry QA report** per run.

### Drift Detection & Dataset Versioning

After each run, compute drift vs. previous successful run.

**Structural drift**:

- Schema changes:
  - Table presence/absence.  
  - Column additions/removals.  
  - Column type changes.  
- Policy:
  - Backward-compatible schema changes → minor dataset version bump.  
  - Breaking changes → major/mode bump + explicit migration docs.

**Content drift**:

- Row counts:
  - Per chunk, per table, and totals.  
- Key sets:
  - Ordered key lists (`mukey`, `cokey`, etc.) with SHA-256 digest.

Policy examples:

- Any change in **key hash** → dataset version bump.  
- Large swings in row counts → mark run as `drift-high` and trigger review.

### Integration into Neo4j & API

After validation:

1. Write processed tabular + spatial into canonical **Parquet/Feather** tables.  
2. Load into Neo4j with stable graph model:
   - `:SoilMapUnit {mukey, musym, muname, …}`  
   - `:SoilComponent {cokey, compname, …}`  
   - Relationships:
     - `(:SoilMapUnit)-[:HAS_COMPONENT]->(:SoilComponent)`  
     - Optional links to **Places** and **Story Nodes**.  
3. API layer exposes:
   - AOI queries (bounding box over Kansas).  
   - Attribute filters (e.g., `compname`, hydrologic group).  
   - Version-aware responses (dataset version, run_id, STAC item ID, SDA provenance summary).

---

## 📦 Data & Metadata

### STAC Collections & Items

For each successful SDA ingestion run:

- **Collection**: `soil-sda-ssurgo-kansas`  
  - Describes domain, CRS, temporal coverage, SDA endpoints, schemas.  

- **Items** (per run or per logical grouping):  
  - `properties.kfm:run_id`  
  - `properties.kfm:sda_sql_template_ids`  
  - `properties.kfm:chunk_manifest_version`  
  - `properties.kfm:row_counts` (per table/chunk)  
  - Asset links:
    - Raw SDA JSON.  
    - Processed tabular/spatial formats.  
    - Geometry QA reports.

### DCAT Alignment

DCAT dataset metadata wraps STAC:

- `dct:source` → SDA Soils Data Access service.  
- `dct:conformsTo` → SDA query contracts + KFM soils schemas.  
- `dcat:distribution` → STAC endpoints + raw/processed storage URIs.

### PROV-O Provenance

Each run is modeled as `prov:Activity`:

- `prov:used`:
  - SDA endpoint URIs.  
  - SQL templates.  
  - Chunk manifest.  
  - Previous dataset snapshot (for drift).  
- `prov:wasAssociatedWith`:
  - USDA NRCS SDA (external agent).  
  - KFM soil ETL pipeline (internal agent).  
- `prov:generated`:
  - Raw SDA snapshots.  
  - Processed tables.  
  - STAC collections & items.  
  - Neo4j ingests.  
  - QA & drift reports.

Location:

~~~text
data/lineage/soil/sda-ingest/<run_id>.prov.jsonld
~~~

### Telemetry, Energy, and Reliability

Each SDA ingestion run **must** emit a telemetry bundle, including:

- Core metrics:
  - `soil_sda_rows_total{table=…,run_id=…}`  
  - `soil_sda_chunks_completed_total{run_id=…}`  
  - `soil_sda_http_requests_total{endpoint=…,status=…}`  

- Reliability:
  - `soil_sda_retry_attempts_total{reason=…}`  
  - `soil_sda_run_outcome{status=success|partial|failed}`  

- Energy & carbon:
  - `soil_sda_energy_kwh{phase=extract|transform|stac|graph}`  
  - `soil_sda_carbon_kgco2e{phase=…}`  

- WAL & idempotency:
  - `soil_sda_wal_events_total{kind=write|replay|rollback}`  

Metric labels must follow **cardinality policy**:

- Use `run_id`, `chunk_index`, enums (e.g., `phase`, `status`).  
- Avoid embedding high-cardinality identifiers (no raw SQL, no full geometry IDs).

---

## 🧪 Validation & CI/CD

### Implementation Checklist

A soils SDA pipeline is **KFM-compliant** if:

- [ ] Uses this pattern’s directory layout (or a documented, versioned variant).  
- [ ] SDA queries are parameterized templates with versioned IDs.  
- [ ] Chunking is manifest-driven, WAL-logged, and resumable.  
- [ ] Per-chunk row counts and response sizes are logged and validated against caps.  
- [ ] Geometry CRS normalized to EPSG:4326 with QA checks and reports.  
- [ ] Drift detection (schema, keys, row counts) is implemented and version-aware.  
- [ ] STAC Collection + Items are written and pass validation.  
- [ ] PROV-O JSON-LD run logs are emitted and stored.  
- [ ] Telemetry (rows, chunks, retries, energy, carbon) is wired into KFM metrics.  
- [ ] Neo4j ingestion and API layer are version- and provenance-aware.

### CI Workflows

Example workflows:

- `soil-sda-ingest-ci.yaml`  
  - Schema and contract lint for configs and SQL templates.  
  - Unit tests for chunking and WAL behavior.  
  - STAC/DCAT/PROV validation.

- `soil-sda-ingest-telemetry.yaml`  
  - Validates telemetry schema (`pipelines-soil-sda-v1`).  
  - Enforces cardinality and label naming rules.

---

## 🗂️ Directory Layout

Canonical layout for SDA-based soils ingestion (emoji-prefixed):

~~~text
docs/
  pipelines/
    soil/
      sda-ingest/
        📄 README.md
        📂 runbooks/
        │  📄 weekly-refresh.md
        │  📄 drift-investigation.md
        📂 specs/
           📄 sda-query-contracts.md
           📄 chunking-policy.md

src/
  pipelines/
    soil/
      sda_ingest/
        📄 __init__.py
        📄 config.py
        📄 chunkspec.py
        📄 sda_client.py
        📄 etl_runner.py
        📄 validators.py
        📄 stac_writer.py
        📄 prov_writer.py
        📄 telemetry.py

data/
  raw/
    soil/
      sda/
        📂 tabular/
        📂 spatial/
        📂 chunk-manifests/
  processed/
    soil/
      ssurgo/
        📂 tabular/
        📂 spatial/
  stac/
    soil/
      sda-ssurgo/
        📂 collections/
        📂 items/

.github/
  workflows/
    📄 soil-sda-ingest-ci.yaml
    📄 soil-sda-ingest-telemetry.yaml
~~~

Rules:

- New SDA soils pipelines must map cleanly into this layout or clearly documented variants.  
- Docs under `sda-ingest/` must reference this pattern and stay MDP-aligned.  

---

## ⚖ FAIR+CARE & Governance

Even though SDA soils data is **public/open**, this pattern supports FAIR+CARE by:

- **FAIR**  
  - Stable identifiers, hash-based manifests, and catalog entries.  
  - Clear provenance (SDA as source, KFM as integrator).  
  - Standard STAC/DCAT/PROV representations.

- **CARE**  
  - Transparent documentation of how soils data is transformed and used.  
  - Clear separation of soils ingestion from any heritage/sensitive pipelines.  
  - Energy/carbon telemetry supporting responsible resource use in large ingests.

Governance hooks:

- Changes to SDA query templates, chunk policy, or geometry QA thresholds must:
  - Update this pattern or a referenced spec.  
  - Be reviewed by Soil Systems + FAIR+CARE oversight (when impacts propagate to sensitive overlays).  

---

## 🕰️ Version History

| Version   | Date       | Description                                               |
|----------:|------------|-----------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | Initial SDA soils ingestion pattern for Kansas SSURGO.   |

---

<div align="center">

🧱 **KFM v11.2.4 — SDA Soils Ingestion Pattern**  
Deterministic SDA Pulls · STAC/DCAT/PROV-Ready · Neo4j-Integrated  

[📘 Pipelines Index](../../README.md) · [🛰 Lineage Standard](../lineage/lineage-telemetry-standard.md) · [⚖ Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>