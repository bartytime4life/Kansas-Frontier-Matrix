---
title: "🌱 KFM v11.2.4 — Delta Ingestion for Soils (STAC Versioned Assets + PROV‑O Lineage) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/soils/delta-ingestion/README.md"
version: "v11.2.4"
last_updated: "2025-12-06"

release_stage: "Stable · Governed"
lifecycle: "Long‑Term Support (LTS)"
review_cycle: "Quarterly · Data Engineering · FAIR+CARE Oversight"
content_stability: "stable"
backward_compatibility: "v11.x ingestion‑contract compatible"
status: "Active / Enforced"

doc_kind: "Pattern"
intent: "soils-delta-ingestion-pattern"
role: "soils-delta-ingestion-contract"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "soils"
  applies_to:
    - "etl"
    - "stac"
    - "provenance"
    - "graph-lineage"
    - "cost/energy telemetry"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Medium‑Sensitivity (soil parcel geometry governance applies)"
sensitivity: "CARE‑aligned geomasking for culturally sensitive overlays"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
classification: "KFM‑Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
risk_category: "Soils Delta Ingestion"
redaction_required: false

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-commit-hash>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
telemetry_ref: "releases/v11.2.4/patterns-telemetry.json"
telemetry_schema: "schemas/telemetry/patterns-v1.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "MIT"

mcp_version: "MCP‑DL v6.3"
markdown_protocol_version: "KFM‑MDP v11.2.4"
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
  - "docs/pipelines/soils/delta-ingestion/README.md@v11.2.4"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-pipelines-soils-delta-ingestion-pattern-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-soils-delta-ingestion-pattern-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"

doc_uuid: "urn:kfm:doc:pipelines:soils:delta-ingestion:pattern:v11.2.4"
semantic_document_id: "kfm-pipelines-soils-delta-ingestion-pattern-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:soils:delta-ingestion:pattern:v11.2.4"

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
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🧱 Architecture"
    - "📦 Data & Metadata"
    - "🧪 Validation & CI/CD"
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
  workflow: ".github/workflows/soils-delta-ci.yml"
  environment: "dev → staging → production"

branding_registry:
  standard: "Delta-First Ingestion × Versioned Assets × Sustainable Intelligence"
  architecture: "STAC Versioned Assets · PROV‑O Lineage · Neo4j DatasetVersion"
  analysis: "Evidence-Led · Carbon-Aware · FAIR+CARE Grounded"
  data-spec: "gNATSGO/SDA Soils × H3 Parcel Space"
  telemetry: "Cost/Energy/Carbon × Delta Efficiency"
  graph: "DatasetVersion · Activity · Parcel Nodes"

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

# 🌱 **KFM v11.2.4 — Delta Ingestion for Soils**  
**STAC Versioned Assets + PROV‑O Lineage**  
`docs/pipelines/soils/delta-ingestion/README.md`

**Purpose:**  
Define a governed **delta‑ingestion pattern** for soils that uses **STAC versioned assets** and **PROV‑O lineage** to reprocess **only parcels whose upstream inputs changed**, while keeping all writes deterministic, idempotent, and carbon‑aware across storage, graph, and APIs.

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode.

</div>

---

## 📘 Overview

Daily soils updates from gNATSGO/SDA usually touch **only a small subset** of parcels. Full re‑ingestion:

- Wastes compute and energy,  
- Increases carbon footprint,  
- Increases risk of non‑deterministic drift under source churn.

This pattern:

- Uses **STAC versioned assets** to separate **immutable content** from **logical pointers**.  
- Tracks end‑to‑end **PROV‑O lineage** per parcel/partition so we reprocess only parcels whose inputs changed.  
- Emits **deterministic, idempotent upserts** to storage, graph, and APIs, backed by WAL.  
- Lowers **cost/CO₂e** while improving repeatability, observability, and auditability.

It is the canonical delta ingestion pattern for soils pipelines that:

- Consume gNATSGO and/or SDA daily snapshots.  
- Publish soils parcels/tiles into KFM STAC, Neo4j, and downstream Story Nodes.

---

## 🗂️ Directory Layout

Authoritative layout for soils delta ingestion, using KFM‑MDP emoji tree conventions:

