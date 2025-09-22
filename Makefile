# --------------------------------------------------------------------
# Kansas Frontier Matrix / Kansas Geo Timeline — Makefile (connected+safe)
# --------------------------------------------------------------------
# - Same interface: fetch, cogs, terrain, kml, site, clean (+ stac, stac-validate)
# - Wires to scripts: fetch.py, make_cog.py, make_hillshade.py,
#   write_meta.py, make_stac.py, validate_sources.py, validate_stac.py
# - GDAL fallbacks for hillshade/slope/aspect
# - Optional vectorization + meta checksum updates
# - Hardened shell, overridable DEM, parallel-safe mkdir
# - Repo-aware STAC path: stac/ (not data/stac/)
# --------------------------------------------------------------------

SHELL := /bin/bash
.SHELLFLAGS := -euo pipefail -c
.ONESHELL:
.DEFAULT_GOAL := help

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
STAC    := stac                   # <-- fixed from data/stac

# Core DEM (can be overridden: `make terrain DEM=.../dem.tif`)
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

# -------- Tools & flags --------
COG_OPTS := -co TILED=YES -co COMPRESS=DEFLATE -co PREDICTOR=2 -co BIGTIFF=IF_SAFER
SHA256   := $(shell (command -v sha256sum || command -v shasum) 2>/dev/null)
SHA256FLAGS := $(shell if command -v sha256sum >/dev/null 2>&1; then echo ""; else echo "-a 256"; fi)
HAVE_GDALDEM    := $(shell command -v gdaldem >/dev/null 2>&1 && echo yes || echo no)
HAVE_GDAL_POLY  := $(shell command -v gdal_polygonize.py >/dev/null 2>&1 && echo yes || echo no)
HAVE_GDAL_CALC  := $(shell command -v gdal_calc.py >/dev/null 2>&1 && echo yes || echo no)
HAVE_RSYNC      := $(shell command -v rsync >/dev/null 2>&1 && echo yes || echo no)
HAVE_KGT        := $(shell command -v kgt >/dev/null 2>&1 && echo yes || echo no)

# Detect helper scripts that exist in this repo
HAVE_FETCH            := $(wildcard $(S)/fetch.py)
HAVE_MAKECOG          := $(wildcard $(S)/make_cog.py)
HAVE_MAKEHILLSHADE    := $(wildcard $(S)/make_hillshade.py)
HAVE_WRITEMETA        := $(wildcard $(S)/write_meta.py)
HAVE_MAKE_STAC        := $(wildcard $(S)/make_stac.py)
HAVE_VALIDATE_STAC    := $(wildcard $(S)/validate_stac.py)
HAVE_VALIDATE_SOURCES := $(wildcard $(S)/validate_sources.py)

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
	  if [ "$(HAVE_RSYNC)" = "yes" ]; then \
	    rsync -a --checksum "$(1)" "$(2)"; \
	  else \
	    cp -f "$(1)" "$(2)"; \
	  fi \
	fi
endef

# -------- Help --------
.PHONY: help env prebuild
help:
	@echo ""
	@echo "Targets:"
	@echo "  env              Show detected tools/paths"
	@echo "  fetch            Download rasters/vectors per data/sources/*.json"
	@echo "  cogs             Build Cloud-Optimized GeoTIFFs (COGs) with overviews"
	@echo "  terrain          Derive hillshade/slope/aspect (COGs); mirror into data/derivatives"
	@echo "  slope_classes    Optional: vectorize slope classes (0–2,2–5,5–10,10–20,20–30,30–45,45+)"
	@echo "  aspect_sectors   Optional: vectorize 8-way aspect sectors (N,NE,E,SE,S,SW,W,NW)"
	@echo "  meta             Optional: update terrain meta JSON checksums (slope/aspect)"
	@echo "  stac             Build STAC items/collections into ./stac/"
	@echo "  stac-validate    Validate STAC + source schemas (uses scripts/ or kgt)"
	@echo "  site             Write web/layers.json (simple preview)"
	@echo "  site-config      Render web/app.config.json from STAC via kgt (if available)"
	@echo "  kml              Build KMZ overlays (placeholder)"
	@echo "  clean            Remove generated raster outputs (keeps stac/)"
	@echo ""
	@echo "Overrides:"
	@echo "  make terrain DEM=/path/to/dem.tif"
	@echo ""

