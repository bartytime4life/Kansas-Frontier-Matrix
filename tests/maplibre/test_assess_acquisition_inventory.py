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

    def test_maplibre_manifest_in_candidate_seam_is_hold(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(
                root,
                "packages/maplibre/package.json",
                json.dumps({"dependencies": {"maplibre-gl": "6.3.0"}}),
            )
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.HOLD)
        self.assertIn("RENDERER_ACQUISITION_PRESENT", result.reasons)
        self.assertNotIn("ACQUISITION_OUTSIDE_CANDIDATE_SEAM", result.reasons)
        self.assertEqual(result.findings[0].kind, "MANIFEST_DEPENDENCY")
        self.assertTrue(result.findings[0].candidate_seam)

    def test_explorer_adapter_import_is_candidate_seam(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(
                root,
                "apps/explorer-web/src/adapters/MapLibreAdapter.ts",
                'import maplibregl from "maplibre-gl";\nexport { maplibregl };\n',
            )
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.HOLD)
        self.assertNotIn("ACQUISITION_OUTSIDE_CANDIDATE_SEAM", result.reasons)
        self.assertTrue(any(f.kind == "STATIC_IMPORT" and f.candidate_seam for f in result.findings))

    def test_renderer_import_outside_candidate_seam_holds(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(root, "scripts/demo.mjs", 'import maplibregl from "maplibre-gl";\n')
            result = MODULE.scan(root)
        self.assertEqual(result.outcome, MODULE.Outcome.HOLD)
        self.assertIn("ACQUISITION_OUTSIDE_CANDIDATE_SEAM", result.reasons)

    def test_parallel_maplibre_package_homes_fail(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            manifest = json.dumps({"dependencies": {"maplibre-gl": "6.3.0"}})
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

    def test_summary_cli_hides_findings_but_keeps_counts(self) -> None:
        with self._root() as tmp:
            root = Path(tmp)
            self._write(root, "scripts/demo.mjs", 'import maplibregl from "maplibre-gl";\n')
            completed = subprocess.run(
                [sys.executable, str(MODULE_PATH), "--repo-root", str(root), "--summary"],
                check=False,
                capture_output=True,
                text=True,
            )
        self.assertEqual(completed.returncode, 3)
        payload = json.loads(completed.stdout)
        self.assertEqual(payload["outcome"], "HOLD")
        self.assertEqual(payload["findings"], [])
        self.assertEqual(payload["finding_counts"]["STATIC_IMPORT"], 1)
        self.assertFalse(payload["authority_created"])


if __name__ == "__main__":
    unittest.main()
