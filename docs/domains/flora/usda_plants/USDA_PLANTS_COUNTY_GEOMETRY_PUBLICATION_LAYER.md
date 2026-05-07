## 1. Purpose
This layer publishes approved, generalized county boundary geometry joined with already-published USDA PLANTS county presence records.

## 2. Lifecycle placement
This layer runs after controlled public publication of USDA PLANTS tabular artifacts (`release_manifest.json`, `dataset_index.json`, `county_presence.json`, etc.).

## 3. Why this layer exists after publication
County geometry is managed as a separately governed artifact class with explicit source registration, intake, validation, request/approval, publication receipt, rollback planning, and audit.

## 4. County boundary geometry vs occurrence coordinates
- Allowed: county polygon/multipolygon boundaries in approved public county-boundary GeoJSON products.
- Forbidden: plant occurrence or specimen coordinate fields (including `decimalLatitude`, `decimalLongitude`, occurrence/specimen coordinate variants).

## 5. Geometry source model
`usda_plants_county_geometry_source` records authority attribution, geometry vintage, join key (`fips`), and network mode (`disabled` in CI).

## 6. Geometry intake model
`usda_plants_county_geometry_intake` records operator-supplied local fixture/input files, media type checks, hashes, and accepted roles without live download.

## 7. Geometry validation model
`usda_plants_county_geometry_validation_report` enforces FeatureCollection shape, Polygon/MultiPolygon-only geometry, 5-digit FIPS format, no coordinate-leak fields, no tile claims, and county presence coverage.

## 8. Join plan
`usda_plants_county_geometry_join_plan` declares a deterministic FIPS-based join from `county_presence.json` to approved county geometry and fixes the target path under `published/.../map/`.

## 9. Published county-presence GeoJSON
This layer emits `published/flora/usda_plants/<snapshot_date>/map/county_presence.geojson` containing joined county boundary features with required PLANTS properties and deterministic hash.

## 10. MapLibre GeoJSON style
This layer emits a MapLibre style fragment that references the published GeoJSON source only; vector, MBTiles, and PMTiles sources are disallowed.

## 11. Geometry publication request and approval
Publication requires a human-authored request artifact and a separate human approval artifact before public geometry outputs can be produced.

## 12. Rollback and audit ledger
Rollback is planned (not executed) via a supersession strategy requiring human approval; all geometry publication artifacts are tracked in a hash-addressed audit ledger.

## 13. Policy gates
OPA policy denies publication when approval is missing/non-human, validation fails, geometry/FIPS safety checks fail, coordinate leaks exist, tile claims exist, attribution is missing, hashes are missing, or raw/work/quarantine refs leak into public outputs.

## 14. CI and no-network posture
This layer does not fetch USDA data. This layer does not fetch Census data in CI. CI uses local synthetic geometry fixtures and deterministic fixed timestamps for reproducibility.

## 15. What is intentionally not implemented
This layer publishes county boundary geometry only after approval. This layer does not publish plant occurrence coordinates. This layer does not generate vector tiles. This layer does not generate MBTiles or PMTiles.

## 16. Future vector tile layer
Vector tile generation remains future work and will require a dedicated reviewed layer with separate schemas, policy controls, and publication safety approvals.
