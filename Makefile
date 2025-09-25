# --------------------------------------------------------------------
# Kansas Frontier Matrix / Kansas Geo Timeline — Makefile (connected+safe)
# --------------------------------------------------------------------
# Targets: help, env, fetch, cogs, terrain, slope_classes, aspect_sectors,
#          meta, stac, stac-validate, site, site-config, kml, clean, prebuild
# Extras:  dem-checksum, hillshade-checksum
# Dev:     install-dev, test, test-cli, test-sources, preview, prebuild-lite
# Data:    nlcd   (1992–2021 NLCD land-cover → COGs, provenance)
# Notes:
#   - Repo-aware STAC path: ./stac
#   - Script fallbacks + GDAL tools when available
#   - Optional: KGS Kansas River hydrology fetch/export → STAC wiring
#   - Auto-patch STAC (DEM checksum/size) inside `make stac` if checksum exists
# --------------------------------------------------------------------

SHELL := /bin/bash
.SHELLFLAGS := -euo pipefail -c
.ONESHELL:
.DEFAULT_GOAL := help
.DELETE_ON_ERROR:

# -------- Paths --------
PY      := python
S       := scripts
DATA    := data
SRC     := $(DATA)/sources
RAW     := $(DATA)/raw
COGS    := $(DATA)/cogs
DEMS    := $(COGS)/dem
HILLS   := $(COGS)/hillshade
TERRAIN := $(COGS)/terrain
DERIV   := $(DATA)/derivatives
VEC     := $(DATA)/processed/vectors
WEB     := web
STAC    := stac
TESTS   := tests

# Core DEM (override via: make terrain DEM=/path/to/dem.tif)
DEM ?= $(DEMS)/ks_1m_dem_2018_2020.tif

# Outputs (COGs)
HILLSHADE := $(HILLS)/ks_hillshade_2018_2020.tif
SLOPE     := $(TERRAIN)/ks_slope_deg.tif
ASPECT    := $(TERRAIN)/ks_aspect_deg.tif

# Optional vectors
SLOPE_CLASSES   := $(VEC)/slope_classes.geojson
ASPECT_SECTORS  := $(VEC)/aspect_sectors.geojson

# Optional meta files
META_SLOPE  := $(SRC)/ks_slope.meta.json
META_ASPECT := $(SRC)/ks_aspect.meta.json

# -------- NLCD (1992–2021) — Kansas COGs --------
NLCD_YEARS    ?= 1992 2001 2006 2011 2016 2019 2021
NLCD_SRC_DIR  ?= $(DATA)/sources/land
NLCD_DST_DIR  ?= $(NLCD_SRC_DIR)/vectors
NLCD_BBOX     ?= -102.05 36.99 -94.61 40.00   # minx miny maxx maxy
define NLCD_SRC_PATH
$(NLCD_SRC_DIR)/raw/NLCD_$(1)_CONUS.tif
endef
define NLCD_COG_PATH
$(NLCD_DST_DIR)/nlcd_$(1)_ks_cog.tif
endef

# -------- Tools & flags --------
COG_OPTS   ?= -co TILED=YES -co COMPRESS=DEFLATE -co PREDICTOR=2 -co BIGTIFF=IF_SAFER
OVERVIEWS  ?= 2 4 8 16

# sha utility (sha256sum/gsha256sum on Linux/Homebrew, shasum -a 256 on macOS)
SHA256_BIN    := $(shell { command -v sha256sum || command -v gsha256sum || command -v shasum; } 2>/dev/null)
SHA256_IS_GNU := $(shell { command -v sha256sum || command -v gsha256sum; } >/dev/null 2>&1 && echo yes || echo no)
SHA256FLAGS   := $(if $(filter yes,$(SHA256_IS_GNU)),,-a 256)

# External tools
HAVE_JQ     := $(shell command -v jq >/dev/null 2>&1 && echo yes || echo no)
HAVE_RSYNC  := $(shell command -v rsync >/dev/null 2>&1 && echo yes || echo no)
HAVE_KGT    := $(shell command -v kgt   >/dev/null 2>&1 && echo yes || echo no)

# GDAL tools
HAVE_GDALDEM   := $(shell command -v gdaldem >/dev/null 2>&1 && echo yes || echo no)
HAVE_GDALTRANS := $(shell command -v gdal_translate >/dev/null 2>&1 && echo yes || echo no)
HAVE_GDALADDO  := $(shell command -v gdaladdo >/dev/null 2>&1 && echo yes || echo no)
HAVE_GDALWARP  := $(shell command -v gdalwarp >/dev/null 2>&1 && echo yes || echo no)

