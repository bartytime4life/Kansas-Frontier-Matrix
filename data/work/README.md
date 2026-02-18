# `data/work/` — Work Zone (Intermediate Pipeline Artifacts)

![Zone](https://img.shields.io/badge/zone-work-orange)
![Served by API](https://img.shields.io/badge/served_by_API-no-lightgrey)
![Promotion](https://img.shields.io/badge/promotion-fail--closed-critical)

> [!IMPORTANT]
> **`data/work/` is not a source of truth.**  
> Anything that will be **served, cited, or published** must be promoted to `data/processed/` through the **Promotion Contract** (policy + validation + receipts).

## Why this directory exists

KFM uses a **raw → work → processed** lifecycle to ensure only validated, reproducible artifacts become “truth” and intermediates do **not** leak into serving.  
`data/work/` is the **scratch + receipts** zone for reproducible ETL runs.

### Zones at a glance

| Zone | Role | Mutability | May be served/cited? |
|---|---|---:|---:|
| `data/raw/` | Immutable source captures (as obtained) | Write-once | ❌ |
| `data/work/` | Intermediate artifacts + run receipts | Ephemeral | ❌ |
| `data/processed/` | Publishable, versioned outputs + checksums | Immutable (per version) | ✅ |

> [!NOTE]
> This README defines **recommended** conventions for `data/work/`.  
> If a pipeline/dataset family defines a stricter structure, follow that.

---

## Non‑negotiable rules ✅ / ❌

- ✅ Pipelines **may** write intermediate artifacts here.
- ✅ Any run that might be promoted **must** emit receipts:
  - `run_record` (what ran)
  - `run_manifest` (what went in/out)
  - `validation_report` (what passed/failed)
- ✅ Work outputs must be **reproducible** from `data/raw/` + pipeline code + config.
- ❌ The API/UI (and Focus Mode) must never serve or cite directly from `data/work/`.
- ❌ No “manual promotion” (copying files into `data/processed/` by hand).
- 🔐 Do not store secrets (tokens/keys/passwords). Use ephemeral credentials and secret managers.

---

## Recommended directory layout 🗂️

```text
data/work/
├── README.md
├── .gitignore               # recommended: keep work mostly untracked
├── runs/                    # per-execution run directories (receipts + intermediates)
│   └── <dataset_family>/    # e.g. "glo_land_patents", "nhgis", "kansas_memory"
│       └── <run_id>/        # one ETL execution (time-sortable recommended)
│           ├── run_record.json
│           ├── run_manifest.json
│           ├── validation_report.json
│           ├── artifacts/   # intermediate outputs (NOT publishable)
│           ├── logs/        # structured logs (jsonl) + human logs (txt)
│           └── tmp/         # safe-to-delete scratch for the run
├── staging/                 # optional: unpacked zips, scratch downloads (non-truth)
└── cache/                   # optional: derived caches (safe to delete)
```

### What goes where

| Path | What lives here | Notes |
|---|---|---|
| `runs/<dataset_family>/<run_id>/` | A single reproducible ETL run | Receipts are required if run is promotable |
| `.../artifacts/` | Intermediate outputs (normalized tables, joins, reprojections, thumbnails) | Must **not** be served |
| `.../logs/` | Run logs (structured + human-readable) | Prefer append-only log files |
| `.../tmp/` | Scratch | Safe to delete |
| `staging/` | Convenience workspace | Avoid keeping anything long-term |
| `cache/` | Performance caches | Treat as disposable |

---

## Promotion flow (conceptual) 🔁

```mermaid
flowchart LR
  RAW["data/raw/\nImmutable inputs + checksums"] -->|ETL normalize + validate| WORK["data/work/\nIntermediates + run receipts"] -->|Promotion Contract\n(fail closed)| PROC["data/processed/\nPublishable artifacts + checksums + catalogs"]
```

> [!IMPORTANT]
> **Promotion is a gate, not a file move.**  
> A run can only be promoted when receipts exist and validation/policy checks pass.

---

## Receipt contract 📜

Receipts are the minimum evidence required for promotion gating and later auditability.

### Required receipts

| Receipt | Filename (recommended) | Purpose | Minimum contents (suggested) |
|---|---|---|---|
| Run record | `run_record.json` | “What ran, when, by whom, with what code” | `run_id`, `dataset_family`, `pipeline_id`, `git_commit`, `started_at`, `ended_at`, `status`, `runner` |
| Run manifest | `run_manifest.json` | “Exactly what inputs and outputs were used/produced” | `spec_hash`, input digests, output digests, versions, parameters |
| Validation report | `validation_report.json` | “What gates were checked and what happened” | gate list, pass/fail, metrics, drift notes, policy label outcomes |

<details>
<summary>📄 Minimal JSON skeletons (copy/paste)</summary>

```json
// run_record.json
{
  "run_id": "01J...ULID",
  "dataset_family": "example_dataset",
  "pipeline_id": "pipelines/example_dataset",
  "git_commit": "abcdef123456",
  "started_at": "2026-02-18T00:00:00Z",
  "ended_at": "2026-02-18T00:10:00Z",
  "status": "success",
  "runner": {
    "type": "ci|local|cluster",
    "host": "hostname",
    "user": "operator_or_service_account"
  }
}
```

```json
// run_manifest.json
{
  "run_id": "01J...ULID",
  "spec_hash": "sha256:...",
  "inputs": [
    {"path": "data/raw/<...>", "digest": "sha256:...", "role": "primary"}
  ],
  "outputs": [
    {"path": "data/work/runs/<...>/artifacts/<...>", "digest": "sha256:...", "role": "intermediate"}
  ],
  "params": {
    "crs_target": "EPSG:4326",
    "join_keys": ["geoid"]
  }
}
```

```json
// validation_report.json
{
  "run_id": "01J...ULID",
  "overall_status": "pass|fail|pass_with_waiver",
  "gates": [
    {"name": "schema", "status": "pass", "details": {}},
    {"name": "geometry_validity", "status": "pass", "details": {}},
    {"name": "license", "status": "pass", "details": {"license": "public_domain"}}
  ],
  "policy": {
    "labels_emitted": ["public"],
    "redactions_applied": false
  }
}
```

</details>

> [!NOTE]
> The exact receipt schemas may evolve; keep them **stable and machine-readable**, and version them if fields change.

---

## Promotion checklist ✅

Use this as the minimum bar before anything from a run is considered promotable:

- [ ] Receipts exist: `run_record`, `run_manifest`, `validation_report`
- [ ] `validation_report.overall_status` is `pass` (or has an approved waiver record)
- [ ] Inputs are traceable to `data/raw/` and include **checksums**
- [ ] Outputs include **checksums** and have stable paths/identifiers
- [ ] License + attribution are known and recorded (no “unknown license”)
- [ ] Provenance chain is complete enough to reconstruct the run
- [ ] Any sensitive fields/locations are labeled and redacted per policy

---

## Cleanup & retention 🧹

`data/work/` is allowed to be **ephemeral**.

Recommended practice:
- Keep only the last *N* runs per dataset family locally (or keep only runs referenced by open PRs).
- If a run is promoted, retain receipts and provenance artifacts in the governed locations (e.g., catalogs / PROV bundles) as defined by the promotion workflow.

> [!WARNING]
> Do not “clean up” a run that is still needed to reproduce a pending promotion or investigation.

---

## Security & sensitivity 🔐

This directory often contains:
- unpacked upstream archives
- intermediate joins
- logs that might include identifiers
- derived geometry at higher precision than what is publishable

Rules of thumb:
- Treat `data/work/` as **restricted-by-default** unless you know otherwise.
- Apply redaction as a first-class transformation (not an afterthought).
- Prefer short-lived credentials for any external fetch operations.
- Keep logs structured and avoid dumping raw secrets/headers/payloads.

---

## Related KFM areas

- `data/raw/` — immutable inputs
- `data/processed/` — publishable outputs served by the platform
- `data/stac/`, `data/catalog/dcat/`, `data/prov/` — catalog + provenance outputs (if present)
- `src/pipelines/` — ETL code that should write intermediates here and promote via gating

---

## Questions / changes

If you need to change the structure of `data/work/` for a dataset family:
1. Update the dataset’s pipeline contract/docs first.
2. Keep receipts stable (or version them).
3. Update CI gates and promotion logic accordingly.