~~~text
KansasFrontierMatrix/
├── 📂 docs/
│   └── 📂 pipelines/
│       └── 📂 soils/
│           └── 📂 delta-ingestion/
│               ├── 📄 README.md                      # This file (pattern spec)
│               ├── 📂 runbooks/
│               │   ├── 📄 daily-delta-run.md         # Ops steps for daily deltas
│               │   └── 📄 rollback-replay.md         # How to rollback/replay a delta epoch
│               └── 📂 specs/
│                   ├── 📄 delta-selection.md         # Hash join logic, thresholds
│                   ├── 📄 versioned-assets.md        # Asset naming + STAC contract
│                   └── 📄 prov-lineage-model.md      # PROV‑O shapes + Neo4j mapping
│
├── 📂 src/
│   ├── 📂 pipelines/
│   │   └── 📂 soils/
│   │       └── 📂 delta_ingestion/                   # Implementation of this pattern
│   │           ├── 📄 __init__.py
│   │           ├── 📄 config.py                      # YAML→config models, collection IDs, limits
│   │           ├── 📄 discover_sources.py            # gNATSGO/SDA snapshot discovery + hashing
│   │           ├── 📄 delta_selector.py              # Parcel‑level delta selection
│   │           ├── 📄 transformer.py                 # Deterministic parcel transforms
│   │           ├── 📄 asset_writer.py                # Content‑addressed parquet writer
│   │           ├── 📄 stac_updater.py                # STAC item/collection upserts
│   │           ├── 📄 prov_emitter.py                # PROV‑O JSON‑LD emission
│   │           ├── 📄 graph_upserter.py              # Neo4j DatasetVersion + edges
│   │           └── 📄 wal.py                         # WAL + idempotency keys
│   └── 📂 graph/
│       └── 📂 lineage/
│           └── 📂 neo4j/
│               ├── 📄 dataset_version_schema.cql     # Dataset/DatasetVersion/Activity model
│               └── 📄 soils_delta_mappings.cql       # Soils‑specific lineage mappings
│
├── 📂 data/
│   ├── 📂 sources/
│   │   └── 📂 soils/
│   │       ├── 📂 gnatsgo/                           # gNATSGO daily snapshots (inputs)
│   │       └── 📂 sda/                               # SDA‑derived daily inputs (if materialized)
│   ├── 📂 work/
│   │   └── 📂 soils/
│   │       └── 📂 delta-cache/                       # Last‑seen source hashes per parcel (KV/parquet)
│   ├── 📂 processed/
│   │   └── 📂 soils/
│   │       └── 📂 parcels/
│   │           └── 📂 h3_res8/                       # Content‑addressed parquet for each parcel/tile
│   └── 📂 stac/
│       └── 📂 soils/
│           ├── 📂 collections/                       # Collections (e.g., kfm-soils-v11)
│           └── 📂 items/
│               └── 📂 h3/
│                   └── 📂 8/                         # One item per H3‑r8 parcel/tile
│
└── 📂 .github/
    └── 📂 workflows/
        ├── 📄 soils-delta-ci.yml                     # STAC/PROV/contract tests + unit tests
        └── 📄 soils-delta-energy-carbon.yml          # Energy/cost/carbon checks & dashboards
~~~

**Author rules:**

- All new docs for soils delta ingestion live under `docs/pipelines/soils/delta-ingestion/`.  
- Code implementing this pattern lives under `src/pipelines/soils/delta_ingestion/` and must reference this doc in its module docs.  
- All new subdirectories must be added to this tree with an emoji and a short trailing description comment.

---

## 🧭 Context

### Why this pattern

Daily soils updates from gNATSGO/SDA often modify **only a small fraction** of parcels:

- Full re‑ingestion is compute‑heavy and **carbon‑intensive**.  
- Rebuilding everything complicates drift analysis and provenance.  
- Idempotency and rollback are harder when outputs are constantly overwritten.

This pattern provides:

- **Delta‑aware selection** so only impacted parcels are re‑processed.  
- **Deterministic behavior** so delta decisions can be audited and replayed.  
- **Lineage‑first design** so downstream Story Nodes and analyses can justify each parcel’s state.