GDAL_POLY_BIN  := $(shell command -v gdal_polygonize.py >/dev/null 2>&1 && echo gdal_polygonize.py || (command -v gdal_polygonize >/dev/null 2>&1 && echo gdal_polygonize || echo ""))
GDAL_CALC_BIN  := $(shell command -v gdal_calc.py      >/dev/null 2>&1 && echo gdal_calc.py      || (command -v gdal_calc      >/dev/null 2>&1 && echo gdal_calc      || echo ""))

# Detect helper scripts present in this repo (value = path or empty)
HAVE_FETCH            := $(wildcard $(S)/fetch.py)
HAVE_MAKECOG          := $(wildcard $(S)/make_cog.py)
HAVE_MAKEHILLSHADE    := $(wildcard $(S)/make_hillshade.py)
HAVE_WRITEMETA        := $(wildcard $(S)/write_meta.py)
HAVE_MAKE_STAC        := $(wildcard $(S)/make_stac.py)
HAVE_VALIDATE_STAC    := $(wildcard $(S)/validate_stac.py)
HAVE_VALIDATE_SOURCES := $(wildcard $(S)/validate_sources.py)
HAVE_GEN_SHA          := $(wildcard $(S)/gen_sha256.sh)
HAVE_PATCH_ASSET      := $(wildcard $(S)/patch_stac_asset.py)

# CI-aware test leniency (fail in CI, be lenient locally)
ifeq ($(CI),true)
ALLOW_FAIL :=
else
ALLOW_FAIL := || true
endif

# Dual checksum file style (also write <name>.tif.sha256 when set)
ALSO_TIF_SHA ?= 0

# -------- Kansas River Hydrology (optional integration) --------
KSRIV_OUTDIR     := $(DATA)/processed/hydrology/kansas_river
KSRIV_CHANNELS   ?= REPLACE_WITH_ARCGIS_REST_LAYER_URL_CHANNELS
KSRIV_FLOODPLAIN ?= REPLACE_WITH_ARCGIS_REST_LAYER_URL_FLOODPLAINS
KSRIV_GAUGES     ?= REPLACE_WITH_ARCGIS_REST_LAYER_URL_GAUGES

KSRIV_CHANNELS_GJ   := $(KSRIV_OUTDIR)/channels.geojson
KSRIV_FLOODPLAIN_GJ := $(KSRIV_OUTDIR)/floodplains.geojson
KSRIV_GAUGES_GJ     := $(KSRIV_OUTDIR)/gauges.geojson

KSRIV_ITEM_DIR      := $(STAC)/items
KSRIV_ITEM_CHANNELS := $(KSRIV_ITEM_DIR)/ks_kansas_river_channels.json
KSRIV_ITEM_FP       := $(KSRIV_ITEM_DIR)/ks_kansas_river_floodplains.json
KSRIV_ITEM_GAUGES   := $(KSRIV_ITEM_DIR)/ks_kansas_river_gauges.json

# -------- Internal helpers --------
define check_dem
	@if [ ! -f "$(DEM)" ]; then \
	  echo "ERROR: DEM not found at '$(DEM)'"; \
	  echo "       Build your DEM COG or pass DEM=/path/to/dem.tif"; \
	  exit 1; \
	fi
endef

define ensure_dir
	@mkdir -p "$(1)"
endef

define mirror_derivatives
	$(call ensure_dir,$(dir $(2)))
	@if [ -f "$(1)" ]; then \
	  if [ "$(HAVE_RSYNC)" = "yes" ]; then rsync -a --checksum "$(1)" "$(2)"; else cp -f "$(1)" "$(2)"; fi; \
	fi
endef

# -------- PHONY --------
.PHONY: help env prebuild preview prebuild-lite print-% fetch cogs terrain slope_classes aspect_sectors meta stac stac-validate site-config kml site clean \
        dem-checksum hillshade-checksum hydrology-fetch hydrology-stac nlcd \
        install-dev test test-cli test-sources

