---
title: "🌱 KFM v11.2.3 — Weekly SDA + soilDB Soil Ingestion Pipeline (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Deterministic weekly ingestion of USDA NRCS SDA and soilDB-derived soil profiles into KFM soil STAC collections with WAL-safe upserts, diff-based batching, and full provenance."
path: "docs/pipelines/soil/sda-weekly/README.md"

version: "v11.2.3"
last_updated: "2025-12-04"
release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Soil Systems · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x ingestion-contract compatible"
status: "Active · Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../releases/v11.2.3/signature.sig"
attestation_ref: "../../../../releases/v11.2.3/slsa-attestation.json"
sbom_ref: "../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.3/soil-sda-weekly-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/soil-sda-weekly-v1.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Pipeline Specification"
intent: "soil-sda-soildb-weekly-ingestion"
category: "Pipelines · Soil Systems · SDA · soilDB"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
jurisdiction: "Kansas / United States"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
immutability_status: "version-pinned"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

ttl_policy: "24 Months"
sunset_policy: "Superseded by next major soil ingestion standard revision"

header_profile: "standard"
footer_profile: "standard"
---

<div align="center">

# 🌱 Weekly SDA + soilDB Soil Ingestion Pipeline

`docs/pipelines/soil/sda-weekly/README.md`

**Deterministic weekly synchronization of SDA and soilDB soil profiles into KFM’s soil STAC collections with WAL-safe upserts, diff-based batching, and full provenance.**

<img src="https://img.shields.io/badge/Docs-MCP--DL_v6.3-blue" />
<img src="https://img.shields.io/badge/Markdown-KFM--MDP_v11.2.3-purple" />
<img src="https://img.shields.io/badge/Data-FAIR%2BCARE-gold" />
<img src="https://img.shields.io/badge/Soil-SDA_%2B_soilDB-brown" />
<img src="https://img.shields.io/badge/Status-Active_%2F_Enforced-brightgreen" />

</div>

---

## 🧭 1. Purpose

The weekly SDA + soilDB ingestion pipeline synchronizes USDA NRCS **Soil Data Access (SDA)** and **soilDB-extracted** content into KFM’s soil STAC collections.

This pipeline exists to:

- Provide continuously updated **canonical soil data** for modeling, archaeology overlays, hydrology, ecology, land use, crop history, and Story Nodes.
- Maintain strict **provenance** through deterministic batching, revision hashing, and WAL-safe upserts.
- Detect and track changes in **mapunits, components, horizons, and ecological site descriptions**.
- Support FAIR+CARE-aligned, reproducible soil analyses across KFM.

---

## 🧱 2. Directory Layout (Emoji-Prefix Standard)

High-level governed layout for this pipeline’s documentation and artifacts:

    docs/pipelines/soil/sda-weekly/
    │
    ├── 📄 README.md                          # This file (pipeline specification)
    │
    ├── 📊 diffs/                             # Weekly change reports & key lists
    │   ├── 📄 weekly-diff-report.json        # Summary of SDA/soilDB deltas
    │   └── 📄 changed-keys.csv               # mukey / composite key changes
    │
    ├── 🧾 provenance/                        # Batch-level provenance summaries
    │   ├── 📁 batch-events/                  # PROV-O / event exports (by run)
    │   └── 📁 lineage-summaries/             # Human-readable lineage rollups
    │
    ├── ✅ validation/                        # Schema & quality checks
    │   ├── 📁 schema/                        # JSON Schemas, SHACL shapes
    │   └── 📁 reports/                       # Validation reports per run
    │
    ├── 🔁 transforms/                        # Conceptual & implementation docs
    │   ├── 📄 soil-normalization.md          # Units, vertical datum, horizons
    │   ├── 📄 ecological-site.md             # Ecological site description mapping
    │   └── 📄 taxonomic-lineage.md           # Taxonomic flattening rules
    │
    └── 🗂️ stac-output/                       # Example Items / references (doc only)
        └── 📄 README.md                      # Pointers into real STAC catalogs

Each subdirectory must provide a KFM-MDP-compliant README where applicable, pointing to operational locations (e.g., real STAC roots, telemetry, and lineage stores).

---

## 🌾 3. Data Sources

Authoritative sources and sinks involved in this pipeline:

