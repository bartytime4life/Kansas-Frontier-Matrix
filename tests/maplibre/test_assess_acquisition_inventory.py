from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

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

    def test_renderer_css_import_outside_candidate_seam_fails(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(
                root,
                "apps/explorer/styles.css",
                '@import "maplibre-gl/dist/maplibre-gl.css";\n',
            )
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.FAIL)
        self.assertEqual(result.findings[0].kind, "CSS_IMPORT")
        self.assertEqual(result.findings[0].subject, "maplibre-gl")

    def test_commented_renderer_css_import_remains_inert(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(
                root,
                "apps/explorer/styles.css",
                '/* retired: @import "maplibre-gl/dist/maplibre-gl.css"; */\n',
            )
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.PASS)
        self.assertEqual(result.findings, ())

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

    def test_total_input_budget_errors_without_becoming_acquisition(self) -> None:
        with self._root() as tmp, patch.object(MODULE, "MAX_TOTAL_INPUT_BYTES", 10):
            root = Path(tmp)
            self._write(root, "scripts/first.mjs", " " * 6)
            self._write(root, "scripts/second.mjs", " " * 6)
            self._write(root, "scripts/third.mjs", 'require("maplibre-gl");\n')
            result = MODULE.scan(root)
            payload = result.to_dict()
        self.assertEqual(result.outcome, MODULE.Outcome.ERROR)
        self.assertEqual(result.reasons, ("SCAN_TOTAL_INPUT_TOO_LARGE",))
        self.assertEqual(result.findings[0].kind, "TOTAL_INPUT_BUDGET_EXCEEDED")
        self.assertEqual(result.findings[0].path, "scripts/second.mjs")
        self.assertNotIn("RENDERER_ACQUISITION_PRESENT", result.reasons)
        self.assertNotIn("ACQUISITION_OUTSIDE_CANDIDATE_SEAM", result.reasons)
        self.assertEqual(payload["max_total_input_bytes"], 10)
        self.assertEqual(payload["scanned_bytes"], 11)
        self.assertEqual(payload["scanned_files"], 2)

    def test_input_at_total_budget_is_scanned(self) -> None:
        with self._root() as tmp, patch.object(MODULE, "MAX_TOTAL_INPUT_BYTES", 12):
            root = Path(tmp)
            self._write(root, "scripts/first.mjs", " " * 6)
            self._write(root, "scripts/second.mjs", " " * 6)
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.PASS)
        self.assertEqual(result.findings, ())
        self.assertEqual(result.scanned_bytes, 12)

    def test_verification_reads_are_counted_in_physical_budget(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(root, "scripts/candidate.mjs", "abcdef")
            actual_read_bytes = 0
            real_read = MODULE.os.read

            def counted_read(descriptor: int, count: int) -> bytes:
                nonlocal actual_read_bytes
                chunk = real_read(descriptor, count)
                actual_read_bytes += len(chunk)
                return chunk

            with patch.object(MODULE.os, "read", counted_read):
                result = MODULE.scan(root)

        self.assertEqual(result.outcome, MODULE.Outcome.PASS)
        self.assertEqual(result.scanned_bytes, 6)
        self.assertEqual(result.physical_read_bytes, 12)
        self.assertEqual(result.physical_read_bytes, actual_read_bytes)
        payload = result.to_dict()
        self.assertEqual(payload["physical_read_bytes"], 12)
        self.assertEqual(
            payload["max_total_physical_read_bytes"],
            MODULE.MAX_TOTAL_PHYSICAL_READ_BYTES,
        )

    def test_physical_read_budget_fails_before_unbudgeted_verification(self) -> None:
        with (
            self._root() as tmp,
            patch.object(MODULE, "MAX_TOTAL_PHYSICAL_READ_BYTES", 10),
        ):
            root = Path(tmp)
            self._write(root, "scripts/first.mjs", " " * 3)
            self._write(root, "scripts/second.mjs", " " * 3)
            self._write(root, "scripts/third.mjs", 'require("maplibre-gl");\n')
            result = MODULE.scan(root)
            payload = result.to_dict()

        self.assertEqual(result.outcome, MODULE.Outcome.ERROR)
        self.assertEqual(result.reasons, ("SCAN_TOTAL_PHYSICAL_READ_TOO_LARGE",))
        self.assertEqual(
            result.findings[0].kind, "TOTAL_PHYSICAL_READ_BUDGET_EXCEEDED"
        )
        self.assertEqual(result.findings[0].path, "scripts/second.mjs")
        self.assertEqual(result.scanned_bytes, 3)
        self.assertEqual(result.physical_read_bytes, 6)
        self.assertEqual(payload["max_total_physical_read_bytes"], 10)
        self.assertNotIn("RENDERER_ACQUISITION_PRESENT", result.reasons)

    def test_input_at_physical_read_budget_is_scanned(self) -> None:
        with (
            self._root() as tmp,
            patch.object(MODULE, "MAX_TOTAL_PHYSICAL_READ_BYTES", 10),
        ):
            root = Path(tmp)
            self._write(root, "scripts/first.mjs", " " * 3)
            self._write(root, "scripts/second.mjs", " " * 2)
            result = MODULE.scan(root)

        self.assertEqual(result.outcome, MODULE.Outcome.PASS)
        self.assertEqual(result.findings, ())
        self.assertEqual(result.scanned_bytes, 5)
        self.assertEqual(result.physical_read_bytes, 10)

    def test_final_symlink_replacement_fails_closed_before_read(self) -> None:
        with self._root() as tmp, self._root() as external_tmp:
            root = Path(tmp)
            candidate = root / "scripts" / "candidate.mjs"
            candidate.parent.mkdir(parents=True)
            candidate.write_text("export const safe = true;\n", encoding="utf-8")
            external = Path(external_tmp) / "renderer.mjs"
            external.write_text('require("maplibre-gl");\n', encoding="utf-8")
            real_open = MODULE.os.open
            swapped = False

            def racing_open(path, flags, mode=0o777, *, dir_fd=None):
                nonlocal swapped
                if path == candidate.name and dir_fd is not None and not swapped:
                    swapped = True
                    candidate.unlink()
                    candidate.symlink_to(external)
                return real_open(path, flags, mode, dir_fd=dir_fd)

            with patch.object(MODULE.os, "open", racing_open):
                result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.ERROR)
        self.assertEqual(result.reasons, ("SCAN_INPUT_CHANGED_DURING_OPEN",))
        self.assertEqual(result.findings[0].kind, "INPUT_CHANGED_DURING_OPEN")
        self.assertNotIn("RENDERER_ACQUISITION_PRESENT", result.reasons)

    def test_regular_file_replacement_fails_inode_consistency(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            candidate = root / "scripts" / "candidate.mjs"
            candidate.parent.mkdir(parents=True)
            candidate.write_text("export const safe = true;\n", encoding="utf-8")
            replacement = candidate.with_suffix(".replacement")
            replacement.write_text('require("maplibre-gl");\n', encoding="utf-8")
            real_open = MODULE.os.open
            swapped = False

            def racing_open(path, flags, mode=0o777, *, dir_fd=None):
                nonlocal swapped
                if path == candidate.name and dir_fd is not None and not swapped:
                    swapped = True
                    replacement.replace(candidate)
                return real_open(path, flags, mode, dir_fd=dir_fd)

            with patch.object(MODULE.os, "open", racing_open):
                result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.ERROR)
        self.assertEqual(result.reasons, ("SCAN_INPUT_CHANGED_DURING_OPEN",))
        self.assertEqual(result.findings[0].kind, "INPUT_CHANGED_DURING_OPEN")
        self.assertNotIn("RENDERER_ACQUISITION_PRESENT", result.reasons)

    def test_same_inode_rewrite_during_read_fails_closed(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            candidate = root / "scripts" / "candidate.mjs"
            candidate.parent.mkdir(parents=True)
            active = 'require("maplibre-gl");\n'
            benign = "export {};\n".ljust(len(active))
            candidate.write_text(benign, encoding="utf-8")
            initial_inode = candidate.stat().st_ino
            initial_size = candidate.stat().st_size
            real_read = MODULE.os.read
            changed = False

            def racing_read(descriptor: int, count: int) -> bytes:
                nonlocal changed
                if not changed:
                    changed = True
                    candidate.write_text(active, encoding="utf-8")
                return real_read(descriptor, count)

            with patch.object(MODULE.os, "read", racing_read):
                result = MODULE.scan(root)
            resulting_inode = candidate.stat().st_ino
            resulting_size = candidate.stat().st_size

        self.assertTrue(changed)
        self.assertEqual(resulting_inode, initial_inode)
        self.assertEqual(resulting_size, initial_size)
        self.assertEqual(result.outcome, MODULE.Outcome.ERROR)
        self.assertEqual(result.reasons, ("SCAN_INPUT_CHANGED_DURING_READ",))
        self.assertEqual(result.findings[0].kind, "INPUT_CHANGED_DURING_READ")
        self.assertEqual(result.physical_read_bytes, len(active))
        self.assertNotIn("RENDERER_ACQUISITION_PRESENT", result.reasons)

    def test_stable_metadata_content_change_fails_digest_consistency(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            candidate = root / "scripts" / "candidate.mjs"
            candidate.parent.mkdir(parents=True)
            active = 'require("maplibre-gl");\n'
            benign = "export {};\n".ljust(len(active))
            candidate.write_text(benign, encoding="utf-8")
            real_read = MODULE.os.read
            real_fstat = MODULE.os.fstat
            raced_descriptor: int | None = None
            stable_snapshot = None
            changed = False

            def racing_read(descriptor: int, count: int) -> bytes:
                nonlocal changed, raced_descriptor, stable_snapshot
                chunk = real_read(descriptor, count)
                if chunk and not changed:
                    raced_descriptor = descriptor
                    stable_snapshot = real_fstat(descriptor)
                    candidate.write_text(active, encoding="utf-8")
                    changed = True
                return chunk

            def stable_fstat(descriptor: int):
                if descriptor == raced_descriptor and stable_snapshot is not None:
                    return stable_snapshot
                return real_fstat(descriptor)

            with (
                patch.object(MODULE.os, "read", racing_read),
                patch.object(MODULE.os, "fstat", stable_fstat),
            ):
                result = MODULE.scan(root)

        self.assertTrue(changed)
        self.assertEqual(result.outcome, MODULE.Outcome.ERROR)
        self.assertEqual(
            result.reasons, ("SCAN_INPUT_CONTENT_CHANGED_DURING_VERIFICATION",)
        )
        self.assertEqual(
            result.findings[0].kind, "INPUT_CONTENT_CHANGED_DURING_VERIFICATION"
        )
        self.assertEqual(result.physical_read_bytes, len(active) * 2)
        self.assertNotIn("RENDERER_ACQUISITION_PRESENT", result.reasons)

    def test_parent_swap_cannot_escape_pinned_directory_descriptor(self) -> None:
        with self._root() as tmp, self._root() as external_tmp:
            root = Path(tmp)
            scripts = root / "scripts"
            candidate = scripts / "candidate.mjs"
            scripts.mkdir()
            candidate.write_text("export const safe = true;\n", encoding="utf-8")
            external = Path(external_tmp)
            (external / candidate.name).write_text(
                'require("maplibre-gl");\n', encoding="utf-8"
            )
            parked = root / "scripts-original"
            real_open = MODULE.os.open
            swapped = False

            def racing_open(path, flags, mode=0o777, *, dir_fd=None):
                nonlocal swapped
                if path == candidate.name and dir_fd is not None and not swapped:
                    swapped = True
                    scripts.rename(parked)
                    scripts.symlink_to(external, target_is_directory=True)
                return real_open(path, flags, mode, dir_fd=dir_fd)

            with patch.object(MODULE.os, "open", racing_open):
                result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.PASS)
        self.assertEqual(result.findings, ())

    def test_missing_descriptor_safety_fails_closed(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(root, "scripts/candidate.mjs", "export const safe = true;\n")
            with patch.object(MODULE, "DESCRIPTOR_SAFETY_SUPPORTED", False):
                result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.ERROR)
        self.assertEqual(result.reasons, ("SCAN_DESCRIPTOR_SAFETY_UNAVAILABLE",))
        self.assertEqual(
            result.findings[0].kind, "INPUT_DESCRIPTOR_SAFETY_UNAVAILABLE"
        )

    def test_external_renderer_symlink_errors_without_becoming_acquisition(self) -> None:
        with self._root() as tmp, self._root() as external_tmp:
            root = Path(tmp)
            external = Path(external_tmp) / "renderer.mjs"
            external.write_text('require("maplibre-gl");\n', encoding="utf-8")
            link = root / "scripts" / "linked.mjs"
            link.parent.mkdir(parents=True)
            link.symlink_to(external)
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.ERROR)
        self.assertEqual(result.reasons, ("SCAN_INPUT_SYMLINK_DENIED",))
        self.assertEqual(result.findings[0].kind, "SYMLINK_INPUT_DENIED")
        self.assertEqual(result.findings[0].path, "scripts/linked.mjs")
        self.assertNotIn("RENDERER_ACQUISITION_PRESENT", result.reasons)
        self.assertNotIn("ACQUISITION_OUTSIDE_CANDIDATE_SEAM", result.reasons)

    def test_benign_external_symlink_fails_closed(self) -> None:
        with self._root() as tmp, self._root() as external_tmp:
            root = Path(tmp)
            external = Path(external_tmp) / "benign.mjs"
            external.write_text("export const benign = true;\n", encoding="utf-8")
            link = root / "scripts" / "linked.mjs"
            link.parent.mkdir(parents=True)
            link.symlink_to(external)
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.ERROR)
        self.assertEqual(result.reasons, ("SCAN_INPUT_SYMLINK_DENIED",))
        self.assertEqual(result.findings[0].kind, "SYMLINK_INPUT_DENIED")

    def test_broken_symlink_fails_closed(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            link = root / "scripts" / "broken.mjs"
            link.parent.mkdir(parents=True)
            link.symlink_to(root / "missing.mjs")
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.ERROR)
        self.assertEqual(result.reasons, ("SCAN_INPUT_SYMLINK_DENIED",))
        self.assertEqual(result.findings[0].kind, "SYMLINK_INPUT_DENIED")

    def test_symlinked_scan_root_fails_closed(self) -> None:
        with self._root() as tmp, self._root() as external_tmp:
            root = Path(tmp)
            external = Path(external_tmp)
            (external / "renderer.mjs").write_text(
                'require("maplibre-gl");\n', encoding="utf-8"
            )
            (root / "scripts").symlink_to(external, target_is_directory=True)
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.ERROR)
        self.assertEqual(result.reasons, ("SCAN_INPUT_SYMLINK_DENIED",))
        self.assertEqual(result.findings[0].path, "scripts")

    def test_resolved_path_outside_root_is_denied_before_read(self) -> None:
        with self._root() as tmp, self._root() as external_tmp:
            root = Path(tmp)
            external = Path(external_tmp)
            (external / "renderer.mjs").write_text(
                'require("maplibre-gl");\n', encoding="utf-8"
            )
            scripts = root / "scripts"
            scripts.symlink_to(external, target_is_directory=True)
            result, finding = MODULE._read_bounded_text(
                root,
                scripts / "renderer.mjs",
                MODULE.ScanBudget(),
                unreadable_kind="TEXT_UNREADABLE",
            )
        self.assertIsNone(result)
        self.assertIsNotNone(finding)
        assert finding is not None
        self.assertEqual(finding.kind, "INPUT_OUTSIDE_ROOT")
        self.assertEqual(finding.path, "scripts/renderer.mjs")

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
        self.assertEqual(payload["profile"], "kfm-maplibre-acquisition-inventory-v14")
        self.assertEqual(payload["max_input_bytes"], MODULE.MAX_INPUT_BYTES)
        self.assertEqual(payload["max_total_input_bytes"], MODULE.MAX_TOTAL_INPUT_BYTES)
        self.assertEqual(
            payload["max_total_physical_read_bytes"],
            MODULE.MAX_TOTAL_PHYSICAL_READ_BYTES,
        )
        self.assertEqual(payload["findings"], [])
        self.assertEqual(payload["finding_counts"]["STATIC_IMPORT"], 1)
        self.assertFalse(payload["authority_created"])


if __name__ == "__main__":
    unittest.main()
