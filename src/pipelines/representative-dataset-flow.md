---
title: "📦 Kansas Frontier Matrix — Representative Dataset Flow (SemVer, Idempotency, STAC) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/architecture/representative-dataset-flow.md"
version: "v10.4.2"
last_updated: "2025-11-16"
review_cycle: "Quarterly / Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.1/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.1/manifest.zip"
telemetry_ref: "../../../releases/v10.4.1/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/pipelines-representative-dataset-flow-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.1"
status: "Active / Enforced"
doc_kind: "Architecture"
intent: "data-ingestion-and-publication"
fair_category: "F1-A1-I1-R1"
care_label: "C2-A2-R2-E1"
audience: ["Data Engineering", "Docs", "FAIR+CARE Council", "Release Engineering"]
owners: ["@kfm-pipelines", "@kfm-release-eng"]
---

<div align="center">

# 📦 **Representative Dataset Flow — Watch → Validate → Transform → Version → Publish**  
`src/pipelines/architecture/representative-dataset-flow.md`

**Purpose:**  
Define the canonical, idempotent path for a “representative dataset” (e.g., `daily-stations.csv`) moving from  
remote source detection to STAC publication and Release packaging with strict SemVer, governance, and auditability.

</div>

---

## 🔎 Big Picture

- **Trigger:** A remote object’s **HTTP `ETag`** (content fingerprint) changes for `daily-stations.csv`.  
- **Safety rails:** Schema + content **Validator** gates everything.  
- **Determinism:** **Transformer** emits column-typed `stations.parquet` and updates `stac.json`.  
- **Versioning:**  
  - New column (additive, nullable) = backward-compatible ⇒ SemVer **minor** (e.g., `v1.4.0 → v1.5.0`).  
  - Fix-only with identical interface ⇒ **patch**.  
  - Breaking change (column removal/rename/type change) ⇒ **major**.  
- **Governance:** CI opens a **PR** summarizing row/column deltas, attaches artifacts for review, then **Release** bundles assets on merge.  
- **Signals:** A **Slack webhook** posts `run_id`, `version`, and links to PR/Release/STAC.  
- **Idempotency:** Re-runs with the same content hash **no-op** via an idempotency key.

---

## 🧭 Flow Overview (Mermaid)

~~~mermaid
flowchart TD
  W[Watcher detects ETag change on daily-stations.csv] --> V[Validator<br/>schema + content checks]
  V -->|pass| T[Transformer<br/>CSV → Parquet + STAC update]
  V -->|fail| X[Stop + file issue with validator logs]
  T --> D[Delta Detector<br/>row/column diff report]
  D --> S[SemVer Decision<br/>major / minor / patch]
  S --> P[PR<br/>summary, artifacts, checks]
  P --> R[Merge → GitHub Release + assets]
  R --> N[Slack webhook<br/>run_id · version · links]
  R --> I[Idempotency register<br/>content hash recorded]
  I -->|same content on re-run| Q[No-op]
~~~

---

## 🧪 Validation Gate (Pass/Fail)

**Validator responsibilities**

- **Schema contract**  
  - Required columns and types  
  - Primary key uniqueness  
  - Nullability rules  
  - Units and enumerations

- **Content sanity**  
  - Duplicate IDs  
  - Time monotonicity  
  - Geospatial bounds (Kansas AOI)  
  - Extreme outlier guardrails

- **Metadata completeness**  
  - Source URL  
  - License  
  - Provenance reference  
  - Checksum

- **Outputs**  
  - `validation_report.json` (artifact)  
  - CI annotations  
  - Fail-fast on critical issues

**Artifacts**

~~~text
artifacts/validation/
  ├─ validation_report.json
  ├─ schema_expected.json
  └─ sample_rows.csv
~~~

---

## 🔁 Transform & Metadata

**Transform**

- Deterministic CSV → `stations.parquet`  
- Column-typed (no schema drift)  
- Stable column order and row sort (e.g., `station_id, date`)  
- No lossy transformations

**STAC update**

- Update `stac.json` for the dataset:  

  - `assets.stations.href` → new Parquet path  
  - `assets.stations.roles` → ensure includes `["data","primary"]`  
  - `assets.stations.checksum:multihash` → recomputed  
  - `assets.stations.content_length` → updated  
  - `properties.kfm:version` → SemVer from decision  
  - `properties.kfm:run_id` → pipeline run identifier  
  - Append to `kfm:stac_version_history[]`

**Lineage attachments**

- `provenance.source_etag`  
- `provenance.content_hash`  
- `provenance.run_id`  
- `provenance.pipeline_version`

**Outputs**

~~~text
data/processed/stations/
  ├─ stations.parquet
  ├─ stac.json
  └─ checksums.txt
~~~

---

## 📊 Delta Detection & SemVer

**Delta Detector**

- **Row deltas**  
  - Counts of new / removed / modified rows  
  - Primary key churn analysis  

- **Column deltas**  
  - Additive columns (nullable) ⇒ backward-compatible  
  - Column removal, rename, or type change ⇒ breaking  
  - Semantic change (units / meaning) ⇒ breaking  