| Source / Target                    | Access Method        | Frequency         | Role / Notes                                                                 |
|-----------------------------------|----------------------|-------------------|-------------------------------------------------------------------------------|
| USDA NRCS Soil Data Access (SDA)  | HTTPS SQL API        | Weekly (scheduled)| Authoritative schema tables, mukey/lkey revisions, and change timestamps.    |
| soilDB (R package)                | R interface → SDA    | Batch per run     | Retrieves full structured profiles (components, horizons, texture, ESD).     |
| KFM Soil STAC Catalog             | Local + remote STAC  | Continuous        | Destination for processed, validated STAC Items and collection updates.      |
| KFM Provenance Ledger             | Graph / PROV store   | Continuous        | Stores batch-level PROV-O Activities and Entities for soil ingestion.        |

---

## 🔁 4. Pipeline Flow (Conceptual)

High-level weekly run:

1. **Discovery**

   - Query SDA endpoint for `mukey` and `lkey` (or equivalent) **revision timestamps**.
   - Compare against KFM’s stored `last_ingested_rev_ts`.
   - Mark each unit as `clean`, `dirty`, or `failed` in the **Dirty Map**.

2. **Dirty Batching**

   - Collect only units with updated revision timestamps (`dirty`).
   - Batch into deterministic groups (e.g., 500–2,000 keys per batch).
   - Allow adaptive batching based on observed latency and error rates (configurable, not ad hoc).

3. **Fetch**

   - Use **soilDB** to retrieve structured profiles for each dirty key.
   - Standardize field names and ensure complete horizon/component tables.
   - Compute and store **input hashes** (e.g., SHA-256) for provenance and idempotency.

4. **Transform**

   - Convert fetched data into the **KFM soil schema**.
   - Apply:
     - Unit conversions (depth, density, etc.).
     - Vertical datum normalization.
     - Taxonomic flattening and lineage encoding.
   - Enforce required metadata:
     - Geometry (where available).
     - Mapunit description.
     - Revision timestamp.
     - Lineage hash (combined from source fields).

5. **Validate**

   - Run JSON Schema / SHACL validation.
   - Enforce completeness for horizons and texture fields.
   - Optionally run **spatial plausibility checks** (e.g., bounds, overlaps with state extent).

6. **Upsert (WAL-Safe)**

   - Write a **WAL entry** describing the proposed changes.
   - Perform idempotent upserts to KFM soil STAC Items and collections.
   - Mark keys as successfully ingested (`clean`) or in error (`failed`).
   - Emit batch-level PROV events.

7. **Publish & Notify**

   - Attach Items to appropriate soil STAC collections or sub-collections.
   - Trigger optional model refresh or downstream analysis tasks.
   - Emit telemetry spans/metrics and, if configured, notifications to monitoring channels.

---

## 🧮 5. Data Structures

### 5.1 Dirty Map Table (Conceptual)

Tracks state for each soil unit key (e.g., `mukey` or composite identifiers).

| Field                | Type       | Description                                      |
|----------------------|-----------|--------------------------------------------------|
| key                  | TEXT      | `mukey` or composite soil identifier             |
| last_seen_rev_ts     | TIMESTAMP | Latest SDA revision timestamp seen               |
| last_ingested_rev_ts | TIMESTAMP | Last successfully processed revision             |
| last_job_id          | TEXT      | Identifier of the last processing run            |
| status               | ENUM      | `clean`, `dirty`, `failed`                       |

**Rules:**

- `status = dirty` → must be included in the next eligible batch.
- `status = failed` → must be queued for retry with explicit reason recorded.
- `last_ingested_rev_ts` must **never** exceed `last_seen_rev_ts`.

### 5.2 STAC Item Fields (Mandatory Soil Fields)

Each soil STAC Item produced by this pipeline **must** include:

- `id` (canonical, deterministic key).
- `geometry` (where spatial representation is known).
- `properties.revision` (SDA/soilDB revision or derived timestamp).
- `properties.source_hash` (hash of source record or record set).
- `properties.ingest_timestamp` (pipeline ingest time, RFC3339).
- Soil profile JSON (components, horizons, texture, etc.).
- Attachments:
  - Ecological site description.
  - Taxonomic lineage / classification fields.
  - Optional derived metrics (e.g., depth-normalized aggregates) with provenance.

---

## 🧬 6. Provenance Model (PROV-O)

Each ingestion batch creates a set of **PROV-O Activities and Entities**.

### 6.1 Activities (Examples)

- `soil.sda.revision-check`  
  - Queries SDA for revision changes.
- `soil.sda.fetch`  
  - Retrieves SDA-level records for targeted keys.
- `soil.soildb.transform`  
  - Applies soilDB-based transformations and KFM soil schema normalization.
- `soil.stac.upsert`  
  - Upserts STAC Items and collections, WAL-backed.

### 6.2 Entities

