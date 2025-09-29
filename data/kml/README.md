# Kansas-Frontier-Matrix — KML / KMZ Exports

This folder holds **Google Earth–ready** exports of our rasters and vectors:  
- Regionated **KML/KMZ super-overlays** of large rasters (DEM hillshade, georeferenced historic topos).  
- Lightweight **KMLs** for vectors (treaties, railroads, trails, floodplains).  
- Small JSON sidecars (`*.meta.json`) for provenance + traceability (MCP-style).  

> 💡 Tip: Prefer **KMZ** (zipped KML + assets) for distribution; aim to keep each file < ~100–200 MB.  
> KMZ files can be attached to GitHub releases or published as project deliverables for educators,  
> historians, and the public.

---

## What belongs here

- `*.kmz` — regionated raster super-overlays for Google Earth.  
- `*.kml` — vectors (and very small rasters).  
- `*.meta.json` — per-export metadata (who/when/how, inputs, checksums).  
- `README.md` — this documentation.  

We **do not** stage raw/processed COGs or GeoJSON here; those live under `data/cogs/**` and `data/processed/**`.  
This directory is strictly for **Earth viewer exports** [oai_citation:0‡Kansas Frontier Matrix – GIS Archive & Deeds Data Integration Guide.pdf](file-service://file-A8GiBPZM1dWsKG68SXPHjE).

---

## Conventions

### CRS
- Google Earth renders in geographic WGS84. Export tools will reproject automatically.  
- Always record the **source CRS** in metadata.

### Naming

[_].kmz
e.g.,
ks_hillshade_2018_2020.kmz
usgs_topo_larned_1894.kmz
treaties.kml
railroads_1900.kml

### Metadata (`*.meta.json`)
Create a JSON sidecar alongside each KML/KMZ:

```json
{
  "id": "usgs_topo_larned_1894_kmz",
  "title": "USGS Topo – Larned (1894), KMZ Super-Overlay",
  "source_raster": "data/cogs/overlays/usgs_topo_larned_1894.tif",
  "export_tool": "gdal_translate -of KMLSUPEROVERLAY -co FORMAT=PNG",
  "processing": "Auto-regionated pyramid inside KMZ",
  "rms_georef_m": 8.6,
  "license": "Public Domain (USGS)",
  "created": "2025-09-19T20:30:00Z",
  "sha256": "<checksum of KMZ>"
}

Metadata ensures traceability and MCP reproducibility ￼.

⸻

How to generate

A) Raster → KMZ super-overlay

gdal_translate -of KMLSUPEROVERLAY \
  -co FORMAT=PNG \
  data/cogs/hillshade/ks_hillshade_2018_2020.tif \
  data/kml/ks_hillshade_2018_2020.kmz

	•	Use PNG for transparency (hillshade, topos).
	•	Use JPEG for photographic imagery (smaller KMZ).

B) Vector → KML

# Treaties (polygon)
ogr2ogr -f KML data/kml/treaties.kml data/processed/vectors/treaties.geojson \
  -dsco NameField=name -select id,name,year

# Railroads circa 1900 (line)
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

Makefile Integration

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

Quality & Troubleshooting
	•	KMZ too large? Crop/downsample first (gdalwarp -te …).
	•	Blurred tiles? Export from the highest-resolution source; avoid double pyramids.
	•	Transparency lost? Ensure alpha band or NODATA is set.
	•	Vector clutter? Simplify and trim attributes (ogr2ogr -simplify 0.0005).
	•	Layer names wrong? Use -dsco NameField=<field> with ogr2ogr.

⸻

Checklist before committing
	•	✅ Opens cleanly in Google Earth Pro (desktop).
	•	✅ Reasonable size (prefer KMZ).
	•	✅ *.meta.json present (provenance, inputs, tool versions).
	•	✅ Titles/descriptions are non-technical.
	•	✅ Linked to STAC items in stac/items/kml/.

⸻

Examples staged next
	•	ks_hillshade_2018_2020.kmz — DEM hillshade super-overlay.
	•	usgs_topo_larned_1894.kmz — georeferenced historic topo.
	•	treaties.kml — treaty/reservation polygons.
	•	railroads_1900.kml — 1900-era railroads (for time slider).

⸻

See Also
	•	data/cogs/ — source rasters for KMZ exports.
	•	data/processed/vectors/ — source vectors for KML exports.
	•	data/stac/ — STAC items documenting exports and provenance.
	•	docs/ — MCP method & reproducibility templates.

---

Would you like me to also generate a **`treaties.meta.json`** and a **`railroads_1900.meta.json`** example so those vector KML exports are immediately STAC-linked and MCP-compliant?