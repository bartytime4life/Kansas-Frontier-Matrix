from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

GENERATOR_PATH = (
    Path(__file__).resolve().parents[2]
    / "tools"
    / "generators"
    / "build_registry_lane_discovery_index.py"
)

_SPEC = importlib.util.spec_from_file_location(
    "build_registry_lane_discovery_index", GENERATOR_PATH
)
assert _SPEC and _SPEC.loader
_MODULE = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_MODULE)

RegistryDiscoveryError = _MODULE.RegistryDiscoveryError
build_registry_lane_discovery_index = _MODULE.build_registry_lane_discovery_index
render_index = _MODULE.render_index


class RegistryLaneDiscoveryIndexTests(unittest.TestCase):
    def _fixture(
        self,
        lanes: tuple[tuple[str, bool], ...],
        *,
        include_noise: bool = True,
    ):
        tempdir = tempfile.TemporaryDirectory()
        root = Path(tempdir.name) / "data" / "registry"
        root.mkdir(parents=True)
        for name, readme_present in lanes:
            lane = root / name
            lane.mkdir()
            if readme_present:
                (lane / "README.md").write_text(f"# {name}\n", encoding="utf-8")
            (lane / "payload.json").write_text('{"ignored":true}\n', encoding="utf-8")
        if include_noise:
            (root / "README.md").write_text("# registry\n", encoding="utf-8")
            (root / ".gitkeep").write_text("", encoding="utf-8")
            hidden = root / ".private"
            hidden.mkdir()
            (hidden / "secret.txt").write_text("ignored\n", encoding="utf-8")
        return tempdir, root

    def test_direct_lanes_are_sorted_and_payloads_are_not_projected(self) -> None:
        tempdir, root = self._fixture(
            (("sources", True), ("agriculture", True), ("source_descriptors", True))
        )
        self.addCleanup(tempdir.cleanup)
        index = build_registry_lane_discovery_index(root)
        self.assertEqual("derived_discovery_only", index["authority"])
        self.assertFalse(index["authority_created"])
        self.assertFalse(index["payloads_read"])
        self.assertFalse(index["public_readiness_inferred"])
        self.assertEqual(3, index["lane_count"])
        self.assertEqual(
            ["agriculture", "source_descriptors", "sources"],
            [item["lane"] for item in index["lanes"]],
        )
        self.assertEqual(
            [
                "data/registry/agriculture",
                "data/registry/source_descriptors",
                "data/registry/sources",
            ],
            [item["path"] for item in index["lanes"]],
        )
        self.assertNotIn("payload.json", render_index(index))
        self.assertNotIn("secret.txt", render_index(index))

    def test_readme_presence_is_discovery_metadata_only(self) -> None:
        tempdir, root = self._fixture(
            (("sources", True), ("datasets", False)), include_noise=False
        )
        self.addCleanup(tempdir.cleanup)
        index = build_registry_lane_discovery_index(root)
        by_lane = {item["lane"]: item for item in index["lanes"]}
        self.assertTrue(by_lane["sources"]["readme_present"])
        self.assertFalse(by_lane["datasets"]["readme_present"])

    def test_hidden_directories_are_excluded(self) -> None:
        tempdir, root = self._fixture((("sources", True),))
        self.addCleanup(tempdir.cleanup)
        index = build_registry_lane_discovery_index(root)
        self.assertEqual(["sources"], [item["lane"] for item in index["lanes"]])

    def test_invalid_lane_name_fails_closed(self) -> None:
        tempdir, root = self._fixture((("Bad Lane", True),), include_noise=False)
        self.addCleanup(tempdir.cleanup)
        with self.assertRaisesRegex(RegistryDiscoveryError, "unsupported registry lane"):
            build_registry_lane_discovery_index(root)

    def test_missing_registry_root_fails_closed(self) -> None:
        tempdir = tempfile.TemporaryDirectory()
        self.addCleanup(tempdir.cleanup)
        missing = Path(tempdir.name) / "data" / "registry"
        with self.assertRaisesRegex(RegistryDiscoveryError, "not a directory"):
            build_registry_lane_discovery_index(missing)

    def test_render_is_deterministic(self) -> None:
        tempdir, root = self._fixture(
            (("sources", True), ("agriculture", True)), include_noise=False
        )
        self.addCleanup(tempdir.cleanup)
        first = render_index(build_registry_lane_discovery_index(root))
        second = render_index(build_registry_lane_discovery_index(root))
        self.assertEqual(first, second)
        parsed = json.loads(first)
        self.assertEqual("kfm.registry-lane-discovery-index.v1", parsed["profile"])

    def test_cli_output_is_deterministic_json(self) -> None:
        tempdir, root = self._fixture(
            (("sources", True), ("agriculture", True)), include_noise=False
        )
        self.addCleanup(tempdir.cleanup)
        first = subprocess.run(
            [sys.executable, str(GENERATOR_PATH), "--registry-root", str(root)],
            check=False,
            capture_output=True,
            text=True,
        )
        second = subprocess.run(
            [sys.executable, str(GENERATOR_PATH), "--registry-root", str(root)],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, first.returncode)
        self.assertEqual(first.stdout, second.stdout)
        parsed = json.loads(first.stdout)
        self.assertEqual("derived_discovery_only", parsed["authority"])
        self.assertEqual("registry-root-lane-topology-only", parsed["scope"])


if __name__ == "__main__":
    unittest.main()
