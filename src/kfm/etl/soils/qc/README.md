---
title: "🧪 KFM — NASIS/SDA Ingest QC Checklist (Deterministic · Provenance‑Ready)"
path: "src/kfm/etl/soils/qc/README.md"
version: "v11.2.6"
last_updated: "2025-12-14"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Soils Domain Board · FAIR+CARE Council"
content_stability: "stable"

status: "Active · Enforced"
doc_kind: "Checklist"
header_profile: "standard"
footer_profile: "standard"
intent: "kfm-soils-nasis-sda-qc-checklist"

license: "MIT"
classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

semantic_document_id: "kfm-soils-nasis-sda-qc"
doc_uuid: "urn:kfm:soils:nasis-sda:qc:v11.2.6"
event_source_id: "ledger:src/kfm/etl/soils/qc/README.md"
immutability_status: "version-pinned"

commit_sha: "<latest-commit-hash>"
provenance_chain: []

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

data_contract_ref: "../../../../docs/contracts/data-contracts/soils-nasis-sda.json"
quality_policy_ref: "../../../../docs/standards/data-quality/README.md"
openlineage_schema_ref: "../../../../schemas/lineage/openlineage-v1.json"
prov_schema_ref: "../../../../schemas/prov/kfm-prov-v11.json"
stac_item_schema_ref: "../../../../schemas/stac/kfm-stac-item-v11.json"
dcat_dataset_schema_ref: "../../../../schemas/dcat/kfm-dcat-dataset-v11.json"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

ai_transform_permissions:
  - "summary"
  - "metadata-extraction"
  - "semantic-highlighting"
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

# 🧪 **KFM — NASIS/SDA Ingest QC Checklist**
`src/kfm/etl/soils/qc/README.md`

**Purpose**  
Enforce **deterministic NASIS/SDA ingestion** and **policy-grade provenance**.  
Copy these checks into the ETL validation step. On **any** failure: **abort**, emit a policy event, and keep the job replayable.

</div>

## 📘 Overview

This QC-first checklist is the minimum “gate” for NASIS/SDA ingestion in KFM.

What it enforces:

- **Determinism:** same inputs → same chunk keys, IDs, stats, and outputs.
- **Interoperability:** canonical units + canonical IDs enable clean joins across domains.
- **Trust & auditability:** STAC/DCAT + PROV/OpenLineage emissions make QC decisions reviewable under governance.

Operational posture:

- **Fail closed:** if a check fails, do not publish partial/ambiguous artifacts.
- **Record why:** every failure should produce machine-readable evidence (validation report + lineage event).

## 🗂️ Directory Layout

~~~text
📁 src/kfm/etl/soils/qc/                               — NASIS/SDA ingest quality controls (this spec)
├── 📄 README.md                                       — Deterministic QC checklist (this document)
└── 🧾 <qc_artifacts_live_elsewhere>                   — QC outputs belong to run/lineage locations
    ├── 📁 mcp/runs/<run_id>/                          — Run logs + config snapshots (repro evidence)
    └── 📁 data/**/lineage/                            — PROV/OpenLineage + manifests (audit-grade)
~~~

Notes:

- This folder is a **policy/checklist surface**, not a place to store run outputs.
- Store execution evidence in run/lineage locations referenced by the pipeline contract.

## 🧭 Context

This checklist is designed to be applied at the **ETL validation gate** for NASIS/SDA ingestion.

Inputs/constraints are governed by:

- `data_contract_ref` (schema + invariants that must hold)
- `quality_policy_ref` (minimum quality thresholds and enforcement posture)

A passing ingest must be able to produce (or prepare):

- deterministic chunking and stable identifiers,
- unit-normalized, contract-conformant data,
- QC metrics and reports,
- provenance events (OpenLineage + PROV) suitable for governance review,
- catalog-ready metadata (STAC/DCAT readiness; publication happens outside this doc).

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A["NASIS/SDA source queries"] --> B["Deterministic chunking + fingerprints"]
  B --> C["Normalize IDs + units"]
  C --> D["QC checks (this checklist)"]
  D -->|pass| E["Materialize staged/processed artifacts"]
  D -->|fail| F["Abort + emit policy event"]
  E --> G["Emit PROV/OpenLineage"]
  E --> H["Prepare STAC/DCAT metadata"]
~~~

## 🧠 Story Node & Focus Mode Integration

This checklist is not narrative evidence; it is a **governed policy gate**.