### Concepts (quick primer)

- **STAC Item/Collection**  
  JSON metadata describing geospatial assets and their context (time, space, lineage).

- **Versioned Asset**  
  - Physical asset URIs encode content hash, e.g.:  
    `…/parcel_<H3>_<date>__sha256-<hash>.parquet`.  
  - Logical asset key (`assets.parcel`) stays stable but points to the **current** version.

- **PROV‑O**  
  W3C model for expressing *which Activity* generated *which Entity* using *which inputs*.

- **Delta gate**  
  A decision step that triggers work **only** when upstream source versions change for that parcel.

---

## 🧱 Architecture

### Deterministic Asset Naming

**Physical (immutable)**

~~~text
s3://kfm/soils/parcel/{h3}/{date}/parcel_{h3}_{date}__sha256-{hash}.parquet
~~~

**Logical (stable in STAC)**

- `assets.parcel.href` → current physical URI.  
- `assets.parcel.checksum:sha256` → `{hash}`.  
- Changing `href` without changing `checksum` is forbidden.

This ensures:

- Content‑addressed assets (no silent data substitution).  
- Clear separation between **version history** and **current view**.

### Delta Selection Flow (DAG Outline)

High‑level DAG:

1. **Discover sources**  
   - Locate latest gNATSGO/SDA snapshots.  
   - Compute stable content hashes (e.g., tree hash of snapshot).

2. **Select deltas**  
   - Compare `(parcel_h3, last_seen_source_hashes)` with current.  
   - Emit only parcels whose inputs changed.

3. **Transform**  
   - Deterministic parcel transforms (pinned libs, fixed seeds, config digests).

4. **Write artifacts**  
   - Physical asset → content‑addressed parquet path.  
   - Verify checksum matches.

5. **Update STAC**  
   - Upsert parcel STAC Item with new asset href + checksums + source version fields.

6. **Emit PROV‑O**  
   - Activity + Entity JSON‑LD for each parcel update.

7. **Upsert Neo4j lineage**  
   - `DatasetVersion` and `Activity` nodes + relationships.

8. **Publish telemetry**  
   - Cost/energy/carbon + delta efficiency metrics (delta vs full re‑ingest).

### Idempotency & WAL (Selection + Commit)

Idempotency key:

~~~text
idempotency_key = "{parcel_h3}:{gnatsgo_sha}:{sda_sha}"
~~~

Reference pseudocode:

~~~python
def maybe_process_parcel(parcel_h3, sha_g, sha_s, wal, cache):
    key = f"{parcel_h3}:{sha_g}:{sha_s}"

    # Idempotent replay guard
    if wal.already_committed(key):
        return "skip-wal"  # replay: no-op

    last = cache.get(parcel_h3)  # {"gnatsgo": old_g, "sda": old_s}

    # No source change → no work
    if last and last["gnatsgo"] == sha_g and last["sda"] == sha_s:
        return "skip-no-change"

    # New work needed
    wal.intent(key, parcel_h3=parcel_h3, gnatsgo=sha_g, sda=sha_s)

    process_parcel(parcel_h3, sha_g, sha_s)  # deterministic transform + write

    cache.set(parcel_h3, {"gnatsgo": sha_g, "sda": sha_s})
    wal.commit(key)
    return "processed"
~~~

**Rules:**

- WAL must record `intent` **before** side‑effects and `commit` **after** verification.  
- Replaying a run with identical inputs **must** produce no new writes.

### Neo4j Lineage Model (Essentials)

Core lineage pattern:

- `(:Dataset {name:"soils"})-[:HAS_VERSION]->(:DatasetVersion {sha:"5e…77", date:"2025‑12‑06"})`  
- `(:Activity {kind:"soils-delta-ingest", run_id:"…"})-[:USED]->(:DatasetVersion {sha:"3b…c9", source:"gnatsgo"})`  
- `(:Activity)-[:USED]->(:DatasetVersion {sha:"91…aa", source:"sda"})`  
- `(:Activity)-[:GENERATED]->(:DatasetVersion {sha:"5e…77", scope:"parcel", h3:"882a1dca7bfffff"})`

Parcel state:

