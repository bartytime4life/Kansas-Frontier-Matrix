# Validation Report

## reorg_status
```
 M docs/adr/README.md
 M docs/registers/README.md
 M docs/registers/domain_doc_index.md
 M docs/registers/domain_file_index.md
 M docs/registers/policy_authority_map.md
 M docs/registers/reorg/REORG_SPRINT_MANIFEST.md
 M docs/registers/reorg/authority_conflicts.md
 M docs/registers/reorg/move_plan.tsv
 M docs/registers/reorg/reference_update_plan.tsv
 M docs/registers/reorg/rollback_plan.sh
 M docs/registers/reorg/validation_report.md
 M docs/registers/schema_authority_map.md
 M docs/runbooks/README.md

```

## reorg_diffstat
```
 docs/adr/README.md                             |   5 +
 docs/registers/README.md                       |   6 +
 docs/registers/domain_doc_index.md             |  20 +-
 docs/registers/domain_file_index.md            | 257 ++++++++++++++++++++++++-
 docs/registers/policy_authority_map.md         |  13 +-
 docs/registers/reorg/REORG_SPRINT_MANIFEST.md  |  53 +++--
 docs/registers/reorg/authority_conflicts.md    |   6 +-
 docs/registers/reorg/move_plan.tsv             |   2 +-
 docs/registers/reorg/reference_update_plan.tsv |   4 +-
 docs/registers/reorg/rollback_plan.sh          |  13 +-
 docs/registers/reorg/validation_report.md      |   4 +-
 docs/registers/schema_authority_map.md         |  14 +-
 docs/runbooks/README.md                        |   3 +
 13 files changed, 333 insertions(+), 67 deletions(-)

```

## reorg_manifest_check
```
OK manifest basic checks passed

```

## reorg_orphans
```
OK no doc orphans in docs/

```

## reorg_boundaries
```
BLOCKED direct raw/work/quarantine references detected:
apps/web/src/__tests__/tileReleasePublisher.test.js

```

## reorg_pytest_repo_inventory
```
....                                                                     [100%]
4 passed in 0.22s

```

