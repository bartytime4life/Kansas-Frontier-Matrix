# 🧰 `scripts/` — KFM Automation Toolkit

![Safe by default](https://img.shields.io/badge/safe--by--default-yes-success)
![Idempotent](https://img.shields.io/badge/idempotent-expected-blue)
![Provenance first](https://img.shields.io/badge/provenance--first-required-informational)
![Documented](https://img.shields.io/badge/--help-required-brightgreen)
![Shell](https://img.shields.io/badge/shell-bash%20%7C%20pwsh-lightgrey)
![Python](https://img.shields.io/badge/python-cli%20scripts-3776AB)
![QA](https://img.shields.io/badge/qa-contract%20gates-purple)

> Repeatable commands for dev, data ops, GIS/remote-sensing workflows, and deployment “glue”.  
> **Safe-by-default** ✅ • **Idempotent** ♻️ • **Provenance-first** 🧾 • **Documented** 📓

> [!IMPORTANT]
> `scripts/` is **orchestration**, not “the truth.”  
> If a script becomes **core behavior**, move the implementation into `src/` and let scripts call it.

---

<details>
<summary><b>🧭 Table of Contents</b></summary>

- [🎯 What belongs here (and what doesn’t)](#what-belongs-here)
- [🏁 Quickstart](#quickstart)
- [🗂️ Recommended folder map](#folder-map)
- [🧱 Standard script contract](#script-contract)
- [🧭 Data lifecycle rules scripts must respect](#data-lifecycle)
- [🧨 Safety guardrails (non-negotiable)](#safety-guardrails)
- [🧾 Observability & provenance](#observability)
- [🧱 Script templates](#script-templates)
- [🗺️ GIS + PostGIS scripting tips](#gis-postgis)
- [🧪 QA scripts (contracts & acceptance gates)](#qa-scripts)
- [🧩 Adding a new script (checklist)](#adding-a-script)
- [📋 Script registry](#script-registry)
- [🧯 Troubleshooting (CLI “kung fu”)](#troubleshooting)
- [🤝 Related docs (inside this repo)](#related-docs)
- [✅ Definition of “done” for a script](#definition-of-done)

</details>

---

<a id="what-belongs-here"></a>

## 🎯 What belongs here (and what doesn’t)

### ✅ Good fits for `scripts/`
- 🧱 **Environment bootstrap**: install deps, initialize DB schema, load seed/reference data  
- 🗺️ **GIS tooling wrappers**: convert shapefiles/GeoJSON, generate tiles, reproject rasters, etc.  
- 🧪 **Data import/export helpers**: admin imports (e.g., boundaries) and exports (snapshots, extracts)  
- 🕒 **Scheduled jobs**: backups, cache cleanup, log rotation (cron / Kubernetes CronJob)  
- 🧰 **Dev helpers**: run local stack, health checks, smoke tests, “make my laptop match CI”  
- 🧾 **Acceptance gates**: dataset/catalog validation, link checks, provenance completeness

### ❌ Not a good fit for `scripts/`
- 🚫 **Core ETL logic** (belongs in `src/pipelines/`)  
- 🚫 **Domain/business rules** (belongs in `src/` domain/application layers)  
- 🚫 **Duplicate implementations** of pipeline steps (scripts should *call into* canonical modules)  
- 🚫 **One-off “forever scripts”** that bypass provenance and approvals

> [!TIP]
> Scripts are the “buttons and levers.” If it’s “the engine,” it belongs in `src/`. 🔧➡️🏗️

---

<a id="quickstart"></a>

## 🏁 Quickstart

### 1) Discover available scripts
- Browse by category (e.g., `scripts/db/`, `scripts/gis/`, `scripts/data/`, `scripts/qa/`)
- Run help first:
  - `./scripts/<path>/my_script.sh --help`
  - `python scripts/<path>/my_script.py --help`

> [!IMPORTANT]
> Every script **must** support `--help` and include **at least 2 runnable examples**.

### 2) Set environment (no secrets in git) 🔐
- Copy env template:
  - `cp .env.example .env`
- Export/load env (shell-specific), then run scripts.

**Never hardcode credentials.** Scripts read config from:
- environment variables ✅
- or a config file *path* provided via env ✅

### 3) Default to safety ✅
Prefer the contract:
- `--dry-run` (default) → prints actions
- `--apply` → performs changes
- `--yes` → skips prompts (still should refuse dangerous prod combos without extra acknowledgement)

---

<a id="folder-map"></a>

## 🗂️ Recommended folder map

> This repo may evolve — keep this README updated when adding new categories.

```text
📁 scripts/
├─ 🧱 bootstrap/        # first-run setup (DB init, seed/reference loads)
├─ 🗄️ db/               # migrations, backups, restores, snapshots, sanity checks
├─ 🗺️ gis/              # geoprocessing helpers (vector/raster, PostGIS utilities)
├─ 🛰️ remote_sensing/   # imagery ingest helpers / GEE wrappers / indexing
├─ 🤖 ml/               # training/eval runners (should call src/ modules)
├─ 🧪 qa/               # validators, contract checks, dataset acceptance gates
├─ 🧹 housekeeping/     # rotate logs, purge caches, cleanup artifacts
└─ 🧰 dev/              # local stack helpers, smoke tests, DX scripts
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
- Output hygiene (recommended):
  - `--run-id <id>` (or env `KFM_RUN_ID`) to correlate logs + provenance
  - `--log-json` for machine-readable logs (JSONL)
  - `--output <path>` or `--outdir <path>` for artifact destinations

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

### ✅ “Thin wrapper” pattern (recommended)
If you’re tempted to put real transformation logic in a script, do this instead:
- implement the core logic in `src/…` (pipelines/domain/services)
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
- 🧪 Default mode should be `--dry-run` (or at minimum support it)
- 🧯 Destructive actions require explicit confirmation flags

**Recommended confirmation pattern**
- `--dry-run` prints what would happen  
- `--apply` performs changes  
- `--yes` skips interactive prompts  
- `--env {dev|staging|prod}` and **refuse** dangerous combos without extra confirmation  

### 🏭 Production protection
Scripts that can write to prod must:
- require explicit `--env prod`
- require an additional “I really mean it” flag  
  - e.g., `--i-acknowledge-production`
- log who/what/when:
  - user (if detectable), host, timestamp, run_id
  - git SHA (if available)
  - container digest (if available)

> [!CAUTION]
> If a script can delete, drop, truncate, overwrite, revoke, or publish:  
> **dry-run default + explicit apply + explicit confirmation** is mandatory. 🚫🧨✅

### 🧊 Atomic writes (strongly recommended)
For file outputs:
- write to `*.tmp` then rename to final output (atomic on most OS/filesystems)
- never leave half-written “published” outputs behind

---

<a id="observability"></a>

## 🧾 Observability & provenance

Every script should:
- 🪵 Use structured logging (`timestamp`, `level`, `component`, `run_id`)
- 🧷 Print where outputs were written (paths) + what changed (counts, bytes, features)
- 🧾 Capture provenance inputs/outputs:
  - input file list + checksums (when feasible)
  - key parameters (bbox, time window, model version, CRS, resolution)
  - links/IDs to produced metadata artifacts (STAC/DCAT/PROV)

**Recommended “run receipt” (optional but 🔥):**
- If `--apply` is used, write a small receipt file:
  - `mcp/runs/<RUN-ID>/MANIFEST.md` (human-readable)
  - or `data/prov/<RUN-ID>.jsonld` (machine lineage)

> 🎛️ If it’s not reproducible, it’s not done.

---

<a id="script-templates"></a>

## 🧱 Script templates

<details>
<summary><b>🐚 Bash template (portable + strict)</b></summary>

```bash
#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  ./scripts/example.sh [--dry-run] [--apply] [--yes] [--env dev|staging|prod]

Purpose:
  Example KFM script (safe-by-default, idempotent).

Examples:
  ./scripts/example.sh --dry-run
  ./scripts/example.sh --apply --yes --env dev
EOF
}

DRY_RUN=1
APPLY=0
YES=0
ENVIRONMENT="${KFM_ENV:-dev}"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run) DRY_RUN=1; APPLY=0; shift ;;
    --apply)   APPLY=1; DRY_RUN=0; shift ;;
    --yes)     YES=1; shift ;;
    --env)     ENVIRONMENT="${2:-}"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown arg: $1" >&2; usage; exit 2 ;;
  esac
done

echo "[INFO] env=$ENVIRONMENT dry_run=$DRY_RUN apply=$APPLY yes=$YES"

if [[ "$ENVIRONMENT" == "prod" && "$APPLY" -eq 1 ]]; then
  echo "[ERROR] Refusing to apply to prod without an explicit prod-ack flag." >&2
  echo "        Add a flag like: --i-acknowledge-production" >&2
  exit 2
fi

if [[ "$APPLY" -eq 1 && "$YES" -ne 1 ]]; then
  read -r -p "This will modify state. Type 'apply' to continue: " confirm
  [[ "$confirm" == "apply" ]] || { echo "Aborted."; exit 1; }
fi

# ✅ Put your logic here
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
    verbose: bool

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
    p.add_argument("--run-id", default=os.getenv("KFM_RUN_ID", ""), help="Optional run identifier.")
    p.add_argument("--log-json", action="store_true", help="Emit JSON logs (JSONL friendly).")
    p.add_argument("-v", "--verbose", action="store_true", help="Verbose logs.")
    ns = p.parse_args(argv)

    dry_run = ns.dry_run or not ns.apply  # default safe
    apply = ns.apply
    run_id = ns.run_id or "run-unknown"
    return Args(
        dry_run=dry_run,
        apply=apply,
        yes=ns.yes,
        env=ns.env,
        run_id=run_id,
        log_json=ns.log_json,
        verbose=ns.verbose,
    )

def _log_event(event: dict, *, log_json: bool) -> None:
    if log_json:
        print(json.dumps(event, ensure_ascii=False))
    else:
        log.info("%s", event)

def main(argv: list[str]) -> int:
    args = parse_args(argv)
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s [%(message)s]",
    )

    if args.env == "prod" and args.apply:
        _log_event(
            {"level": "error", "msg": "refusing_prod_apply_without_ack", "run_id": args.run_id},
            log_json=args.log_json,
        )
        return 2

    _log_event(
        {"level": "info", "msg": "start", "run_id": args.run_id, "env": args.env, "dry_run": args.dry_run},
        log_json=args.log_json,
    )

    # ✅ Put your logic here
    if args.dry_run:
        _log_event({"level": "info", "msg": "dry_run_no_changes", "run_id": args.run_id}, log_json=args.log_json)
    else:
        if not args.yes:
            # Keep prompts out of non-interactive environments (CI)
            if not sys.stdin.isatty():
                _log_event({"level": "error", "msg": "no_tty_and_no_yes", "run_id": args.run_id}, log_json=args.log_json)
                return 2
            confirm = input("This will modify state. Type 'apply' to continue: ").strip()
            if confirm != "apply":
                _log_event({"level": "info", "msg": "aborted", "run_id": args.run_id}, log_json=args.log_json)
                return 1

        _log_event({"level": "info", "msg": "apply_doing_work", "run_id": args.run_id}, log_json=args.log_json)

    _log_event({"level": "info", "msg": "done", "run_id": args.run_id}, log_json=args.log_json)
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
```

</details>

---

<a id="gis-postgis"></a>

## 🗺️ GIS + PostGIS scripting tips

- Prefer **PostGIS for heavy lifting** when appropriate (buffers, intersections, within queries)
- Use scripts to:
  - validate CRS (and refuse unexpected CRS) 🧭
  - load data into PostGIS safely (staging tables, transactions) 🐘
  - export to GeoJSON/tiles for UI consumption 🗺️
  - generate derived layers that can be tiled (vector tiles, raster tiles) 🧊

**Practical safety patterns**
- Load into a staging table → validate counts/geometry → swap/rename in a transaction ✅
- Refuse “unknown SRID” geometries by default 🚫
- Log `feature_count_in`, `feature_count_out`, and any invalid geometries found 🪵

> 🧠 Rule of thumb: big spatial ops belong close to the data; scripts orchestrate + validate.

---

<a id="qa-scripts"></a>

## 🧪 QA scripts (contracts & acceptance gates)

`scripts/qa/` is for “trust checks” — scripts that keep the system honest:
- ✅ schema validation for metadata records (STAC/DCAT/PROV)  
- ✅ catalog link checks (assets exist; hrefs resolve)  
- ✅ “definition of done” checks (data present, metadata present, provenance present)  
- ✅ safety scans (secrets/PII patterns; classification consistency where applicable)

**Starter examples (conceptual)**
```bash
# JSON sanity (fast fail)
find data/stac data/catalog/dcat data/prov -name "*.json*" -print0 | xargs -0 -n 1 jq empty

# Catalog asset/link integrity
python scripts/qa/validate_stac_links.py data/stac/items

# Provenance completeness
python scripts/qa/validate_prov_bundle.py data/prov

# Fast secrets scan (repo-wide)
python scripts/qa/scan_secrets.py .
```

> [!TIP]
> Keep CI fast: run heavy GIS QA nightly; keep PR checks “tight and quick.” ⚡

---

<a id="adding-a-script"></a>

## 🧩 Adding a new script (checklist)

1) 📁 Put it in the right subfolder (`bootstrap/ db/ gis/ remote_sensing/ ml/ qa/ …`)  
2) 🏷️ Name it as a **verb**: `import_*`, `export_*`, `generate_*`, `validate_*`, `backup_*`  
3) 🧪 Add `--help` + **2 examples**  
4) 🛡️ Add `--dry-run` default and explicit confirmations for writes  
5) 🧾 Write outputs to the correct `data/` stage + generate provenance/metadata when relevant  
6) 🪵 Log clearly (what, where, how many records, elapsed time)  
7) ♻️ Make it idempotent (re-runs should not duplicate or corrupt)  
8) 📝 Update this README **and** the script registry below  

---

<a id="script-registry"></a>

## 📋 Script registry

> ✍️ Add rows as scripts are introduced. Keep this current.

| Category | Script | Purpose | Safe mode |
|---|---|---|---|
| 🗄️ db | `backup_*` | Create encrypted DB backups | `--dry-run` default |
| 🗄️ db | `restore_*` | Restore DB backup into a target env | `--dry-run` + confirmations |
| 🗺️ gis | `import_*` | Load boundaries/shape data into PostGIS | `--dry-run` + `--apply` |
| 🗺️ gis | `export_*` | Export PostGIS layers to GeoJSON/tiles | read-only / `--apply` for writes |
| 🛰️ remote_sensing | `fetch_*` | Pull imagery/metadata; stage inputs | `--dry-run` default |
| 🧪 qa | `validate_*` | Validate schemas/contracts/metadata | read-only |
| 🧹 housekeeping | `purge_*` | Cleanup caches/logs | confirmations required |
| 🧰 dev | `start_*` / `smoke_*` | Local stack helpers & smoke tests | read-only |

> [!NOTE]
> If the registry grows, consider splitting it into `scripts/REGISTRY.md` and linking here. 📌

---

<a id="troubleshooting"></a>

## 🧯 Troubleshooting (CLI “kung fu”)

A few battle-tested patterns:
- 🔎 Inspect logs quickly: `grep`, `tail -f`, `less`
- 🧮 Quick stats: `cut`, `awk`, `sort | uniq -c`
- 🧹 Preview destructive ops before running them:
  - `find … -mtime +N -print` *(preview)*
  - then `find … -mtime +N -delete` *(apply)*

**GIS sanity helpers**
- `gdalinfo <file.tif>` (raster metadata)
- `ogrinfo <file.geojson> -so` (vector summary)
- `psql "$DATABASE_URL" -c "<query>"` (fast DB truth check)

> [!CAUTION]
> Avoid “creative one-liners” on production data.  
> If it matters, turn it into a script with dry-run + logs + provenance. ✅

---

<a id="related-docs"></a>

## 🤝 Related docs (inside this repo)

- 📦 Data staging & dataset conventions → `data/README.md`
- 🧪 Source-of-truth ETL + catalogs + API boundary → `src/README.md`
- 📓 MCP experiment reports + run receipts → `mcp/README.md`
- 🌐 Web app tooling & layer registry → `web/README.md`
- 🧭 Collaboration & automation → `.github/README.md`
- 🏛️ Governance, contracts, standards → `docs/` and `.github/`

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
- ⭐ (Recommended) passes basic linters (`shellcheck` / `ruff`) and is CI-friendly (no interactive prompts without `--yes`)