- `(:Parcel {h3:"882a1dca7bfffff"})-[:HAS_VERSION]->(:DatasetVersion {sha:"5e…77"})`

### Rollback & Replay

- **Replay:** running the same date with same input hashes:
  - WAL sees committed `idempotency_key` → no work.  
- **Rollback:** preferred approach is **forward‑fix**:
  - Create new `DatasetVersion` with corrected content.  
  - Update STAC item to point to the corrected asset.  
  - Lineage graph keeps both the prior and corrected versions visible.  

Hard rollback (if necessary):

- Point STAC asset back to prior version.  
- Mark later `DatasetVersion` nodes as deprecated with a governance note.

---

## 📦 Data & Metadata

### Data Layout & Delta Cache

- **Inputs:**  
  - `data/sources/soils/gnatsgo/{date}/…`  
  - `data/sources/soils/sda/{date}/…`  

- **Delta cache:**  
  - `data/work/soils/delta-cache/` keyed by `parcel_h3`, storing last‑seen source hashes.  

- **Outputs:**  
  - `data/processed/soils/parcels/h3_res8/…` (content‑addressed parquet).  
  - `data/stac/soils/collections/` + `data/stac/soils/items/h3/…`.  

### Minimal STAC Item Delta Fields (Excerpt)

~~~json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "soil-parcel-h3-8-882a1dca7bfffff",
  "properties": {
    "kfm:dataset": "soils",
    "kfm:parcel_h3": "882a1dca7bfffff",
    "kfm:source_versions": {
      "gnatsgo": "sha256:3b…c9",
      "sda": "sha256:91…aa"
    },
    "kfm:derivation_version": "sha256:5e…77",
    "kfm:delta_epoch": "2025-12-06"
  },
  "assets": {
    "parcel": {
      "href": "s3://…/parcel_882a1dca7bfffff_2025-12-06__sha256-5e…77.parquet",
      "roles": ["data"],
      "checksum:sha256": "5e…77",
      "version": "2025-12-06T00:00:00Z"
    }
  }
}
~~~

**Rules:**

- `kfm:source_versions` must reflect **all** sources used for the parcel.  
- `kfm:derivation_version` = content hash of the output asset.  
- `kfm:delta_epoch` = logical delta date (not necessarily wall‑clock).  

### PROV‑O Lineage Event (JSON‑LD Excerpt)

~~~json
{
  "@context": ["https://www.w3.org/ns/prov", "https://schema.kfm.dev/prov/v1"],
  "@id": "urn:kfm:activity:soils:delta:2025-12-06:882a1dca7bfffff",
  "@type": "prov:Activity",
  "prov:used": [
    "urn:kfm:entity:gnatsgo:sha256:3b…c9",
    "urn:kfm:entity:sda:sha256:91…aa"
  ],
  "prov:generated": "urn:kfm:entity:soils:parcel:sha256:5e…77",
  "prov:wasAssociatedWith": "urn:kfm:agent:pipeline:soils-delta-ingest@v11.2.4",
  "kfm:idempotency_key": "882a1dca7bfffff:3b…c9:91…aa"
}
~~~

Location:

~~~text
data/lineage/soils/delta-ingestion/<delta_epoch>/<parcel_h3>.prov.jsonld
~~~

### Configuration Contract (YAML)

~~~yaml
delta_ingest:
  dataset: soils
  delta_epoch: "2025-12-06"

  sources:
    - name: gnatsgo
      locator: s3://kfm/sources/soils/gnatsgo/{date}/
      hash_mode: sha256-filetree
    - name: sda
      locator: s3://kfm/sources/soils/sda/{date}/
      hash_mode: sha256-filetree

  partitioning:
    id_space: h3_res8

  wal:
    table: kfm_soils_delta_wal
    key_template: "{parcel_h3}:{gnatsgo_sha}:{sda_sha}"

  stac:
    collection_id: "kfm-soils-v11"
    write_mode: upsert
    items_root: "data/stac/soils/items/h3/8/"

  care:
    sensitive_overlay: "s3://kfm/sensitivity/cultural_sensitivity.gpkg"
    action: mask_or_hold
~~~

**Rules:**

