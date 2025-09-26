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
#   deps        Check required CLI tools and scripts
#   init        Create a starter source descriptor + folders
#   fetch       Download raw sources listed in data/sources/arch_sites_*.json
#   unpack      Unzip/untar raw archives into data/raw/arch_sites/
#   process     Convert to GeoJSON (EPSG:4326), basic QA, per-item outputs
#   merge       Optional: merge site layers by year/id into rollups
#   stac        Generate STAC Items under stac/items/archaeology-sites/
#   validate    Validate STAC + source schemas (+warn if collection missing)
#   thumbs      Render 512x512 PNG thumbnails for processed layers
#   attach-thumbs  Attach thumbnails to STAC items (if missing)
#   render      Regenerate web/app.config.json (auto thumbnails)
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
#   - GDAL/ogr2ogr (and ogrinfo, gdal_rasterize, gdal_translate)
#   - rio-cogeo (for COGs if rasters sneak in)
#   - jq
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
COLLECTION_JSON="$ROOT/stac/collections/archaeology-sites.json"
THUMBS_DIR="$ROOT/web/assets/thumbnails"

mkdir -p "$RAW" "$PROC" "$TMP" "$STAC_DIR" "$THUMBS_DIR"

log() { echo "[archaeology-sites] $*" >&2; }
die() { log "ERROR: $*"; exit 1; }

_need() {
  command -v "$1" >/dev/null 2>&1 || die "missing dependency: $1"
}

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

  case "$in" in
    *.SHP|*.shp)
      ogr2ogr -f GeoJSON -t_srs EPSG:4326 "$out" "$in"
      ;;
    *.GPKG|*.gpkg)
      # export all layers from GPKG; suffix layer name
      local layers
      layers="$(ogrinfo -so "$in" 2>/dev/null | awk '/^[[:space:]]*[0-9]+:/{print $2}')"
      if [ -z "$layers" ]; then
        # fallback: try inspecting quietly
        layers="$(ogrinfo "$in" 2>/dev/null | awk '/^[[:space:]]*[0-9]+:/{print $2}')"
      fi
      if [ -z "$layers" ]; then
        log "No layers detected in $(basename "$in") (skipping)"
        return 0
      fi
      local ly
      for ly in $layers; do
        ogr2ogr -f GeoJSON -t_srs EPSG:4326 "$PROC/${base%.*}_${ly}.geojson" "$in" "$ly"
      done
      return 0
      ;;
    *.CSV|*.csv)
      # map lon/lat headers or X/Y; also try common geom names
      ogr2ogr -f GeoJSON -t_srs EPSG:4326 \
        -oo X_POSSIBLE_NAMES=lon,LON,LONGITUDE,x,X \
        -oo Y_POSSIBLE_NAMES=lat,LAT,LATITUDE,y,Y \
        -oo GEOM_POSSIBLE_NAMES=the_geom,geom \
        "$out" "$in"
      ;;
    *.JSON|*.json|*.GEOJSON|*.geojson)
      # ensure CRS & geometry validity; reproject to EPSG:4326
      ogr2ogr -f GeoJSON -t_srs EPSG:4326 "$out" "$in"
      ;;
    *.TIF|*.TIFF|*.tif|*.tiff)
      # rarely: raster masks for sites → convert to COG to keep it
      local cog="$PROC/${base%.*}.cog.tif"
      rio cogeo create "$in" "$cog" --overview-level=5 --web-optimized
      return 0
      ;;
    *)
      # skip non data files (sidecars, etc.)
      return 0
      ;;
  esac

  # Basic geometry fix (if polygons have issues OR JSON malformed)
  if ! jq . >/dev/null 2>&1 <"$out"; then
    log "GeoJSON not valid JSON, re-exporting simplified: $(basename "$out")"
    ogr2ogr -f GeoJSON -t_srs EPSG:4326 -simplify 0.00005 "$out" "$in"
  fi
}

_find_sources() {
  ls "$SRC_DIR"/arch_sites_*.json 2>/dev/null || true
}

