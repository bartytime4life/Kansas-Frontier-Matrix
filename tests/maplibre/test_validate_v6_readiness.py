from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.validators.maplibre.validate_v6_readiness import Outcome, evaluate_manifest, scan_repository

PROBES = {
    "webgl2_failure_handling": "PASS",
    "worker_csp_loading": "PASS",
    "style_spec_v25": "PASS",
    "geojson_set_data": "PASS",
    "query_rendered_features": "PASS",
    "visual_pixel_diff": "PASS",
}


def write_repo(root: Path, *, version: str | None = "6.0.0", source: str = "export const ok = true;\n", probes: dict[str, str] | None = None) -> None:
    root.joinpath("apps/explorer-web/src").mkdir(parents=True)
    root.joinpath("packages/maplibre/src").mkdir(parents=True)
    root.joinpath("configs/maplibre").mkdir(parents=True)
    root_manifest = {"name": "root", "private": True}
    explorer = {"name": "explorer-web", "type": "module", "dependencies": {}}
    if version is not None:
        explorer["dependencies"]["maplibre-gl"] = version
    root.joinpath("package.json").write_text(json.dumps(root_manifest))
    root.joinpath("apps/explorer-web/package.json").write_text(json.dumps(explorer))
    root.joinpath("apps/explorer-web/tsconfig.json").write_text(json.dumps({"compilerOptions": {"target": "ES2022"}}))
    root.joinpath("apps/explorer-web/src/app.ts").write_text(source)
    root.joinpath("packages/maplibre/src/adapter.ts").write_text('import maplibregl from "maplibre-gl";\nexport default maplibregl;\n')
    root.joinpath("configs/maplibre/v6-probe-results.json").write_text(json.dumps({"profile": "kfm-maplibre-v6-readiness-v1", "probes": probes or PROBES}))


class MapLibreV6ReadinessTests(unittest.TestCase):
    def test_ready_repository_requires_exact_v6_and_all_probes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_repo(root)
            result = scan_repository(root)
            self.assertEqual(result.outcome, Outcome.READY)
            self.assertEqual(result.reasons, ())

    def test_missing_dependency_is_hold_not_false_ready(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_repo(root, version=None)
            result = scan_repository(root)
            self.assertEqual(result.outcome, Outcome.HOLD)
            self.assertIn("MAPLIBRE_DEPENDENCY_UNPINNED", result.reasons)

    def test_floating_version_is_hold(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_repo(root, version="^6.0.0")
            result = scan_repository(root)
            self.assertIn("MAPLIBRE_VERSION_NOT_EXACT", result.reasons)

    def test_internal_transform_access_is_hold(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_repo(root, source="export const x = map.transform.center;\n")
            result = scan_repository(root)
            self.assertIn("INTERNAL_TRANSFORM_ACCESS_PRESENT", result.reasons)

    def test_direct_import_outside_adapter_is_hold(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_repo(root, source='import { Map } from "maplibre-gl";\nexport { Map };\n')
            result = scan_repository(root)
            self.assertIn("MAPLIBRE_IMPORT_BOUNDARY_VIOLATION", result.reasons)

    def test_pending_probe_is_hold(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            probes = dict(PROBES); probes["visual_pixel_diff"] = "NOT_RUN"
            write_repo(root, probes=probes)
            result = scan_repository(root)
            self.assertEqual(result.outcome, Outcome.HOLD)
            self.assertIn("RUNTIME_PROBES_PENDING", result.reasons)

    def test_declared_outcome_cannot_override_computed_state(self) -> None:
        manifest = {"profile": "kfm-maplibre-v6-readiness-v1", "selected_version": None, "module_mode": "module", "typescript_target": "ES2022", "internal_transform_access": False, "direct_import_boundary_violations": [], "probes": {**PROBES, "visual_pixel_diff": "NOT_RUN"}, "outcome": "READY", "governance": {"authority_created": False, "upgrade_authorized": False, "release_authorized": False, "publication_authorized": False}}
        result = evaluate_manifest(manifest)
        self.assertEqual(result.outcome, Outcome.ERROR)
        self.assertIn("DECLARED_OUTCOME_MISMATCH", result.reasons)


if __name__ == "__main__":
    unittest.main()
