# 🔬 MCP Experiment — TEMPLATE

> Copy this folder and rename to `mcp/experiments/EXP-YYYYMMDD-<slug>/`.

## 0) Metadata

- **Experiment ID:** `EXP-YYYYMMDD-<slug>`
- **Owner(s):** @you
- **Status:** ☐ Planned ☐ Running ☐ Completed ☐ Abandoned
- **Scope areas:** `data` | `stac` | `web` | `src` | `scripts` | `ci` | `docker`
- **Related issues/PRs:** Fixes #…, Relates #…
- **Milestone:** `m1-data` | `m2-analytics` | `m3-story` | `m4-tech` | `m5-mcp`

## 1) Objective / Hypothesis

- **Question:** …
- **Hypothesis:** …
- **Success criteria:** …

## 2) Inputs & Bounds

- **STAC inputs:** list item/collection IDs or paths
- **Source descriptors:** `data/sources/*.json`
- **AOI / timeframe:** bbox / dates
- **Licenses / provenance:** notes + citations

## 3) Method (SOP)

- Controls/treatments/params noted in `params.yaml`
- Deterministic commands live in `commands.sh`

## 4) Repro Commands

Run from repo root (or this dir) after activating your venv:

```bash
bash mcp/experiments/EXP-YYYYMMDD-<slug>/commands.sh
This script:

Validates STAC & configs

Builds derivatives if needed

Captures env + git SHA

Snapshots artifact hashes

Writes metrics & a STAC report to results/

5) Results
Metrics: results/metrics.json

STAC report: results/stac_report.json

Figures: figures/ (PNG/SVG)

6) Provenance
Git commit: provenance/git_sha.txt

Artifact hashes: provenance/artifact_hashes.txt (SHA-256)

7) Ethics / Legal
Sensitive locations handled?

Licenses verified?

Indigenous/community data reviewed where applicable?

8) Follow-ups
 …

 …

Validation & CI hooks
bash
Copy code
make stac-validate
make config-validate || true
mermaid
Copy code
flowchart TD
  A["Params & SOP"] --> B["Run commands.sh"]
  B --> C["Artifacts & Figures"]
  B --> D["Metrics & Reports"]
  B --> E["Provenance\n(git SHA + hashes)"]
  D --> F["Review vs. Success Criteria"]
<!-- END OF MERMAID -->
bash
Copy code

---

# `mcp/experiments/template/commands.sh`

```bash
#!/usr/bin/env bash
set -euo pipefail

# --- Config -------------------------------------------------------------------
EXP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo "$(pwd)")"
cd "$ROOT_DIR"

EXP_NAME="${EXP_DIR##*/}"   # e.g., EXP-20251001-kansas-hillshade
OUT_DIR="$EXP_DIR"
RESULTS_DIR="$OUT_DIR/results"
ENV_DIR="$OUT_DIR/env"
PROV_DIR="$OUT_DIR/provenance"
FIG_DIR="$OUT_DIR/figures"
PARAMS="$OUT_DIR/params.yaml"

mkdir -p "$RESULTS_DIR" "$ENV_DIR" "$PROV_DIR" "$FIG_DIR"

# --- Helpers ------------------------------------------------------------------
log() { printf "\n\033[1;34m[%s]\033[0m %s\n" "$(date +%H:%M:%S)" "$*"; }

# --- 0) Capture environment ---------------------------------------------------
log "Capturing environment"
python -V || true
{ python -V; echo; pip freeze || true; } > "$ENV_DIR/env.txt"
git rev-parse HEAD > "$PROV_DIR/git_sha.txt" 2>/dev/null || true

# --- 1) Optional: fetch / build inputs ---------------------------------------
# Customize these if your experiment needs new data.
if grep -q '^fetch:' "$PARAMS" 2>/dev/null; then
  log "Fetching sources (per params.yaml)"
  make fetch || true
fi

# --- 2) Build derivatives (if requested) -------------------------------------
if grep -q '^build_derivatives:' "$PARAMS" 2>/dev/null; then
  log "Building derivatives"
  make cogs || true
  make terrain || true
fi

# --- 3) STAC + config validation ---------------------------------------------
log "Validating STAC & viewer config"
make stac-validate || true
make config-validate || true

# --- 4) Render site config (if needed) ---------------------------------------
if grep -q '^render_site_config:' "$PARAMS" 2>/dev/null; then
  log "Rendering web/app.config.json"
  make site-config || true
fi

# --- 5) Compute metrics (placeholder) ----------------------------------------
# Implement your metrics below. Example leaves a stub JSON.
log "Computing metrics (placeholder)"
jq -n --arg exp "$EXP_NAME" \
  '{experiment:$exp, metrics:{example_metric:0}, timestamp:now}' \
  > "$RESULTS_DIR/metrics.json"

# --- 6) STAC report (placeholder) --------------------------------------------
log "Writing STAC report (placeholder)"
jq -n --arg exp "$EXP_NAME" \
  '{experiment:$exp, stac_validation:"see CI artifacts or local validator output"}' \
  > "$RESULTS_DIR/stac_report.json"

# --- 7) Snapshot artifact hashes ---------------------------------------------
log "Hashing artifacts (SHA-256)"
# You can scope this to relevant output dirs; the glob handles missing dirs.
( find data/cogs -type f -name '*.tif' 2>/dev/null
  find data/processed -type f 2>/dev/null
  find web -maxdepth 1 -type f -name '*.json' 2>/dev/null
) | LC_ALL=C sort | xargs -r sha256sum > "$PROV_DIR/artifact_hashes.txt" || true

log "Done. Results in: $OUT_DIR"
Make it executable:

bash
Copy code
chmod +x mcp/experiments/template/commands.sh