# --- thumbnails ------------------------------------------------------
# Renders small PNG thumbnails for each processed GeoJSON (EPSG:4326)
# Output: web/assets/thumbnails/<basename>.png
# Notes:
#  - background: white
#  - fill color : #cd5c5c (205,92,92)
#  - size       : 512x512
_geom_extent() {
  local src="$1"
  ogrinfo -ro -al -so "$src" 2>/dev/null \
  | awk '
    /Extent: \(/ {
      gsub(/[(),]/, " ");
      xmin=$2; ymin=$3; xmax=$6; ymax=$7;
      print xmin, ymin, xmax, ymax;
      exit
    }'
}

_render_thumb() {
  local gj="$1"
  local base out tmp_tif xmin ymin xmax ymax ymax_fallback
  base="$(basename "$gj" .geojson)"
  out="$THUMBS_DIR/${base}.png"

  read -r xmin ymin xmax ymax < <(_geom_extent "$gj" || true)
  if [ -z "${xmin:-}" ]; then
    # fallback to Kansas bbox if extent missing
    xmin=-102.05; ymin=36.99; xmax=-94.59; ymax=40.00
  fi

  tmp_tif="$TMP/${base}.thumb.tif"
  rm -f "$tmp_tif" "$out"

  # Note: -a_ullr expects (minx, maxy, maxx, miny)
  gdal_rasterize \
    -a_srs EPSG:4326 \
    -a_ullr "$xmin" "$ymax" "$xmax" "$ymin" \
    -ot Byte -of GTiff \
    -init 255 -init 255 -init 255 \
    -ts 512 512 \
    -burn 205 -burn 92 -burn 92 \
    "$gj" "$tmp_tif" >/dev/null 2>&1 || {
      log "gdal_rasterize failed for $(basename "$gj") (skipping)"; return 0;
    }

  gdal_translate -of PNG "$tmp_tif" "$out" >/dev/null 2>&1 || {
    log "gdal_translate failed for $(basename "$gj")"; rm -f "$tmp_tif"; return 0;
  }
  rm -f "$tmp_tif"
  log "✓ thumbnail: $(basename "$out")"
}

_attach_thumb_to_item() {
  local item="$1"
  local id thumb_guess data_href b rel tmp
  id="$(jq -r '.id' "$item")"
  thumb_guess="$THUMBS_DIR/${id}.png"
  if [ ! -f "$thumb_guess" ]; then
    data_href="$(jq -r '.assets.data.href // .assets.image.href // empty' "$item")"
    if [ -n "$data_href" ]; then
      b="$(basename "$data_href")"; b="${b%.*}.png"
      thumb_guess="$THUMBS_DIR/$b"
    fi
  fi
  [ -f "$thumb_guess" ] || { log "no thumbnail for $id (skipping attach)"; return 0; }
  rel="../../web/assets/thumbnails/$(basename "$thumb_guess")"

  if jq -e 'has("assets") and (.assets|has("thumbnail"))' "$item" >/dev/null; then
    log "thumb already present: $id"
    return 0
  fi

  tmp="$TMP/$(basename "$item").tmp.json"
  jq --arg href "$rel" '
    .assets = (.assets // {}) +
    { "thumbnail": { "href": $href, "type": "image/png", "roles": ["thumbnail"], "title": "Thumbnail" } }
  ' "$item" > "$tmp" && mv "$tmp" "$item"
  log "✓ attached thumbnail: $id"
}

# --- commands --------------------------------------------------------

cmd_deps() {
  _need ogr2ogr
  _need ogrinfo
  _need gdal_rasterize
  _need gdal_translate
  _need jq
  _need rio
  _need python
  _need kgt
  [ -f "$ROOT/scripts/fetch.py" ] || die "missing script: scripts/fetch.py"
  [ -f "$ROOT/scripts/make_stac.py" ] || die "missing script: scripts/make_stac.py"
  log "All dependencies OK"
}

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
  for f in "$RAW"/*.zip "$RAW"/*.tar.gz "$RAW"/*.tgz "$RAW"/*.tar.bz2 "$RAW"/*.tbz2; do
    [ -e "$f" ] || continue
    _unzip_any "$f"
  done
  shopt -u nullglob
}

cmd_process() {
  log "Processing vectors/rasters to web-friendly outputs..."
  shopt -s nullglob
  # walk one level + immediate subdirs to catch unpacked bundles
  for f in "$RAW"/*; do
    if [ -d "$f" ]; then
      find "$f" -maxdepth 1 -type f -print0 | while IFS= read -r -d '' g; do _to_geojson "$g"; done
    else
      _to_geojson "$f"
    fi
  done
  shopt -u nullglob

  # Optional: attribute QA (ensure at least some ID field exists)
  shopt -s nullglob
  for gj in "$PROC"/*.geojson; do
    [ -f "$gj" ] || continue
    if ! grep -q '"site_id"' "$gj" && ! grep -q '"id"' "$gj"; then
      jq '
        .features |=
        (to_entries | map(.value.properties.site_id = ("site_" + ( (.key|tostring)))) | map(.value))
      ' "$gj" >"$TMP/site_fix.json" && mv "$TMP/site_fix.json" "$gj"
    fi
  done
  shopt -u nullglob
}

cmd_merge() {
  local out="$PROC/_sites_rollup.geojson"
  log "Merging all site GeoJSON into: $(basename "$out")"
  if command -v ogrmerge.py >/dev/null 2>&1; then
    ogrmerge.py -single -f GeoJSON -o "$out" "$PROC"/*.geojson >/dev/null 2>&1 || \
      log "merge failed; skipping"
  else
    log "ogrmerge.py not available; skipping"
  fi
}

cmd_stac() {
  log "Generating STAC items for archaeology-sites..."
  if [ ! -f "$COLLECTION_JSON" ]; then
    log "WARNING: STAC collection missing: $COLLECTION_JSON"
    log "         Add stac/collections/archaeology-sites.json to parent items."
  fi
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
  # Source schema (optional)
  if [ -f "$ROOT/src/kansas_geo_timeline/schemas/source.schema.json" ]; then
    kgt validate-sources --schema "$ROOT/src/kansas_geo_timeline/schemas/source.schema.json" \
      "$SRC_DIR"/arch_sites_*.json || die "source schema validation failed"
  fi
  # STAC structural
  kgt validate-stac --stac "$STAC_DIR" || die "STAC validation failed"
  # Collection presence
  if [ ! -f "$COLLECTION_JSON" ]; then
    log "WARNING: collection not found: $COLLECTION_JSON (items will lack a proper parent)"
  fi
}

cmd_thumbs() {
  log "Rendering thumbnails for processed archaeology site layers..."
  shopt -s nullglob
  for gj in "$PROC"/*.geojson; do
    [ -f "$gj" ] || continue
    _render_thumb "$gj"
  done
  shopt -u nullglob
}

cmd_attach_thumbs() {
  log "Attaching thumbnails to STAC items (if missing)..."
  shopt -s nullglob
  for item in "$STAC_DIR"/*.json; do
    [ -f "$item" ] || continue
    _attach_thumb_to_item "$item"
  done
  shopt -u nullglob
}

cmd_render() {
  log "Rendering web app config from STAC..."
  # Generate/attach thumbnails opportunistically (non-fatal)
  cmd_thumbs || true
  cmd_attach_thumbs || true
  kgt render-config --stac "$ROOT/stac/items" --output "$ROOT/web/app.config.json" --pretty
}

cmd_clean() {
  log "Cleaning processed + temp + STAC artifacts for archaeology-sites..."
  rm -rf "$PROC"/* "$TMP"/* "$STAC_DIR"/*
}

cmd_doctor() {
  log "Doctor:"
  echo "sources:  $(ls "$SRC_DIR"/arch_sites_*.json 2>/dev/null | wc -l | tr -d ' ')"
  echo "raw:      $(find "$RAW" -maxdepth 1 -type f 2>/dev/null | wc -l | tr -d ' ')"
  echo "proc:     $(find "$PROC" -maxdepth 1 -type f -name '*.geojson' 2>/dev/null | wc -l | tr -d ' ')"
  echo "thumbs:   $(find "$THUMBS_DIR" -maxdepth 1 -type f -name '*.png' 2>/dev/null | wc -l | tr -d ' ')"
  echo "stac:     $(find "$STAC_DIR" -maxdepth 1 -type f -name '*.json' 2>/dev/null | wc -l | tr -d ' ')"
  echo "collection: $(test -f "$COLLECTION_JSON" && echo 'present' || echo 'missing')"
  echo "app.cfg:  $(test -f "$ROOT/web/app.config.json" && echo 'present' || echo 'missing')"
}

# --- dispatch --------------------------------------------------------

case "${1:-}" in
  deps)     shift; cmd_deps "$@";;
  init)     shift; cmd_init "$@";;
  fetch)    shift; cmd_fetch "$@";;
  unpack)   shift; cmd_unpack "$@";;
  process)  shift; cmd_process "$@";;
  merge)    shift; cmd_merge "$@";;
  stac)     shift; cmd_stac "$@";;
  validate) shift; cmd_validate "$@";;
  thumbs)   shift; cmd_thumbs "$@";;
  attach-thumbs|thumbs-attach) shift; cmd_attach_thumbs "$@";;
  render)   shift; cmd_render "$@";;
  clean)    shift; cmd_clean "$@";;
  doctor)   shift; cmd_doctor "$@";;
  ""|help|-h|--help)
    sed -n '1,120p' "$0" | sed 's/^# \{0,1\}//'
    ;;
  *)
    die "Unknown command: $1"
    ;;
esac
