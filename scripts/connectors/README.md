# `scripts/connectors/` — KFM Dataset Connectors (Ingestion + Promotion Runners) ️🧭
![Governed](https://img.shields.io/badge/governed-artifact-2b6cb0)
![Evidence-first](https://img.shields.io/badge/evidence--first-required-0f766e)
![Fail-closed](https://img.shields.io/badge/policy-default%20deny-111827)
![Promotion](https://img.shields.io/badge/promotion%20contract-required-critical)
![spec_hash](https://img.shields.io/badge/spec__hash-RFC8785%20JCS%20%2B%20sha256-6a5acd)
![Catalogs](https://img.shields.io/badge/catalogs-DCAT%20%7C%20STAC%20%7C%20PROV-2563eb)

This folder contains **dataset-scoped connector runners** (thin CLI scripts) that operationalize KFM’s governed data lifecycle:

**Upstream → Raw (immutable) → Work (receipts + validation) → Processed (publishable) → Catalogs (DCAT/STAC/PROV)**

> [!IMPORTANT]
> **Processed is the only publishable truth.**  
> Connectors may write to `raw/` and `work/` during ingestion, but **nothing** here is allowed to “serve” data.
> Serving is done **only** via the governed API + policy boundary (trust membrane).

> [!WARNING]
> **Fail-closed rule:** If license, sensitivity classification, receipts, checksums, catalogs, or policy inputs are missing → **deny promotion / abort publish**.  
> No “best effort publish.” No silent redaction.

---

## Table of contents
- [Governance header](#governance-header)
- [What is a “connector” in KFM](#what-is-a-connector-in-kfm)
- [Connector contract](#connector-contract)
- [Directory layout](#directory-layout)
- [Common CLI contract](#common-cli-contract)
- [Artifact obligations](#artifact-obligations)
- [Idempotency and backfills](#idempotency-and-backfills)
- [Policy, sensitivity, and redaction](#policy-sensitivity-and-redaction)
- [Testing and CI gates](#testing-and-ci-gates)
- [Add a new connector](#add-a-new-connector)
- [Troubleshooting](#troubleshooting)
- [Glossary](#glossary)
- [References](#references)

---

## Governance header
| Field | Value |
|---|---|
| Document | `scripts/connectors/README.md` |
| Status | **Governed** |
| Applies to | dataset-scoped ingestion runners; raw/work/processed zone discipline; Promotion Contract behavior |
| Version | `v3.0.0-draft` |
| Effective date | `2026-02-16` (America/Chicago) |
| Owners | `../../.github/CODEOWNERS` *(required; if missing → governance gap)* |
| Review triggers | Any change affecting: zone writes, promotion behavior, receipts/catalog obligations, policy/sensitivity handling, spec hashing |

---

## What is a “connector” in KFM

A **connector** is the KFM component that “touches upstream reality” and turns it into governed, reproducible artifacts.

- It **discovers** upstream capabilities (endpoints, formats, auth needs, rate limits).
- It **acquires** upstream data (incremental windows if possible; snapshot+diff if not).
- It **normalizes/transforms** into canonical formats (encoding, geometry CRS, time model).
- It **validates** and emits machine-readable gate reports.
- It **publishes** by promoting immutable versions into `processed/` **only** when Promotion Contract proofs exist.

> [!NOTE]
> In this repo, `scripts/connectors/**` are **operator-facing runners**.  
> The reusable pipeline logic should live in the pipeline layer (`../../pipelines/` and/or `../../src/`) behind contracts/interfaces.

### Truth path (connector perspective)
```mermaid
flowchart LR
  U[Upstream sources] --> C[Connector runner]
  C --> RAW[data/raw<br/>manifest + checksums]
  RAW --> WORK[data/work<br/>run_record + validation_report + run_manifest]
  WORK -->|Promotion Contract gate| PROC[data/processed<br/>immutable versioned artifacts + checksums]
  PROC --> CAT[data/catalog<br/>DCAT + STAC (if spatial) + PROV]
  CAT --> API[Governed API + Policy + Evidence Resolver]
```

---

## Connector contract

KFM’s shared ingestion contract is:

**discover → acquire → transform/normalize → validate → publish**

A connector in `scripts/connectors/<dataset_id>/` typically implements this contract as a set of runners:

| Contract step | Typical runner | Zone write scope | Must emit |
|---|---|---|---|
| `discover` | (often inside `ingest.*`) | none / work | capability cache (optional) |
| `acquire` | `ingest.(py|ts|sh)` | raw + work | raw manifest + raw checksums |
| `transform/normalize` | `transform.(py|ts|sh)` *(optional)* | work | deterministic outputs |
| `validate` | `validate.(py|ts|sh)` | work | `validation_report.json` |
| `publish` | `promote.(py|ts|sh)` | processed + catalog | `run_manifest.json` + catalogs + processed checksums |

> [!CAUTION]
> `promote.*` is the only step allowed to write to `data/processed/**` and `data/catalog/**`.

<details>
<summary><strong>Reference interface (conceptual)</strong> (click to expand)</summary>

```ts
interface DataSourceConnector {
  discover(ctx): Capabilities
  acquire(ctx, plan): RawManifest
  transform(ctx, manifest): WorkArtifacts
  validate(ctx, work): ValidationReport
  publish(ctx, work, report): DatasetVersionRef
}
```

</details>

---

## Directory layout

> [!IMPORTANT]
> The directory structure below is the **governed target**.
> If the repo differs, update this README *and* update validators/CI accordingly (no “docs drift”).

```text
scripts/
└─ connectors/
   ├─ README.md                    # (this file) connector runner contract + DoD
   ├─ _templates/                  # OPTIONAL: copy/paste skeletons (no secrets)
   │  └─ dataset_connector_skeleton/
   │     ├─ ingest.py
   │     ├─ validate.py
   │     ├─ promote.py
   │     └─ README.md
   └─ <dataset_id>/                # REQUIRED: one folder per dataset stream (snake_case)
      ├─ ingest.(py|ts|sh)         # REQUIRED: discover+acquire → raw/work
      ├─ transform.(py|ts|sh)      # OPTIONAL: deterministic work→work transforms
      ├─ validate.(py|ts|sh)       # REQUIRED: work gating (schema/geo/time/license/policy)
      ├─ promote.(py|ts|sh)        # REQUIRED: promotion to processed + catalogs + receipts
      ├─ backfill.(py|ts|sh)       # OPTIONAL: explicit historic reprocessing windows
      ├─ mapping.yml               # OPTIONAL: source→canonical mapping notes
      ├─ fixtures/                 # OPTIONAL: synthetic/generalized test slices (NO sensitive locations)
      └─ tests/                    # OPTIONAL: connector-specific unit/integration tests
```

### Naming rules
- `<dataset_id>` **MUST** match the dataset registry key (see `../../data/README.md#registry`).
- Use verbs that map to governance stages:
  - `ingest` (raw/work only)
  - `transform` (work only; deterministic)
  - `validate` (work gating)
  - `promote` (processed + catalogs + manifest)
  - `backfill` (explicit reruns; must emit receipts + audit artifacts)

---

## Common CLI contract

All dataset connector runners **MUST**:
- provide `--help` that matches real behavior
- accept `--dataset_id` (or infer from folder name, but still record it)
- accept `--spec` (governed run spec) and emit `spec_hash`
- support `--dry-run` where feasible (no writes outside `work/`)
- output machine-readable receipts/reports (not just logs)
- be idempotent when possible

### Recommended baseline flags
| Flag | Purpose |
|---|---|
| `--dataset_id <id>` | stable dataset identifier |
| `--run_id <id>` | override run ID (otherwise generate ULID/ISO-based run id) |
| `--spec <path>` | governed run spec (inputs to compute `spec_hash`) |
| `--since <iso>` / `--until <iso>` | time window for incremental harvest/backfill |
| `--config <path>` | connector config (YAML/JSON) |
| `--raw_dir <path>` / `--work_dir <path>` / `--processed_dir <path>` | override zone roots (CI/special ops only) |
| `--emit_catalogs` | emit DCAT/STAC/PROV as applicable |
| `--dry-run` | no writes outside `work/` |
| `--log_json` | structured logs for CI ingestion |

### Example usage (local dev)
```bash
# run inside the container (preferred for deterministic deps)
docker compose exec api python scripts/connectors/example_dataset/ingest.py \
  --dataset_id example_dataset \
  --spec pipelines/specs/example_dataset.json \
  --log_json

docker compose exec api python scripts/connectors/example_dataset/validate.py \
  --dataset_id example_dataset \
  --run_id run_2026-02-16T00:00:00Z \
  --log_json

docker compose exec api python scripts/connectors/example_dataset/promote.py \
  --dataset_id example_dataset \
  --run_id run_2026-02-16T00:00:00Z \
  --emit_catalogs \
  --log_json
```

---

## Artifact obligations

Connectors are accountable for producing the artifacts that make KFM **auditable** and **citable**.

### Minimum outputs by zone
| Zone | Must write | Why |
|---|---|---|
| `data/raw/<dataset_id>/` | `manifest.yml` + `checksums.sha256` | immutable capture + integrity |
| `data/work/<dataset_id>/runs/<run_id>/` | `run_record.json` + `validation_report.json` + `run_manifest.json` | receipts + gating |
| `data/processed/<dataset_id>/<version_id>/` | artifacts + `checksums.sha256` | publishable truth |
| `data/catalog/` | DCAT (always), STAC (if spatial), PROV (always) | discovery + lineage |

> [!IMPORTANT]
> Promotion is **merge-blocking** / **publish-blocking** unless:
> - receipts validate (`run_record`, `validation_report`, `run_manifest`)
> - processed checksums exist for every servable artifact
> - catalogs validate (DCAT required; PROV required; STAC conditional)
> - policy labels + sensitivity classification exist (missing ⇒ deny)

### Canonical artifact paths (quick reference)
```text
data/raw/<dataset_id>/manifest.yml
data/raw/<dataset_id>/checksums.sha256

data/work/<dataset_id>/runs/<run_id>/run_record.json
data/work/<dataset_id>/runs/<run_id>/validation_report.json
data/work/<dataset_id>/runs/<run_id>/run_manifest.json

data/processed/<dataset_id>/<version_id>/checksums.sha256

data/catalog/dcat/<dataset_id>.json
data/catalog/stac/<dataset_id>/collection.json              # if spatial
data/catalog/stac/<dataset_id>/items/<version_id>/*.json    # if spatial
data/catalog/prov/<dataset_id>/run_<run_id>.json
```

---

## Idempotency and backfills

### Idempotency
- Re-running a job **MUST NOT** mutate a published `DatasetVersion`.
- A run that produces different outputs must produce a **new version** (new `version_id`), never overwrite.

### Backfills
Backfills are not “reruns”; they are **explicit historical reprocessing windows**.

> [!NOTE]
> A backfill MUST:
> - be windowed (`--since/--until`)
> - emit receipts + audit artifacts
> - document expected runtime + batching strategy
> - be restart-safe and rate-limit aware

---

## Policy, sensitivity, and redaction

Connectors must treat **rights and sensitivity** as first-class inputs to publication.

### Baseline sensitivity classes (recommended)
- `public`
- `restricted`
- `sensitive-location`
- `aggregate-only`

> [!IMPORTANT]
> **Redaction/generalization is a governed transformation.**
> If you redact or generalize (fields or geometry):
> - raw stays immutable
> - processed outputs become derived versions
> - PROV lineage MUST record the transformation
> - receipts MUST summarize what was changed

### Secrets and auth (connector hygiene)
- never commit keys/tokens
- never print tokens/PII to logs
- prefer environment variables or secret managers
- implement provider rate limits + exponential backoff

---

## Testing and CI gates

Minimum test expectations per connector:
- **Unit**: mapping/type coercion helpers; cursor logic; hashing determinism
- **Integration**: run against a fixed small slice and assert stable counts + stable checksums
- **Contract**: at least one API query depends on the dataset and returns provenance bundle + respects policy redaction
- **Regression**: profiling metrics (null rates/min/max/key counts) are stable or explainably versioned

### Merge-blocking (recommended) checklist
- [ ] receipts validate (schemas)
- [ ] catalog validation passes (DCAT/STAC/PROV)
- [ ] checksums present + verified
- [ ] policy regression suite passes (default-deny, sensitive-location precision rules)
- [ ] docs updated (registry + connector docs) and link-check clean

---

## Add a new connector

> [!TIP]
> The smallest safe slice is:
> **one dataset → one promoted version → one API query proved with citations**.

### Step-by-step
1) **Register the dataset**
   - Update/create dataset profile in `../../data/registry/` (see `../../data/README.md#registry`)
2) **Create connector skeleton**
   - Add `scripts/connectors/<dataset_id>/ingest.py`, `validate.py`, `promote.py`
3) **Implement raw capture**
   - Write `data/raw/<dataset_id>/manifest.yml` + `checksums.sha256`
4) **Implement validation**
   - Emit `validation_report.json` with license + sensitivity + schema/geo/time checks
5) **Implement promotion**
   - Write immutable outputs to `data/processed/<dataset_id>/<version_id>/`
   - Compute processed checksums
   - Emit catalogs (DCAT always; STAC/PROV as applicable)
   - Emit `run_manifest.json` (Promotion Contract receipt)
6) **Wire CI**
   - Add fixture-based tests + validators so governance is enforced (fail closed)

### Definition of Done (connector integration ticket)
- [ ] dataset is registered (registry schema validates)
- [ ] connector implements discover/acquire/transform/validate/publish flow (even if discover is embedded)
- [ ] raw acquisition produces deterministic manifest + checksums
- [ ] validation gates exist and are CI-enforced
- [ ] policy labels defined; restricted fields/locations redacted per rules
- [ ] catalogs emitted (DCAT always; STAC/PROV as applicable) and link-check clean
- [ ] at least one API contract test passes for a representative query
- [ ] backfill strategy documented (historic ranges + batching + expected runtime)

<details>
<summary><strong>Starter “connector script header” template</strong> (click to expand)</summary>

```python
"""
KFM Connector Runner: <dataset_id>/<stage>

Stage: ingest|transform|validate|promote|backfill
Purpose:
Inputs:
Outputs:
Zone writes:
- raw: yes/no
- work: yes/no
- processed: yes/no (ONLY promote)
Governance invariants:
- Processed-only publishable truth
- Fail-closed on missing license/sensitivity/receipts/catalogs
- Emit receipts when promoting: run_record + validation_report + run_manifest
- Catalog obligations: DCAT always; STAC conditional; PROV always
"""
```

</details>

---

## Troubleshooting

### “Promotion blocked”
Expected blockers:
- missing/invalid `run_manifest.json`
- failed `validation_report.json` (license missing, sensitivity missing, schema/geo/time fails)
- processed checksums missing or mismatch
- catalogs missing/invalid or dangling refs

### “Non-deterministic output”
Fixes:
- run inside pinned containers
- capture `git_sha` + `image_digest` in receipts
- ensure stable ordering when hashing
- keep timestamps out of deterministic payloads (timestamps belong in receipts)

---

## Glossary
| Term | Meaning |
|---|---|
| **Connector** | Adapter/runners that acquire upstream truth and drive raw→processed promotion |
| **Receipt** | Machine-readable proof objects (`run_record`, `validation_report`, `run_manifest`) |
| **Promotion Contract** | Rule: no processed version without receipts + checksums + catalogs + policy classification |
| **spec_hash** | Deterministic identity for a run spec (`sha256(JCS(spec))`) |
| **Fail closed** | Missing inputs/proofs ⇒ deny/abort; never “publish anyway” |

---

## References
- Repo constitution + truth path: `../../README.md`
- Scripts layer contract: `../README.md`
- Data plane (zones + registry + Promotion Contract): `../../data/README.md`
- Pipeline layer contract: `../../pipelines/README.md`
- Policy-as-code (default deny + sensitivity/redaction): `../../policy/README.md`

> This README is a governed operational artifact. Keep it accurate, complete, and reviewable.