# -------- Help --------
help:
	@echo ""
	@echo "Targets:"
	@echo "  env               Show detected tools/paths"
	@echo "  fetch             Download rasters/vectors per data/sources/*.json"
	@echo "  cogs              Build Cloud-Optimized GeoTIFFs (COGs) with overviews"
	@echo "  terrain           Derive hillshade/slope/aspect (COGs); mirror into data/derivatives"
	@echo "  slope_classes     Optional: vectorize slope classes"
	@echo "  aspect_sectors    Optional: vectorize 8-way aspect sectors"
	@echo "  meta              Optional: update terrain meta JSON checksums (slope/aspect)"
	@echo "  stac              Build STAC items/collections into ./stac/ (auto-patches DEM if checksum exists)"
	@echo "  stac-validate     Validate STAC + source schemas (scripts/ or kgt)"
	@echo "  site              Write web/layers.json (simple preview)"
	@echo "  site-config       Render web/app.config.json from STAC via kgt (if available)"
	@echo "  kml               Build KMZ overlays (placeholder)"
	@echo "  clean             Remove generated raster outputs (keeps stac/)"
	@echo "  prebuild          stac-validate + site (used by CI)"
	@echo "  preview           Minimal local preview (site only)"
	@echo "  prebuild-lite     Site only (no validation/checksums)"
	@echo ""
	@echo "Data:"
	@echo "  nlcd              Build NLCD (1992–2021) COGs for Kansas (expects raw files under data/sources/land/raw)"
	@echo ""
	@echo "Checksums:"
	@echo "  dem-checksum         Write+verify checksum(s) for DEM and print STAC fields"
	@echo "  hillshade-checksum   Write+verify checksum(s) for hillshade"
	@echo ""
	@echo "Hydrology (optional):"
	@echo "  hydrology-fetch   Export Kansas River channels/floodplains/gauges (GeoJSON)"
	@echo "  hydrology-stac    Wire local GeoJSON hrefs into the hydrology STAC Items"
	@echo ""
	@echo "Dev:"
	@echo "  install-dev, test, test-cli, test-sources"
	@echo ""
	@echo "Overrides:  make terrain DEM=/path/to/dem.tif"
	@echo ""

env:
	@echo "PY=$(PY)"
	@echo "DEM=$(DEM)"
	@echo "STAC_DIR=$(STAC)"
	@echo "HAVE_KGT=$(HAVE_KGT)  HAVE_JQ=$(HAVE_JQ)"
	@echo "HAVE_GDALDEM=$(HAVE_GDALDEM) HAVE_GDALTRANS=$(HAVE_GDALTRANS) HAVE_GDALADDO=$(HAVE_GDALADDO) HAVE_GDALWARP=$(HAVE_GDALWARP)"
	@echo "GDAL_POLY_BIN=$(GDAL_POLY_BIN) GDAL_CALC_BIN=$(GDAL_CALC_BIN)"
	@echo "HAVE_FETCH=$(if $(HAVE_FETCH),yes,no) HAVE_MAKECOG=$(if $(HAVE_MAKECOG),yes,no) HAVE_MAKEHILLSHADE=$(if $(HAVE_MAKEHILLSHADE),yes,no)"
	@echo "HAVE_MAKE_STAC=$(if $(HAVE_MAKE_STAC),yes,no) HAVE_VALIDATE_STAC=$(if $(HAVE_VALIDATE_STAC),yes,no) HAVE_VALIDATE_SOURCES=$(if $(HAVE_VALIDATE_SOURCES),yes,no)"
	@echo "HAVE_PATCH_ASSET=$(if $(HAVE_PATCH_ASSET),yes,no)"
	@echo "SHA256=$(SHA256_BIN)  SHA256FLAGS=$(SHA256FLAGS)  HAVE_GEN_SHA=$(if $(HAVE_GEN_SHA),yes,no)"

print-%:
	@echo '$*=$($*)'

prebuild: stac-validate site
	@echo ">> Prebuild complete."

preview: site
	@echo "✓ preview assets written (skipped STAC validation/patching)"

prebuild-lite: site
	@echo ">> Prebuild-lite complete (no validation/checksums)."

# -------- Fetch --------
fetch: | $(RAW)
ifeq ($(strip $(HAVE_FETCH)),)
	@echo "[fetch] No $(S)/fetch.py found. Skipping."
else
	$(PY) "$(S)/fetch.py" --sources "$(SRC)" --out "$(RAW)"
endif

# -------- COGS --------
cogs: | $(COGS)
ifeq ($(strip $(HAVE_MAKECOG)),)
	@echo "[cogs] No $(S)/make_cog.py found. Skipping."
