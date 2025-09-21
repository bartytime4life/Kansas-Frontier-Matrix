# --------------------------------------------------------------------
# Kansas Frontier Matrix / Kansas Geo Timeline — Makefile (connected)
# --------------------------------------------------------------------
# - Backward compatible: fetch, cogs, terrain, kml, site, clean
# - Wires to existing scripts: fetch.py, make_cog.py, make_hillshade.py,
#   write_meta.py, make_stac.py, validate_sources.py, validate_stac.py
# - Robust terrain derivation: hillshade (script or gdaldem), slope, aspect
# - Optional vectorization (slope classes, aspect sectors)
# - Optional meta checksum update via write_meta.py (or sha256 fallback)
# - Safe fallbacks if helper scripts are missing
# - Extras: STAC build/validate targets; rsync mirroring when available
# --------------------------------------------------------------------

SHELL := /bin/bash
.ONESHELL:

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
DERIV   := $(DATA)/derivatives            # legacy path for site/kml
VEC     := $(DATA)/processed/vectors
WEB     := web
STAC    := $(DATA)/stac

# Core DEM (adjust if your DEM filename differs)
DEM := $(DEMS)/ks_1m_dem_2018_2020.tif

# Outputs (COGs)
HILLSHADE := $(HILLS)/ks_hillshade_2018_2020.tif
SLOPE     := $(TERRAIN)/ks_slope_deg.tif
ASPECT    := $(TERRAIN)/ks_aspect_deg.tif

# Optional vectors
SLOPE_CLASSES   := $(VEC)/slope_classes.geojson
ASPECT_SECTORS  := $(VEC)/aspect_sectors.geojson

# Optional meta files you maintain (if present)
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

# Detect helper scripts that exist in this repo
HAVE_FETCH           := $(wildcard $(S)/fetch.py)
HAVE_MAKECOG         := $(wildcard $(S)/make_cog.py)
HAVE_MAKEHILLSHADE   := $(wildcard $(S)/make_hillshade.py)
HAVE_WRITEMETA       := $(wildcard $(S)/write_meta.py)
HAVE_MAKE_STAC       := $(wildcard $(S)/make_stac.py)
HAVE_VALIDATE_STAC   := $(wildcard $(S)/validate_stac.py)
HAVE_VALIDATE_SOURCES:= $(wildcard $(S)/validate_sources.py)

# -------- Internal helpers --------
define check_dem
	@if [ ! -f "$(DEM)" ]; then \
	  echo "ERROR: DEM not found at '$(DEM)'"; \
	  echo "       Make sure your DEM COG exists (see README) or adjust DEM path in Makefile."; \
	  exit 1; \
	fi
endef

define check_gdal
	@if [ "$(HAVE_GDALDEM)" != "yes" ]; then \
	  echo "ERROR: 'gdaldem' not found in PATH."; \
	  echo "       On Ubuntu/Debian: sudo apt-get update && sudo apt-get install -y gdal-bin"; \
	  exit 1; \
	fi
endef

define mirror_derivatives
	@mkdir -p "$(DERIV)"
	@if [ -f "$(1)" ]; then \
	  if [ "$(HAVE_RSYNC)" = "yes" ]; then \
	    rsync -a --checksum "$(1)" "$(2)"; \
	  else \
	    cp -f "$(1)" "$(2)"; \
	  fi \
	fi
endef

# -------- Help --------
.PHONY: help
help:
	@echo ""
	@echo "Targets:"
	@echo "  fetch            Download rasters/vectors per data/sources/*.json (ArcGIS/USGS/etc.)"
	@echo "  cogs             Build Cloud-Optimized GeoTIFFs (COGs) with overviews"
	@echo "  terrain          Derive hillshade/slope/aspect (COGs); mirror into data/derivatives"
	@echo "  slope_classes    Optional: vectorize slope classes (0–2,2–5,5–10,10–20,20–30,30–45,45+)"
	@echo "  aspect_sectors   Optional: vectorize 8-way aspect sectors (N,NE,E,SE,S,SW,W,NW)"
	@echo "  meta             Optional: update terrain meta JSON checksums (slope/aspect)"
	@echo "  stac             Build STAC items/collections (if make_stac.py present)"
	@echo "  stac-validate    Validate STAC + source schemas"
	@echo "  kml              Build KMZ overlays (legacy; requires your own regionate scripts)"
	@echo "  site             Write web/layers.json to preview hillshade/slope/aspect"
	@echo "  clean            Remove generated outputs"
	@echo ""

