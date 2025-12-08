---
title: "🧩 Kansas Frontier Matrix — Unified Pipeline Idempotency, Safety & Governance Pattern (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/patterns/idempotent-safety-governance.md"
version: "v11.2.4"
last_updated: "2025-12-07"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability Engineering · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x compliant"

status: "Active / Enforced"
doc_kind: "Pattern"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256-or-null>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
telemetry_ref: "releases/v11.2.4/patterns-telemetry.json"
telemetry_schema: "schemas/telemetry/pattern-idempotent-safety-governance-v3.json"
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
sensitivity: "Mixed (geospatial joins may involve sovereign or sensitive data)"
classification: "Public / Internal (governance pattern)"

provenance_chain:
  - "docs/pipelines/patterns/idempotent-node/README.md@v11.2.4"
  - "docs/pipelines/patterns/event-driven-deterministic-ingest.md@v11.2.4"
  - "docs/analyses/metadata/README.md@v11.2.4"

doc_uuid: "urn:kfm:doc:pipelines:patterns:idempotent-safety-governance:v11.2.4"

test_profiles:
  - "markdown-frontmatter-v11"
  - "markdown-structure-v11"
  - "footer-governance-links-v11"
  - "pattern-idempotent-safety-governance-v1"

ci_integration: ".github/workflows/docs-lint.yml"

scope:
  domain: "multi-domain"
  applies_to:
    - "etl"
    - "event-driven"
    - "stac"
    - "graph"
    - "provenance"
    - "telemetry"
    - "governance"
  impacted_modules:
    - "docs/pipelines/patterns"
    - "src/pipelines/_common/*"
    - "src/pipelines/*"
    - "data/work/*"
    - "data/processed/*"
    - "data/dlq/*"
    - "data/stac/*"
    - "dist/provenance/*"
---

<div align="center">

# 🧩 **KFM Unified Pipeline Idempotency, Safety & Governance Pattern**  

### Deterministic ETL · Write-Ahead Logging · Atomic Publishing · CARE-Aligned Masking · Energy + Carbon Telemetry  

`docs/pipelines/patterns/idempotent-safety-governance.md`

**Diamond⁹ Ω / Crown∞Ω Ultimate Certified**

</div>

---

## 📁 1. Directory Layout

```text
📁 docs/
└── 📁 pipelines/
    └── 📁 patterns/
        📄 idempotent-safety-governance.md    # ← This file (unified governance pattern)
        📁 idempotent-node/
        │   📄 README.md                      # Idempotent ETL node pattern
        └── 📄 event-driven-deterministic-ingest.md

📁 src/
└── 📁 pipelines/
    └── 📁 _common/
        📄 wal.py                             # WAL utilities
        📄 atomic_io.py                       # Atomic write/rename helpers
        📄 idempotency.py                     # Idempotency key helpers
        📄 care_masking.py                    # CARE masking + generalization
        📄 observability.py                   # Metrics + tracing helpers
        📄 retries.py                         # Retry + backoff policies

📁 data/
└── 📁 work/
    └── 📁 <pipeline>/
        📄 <key>.wal                          # Pipeline WAL files (optional FS-backed)
📁 data/
└── 📁 processed/
    └── 📁 <pipeline>/
        📄 <key>.parquet                      # Canonical processed outputs
📁 data/
└── 📁 dlq/
    └── 📁 <pipeline>/
        └── 📁 <YYYY-MM-DD>/
            📄 <key>.json                     # DLQ records for failed runs

📁 schemas/
└── 📁 telemetry/
    📄 pattern-idempotent-safety-governance-v3.json
```

---

## 📘 2. Purpose

This pattern defines the **authoritative operational standard** for all KFM ingestion, transformation, and publishing pipelines.

Pipelines implementing this pattern must:

- Execute **idempotently** (safe retried runs, no duplicate effects).  
- Be **replayable** under WAL with deterministic results.  
- Publish **atomically** to processed tiers or versioned branches.  
- Honor **FAIR+CARE** via explicit masking and governance checks.  
- Emit complete **OpenTelemetry, energy, carbon, cost** telemetry.  
- Pass CI/CD **governance tests** before promotion.

It sits above:

- **Idempotent ETL Node Pattern** — node-level semantics, and  
- **Event‑Driven Deterministic Ingestion Pattern** — event-triggered orchestration,

and provides a **unified safety & governance envelope** for all pipeline architectures.

---

## 🔁 3. Idempotency Model

### 3.1 Canonical Idempotency Key

Every pipeline **MUST** derive a canonical idempotency key for each logical run:

```text
{source}:{aoi}:{h3_res}:{time_window}:{transform_version}
```

Where:

- `source` — upstream system ID (e.g., `sda`, `nexrad`, `hrrr`, `parcels`).  
- `aoi` — spatial AOI identifier (e.g., `kansas_statewide`, `flint_hills`).  
- `h3_res` — H3 resolution for aggregations or `"none"`.  
- `time_window` — logical interval (e.g., `2025-12-01`, `2025-12-07T00Z`).  
- `transform_version` — code/config version (e.g., Git SHA or semver tag).

