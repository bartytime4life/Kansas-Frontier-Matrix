import json
import unittest
from pathlib import PurePosixPath, PureWindowsPath
from unittest.mock import MagicMock, patch

from tests.subprocess_utils import assert_python_ok
from tools import check_no_public_internal_paths as checker


class NoPublicInternalPathsTests(unittest.TestCase):
    def check_fixture(self, path, metadata):
        fixture = MagicMock()
        fixture.parts = path.parts
        fixture.__str__.return_value = str(path)
        fixture.read_text.return_value = json.dumps({
            "geometry": {"type": "Point", "coordinates": [0, 0]},
            **metadata,
        })
        with patch.object(checker, "Path") as root, patch("builtins.print") as output:
            root.return_value.rglob.return_value = [fixture]
            result = checker.main()
        return result, output.call_args.args

    def test_hydrology_geometry_exemption_is_portable(self):
        for path_type in (PurePosixPath, PureWindowsPath):
            for metadata in ({"sensitivity": "PUBLIC_SAFE"}, {"knowledge_character": "SYNTHETIC_TEST"}):
                with self.subTest(path_type=path_type, metadata=metadata):
                    result, output = self.check_fixture(
                        path_type("fixtures/domains/hydrology/hydrology_feature.valid.json"), metadata
                    )
                    self.assertEqual(result, 0)
                    self.assertEqual(output[0], "PASS")

    def test_nonexempt_precise_geometry_is_rejected(self):
        for path_type in (PurePosixPath, PureWindowsPath):
            for lane, metadata in (
                ("hydrology", {}),
                ("hydrology", {"sensitivity": "UNKNOWN"}),
                ("soil", {"sensitivity": "PUBLIC_SAFE"}),
                ("soil", {"knowledge_character": "SYNTHETIC_TEST"}),
                ("hydrology-extra", {"sensitivity": "PUBLIC_SAFE"}),
            ):
                with self.subTest(path_type=path_type, lane=lane, metadata=metadata):
                    result, output = self.check_fixture(
                        path_type(f"fixtures/domains/{lane}/feature.valid.json"), metadata
                    )
                    self.assertEqual(result, 1)
                    self.assertTrue(any("precise geometry cannot be public fixture" in v for v in output[1]))

    def test_synthetic_hydrology_does_not_override_restricted_sensitivity(self):
        for path_type in (PurePosixPath, PureWindowsPath):
            for sensitivity in ("RESTRICTED", "STEWARD_ONLY"):
                with self.subTest(path_type=path_type, sensitivity=sensitivity):
                    result, output = self.check_fixture(
                        path_type("fixtures/domains/hydrology/feature.valid.json"),
                        {"sensitivity": sensitivity, "knowledge_character": "SYNTHETIC_TEST"},
                    )
                    self.assertEqual(result, 1)
                    self.assertTrue(any("restricted sensitivity cannot be public fixture" in v for v in output[1]))

    def test_check_no_public_internal_paths(self):
        assert_python_ok(self, ["tools/check_no_public_internal_paths.py"])
