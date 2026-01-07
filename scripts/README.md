<!--
📌 This README defines the repo-wide automation surface for KFM.
🗓️ Last updated: 2026-01-07
-->

# 🧰 `scripts/` — KFM Automation Toolkit

![Safe by default](https://img.shields.io/badge/safe--by--default-yes-success)
![Idempotent](https://img.shields.io/badge/idempotent-expected-blue)
![Provenance first](https://img.shields.io/badge/provenance--first-required-informational)
![Documented](https://img.shields.io/badge/--help-required-brightgreen)
![Shell](https://img.shields.io/badge/shell-bash%20%7C%20pwsh-lightgrey)
![Python](https://img.shields.io/badge/python-cli%20scripts-3776AB)
![GIS](https://img.shields.io/badge/gis-GDAL%20%7C%20PostGIS-2b9348)
![Contracts](https://img.shields.io/badge/contracts-OpenAPI%20%7C%20JSON%20Schema-0aa3a3)
![Security](https://img.shields.io/badge/security-hostile--inputs%20%2B%20deny--by--default-red)

> Repeatable commands for dev, data ops, GIS/remote‑sensing workflows, modeling/simulation orchestration, and deployment “glue”.  
> **Safe-by-default** ✅ • **Idempotent** ♻️ • **Provenance-first** 🧾 • **Documented** 📓

> [!IMPORTANT]
> `scripts/` is **orchestration**, not “the truth.”  
> If something becomes **core behavior**, move the implementation into `src/` (or `api/src/`) and let scripts call it.

> [!IMPORTANT]
> KFM pipeline ordering is absolute:  
> **ETL → STAC/DCAT/PROV Catalogs → Graph → APIs → UI → Story Nodes → Focus Mode**  
> Scripts must not create “mystery artifacts” that bypass catalogs/provenance.

---

<details>
<summary><b>🧭 Table of contents</b></summary>

- [🎯 What belongs here (and what doesn’t)](#what-belongs-here)
- [🏁 Quickstart](#quickstart)
- [🗂️ Recommended folder map](#folder-map)
- [🧱 Standard script contract](#script-contract)
- [🧭 Data lifecycle rules scripts must respect](#data-lifecycle)
- [🧨 Safety guardrails (non-negotiable)](#safety-guardrails)
- [🧾 Observability & provenance](#observability)
- [🧱 Script templates](#script-templates)
- [🗺️ GIS + PostGIS scripting tips](#gis-postgis)
- [🛰️ Remote sensing scripting tips](#remote-sensing)
- [🧪 QA scripts (contracts & acceptance gates)](#qa-scripts)
- [🧩 Adding a new script (checklist)](#adding-a-script)
- [📋 Script registry](#script-registry)
- [🧯 Troubleshooting (CLI “kung fu”)](#troubleshooting)
- [🤝 Related docs (inside this repo)](#related-docs)
- [📚 Project reference library influence map](#reference-library-influence-map)
- [✅ Definition of “done” for a script](#definition-of-done)

</details>

---

<a id="what-belongs-here"></a>

## 🎯 What belongs here (and what doesn’t)

### ✅ Good fits for `scripts/`
- 🧱 **Environment bootstrap**: install deps, initialize DB schema, load seed/reference data
- 🧰 **Dev helpers**: run local stack, health checks, smoke tests, “make my laptop match CI”
- 🗺️ **GIS tooling wrappers**: convert formats, validate CRS, generate tiles, build COGs, raster reprojection
- 🛰️ **Remote sensing helpers**: Earth Engine export triggers, index builders, downloaders for *derived* products
- 🤖 **Model/simulation orchestration**: run pipelines/jobs with recorded configs, seeds, and output receipts
- 🧪 **Acceptance gates**: schema validation, link checks, provenance completeness, contract checks (OpenAPI/JSON Schema)
- 🕒 **Scheduled jobs**: backups, cache cleanup, log rotation (cron/Kubernetes CronJob)

### ❌ Not a good fit for `scripts/`
- 🚫 **Core ETL logic** (belongs in `src/pipelines/`)
- 🚫 **Domain/business rules** (belongs in `src/` domain/application layers or `api/src/`)
- 🚫 **Duplicate implementations** of pipeline steps (scripts should *call into* canonical modules)
- 🚫 **One-off “forever scripts”** that bypass provenance, approvals, or classification propagation
- 🚫 **Unreviewed publishing** (any path that creates “published-looking” outputs without STAC/DCAT/PROV)

> [!TIP]
> Scripts are the “buttons and levers.” If it’s “the engine,” it belongs in `src/`. 🔧➡️🏗️

---

<a id="quickstart"></a>

## 🏁 Quickstart

### 1) Discover available scripts
- Browse by category (e.g., `scripts/dev/`, `scripts/db/`, `scripts/gis/`, `scripts/qa/`)
- Run help first:
  - `./scripts/<path>/my_script.sh --help`
  - `pwsh ./scripts/<path>/my_script.ps1 --help`
  - `python scripts/<path>/my_script.py --help`

> [!IMPORTANT]
> Every script **must** support `--help` and include **at least 2 runnable examples**.

### 2) Set environment (no secrets in git) 🔐
- Copy env template (repo-level):
  - `cp .env.example .env`
- Load env in your shell (or pass vars inline).

Scripts should read config from:
- environment variables ✅
- or a config file *path* provided via env ✅

**Never hardcode credentials. Never print secrets.**

### 3) Default to safety ✅
Preferred contract:
- `--dry-run` (default) → prints actions
- `--apply` → performs changes
- `--yes` → skips prompts  
- `--env {dev|staging|prod}` → required when environment matters

---

<a id="folder-map"></a>

## 🗂️ Recommended folder map

> This repo may evolve — keep this README updated when adding new categories.

```text
📁 scripts/
├─ 🧰 _lib/               # shared helpers (logging, env validation, guardrails)
├─ 🧰 dev/                # local stack helpers, smoke tests, DX scripts
├─ 🧱 bootstrap/          # first-run setup (deps, DB init, seed/reference loads)
├─ 🗄️ db/                 # migrations, backups, restores, snapshots, sanity checks
├─ 🕸️ graph/              # graph sync/load helpers (must reference catalog IDs)
├─ 🏷️ catalogs/            # STAC/DCAT/PROV build + validate wrappers (usually call src/)
├─ 🧪 pipelines/           # pipeline runners (thin wrappers around src/pipelines)
├─ 🗺️ gis/                # geoprocessing helpers (vector/raster, tiling, CRS checks)
├─ 🛰️ remote_sensing/     # GEE wrappers, export tracking, indexing helpers
├─ 🧮 simulation/         # scenario runners (must record seeds/configs + provenance)
├─ 🤖 ml/                 # train/eval runners (must record datasets + metrics + provenance)
├─ 🧪 qa/                 # validators, contract checks, dataset acceptance gates
├─ 🔐 security/           # secrets scans, sensitive-data scans, hostile-input checks
├─ 🧹 housekeeping/       # rotate logs, purge caches, cleanup artifacts
└─ 🧪 ci/                 # stable entrypoints used by CI (deterministic, non-interactive)
```

> [!NOTE]
> If you add a new category folder, also add it to the Table of Contents and script registry. 🧩

---

<a id="script-contract"></a>

## 🧱 Standard script contract

To keep `scripts/` predictable (and safe), every script **must** follow the same behavioral contract.

### ✅ CLI interface requirements
All scripts must support:

- `--help` prints:
  - purpose (1–2 lines)
  - inputs/outputs (paths or tables)
  - side effects (DB writes? file writes? network calls?)
  - required env vars
  - examples (at least 2)

- Modes:
  - `--dry-run` is the default (or clearly supported)
  - `--apply` performs writes/changes

- Safety:
  - `--yes` skips interactive prompts
  - `--env {dev|staging|prod}` when environment matters
  - if `--env prod` + `--apply` → require an additional explicit prod acknowledgement flag
    - e.g., `--i-acknowledge-production`

- Output hygiene (recommended):
  - `--run-id <id>` (or env `KFM_RUN_ID`) to correlate logs + provenance
  - `--log-json` for machine-readable logs (JSONL)
  - `--outdir <path>` for artifact destinations
  - `--no-network` default (or at least an explicit `--allow-network` for scripts that fetch remote content)

**Exit codes (standard):**
- `0` success
- `2` usage/CLI error (bad args)
- `3` validation failure (inputs invalid; catalogs missing; schema mismatch) *(recommended)*
- `>=10` runtime failures (I/O, network, DB, permissions, unexpected exceptions)

> [!NOTE]
> It’s okay to add flags, but don’t break the standard ones (`--help`, `--dry-run`, `--apply`, `--yes`, `--env`).  
> Consistency beats cleverness. 🧠✅

### 🧾 “Script header” (recommended)
At the top of each script, include:
- Name
- Purpose
- Inputs / Outputs
- Side effects
- Owner/team (or “unowned”)
- Safety defaults (`dry-run` default, confirmation behavior)
- Provenance expectations (what IDs/receipts are written)

---

<a id="data-lifecycle"></a>

## 🧭 Data lifecycle rules scripts must respect

KFM’s data work is **staged** and **traceable**. Scripts that ingest or transform data must:

1) 📥 Write raw inputs → `data/raw/<domain>/`  
2) 🧱 Write intermediates → `data/work/<domain>/`  
3) ✅ Write publishable outputs → `data/processed/<domain>/`  
4) 🗃️ Emit metadata + lineage artifacts (STAC/DCAT/PROV) **before** anything is used downstream

> [!IMPORTANT]
> If a script produces “evidence artifacts” (derived analyses, model outputs, generated layers),  
> treat them like first-class datasets: store them correctly, catalog them, and capture provenance. 🧾🧬

### ✅ “Thin wrapper” pattern (required for anything important)
If you’re tempted to put real transformation logic in a script, do this instead:
- implement core logic in `src/…` (pipelines/domain/services)
- keep the script as a thin CLI wrapper that:
  - validates inputs
  - calls the canonical module
  - writes run receipts/logs
  - triggers catalog/provenance generation

---

<a id="safety-guardrails"></a>

## 🧨 Safety guardrails (non-negotiable)

### ✅ Safe-by-default behavior
- 🛑 **No destructive actions by default**
- 🧪 Default mode should be `--dry-run`
- 🧯 Destructive actions require explicit confirmation flags

**Recommended confirmation pattern**
- `--dry-run` prints what would happen  
- `--apply` performs changes  
- `--yes` skips interactive prompts  
- `--env {dev|staging|prod}` and **refuse** dangerous combos without extra confirmation  

### 🏭 Production protection
Scripts that can write to prod must:
- require explicit `--env prod`
- require an additional “I really mean it” flag (`--i-acknowledge-production`)
- log who/what/when:
  - user (if detectable), host, timestamp, run_id
  - git SHA (if available)
  - container digest (if available)

### 🧊 Atomic writes (strongly recommended)
For file outputs:
- write to `*.tmp` then rename to final output (atomic on most OS/filesystems)
- never leave half-written “published” outputs behind
- prefer content-addressed paths (hash-in-path) for immutable artifacts

### 🧯 Hostile input posture
Assume inputs are hostile (files from the world, archives, rasters, JSON, OBJ models, PDFs).
- validate file types (allowlists)
- enforce size limits and decompression limits
- treat URL fetching as high-risk (SSRF; private IP blocks; allowlists)
- isolate complex parsing when possible (containers / sandboxing / subprocess limits)

> [!CAUTION]
> If a script can delete, drop, truncate, overwrite, revoke, or publish:  
> **dry-run default + explicit apply + explicit confirmation** is mandatory. 🚫🧨✅

---

<a id="observability"></a>

## 🧾 Observability & provenance

Every script should:
- 🪵 Use structured logging (`timestamp`, `level`, `component`, `run_id`)
- 🧷 Print where outputs were written (paths) + what changed (counts, bytes, features)
- 🧾 Capture provenance inputs/outputs:
  - input file list + checksums (when feasible)
  - key parameters (bbox, time window, model version, CRS, resolution, seeds)
  - IDs/paths to produced STAC/DCAT/PROV artifacts

### 🧾 Recommended “run receipt” (optional but 🔥)
When `--apply` is used, write a small receipt:
- human-readable: `mcp/runs/<RUN-ID>/MANIFEST.md`
- machine-readable: `data/prov/<RUN-ID>.jsonld`

Receipt should include:
- git SHA, environment, operator identity (if available)
- inputs + checksums
- outputs + checksums
- produced catalog IDs (collection/item/dataset IDs)
- warnings (redactions applied, schema deviations, missing optional evidence)

> 🎛️ If it’s not reproducible, it’s not done.

---

<a id="script-templates"></a>

## 🧱 Script templates

<details>
<summary><b>🐚 Bash template (portable + strict)</b></summary>

```bash
#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

usage() {
  cat <<'EOF'
Usage:
  ./scripts/example.sh [--dry-run] [--apply] [--yes] [--env dev|staging|prod] [--run-id ID]

Purpose:
  Example KFM script (safe-by-default, idempotent).

Examples:
  ./scripts/example.sh --dry-run
  ./scripts/example.sh --apply --yes --env dev --run-id etl_20260107_120000_abcd123
EOF
}

DRY_RUN=1
APPLY=0
YES=0
ENVIRONMENT="${KFM_ENV:-dev}"
RUN_ID="${KFM_RUN_ID:-run-unknown}"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run) DRY_RUN=1; APPLY=0; shift ;;
    --apply)   APPLY=1; DRY_RUN=0; shift ;;
    --yes)     YES=1; shift ;;
    --env)     ENVIRONMENT="${2:-}"; shift 2 ;;
    --run-id)  RUN_ID="${2:-}"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown arg: $1" >&2; usage; exit 2 ;;
  esac
done

echo "[INFO] run_id=$RUN_ID env=$ENVIRONMENT dry_run=$DRY_RUN apply=$APPLY yes=$YES"

if [[ "$ENVIRONMENT" == "prod" && "$APPLY" -eq 1 ]]; then
  echo "[ERROR] Refusing to apply to prod without an explicit prod-ack flag." >&2
  echo "        Add a flag like: --i-acknowledge-production" >&2
  exit 2
fi

if [[ "$APPLY" -eq 1 && "$YES" -ne 1 ]]; then
  read -r -p "This will modify state. Type 'apply' to continue: " confirm
  [[ "$confirm" == "apply" ]] || { echo "Aborted."; exit 1; }
fi

# ✅ Put orchestration here (call into src/ modules, validate, write receipts)
echo "[OK] Done."
```

</details>

<details>
<summary><b>🐍 Python template (CLI + logging + exit codes)</b></summary>

```python
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import logging
import os
import sys
from dataclasses import dataclass

log = logging.getLogger("kfm.scripts")

@dataclass(frozen=True)
class Args:
    dry_run: bool
    apply: bool
    yes: bool
    env: str
    run_id: str
    log_json: bool

def parse_args(argv: list[str]) -> Args:
    p = argparse.ArgumentParser(
        prog="python scripts/example.py",
        description="Example KFM script (safe-by-default, idempotent).",
    )
    mode = p.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="Print actions without changing state.")
    mode.add_argument("--apply", action="store_true", help="Perform actions (writes/changes).")
    p.add_argument("--yes", action="store_true", help="Skip interactive prompts.")
    p.add_argument("--env", default=os.getenv("KFM_ENV", "dev"), choices=["dev", "staging", "prod"])
    p.add_argument("--run-id", default=os.getenv("KFM_RUN_ID", "run-unknown"))
    p.add_argument("--log-json", action="store_true", help="Emit JSON logs (JSONL friendly).")
    ns = p.parse_args(argv)

    dry_run = ns.dry_run or not ns.apply  # safe default
    return Args(
        dry_run=dry_run,
        apply=ns.apply,
        yes=ns.yes,
        env=ns.env,
        run_id=ns.run_id,
        log_json=ns.log_json,
    )

def emit(event: dict, *, log_json: bool) -> None:
    if log_json:
        print(json.dumps(event, ensure_ascii=False))
    else:
        log.info("%s", event)

def main(argv: list[str]) -> int:
    args = parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s %(message)s")

    if args.env == "prod" and args.apply:
        emit({"level": "error", "msg": "refusing_prod_apply_without_ack", "run_id": args.run_id}, log_json=args.log_json)
        return 2

    emit({"level": "info", "msg": "start", "run_id": args.run_id, "env": args.env, "dry_run": args.dry_run}, log_json=args.log_json)

    # ✅ Put orchestration here (call into src/ modules; write receipts; emit STAC/DCAT/PROV when relevant)
    if args.dry_run:
        emit({"level": "info", "msg": "dry_run_no_changes", "run_id": args.run_id}, log_json=args.log_json)
    else:
        if not args.yes and sys.stdin.isatty():
            confirm = input("This will modify state. Type 'apply' to continue: ").strip()
            if confirm != "apply":
                emit({"level": "info", "msg": "aborted", "run_id": args.run_id}, log_json=args.log_json)
                return 1
        elif not args.yes:
            emit({"level": "error", "msg": "no_tty_and_no_yes", "run_id": args.run_id}, log_json=args.log_json)
            return 2

        emit({"level": "info", "msg": "apply_doing_work", "run_id": args.run_id}, log_json=args.log_json)

    emit({"level": "info", "msg": "done", "run_id": args.run_id}, log_json=args.log_json)
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
```

</details>

---

<a id="gis-postgis"></a>

## 🗺️ GIS + PostGIS scripting tips

### ✅ Make CRS and units explicit
- refuse “unknown SRID” geometries by default
- log CRS for inputs/outputs
- document any axis-order or unit conversion

### ✅ Prefer database-side spatial operations when appropriate
- buffers, intersects, within, distance joins: PostGIS is usually safer and faster than “loop in Python”
- use staging tables and transactional swaps:
  1) load → 2) validate counts/geometry → 3) swap/rename in a transaction

### ✅ Web-serving friendliness
When scripts generate assets meant for the UI:
- vectors: simplify or tile (avoid megabyte GeoJSON blobs)
- rasters: prefer COG (with overviews)
- tiles: verify CRS (EPSG:3857 for web tiles) and metadata

### 🔐 Privacy reminder
GeoJSON is easy to copy. Treat “committed vectors” as a disclosure boundary:
- don’t export restricted geometries without explicit governance approval
- prefer catalog pointers to governed stores for sensitive layers

---

<a id="remote-sensing"></a>

## 🛰️ Remote sensing scripting tips

Remote sensing scripts are usually *orchestrators* for:
- exporting derived indices (NDVI, moisture proxies, composites)
- producing COGs and thumbnails
- emitting STAC Items and linking distributions via DCAT
- capturing PROV runs (inputs, AOI, time window, method, parameters)

### ✅ Prefer “derived products + provenance” over raw archives
- avoid committing raw satellite archives into the repo
- store raw externally when needed; keep catalog pointers in-repo
- ensure every derived product is traceable (PROV) and discoverable (STAC/DCAT)

### ✅ Record “how it was made”
For any export, record:
- AOI (bbox/geometry), time window
- dataset/source IDs
- compositing method (median/mean/mosaic, cloud mask logic)
- resolution/CRS
- model/algorithm version if AI-assisted

---

<a id="qa-scripts"></a>

## 🧪 QA scripts (contracts & acceptance gates)

`scripts/qa/` is for “trust checks” — scripts that keep the system honest:
- ✅ schema validation for metadata records (STAC/DCAT/PROV)
- ✅ catalog link checks (assets exist; hrefs resolve)
- ✅ definition-of-done checks (data present, metadata present, provenance present)
- ✅ contract checks (OpenAPI snapshots, schema diffs)
- ✅ security scans (secrets + sensitive patterns)
- ✅ governance checks (classification propagation; “no downgrade” rules)

**Starter examples (conceptual)**
```bash
# JSON sanity (fast fail)
find data/stac data/catalog/dcat data/prov -name "*.json*" -print0 | xargs -0 -n 1 jq empty

# Catalog asset/link integrity
python scripts/qa/validate_stac_links.py data/stac/items

# Provenance completeness
python scripts/qa/validate_prov_bundle.py data/prov

# OpenAPI/contract checks (if applicable)
python scripts/qa/validate_openapi.py src/server/contracts/openapi.yaml

# Secrets scan (repo-wide)
python scripts/security/scan_secrets.py .
```

> [!TIP]
> Keep PR checks fast. Put heavy raster QA into nightly jobs unless it blocks correctness. ⚡

---

<a id="adding-a-script"></a>

## 🧩 Adding a new script (checklist)

1) 📁 Put it in the right subfolder (`db/ gis/ remote_sensing/ qa/ …`)
2) 🏷️ Name it as a **verb**: `import_*`, `export_*`, `generate_*`, `validate_*`, `backup_*`
3) 🧪 Add `--help` + **2 examples**
4) 🛡️ Add `--dry-run` default and explicit confirmations for writes
5) 🧾 Write outputs to the correct `data/` stage + generate provenance/metadata when relevant
6) 🪵 Log clearly (what, where, record counts, elapsed time)
7) ♻️ Make it idempotent (re-runs should not duplicate or corrupt)
8) 🧪 Make it CI-friendly (non-interactive; stable exit codes)
9) 📝 Update this README **and** the script registry below

---

<a id="script-registry"></a>

## 📋 Script registry

> ✍️ Add rows as scripts are introduced. Keep this current.

| Category | Script pattern | Purpose | Safety posture |
|---|---|---|---|
| 🧰 dev | `dev/up.*` | Start local stack (compose) | read-only-ish |
| 🧰 dev | `dev/smoke.*` | Quick sanity checks | read-only |
| 🗄️ db | `db/migrate.*` | Apply DB migrations | `--apply` gated |
| 🗄️ db | `db/backup_*` | Create encrypted DB backups | `--dry-run` default |
| 🗄️ db | `db/restore_*` | Restore backups | multi-confirm required |
| 🗺️ gis | `gis/import_*` | Load vectors/rasters into staging | `--dry-run` + `--apply` |
| 🗺️ gis | `gis/export_*` | Export layers to GeoJSON/tiles/COGs | safe defaults |
| 🏷️ catalogs | `catalogs/build_*` | Build STAC/DCAT/PROV artifacts | read-only → writes artifacts |
| 🏷️ catalogs | `catalogs/validate_*` | Validate schemas + links | read-only |
| 🕸️ graph | `graph/sync_*` | Sync catalog references into graph | `--apply` gated |
| 🛰️ remote_sensing | `remote_sensing/export_*` | Trigger/track exports of derived EO products | record provenance always |
| 🧮 simulation | `simulation/run_*` | Run scenarios/jobs | seed + provenance required |
| 🤖 ml | `ml/train_*` / `ml/eval_*` | Train/evaluate models | dataset IDs + metrics required |
| 🧪 qa | `qa/validate_*` | Acceptance gates | read-only |
| 🔐 security | `security/scan_*` | Secrets/sensitive patterns | read-only |
| 🧹 housekeeping | `housekeeping/purge_*` | Cleanup caches/logs | confirmations required |
| 🧪 ci | `ci/check.*` | CI entrypoint | deterministic + non-interactive |

---

<a id="troubleshooting"></a>

## 🧯 Troubleshooting (CLI “kung fu”)

Useful patterns:
- log triage: `tail -f`, `less`, `grep`, `rg` (ripgrep)
- JSON sanity: `jq`
- YAML sanity: `yq` *(if used)*
- quick DB truth checks: `psql "$DATABASE_URL" -c "<query>"`

GIS sanity helpers:
- `gdalinfo <file.tif>`
- `ogrinfo <file.geojson> -so`
- `ogr2ogr -f GeoJSON /tmp/out.json in.shp -t_srs EPSG:4326` *(example transform)*

> [!CAUTION]
> Avoid “creative one-liners” on production data.  
> If it matters, turn it into a script with dry-run + logs + provenance. ✅

---

<a id="related-docs"></a>

## 🤝 Related docs (inside this repo)

- 📦 Data staging & dataset conventions → `data/README.md`
- 🧪 Canonical executable boundary → `src/README.md`
- 🛰️ API boundary scripts (service-local) → `api/scripts/README.md` *(if present)*
- 🧪 API tests (boundary test suite) → `api/tests/README.md` *(if present)*
- 📓 MCP runs, receipts, and research workflow → `mcp/MCP-README.md`
- 📓 Notebooks (explore → graduate to src) → `notebooks/README.md` *(if present)*
- 🌐 Web app conventions → `web/README.md` *(if present)*

---

<a id="reference-library-influence-map"></a>

## 📚 Project reference library influence map

> This is an explicit map from the project’s included reference files to the conventions enforced (or expected) in `scripts/`.

<details>
<summary><b>📦 Expand: project files → how they shape scripts</b></summary>

| Project file | What it contributes to `scripts/` conventions |
|---|---|
| `Kansas Frontier Matrix (KFM) – Comprehensive Engineering Design.docx` | Pipeline ordering, governance boundary posture, “no mystery artifacts,” and why scripts must be orchestration (not business logic). |
| `Latest Ideas.docx` | A place for experimental automation ideas that should graduate into canonical modules + contracts before becoming “prod scripts.” |
| `Kansas Frontier Matrix (KFM) – Master Technical Specification.pdf` | System invariants, API boundary rule, provenance-first publishing, performance constraints, and “deny-by-default” thinking. |
| `clean-architectures-in-python.pdf` | Thin-wrapper pattern: scripts call canonical services/modules; keep logic importable and testable. |
| `implementing-programming-languages-an-introduction-to-compilers-and-interpreters.pdf` | Interface/contract mindset: validate inputs early; fail fast; standardize exit codes and parsing. |
| `Node.js Notes for Professionals - NodeJSNotesForProfessionals.pdf` | Practical CLI/tooling patterns in JS ecosystems (useful for build glue, web tooling, generators). |
| `Introduction-to-Docker.pdf` | Container parity for scripts; reproducible environments; safe handling of secrets via env. |
| `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf` | DB scripting discipline: migrations, backups/restores, roles, transactional safety, repeatable ops. |
| `MySQL Notes for Professionals - MySQLNotesForProfessionals.pdf` | General relational ops patterns; import/export caution; consistent admin workflows. |
| `python-geospatial-analysis-cookbook.pdf` | CRS hygiene; geospatial IO; PostGIS integration; “fix data at boundaries, not ad-hoc.” |
| `geoprocessing-with-python.pdf` | Pipeline-style geoprocessing orchestration patterns and repeatable spatial processing workflows. |
| `Geographic Information System Basics - geographic-information-system-basics.pdf` | Map “truth” discipline: symbology implications; disclosure boundaries; QA checks for geometry and CRS. |
| `making-maps-a-visual-guide-to-map-design-for-gis.pdf` | Why “export defaults” matter; avoid misleading ramps; ensure legends/outputs are honest. |
| `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf` | Offline/mobile constraints that scripts should respect when generating tiles/derivatives (size budgets, caching). |
| `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf` | Remote sensing export orchestration patterns; how to record AOI/time/method for provenance. |
| `Google Earth Engine Applications.pdf` | Real-world GEE workflow variety; reinforces that scripts should track parameters and outputs systematically. |
| `responsive-web-design-with-html5-and-css3.pdf` | “Web reality” constraints: payload size budgets, responsive asset generation, and why scripts should optimize outputs. |
| `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf` | 3D/GL tooling awareness; coordinate conventions; caution with parsing complex model formats. |
| `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf` | Practical compression guidance for screenshots, thumbnails, QA artifacts, and web-facing outputs. |
| `Scalable Data Management for Future Hardware.pdf` | Performance thinking: partitions, locality, concurrency safety, and metadata-driven access patterns. |
| `Data Spaces.pdf` | Federation mindset: scripts should prefer dataset IDs + catalogs over local-only file assumptions. |
| `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf` | Simulation hygiene: verification/validation posture, parameter recording, seeds, and run receipts. |
| `Understanding Statistics & Experimental Design.pdf` | QA scripts should include sanity checks; avoid false confidence; validate assumptions. |
| `regression-analysis-with-python.pdf` | Baseline modeling scripts: reproducible training/eval; diagnostics and stability checks. |
| `slides-linear-regression.pdf` | Quick reminders for evaluation conventions and assumptions; supports “minimum viable eval” scripts. |
| `graphical-data-analysis-with-r.pdf` | EDA sanity outputs; encourages “plot and verify” acceptance gates for derived products. |
| `think-bayes-bayesian-statistics-in-python.pdf` | Uncertainty reporting expectations; scripts should record priors/assumptions when Bayesian workflows are used. |
| `Spectral Geometry of Graphs.pdf` | Graph-related QA scripts: be explicit about what metrics mean and validate graph integrity. |
| `Generalized Topology Optimization for Structural Design.pdf` | Optimization workflows: record constraints/objectives; deterministic run IDs; repeatable results packaging. |
| `Principles of Biological Autonomy - book_9780262381833.pdf` | Systems thinking: feedback loops, stability, and why automation must be observable and safe. |
| `Introduction to Digital Humanism.pdf` | Human-centered governance: transparency, accountability, ethical defaults, and “don’t automate harm.” |
| `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf` | AI governance: label AI-assisted outputs; record model/version/config where permissible; treat derived outputs carefully. |
| `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf` | Hostile-input mindset: treat parsers as attack surfaces; sandbox and validate. |
| `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf` | Threat modeling posture for scripts touching networks and privileged infra. |
| `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf` | Concurrency warnings: avoid races; lock/serialize destructive ops; design for determinism. |
| `Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf` | Practical ML automation: prioritize baselines, data-centric iteration, and clear evaluation artifacts. |
| `applied-data-science-with-python-and-jupyter.pdf` | Reproducible research habits: record environment, parameters, outputs; avoid “mystery notebooks” powering prod. |
| `MATLAB Programming for Engineers Stephen J. Chapman.pdf` | Engineering workflow discipline: repeatable scripts, explicit parameters, careful I/O handling. |
| `A programming Books.pdf` | General CLI/automation craftsmanship across languages; reinforces “boring, reliable scripts.” |
| `B-C programming Books.pdf` | Same: foundational engineering patterns and interoperability basics. |
| `D-E programming Books.pdf` | Same: tooling, interfaces, and maintainability patterns. |
| `F-H programming Books.pdf` | Same: pragmatic engineering discipline and robust automation culture. |
| `I-L programming Books.pdf` | Same: standardization and long-term maintainability. |
| `M-N programming Books.pdf` | Same: systems/network awareness relevant to ops scripts. |
| `O-R programming Books.pdf` | Same: reliability patterns and practical automation approaches. |
| `S-T programming Books.pdf` | Same: testing/tooling patterns that should influence script QA. |
| `U-X programming Books.pdf` | Same: breadth reference that supports consistent automation practices. |

</details>

---

<a id="definition-of-done"></a>

## ✅ Definition of “done” for a script

A script is considered complete when:
- ✅ Safe by default (`--dry-run` default or clearly supported)
- ✅ Repeatable/idempotent (re-run doesn’t duplicate or corrupt)
- ✅ Documented (`--help` + 2 examples)
- ✅ Logs what it did (counts, paths, elapsed time)
- ✅ Outputs land in the correct stage (`raw/ → work/ → processed/`)
- ✅ (When applicable) emits/updates metadata + provenance artifacts (STAC/DCAT/PROV)
- ✅ Registered in the script registry (table above)
- ⭐ (Recommended) passes basic linters (`shellcheck` / `ruff`) and is CI-friendly (non-interactive prompts require `--yes`)