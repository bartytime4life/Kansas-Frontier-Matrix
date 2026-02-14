# KFM Pipeline Connectors
![Governed Artifact](https://img.shields.io/badge/status-governed-informational)
![Evidence First](https://img.shields.io/badge/principle-evidence--first-success)
![Fail Closed](https://img.shields.io/badge/policy-default--deny-critical)

This directory contains **KFM data connectors**: adapter modules that integrate external sources (APIs/files/STAC/DCAT endpoints/etc.) into KFM’s **Raw → Work → Processed** truth path, producing required **STAC/DCAT/PROV** artifacts, checksums, and run receipts/records.

> [!IMPORTANT]
> **Processed is the only publishable source of truth.** Raw/Work are never served directly to users.  
> Runtime services must serve only from **Processed** artifacts referenced by **validated catalogs**.

---

## Why this folder exists

Connectors are the **only allowed** place to:
- talk to upstream systems (HTTP APIs, bulk downloads, file drops)
- translate provider-specific formats into KFM canonical artifacts
- write **run receipts**, **run records**, **validation reports**, and **catalog outputs**
- support **incremental updates** and **explicit backfills** without breaking provenance

Connectors are *not* the place to:
- implement UI, API endpoints, or direct database access
- bypass governance checks (promotion gates, validation, policy labeling)
- “fix” sensitive data exposure by improvisation (sensitivity is a first-class transformation with its own provenance chain)

---

## KFM truth path and where connectors fit

```mermaid
flowchart LR
  A[Upstream Provider\nAPI / Files / STAC / DCAT] --> B[Connector\nsrc/pipelines/connectors/*]
  B --> C[Raw Zone\nimmutable capture]
  C --> D[Work Zone\nnormalize + QA]
  D --> E[Processed Zone\npublishable artifacts]
  E --> F[Catalogs\nSTAC / DCAT / PROV + checksums]
  F --> G[Stores + Indexes]
  G --> H[Governed API + Policy\n(trust membrane)]
  H --> I[UI / Stories / Focus Mode]
```

---

## Folder layout

> [!NOTE]
> This is the **connector layer** only. The orchestrator/runner and shared pipeline utilities may live elsewhere under `src/pipelines/` (verify exact paths in repo).

Recommended structure:

```text
src/
  pipelines/
    connectors/
      README.md                      # this file
      _contracts/                    # connector interface, DTOs, config schemas
      _shared/                       # shared HTTP client, retry, auth helpers, parsing utils
      <source_id>/                   # one connector per upstream source
        connector.<ext>              # implementation (language/framework per repo)
        mapping/                     # canonical field mapping + transforms
        fixtures/                    # small deterministic fixtures for CI
        tests/                       # unit/contract/integration tests (as supported)
```

---

## Connector invariants (non-negotiables)

| Invariant | What it means for connectors |
|---|---|
| **Fail-closed** | If required inputs/metadata are missing, ambiguous, or invalid → **stop** and surface a clear error. No “best effort” promotion. |
| **Processed-only serving** | Raw/Work artifacts are **never** treated as publishable outputs. |
| **Promotion gate** | No promotion to Processed unless **catalogs + checksums + run record + validation report** exist and validate. |
| **Evidence-first** | Every user-visible claim must be traceable to a dataset version and (where applicable) specific source record IDs. |
| **Trust membrane preserved** | Connectors never create a side-channel that bypasses policy or auditability. |

---

## Connector contract

All connectors implement a single contract (interface) so orchestration, validation gates, and catalog writing are consistent.

### Interface

The canonical lifecycle is:

1. `discover()` – what changed / what is available
2. `acquire()` – fetch raw payload(s) into Raw zone
3. `transform()` – normalize into Work artifacts
4. `validate()` – schema/geo/time/license/sensitivity/provenance checks
5. `publish()` – write Processed artifacts + catalogs, emit run record(s)

Pseudocode:

```python
class DataSourceConnector:
    def discover(self, spec, state): ...
    def acquire(self, discovery, spec, state): ...
    def transform(self, raw_artifacts, spec, state): ...
    def validate(self, work_artifacts, spec, state): ...
    def publish(self, processed_artifacts, spec, state): ...
```

> [!TIP]
> Keep connector logic **deterministic** and **idempotent**:
> - repeated runs with the same inputs/spec should produce the same digests
> - avoid hidden “now()” behaviors unless explicitly recorded in receipts/records

---

## Connector configuration

Each connector is configured by a **connector spec** (YAML recommended) registered in the data source registry.

### Where config lives

Typical governed files (verify exact paths in repo; these are normative patterns from KFM docs):

- `data/sources/registry.yml` – global registry: dataset_id, title, license, cadence, etc.
- `data/sources/<dataset_id>.yml` – per-source connector config/spec

### Common config keys

| Key | Purpose |
|---|---|
| `schedule` | cadence / cron / polling strategy |
| `incremental_cursor` | watermark or cursor field(s) for incremental pulls |
| `auth` | reference to secret material (never store secrets in git) |
| `rate_limit` | provider-friendly throttling |
| `format_targets` | intended processed formats (e.g., parquet, geopackage, cog) |
| `policy_label` | sensitivity/access labeling for downstream policy enforcement |

Example spec:

```yaml
dataset_id: ks_example_dataset
source_id: example_provider
schedule: "0 2 * * *" # daily at 02:00
incremental_cursor:
  type: "timestamp"
  field: "updated_at"
auth:
  method: "oauth2"
  secret_ref: "vault://kfm/example_provider"
rate_limit:
  requests_per_minute: 60
format_targets: ["parquet"]
policy_label: "public|restricted|culturally_sensitive|pii_risk"
```

---

## Required outputs per run

Each connector run must emit **machine-checkable** artifacts for governance and auditability.

### Raw zone (immutable capture)

- raw fetch manifest / receipt (what was fetched, from where, when, with which preconditions)
- raw payload snapshot(s)
- checksums/digests

### Work zone (repeatable transforms + QA)

- normalized/intermediate artifacts
- validation report(s)
- QA summaries (optional but encouraged)

### Processed zone (publishable artifacts)

- query-ready datasets (e.g., Parquet/GeoPackage/COG as appropriate)
- stable record identifiers for evidence linking (see below)
- checksums
- catalogs: STAC/DCAT/PROV (validated and cross-linked)

---

## Run receipt and run record

### Run receipt (source acquisition receipt)

A run receipt is a typed record capturing “what we fetched” and anchoring it to reproducible identifiers:

- `fetched_at`
- `accessURL` (source)
- conditional request fields (e.g., `etag`, `last_modified`) when available
- `spec_hash` – content hash of the connector spec (canonicalized)
- `artifact_digest` – digest(s) of acquired artifact(s)
- `tool_versions`
- `policy_gate` summary (pass/fail + checks)

Example (illustrative):

```json
{
  "example": "kfm.run_receipt.v1",
  "fetched_at": "2026-02-13T00:00:00Z",
  "accessURL": "https://example.org/source",
  "etag": "W/\"abc123\"",
  "last_modified": "Wed, 12 Feb 2026 00:00:00 GMT",
  "spec_hash": "sha256:<spec>",
  "artifact_digest": "sha256:<artifact>",
  "tool_versions": {"pipeline": "1.0.0"},
  "policy_gate": {"status": "pass", "checks": ["license_present", "stac_present"]}
}
```

### spec_hash (how to compute)

- Canonicalize the spec deterministically (JSON Canonicalization Scheme / RFC 8785 recommended)
- Hash using SHA-256
- Store as `sha256:<hex>`

This allows KFM to compare runs, detect spec drift, and prove reproducibility.

### Run record (end-to-end run lineage)

A run record links:
- inputs (URIs + hashes)
- code identity (git sha / image digest)
- outputs (URIs + hashes)
- pointers to validation report and PROV record

Example (illustrative):

```json
{
  "run_id": "run_...",
  "dataset_id": "example_dataset",
  "inputs": [{"uri":"data/raw/example.csv","sha256":"..."}],
  "code": {"git_sha":"...","image":"kfm/pipeline:..."},
  "outputs": [{"uri":"data/processed/example.parquet","sha256":"..."}],
  "validation_report": "data/work/example/validation_report.json",
  "prov_ref": "data/catalog/prov/example/run_....json"
}
```

---

## Evidence linking: dataset versions and record IDs

KFM’s evidence-first contract requires:
- every claim can link to a **dataset_version_id**
- when referencing rows/features, the system can point to the exact record(s) used

Connector responsibilities:
- produce stable `dataset_id`
- ensure each processed row/feature contains a `source_record_id` (or equivalent stable identifier) suitable for evidence resolution
- ensure catalogs (DCAT/STAC/PROV) reference the correct dataset/version/run artifacts

---

## Validation gates (minimum)

Promotion to processed must be blocked unless these pass:

- **schema validation** (row-level types, required fields)
- **geospatial validation** (geometry validity, CRS consistency, bbox/extent sanity)
- **temporal validation** (time ranges coherent; no impossible timestamps)
- **license/attribution captured** in DCAT + restrictions encoded for policy
- **provenance completeness** (raw→work→processed activities + deterministic checksums)

> [!IMPORTANT]
> If any gate fails → do not publish processed artifacts. Emit a validation report and fail the run.

---

## Catalog outputs: DCAT / STAC / PROV (KFM profile)

KFM uses standards-aligned catalogs with a small enforced profile:
- **DCAT** for dataset discovery/interoperability
- **STAC** for geospatial assets (collections + items)
- **PROV** for lineage (entities/activities/agents)

Connectors must generate catalogs that:
- include required minimum fields
- cross-link (e.g., STAC collection links to DCAT dataset; DCAT references PROV activity)
- validate under CI

<details>
<summary><strong>Minimum DCAT/STAC/PROV fields (quick checklist)</strong></summary>

- DCAT: identifier, title, description, license, keyword(s), spatial/temporal, distribution(s), prov ref  
- STAC: collection id/title/license/extent + item assets and geometry/bbox/time  
- PROV: activity (run), entities (raw/work/processed artifacts), agent (connector/pipeline), relations

</details>

---

## Backfills and incremental loads

Backfills are **explicit**, **idempotent**, and must not overwrite history.

### Patterns
- **incremental cursor**: fetch only new/updated data since last watermark
- **snapshot + diff**: store snapshots and compute changes deterministically
- **time-window backfill**: reprocess a bounded interval as a new dataset version

Backfill rules:
- always produce a new dataset version / run lineage
- keep raw snapshots immutable (append-only)
- update catalogs only after validation gates pass

---

## Sensitivity and redaction (FAIR/CARE aligned)

If a dataset contains sensitive locations, culturally restricted knowledge, or PII risk:
- publish a **generalized derivative** for public use
- store precise data under **restricted access**
- both derivatives must have **separate provenance chains** documenting the redaction/transformation step

Connector obligations:
- classify sensitivity early (at least by Work stage)
- implement redaction/generalization as an explicit, logged transformation
- ensure `policy_label` (or equivalent) is present so the trust membrane can enforce access

---

## Security requirements (connector-specific)

Connectors commonly handle credentials and external network calls.

Do:
- keep secrets out of git (use secret refs)
- minimize scopes and rotate credentials
- implement safe retries/backoff and rate limiting
- record request preconditions (etag/last-modified) when available
- log in a way that avoids leaking secrets or sensitive payload

Don’t:
- print tokens, session cookies, or full raw payloads into logs
- introduce “temporary” hard-coded keys
- bypass validation/promotion gates to “get it working”

---

## Observability and operations

Each run should produce enough telemetry to answer:
- **What changed upstream?**
- **What exactly did we fetch?**
- **What code + config produced this dataset version?**
- **Did validation/policy gates pass?**
- **What is the freshness / staleness of the dataset?**

Minimum recommended signals:
- run status + duration
- artifacts written (URIs + digests)
- validation summary + gate failures
- catalog validation results
- backfill markers (if run is a backfill)

---

## Adding a new connector (thin-slice workflow)

### 1) Create connector implementation
- `src/pipelines/connectors/<source_id>/...`
- implement the connector contract (discover/acquire/transform/validate/publish)

### 2) Register the data source
- add entry to `data/sources/registry.yml`
  - `dataset_id`, `title`, `license`, `cadence`, etc.

### 3) Add the connector spec
- create `data/sources/<dataset_id>.yml`
  - include schedule, cursor, auth placeholder, policy_label

### 4) Add deterministic fixtures + tests
- fixtures must be small and synthetic (CI-fast)
- add:
  - unit tests for transforms
  - contract tests for config schema
  - integration test using fixtures (where feasible)

### 5) Ensure the first run produces required artifacts
- raw snapshot + run receipt
- work normalization + validation report
- processed output + catalogs + checksums

---

## Definition of Done (connector PR checklist)

- [ ] Connector exists at `src/pipelines/connectors/<source_id>/` and implements the connector contract
- [ ] Source registered in `data/sources/registry.yml` (dataset_id/title/license/cadence)
- [ ] Spec present at `data/sources/<dataset_id>.yml` including schedule/cursor/auth placeholder/policy label
- [ ] First run produces: raw snapshot + run receipt (etag/last-modified if present) + spec_hash + artifact digests
- [ ] Work stage produces: normalized outputs + **validation_report.json**
- [ ] Processed stage produces: query-ready artifacts (and stable `source_record_id` per record where applicable)
- [ ] Catalogs exist and validate: DCAT + STAC + PROV (cross-linked)
- [ ] Tests exist: unit + contract + (where feasible) integration; regression fixtures added
- [ ] Promotion is blocked on any validation/catalog failure (fail-closed)

---

## Troubleshooting playbook (common failure modes)

| Symptom | Likely cause | Expected fix |
|---|---|---|
| “Promotion blocked: catalog invalid” | missing required fields / broken cross-links | fix generator; run catalog validators locally |
| “Schema drift detected” | upstream changed field names/types | update mapping + bump version; add regression fixture |
| “Duplicate rows/features after incremental run” | cursor not stable or not persisted | refine cursor logic; ensure watermark persists in state |
| “Sensitive data exposed in processed output” | missing policy labeling or redaction transform | move redaction into explicit Work→Processed step; generate separate public derivative |

---

## Appendix: starter templates

<details>
<summary><strong>Connector spec (YAML)</strong></summary>

```yaml
dataset_id: ks_example_dataset
source_id: example_provider
schedule: "0 2 * * *"
incremental_cursor:
  type: "timestamp"
  field: "updated_at"
auth:
  method: "oauth2"
  secret_ref: "vault://kfm/example_provider"
rate_limit:
  requests_per_minute: 60
format_targets: ["parquet"]
policy_label: "public"
```

</details>

<details>
<summary><strong>Validation report (JSON)</strong></summary>

```json
{
  "dataset_id": "ks_example_dataset",
  "run_id": "run_...",
  "status": "pass|fail",
  "checks": [
    {"name": "schema_validation", "status": "pass"},
    {"name": "geometry_validity", "status": "pass"},
    {"name": "temporal_consistency", "status": "pass"},
    {"name": "license_present", "status": "pass"},
    {"name": "provenance_complete", "status": "pass"}
  ],
  "notes": []
}
```

</details>

<details>
<summary><strong>Catalog generation (high level)</strong></summary>

```text
Processed artifacts
  -> compute checksums
  -> generate DCAT dataset + distributions
  -> generate STAC collection + items
  -> generate PROV activity/entity graph
  -> validate all catalogs
  -> write run record pointing to validation + PROV ref
```

</details>