## reorg_collect
```
apps/governed_api/ecology/tests/test_evidencebundle_resolver.py::test_resolver_returns_cite_for_valid_proof_pack
apps/governed_api/ecology/tests/test_evidencebundle_resolver.py::test_resolver_abstains_when_proof_pack_missing
apps/governed_api/ecology/tests/test_evidencebundle_resolver.py::test_resolver_abstains_on_malformed_json
apps/governed_api/ecology/tests/test_evidencebundle_resolver.py::test_resolver_abstains_on_non_object_json
apps/governed_api/ecology/tests/test_evidencebundle_resolver.py::test_resolver_abstains_on_schema_failure
apps/governed_api/ecology/tests/test_evidencebundle_resolver.py::test_resolver_abstains_on_spec_hash_mismatch
apps/governed_api/ecology/tests/test_evidencebundle_resolver.py::test_resolver_abstains_when_prov_missing
apps/governed_api/ecology/tests/test_evidencebundle_resolver.py::test_resolver_abstains_when_status_not_complete
apps/governed_api/ecology/tests/test_fastapi_routes.py::test_evidence_bundle_route_is_registered
apps/governed_api/ecology/tests/test_focus_app.py::test_ecology_focus_returns_runtime_response
apps/governed_api/ecology/tests/test_focus_app.py::test_ecology_focus_wraps_runtime_errors
apps/governed_api/ecology/tests/test_route_response_contract_schema.py::test_route_cite_payload_matches_contract_schema
apps/governed_api/ecology/tests/test_route_response_contract_schema.py::test_route_abstain_payload_matches_contract_schema
apps/governed_api/ecology/tests/test_route_response_contract_schema.py::test_route_contract_negative_missing_candidate_id_is_rejected
apps/governed_api/ecology/tests/test_routes.py::test_default_schema_path_points_to_existing_schema
apps/governed_api/ecology/tests/test_routes.py::test_abstain_when_proof_pack_missing
apps/governed_api/ecology/tests/test_runtime_envelope_compatibility.py::test_cite_response_matches_runtime_envelope
apps/governed_api/ecology/tests/test_runtime_envelope_compatibility.py::test_abstain_response_matches_runtime_envelope
apps/ui/ecology/tests/test_evidence_drawer_contract_schema.py::test_drawer_cite_payload_matches_contract_schema
apps/ui/ecology/tests/test_evidence_drawer_contract_schema.py::test_drawer_abstain_payload_matches_contract_schema
apps/ui/ecology/tests/test_evidence_drawer_contract_schema.py::test_drawer_contract_negative_missing_actions_is_rejected
apps/ui/ecology/tests/test_evidence_drawer_mapper.py::test_maps_cite_response_to_drawer_payload
apps/ui/ecology/tests/test_evidence_drawer_mapper.py::test_maps_abstain_response_to_drawer_payload
apps/ui/ecology/tests/test_evidence_drawer_mapper.py::test_malformed_response_defaults_to_abstain
apps/ui/ecology/tests/test_evidence_drawer_mapper.py::test_missing_evidence_sections_render_empty_values
apps/ui/ecology/tests/test_evidence_drawer_mapper.py::test_non_cite_decision_maps_to_abstain
packages/ingest/tests/test_decision_engine.py::test_decision_paths_and_artifacts
packages/ingest/tests/test_decision_engine.py::test_canonical_hash_stability
packages/ingest/tests/test_decision_engine.py::test_conflicting_signal_fails_closed
pipelines/habitat_layer_build/tests/test_habitat_layer_build.py::test_good_fixture_validates
pipelines/habitat_layer_build/tests/test_habitat_layer_build.py::test_bad_fixture_fails
pipelines/kansas_biodiversity_etl/catalog/tests/test_validate_catalog.py::test_valid_catalog_passes
pipelines/kansas_biodiversity_etl/catalog/tests/test_validate_catalog.py::test_missing_collection_fails
pipelines/kansas_biodiversity_etl/catalog/tests/test_validate_catalog.py::test_no_stac_items_fails
pipelines/kansas_biodiversity_etl/catalog/tests/test_validate_catalog.py::test_stac_item_hash_mismatch_fails
pipelines/kansas_biodiversity_etl/catalog/tests/test_validate_catalog.py::test_dcat_hash_mismatch_fails
pipelines/kansas_biodiversity_etl/catalog/tests/test_validate_catalog.py::test_prov_missing_spec_hash_fails
pipelines/kansas_biodiversity_etl/catalog/tests/test_validate_catalog.py::test_stac_root_missing_fails
pipelines/watchers/kansas_flora_watch/tests/test_runner.py:
```