The key governs:

- WAL record identity & filenames,  
- Output object naming,  
- Lineage node identity (graph + PROV),  
- Retry behaviors,  
- Rollback semantics.

### 3.2 WAL (Write-Ahead Log)

All pipeline work must occur under a WAL transaction, either:

- Backed by a **database table** (preferred), and/or  
- Mirrored via **FS artifacts** under `data/work`.

Canonical FS path (optional mirror):

```text
data/work/{pipeline}/{key}.wal
```

Logical WAL stages:

1. `begin` — record intent; attach idempotency key, inputs, config snapshot.  
2. `compute` — transforms run; intermediate artifacts recorded.  
3. `validate` — schema, QA, CARE, and governance checks.  
4. `stage_atomic` — candidate outputs written to temp locations.  
5. `publish` — atomic promotion to processed or versioned branch.  
6. `commit` — mark WAL as APPLIED; telemetry + provenance finalized.

Failure at any stage triggers:

- Safe rollback of staged artifacts,  
- DLQ record emission,  
- Optional alerts (see §7).

---

## 🧱 4. Atomic Publishing

### 4.1 Rules for Filesystems / Object Stores

- Outputs **must NOT** be written directly to processed paths.  
- Required pattern:

  1. Write to temporary path (e.g., `*.tmp`).  
  2. Validate data (schema, QA, CARE, checksums).  
  3. Perform **atomic rename/move** into processed location:

     ```text
     data/processed/{pipeline}/{key}.parquet
     ```

- For multiple files, treat the set as a single **atomic unit** via:
  - A versioned directory, or  
  - A manifest file that becomes authoritative only upon commit.

### 4.2 lakeFS / Versioned Storage

For lakeFS or equivalent:

- Stage changes in a dedicated branch/commit.  
- Include metadata:
  - Checksums, schema versions, idempotency key, upstream hashes.  
- Commit as a **single atomic delta**.  
- Optionally, use **tags** for named dataset versions aligned with `key`.

### 4.3 Deterministic Transforms

Transforms **must**:

- Use fixed seeds derived from `transform_version` or `key`.  
- Refuse to publish if any of the following hold:

  - Schema mismatch vs expected schema (unapproved drift).  
  - Checksum drift for a given logical subset (if transform is expected to be stable).  
  - Row-count anomaly outside configured thresholds.

Thresholds and policies are captured in:

- Pipeline‑specific config under `src/pipelines/<pipeline>/config/`, and  
- Governance rules under `docs/analyses/metadata/` & audit reports.

---

## 📊 5. Observability & Safety Standards

### 5.1 Required Metrics

All runs must emit at least:

| Metric          | Description                               |
|-----------------|-------------------------------------------|
| `freshness_min` | Minutes from source timestamp to publish  |
| `pipeline_success` | Boolean per run (or 0/1 gauge)        |
| `energy_kwh`    | Energy consumed for the run              |
| `co2e_kg`       | Carbon footprint of the run              |
| `cost_usd`      | Cloud + compute cost estimate            |
| `row_delta_pct` | Percent change in rows vs prior version  |

Values must be logged to telemetry (conforming to the pattern telemetry schema) and should be visible in SLO dashboards.

### 5.2 Tracing (OpenTelemetry)

OTel spans should follow the canonical pipeline stages:

```text
extract → validate → transform → mask → publish
```

Each span should include attributes such as:

```text
kfm.pipeline
kfm.key
kfm.stage
kfm.version
kfm.lineage.inputs[]
kfm.lineage.outputs[]
kfm.energy_kwh
kfm.co2e_kg
kfm.cost_usd
```

### 5.3 Alerts

Alert classes include (non‑exhaustive):

- **Freshness SLO violations** (e.g., window > X minutes).  
- **Validation failures** (schema, domain, CARE).  
- **Masking compliance errors** (missing or failed generalization).  
- **Publish anomalies** (unexpected row deltas, out-of-range metrics).  
- **Retry exhaustion / circuit breaker activation**.

Alerts must integrate into KFM’s reliability and governance alerting channels.

---

## 🧿 6. CARE‑Aligned Masking Requirements

Pipelines handling potentially sensitive locations (cultural, ecological, heritage, archaeological, community‑governed) **must comply with CARE v2** and KFM data generalization standards.

Masking tools / strategies:

- **H3 generalization** (coarsening spatial resolution).  
- **Distance fuzzing** (displacing points within a bounded radius).  
- **Geometry suppression windows** (omitting detail below certain zooms).  
- **Grouping & aggregation** to hide individual sites.

Governance requirements:

- Masking (or explicit non‑masking rationale) must be:

  - Encoded in PROV as a distinct `Activity` (e.g., `care:Masking`),  
  - Recorded in audit logs where sovereign reviewers can inspect.

