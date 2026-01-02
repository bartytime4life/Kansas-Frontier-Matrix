# 🧰 `scripts/` — KFM Automation Toolkit

> Repeatable commands for dev, data ops, GIS/remote-sensing workflows, and deployment “glue”.
>
> **Safe-by-default** ✅ • **Idempotent** ♻️ • **Provenance-first** 🧾 • **Documented** 📓

---

## 🎯 What belongs here (and what doesn’t)

### ✅ Good fits for `scripts/`
- 🧱 **Environment bootstrap**: install deps, initialize DB schema, load seed/reference data
- 🗺️ **GIS tooling wrappers**: convert shapefiles/GeoJSON, generate tiles, reproject rasters, etc.
- 🧪 **Data import/export**: one-off admin imports (e.g., boundaries) and exports (snapshots, extracts)
- 🕒 **Scheduled jobs**: backups, cache cleanup, log rotation (cron / Kubernetes CronJob)
- 🧰 **Dev helpers**: run local stack, health checks, smoke tests, “make my laptop match CI”

### ❌ Not a good fit for `scripts/`
- 🚫 **Core ETL logic** (belongs in `src/pipelines/` / the canonical pipeline subsystem)
- 🚫 **Domain/business rules** (belongs in the core `src/` modules)
- 🚫 **Duplicate implementations** of pipeline steps (scripts should *call into* canonical modules)

---

## 🏁 Quickstart

### 1) Discover available scripts
- Look for subfolders (e.g., `scripts/db/`, `scripts/gis/`, `scripts/data/`)
- Run help first:
  - `./scripts/<path>/my_script.sh --help`
  - `python scripts/<path>/my_script.py --help`

> 💡 Tip: Every script should support `--help` and print clear examples.

### 2) Set environment (no secrets in git)
- Copy env template:
  - `cp .env.example .env`
- Load env (shell-specific), then run scripts.

> 🔐 Scripts must read configuration from environment variables (or a config file referenced by env),
> and **never** hardcode credentials.

---

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

---

## 🧭 Data lifecycle rules scripts must respect

KFM’s data work is **staged** and **traceable**. Scripts that ingest or transform data must:

1) 📥 **Write raw inputs** to `data/raw/<domain>/`
2) 🧱 **Write intermediates** to `data/work/<domain>/`
3) ✅ **Write publishable outputs** to `data/processed/<domain>/`
4) 🗃️ **Emit metadata + lineage artifacts** (STAC/DCAT/PROV) *before* anything is used downstream

> 🧾 If a script produces “evidence artifacts” (derived analyses, model outputs, generated map layers),
> treat them like first-class datasets: store them properly, catalog them, and capture provenance.

---

## 🧨 Safety guardrails (non‑negotiable)

### ✅ Safe-by-default behavior
- 🛑 **No destructive actions by default**
- 🧪 Default mode should be `--dry-run` (or at minimum support it)
- 🧯 Destructive actions require explicit confirmation flags (example patterns below)

**Recommended confirmation pattern**
- `--dry-run` prints what would happen
- `--apply` performs changes
- `--yes` skips interactive prompts
- `--env {dev|staging|prod}` and **refuse** dangerous combos without extra confirmation

### 🏭 Production protection
- Scripts that can write to prod must:
  - require explicit `--env prod`
  - require an additional “I really mean it” confirmation flag (e.g., `--i-acknowledge-production`)
  - log who/what/when (user, git SHA if available, host, timestamp)

---

## 🧾 Observability & provenance

Every script should:
- 🪵 Use structured logging (timestamp, level, component, run_id)
- 🧷 Print where outputs were written (paths) and what changed
- 🧾 Capture provenance inputs/outputs:
  - input file list + checksums (when feasible)
  - key parameters (bounding box, time window, model version, CRS, etc.)
  - links/IDs to produced metadata artifacts (STAC/DCAT/PROV)

> 🎛️ If it’s not reproducible, it’s not done.

---

## 🧱 Script templates

### 🐚 Bash template (portable + strict)
```bash
#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  ./scripts/example.sh [--dry-run] [--apply] [--yes]

Examples:
  ./scripts/example.sh --dry-run
  ./scripts/example.sh --apply --yes
EOF
}

DRY_RUN=1
APPLY=0
YES=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run) DRY_RUN=1; APPLY=0; shift ;;
    --apply)   APPLY=1; DRY_RUN=0; shift ;;
    --yes)     YES=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown arg: $1" >&2; usage; exit 2 ;;
  esac
done

echo "[INFO] dry_run=$DRY_RUN apply=$APPLY yes=$YES"

if [[ "$APPLY" -eq 1 && "$YES" -ne 1 ]]; then
  read -r -p "This will modify state. Type 'apply' to continue: " confirm
  [[ "$confirm" == "apply" ]] || { echo "Aborted."; exit 1; }
fi

# ✅ Put your logic here
echo "[OK] Done."
```