# -------- Fetch --------
.PHONY: fetch
fetch:
ifndef HAVE_FETCH
	@echo "[fetch] No $(S)/fetch.py found. Skipping."
else
	@mkdir -p $(RAW)
	$(PY) $(S)/fetch.py --sources $(SRC) --out $(RAW)
endif

# -------- COGS --------
.PHONY: cogs
cogs:
ifndef HAVE_MAKECOG
	@echo "[cogs] No $(S)/make_cog.py found. Skipping."
else
	@mkdir -p $(COGS)
	$(PY) $(S)/make_cog.py --in $(RAW) --out $(COGS)
endif

# -------- Terrain (COGs) --------
.PHONY: terrain
terrain: $(HILLSHADE) $(SLOPE) $(ASPECT)
	$(call mirror_derivatives,$(HILLSHADE),$(DERIV)/hillshade.tif)
	$(call mirror_derivatives,$(SLOPE),$(DERIV)/slope.tif)
	$(call mirror_derivatives,$(ASPECT),$(DERIV)/aspect.tif)
	@echo "✓ terrain built (COGs) and mirrored into $(DERIV)"

# Hillshade COG (use your script if available; else gdaldem)
$(HILLSHADE): $(DEM)
	$(check_dem)
	@mkdir -p $(HILLS)
	@if [ -f "$(S)/make_hillshade.py" ]; then \
	  echo "[hillshade] using $(S)/make_hillshade.py"; \
	  $(PY) $(S)/make_hillshade.py --dem $(DEM) --out $(HILLSHADE) --cog; \
	else \
	  if [ "$(HAVE_GDALDEM)" = "yes" ]; then \
	    echo "[hillshade] gdaldem hillshade"; \
	    gdaldem hillshade $(DEM) $(HILLSHADE) -compute_edges -z 1.0 -az 315 -alt 45; \
	    gdaladdo -r average $(HILLSHADE) 2 4 8 16; \
	    gdal_translate $(HILLSHADE) $(HILLSHADE) $(COG_OPTS); \
	  else \
	    echo "ERROR: neither $(S)/make_hillshade.py nor gdaldem available."; exit 1; \
	  fi; \
	fi

# Slope COG (gdaldem)
$(SLOPE): $(DEM)
	$(check_dem)
	@mkdir -p $(TERRAIN)
	@if [ "$(HAVE_GDALDEM)" = "yes" ]; then \
	  echo "[slope] gdaldem slope (degrees)"; \
	  gdaldem slope $(DEM) $(SLOPE) -compute_edges -s 1.0; \
	  gdaladdo -r average $(SLOPE) 2 4 8 16; \
	  gdal_translate $(SLOPE) $(SLOPE) $(COG_OPTS); \
	else \
	  echo "ERROR: gdaldem required for slope."; exit 1; \
	fi

# Aspect COG (gdaldem)
$(ASPECT): $(DEM)
	$(check_dem)
	@mkdir -p $(TERRAIN)
	@if [ "$(HAVE_GDALDEM)" = "yes" ]; then \
	  echo "[aspect] gdaldem aspect (0–360°)"; \
	  gdaldem aspect $(DEM) $(ASPECT) -compute_edges; \
	  gdaladdo -r average $(ASPECT) 2 4 8 16; \
	  gdal_translate $(ASPECT) $(ASPECT) $(COG_OPTS); \
	else \
	  echo "ERROR: gdaldem required for aspect."; exit 1; \
	fi

