from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.validators.maplibre.validate_v6_readiness import (
    PROFILE,
    PROBE_NAMES,
    TARGET_VERSION,
    UPSTREAM_TAG_COMMIT,
    Outcome,
    evaluate_manifest,
    scan_repository,
)

PROBES = {name: "PASS" for name in PROBE_NAMES}


def write_repo(
    root: Path,
    *,
    version: str | None = TARGET_VERSION,
    explorer_version: str | None = None,
    root_version: str | None = None,
    source: str = "export const ok = true;\n",
    probes: dict[str, str] | None = None,
    probe_profile: str = PROFILE,
) -> None:
    root.joinpath("apps/explorer-web/src").mkdir(parents=True)
    root.joinpath("packages/maplibre/src").mkdir(parents=True)
    root.joinpath("configs/maplibre").mkdir(parents=True)
    root_manifest = {"name": "root", "private": True, "dependencies": {}}
    explorer = {"name": "explorer-web", "type": "module", "dependencies": {}}
    package = {"name": "@kfm/maplibre", "private": True, "version": "0.0.0", "dependencies": {}}
    if root_version is not None:
        root_manifest["dependencies"]["maplibre-gl"] = root_version
    if version is not None:
        package["dependencies"]["maplibre-gl"] = version
    if explorer_version is not None:
        explorer["dependencies"]["maplibre-gl"] = explorer_version
    root.joinpath("package.json").write_text(json.dumps(root_manifest), encoding="utf-8")
    root.joinpath("apps/explorer-web/package.json").write_text(json.dumps(explorer), encoding="utf-8")
    root.joinpath("packages/maplibre/package.json").write_text(json.dumps(package), encoding="utf-8")
    root.joinpath("apps/explorer-web/tsconfig.json").write_text(
        json.dumps({"compilerOptions": {"target": "ES2022"}}), encoding="utf-8"
    )
    root.joinpath("apps/explorer-web/src/app.ts").write_text(source, encoding="utf-8")
    root.joinpath("packages/maplibre/src/adapter.ts").write_text(
        'import maplibregl from "maplibre-gl";\nexport default maplibregl;\n',
        encoding="utf-8",
    )
    root.joinpath("configs/maplibre/v6-probe-results.json").write_text(
        json.dumps({"profile": probe_profile, "probes": probes or PROBES}), encoding="utf-8"
    )


