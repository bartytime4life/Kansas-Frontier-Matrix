# Migrations

This directory contains ordered SQL migrations that can be applied directly to provision and evolve the `kfm_crosswalk` database objects used by the hydrology HUC12/admin crosswalk watcher.

## Files

- `001_create_kfm_crosswalk_schema.sql`
  - Creates the `kfm_crosswalk` schema.
  - Enables required extensions (`postgis`, `pgcrypto`).
  - Creates core source, processed geometry, and crosswalk candidate tables.
  - Creates supporting indexes.

- `002_build_crosswalk_pairs.sql`
  - Builds/refreshes `kfm_crosswalk.crosswalk_pairs` from processed HUC12/admin layers.
  - Requires `psql` variables:
    - `run_receipt_id`
    - `algorithm_version`

## Apply

```bash
psql "$KFM_DATABASE_URL" -v ON_ERROR_STOP=1 -f migrations/001_create_kfm_crosswalk_schema.sql
psql "$KFM_DATABASE_URL" -v ON_ERROR_STOP=1 \
  -v run_receipt_id='receipt:local:dev' \
  -v algorithm_version='v1' \
  -f migrations/002_build_crosswalk_pairs.sql
```

## Notes

- These migrations are idempotent where practical (`IF NOT EXISTS`, upsert behavior).
- They are candidate-generation infrastructure only; promotion/publication remains governed outside these migrations.
