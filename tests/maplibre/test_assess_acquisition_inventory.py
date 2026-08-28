from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "tools" / "validators" / "maplibre" / "assess_acquisition_inventory.py"
SPEC = importlib.util.spec_from_file_location("assess_acquisition_inventory", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class AcquisitionInventoryTests(unittest.TestCase):
    def _root(self) -> tempfile.TemporaryDirectory[str]:
        return tempfile.TemporaryDirectory()

    @staticmethod
    def _write(root: Path, relative: str, content: str) -> None:
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def test_empty_repository_passes_without_authority(self) -> None:
        with self._root() as tmp:
            result = MODULE.scan(Path(tmp))
        self.assertEqual(result.outcome, MODULE.Outcome.PASS)
        payload = result.to_dict()
        self.assertFalse(payload["authority_created"])
        self.assertFalse(payload["dependency_admitted"])
        self.assertFalse(payload["renderer_selected"])
        self.assertEqual(payload["findings"], [])

    def test_kfm_facade_import_and_dependency_are_not_raw_acquisition(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(
                root,
                "apps/explorer-web/package.json",
                json.dumps({"dependencies": {"@kfm/maplibre": "workspace:*"}}),
            )
            self._write(
                root,
                "apps/explorer-web/src/features/map_runtime/index.ts",
                'import { MAP_RUNTIME_PORT_PROFILE } from "@kfm/maplibre";\n'
                'export { MAP_RUNTIME_PORT_PROFILE };\n',
            )
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.PASS)
        self.assertEqual(result.findings, ())

    def test_maplibre_manifest_in_candidate_seam_is_hold(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(
                root,
                "packages/maplibre/package.json",
                json.dumps({"dependencies": {"maplibre-gl": "6.4.0"}}),
            )
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.HOLD)
        self.assertIn("RENDERER_ACQUISITION_PRESENT", result.reasons)
        self.assertNotIn("ACQUISITION_OUTSIDE_CANDIDATE_SEAM", result.reasons)
        self.assertEqual(result.findings[0].kind, "MANIFEST_DEPENDENCY")
        self.assertTrue(result.findings[0].candidate_seam)

    def test_package_owned_adapter_import_is_confined_to_candidate_seam(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(
                root,
                "packages/maplibre/src/maplibre-adapter.ts",
                'import { Map } from "maplibre-gl";\nexport const create = Map;\n',
            )
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.HOLD)
        self.assertEqual(result.reasons, ("RENDERER_ACQUISITION_PRESENT",))
        self.assertEqual(len(result.findings), 1)
        self.assertEqual(result.findings[0].kind, "STATIC_IMPORT")
        self.assertTrue(result.findings[0].candidate_seam)

    def test_package_local_maplibre_filename_is_not_raw_acquisition(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(
                root,
                "packages/maplibre/tests/adapter.test.ts",
                'import { create } from "../src/maplibre-adapter";\nexport { create };\n',
            )
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.PASS)
        self.assertEqual(result.findings, ())

    def test_kfm_facade_and_package_local_re_exports_are_not_raw_acquisition(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(
                root,
                "apps/explorer-web/src/map-runtime.ts",
                'export type { MapRuntimePort } from "@kfm/maplibre";\n'
                'export { createAdapter } from "./maplibre-adapter";\n',
            )
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.PASS)
        self.assertEqual(result.findings, ())

    def test_explorer_adapter_raw_import_is_outside_accepted_seam(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(
                root,
                "apps/explorer-web/src/adapters/MapLibreAdapter.ts",
                'import maplibregl from "maplibre-gl";\nexport { maplibregl };\n',
            )
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.FAIL)
        self.assertIn("ACQUISITION_OUTSIDE_CANDIDATE_SEAM", result.reasons)
        self.assertTrue(any(f.kind == "STATIC_IMPORT" and not f.candidate_seam for f in result.findings))

    def test_renderer_import_outside_candidate_seam_fails(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(root, "scripts/demo.mjs", 'import maplibregl from "maplibre-gl";\n')
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.FAIL)
        self.assertIn("ACQUISITION_OUTSIDE_CANDIDATE_SEAM", result.reasons)

    def test_renderer_re_exports_outside_candidate_seam_fail(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(
                root,
                "apps/explorer-web/src/renderer.ts",
                'export { Map } from "maplibre-gl";\n'
                'export type { MapOptions } from "maplibre-gl";\n'
                'export * as maplibregl from "maplibre-gl";\n'
                'export * from "maplibre-gl";\n',
            )
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.FAIL)
        self.assertIn("ACQUISITION_OUTSIDE_CANDIDATE_SEAM", result.reasons)
        self.assertEqual(
            [finding.kind for finding in result.findings],
            ["RE_EXPORT"],
        )

    def test_package_owned_renderer_re_export_is_hold(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(
                root,
                "packages/maplibre/src/renderer.ts",
                'export { Map } from "maplibre-gl";\n',
            )
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.HOLD)
        self.assertEqual(result.findings[0].kind, "RE_EXPORT")
        self.assertTrue(result.findings[0].candidate_seam)

    def test_renderer_module_resolution_outside_candidate_seam_fails(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(
                root,
                "scripts/resolve-renderer.mjs",
                'const esm = import.meta.resolve("maplibre-gl");\n'
                'const cjs = require.resolve("maplibre-gl");\n',
            )
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.FAIL)
        self.assertEqual(
            [finding.kind for finding in result.findings],
            ["IMPORT_META_RESOLVE", "REQUIRE_RESOLVE"],
        )

    def test_create_require_alias_acquisition_outside_candidate_seam_fails(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(
                root,
                "scripts/load-renderer.mjs",
                'import { createRequire } from "node:module";\n'
                "const localRequire = createRequire(import.meta.url);\n"
                'localRequire("maplibre-gl");\n'
                'localRequire.resolve("maplibre-gl");\n',
            )
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.FAIL)
        self.assertEqual(
            [finding.kind for finding in result.findings],
            ["CREATE_REQUIRE", "CREATE_REQUIRE_RESOLVE"],
        )

    def test_aliased_and_namespace_create_require_resolution_is_classified(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(
                root,
                "scripts/resolve-renderer.mjs",
                'import { createRequire as makeRequire } from "module";\n'
                'import * as nodeModule from "node:module";\n'
                "const resolveFromHere = makeRequire(import.meta.url);\n"
                'resolveFromHere.resolve("maplibre-gl");\n'
                'nodeModule.createRequire(import.meta.url)("maplibre-gl");\n',
            )
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.FAIL)
        self.assertEqual(
            [finding.kind for finding in result.findings],
            ["CREATE_REQUIRE", "CREATE_REQUIRE_RESOLVE"],
        )

    def test_package_owned_create_require_acquisition_is_hold(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(
                root,
                "packages/maplibre/scripts/load-renderer.cjs",
                'const { createRequire: makeRequire } = require("node:module");\n'
                "const localRequire = makeRequire(__filename);\n"
                'localRequire("maplibre-gl");\n',
            )
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.HOLD)
        self.assertEqual(result.findings[0].kind, "CREATE_REQUIRE")
        self.assertTrue(result.findings[0].candidate_seam)

    def test_unimported_create_require_and_kfm_facade_are_not_raw_acquisition(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(
                root,
                "scripts/local-helper.mjs",
                "const localRequire = createRequire(import.meta.url);\n"
                'localRequire("maplibre-gl");\n'
                'import { createRequire as makeRequire } from "node:module";\n'
                "const facadeRequire = makeRequire(import.meta.url);\n"
                'facadeRequire("@kfm/maplibre");\n',
            )
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.PASS)
        self.assertEqual(result.findings, ())

    def test_renderer_examples_in_comments_are_not_active_acquisition(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(
                root,
                "scripts/retired-example.mjs",
                "/* retired example:\n"
                'import { Map } from "maplibre-gl";\n'
                "const map = new maplibregl.Map({});\n"
                'const url = "https://unpkg.com/maplibre-gl@6.6.0/dist/maplibre-gl.mjs";\n'
                "*/\n"
                '// require.resolve("maplibre-gl");\n'
                '<!-- <script src="https://unpkg.com/maplibre-gl@6.6.0/dist/maplibre-gl.mjs"></script> -->\n',
            )
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.PASS)
        self.assertEqual(result.findings, ())

    def test_comment_markers_inside_runtime_strings_are_preserved(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(
                root,
                "scripts/runtime-url.mjs",
                'const rendererUrl = "https://unpkg.com/maplibre-gl@6.6.0/dist/maplibre-gl.mjs";\n',
            )
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.FAIL)
        self.assertEqual(result.findings[0].kind, "CDN_URL")

    def test_active_acquisition_after_comments_still_fails(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(
                root,
                "scripts/active-renderer.mjs",
                '// retired: require.resolve("maplibre-gl");\n'
                'import { Map } from "maplibre-gl";\n',
            )
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.FAIL)
        self.assertEqual(result.findings[0].kind, "STATIC_IMPORT")

    def test_active_acquisition_after_regex_literal_still_fails(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(
                root,
                "scripts/active-after-regex.mjs",
                'const protocol = /https?:\\/\\//; require("maplibre-gl");\n',
            )
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.FAIL)
        self.assertEqual(result.findings[0].kind, "REQUIRE")

    def test_comment_after_regex_literal_remains_inert(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(
                root,
                "scripts/comment-after-regex.mjs",
                '/["\']/; // require("maplibre-gl")\n',
            )
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.PASS)
        self.assertEqual(result.findings, ())

    def test_division_before_comment_is_not_treated_as_regex(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(
                root,
                "scripts/division-before-comment.mjs",
                'const ratio = distance / duration; // require("maplibre-gl")\n',
            )
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.PASS)
        self.assertEqual(result.findings, ())

    def test_governance_link_and_maplibre_css_class_are_not_acquisition(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(
                root,
                "apps/explorer-web/src/site.ts",
                """
                const issue = `https://github.com/example/project/issues/${CURRENT_MAPLIBRE_READINESS.issue}`;
                const docs = "https://maplibre.org/maplibre-gl-js/docs/";
                expect(root).toHaveClass(/maplibregl-map/);
                """,
            )
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.PASS)
        self.assertEqual(result.findings, ())

    def test_renderer_cdn_asset_outside_candidate_seam_fails(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(
                root,
                "public/demo.html",
                '<script src="https://unpkg.com/maplibre-gl@6.6.0/dist/maplibre-gl.js"></script>\n',
            )
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.FAIL)
        self.assertTrue(any(f.kind == "CDN_URL" for f in result.findings))

    def test_extensionless_renderer_package_on_known_cdn_fails(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(
                root,
                "public/demo.html",
                '<script type="module" src="https://esm.sh/maplibre-gl@6.6.0"></script>\n',
            )
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.FAIL)
        self.assertTrue(any(f.kind == "CDN_URL" for f in result.findings))

    def test_renderer_global_usage_outside_candidate_seam_fails(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(root, "scripts/demo.js", "const map = new maplibregl.Map({});\n")
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.FAIL)
        self.assertTrue(any(f.kind == "GLOBAL_RUNTIME" for f in result.findings))

    def test_standalone_renderer_global_reference_fails(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(root, "scripts/demo.js", "const renderer = maplibregl;\n")
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.FAIL)
        self.assertTrue(any(f.kind == "GLOBAL_RUNTIME" for f in result.findings))

    def test_parallel_maplibre_package_homes_fail(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            manifest = json.dumps({"dependencies": {"maplibre-gl": "6.4.0"}})
            self._write(root, "packages/maplibre/package.json", manifest)
            self._write(root, "packages/maplibre-runtime/package.json", manifest)
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.FAIL)
        self.assertIn("PARALLEL_MAPLIBRE_PACKAGE_HOMES", result.reasons)

    def test_malformed_manifest_errors(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(root, "packages/maplibre/package.json", "{not-json")
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.ERROR)
        self.assertIn("SCAN_INPUT_UNREADABLE", result.reasons)

    def test_oversized_input_errors_without_becoming_acquisition(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            path = root / "scripts" / "oversized.mjs"
            path.parent.mkdir(parents=True)
            path.write_bytes(b" " * (MODULE.MAX_INPUT_BYTES + 1))
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.ERROR)
        self.assertEqual(result.reasons, ("SCAN_INPUT_TOO_LARGE",))
        self.assertEqual(result.findings[0].kind, "INPUT_TOO_LARGE")
        self.assertNotIn("RENDERER_ACQUISITION_PRESENT", result.reasons)
        self.assertNotIn("ACQUISITION_OUTSIDE_CANDIDATE_SEAM", result.reasons)
        self.assertEqual(result.to_dict()["max_input_bytes"], MODULE.MAX_INPUT_BYTES)

    def test_input_at_byte_limit_is_scanned(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            path = root / "scripts" / "at-limit.mjs"
            path.parent.mkdir(parents=True)
            path.write_bytes(b" " * MODULE.MAX_INPUT_BYTES)
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.PASS)
        self.assertEqual(result.findings, ())

    def test_summary_cli_hides_findings_but_keeps_counts(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(root, "packages/maplibre/src/demo.mjs", 'import { Map } from "maplibre-gl";\n')
            completed = subprocess.run(
                [sys.executable, str(MODULE_PATH), "--repo-root", str(root), "--summary"],
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(completed.returncode, 3)
        payload = json.loads(completed.stdout)
        self.assertEqual(payload["outcome"], "HOLD")
        self.assertEqual(payload["profile"], "kfm-maplibre-acquisition-inventory-v7")
        self.assertEqual(payload["max_input_bytes"], MODULE.MAX_INPUT_BYTES)
        self.assertEqual(payload["findings"], [])
        self.assertEqual(payload["finding_counts"]["STATIC_IMPORT"], 1)
        self.assertFalse(payload["authority_created"])


if __name__ == "__main__":
    unittest.main()