Focus Mode may:

- summarize this checklist for internal operator guidance,
- extract “required checks” as structured tasks,
- link QC outcomes to the corresponding run and lineage records.

Focus Mode must not:

- claim a dataset “passed QC” without a linked run record and validation artifact,
- invent governance approval outcomes,
- infer sensitive location details from spatial checks beyond policy bounds.

## 🧪 Validation & CI/CD

### How to use this checklist

- Implement each check as a deterministic validator in the ingestion pipeline.
- Emit the listed metrics and an aggregate validation report.
- On **any** failure:
  - abort the load,
  - emit failure lineage (OpenLineage + PROV),
  - preserve replayability (inputs + parameters + environment snapshot).

### QC Checklist

#### 1) Deterministic Chunking
- **Rule:** fixed, content-derived chunk keys.
- **Action:** use stable partitioners (e.g., H3/quadkey or county‑FIPS) plus a schema fingerprint.
- **Assert:**
  - chunk key = `hash(namespace|schema_version|source_ids)` (stable across re-ingests)
  - no chunk drift between runs (checksum equality for equivalent inputs)
- **Emit (metrics):** `qc.chunk.count`, `qc.chunk.drift=0/1`, `qc.input.fingerprint`

#### 2) Canonical ID Normalization
- **Rule:** every entity has a stable `canonical_id`.
- **Action:** map NASIS/SDA identifiers → `soil_series_id`, `comp_id`, `hz_id` with namespaced URNs.
- **Assert:**
  - `canonical_id` pattern validation passes (per contract)
  - duplicates collapse deterministically (stable tie-breakers)
- **Emit:** `qc.id.duplicates_resolved`, `qc.id.nulls=0`

#### 3) Unit Normalization
- **Rule:** normalize to SI + declared profile (e.g., depth in meters; controlled vocabularies).
- **Action:** convert fields (`hzdept_r`, `hzdepb_r`, bulk density, organic matter) to canonical units.
- **Assert:**
  - no unitless numerics in governed outputs
  - conversions logged deterministically
  - schema profile tag = `soils-v11` (or contract-defined profile)
- **Emit:** `qc.units.converted_count`, `qc.units.profile=soils-v11`

#### 4) Strict Horizon Monotonicity
- **Rule:** for each component/pedon: `top < bottom` and horizons strictly increase with depth.
- **Action:** sort by `hzdept_r`; verify `hzdept_r[i+1] >= hzdepb_r[i]`.
- **Assert:**
  - no overlaps
  - no inversions
  - no gaps unless explicitly allowed by contract (`allow_gaps=false` default)
- **Emit:** `qc.hz.inversions=0`, `qc.hz.overlaps=0`, `qc.hz.gaps=0`

#### 5) Join‑Cardinality Asserts
- **Rule:** key joins are `1:1` or `1:N` as designed; no fan‑out explosions.
- **Action:** compute expected vs observed cardinalities (series→component, component→horizon) before materializing.
- **Assert:**
  - observed cardinalities within contract bounds
  - orphan keys = 0
- **Emit:** `qc.join.violations=0`, `qc.join.orphans=0`, `qc.join.max_fanout<=policy.max`

#### 6) Vocabulary & Domain Checks
- **Rule:** categorical fields map to controlled lists (e.g., texture class, drainage class).
- **Action:** validate against contract vocabularies; map deprecated values deterministically.
- **Assert:** unknown categories = 0 (or explicitly quarantined per contract)
- **Emit:** `qc.vocab.unknown=0`, `qc.vocab.deprecated_mapped`

#### 7) Spatial Validity
- **Rule:** geometries valid; CRS = EPSG:4326; AOI rules per contract.
- **Action:** validate geometry; reproject if allowed; enforce centroid precision policy.
- **Assert:**
  - `is_valid(geom)`
  - within AOI (when AOI enforcement is enabled)
  - no self-intersections
- **Emit:** `qc.spatial.invalid=0`, `qc.spatial.out_of_aoi=0`

#### 8) Null & Range Policies
- **Rule:** no critical nulls; numeric ranges within pedologic plausibility.
- **Action:** enforce required fields; validate ranges and units after normalization.
- **Assert:**
  - critical required fields non-null
  - plausible ranges pass (per contract)
- **Emit:** `qc.nulls.critical=0`, `qc.range.violations=0`