else
	$(PY) "$(S)/make_cog.py" --in "$(RAW)" --out "$(COGS)"
endif

# -------- Terrain (COGs) --------
terrain: $(HILLSHADE) $(SLOPE) $(ASPECT)
	$(call mirror_derivatives,$(HILLSHADE),$(DERIV)/hillshade.tif)
	$(call mirror_derivatives,$(SLOPE),$(DERIV)/slope.tif)
	$(call mirror_derivatives,$(ASPECT),$(DERIV)/aspect.tif)
	@echo "✓ terrain built (COGs) and mirrored into $(DERIV)"

$(HILLSHADE): $(DEM) | $(HILLS)
	$(check_dem)
	@if [ -n "$(HAVE_MAKEHILLSHADE)" ]; then \
	  echo "[hillshade] $(S)/make_hillshade.py"; \
	  $(PY) "$(S)/make_hillshade.py" --dem "$(DEM)" --out "$@" --cog; \
	elif [ "$(HAVE_GDALDEM)" = "yes" ] && [ "$(HAVE_GDALADDO)" = "yes" ] && [ "$(HAVE_GDALTRANS)" = "yes" ]; then \
	  echo "[hillshade] gdaldem hillshade"; \
	  tmp="$@.$$$$.tmp.tif"; \
	  gdaldem hillshade "$(DEM)" "$$tmp" -compute_edges -z 1.0 -az 315 -alt 45; \
	  gdaladdo -r average "$$tmp" $(OVERVIEWS); \
	  gdal_translate "$$tmp" "$@" $(COG_OPTS); \
	  rm -f "$$tmp"; \
	else \
	  echo "ERROR: neither $(S)/make_hillshade.py nor sufficient GDAL tools available."; exit 1; \
	fi

$(SLOPE): $(DEM) | $(TERRAIN)
	$(check_dem)
	@if [ "$(HAVE_GDALDEM)" = "yes" ] && [ "$(HAVE_GDALADDO)" = "yes" ] && [ "$(HAVE_GDALTRANS)" = "yes" ]; then \
	  echo "[slope] gdaldem slope (degrees)"; \
	  tmp="$@.$$$$.tmp.tif"; \
	  gdaldem slope "$(DEM)" "$$tmp" -compute_edges -s 1.0; \
	  gdaladdo -r average "$$tmp" $(OVERVIEWS); \
	  gdal_translate "$$tmp" "$@" $(COG_OPTS); \
	  rm -f "$$tmp"; \
	else \
	  echo "ERROR: gdaldem/gdaladdo/gdal_translate required for slope."; exit 1; \
	fi

$(ASPECT): $(DEM) | $(TERRAIN)
	$(check_dem)
	@if [ "$(HAVE_GDALDEM)" = "yes" ] && [ "$(HAVE_GDALADDO)" = "yes" ] && [ "$(HAVE_GDALTRANS)" = "yes" ]; then \
	  echo "[aspect] gdaldem aspect (0–360°)"; \
	  tmp="$@.$$$$.tmp.tif"; \
	  gdaldem aspect "$(DEM)" "$$tmp" -compute_edges; \
	  gdaladdo -r average "$$tmp" $(OVERVIEWS); \
	  gdal_translate "$$tmp" "$@" $(COG_OPTS); \
	  rm -f "$$tmp"; \
	else \
	  echo "ERROR: gdaldem/gdaladdo/gdal_translate required for aspect."; exit 1; \
	fi

# -------- Optional vectors --------
slope_classes: $(SLOPE) | $(VEC)
	@if [ -n "$(GDAL_CALC_BIN)" ] && [ -n "$(GDAL_POLY_BIN)" ]; then \
	  echo "[slope_classes] binning slope → polygons"; \
	  tmp=$$(mktemp -t kfm_slope_classes.XXXXXX.tif); \
	  $(GDAL_CALC_BIN) -A "$(SLOPE)" --NoDataValue=0 \
	    --calc="(A>=0)*(A<2)*1 + (A>=2)*(A<5)*2 + (A>=5)*(A<10)*3 + (A>=10)*(A<20)*4 + (A>=20)*(A<30)*5 + (A>=30)*(A<45)*6 + (A>=45)*7" \
	    --outfile="$$tmp" --type=Byte $(COG_OPTS); \
	  $(GDAL_POLY_BIN) "$$tmp" -f GeoJSON "$(SLOPE_CLASSES)"; \
	  rm -f "$$tmp"; \
	else \
	  echo "[slope_classes] GDAL calc/polygonize not available. Skipping."; \
	fi

