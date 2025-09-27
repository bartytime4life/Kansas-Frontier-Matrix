### `web/docs/sources.md`
```markdown
# Source Descriptors

All datasets should have a `data/sources/*.json` file.

## Example: Historic Soil Map
```json
{
  "id": "usda_soil_1967",
  "title": "Soil Survey Map (1967)",
  "type": "raster",
  "endpoint": {
    "type": "http",
    "urls": ["https://archive.example.org/soils/kansas_1967_map.tif"]
  },
  "spatial": { "bbox": [-101.5,39.0,-100.8,39.5], "crs": "EPSG:4326" },
  "temporal": { "start": "1967-01-01", "end": "1967-12-31" },
  "license": "Public Domain",
  "outputs": { "cog": "data/cogs/overlays/soil_map_1967.tif" }
}
