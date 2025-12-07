---
title: "🚦 KFM v11.2.4 — Event‑Driven Deterministic Ingestion & Promotion Pattern (Idempotent · WAL‑Safe · FAIR+CARE)"
path: "docs/pipelines/patterns/event-driven-deterministic-ingest.md"
version: "v11.2.4"
last_updated: "2025-12-07"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability + FAIR+CARE Councils"
content_stability: "stable"
backward_compatibility: "Backward compatible with v11.0.x patterns"

status: "Active / Enforced"
doc_kind: "Pattern"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-commit-hash-or-null>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
telemetry_ref: "releases/v11.2.4/patterns-telemetry.json"
telemetry_schema: "schemas/telemetry/patterns-event-driven-v1.json"
governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-compliant (auto-mask on)"
sensitivity: "Mixed (enable dynamic generalization & tribal review)"
classification: "Public / Internal (feature-flag cutover)"

provenance_chain:
  - "docs/standards/kfm_markdown_protocol_v11.2.4.md@v11.2.4"
  - "docs/pipelines/patterns/run-state/README.md@v11.2.4"
  - "docs/standards/lineage/openlineage-ci-integration.md@v11.2.4"

doc_uuid: "urn:kfm:doc:pipelines:patterns:event-driven-deterministic-ingest:v11.2.4"

test_profiles:
  - "markdown-frontmatter-v11"
  - "markdown-structure-v11"
  - "footer-governance-links-v11"
  - "pipeline-pattern-event-driven-deterministic-v1"

ci_integration: ".github/workflows/docs-lint.yml"

scope:
  domain: "multi-domain"
  applies_to:
    - "etl"
    - "stac"
    - "dcat"
    - "graph"
    - "lineage"
    - "provenance"
    - "telemetry"
    - "focus-mode"
  impacted_modules:
    - "docs/pipelines/patterns"
    - "src/pipelines/*"
    - "src/graph/*"
    - "src/api/*"
    - "data/raw/*"
    - "data/work/*"
    - "data/processed/*"
    - "data/stac/*"
    - "dist/provenance/*"
    - ".github/workflows/*"
---

<div align="center">

# 🚦 **Event‑Driven Deterministic Ingestion & Promotion Pattern**  

**Triggers → Orchestrate → Stage → Transform → QA → Canary → Monitor → Promote / Rollback**  
_Idempotent keys · Write‑Ahead Log · STAC/DCAT · PROV‑O · Lineage · Energy/Cost Telemetry_

`docs/pipelines/patterns/event-driven-deterministic-ingest.md`

</div>

---

## 📘 Overview

### Purpose

This pattern defines the **canonical KFM v11.2.4 approach** for turning any external change signal:

- Object‑store drops,  
- Dataset webhooks,  
- Scheduled cadence fallbacks  

into **deterministic, replayable ingestion & promotion runs** with:

- Idempotent execution,  
- WAL‑safe writes,  
- STAC/DCAT/PROV‑aligned catalogs,  
- FAIR+CARE‑aware masking and tribal review hooks,  
- One‑click, feature‑flagged promotion and rollback.

It must be used whenever a KFM pipeline:

- Reacts to **events** (not just cron), and  
- **Publishes** to canonical KFM data spaces:
  - `data/raw`, `data/work`, `data/processed`,  
  - `data/stac`, Neo4j graph, Story Node feeds.

### Goals

- Turn **triggers** into **RunEvents** with stable idempotency keys.  
- Enforce **deterministic transforms** (no hidden randomness or clock usage).  
- Capture **full provenance** (PROV‑O + OpenLineage) and energy/cost telemetry.  
- Gate publication with **schema, QA, and CARE checks**.  
- Publish via **canary → monitor → promote/rollback** instead of direct writes.  

---

## 🗂️ Directory Layout

This pattern governs layout and behavior, not individual pipelines, but a typical KFM‑aligned structure is:

```text
📁 docs/
└── 📁 pipelines/
    └── 📁 patterns/
        ├── 📄 README.md                                   # Patterns index
        ├── 📄 run-state/README.md                         # Run-state pattern
        └── 📄 event-driven-deterministic-ingest.md        # ← This file

📁 data/
├── 📁 raw/
│   └── 📁 <dataset>/
│       └── 📁 <window>/...                               # Event-aligned window (e.g., YYYY-MM-DD, run-id)
├── 📁 work/
│   └── 📁 <dataset>/
│       └── 📁 <run_id>/...                               # Intermediate, per-run staging
├── 📁 processed/
│   └── 📁 <dataset>/
│       └── 📁 <version>/...                              # Canonical processed outputs (versioned)
└── 📁 stac/
    └── 📁 <dataset>/
        └── 📁 <version>/
            ├── 📄 collection.json
            └── 📄 item-*.json

📁 schemas/
└── 📁 telemetry/
    ├── 📄 patterns-event-driven-v1.json                  # This pattern’s telemetry schema
    ├── 📁 tabular/
    │   └── 📄 <dataset>.schema.json                      # JSON Schema / Pydantic compatible
    └── 📁 geo/
        └── 📄 <dataset>.geo.schema.json                  # Geometry & CRS rules

📁 src/
├── 📁 pipelines/
│   └── 📁 <dataset>/
│       ├── 📄 orchestrator.py                            # Event-driven orchestrator
│       ├── 📄 validators.py                              # Schema + domain + CARE checks
│       ├── 📄 stac_emit.py                               # STAC/DCAT emission helpers
│       └── 📄 wal.py                                     # Write-ahead log utilities (or shared lib)
├── 📁 graph/
│   └── 📁 neo4j/
│       ├── 📄 models.py                                  # Dataset/Run/Artifact node & rel types
│       └── 📄 emit.py                                    # Shadow + prod graph emitters
└── 📁 qa/
    ├── 📁 great_expectations/                            # Optional expectations suites
    └── 📁 care_policies/                                 # H3 generalization & masking policies
```

Pipelines may reorganize internals, but **must not diverge** from the logical separation of:

- `raw` → `work` → `processed` → `stac` → `graph`, and  
- `docs` → `schemas` → `src` triad for documentation, schemas, and implementation.

---

## 🧭 Context

KFM’s pipeline backbone is:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode

This pattern is the **event‑driven special case** of that backbone:

- Inputs are driven by **external events**, not just cron.  
- Multiple events may target the **same dataset and window**.  
- It must be possible to **replay** events and **rollback** bad promotions.  

It sits alongside:

- The **Run‑State pattern** (`docs/pipelines/patterns/run-state/README.md`), and  
- The **OpenLineage CI Integration Standard** (`docs/standards/lineage/openlineage-ci-integration.md`),

and assumes:

- All runs are **run-state tracked**,  
- All runs **emit OpenLineage + PROV‑O**,  
- All promotions are **feature-flag‑controlled** and WAL‑backed.

---

## 🧱 Architecture

### High-level flow (conceptual)

```text
Triggers → Event Bus → Orchestrator → Stage (raw) → Transform (work/processed)
→ QA (schema + domain + CARE) → Canary STAC/graph → Monitors → Promote / Rollback
```

Or step-wise:

1. **Triggers → Event Bus**  
   - Sources: object store events, dataset webhooks, or cron fallbacks.  
   - Normalized into `RunEvent` with:
     - `source_uri`,  
     - `content_hash` (e.g., BLAKE3),  
     - logical `time_window` (e.g., [t0, t1)).  

2. **Orchestrator → Deterministic Run**  
   - Derive **idempotency key**:
     - `idempotency_key = hash(source_uri + content_hash + time_window)`.  
   - Spawn pipeline with:
     - Fixed seeds,  
     - Pinned dependencies & containers,  
     - Run labels (dataset, window, env).  

3. **Stage → Lake (Raw)**  
   - WAL‑guarded write to `data/raw/<dataset>/<window>/...`:
     - Download → temp path → checksum → atomic rename.  
   - Capture:
     - Bytes, checksums, ETags, and any remote version IDs.  

4. **Transform → Work / Processed**  
   - Transform nodes must be **pure** with respect to:
     - Inputs (raw files and configs),  
     - Seeds (explicit and logged).  
   - Intermediate artifacts:
     - `data/work/<dataset>/<run_id>/...`  
   - Final canonical outputs:
     - `data/processed/<dataset>/<version>/...`  

5. **Provenance + Telemetry**  
   - Emit **OpenLineage events** (START, COMPLETE/FAIL).  
   - Emit **PROV‑O JSON‑LD**:
     - Entities (inputs, outputs, configs),  
     - Activity (run),  
     - Agent (pipeline/CI).  
   - Emit **telemetry**:
     - Energy (kWh), carbon (kgCO₂e), cost (USD), records in/out.

6. **Quality Gates (hard fail on red)**  
   - Schema & type checks (tabular/geospatial).  
   - Domain QA (ranges, uniqueness, dedup, etc.).  
   - CARE masking and tribal review hooks where necessary.