### 🐍 Python template (CLI + logging + exit codes)
```python
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import logging
import sys
from dataclasses import dataclass

log = logging.getLogger("kfm.scripts")

@dataclass(frozen=True)
class Args:
    dry_run: bool
    apply: bool
    verbose: bool

def parse_args(argv: list[str]) -> Args:
    p = argparse.ArgumentParser(
        prog="python scripts/example.py",
        description="Example KFM script (safe-by-default, idempotent).",
    )
    mode = p.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="Print actions without changing state.")
    mode.add_argument("--apply", action="store_true", help="Perform actions (writes/changes).")
    p.add_argument("-v", "--verbose", action="store_true", help="Verbose logs.")
    ns = p.parse_args(argv)

    dry_run = ns.dry_run or not ns.apply  # default safe
    apply = ns.apply
    return Args(dry_run=dry_run, apply=apply, verbose=ns.verbose)

def main(argv: list[str]) -> int:
    args = parse_args(argv)
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s - %(message)s",
    )

    log.info("start dry_run=%s apply=%s", args.dry_run, args.apply)

    # ✅ Put your logic here
    if args.dry_run:
        log.info("DRY RUN: would do work here…")
    else:
        log.info("APPLY: doing work…")

    log.info("done")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
```

---

## 🗺️ GIS + PostGIS scripting tips

- Prefer **PostGIS for heavy lifting** when appropriate (buffers, intersections, within queries)
- Use scripts to:
  - validate CRS
  - load data into PostGIS safely (staging tables, transactions)
  - export to GeoJSON for UI consumption
  - generate derived layers that can be tiled

> 🧠 Rule of thumb: big spatial ops belong close to the data; scripts orchestrate and validate.

---

## 🧪 QA scripts (contracts & acceptance gates)

`scripts/qa/` is for “trust checks” — scripts that keep the system honest:
- ✅ schema validation for metadata records
- ✅ linting / formatting
- ✅ “definition of done” checks (data present, metadata present, provenance present)

> 📦 Any dataset/evidence artifact should be verifiable via a repeatable command.

---

## 🧩 Adding a new script (checklist)

1) 📁 Put it in the right subfolder (bootstrap/db/gis/remote_sensing/ml/qa/…)
2) 🏷️ Name it as a verb: `import_*`, `export_*`, `generate_*`, `validate_*`, `backup_*`
3) 🧪 Add `--help` + examples
4) 🛡️ Add `--dry-run` (or safe default) and explicit confirmations for writes
5) 🧾 Write outputs to the correct `data/` stage + generate provenance/metadata when relevant
6) 🪵 Log clearly (what, where, how many records, elapsed time)
7) 🧼 Make it idempotent (re-runs should not duplicate)
8) 📝 Update this README (and any script registry table below)

---

## 📋 Script registry (keep this current)

| Category | Script | Purpose | Safe mode |
|---|---|---|---|
| 🗄️ db | `backup_*` | Create encrypted DB backups | `--dry-run` default |
| 🗺️ gis | `import_*` | Load boundaries/shape data into PostGIS | `--dry-run` + `--apply` |
| 🧪 qa | `validate_*` | Validate schemas/contracts/metadata | read-only |
| 🧹 housekeeping | `purge_*` | Cleanup caches/logs | confirm required |

> ✍️ Add rows as scripts are introduced.

---

## 🧯 Troubleshooting (CLI “kung fu”)

A few battle-tested patterns:
- 🔎 Inspect logs quickly: `grep`, `tail -f`, `less`
- 🧮 Quick stats: `cut`, `awk`, `sort | uniq -c`
- 🧹 Cleanup old logs: `find … -mtime +N -delete` *(be careful — pair with `--dry-run` style previews)*

---

## 🤝 Related docs (inside this repo)

- 📦 Data staging & dataset conventions → `data/README.md`
- 🌐 Web app tooling & layer registry → `web/README.md`
- 🧩 MCP services & tool interfaces → `mcp/README.md`
- 🏛️ Governance, contracts, and standards → `.github/*` and `docs/*`

---

## ✅ Definition of “done” for a script

A script is considered complete when:
- ✅ It’s safe by default
- ✅ It’s repeatable/idempotent
- ✅ It logs what it did
- ✅ Outputs land in the correct stage
- ✅ (When applicable) it emits/updates metadata + provenance artifacts
- ✅ It has a minimal usage example and is referenced in this README