aspect_sectors: $(ASPECT) | $(VEC)
	@if [ -n "$(GDAL_CALC_BIN)" ] && [ -n "$(GDAL_POLY_BIN)" ]; then \
	  echo "[aspect_sectors] binning 8-way aspect → polygons"; \
	  tmp=$$(mktemp -t kfm_aspect_sectors.XXXXXX.tif); \
	  $(GDAL_CALC_BIN) -A "$(ASPECT)" --NoDataValue=0 \
	    --calc="(A<22.5)*(A>=0)*1 + (A>=22.5)*(A<67.5)*2 + (A>=67.5)*(A<112.5)*3 + (A>=112.5)*(A<157.5)*4 + (A>=157.5)*(A<202.5)*5 + (A>=202.5)*(A<247.5)*6 + (A>=247.5)*(A<292.5)*7 + (A>=292.5)*(A<337.5)*8 + (A>=337.5)*1" \
	    --outfile="$$tmp" --type=Byte $(COG_OPTS); \
	  $(GDAL_POLY_BIN) "$$tmp" -f GeoJSON "$(ASPECT_SECTORS)"; \
	  rm -f "$$tmp"; \
	else \
	  echo "[aspect_sectors] GDAL calc/polygonize not available. Skipping."; \
	fi

# -------- NLCD (1992–2021) — Kansas COGs --------
nlcd: $(foreach Y,$(NLCD_YEARS),$(call NLCD_COG_PATH,$(Y)))
	@echo "✓ NLCD COGs built under $(NLCD_DST_DIR)"

# Build one year: clip (nearest), COG, provenance update (if script present)
$(NLCD_DST_DIR)/nlcd_%_ks_cog.tif: $(NLCD_SRC_DIR)/raw/NLCD_%_CONUS.tif
	@mkdir -p $(NLCD_DST_DIR)
	@if [ "$(HAVE_GDALWARP)" != "yes" ] || [ "$(HAVE_GDALTRANS)" != "yes" ]; then echo "ERROR: gdalwarp/gdal_translate required for NLCD"; exit 1; fi
	@echo "[nlcd] $* → clip to Kansas bbox (nearest)"
	@tmp=$$(mktemp -t nlcd_$*_ks.XXXXXX.tif); \
	gdalwarp -te $(NLCD_BBOX) -r near -multi -overwrite "$<" "$$tmp"; \
	echo "[nlcd] $* → translate to COG"; \
	gdal_translate "$$tmp" "$@" -of COG -co COMPRESS=LZW -co NUM_THREADS=ALL_CPUS -co OVERVIEWS=IGNORE_EXISTING; \
	rm -f "$$tmp"; \
	echo "[nlcd] $* → provenance update"; \
	{ test -f "$(S)/update_registry.py" && $(PY) "$(S)/update_registry.py" "$@" "landcover_nlcd_$*"; } || true

# Optional helper to nudge users to put raw files in place
$(NLCD_SRC_DIR)/raw/NLCD_%_CONUS.tif:
	@mkdir -p $(NLCD_SRC_DIR)/raw
	@echo "!! Please download NLCD $* GeoTIFF from MRLC and place at $@"
	@exit 1

# -------- Meta checksums (optional) --------
meta: $(SLOPE) $(ASPECT)
	@if [ -f "$(META_SLOPE)" ] || [ -f "$(META_ASPECT)" ]; then \
	  if [ -n "$(SHA256_BIN)" ]; then \
	    echo "[meta] updating simple checksums (sha256)"; \
	    if [ -f "$(META_SLOPE)" ]; then \
	      SUM_DEM=$$($(SHA256_BIN) $(SHA256FLAGS) "$(DEM)" | awk '{print $$1}'); \
	      SUM_SLOPE=$$($(SHA256_BIN) $(SHA256FLAGS) "$(SLOPE)" | awk '{print $$1}'); \
	      $(PY) - <<'PYCODE' "$(META_SLOPE)" "$$SUM_DEM" "$$SUM_SLOPE"