**SemVer decision**

- Encoded into `semver_decision.json` using a stable schema.

**Artifacts**

~~~text
artifacts/delta/
  ├─ column_diff.md
  ├─ row_diff_summary.json
  └─ semver_decision.json
~~~

---

## 🔐 Idempotency & No-Op

**Idempotency key**

- `idempotency_key = sha256(content_hash | source_uri | pipeline_version)`

**Behavior**

- If key **already exists** in idempotency ledger:
  - Skip transform, STAC update, PR & Release  
  - Emit “no change” notification (Slack / logs)

**Ledger**

- `pipelines/ledger/idempotency.sqlite` or a table in the metadata DB  
- Must be **append-only**, version-pinned, and backed up.

---

## 🧰 Pull Request (Human-in-the-Loop)

**PR content**

- Summary of source and change  
- ETag before/after  
- SemVer decision and rationale  
- Sample rows and deltas  
- Governance declarations (license, CARE category)  
- Links to artifacts and STAC validation results

**Checks**

- `validate.yml` (schema + content)  
- `stac-validate.yml`  
- `faircare-validate.yml`  
- SBOM + license scans  
- Unit & integration tests for dataset consumers

**Reviewers** (enforced via CODEOWNERS)

- Data Engineering representative  
- FAIR+CARE steward  
- Release Engineering representative  

**PR Template Snippet**

~~~text
### Summary
- Source: <url>
- ETag: <old> → <new>
- SemVer: <prev> → <next> (reason: additive column)

### Deltas
- Rows: +12, -0, changed 3
- Columns: +1 (new: `station_class`), 0 removed, 0 breaking

### Artifacts
- artifacts/validation/validation_report.json
- artifacts/delta/column_diff.md
- updated data/processed/stations/stac.json
~~~

---

## 📦 Release Packaging & Notifications

**On merge:**

- Tag created: `dataset/stations@vX.Y.Z`  
- GitHub Release created with this tag  
- Assets attached (see below)  
- Slack notification sent with `run_id`, `version`, and links

**Release Asset Layout**

~~~text
releases/datasets/stations/vX.Y.Z/
  ├─ stations.parquet
  ├─ stac.json
  ├─ checksums.txt
  ├─ validation_report.json
  ├─ column_diff.md
  ├─ row_diff_summary.json
  ├─ semver_decision.json
  ├─ manifest.zip
  └─ sbom.spdx.json
~~~

Slack message includes:

- `run_id`  
- `version`  
- link to PR  
- link to Release  
- dataset identifier  
- row/column deltas summary  

---

## 🧾 STAC Fields (Minimal Update Set)

| Field                                | Update Rule                         | Example                                              |
| ------------------------------------ | ----------------------------------- | ---------------------------------------------------- |
| `assets.stations.href`               | Replace with new artifact path      | `data/processed/stations/stations.parquet`           |
| `assets.stations.roles`              | Ensure includes `data`,`primary`    | `["data","primary"]`                                 |
| `assets.stations.checksum:multihash` | Recompute for new Parquet           | `1220…`                                              |
| `assets.stations.content_length`     | Update based on new file size       | `1234567`                                            |
| `properties.kfm:version`             | Set from SemVer decision            | `1.5.0`                                              |
| `properties.kfm:run_id`              | Set from pipeline run               | `runs/2025-11-16-0012`                               |
| `kfm:stac_version_history[]`         | Append entry with rationale         | `{from:"1.4.0",to:"1.5.0",reason:"additive column"}` |

---

## 🧭 SemVer Decision Matrix (Quick Reference)

| Change                                  | SemVer      | Notes                                                                        |
|-----------------------------------------|------------|------------------------------------------------------------------------------|
| Add column with default/nullable        | **Minor**   | Backward-compatible                                                          |
| Add row(s) only                         | Patch/Minor | Patch if purely additive; Minor if it affects exposed aggregates             |
| Fix data value without interface change | Patch       | Corrective                                                                   |
| Change type / remove / rename column    | **Major**   | Breaking                                                                     |
| Change primary key semantics            | **Major**   | Breaking                                                                     |

---

## 🧩 CI/CD Hooks (GitHub Actions)

**Recommended workflows**

- `data-watch.yml`  
  - Detect remote changes (polling or webhook)  
  - Enqueue pipeline runs when ETag changes  

- `validate.yml`  
  - Run schema + content validation  
  - Upload validation artifacts  

- `transform.yml`  
  - Convert to Parquet  
  - Update STAC  
  - Compute deltas and SemVer decision  

- `stac-validate.yml`  
  - Validate updated STAC items/collections  

- `release.yml`  
  - Tag + create Release  
  - Attach artifacts  
  - Trigger Slack notification  

- `faircare-validate.yml`  
  - FAIR+CARE checklist (license, CARE label, provenance, redaction rules)  

---

## 📑 Governance & Audit

**Governance Ledger**

