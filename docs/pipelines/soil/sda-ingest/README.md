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
classification: "Public / Open Data (USDA-NRCS SDA)"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-commit-hash>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.4/pipelines-soil-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/pipelines-soil-sda-v1.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
---

# 🧱 SDA Soils Ingestion Pattern  
**Deterministic Chunked Pulls for Kansas SSURGO via USDA Soil Data Access (SDA)**  

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode.

---

## 1. Purpose & Scope

This pattern standardizes how KFM ingests SSURGO/SDM soils data from USDA **Soil Data Access (SDA)** for Kansas:

- Deterministic, chunked **tabular + spatial** pulls
- Hard-limit safe (SDA result size caps)
- STAC/DCAT/PROV-ready snapshots
- Neo4j graph mapping and geometry validation
- Energy/carbon/reliability telemetry for each run

Use this pattern for **any soils pipeline** that fetches data from SDA (R/`soilDB`, Python, or direct HTTP) before publishing into KFM’s canonical STAC + graph layers.

---

## 2. Directory Layout (Pattern-Conformant)

The canonical layout for SDA-based soils ingestion:

    docs/
      pipelines/
        soil/
          sda-ingest/
            README.md
            runbooks/
              weekly-refresh.md
              drift-investigation.md
            specs/
              sda-query-contracts.md
              chunking-policy.md

    src/
      pipelines/
        soil/
          sda_ingest/
            __init__.py
            config.py
            chunkspec.py
            sda_client.py
            etl_runner.py
            validators.py
            stac_writer.py
            prov_writer.py
            telemetry.py

    data/
      raw/
        soil/
          sda/
            tabular/
            spatial/
      processed/
        soil/
          ssurgo/
            tabular/
            spatial/
      stac/
        soil/
          sda-ssurgo/
            collections/
            items/

    .github/
      workflows/
        soil-sda-ingest-ci.yaml
        soil-sda-ingest-telemetry.yaml

Any new SDA soils pipeline **must** map cleanly into this layout (or a documented, versioned variant) and link back to this pattern.

---

## 3. SDA Overview (Within KFM Constraints)

### 3.1 Endpoint Types

KFM recognizes three SDA access modes:

- **Tabular REST**  
  - Endpoint: SDA `Tabular/post.rest` (HTTP POST)  
  - Payload: T-SQL query (`text/sql` or equivalent)  
  - Output: JSON with tabular results

- **Spatial via tabular**  
  - Tables with geometry (e.g., `mupolygongeo`) for WKT/WKB geometries

- **Spatial via WFS/WMS**  
  - Used for tiles/visual layers; canonical storage & STAC come from tabular pulls

All KFM SDA ingestion **must**:

- Pin the exact endpoint base URL and API variant in config
- Log the **full T-SQL** (or templated T-SQL + parameters) in PROV
- Validate result sizes against SDA caps

### 3.2 Hard Limits (Pattern Assumptions)

We assume:

- **≤ 100,000 rows per SDA query**
- **≤ ~32 MB JSON** per response

These are treated as **governed constraints**:

- Hitting limits → pipeline error (not silent truncation)
- Exceeding thresholds → chunk size must be reduced and re-run using WAL-safe logic

---

## 4. Chunking Strategy (Deterministic & Resumable)

### 4.1 Chunk Identification

Standard chunk key options:

- Primary: `areasymbol` (e.g., all Kansas soil survey areas)
- Alternative: `mukey` ranges or `cokey` ranges for more granular control

Pattern:

1. **Discover chunk universe** deterministically:
   - Single SDA query to list all `areasymbol` in Kansas
   - Sort ascending, store as a manifest in `data/raw/soil/sda/chunk-manifests/`
2. Treat the chunk manifest as **input data**, not code:
   - Versioned
   - Has PROV entity entry
   - Has checksum logged in the run metadata

### 4.2 Tabular Example (Indented SQL)

All SQL queries are **templates** parameterized by chunk key(s). Example:

    SELECT c.*
    FROM component c
    JOIN mapunit mu ON c.mukey = mu.mukey
    WHERE mu.areasymbol IN (@areasymbol_list);

And for polygons:

    SELECT mu.mukey,
           mu.musym,
           mu.muname,
           mpg.WKT
    FROM mupolygongeo AS mpg
    JOIN mapunit AS mu
      ON mpg.mukey = mu.mukey
    WHERE mu.areasymbol = @areasymbol;

The pipeline:

- Binds a **concrete @areasymbol_list** (e.g., 10 areas) per chunk
- Never changes the SQL template without bumping pipeline & dataset versions

### 4.3 WAL, Idempotency, and Resumes

For each chunk:

1. Log a WAL entry with:
   - Chunk ID(s)
   - SQL template ID + parameter set
   - Attempt number
2. Execute SDA POST; capture:
   - HTTP status
   - Row count
   - Response size (bytes)
3. Write the raw JSON response to `data/raw/soil/sda/tabular/…` with:
   - Deterministic filename (chunk + query kind + attempt)
4. If success:
   - Mark chunk as **completed** in WAL
5. If failure:
   - Retry within bounded policy
   - Only proceed on full success; **no partial acceptance**

Re-running the pipeline with the same configuration:

- Skips already-completed chunks
- Reuses WAL state
- Produces identical processed outputs given identical SDA responses

---

## 5. Geometry & CRS Validation

All spatial outputs must be normalized to **EPSG:4326** for canonical KFM storage.

### 5.1 Validation Rules

For each geometry:

- Ensure CRS known and logged:
  - If table is in Web Mercator: must reproject to EPSG:4326
- Validate topology:
  - No self-intersections (configurable tolerance)
  - Positive area (or valid linestring/point, depending on geometry type)
