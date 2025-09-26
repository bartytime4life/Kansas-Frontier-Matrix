#!/usr/bin/env bash
# scripts/collections/archaeology.sh
# -----------------------------------------------------------
# Kansas-Frontier-Matrix — Archaeology Collection Pipeline
#
# Purpose:
#   Automates ETL, validation, and STAC integration for
#   archaeology-related datasets (excavations, surveys,
#   stratigraphy, lab analyses).
#
# References:
#   - MCP Domain Module: Archaeology:contentReference[oaicite:3]{index=3}
#   - Cross-disciplinary integration templates (history,
#     cartography, geology):contentReference[oaicite:4]{index=4}
#   - Mapping Hub Design + Audit:contentReference[oaicite:5]{index=5}:contentReference[oaicite:6]{index=6}
#
# Usage:
#   ./scripts/collections/archaeology.sh <command> [options]
#
# Commands:
#   fetch        Download raw sources listed in data/sources/archaeology_*.json
#   process      Convert to GeoJSON/COG, normalize CRS, prep metadata
#   stac         Build STAC Items for archaeology datasets
#   validate     Run schema + checksum validation
#   clean        Remove temporary/intermediate artifacts
#   doctor       Debug info (paths, counts, STAC links)
#
# Notes:
#   - All outputs land in ./data/processed/archaeology/ and ./stac/items/archaeology/
#   - Uses GDAL/ogr2ogr for vector, rio-cogeo for rasters
#   - STAC compliance: v1.0.0, assets link to COG/GeoJSON:contentReference[oaicite:7]{index=7}
# -----------------------------------------------------------

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
DATA="$ROOT/data"
RAW="$DATA/raw/archaeology"
PROC="$DATA/processed/archaeology"
STAC="$ROOT/stac/items/archaeology"

mkdir -p "$RAW" "$PROC" "$STAC"

log() { echo "[archaeology] $*" >&2; }

cmd_fetch() {
  log "Fetching archaeology sources..."
  for src in "$DATA"/sources/archaeology_*.json; do
    [ -f "$src" ] || continue
    python "$ROOT/scripts/fetch.py" --source "$src" --out "$RAW"
  done
}

cmd_process() {
  log "Processing raw archaeology data..."
  for f in "$RAW"/*; do
    case "$f" in
      *.tif|*.tiff)
        out="$PROC/$(basename "$f" .tif).cog.tif"
        log "→ Converting raster → COG: $(basename "$f")"
        rio cogeo create "$f" "$out" --overview-level=5 --web-optimized
        ;;
      *.shp)
        out="$PROC/$(basename "$f" .shp).geojson"
        log "→ Converting vector → GeoJSON: $(basename "$f")"
        ogr2ogr -f GeoJSON -t_srs EPSG:4326 "$out" "$f"
        ;;
      *)
        log "Skipping unrecognized file: $f"
        ;;
    esac
  done
}

cmd_stac() {
  log "Generating STAC Items..."
  python "$ROOT/scripts/make_stac.py" \
    --input "$PROC" \
    --output "$STAC" \
    --collection archaeology \
    --id-prefix arch
}

cmd_validate() {
  log "Validating archaeology STAC + checksums..."
  kgt validate-stac --stac "$STAC"
  kgt validate-sources --schema "$ROOT/src/kansas_geo_timeline/schemas/source.schema.json" \
    "$DATA"/sources/archaeology_*.json
}

cmd_clean() {
  log "Cleaning processed/stac artifacts..."
  rm -rf "$PROC"/* "$STAC"/*
}

cmd_doctor() {
  log "Doctor report:"
  echo "RAW count:   $(ls "$RAW" | wc -l)"
  echo "PROC count:  $(ls "$PROC" | wc -l)"
  echo "STAC items:  $(ls "$STAC" | wc -l)"
}

case "${1:-}" in
  fetch)     shift; cmd_fetch "$@";;
  process)   shift; cmd_process "$@";;
  stac)      shift; cmd_stac "$@";;
  validate)  shift; cmd_validate "$@";;
  clean)     shift; cmd_clean "$@";;
  doctor)    shift; cmd_doctor "$@";;
  ""|help|--help|-h)
    grep '^# ' "$0" | sed 's/^# \{0,1\}//'
    ;;
  *)
    log "Unknown command: $1"; exit 1;;
esac