env:
	@echo "PY=$(PY)"
	@echo "DEM=$(DEM)"
	@echo "STAC_DIR=$(STAC)"
	@echo "HAVE_KGT=$(HAVE_KGT)"
	@echo "HAVE_GDALDEM=$(HAVE_GDALDEM) HAVE_GDAL_CALC=$(HAVE_GDAL_CALC) HAVE_GDAL_POLY=$(HAVE_GDAL_POLY)"
	@echo "HAVE_FETCH=$(if $(HAVE_FETCH),yes,no) HAVE_MAKECOG=$(if $(HAVE_MAKECOG),yes,no) HAVE_MAKEHILLSHADE=$(if $(HAVE_MAKEHILLSHADE),yes,no)"
	@echo "HAVE_MAKE_STAC=$(if $(HAVE_MAKE_STAC),yes,no) HAVE_VALIDATE_STAC=$(if $(HAVE_VALIDATE_STAC),yes,no) HAVE_VALIDATE_SOURCES=$(if $(HAVE_VALIDATE_SOURCES),yes,no)"

# CI convenience: validate + build minimal site
prebuild: stac-validate site
	@echo ">> Prebuild complete."

# -------- Fetch --------
.PHONY: fetch
fetch:
ifeq ($(strip $(HAVE_FETCH)),)
	@echo "[fetch] No $(S)/fetch.py found. Skipping."
else
	$(call ensure_dir,$(RAW))
	$(PY) $(S)/fetch.py --sources $(SRC) --out $(RAW)
endif

# -------- COGS --------
.PHONY: cogs
cogs:
ifeq ($(strip $(HAVE_MAKECOG)),)
	@echo "[cogs] No $(S)/make_cog.py found. Skipping."
else
	$(call ensure_dir,$(COGS))
	$(PY) $(S)/make_cog.py --in $(RAW) --out $(COGS)
endif

# -------- Terrain (COGs) --------
.PHONY: terrain
terrain: $(HILLSHADE) $(SLOPE) $(ASPECT)
	$(call mirror_derivatives,$(HILLSHADE),$(DERIV)/hillshade.tif)
	$(call mirror_derivatives,$(SLOPE),$(DERIV)/slope.tif)
	$(call mirror_derivatives,$(ASPECT),$(DERIV)/aspect.tif)
	@echo "✓ terrain built (COGs) and mirrored into $(DERIV)"

# Hillshade COG (script or gdaldem)
$(HILLSHADE): $(DEM)
	$(check_dem)
	$(call ensure_dir,$(HILLS))
	@if [ -f "$(S)/make_hillshade.py" ]; then \
	  echo "[hillshade] $(S)/make_hillshade.py"; \
	  $(PY) $(S)/make_hillshade.py --dem $(DEM) --out $(HILLSHADE) --cog; \
	else \
	  if [ "$(HAVE_GDALDEM)" = "yes" ]; then \
	    echo "[hillshade] gdaldem hillshade"; \
	    gdaldem hillshade "$(DEM)" "$(HILLSHADE)" -compute_edges -z 1.0 -az 315 -alt 45; \
	    gdaladdo -r average "$(HILLSHADE)" 2 4 8 16; \
	    gdal_translate "$(HILLSHADE)" "$(HILLSHADE)" $(COG_OPTS); \
	  else \
	    echo "ERROR: neither $(S)/make_hillshade.py nor gdaldem available."; exit 1; \
	  fi; \
	fi

# Slope COG (gdaldem)
$(SLOPE): $(DEM)
	$(check_dem)
	$(call ensure_dir,$(TERRAIN))
	@if [ "$(HAVE_GDALDEM)" = "yes" ]; then \
	  echo "[slope] gdaldem slope (degrees)"; \
	  gdaldem slope "$(DEM)" "$(SLOPE)" -compute_edges -s 1.0; \
	  gdaladdo -r average "$(SLOPE)" 2 4 8 16; \
	  gdal_translate "$(SLOPE)" "$(SLOPE)" $(COG_OPTS); \
	else \
	  echo "ERROR: gdaldem required for slope."; exit 1; \
	fi

