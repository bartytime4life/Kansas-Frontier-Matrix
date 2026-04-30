# Pipeline roadmap-only lanes

These lanes are intentionally marked **roadmap-only** until runnable entrypoints and tests are added:

- `pipelines/habitat_layer_build/`
- `pipelines/kansas_biodiversity_etl/dedupe/`
- `pipelines/kansas_biodiversity_etl/normalize/`
- `pipelines/usgs-gage-watch/`
- `pipelines/watchers/kansas_flora_watch/`
- `pipelines/watchers/usda_plants_flora_no_network_slice/`
- `pipelines/watchers/soil_air_quality/`

Exit criteria:
1. Add minimal runnable entrypoint(s).
2. Add lane-local fixtures/tests or validator wiring.
3. Replace README placeholders with verified commands/paths.
