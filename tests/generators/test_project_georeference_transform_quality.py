from __future__ import annotations

import copy
import importlib.util
import io
import json
import socket
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "tools/generators/project_georeference_transform_quality.py"
SPEC = importlib.util.spec_from_file_location(
    "project_georeference_transform_quality", MODULE_PATH
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

CONTROL_SET = ROOT / "fixtures/contracts/v1/map/georeference_control_point_set/valid.json"
REQUEST = ROOT / "fixtures/contracts/v1/map/georeference_transform_quality/projection_request.json"


class GeoreferenceTransformQualityProjectionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.control_set = MODULE.read_json_object(CONTROL_SET)
        self.request = MODULE.read_json_object(REQUEST)

    def test_projection_is_deterministic_and_quality_valid(self) -> None:
        first = MODULE.project(self.control_set, self.request)
        second = MODULE.project(self.control_set, self.request)
        self.assertEqual(first, second)
        result = MODULE.quality_validator.validate_candidate(
            first["transform_quality_candidate"]
        )
        self.assertEqual("READY", result.outcome)

    def test_projection_preserves_identity_and_exact_point_order(self) -> None:
        result = MODULE.project(self.control_set, self.request)
        self.assertEqual(
            {
                "resource_set_hash": self.control_set["resource_set_hash"],
                "set_id": self.control_set["set_id"],
                "target_set_hash": self.control_set["target_set_hash"],
            },
            result["source_control_point_set"],
        )
        candidate = result["transform_quality_candidate"]
        self.assertEqual(self.control_set["control_points"], candidate["gcps"])
        self.assertEqual(self.control_set["control_point_count"], candidate["gcp_count"])
        self.assertEqual(self.control_set["target_space"]["unit"], candidate["target_unit"])

    def test_invalid_control_point_identity_fails_closed(self) -> None:
        control_set = copy.deepcopy(self.control_set)
        control_set["resource_set_hash"] = "sha256:" + "1" * 64
        with self.assertRaisesRegex(MODULE.ProjectionFailure, "CONTROL_POINT_SET_INVALID"):
            MODULE.project(control_set, self.request)

    def test_invalid_threshold_posture_fails_closed(self) -> None:
        request = copy.deepcopy(self.request)
        request["thresholds"]["minimum_gcps"] = 3
        with self.assertRaisesRegex(MODULE.ProjectionFailure, "MINIMUM_GCPS_INVALID"):
            MODULE.project(self.control_set, request)

    def test_default_cli_writes_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "projection.json"
            stream = io.StringIO()
            with redirect_stdout(stream):
                code = MODULE.main([str(CONTROL_SET), str(REQUEST)])
            self.assertEqual(0, code)
            self.assertFalse(output.exists())
            self.assertEqual(
                "GeoreferenceTransformQualityProjection",
                json.loads(stream.getvalue())["object_type"],
            )

    def test_explicit_write_and_overwrite_guard(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "projection.json"
            self.assertEqual(
                0,
                MODULE.main(
                    [str(CONTROL_SET), str(REQUEST), "--write", str(output)]
                ),
            )
            first = output.read_bytes()
            self.assertEqual(
                2,
                MODULE.main(
                    [str(CONTROL_SET), str(REQUEST), "--write", str(output)]
                ),
            )
            self.assertEqual(first, output.read_bytes())
            self.assertEqual(
                0,
                MODULE.main(
                    [
                        str(CONTROL_SET),
                        str(REQUEST),
                        "--write",
                        str(output),
                        "--force",
                    ]
                ),
            )
            self.assertEqual(first, output.read_bytes())

    def test_projection_does_not_open_network(self) -> None:
        def denied(*_args: object, **_kwargs: object) -> None:
            raise AssertionError("network access denied")

        with mock.patch.object(socket, "socket", denied), mock.patch.object(
            socket, "create_connection", denied
        ), mock.patch.object(socket, "getaddrinfo", denied):
            result = MODULE.project(self.control_set, self.request)
            self.assertTrue(all(
                value is False or value is None
                for value in result["governance"].values()
            ))


if __name__ == "__main__":
    unittest.main()