# Aspect COG (gdaldem)
$(ASPECT): $(DEM)
	$(check_dem)
	$(call ensure_dir,$(TERRAIN))
	@if [ "$(HAVE_GDALDEM)" = "yes" ]; then \
	  echo "[aspect] gdaldem aspect (0–360°)"; \
	  gdaldem aspect "$(DEM)" "$(ASPECT)" -compute_edges; \
	  gdaladdo -r average "$(ASPECT)" 2 4 8 16; \
	  gdal_translate "$(ASPECT)" "$(ASPECT)" $(COG_OPTS); \
	else \
	  echo "ERROR: gdaldem required for aspect."; exit 1; \
	fi

# -------- Optional vectors --------
.PHONY: slope_classes
slope_classes: $(SLOPE)
	$(call ensure_dir,$(VEC))
	@if [ "$(HAVE_GDAL_CALC)" = "yes" ] && [ "$(HAVE_GDAL_POLY)" = "yes" ]; then \
	  echo "[slope_classes] binning slope → polygons"; \
	  gdal_calc.py -A "$(SLOPE)" --NoDataValue=0 \
	    --calc="(A>=0)*(A<2)*1 + (A>=2)*(A<5)*2 + (A>=5)*(A<10)*3 + (A>=10)*(A<20)*4 + (A>=20)*(A<30)*5 + (A>=30)*(A<45)*6 + (A>=45)*7" \
	    --outfile=/tmp/_slope_classes.tif --type=Byte $(COG_OPTS); \
	  gdal_polygonize.py /tmp/_slope_classes.tif -f GeoJSON "$(SLOPE_CLASSES)"; \
	  rm -f /tmp/_slope_classes.tif; \
	else \
	  echo "[slope_classes] GDAL calc/polygonize not available. Skipping."; \
	fi

.PHONY: aspect_sectors
aspect_sectors: $(ASPECT)
	$(call ensure_dir,$(VEC))
	@if [ "$(HAVE_GDAL_CALC)" = "yes" ] && [ "$(HAVE_GDAL_POLY)" = "yes" ]; then \
	  echo "[aspect_sectors] binning 8-way aspect → polygons"; \
	  gdal_calc.py -A "$(ASPECT)" --NoDataValue=0 \
	    --calc="(A<22.5)*(A>=0)*1 + (A>=22.5)*(A<67.5)*2 + (A>=67.5)*(A<112.5)*3 + (A>=112.5)*(A<157.5)*4 + (A>=157.5)*(A<202.5)*5 + (A>=202.5)*(A<247.5)*6 + (A>=247.5)*(A<292.5)*7 + (A>=292.5)*(A<337.5)*8 + (A>=337.5)*1" \
	    --outfile=/tmp/_aspect_sectors.tif --type=Byte $(COG_OPTS); \
	  gdal_polygonize.py /tmp/_aspect_sectors.tif -f GeoJSON "$(ASPECT_SECTORS)"; \
	  rm -f /tmp/_aspect_sectors.tif; \
	else \
	  echo "[aspect_sectors] GDAL calc/polygonize not available. Skipping."; \
	fi

# -------- Meta checksums (optional) --------
.PHONY: meta
meta: $(SLOPE) $(ASPECT)
	@if [ -f "$(META_SLOPE)" ] || [ -f "$(META_ASPECT)" ]; then \
	  if [ -n "$(SHA256)" ]; then \
	    echo "[meta] updating simple checksums (sha256)"; \
	    if [ -f "$(META_SLOPE)" ]; then \
	      SUM_DEM=$$($(SHA256) $(SHA256FLAGS) "$(DEM)" | awk '{print $$1}'); \
	      SUM_SLOPE=$$($(SHA256) $(SHA256FLAGS) "$(SLOPE)" | awk '{print $$1}'); \
	      $(PY) - <<'PYCODE' "$(META_SLOPE)" "$$SUM_DEM" "$$SUM_SLOPE"
