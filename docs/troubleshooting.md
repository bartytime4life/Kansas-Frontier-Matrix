# Troubleshooting

## Common

- **Jinja2 missing**  
  `pip install jinja2`

- **JSON Schema warnings**  
  `pip install jsonschema` or run with `--no-strict`

- **Blank map**  
  Ensure `web/app.config.json` exists and `assets[*].href` resolve via HTTP

- **ArcGIS reprojection oddities**  
  Confirm `spatial.crs` in `data/sources/*.json` and ensure outputs target `EPSG:4326`

## Helpful Commands

```bash
make stac-validate
kgt validate-stac stac/items --report-json build/stac_report.json