7. **Publish (canary first)**  
   - Generate **STAC Collections/Items** (source-of-truth).  
   - Derive **DCAT 3.0 datasets/distributions** from STAC.  
   - Publish to:
     - **Canary STAC/DCAT** namespace,  
     - **Shadow Neo4j graph**.  

8. **Monitors → Promote or Rollback**  
   - Monitors watch:
     - Availability,  
     - Schema & value diffs,  
     - Performance,  
     - User smoke tests.  
   - On green within a window:
     - Promote to **prod catalogs & graph**; flip feature flags.  
   - On red:
     - Trigger structured **rollback**:
       - Reset flags,  
       - Roll back graph pointer,  
       - Optionally purge invalid processed artifacts.

### Idempotent run contract (canonical pseudo-code)

```python
from blake3 import blake3

def derive_idempotency_key(source_uri: str, content_hash: str, time_window: str) -> str:
    return blake3(f"{source_uri}|{content_hash}|{time_window}".encode("utf-8")).hexdigest()

key = derive_idempotency_key(source_uri, content_hash, time_window)

with orchestrator.run(idempotency_key=key, seed=SEED) as run:
    wal.begin("stage_raw", inputs=[source_uri])
    paths = stage_raw_to_lake(source_uri, checksums=True)
    wal.commit("stage_raw", outputs=paths)

    qa.assert_schema(paths.raw)            # JSON Schema / pydantic
    qa.assert_geo_valid(paths.raw_geo)     # CRS + topology

    wal.begin("transform")
    art = transform(paths.raw, seed=SEED)
    wal.commit("transform", outputs=art)

    qa.assert_expectations(art)            # Domain rules (GE, etc.)
    care.apply_masking_if_needed(art)      # H3 / generalization rules

    prov.emit(run=run.id, inputs=[paths], outputs=[art])
    tel.emit(node="transform", energy_kwh=..., cost_usd=...)

    stac_emit.canary(art)
    graph.shadow(art)

    if monitors.green_within("30m"):
        promote(art)
        flags.cutover("dataset-prod", "on")
    else:
        rollback.from_wal(run.id)
        flags.cutover("dataset-prod", "off")
```

---

## 📦 Data & Metadata

### Data tiers

- **Raw (`data/raw`)**  
  - Direct mirror of external payloads (optionally normalized to KFM codecs).  
  - Must be **immutable** for a given `(dataset, window, hash)` tuple.

- **Work (`data/work`)**  
  - Per‑run temporary artifacts.  
  - May be cleaned according to retention policy, but WAL must remain long enough to support rollback windows.

- **Processed (`data/processed`)**  
  - Canonical, referenceable layers, versioned as:
    - `<dataset>/<semver-or-tag>/...`.  
  - Only these are considered “published” once promoted.

### Metadata & manifests

Every stage must write **machine‑readable manifests** (JSON/YAML) containing:

- Inputs and outputs (paths, checksums, sizes),  
- Schema versions,  
- Run identifiers (`openlineage:runId`, `prov:Activity` IDs),  
- Validation & CARE status flags,  
- Energy/cost telemetry references.

These manifests are:

- Linked from STAC Item properties,  
- Linked from PROV‑O bundles,  
- Discoverable through the metadata & provenance registry.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC (source-of-truth catalogs)

For each promoted dataset version, this pattern requires:

- A **STAC Collection** describing:
  - Dataset, spatial and temporal extent,  
  - Sources and license,  
  - KFM extensions (energy, lineage, CARE labels).  

- A set of **STAC Items** describing:
  - Individual assets (Parquet, NetCDF, GeoTIFF, etc.),  
  - Checksums (`checksum:multihash` or equivalent),  
  - Linkage to:
    - PROV bundles (`kfm:provenance_ref`),  
    - Telemetry (`kfm:telemetry_ref`),  
    - OpenLineage runs (`openlineage:runId`).

### DCAT (derived from STAC)

DCAT 3.0 datasets/distributions are:

- Generated from STAC via the KFM STAC→DCAT derivation standard,  
- Never manually authored in conflict with the STAC source-of-truth,  
- Used for external cataloging and interoperability.

### PROV-O & Lineage

OpenLineage and PROV‑O work together:

- **OpenLineage**:
  - Run‑centric event stream (START, COMPLETE/FAIL, inputs/outputs).  