import json, sys
p, dem, slope = sys.argv[1:]
d=json.load(open(p))
d.setdefault("inputs",{}).setdefault("dem_cog",{})["checksum"]=dem
d.setdefault("outputs",{}).setdefault("slope_cog",{})["checksum"]=slope
json.dump(d, open(p,'w'), indent=2)
print("updated", p)
PYCODE \
	    ; fi; \
	    if [ -f "$(META_ASPECT)" ]; then \
	      SUM_DEM=$$($(SHA256) $(SHA256FLAGS) "$(DEM)" | awk '{print $$1}'); \
	      SUM_ASPECT=$$($(SHA256) $(SHA256FLAGS) "$(ASPECT)" | awk '{print $$1}'); \
	      $(PY) - <<'PYCODE' "$(META_ASPECT)" "$$SUM_DEM" "$$SUM_ASPECT"
import json, sys
p, dem, aspect = sys.argv[1:]
d=json.load(open(p))
d.setdefault("inputs",{}).setdefault("dem_cog",{})["checksum"]=dem
d.setdefault("outputs",{}).setdefault("aspect_cog",{})["checksum"]=aspect
json.dump(d, open(p,'w'), indent=2)
print("updated", p)
PYCODE \
	    ; fi; \
	  else \
	    echo "[meta] sha256 tool not found. Skipping."; \
	  fi; \
	else \
	  echo "[meta] no META_* json files found. Skipping."; \
	fi

# -------- STAC build / validate --------
.PHONY: stac
stac:
ifeq ($(strip $(HAVE_MAKE_STAC)),)
	@echo "[stac] No $(S)/make_stac.py found. Skipping."
else
	$(call ensure_dir,$(STAC)/items)
	$(call ensure_dir,$(STAC)/collections)
	$(PY) $(S)/make_stac.py --data "$(DATA)" --stac "$(STAC)"
endif

.PHONY: stac-validate
stac-validate:
	@if [ -f "$(S)/validate_sources.py" ]; then \
	  $(PY) $(S)/validate_sources.py --sources "$(SRC)"; \
	else \
	  echo "[stac-validate] $(S)/validate_sources.py missing (source schema check skipped)."; \
	fi
	@if [ -f "$(S)/validate_stac.py" ]; then \
	  $(PY) $(S)/validate_stac.py --stac "$(STAC)"; \
	elif [ "$(HAVE_KGT)" = "yes" ]; then \
	  echo "[stac-validate] scripts missing; using kgt validate-stac as fallback"; \
	  kgt validate-stac "$(STAC)/items" --no-strict; \
	else \
	  echo "[stac-validate] No validators found (install kgt or add scripts/validate_stac.py)."; \
	fi

# -------- Web viewer config (optional, via kgt) --------
.PHONY: site-config
site-config:
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
.PHONY: kml
kml: terrain
	@echo "[kml] Legacy prototype. Provide your regionate script if needed."

# -------- Simple site manifest (always available) --------
.PHONY: site
site:
	$(call ensure_dir,$(WEB))
	@$(PY) - <<'PYCODE'
import json, pathlib
p = pathlib.Path('web/layers.json')
p.parent.mkdir(parents=True, exist_ok=True)
layers = {
  "layers": [
    {"id": "hillshade", "title": "Hillshade", "type": "raster", "path": "../data/derivatives/hillshade.tif"},
    {"id": "slope",     "title": "Slope (deg)", "type": "raster", "path": "../data/derivatives/slope.tif"},
    {"id": "aspect",    "title": "Aspect (deg)", "type": "raster", "path": "../data/derivatives/aspect.tif"}
  ]
}
json.dump(layers, open(p, 'w'), indent=2)
print("wrote", p)
PYCODE

# -------- Clean --------
.PHONY: clean
clean:
	rm -rf "$(RAW)" "$(COGS)" "$(DERIV)" "$(DATA)/kml" "$(DATA)"/*.kmz
	@echo "✓ cleaned generated raster outputs (kept ./stac)."