# -------- Optional vectors --------
.PHONY: slope_classes
slope_classes: $(SLOPE)
	@mkdir -p $(VEC)
	@if [ "$(HAVE_GDAL_CALC)" = "yes" ] && [ "$(HAVE_GDAL_POLY)" = "yes" ]; then \
	  echo "[slope_classes] binning slope → polygons"; \
	  gdal_calc.py -A $(SLOPE) --NoDataValue=0 \
	    --calc="(A>=0)*(A<2)*1 + (A>=2)*(A<5)*2 + (A>=5)*(A<10)*3 + (A>=10)*(A<20)*4 + (A>=20)*(A<30)*5 + (A>=30)*(A<45)*6 + (A>=45)*7" \
	    --outfile=/tmp/_slope_classes.tif --type=Byte $(COG_OPTS); \
	  gdal_polygonize.py /tmp/_slope_classes.tif -f GeoJSON $(SLOPE_CLASSES); \
	  rm -f /tmp/_slope_classes.tif; \
	else \
	  echo "[slope_classes] GDAL calc/polygonize not available. Skipping."; \
	fi

.PHONY: aspect_sectors
aspect_sectors: $(ASPECT)
	@mkdir -p $(VEC)
	@if [ "$(HAVE_GDAL_CALC)" = "yes" ] && [ "$(HAVE_GDAL_POLY)" = "yes" ]; then \
	  echo "[aspect_sectors] binning 8-way aspect → polygons"; \
	  gdal_calc.py -A $(ASPECT) --NoDataValue=0 \
	    --calc="(A<22.5)*(A>=0)*1 + (A>=22.5)*(A<67.5)*2 + (A>=67.5)*(A<112.5)*3 + (A>=112.5)*(A<157.5)*4 + (A>=157.5)*(A<202.5)*5 + (A>=202.5)*(A<247.5)*6 + (A>=247.5)*(A<292.5)*7 + (A>=292.5)*(A<337.5)*8 + (A>=337.5)*1" \
	    --outfile=/tmp/_aspect_sectors.tif --type=Byte $(COG_OPTS); \
	  gdal_polygonize.py /tmp/_aspect_sectors.tif -f GeoJSON $(ASPECT_SECTORS); \
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
	      SUM_DEM=$$($(SHA256) $(SHA256FLAGS) $(DEM) | awk '{print $$1}'); \
	      SUM_SLOPE=$$($(SHA256) $(SHA256FLAGS) $(SLOPE) | awk '{print $$1}'); \
	      $(PY) - <<'PYCODE' $(META_SLOPE) $$SUM_DEM $$SUM_SLOPE
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
	      SUM_DEM=$$($(SHA256) $(SHA256FLAGS) $(DEM) | awk '{print $$1}'); \
	      SUM_ASPECT=$$($(SHA256) $(SHA256FLAGS) $(ASPECT) | awk '{print $$1}'); \
	      $(PY) - <<'PYCODE' $(META_ASPECT) $$SUM_DEM $$SUM_ASPECT
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
ifndef HAVE_MAKE_STAC
	@echo "[stac] No $(S)/make_stac.py found. Skipping."
else
	@mkdir -p $(STAC)/items $(STAC)/collections
	$(PY) $(S)/make_stac.py --data $(DATA) --stac $(STAC)
endif

.PHONY: stac-validate
stac-validate:
	@if [ -f "$(S)/validate_sources.py" ]; then \
	  $(PY) $(S)/validate_sources.py --sources $(SRC); \
	else \
	  echo "[stac-validate] $(S)/validate_sources.py missing (source schema check skipped)."; \
	fi
	@if [ -f "$(S)/validate_stac.py" ]; then \
	  $(PY) $(S)/validate_stac.py --stac $(STAC); \
	else \
	  echo "[stac-validate] $(S)/validate_stac.py missing (STAC validation skipped)."; \
	fi

# -------- KML / KMZ (legacy demo) --------
.PHONY: kml
kml: terrain
	@echo "[kml] Legacy prototype. Provide your own regionate script if needed."

.PHONY: site
site:
	@mkdir -p $(WEB)
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
	rm -rf $(RAW) $(COGS) $(DERIV) $(DATA)/kml $(DATA)/*.kmz
	@echo "✓ cleaned generated outputs."
