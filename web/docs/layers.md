# Layer Documentation

Each map layer is defined as JSON in `web/data/*.json`.

## Required Fields
- `id`: unique identifier
- `title`: human-readable title
- `type`: `"raster" | "raster-dem" | "vector" | "geojson"`
- `data` or `url`: location of processed asset
- `category`: matches `categories.json`
- `time`: `{ "start": <date>, "end": <date|null> }`
- `style`: symbolization (circle, line, fill)
- `visible`: default visibility

## Example
```json
{
  "id": "ks_settlements",
  "title": "Settlements, Forts, Trading Posts",
  "type": "vector",
  "data": "data/processed/towns_points.json",
  "category": "culture",
  "time": { "start": "1800-01-01", "end": null },
  "timeProperty": "year",
  "style": { "circleColor": "#FF595E", "circleRadius": 4 },
  "visible": true,
  "attribution": "Compiled / KFM"
}