#### 9) Reproducibility Envelope
- **Rule:** seeded transforms; environment pinned.
- **Action:** capture seed, container image digest, dependency lockfile hashes in run record.
- **Assert:** reproducibility fields present and stable for the run.
- **Emit:** `qc.env.image_digest`, `qc.env.deps_lock_sha`

#### 10) Policy‑Ready Provenance Emits
- **Rule:** on success/fail, emit STAC/DCAT metadata + PROV/OpenLineage events.
- **Action:** write sidecar provenance artifacts alongside governed run artifacts (not in this folder).
- **Assert:** provenance artifacts validate against schema references in front matter.
- **Emit:** `qc.prov.emitted=0/1`, `qc.openlineage.emitted=0/1`, `qc.catalog.ready=0/1`

## 📦 Data & Metadata

### Deterministic chunk key (pseudo‑Python)

~~~python
from hashlib import blake2b

def stable_chunk_key(namespace: str, schema_ver: str, part_keys: dict) -> str:
    material = "|".join([
        namespace,
        schema_ver,
        *(f"{k}={part_keys[k]}" for k in sorted(part_keys))
    ]).encode("utf-8")
    return "urn:kfm:chunk:" + blake2b(material, digest_size=16).hexdigest()
~~~

### Required QC output shape (minimum)

A QC gate should be able to produce (or allow reconstruction of) the following:

- input fingerprint(s) (source IDs + schema version + query parameters)
- deterministic chunk keys list
- QC metrics (namespaced `qc.*`)
- validation report summary (`passed` / `failed` + reasons)
- links/refs to provenance artifacts emitted for the run

This checklist does not dictate file locations for these artifacts beyond “do not store run outputs in this folder”; the pipeline contract governs exact output paths.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
QC outcomes should be representable as STAC Item properties for the produced artifacts (or their promotion candidates):

- `properties.kfm:qc_status` (`passed` / `failed`)
- `properties.kfm:qc_report_ref` (repo path or artifact reference)
- `properties.kfm:input_fingerprint`
- `properties.kfm:chunk_key` / shard key(s) as applicable

Validate Item shape against `stac_item_schema_ref`.

### DCAT
QC readiness should support a DCAT Dataset / Distribution representation:

- `dct:identifier` derived from stable dataset ID
- `dct:conformsTo` referencing the data contract/schema version
- rights/license fields confirmed by policy checks
- distribution references point to governed outputs, not this checklist

Validate dataset metadata against `dcat_dataset_schema_ref`.

### PROV + OpenLineage
QC must be auditable:

- checks are `prov:Activity` (and OpenLineage `Run`)
- inputs/outputs are `prov:Entity` (and OpenLineage `Dataset`)
- the actor is `prov:Agent` (pipeline runner, steward role, CI)

Validate lineage outputs against:

- `openlineage_schema_ref`
- `prov_schema_ref`

## 🧱 Architecture

Integration expectations:

- implement validators as deterministic, config-driven steps in the soils ingestion pipeline,
- ensure idempotent re-runs (same inputs produce the same chunk keys, IDs, and QC metrics),
- keep QC “gate logic” separate from “promotion logic” (promotion is a distinct activity with explicit lineage).

Frontends must not depend on this checklist or any staging/QC scratch outputs directly; they should consume only governed APIs/catalogs and promoted assets.

## ⚖ FAIR+CARE & Governance

This checklist is binding under governance and must not be bypassed.

Governance expectations:

- QC failures must be visible to reviewers through lineage artifacts, not informal notes.
- Rights/licensing checks must prevent publication of data with unclear reuse status.
- Sovereignty constraints must be respected: do not increase discoverability of sensitive locations through QC reporting; apply masking/generalization policies where required.

If a check requires exceptions (e.g., allowing gaps in horizons), exceptions must be:

- encoded in the data contract,
- justified in governed notes,
- traceable in provenance for each run where applied.

## 🕰️ Version History

| Version | Date | Author | Summary |
|---|---:|---|---|
| v11.2.6 | 2025-12-14 | `@kfm-soils` | Initial KFM‑MDP v11.2.6 compliant QC checklist for deterministic NASIS/SDA ingestion with provenance-ready emissions. |

<div align="center">

[🏛️ Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md) ·
[📜 Soils Data Contract](../../../../docs/contracts/data-contracts/soils-nasis-sda.json) ·
[✅ Data Quality Standard](../../../../docs/standards/data-quality/README.md)

</div>