import json, sys, os
p, dem, slope = sys.argv[1:]
d=json.load(open(p))
d.setdefault("inputs",{}).setdefault("dem_cog",{})["checksum"]=dem
d.setdefault("outputs",{}).setdefault("slope_cog",{})["checksum"]=slope
json.dump(d, open(p,'w'), indent=2)
print("updated", os.path.basename(p))
PYCODE \
	    ; fi; \
	    if [ -f "$(META_ASPECT)" ]; then \
	      SUM_DEM=$$($(SHA256_BIN) $(SHA256FLAGS) "$(DEM)" | awk '{print $$1}'); \
	      SUM_ASPECT=$$($(SHA256_BIN) $(SHA256FLAGS) "$(ASPECT)" | awk '{print $$1}'); \
	      $(PY) - <<'PYCODE' "$(META_ASPECT)" "$$SUM_DEM" "$$SUM_ASPECT"
import json, sys, os
p, dem, aspect = sys.argv[1:]
d=json.load(open(p))
d.setdefault("inputs",{}).setdefault("dem_cog",{})["checksum"]=dem
d.setdefault("outputs",{}).setdefault("aspect_cog",{})["checksum"]=aspect
json.dump(d, open(p,'w'), indent=2)
print("updated", os.path.basename(p))
PYCODE \
	    ; fi; \
	  else \
	    echo "[meta] sha256 tool not found. Skipping."; \
	  fi; \
	else \
	  echo "[meta] no META_* json files found. Skipping."; \
	fi

# -------- STAC build / validate (auto-patch DEM if checksum exists) --------
stac: | $(STAC)/items $(STAC)/collections
ifeq ($(strip $(HAVE_MAKE_STAC)),)
	@echo "[stac] No $(S)/make_stac.py found. Skipping."
else
	$(PY) "$(S)/make_stac.py" --data "$(DATA)" --stac "$(STAC)"
endif
	@ITEM="$(STAC)/items/dem/ks_1m_dem_2018_2020.json"; \
	if [ -f "$(DEM:.tif=.sha256)" ] && [ -f "$$ITEM" ]; then \
	  echo "[stac] checksum detected → auto-patching DEM asset"; \
	  if [ -n "$(HAVE_PATCH_ASSET)" ]; then \
	    $(PY) "$(S)/patch_stac_asset.py" "$$ITEM" --asset dem --from-file-size --from-sha256-file --pretty; \
	  else \
	    SIZE=$$($(PY) - <<'PYCODE' "$(DEM)"
import os, sys; print(os.path.getsize(sys.argv[1]))
PYCODE \
	    ); HEX=$$(cut -d' ' -f1 "$(DEM:.tif=.sha256)"); \
	    $(PY) - <<'PYCODE' "$$ITEM" "$$SIZE" "$$HEX"
