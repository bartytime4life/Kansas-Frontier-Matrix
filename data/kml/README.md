<div align="center">

# 🌐 Kansas Geo Timeline — KML / KMZ Exports

**Google Earth–ready exports** of rasters and vectors from the  
**Kansas Frontier Matrix / Kansas Geo Timeline** project.  

Includes:
- Regionated **KML/KMZ super-overlays** for large rasters (DEM hillshade, georeferenced historic topos).  
- Lightweight **KMLs** for vectors (treaties, railroads, trails, floodplains).  
- JSON sidecars (`*.meta.json`) for provenance and reproducibility (MCP-style).  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/.pre-commit-config.yaml)

</div>

---

```mermaid
flowchart TD
  A["Source rasters & vectors\n(data/cogs/**, data/processed/vectors/**)"] --> B["Export to KML/KMZ\n(gdal_translate · ogr2ogr)"]
  B --> C["KML/KMZ outputs\n(data/kml/**)"]
  C --> D["Meta JSON sidecars\n(*.meta.json)"]
  C --> E["STAC Items\n(stac/items/kml/**)"]
  E --> F["Validate\n(stac-validate)"]
  F --> G["Google Earth / Public delivery\n(KMZ <200 MB)"]

<!-- END OF MERMAID -->



⸻

🎯 Purpose
	•	Provide Google Earth–ready exports for educators, historians, and the public.
	•	Package large rasters as regionated KMZ super-overlays.
	•	Deliver vector layers as KML for lightweight use.
	•	Preserve provenance + reproducibility with .meta.json and STAC links.

⸻

📂 What belongs here
	•	*.kmz — regionated raster super-overlays.
	•	*.kml — vector exports (and very small rasters).
	•	*.meta.json — per-export metadata (who/when/how, inputs, checksums).
	•	README.md — this documentation.

❌ Raw/processed COGs or GeoJSON do not belong here.
They live under data/cogs/** and data/processed/**.
This directory is strictly for Earth viewer exports.

⸻

🧭 Conventions

CRS
	•	Google Earth requires EPSG:4326 (WGS84).
	•	Export tools will reproject automatically — always document source CRS in metadata.

Naming

<theme>_<region>_<year>.kmz

Examples:
	•	ks_hillshade_2018_2020.kmz
	•	usgs_topo_larned_1894.kmz
	•	treaties.kml
	•	railroads_1900.kml

Metadata (*.meta.json)

Each export should have a JSON sidecar:

{
  "id": "usgs_topo_larned_1894_kmz",
  "title": "USGS Topo – Larned (1894), KMZ Super-Overlay",
  "source_raster": "data/cogs/overlays/usgs_topo_larned_1894.tif",
  "export_tool": "gdal_translate -of KMLSUPEROVERLAY -co FORMAT=PNG",
  "processing": "Auto-regionated pyramid inside KMZ",
  "rms_georef_m": 8.6,
  "license": "Public Domain (USGS)",
  "created": "2025-09-19T20:30:00Z",
  "sha256": "<checksum>"
}


⸻

🛠️ How to generate

A) Raster → KMZ super-overlay

gdal_translate -of KMLSUPEROVERLAY -co FORMAT=PNG \
  data/cogs/hillshade/ks_hillshade_2018_2020.tif \
  data/kml/ks_hillshade_2018_2020.kmz

	•	PNG for transparency (hillshade, topo maps).
	•	JPEG for photo-like imagery (smaller KMZ).

B) Vector → KML

# Treaties (polygon)
ogr2ogr -f KML data/kml/treaties.kml data/processed/vectors/treaties.geojson \
  -dsco NameField=name -select id,name,year

# Railroads (circa 1900, line)
ogr2ogr -f KML data/kml/railroads_1900.kml data/processed/vectors/railroads_1900.geojson \
  -nlt PROMOTE_TO_MULTI -select id,name,year

C) Styled rasters (optional pre-step)

gdaldem color-relief \
  data/processed/dem/ks_1m_dem.tif \
  configs/colorramps/hillshade.txt \
  /tmp/ks_hillshade_rgba.tif

gdal_translate -of KMLSUPEROVERLAY -co FORMAT=PNG \
  /tmp/ks_hillshade_rgba.tif data/kml/ks_hillshade_2018_2020.kmz


⸻

🧰 Makefile integration

KML_DIR := data/kml

# Raster → KMZ
$(KML_DIR)/%.kmz: data/cogs/hillshade/%.tif
	@mkdir -p $(KML_DIR)
	gdal_translate -of KMLSUPEROVERLAY -co FORMAT=PNG $< $@

# Historic topo overlays
$(KML_DIR)/usgs_topo_%.kmz: data/cogs/overlays/usgs_topo_%.tif
	@mkdir -p $(KML_DIR)
	gdal_translate -of KMLSUPEROVERLAY -co FORMAT=PNG $< $@

# Vectors → KML
$(KML_DIR)/%.kml: data/processed/vectors/%.geojson
	@mkdir -p $(KML_DIR)
	ogr2ogr -f KML $@ $<

.PHONY: kml-all
kml-all: \
	$(KML_DIR)/ks_hillshade_2018_2020.kmz \
	$(KML_DIR)/treaties.kml \
	$(KML_DIR)/railroads_1900.kml


⸻

🔍 Quality & troubleshooting
	•	KMZ too large? → crop/downsample first (gdalwarp -te …).
	•	Blurry tiles? → export from highest-resolution source, avoid double pyramids.
	•	Transparency missing? → ensure alpha band / NODATA is set.
	•	Vector clutter? → simplify + trim attributes (ogr2ogr -simplify 0.0005).
	•	Wrong names? → use -dsco NameField=<field> in ogr2ogr.

⸻

✅ Checklist before committing
	•	Opens cleanly in Google Earth Pro.
	•	Reasonable size (prefer KMZ < 200 MB).
	•	.meta.json sidecar present (provenance, inputs, checksums).
	•	Human-readable title + description.
	•	Linked to STAC in stac/items/kml/.

⸻

📚 Examples
	•	ks_hillshade_2018_2020.kmz — DEM hillshade super-overlay.
	•	usgs_topo_larned_1894.kmz — georeferenced topo.
	•	treaties.kml — polygon treaty/reservation boundaries.
	•	railroads_1900.kml — 1900-era railroads.

⸻

🔗 See also
	•	data/cogs/ — source rasters for exports.
	•	data/processed/vectors/ — source vectors for exports.
	•	data/stac/ — STAC metadata + provenance.
	•	docs/ — MCP reproducibility templates & methods.

⸻

✅ Mission-grade principle: KML/KMZ exports must be lightweight, reproducible, and STAC-linked.
If it doesn’t open cleanly in Google Earth, it doesn’t belong here.