- Publishing is **blocked** unless CARE masking (or explicit exemption) is verified in the run’s validation report.

- Reversible details, if stored, must be:

  - Strictly access‑controlled,  
  - Excluded from public distributions and STAC assets,  
  - Visible only to sovereign reviewers / authorized teams.

---

## 🧨 7. DLQ + Replay System

### 7.1 DLQ Record Structure

Each failure event must emit a DLQ record:

```text
data/dlq/{pipeline}/{YYYY-MM-DD}/{key}.json
```

Containing (minimum):

- Input payload summary (or manifest references).  
- `failure_stage` (e.g., `validate`, `mask`, `publish`).  
- Error / stacktrace (sanitized for PII/sensitivity).  
- `retry_count`.  
- Lineage snapshot (inputs, attempted outputs).  
- Energy/cost consumption up to failure.

DLQ records must be:

- Discoverable by governance and reliability teams.  
- Linkable to OpenLineage & PROV records.

### 7.2 Replay Safety

Replay jobs must:

- Be **rate‑limited** and **time‑boxed** (avoid thundering herds).  
- Use **canary‑first** approach:
  - Reprocess in limited scope before full batch replay.  
- Always re‑run:
  - Validation,  
  - CARE masking,  
  - Telemetry emission.

Replay must be **WAL‑protected** and respect idempotency:

- If a prior `content_hash`/`key` has already been APPLIED,  
  - The effect is not duplicated,  
  - The WAL record should transition to SKIPPED or remain APPLIED.

---

## 📜 8. Governance Enforcement

### 8.1 Required Artifacts per Run

Each governed pipeline run must produce:

- **Schema validation report**  
  - Capturing which checks ran and their outcomes.  

- **SLSA attestation (v2+)**  
  - Referencing OpenLineage run IDs and code + artifact hashes.  

- **SBOM cross-check**  
  - Consistency of runtime environment with declared SBOM (`sbom.spdx.json`).  

- **Energy + carbon ledger entry**  
  - For sustainability tracking and FAIR+CARE reporting.  

- **PROV-O patch**  
  - Extension to the global provenance graph for this run.

### 8.2 CI/CD Tests

CI/CD must block merges or promotions when:

- Idempotency key format/derivation changes are **undocumented**.  
- Schema drift occurs without governance approval.  
- Required telemetry fields are missing or invalid.  
- Masking stage is absent where required (based on domain classification).  
- Lineage graph output is malformed or incomplete.  
- WAL transitions are invalid (e.g., PENDING → APPLIED without proper transaction).

CI should include:

- Unit tests for each helper (`wal.py`, `atomic_io.py`, `care_masking.py`, etc.).  
- Integration tests that simulate failure modes and replay behavior.

---

## 🧪 9. Reference Implementation (Python Sketch)

```python
from kfm_common.wal import WAL
from kfm_common.idempotency import make_key
from kfm_common.care_masking import apply_care_mask
from kfm_common.observability import emit_telemetry

def run_pipeline(pipeline: str, source, aoi, h3_res, time_window, transform_version, inputs):
    key = make_key(source, aoi, h3_res, time_window, transform_version)
    with WAL(pipeline, key).begin() as txn:
        tmp = f"data/work/{pipeline}/{key}.parquet.tmp"

        # Deterministic compute
        df = compute(inputs, seed=transform_version)

        # CARE-aligned masking
        safe = apply_care_mask(df, policy="heritage_sensitive_v2")

        # Validation (schema + domain + CARE)
        validate(safe, EXPECTED_SCHEMA, EXPECTED_RANGES)

        # Stage
        write_parquet(safe, tmp)
        checksum = sha256_file(tmp)

        # Atomic publish
        final_path = f"data/processed/{pipeline}/{key}.parquet"
        atomic_move(tmp, final_path)

        # Telemetry + lineage
        emit_telemetry(
            pipeline=pipeline,
            key=key,
            checksum=checksum,
            energy_kwh=txn.energy_kwh,
            co2e_kg=txn.co2e_kg,
            cost_usd=txn.cost_usd,
        )
        txn.commit()
```

This sketch must be specialized per pipeline, but the semantics:

- WAL → compute → mask → validate → atomic publish → telemetry → commit

are non‑negotiable for governed pipelines.

---

## 🧭 10. Version History

| Version | Date       | Author / Steward            | Notes                                                         |
|---------|------------|-----------------------------|---------------------------------------------------------------|
| v11.2.4 | 2025-12-07 | Reliability + FAIR+CARE Council | First unified idempotency, safety & governance pattern under KFM-MDP v11.2.4. |

---

<div align="center">

**Kansas Frontier Matrix — Reliability · Ethics · Reproducibility**  

[⚖️ Root Governance](docs/standards/governance/ROOT-GOVERNANCE.md) ·  
[📦 SBOM](releases/v11.2.4/sbom.spdx.json) ·  
[🧾 Manifest](releases/v11.2.4/manifest.zip)

</div>