- Enforce AOI (Kansas) clip:
  - Polygons must intersect Kansas AOI geometry
  - Optional border-buffer handling for cross-border units

### 5.2 Failure Handling

- Hard failures:
  - Unknown CRS
  - Invalid WKT/WKB parse
  - > configurable fraction of geometries failing topology checks
- Soft failures (record + flag):
  - Individual geometry issues under threshold
  - These are logged in a **geometry QA report** stored with each run

---

## 6. Drift Detection & Dataset Versioning

After each run, compute drift compared to previous successful run:

### 6.1 Structural Drift

- Schema:
  - Table presence / absence
  - Column additions/removals
  - Column type changes
- Policy:
  - Backward-compatible changes → minor version bump
  - Breaking changes → major/minor bump + explicit migration docs

### 6.2 Content Drift

- Row counts:
  - Per chunk
  - Totals per table
- Key sets:
  - Canonical ordered list of keys (`mukey`, `cokey`, etc.)
  - Hash (e.g., SHA-256) stored in telemetry/provenance

Policy examples:

- Any change in **key hash** → dataset version bump
- Large swings in row counts → mark run as “drift-high” and trigger review workflow

---

## 7. STAC / DCAT / PROV Mapping

### 7.1 STAC Collections & Items

For each successful SDA ingestion run:

- **Collection**: `soil-sda-ssurgo-kansas`
  - Describes domain, CRS, temporal coverage, SDA endpoints, and schemas
- **Items**:
  - One per run (or per major chunk grouping) with:
    - `properties.kfm:run_id`
    - `properties.kfm:sda_sql_template_ids`
    - `properties.kfm:chunk_manifest_version`
    - `properties.kfm:row_counts` (per table)
    - Links to:
      - Raw SDA JSON
      - Processed tabular/spatial formats
      - Geometry QA reports

### 7.2 DCAT Alignment

DCAT dataset metadata wraps STAC Collections:

- `dct:source` → SDA Soils Data Access service
- `dct:conformsTo` → SDA query contract doc + KFM soils schemas
- `dcat:distribution` → STAC endpoints + raw/processed storage locations

### 7.3 PROV-O Provenance

Each run is a `prov:Activity`:

- `prov:used`:
  - SDA endpoint URIs
  - SQL templates
  - Chunk manifest
  - Previous dataset snapshot (for drift comparisons)
- `prov:wasAssociatedWith`:
  - USDA NRCS SDA (external agent)
  - KFM soil ETL pipeline (internal agent)
- `prov:generated`:
  - Raw SDA snapshots
  - Processed tables
  - STAC collections & items
  - Neo4j ingests
  - QA & drift reports

All PROV logs are emitted as JSON-LD and stored under:

    data/lineage/soil/sda-ingest/<run-id>.prov.jsonld

---

## 8. Telemetry, Energy, and Reliability

Each SDA ingestion run **must** emit a telemetry bundle:

- Core metrics:
  - `soil_sda_rows_total{table=…,run_id=…}`
  - `soil_sda_chunks_completed_total{run_id=…}`
  - `soil_sda_http_requests_total{endpoint=…,status=…}`
- Reliability:
  - `soil_sda_retry_attempts_total{reason=…}`
  - `soil_sda_run_outcome{status=success|partial|failed}`
- Energy & carbon:
  - `soil_sda_energy_kwh{phase=extract|transform|stac|graph}`
  - `soil_sda_carbon_kgco2e{phase=…}` (with region factor link in metadata)
- WAL & idempotency:
  - `soil_sda_wal_events_total{kind=write|replay|rollback}`

Metric label sets must follow KFM **cardinality policy** (no unbounded IDs; use run_id, chunk_index, and enumerated enums only).

---

## 9. Integration into Neo4j & API

After validation:

1. Write processed tabular + spatial into **canonical parquet/feather** tables.
2. Load into Neo4j with stable graph model:
   - `:SoilMapUnit {mukey, musym, muname, …}`
   - `:SoilComponent {cokey, compname, …}`
   - Relationships:
     - `(:SoilMapUnit)-[:HAS_COMPONENT]->(:SoilComponent)`
     - Optional links to **Story Nodes** and **Places** layers.
3. API layer exposes:
   - Bounding box queries over Kansas AOI
   - Attribute-based filters (e.g., `compname`, hydrologic group)
   - Time-scoped views by dataset version / run_id

All API responses must reference:

- STAC item ID
- Dataset version
- SDA provenance summary

---

## 10. Implementation Checklist

Before declaring a soils SDA pipeline **KFM-compliant**, confirm:

- [ ] Uses this doc’s directory layout (or a documented, versioned variant)
- [ ] All SDA queries are parameterized templates with versioned IDs
- [ ] Chunking is manifest-driven, WAL-logged, and resumable
- [ ] Per-chunk row counts and response sizes are logged and checked
- [ ] Geometry CRS is normalized to EPSG:4326 with QA checks
- [ ] Drift detection (schema + keys + row counts) is implemented
- [ ] STAC Collection + Items written and validated
- [ ] PROV-O JSON-LD run logs emitted
- [ ] Telemetry (rows, chunks, retries, energy, carbon) is wired to KFM metrics
- [ ] Neo4j ingestion and API layer are version-aware and provenance-aware

---

## 11. Version History

| Version   | Date       | Description                                                |
|----------:|-----------:|------------------------------------------------------------|
| v11.2.4   | 2025-12-06 | Initial SDA soils ingestion pattern for Kansas SSURGO     |

---

## 12. Footer

- KFM Root Documentation Index: `../../../README.md`  
- KFM Governance Root: `../../../standards/governance/ROOT-GOVERNANCE.md`  
- KFM Markdown Protocol v11.2.4: `../../../standards/kfm_markdown_protocol_v11.2.4.md`  

--- 