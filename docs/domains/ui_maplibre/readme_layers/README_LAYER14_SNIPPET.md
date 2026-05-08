## Layer 14 Runtime (Read-only)

Build dashboard:
`python tools/soilgrids/soilgrids_registry_runtime.py --runtime-root runtime_bundles --runtime-mode build-dashboard --registry-manifest ... --registry-snapshot ... --registry-receipt ... --sqlite-db ... --openapi ... --saved-queries ...`

Validate runtime: use `--runtime-mode validate-runtime` (planned extension).

Serve local: use `--runtime-mode serve-local` (planned extension).

Query session:
`python tools/soilgrids/soilgrids_registry_runtime.py --runtime-root runtime_bundles --runtime-mode query-session --sqlite-db ... --saved-queries ... --query-id latest_remote_health`

This layer is strictly read-only and never mutates registry SQLite or evidence crates.
