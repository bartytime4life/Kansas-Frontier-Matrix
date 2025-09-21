# --------------------------------------------------------------------
# Kansas Frontier Matrix / Kansas Geo Timeline — Makefile (upgraded)
# --------------------------------------------------------------------
# - Backward compatible with original targets (fetch, cogs, terrain, kml, site, clean)
# - Robust terrain derivation: hillshade, slope, aspect -> COGs + optional vector generalizations
# - Optional meta checksum update (Linux/macOS)
# - Safe fallbacks if Python helper scripts are missing
#
# Layout conventions (analysis rasters kept near source DEMs):
#   data/cogs/dem/ks_1m_dem_2018_2020.tif   # input COG DEM (statewide)
#   data/cogs/hillshade/ks_hillshade_2018_2020.tif
#   data/cogs/terrain/ks_slope_deg.tif
#   data/cogs/terrain/ks_aspect_deg.tif
#   data/processed/vectors/slope_classes.geojson
#   data/processed/vectors/aspect_sectors.geojson
#
# Legacy compatibility:
#   - we mirror hillshade/slope/aspect into data/derivatives/* for old site/kml targets
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
DERIV   := $(DATA)/derivatives     # legacy path for site/kml
VEC     := $(DATA)/processed/vectors
WEB     := web

# Core DEM (adjust if your DEM filename differs)
DEM := $(DEMS)/ks_1m_dem_2018_2020.tif

# Outputs (COGs)
HILLSHADE := $(HILLS)/ks_hillshade_2018_2020.tif
SLOPE     := $(TERRAIN)/ks_slope_deg.tif
ASPECT    := $(TERRAIN)/ks_aspect_deg.tif

# Optional vectors
SLOPE_CLASSES   := $(VEC)/slope_classes.geojson
ASPECT_SECTORS  := $(VEC)/aspect_sectors.geojson

# Meta files (optional; created by you earlier)
META_SLOPE  := $(SRC)/ks_slope.meta.json
META_ASPECT := $(SRC)/ks_aspect.meta.json

# -------- Tools & flags --------
COG_OPTS := -co TILED=YES -co COMPRESS=DEFLATE -co PREDICTOR=2 -co BIGTIFF=IF_SAFER
SHA256   := $(shell (command -v sha256sum || command -v shasum) 2>/dev/null)
SHA256FLAGS := $(shell if command -v sha256sum >/dev/null 2>&1; then echo ""; else echo "-a 256"; fi)

# Detect if helper scripts exist
HAVE_FETCH      := $(wildcard $(S)/fetch_arcgis.py)
HAVE_MAKECOGS   := $(wildcard $(S)/make_cogs.py)
HAVE_DERIVETERR := $(wildcard $(S)/derive_terrain.py)
HAVE_REGIONATE  := $(wildcard $(S)/regionate_kml.py)
HAVE_PACKKMZ    := $(wildcard $(S)/pack_kmz.py)
HAVE_UPDCHECK   := $(wildcard $(S)/update_checksums.py)

# -------- Help --------
.PHONY: help
help:
	@echo ""
	@echo "Targets:"
	@echo "  fetch           Download rasters/vectors per data/sources/*.json (ArcGIS/USGS)"
	@echo "  cogs            Build Cloud-Optimized GeoTIFFs (COGs) with overviews"
	@echo "  terrain         Derive hillshade/slope/aspect (COGs); mirror into data/derivatives for legacy site/kml"
	@echo "  slope_classes   Optional: vectorize slope classes (0–2,2–5,5–10,10–20,20–30,30–45,45+)"
	@echo "  aspect_sectors  Optional: vectorize 8-way aspect sectors (N,NE,E,SE,S,SW,W,NW)"
	@echo "  meta            Optional: update terrain meta JSON checksums (slope/aspect)"
	@echo "  kml             Build KMZ overlays (legacy prototype regionation)"
	@echo "  site            Write web/layers.json to preview hillshade (legacy demo)"
	@echo "  clean           Remove generated outputs"
	@echo ""

# -------- Fetch --------
.PHONY: fetch
fetch:
ifndef HAVE_FETCH
	@echo "[fetch] No $(S)/fetch_arcgis.py found. Skipping."
else
	$(PY) $(S)/fetch_arcgis.py --sources $(SRC) --out $(RAW)
endif

# -------- COGS --------
.PHONY: cogs
cogs:
ifndef HAVE_MAKECOGS
	@echo "[cogs] No $(S)/make_cogs.py found. Skipping."
else
	$(PY) $(S)/make_cogs.py --inp $(RAW) --out $(COGS)
endif

# -------- Terrain (COGs) --------
.PHONY: terrain
terrain: $(HILLSHADE) $(SLOPE) $(ASPECT)
	@mkdir -p $(DERIV)
	# Mirror into legacy derivatives for existing site/kml recipes
	@if [ -f "$(HILLSHADE)" ]; then cp -f "$(HILLSHADE)" "$(DERIV)/hillshade.tif"; fi
	@if [ -f "$(SLOPE)" ]; then cp -f "$(SLOPE)" "$(DERIV)/slope.tif"; fi
	@if [ -f "$(ASPECT)" ]; then cp -f "$(ASPECT)" "$(DERIV)/aspect.tif"; fi
	@echo "✓ terrain built (COGs) and mirrored into $(DERIV)"