class MapLibreV64ReadinessTests(unittest.TestCase):
    def test_ready_repository_accepts_exact_package_owned_6_4_candidate(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_repo(root)
            result = scan_repository(root)
            self.assertEqual(result.outcome, Outcome.READY)
            self.assertEqual(result.reasons, ())
            self.assertEqual(result.selected_version, TARGET_VERSION)
            self.assertEqual(result.to_dict()["upstream_tag_commit"], UPSTREAM_TAG_COMMIT)

    def test_previous_v6_minor_is_hold(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_repo(root, version="6.3.0")
            result = scan_repository(root)
            self.assertEqual(result.outcome, Outcome.HOLD)
            self.assertIn("MAPLIBRE_TARGET_CANDIDATE_NOT_SELECTED", result.reasons)

    def test_package_and_explorer_version_conflict_is_hold(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_repo(root, explorer_version="5.5.0")
            result = scan_repository(root)
            self.assertEqual(result.outcome, Outcome.HOLD)
            self.assertIn("MAPLIBRE_DEPENDENCY_OWNER_VIOLATION", result.reasons)
            self.assertIn("MAPLIBRE_DEPENDENCY_CONFLICT", result.reasons)

    def test_explorer_owned_exact_version_is_hold(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_repo(root, version=None, explorer_version=TARGET_VERSION)
            result = scan_repository(root)
            self.assertEqual(result.outcome, Outcome.HOLD)
            self.assertIsNone(result.selected_version)
            self.assertIn("MAPLIBRE_DEPENDENCY_OWNER_VIOLATION", result.reasons)
            self.assertIn("MAPLIBRE_DEPENDENCY_UNPINNED", result.reasons)

    def test_duplicate_exact_version_outside_package_is_hold(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_repo(root, explorer_version=TARGET_VERSION)
            result = scan_repository(root)
            self.assertEqual(result.outcome, Outcome.HOLD)
            self.assertEqual(result.selected_version, TARGET_VERSION)
            self.assertIn("MAPLIBRE_DEPENDENCY_OWNER_VIOLATION", result.reasons)
            self.assertNotIn("MAPLIBRE_DEPENDENCY_CONFLICT", result.reasons)

    def test_root_owned_exact_version_is_hold(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_repo(root, version=None, root_version=TARGET_VERSION)
            result = scan_repository(root)
            self.assertEqual(result.outcome, Outcome.HOLD)
            self.assertIsNone(result.selected_version)
            self.assertIn("MAPLIBRE_DEPENDENCY_OWNER_VIOLATION", result.reasons)
            self.assertIn("MAPLIBRE_DEPENDENCY_UNPINNED", result.reasons)

    def test_unreadable_present_package_manifest_is_error(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_repo(root)
            root.joinpath("packages/maplibre/package.json").write_text("{", encoding="utf-8")
            result = scan_repository(root)
            self.assertEqual(result.outcome, Outcome.ERROR)
            self.assertIn("JSON_UNREADABLE", result.reasons)

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
            write_repo(root, version="^6.4.0")
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

    def test_new_kfm_probe_pending_is_hold(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            probes = dict(PROBES)
            probes["image_source_texture_reclamation"] = "NOT_RUN"
            write_repo(root, probes=probes)
            result = scan_repository(root)
            self.assertEqual(result.outcome, Outcome.HOLD)
            self.assertIn("RUNTIME_PROBES_PENDING", result.reasons)

    def test_tile_churn_probe_failure_is_hold(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            probes = dict(PROBES)
            probes["query_rendered_features_tile_churn"] = "FAIL"
            write_repo(root, probes=probes)
            result = scan_repository(root)
            self.assertEqual(result.outcome, Outcome.HOLD)
            self.assertIn("RUNTIME_PROBE_FAILED", result.reasons)

    def test_legacy_probe_profile_is_error(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            write_repo(root, probe_profile="kfm-maplibre-v6-3-readiness-v2")
            result = scan_repository(root)
            self.assertEqual(result.outcome, Outcome.ERROR)
            self.assertIn("PROBE_PROFILE_INVALID", result.reasons)

    def test_upstream_tag_commit_mismatch_is_error(self) -> None:
        manifest = {
            "profile": PROFILE,
            "upstream_tag_commit": "2ebfa18959ae7e737f14da4d565a6c56bb2a6d44",
            "selected_version": TARGET_VERSION,
            "module_mode": "module",
            "typescript_target": "ES2022",
            "internal_transform_access": False,
            "direct_import_boundary_violations": [],
            "probes": PROBES,
            "outcome": "READY",
            "governance": {
                "authority_created": False,
                "upgrade_authorized": False,
                "release_authorized": False,
                "publication_authorized": False,
            },
        }
        result = evaluate_manifest(manifest)
        self.assertEqual(result.outcome, Outcome.ERROR)
        self.assertEqual(result.reasons, ("UPSTREAM_TAG_COMMIT_MISMATCH",))

    def test_declared_outcome_cannot_override_computed_state(self) -> None:
        probes = dict(PROBES)
        probes["headless_render_parity"] = "NOT_RUN"
        manifest = {
            "profile": PROFILE,
            "upstream_tag_commit": UPSTREAM_TAG_COMMIT,
            "selected_version": None,
            "module_mode": "module",
            "typescript_target": "ES2022",
            "internal_transform_access": False,
            "direct_import_boundary_violations": [],
            "probes": probes,
            "outcome": "READY",
            "governance": {
                "authority_created": False,
                "upgrade_authorized": False,
                "release_authorized": False,
                "publication_authorized": False,
            },
        }
        result = evaluate_manifest(manifest)
        self.assertEqual(result.outcome, Outcome.ERROR)
        self.assertIn("DECLARED_OUTCOME_MISMATCH", result.reasons)
        self.assertIn("MAPLIBRE_TARGET_EXACT_VERSION_REQUIRED", result.reasons)


if __name__ == "__main__":
    unittest.main()
