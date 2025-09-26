#!/usr/bin/env bash
# scripts/collections/archaeology_sites.sh
# -------------------------------------------------------------------
# Kansas-Frontier-Matrix — Archaeology Sites Pipeline
#
# Purpose
#   ETL + STAC + validation for archaeology site layers
#   (e.g., site points/polygons, survey footprints, registers).
#
# Commands
#   init        Create a starter source descriptor + folders
#   fetch       Download raw sources listed in data/sources/arch_sites_*.json
#   unpack      Unzip/untar raw archives into data/raw/arch_sites/
#   process     Convert to GeoJSON (EPSG:4326), basic QA, per-item outputs
#   merge       Optional: merge site layers by year/id into rollups
#   stac        Generate STAC Items under stac/items/archaeology-sites/
#   validate    Validate STAC + source schemas + checksums
#   render      Regenerate web/app.config.json from STAC
#   clean       Remove processed + temp artifacts for this collection
#   doctor      Print quick diagnostics (counts/paths)
#
# Conventions
#   - Source descriptors: data/sources/arch_sites_*.json
#   - Raw input:        data/raw/arch_sites/
#   - Processed out:    data/processed/arch_sites/
#   - STAC items:       stac/items/archaeology-sites/
#
# Requirements
#   - GDAL/ogr2ogr, rio-cogeo (for any rasters that sneak in)
#   - Python scripts/fetch.py, scripts/make_stac.py, kgt CLI
#
# -------------------------------------------------------------------

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
DATA="$ROOT/data"
SRC_DIR="$DATA/sources"
RAW="$DATA/raw/arch_sites"
PROC="$DATA/processed/arch_sites"
TMP="$DATA/tmp/arch_sites"
STAC_DIR="$ROOT/stac/items/archaeology-sites"

mkdir -p "$RAW" "$PROC" "$TMP" "$STAC_DIR"

log() { echo "[archaeology-sites] $*" >&2; }
die() { log "ERROR: $*"; exit 1; }

# --- helpers ---------------------------------------------------------

_unzip_any() {
  local f="$1"
  case "$f" in
    *.zip) unzip -o -q "$f" -d "$RAW" ;;
    *.tar.gz|*.tgz) tar -xzf "$f" -C "$RAW" ;;
    *.tar.bz2|*.tbz2) tar -xjf "$f" -C "$RAW" ;;
    *) log "No unpack rule for: $(basename "$f") (skipping)";;
  esac
}

_to_geojson() {
  local in="$1"
  local base out
  base="$(basename "$in")"
  out="$PROC/${base%.*}.geojson"

  # Detect vector containers
  case "$in" in
    *.shp)
      ogr2ogr -f GeoJSON -t_srs EPSG:4326 "$out" "$in"
      ;;
    *.gpkg)
      # export all layers from GPKG; suffix layer name
      local layers
      layers=$(ogrinfo -so "$in" | awk '/^1:|^ *[0-9]+:/{print $2}')
      for ly in $layers; do
        ogr2ogr -f GeoJSON -t_srs EPSG:4326 "$PROC/${base%.*}_${ly}.geojson" "$in" "$ly"
      done
      return 0
      ;;
    *.csv)
      # expect lon/lat headers or X/Y; try common mappings
      ogr2ogr -f GeoJSON -t_srs EPSG:4326 \
        -oo X_POSSIBLE_NAMES=lon,LON,LONGITUDE,x,X \
        -oo Y_POSSIBLE_NAMES=lat,LAT,LATITUDE,y,Y \
        "$out" "$in"
      ;;
    *.json|*.geojson)
      # ensure CRS & geometry validity
      ogr2ogr -f GeoJSON -t_srs EPSG:4326 "$out" "$in"
      ;;
    *.tif|*.tiff)
      # rarely: raster masks for sites → convert to COG to keep it
      local cog="$PROC/${base%.*}.cog.tif"
      rio cogeo create "$in" "$cog" --overview-level=5 --web-optimized
      return 0
      ;;
    *)
      log "Unsupported input (skip): $in"
      return 0
      ;;
  esac

  # Basic geometry fix (if polygons have issues)
  if jq . >/dev/null 2>&1 <"$out"; then
    :
  else
    log "GeoJSON not valid JSON, re-exporting simplified: $(basename "$out")"
    ogr2ogr -f GeoJSON -t_srs EPSG:4326 -simplify 0.00005 "$out" "$in"
  fi
}

_find_sources() {
  ls "$SRC_DIR"/arch_sites_*.json 2>/dev/null || true
}

# --- commands --------------------------------------------------------

cmd_init() {
  mkdir -p "$SRC_DIR" "$RAW" "$PROC" "$STAC_DIR"

  local tmpl="$SRC_DIR/arch_sites_example.json"
  if [ -f "$tmpl" ]; then
    log "Template already exists: $tmpl"
  else
    cat >"$tmpl" <<'JSON'
{
  "id": "arch_sites_example_1975",
  "title": "Archaeology Sites (Example, 1975)",
  "type": "vector",
  "version": "1.0.0",
  "description": "Example site register polygons/points from a 1975 survey.",
  "endpoints": [
    {
      "type": "http",
      "role": ["source"],
      "urls": [
        "https://example.org/arch_sites/ks_sites_1975.shp.zip"
      ],
      "notes": "Replace with actual URL or local file reference."
    }
  ],
  "spatial": {
    "bbox": [-101.0, 38.5, -99.0, 39.5],
    "crs": "EPSG:4326"
  },
  "temporal": {
    "start": "1975-01-01",
    "end": "1975-12-31"
  },
  "provenance": {
    "source": "Example Heritage Authority",
    "license": "Public Domain",
    "notes": "Digitized from 1975 field forms; QC pending."
  },
  "outputs": {
    "geojson": "data/processed/arch_sites/ks_sites_1975.geojson"
  },
  "style": {
    "stroke": "#8b0000",
    "stroke-width": 1.0,
    "fill": "#cd5c5c",
    "opacity": 0.75
  },
  "schema.source": "src/kansas_geo_timeline/schemas/source.schema.json"
}
JSON
    log "Starter source descriptor created: $tmpl"
  fi
}