## reorg_web_test
```
npm warn Unknown env config "http-proxy". This will stop working in the next major version of npm.

> @kfm/web@0.1.0 test
> vitest run --passWithNoTests --run

vite.config.js (2:18) [33m[UNRESOLVED_IMPORT] Warning:[0m Could not resolve '@vitejs/plugin-react' in vite.config.js
   [38;5;246m╭[0m[38;5;246m─[0m[38;5;246m[[0m vite.config.js:2:19 [38;5;246m][0m
   [38;5;246m│[0m
 [38;5;246m2 │[0m [38;5;249mi[0m[38;5;249mm[0m[38;5;249mp[0m[38;5;249mo[0m[38;5;249mr[0m[38;5;249mt[0m[38;5;249m [0m[38;5;249mr[0m[38;5;249me[0m[38;5;249ma[0m[38;5;249mc[0m[38;5;249mt[0m[38;5;249m [0m[38;5;249mf[0m[38;5;249mr[0m[38;5;249mo[0m[38;5;249mm[0m[38;5;249m [0m'@vitejs/plugin-react'[38;5;249m;[0m
 [38;5;240m  │[0m                   ───────────┬──────────  
 [38;5;240m  │[0m                              ╰──────────── Module not found, treating it as an external dependency
[38;5;246m───╯[0m

failed to load config from /workspace/Kansas-Frontier-Matrix/apps/web/vite.config.js

⎯⎯⎯⎯⎯⎯⎯ Startup Error ⎯⎯⎯⎯⎯⎯⎯⎯
Error [ERR_MODULE_NOT_FOUND]: Cannot find package '@vitejs/plugin-react' imported from /workspace/Kansas-Frontier-Matrix/apps/web/node_modules/.vite-temp/vite.config.js.timestamp-1777784190147-8577b0b641f1d.mjs
    at Object.getPackageJSONURL (node:internal/modules/package_json_reader:314:9)
    at packageResolve (node:internal/modules/esm/resolve:767:81)
    at moduleResolve (node:internal/modules/esm/resolve:853:18)
    at defaultResolve (node:internal/modules/esm/resolve:983:11)
    at #cachedDefaultResolve (node:internal/modules/esm/loader:731:20)
    at ModuleLoader.resolve (node:internal/modules/esm/loader:708:38)
    at ModuleLoader.getModuleJobForImport (node:internal/modules/esm/loader:310:38)
    at ModuleJob._link (node:internal/modules/esm/module_job:182:49) {
  code: 'ERR_MODULE_NOT_FOUND'
}




```

## reorg_web_build
```
npm warn Unknown env config "http-proxy". This will stop working in the next major version of npm.

> @kfm/web@0.1.0 build
> vite build

vite.config.js (2:18) [33m[UNRESOLVED_IMPORT] Warning:[0m Could not resolve '@vitejs/plugin-react' in vite.config.js
   [38;5;246m╭[0m[38;5;246m─[0m[38;5;246m[[0m vite.config.js:2:19 [38;5;246m][0m
   [38;5;246m│[0m
 [38;5;246m2 │[0m [38;5;249mi[0m[38;5;249mm[0m[38;5;249mp[0m[38;5;249mo[0m[38;5;249mr[0m[38;5;249mt[0m[38;5;249m [0m[38;5;249mr[0m[38;5;249me[0m[38;5;249ma[0m[38;5;249mc[0m[38;5;249mt[0m[38;5;249m [0m[38;5;249mf[0m[38;5;249mr[0m[38;5;249mo[0m[38;5;249mm[0m[38;5;249m [0m'@vitejs/plugin-react'[38;5;249m;[0m
 [38;5;240m  │[0m                   ───────────┬──────────  
 [38;5;240m  │[0m                              ╰──────────── Module not found, treating it as an external dependency
[38;5;246m───╯[0m

failed to load config from /workspace/Kansas-Frontier-Matrix/apps/web/vite.config.js
error during build:
Error [ERR_MODULE_NOT_FOUND]: Cannot find package '@vitejs/plugin-react' imported from /workspace/Kansas-Frontier-Matrix/apps/web/node_modules/.vite-temp/vite.config.js.timestamp-1777784190946-661ae3551b6b4.mjs
    at Object.getPackageJSONURL (node:internal/modules/package_json_reader:314:9)
    at packageResolve (node:internal/modules/esm/resolve:767:81)
    at moduleResolve (node:internal/modules/esm/resolve:853:18)
    at defaultResolve (node:internal/modules/esm/resolve:983:11)
    at #cachedDefaultResolve (node:internal/modules/esm/loader:731:20)
    at ModuleLoader.resolve (node:internal/modules/esm/loader:708:38)
    at ModuleLoader.getModuleJobForImport (node:internal/modules/esm/loader:310:38)
    at ModuleJob._link (node:internal/modules/esm/module_job:182:49) {
  code: 'ERR_MODULE_NOT_FOUND'
}

```