- **Source SDA record** (`prov:Entity`)
- **soilDB structured profile** (`prov:Entity`)
- **Final STAC Item** (`prov:Entity`)
- **Dirty Map snapshot** (`prov:Entity`) for the batch.

Relationships:

- `prov:wasDerivedFrom`  
  SDA record → soilDB profile → STAC Item.
- `prov:used`  
  Activities use prior Entities (e.g., Dirty Map snapshot, WAL entries).
- `prov:wasAssociatedWith`  
  Activities are associated with the soil ingestion service / operator Agent.

Hash-based lineage:

- Combined **source hashes** and **transform hashes** are used to generate a **certainty score** and ensure re-runs generate identical provenance graphs.

---

## 🛡️ 7. Reliability & Determinism

Reliability constraints for this pipeline:

- **Bounded retries** for SDA/soilDB calls with deterministic backoff.
- **Transactional upsert with rollback**:
  - If any checksum or validation mismatch occurs, the WAL entry is rolled back and the affected keys remain `dirty` or become `failed`.
- **Retry queue** for failed keys:
  - Keys are not dropped; they are retried according to configurable policies.
- **Safety switch**:
  - Ingest pauses automatically if a batch exceeds a failure threshold (e.g., ≥ X% failures) and raises a governance/ops alert.

Determinism:

- Given the same SDA/soilDB inputs and configuration:
  - Batches, STAC Items, PROV-O graphs, and telemetry **must** be reproducible.
- Randomness (if any) must be seeded and documented; preferably avoided in this pipeline.

---

## 📊 8. Telemetry & Metrics

Minimum metrics to be captured and exported via OpenTelemetry:

- `soil.sda_weekly.items_updated` — Count of Items updated in the run.
- `soil.sda_weekly.revision_delta` — Number of SDA units marked `dirty`.
- `soil.sda_weekly.soildb_fetch_latency` — Latency distribution for soilDB fetches.
- `soil.sda_weekly.hash_mismatches` — Count of source vs stored hash mismatches.
- `soil.sda_weekly.validation_errors` — Count and rate of schema/quality failures.
- `soil.sda_weekly.stac_publish_duration` — Time to register Items in STAC.
- `soil.sda_weekly.energy_kwh` — Estimated energy usage per run (if enabled).
- `soil.sda_weekly.cost_estimate` — Cloud cost estimate per run (if enabled).

Telemetry MUST:

- Be documented under `telemetry_schema`.
- Respect cardinality constraints (e.g., avoid high-cardinality labels on keys).
- Feed into soil system SLOs and error budget policies (e.g., maximum acceptable validation error rate).

---

## 🌱 9. Future Extensions

Planned and supported extension points:

- Integration with **gNATSGO annual refresh** for deeper profile consistency.
- Inclusion of **soil moisture, EC, and correlative remote sensing layers** (e.g., Sentinel, Landsat-derived indices).
- **AI-assisted horizon classification** to standardize horizon labels across datasets.
- **H3-indexed derived soil generalization layers** for privacy-preserving spatial summaries.
- Tight coupling with **cultural landscape archaeology modules** to link soil properties, land use, and archaeological context.

All extensions must:

- Maintain deterministic, provenance-aware behavior.
- Be documented in `transforms/` and associated schemas.
- Respect FAIR+CARE and sovereignty constraints.

---

## 🧾 10. Summary

This weekly ingestion pipeline provides KFM with a **reliable, scalable, and provenance-aware** mechanism for maintaining up-to-date soil datasets.

It:

- Reduces workloads via **revision-aware diffing** and **dirty batching**.
- Ensures **idempotent transformations** and **retry-safe ingestion**.
- Produces **standardized STAC Items** with strong integrity and lineage metadata.
- Supplies high-quality soil data for **hydrology**, **ecology**, **agriculture**, **archaeology**, and **Story Nodes** across KFM.

---

## 🕰 11. Version History

| Version  | Date       | Summary                                                                                       |
|---------:|------------|-----------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | First KFM-MDP v11.2.3-aligned spec; emoji directory layout; telemetry + provenance sections. |
| v11.2.2  | 2025-11-20 | Refined diff-based batching and dirty-map semantics; added WAL replay semantics.             |
| v11.2.1  | 2025-11-10 | Initial formalization of weekly SDA + soilDB ingestion flow and data structures.             |

---

<div align="center">

### 🌱 Weekly SDA + soilDB Soil Ingestion Pipeline · KFM v11.2.3

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[📚 Soil Systems Index](../README.md) ·  
[🗂 Data Contracts (Soils)](../../../../docs/data/README.md) ·  
[⚖ Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>