- Any change to key fields (`sources`, `partitioning`, `wal.key_template`, `stac.collection_id`) requires a **pattern version review**.  
- Configs must be stored under `data/sources/…` or `docs/pipelines/soils/delta-ingestion/specs/` and tracked via git.

---

## 🧪 Validation & CI/CD

### CI / Quality Gates

Delta ingestion must pass:

- **STAC lint**  
  - Schema validation.  
  - `checksum:sha256` matches actual asset.  
  - Asset roles, IDs, and collection references valid.

- **PROV‑O validator**  
  - Every output asset has one or more generating `prov:Activity`.  
  - Activities list all input entities used.  

- **Idempotency check**  
  - WAL replay with identical inputs is no‑op (no new writes, no new PROV).

- **Determinism check**  
  - Byte‑stable parquet for the same inputs/config.  
  - Pinned libraries and seed‑fixed UDFs.

- **CARE geometry guards**  
  - Parcel overlays that intersect culturally sensitive layers trigger mask/hold actions.  

- **Energy/CO₂e efficiency**  
  - Emit `kwh`, `co2e_g`, and cost per processed parcel.  
  - Daily delta ratio (changed_parcels / all_parcels) should trend ≥ 0.9 for stable sources, or be explainable.

### SLOs

- **p95 daily cycle time:** ≤ 30 minutes for 100k parcels (delta‑only).  
- **False‑positive reprocess rate:** < 0.5% (hash stability).  
- **Lineage completeness:** 100% of outputs have PROV‑O linkage.  
- **Carbon intensity trend:** ≥ 60% reduction vs full re‑ingest baseline over 30 days.

### Observability

- **Span phases:**  
  `discover_sources` → `select_deltas` → `transform` → `write_artifact` → `stac_upsert` → `prov_emit` → `graph_upsert`.

- **Metric cardinality:**  
  - Labels limited to controlled sets: `dataset`, `delta_epoch`, `parcel_h3` (optionally bucketed), status enums.  
  - No raw hashes in metric labels (bucketed or summarized instead).

Example dev workflow:

~~~bash
make soils-delta.init         # create cache, WAL table, baseline config
make soils-delta.run DATE=2025-12-06
make soils-delta.audit        # STAC, PROV, lineage, energy checks
~~~

---

## ⚖ FAIR+CARE & Governance

This pattern is FAIR+CARE‑aligned by design:

- **FAIR**  
  - **Findable:** STAC Items, DatasetVersion nodes, and PROV docs make parcel histories discoverable.  
  - **Accessible:** Stored under standard `data/` and `stac/` hierarchies with documented paths.  
  - **Interoperable:** Uses STAC 1.0, DCAT, and PROV‑O for metadata and lineage.  
  - **Reusable:** Content‑addressed assets with clear provenance and version history.

- **CARE**  
  - **Collective Benefit:** Efficient deltas reduce unnecessary compute and carbon for public soils data.  
  - **Authority to Control:** CARE overlays and `mask_or_hold` actions allow culturally sensitive layers to govern visibility.  
  - **Responsibility:** Delta decisions are fully logged; mis‑configured gates can be audited and corrected.  
  - **Ethics:** Explicit documentation of how soils parcels may interact with sensitive overlays (e.g., heritage sites) ensures transparent governance.

Governance hooks:

- Changes that affect:
  - Delta selection logic,  
  - CARE overlay handling, or  
  - DatasetVersion semantics  

must be reviewed by:

- Data Engineering leads,  
- FAIR+CARE Oversight, and  
- (where relevant) Indigenous and cultural data stewards.

---

## 🕰️ Version History

| Version   | Date       | Description                                                                                      |
|----------:|------------|--------------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025‑12‑06 | Initial governed release: STAC versioned assets, PROV‑O lineage, Neo4j DatasetVersion wiring, WAL idempotency, CARE mask hooks. |

---

<div align="center">

🌱 **KFM v11.2.4 — Delta Ingestion for Soils**  
STAC Versioned Assets · PROV‑O Lineage · Neo4j‑Integrated · Carbon‑Aware  

[📘 Pipelines Index](../../README.md) · [🛰 Lineage Standard](../lineage/lineage-telemetry-standard.md) · [⚖ Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>