# Hillshade COG
$(HILLSHADE): $(DEM)
	@mkdir -p $(HILLS)
	@if command -v gdaldem >/dev/null 2>&1; then \
	  echo "[hillshade] gdaldem hillshade"; \
	  gdaldem hillshade $(DEM) $(HILLSHADE) -compute_edges -z 1.0 -az 315 -alt 45; \
	  gdaladdo -r average $(HILLSHADE) 2 4 8 16; \
	  gdal_translate $(HILLSHADE) $(HILLSHADE) $(COG_OPTS); \
	else \
	  echo "[hillshade] gdaldem not found. Trying Python derive_terrain.py (if present)"; \
	  if [ -f "$(S)/derive_terrain.py" ]; then \
	    $(PY) $(S)/derive_terrain.py --dem $(COGS) --out $(DATA)/derivatives; \
	  else \
	    echo "ERROR: neither GDAL nor $(S)/derive_terrain.py available."; exit 1; \
	  fi; \
	fi

# Slope COG
$(SLOPE): $(DEM)
	@mkdir -p $(TERRAIN)
	@if command -v gdaldem >/dev/null 2>&1; then \
	  echo "[slope] gdaldem slope (degrees)"; \
	  gdaldem slope $(DEM) $(SLOPE) -compute_edges -s 1.0; \
	  gdaladdo -r average $(SLOPE) 2 4 8 16; \
	  gdal_translate $(SLOPE) $(SLOPE) $(COG_OPTS); \
	else \
	  echo "[slope] gdaldem not found. Trying Python derive_terrain.py (if present)"; \
	  if [ -f "$(S)/derive_terrain.py" ]; then \
	    $(PY) $(S)/derive_terrain.py --dem $(COGS) --out $(DATA)/derivatives; \
	  else \
	    echo "ERROR: neither GDAL nor $(S)/derive_terrain.py available."; exit 1; \
	  fi; \
	fi

# Aspect COG
$(ASPECT): $(DEM)
	@mkdir -p $(TERRAIN)
	@if command -v gdaldem >/dev/null 2>&1; then \
	  echo "[aspect] gdaldem aspect (0–360°)"; \
	  gdaldem aspect $(DEM) $(ASPECT) -compute_edges; \
	  gdaladdo -r average $(ASPECT) 2 4 8 16; \
	  gdal_translate $(ASPECT) $(ASPECT) $(COG_OPTS); \
	else \
	  echo "[aspect] gdaldem not found. Trying Python derive_terrain.py (if present)"; \
	  if [ -f "$(S)/derive_terrain.py" ]; then \
	    $(PY) $(S)/derive_terrain.py --dem $(COGS) --out $(DATA)/derivatives; \
	  else \
	    echo "ERROR: neither GDAL nor $(S)/derive_terrain.py available."; exit 1; \
	  fi; \
	fi

# -------- Optional vectors --------
.PHONY: slope_classes
slope_classes: $(SLOPE)
	@mkdir -p $(VEC)
	@if command -v gdal_calc.py >/dev/null 2>&1; then \
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
	@if command -v gdal_calc.py >/dev/null 2>&1; then \
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
ifndef HAVE_UPDCHECK
	@echo "[meta] $(S)/update_checksums.py not found. Skipping checksum update."
else
	@if [ -f "$(META_SLOPE)" ]; then \
	  $(PY) $(S)/update_checksums.py \
	    --meta $(META_SLOPE) \
	    --set inputs.dem_cog.checksum=$$($(SHA256) $(SHA256FLAGS) $(DEM) | awk '{print $$1}') \
	    --set outputs.slope_cog.checksum=$$($(SHA256) $(SHA256FLAGS) $(SLOPE) | awk '{print $$1}') \
	    $(if $(wildcard $(SLOPE_CLASSES)),--set outputs.slope_classes.checksum=$$($(SHA256) $(SHA256FLAGS) $(SLOPE_CLASSES) | awk '{print $$1}'),) ; \
	fi
	@if [ -f "$(META_ASPECT)" ]; then \
	  $(PY) $(S)/update_checksums.py \
	    --meta $(META_ASPECT) \
	    --set inputs.dem_cog.checksum=$$($(SHA256) $(SHA256FLAGS) $(DEM) | awk '{print $$1}') \
	    --set outputs.aspect_cog.checksum=$$($(SHA256) $(SHA256FLAGS) $(ASPECT) | awk '{print $$1}') \
	    $(if $(wildcard $(ASPECT_SECTORS)),--set outputs.aspect_sectors.checksum=$$($(SHA256) $(SHA256FLAGS) $(ASPECT_SECTORS) | awk '{print $$1}'),) ; \
	fi
endif

# -------- KML / KMZ (legacy demo) --------
.PHONY: kml
kml: terrain
ifndef HAVE_REGIONATE
	@echo "[kml] No $(S)/regionate_kml.py found. Skipping."
else
	$(PY) $(S)/regionate_kml.py --inp $(DERIV) --out $(DATA)/kml --kmz kansas_elevation.kmz
endif

.PHONY: site
site:
ifndef HAVE_PACKKMZ
	@echo "[site] No $(S)/pack_kmz.py found. Writing minimal web/layers.json only."
else
	$(PY) $(S)/pack_kmz.py --kml $(DATA)/kml --out $(DATA)
endif
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
PYCODE
	@echo "✓ web/layers.json written."

# -------- Clean --------
.PHONY: clean
clean:
	rm -rf $(RAW) $(COGS) $(DERIV) $(DATA)/kml $(DATA)/*.kmz
	@echo "✓ cleaned generated outputs."