import json, sys, pathlib
p, size, hexsum = pathlib.Path(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
d = json.loads(p.read_text())
asset = d.setdefault("assets",{}).setdefault("dem",{})
asset["checksum:sha256"] = hexsum
asset["file:size"] = size
p.write_text(json.dumps(d, indent=2))
print("[stac] auto-patched DEM checksum/size")
PYCODE \
	  ; fi; \
	else \
	  echo "[stac] checksum not found; skipping auto-patch"; \
	fi

stac-validate:
	@if [ -n "$(HAVE_VALIDATE_SOURCES)" ]; then \
	  $(PY) "$(S)/validate_sources.py" --sources "$(SRC)"; \
	else \
	  echo "[stac-validate] $(S)/validate_sources.py missing (source schema check skipped)."; \
	fi
	@if [ -n "$(HAVE_VALIDATE_STAC)" ]; then \
	  $(PY) "$(S)/validate_stac.py" --stac "$(STAC)"; \
	elif [ "$(HAVE_KGT)" = "yes" ]; then \
	  echo "[stac-validate] scripts missing; using kgt validate-stac as fallback"; \
	  kgt validate-stac "$(STAC)/items" --no-strict; \
	else \
	  echo "[stac-validate] No validators found (install kgt or add scripts/validate_stac.py)."; \
	fi

# -------- Web viewer config (optional, via kgt) --------
site-config: | $(WEB)
	@if [ "$(HAVE_KGT)" = "yes" ]; then \
	  if [ -f "src/kansas_geo_timeline/templates/app.config.json.j2" ]; then \
	    kgt render-config --stac "$(STAC)/items" --output "$(WEB)/app.config.json" --pretty; \
	  else \
	    echo "[site-config] Template missing (src/.../templates/app.config.json.j2)."; \
	  fi; \
	else \
	  echo "[site-config] kgt not installed (pip install -e . && pip install jinja2)."; \
	fi

# -------- KML / KMZ (legacy demo) --------
kml: terrain
	@echo "[kml] Legacy prototype. Provide your regionate script if needed."

# -------- Simple site manifest (always available) --------
site: | $(WEB)
	@$(PY) - <<'PYCODE'
import json, pathlib
p = pathlib.Path('web/layers.json')
p.parent.mkdir(parents=True, exist_ok=True)
layers = {
  "layers": [
    {"id": "hillshade", "title": "Hillshade",     "type": "raster", "path": "../data/derivatives/hillshade.tif"},
    {"id": "slope",     "title": "Slope (deg)",   "type": "raster", "path": "../data/derivatives/slope.tif"},
    {"id": "aspect",    "title": "Aspect (deg)",  "type": "raster", "path": "../data/derivatives/aspect.tif"}
  ]
}
json.dump(layers, open(p, 'w'), indent=2)
print("wrote", p)
PYCODE

# -------- Checksums (COGs) --------
dem-checksum:
	@if [ -n "$(HAVE_GEN_SHA)" ]; then \
	  bash "$(S)/gen_sha256.sh" "$(DEM)"; \
	elif [ -n "$(SHA256_BIN)" ]; then \
	  echo "• hashing $(DEM) → $(DEM:.tif=.sha256)"; \
	  ( cd "$$(dirname "$(DEM)")" && $(SHA256_BIN) $(SHA256FLAGS) "$$(basename "$(DEM)")" > "$$(basename "$(DEM:.tif=.sha256)")" ); \
	  if [ "$(ALSO_TIF_SHA)" = "1" ]; then cp -f "$(DEM:.tif=.sha256)" "$(DEM).sha256"; fi; \
	  echo "• verifying"; \
	  ( cd "$$(dirname "$(DEM)")" && { command -v sha256sum >/dev/null 2>&1 || command -v gsha256sum >/dev/null 2>&1; } && sha256sum -c "$$(basename "$(DEM:.tif=.sha256)")" >/dev/null || shasum -a 256 -c "$$(basename "$(DEM:.tif=.sha256)")" >/dev/null ); \
	  SIZE=$$($(PY) - <<'PYCODE' "$(DEM)"
import os, sys; print(os.path.getsize(sys.argv[1]))
PYCODE \
	  ); HEX=$$(cut -d' ' -f1 "$(DEM:.tif=.sha256)"); \
	  echo "STAC patch fields:"; \
	  echo "  \"file:size\": $$SIZE,"; \
	  echo "  \"checksum:sha256\": \"$$HEX\""; \
	else \
	  echo "ERROR: No SHA tool found; install coreutils (sha256sum/gsha256sum) or use scripts/gen_sha256.sh"; exit 1; \
	fi

hillshade-checksum:
	@if [ -n "$(HAVE_GEN_SHA)" ]; then \
	  bash "$(S)/gen_sha256.sh" "$(HILLSHADE)"; \
	elif [ -n "$(SHA256_BIN)" ]; then \
	  echo "• hashing $(HILLSHADE) → $(HILLSHADE:.tif=.sha256)"; \
	  ( cd "$$(dirname "$(HILLSHADE)")" && $(SHA256_BIN) $(SHA256FLAGS) "$$(basename "$(HILLSHADE)")" > "$$(basename "$(HILLSHADE:.tif=.sha256)")" ); \
	  if [ "$(ALSO_TIF_SHA)" = "1" ]; then cp -f "$(HILLSHADE:.tif=.sha256)" "$(HILLSHADE).sha256"; fi; \
	  echo "• verifying"; \
	  ( cd "$$(dirname "$(HILLSHADE)")" && { command -v sha256sum >/dev/null 2>&1 || command -v gsha256sum >/dev/null 2>&1; } && sha256sum -c "$$(basename "$(HILLSHADE:.tif=.sha256)")" >/dev/null || shasum -a 256 -c "$$(basename "$(HILLSHADE:.tif=.sha256)")" >/dev/null ); \
	else \
	  echo "ERROR: No SHA tool found; install coreutils (sha256sum/gsha256sum) or use scripts/gen_sha256.sh"; exit 1; \
	fi

# -------- Clean --------
clean:
	rm -rf "$(COGS)" "$(DERIV)" "$(DATA)"/kml "$(DATA)"/*.kmz || true
	@echo "✓ cleaned generated raster outputs (kept ./stac and $(DATA)/raw)."

# ====================================================================
# Kansas River Hydrology — fetch/export + STAC wiring (optional)
# ====================================================================

hydrology-fetch: | $(KSRIV_OUTDIR)
	@if [ "$(KSRIV_CHANNELS)" = "REPLACE_WITH_ARCGIS_REST_LAYER_URL_CHANNELS" ]; then echo "Set KSRIV_CHANNELS=..."; exit 1; fi
	@if [ "$(KSRIV_FLOODPLAIN)" = "REPLACE_WITH_ARCGIS_REST_LAYER_URL_FLOODPLAINS" ]; then echo "Set KSRIV_FLOODPLAIN=..."; exit 1; fi
	@if [ "$(KSRIV_GAUGES)" = "REPLACE_WITH_ARCGIS_REST_LAYER_URL_GAUGES" ]; then echo "Set KSRIV_GAUGES=..."; exit 1; fi
	@if ! command -v ogr2ogr >/dev/null 2>&1; then echo "ERROR: ogr2ogr (GDAL) is required."; exit 1; fi
	ogr2ogr -f GeoJSON "$(KSRIV_CHANNELS_GJ)"   "$(KSRIV_CHANNELS)?where=1=1&f=json&outSR=4326"    -t_srs EPSG:4326
	ogr2ogr -f GeoJSON "$(KSRIV_FLOODPLAIN_GJ)" "$(KSRIV_FLOODPLAIN)?where=1=1&f=json&outSR=4326" -t_srs EPSG:4326
	ogr2ogr -f GeoJSON "$(KSRIV_GAUGES_GJ)"     "$(KSRIV_GAUGES)?where=1=1&f=json&outSR=4326"     -t_srs EPSG:4326
	@echo "✓ Kansas River hydrology exported → $(KSRIV_OUTDIR)"

hydrology-stac:
	@if [ "$(HAVE_JQ)" != "yes" ]; then echo "ERROR: jq is required for hydrology-stac"; exit 1; fi
	@if [ ! -f "$(KSRIV_ITEM_CHANNELS)" ] || [ ! -f "$(KSRIV_ITEM_FP)" ] || [ ! -f "$(KSRIV_ITEM_GAUGES)" ]; then \
	  echo "ERROR: hydrology STAC items missing under $(STAC)/items"; exit 1; fi
	jq --arg H "$(KSRIV_CHANNELS_GJ)"   '.assets.geojson.href = $H' "$(KSRIV_ITEM_CHANNELS)" > "$(KSRIV_ITEM_CHANNELS).tmp" && mv "$(KSRIV_ITEM_CHANNELS).tmp" "$(KSRIV_ITEM_CHANNELS)"
	jq --arg H "$(KSRIV_FLOODPLAIN_GJ)" '.assets.geojson.href = $H' "$(KSRIV_ITEM_FP)"       > "$(KSRIV_ITEM_FP).tmp"       && mv "$(KSRIV_ITEM_FP).tmp"       "$(KSRIV_ITEM_FP)"
	jq --arg H "$(KSRIV_GAUGES_GJ)"     '.assets.geojson.href = $H' "$(KSRIV_ITEM_GAUGES)"   > "$(KSRIV_ITEM_GAUGES).tmp"   && mv "$(KSRIV_ITEM_GAUGES).tmp"   "$(KSRIV_ITEM_GAUGES)"
	@echo "✓ STAC Items updated with local GeoJSON hrefs"

# ====================================================================
# Dev / Tests
# ====================================================================

install-dev:
	@python -m pip install --upgrade pip
	@python -m pip install -r requirements-dev.txt $(ALLOW_FAIL)

test: install-dev
	@pytest -q $(ALLOW_FAIL)

test-cli: install-dev
	@pytest -q $(TESTS)/test_cli.py $(ALLOW_FAIL)

test-sources: install-dev
	@pytest -q $(TESTS)/test_sources.py $(ALLOW_FAIL)

# -------- Order-only dir prereqs --------
$(RAW) $(COGS) $(HILLS) $(TERRAIN) $(VEC) $(WEB) $(STAC)/items $(STAC)/collections $(KSRIV_OUTDIR):
	$(call ensure_dir,$@)