cmd_fetch() {
  log "Fetching archaeology site sources..."
  local any=0
  for src in $(_find_sources); do
    any=1
    log "→ $src"
    python "$ROOT/scripts/fetch.py" --source "$src" --out "$RAW"
  done
  [ "$any" -eq 1 ] || log "No source descriptors matched: $SRC_DIR/arch_sites_*.json"
}

cmd_unpack() {
  log "Unpacking archives..."
  shopt -s nullglob
  for f in "$RAW"/*.zip "$RAW"/*.tar.gz "$RAW"/*.tgz "$RAW"/*.tar.bz2" "$RAW"/*.tbz2; do
    [ -e "$f" ] || continue
    _unzip_any "$f"
  done
  shopt -u nullglob
}

cmd_process() {
  log "Processing vectors/rasters to web-friendly outputs..."
  shopt -s nullglob
  for f in "$RAW"/*; do
    # dive into expanded directories (e.g., shapefile sets)
    if [ -d "$f" ]; then
      for g in "$f"/*; do _to_geojson "$g"; done
    else
      _to_geojson "$f"
    fi
  done
  shopt -u nullglob

  # Optional: attribute QA (ensure at least some ID field exists)
  for gj in "$PROC"/*.geojson; do
    [ -f "$gj" ] || continue
    # If no "site_id" and no "id", inject a stable id from feature index
    if ! grep -q '"site_id"' "$gj" && ! grep -q '"id"' "$gj"; then
      jq '
        .features |=
        (to_entries | map(.value.properties.site_id = ("site_" + ( (.key|tostring)))) | map(.value))
      ' "$gj" >"$TMP/site_fix.json" && mv "$TMP/site_fix.json" "$gj"
    fi
  done
}

cmd_merge() {
  # Example: merge all processed site layers into a single rollup (optional)
  local out="$PROC/_sites_rollup.geojson"
  log "Merging all site GeoJSON into: $(basename "$out")"
  ogrmerge.py -single -f GeoJSON -o "$out" "$PROC"/*.geojson >/dev/null 2>&1 || \
    log "ogrmerge not available or merge failed; skipping"
}

cmd_stac() {
  log "Generating STAC items for archaeology-sites..."
  python "$ROOT/scripts/make_stac.py" \
    --input "$PROC" \
    --output "$STAC_DIR" \
    --collection archaeology-sites \
    --id-prefix archsite \
    --tags "archaeology,site,survey,heritage" \
    --datetime-from-sources "$SRC_DIR"/arch_sites_*.json
}

cmd_validate() {
  log "Validating sources + STAC..."
  # Source schema (if you keep JSON schema here)
  if [ -f "$ROOT/src/kansas_geo_timeline/schemas/source.schema.json" ]; then
    kgt validate-sources --schema "$ROOT/src/kansas_geo_timeline/schemas/source.schema.json" \
      "$SRC_DIR"/arch_sites_*.json
  fi
  # STAC structural
  kgt validate-stac --stac "$STAC_DIR"
}

cmd_render() {
  log "Rendering web app config from STAC..."
  kgt render-config --stac "$ROOT/stac/items" --output "$ROOT/web/app.config.json" --pretty
}

cmd_clean() {
  log "Cleaning processed + temp + STAC artifacts for archaeology-sites..."
  rm -rf "$PROC"/* "$TMP"/* "$STAC_DIR"/*
}

cmd_doctor() {
  log "Doctor:"
  echo "sources:  $(ls "$SRC_DIR"/arch_sites_*.json 2>/dev/null | wc -l)"
  echo "raw:      $(ls "$RAW" 2>/dev/null | wc -l)"
  echo "proc:     $(ls "$PROC" 2>/dev/null | wc -l)"
  echo "stac:     $(ls "$STAC_DIR" 2>/dev/null | wc -l)"
  echo "app.cfg:  $(test -f "$ROOT/web/app.config.json" && echo 'present' || echo 'missing')"
}

# --- dispatch --------------------------------------------------------

case "${1:-}" in
  init)     shift; cmd_init "$@";;
  fetch)    shift; cmd_fetch "$@";;
  unpack)   shift; cmd_unpack "$@";;
  process)  shift; cmd_process "$@";;
  merge)    shift; cmd_merge "$@";;
  stac)     shift; cmd_stac "$@";;
  validate) shift; cmd_validate "$@";;
  render)   shift; cmd_render "$@";;
  clean)    shift; cmd_clean "$@";;
  doctor)   shift; cmd_doctor "$@";;
  ""|help|-h|--help)
    sed -n '1,60p' "$0" | sed 's/^# \{0,1\}//'
    ;;
  *)
    die "Unknown command: $1"
    ;;
esac

