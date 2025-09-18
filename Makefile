# --------------------------------------------------------------------
# Kansas Geo Timeline — Makefile
# --------------------------------------------------------------------
PY := python
S := scripts
DATA := data
SRC := $(DATA)/sources
WEB := web

.PHONY: help fetch cogs terrain kml site clean

help:
	@echo "Targets:"
	@echo "  fetch    - Download rasters/vectors from ArcGIS/USGS per data/sources/*.json"
	@echo "  cogs     - Convert GeoTIFFs to Cloud-Optimized GeoTIFFs (COGs) with overviews"
	@echo "  terrain  - Derive hillshade/slope/aspect from DEM COGs"
	@echo "  kml      - Build simple KMZ overlays from rasters (prototype regionation)"
	@echo "  site     - Generate web/layers.json from catalog and ensure index.html ready"
	@echo "  clean    - Remove generated outputs"

fetch:
	$(PY) $(S)/fetch_arcgis.py --sources $(SRC) --out $(DATA)/raw

cogs:
	$(PY) $(S)/make_cogs.py --inp $(DATA)/raw --out $(DATA)/cogs

terrain:
	$(PY) $(S)/derive_terrain.py --dem $(DATA)/cogs --out $(DATA)/derivatives

kml:
	$(PY) $(S)/regionate_kml.py --inp $(DATA)/derivatives --out $(DATA)/kml --kmz kansas_elevation.kmz

site:
	$(PY) $(S)/pack_kmz.py --kml $(DATA)/kml --out $(DATA)
	$(PY) -c "import json, pathlib; p=pathlib.Path('web/layers.json'); p.parent.mkdir(parents=True, exist_ok=True); json.dump({'layers':[{'id':'hillshade','title':'Hillshade','type':'raster','path':'../data/derivatives/hillshade.tif'}]}, open(p,'w'))"

clean:
	rm -rf $(DATA)/raw $(DATA)/cogs $(DATA)/derivatives $(DATA)/kml $(DATA)/*.kmz