- Each run appends an entry to a Governance Ledger (JSONL / DB):  
  - `run_id`  
  - dataset ID  
  - `version_from`, `version_to`  
  - reviewer IDs  
  - license  
  - CARE classification  
  - content hashes  
  - link to Release  

**Reproducibility**

- Pin container images (`image@sha256:...`)  
- Record `pipeline_version`  
- Record tool versions used in validation & transform  

**SBOM**

- Update `sbom.spdx.json` for:  
  - pipeline containers  
  - validation tools  
  - transform tools  

**CARE & Access**

- If sensitive fields are detected:  
  - run redaction/generalization before publishing  
  - append CARE notes to STAC + Governance Ledger  

---

## 📁 Canonical File & Directory Layout (Excerpt)

~~~text
data/
├── raw/
│   └── daily-stations.csv                 # Raw source file synced from remote ETag
│
├── processed/
│   └── stations/
│       ├── stations.parquet               # Deterministic column-typed Parquet artifact
│       ├── stac.json                      # Updated STAC Item with SemVer + checksums
│       └── checksums.txt                  # SHA-256 file integrity + lineage hashes
│
└── stac/
    └── stations/
        └── stac.json                      # Previous STAC descriptor (for diff + history)

pipelines/
├── watcher/                                # Detect remote changes via ETag or webhook
├── validator/                              # Schema + content validator
├── transformer/                            # CSV → Parquet conversion + STAC update
├── delta/                                  # Row/column diff computation
├── release/                                # PR creation, Release assets, tagging
│
└── ledger/
    └── idempotency.sqlite                  # Ensures no-op behavior on identical content runs

artifacts/
├── validation/
│   ├── validation_report.json              # Full validator output (schema + content)
│   ├── schema_expected.json                # Expected schema contract version
│   └── sample_rows.csv                     # Extract of rows for human governance review
│
└── delta/
    ├── column_diff.md                      # Human-readable column changes
    ├── row_diff_summary.json               # Machine-readable row deltas
    └── semver_decision.json                # SemVer major/minor/patch decision record

releases/
└── datasets/
    └── stations/
        └── vX.Y.Z/
            ├── stations.parquet            # Release-published Parquet artifact
            ├── stac.json                   # Release-pinned STAC item
            ├── checksums.txt               # Hashes for Parquet, STAC, and metadata
            ├── validation_report.json      # Validator output for auditors
            ├── column_diff.md              # Column-level change summary
            ├── row_diff_summary.json       # Row-level delta summary
            ├── semver_decision.json        # Version decision + rationale
            ├── manifest.zip                # Release manifest bundle
            └── sbom.spdx.json              # SBOM for pipeline tools + environment
~~~

---

## ✅ Acceptance Criteria (Enforced by CI)

A dataset update is considered **valid** when:

- ETag change is detected and logged  
- Validation report exists and passes required checks  
- Deterministic Parquet artifact is produced  
- STAC item/collection updated and **passes validation**  
- Delta artifacts exist and SemVer decision is recorded  
- PR created with correct summary, artifacts, and governance metadata  
- On merge, Release exists with all required assets attached  
- Slack notification includes `run_id`, `version`, and links  
- Idempotency ledger updated; re-run with same content becomes a **no-op**

---

## 🔧 Implementation Notes

- Prefer **ETag** over Last-Modified as content identity; treat Last-Modified as advisory.  
- Use **SHA-256** for content hashing; encode via multihash for STAC.  
- Always sort rows + columns deterministically before hashing to prevent spurious SemVer bumps.  
- Ensure additive columns are:
  - documented in STAC’s `assets.stations.fields` or equivalent metadata  
  - clearly described in PR and Release notes.  
- For backfills or “time travel” updates, ensure:
  - `effective_date` is tracked  
  - SemVer reflects interface changes, not data volume alone.

---

## 🧰 CLI Sketch (For Repo Tools)

~~~text
kfm-data watch \
  --source daily-stations.csv

kfm-data validate \
  --input data/raw/daily-stations.csv \
  --schema schemas/stations.schema.json

kfm-data transform \
  --input data/raw/daily-stations.csv \
  --out data/processed/stations/stations.parquet

kfm-data delta \
  --prev-tag dataset/stations@1.4.0 \
  --curr-file data/processed/stations/stations.parquet

kfm-data semver decide \
  --delta artifacts/delta/row_diff_summary.json \
  --columns artifacts/delta/column_diff.md

kfm-data stac update \
  --item data/stac/stations/stac.json \
  --asset data/processed/stations/stations.parquet

kfm-data release create \
  --dataset stations \
  --version 1.5.0 \
  --attach releases/datasets/stations/v1.5.0/*
~~~

---

## 📜 Version History

| Version | Date       | Summary                                                                                                                      |
|--------:|------------|------------------------------------------------------------------------------------------------------------------------------|
| v10.4.2 | 2025-11-16 | Polished to KFM-MDP v10.4.1: converted inner fences to `~~~`, clarified CI hooks and governance ledger details              |
| v10.4.1 | 2025-11-16 | Initial specification for Representative Dataset Flow, including SemVer matrix, idempotency, PR/Release, STAC update rules |

---