- **PROV‑O JSON‑LD**:
  - Rich, graph‑centric description of:
    - Entities: datasets, configs, code, manifests, audits,  
    - Activities: staging, transform, QA, publish, rollback,  
    - Agents: pipelines, CI, governance councils.

All promoted artifacts **must** be reachable in the PROV graph and include:

- `prov:wasGeneratedBy` (activities),  
- `prov:wasDerivedFrom` (earlier datasets or runs),  
- `prov:wasAssociatedWith` (agents).

---

## 🧪 Validation & CI/CD

### QA gate matrix (examples)

| Dimension  | Checks (non-exhaustive)                                                                 |
|-----------|------------------------------------------------------------------------------------------|
| Tabular   | JSON Schema / pydantic, enum domains, null policy, PK/UK uniqueness, dedup              |
| Geo       | Geometry validity, CRS matches declared, area/extent sanity, topology rules             |
| Time      | OWL‑Time alignment, no unintentional gaps/overlaps, ordered intervals                   |
| Domain    | Great‑Expectations‑style ranges, distributions, business rules                          |
| CARE      | Sensitive feature detection, H3 generalization, masking, and tribal review flags        |

All QA must be:

- **Automated & deterministic**,  
- Logged as part of run telemetry and PROV,  
- Binding for promotion decisions (red → no promote).

### CI integration

Typical workflows (per dataset or shared):

- `event-driven-ingest.yml`  
  - Executes the pattern end‑to‑end for integration tests,  
  - Validates manifests, STAC, PROV, and QA behavior.

- `lineage.yml` (per lineage standard)  
  - Verifies OpenLineage & PROV‑O completeness,  
  - Enforces the presence of `openlineage:runId` in STAC.

- `patterns-telemetry.yml`  
  - Aggregates pattern‑level telemetry into:
    - `releases/v11.2.4/patterns-telemetry.json`.

Failures in:

- Idempotency enforcement,  
- WAL correctness,  
- STAC/PROV completeness, or  
- CARE masking

are **ship‑blockers** and must block merges/promotions.

---

## 🧠 Story Node & Focus Mode Integration

Although this pattern lives in pipelines, it is **directly visible** to narratives:

- Story Nodes referencing datasets must be able to:
  - Jump to **STAC/PROV entries** for the exact promoted version,  
  - See whether the last promotion passed QA and CARE checks,  
  - Understand rollback events (if a dataset was reverted).

- Focus Mode relies on:
  - Stable **dataset versions** and **promotion histories**,  
  - Trust indicators derived from QA and audit outcomes,  
  - The ability to filter out views based on non‑green promotions.

Because promotions are:

- Feature‑flagged,  
- Graph‑pointer controlled,  
- Version‑tagged,

Focus Mode can present:

- “Current production view” vs  
- “Previous stable versions” (where Story Nodes may anchor to a specific version).

---

## ⚖ FAIR+CARE & Governance

This pattern is explicitly **CARE‑aware**:

- `care_label: "CARE-compliant (auto-mask on)"` implies:
  - All event‑driven pipelines must:
    - Detect sensitive or sovereign features when joining with soil, hydrology, archaeology, etc.,  
    - Apply **data generalization** (e.g., H3, distance fuzzing) where policies require,  
    - Record masking and generalization decisions in PROV and audit logs.

- `sensitivity: "Mixed"` implies:
  - Some datasets may be fully public, others require:
    - Indigenous Data Governance Board (IDGB) review,  
    - Restricted STAC/ DCAT visibility or redacted distributions.

Governance responsibilities:

- **Reliability & Observability teams**  
  - Own WAL, idempotency, and rollback guarantees.  

- **FAIR+CARE Data Governance Council + IDGB**  
  - Own policies for:
    - Sensitive data detection,  
    - Masking strategies,  
    - Approval gates before certain datasets can be promoted.

Any pipeline implementation claiming to follow this pattern must:

- Pass governance review (design + implementation),  
- Be linked from the analytical metadata & provenance registry,  
- Be covered by audit reports under `docs/analyses/metadata/audit-reports/`.

---

## 🕰️ Version History

| Version  | Date       | Author / Steward        | Summary                                                                 |
|----------|------------|------------------------|-------------------------------------------------------------------------|
| v11.2.4  | 2025-12-07 | KFM Reliability Guild  | Initial KFM-MDP v11.2.4–aligned event-driven deterministic ingest & promotion pattern. |

---

<div align="center">

**Kansas Frontier Matrix (KFM v11)**  

[📁 Pipeline Patterns Index](./README.md) · [📚 Pipelines Overview](../README.md) · [⚖️ Root Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
