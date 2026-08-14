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
MODULE_PATH = ROOT / "tools/generators/project_georeference_spatial_distribution.py"
SPEC = importlib.util.spec_from_file_location(
    "project_georeference_spatial_distribution", MODULE_PATH
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

CONTROL_SET = ROOT / "fixtures/contracts/v1/map/georeference_control_point_set/valid.json"
REQUEST = ROOT / "fixtures/contracts/v1/map/georeference_spatial_distribution/projection_request.json"


class GeoreferenceSpatialDistributionProjectionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.control_set = MODULE.read_json_object(CONTROL_SET)
        self.request = MODULE.read_json_object(REQUEST)

    def test_projection_is_deterministic_and_spatial_candidate_valid(self) -> None:
        first = MODULE.project(self.control_set, self.request)
        second = MODULE.project(self.control_set, self.request)
        self.assertEqual(first, second)
        result = MODULE.spatial_validator.validate_candidate(
            first["spatial_distribution_candidate"]
        )
        self.assertEqual("READY", result.outcome)

    def test_projection_binds_resource_identity_and_exact_resource_points(self) -> None:
        result = MODULE.project(self.control_set, self.request)
        self.assertEqual(
            {"resource_set_hash": self.control_set["resource_set_hash"]},
            result["source_control_point_set"],
        )
        candidate = result["spatial_distribution_candidate"]
        expected_points = [
            {"id": point["id"], "resource": point["resource"]}
            for point in self.control_set["control_points"]
        ]
        self.assertEqual(expected_points, candidate["gcps"])
        self.assertEqual(self.control_set["control_point_count"], candidate["gcp_count"])
        self.assertEqual(
            {
                "resource_height_px": self.control_set["resource_space"]["height_px"],
                "resource_mask": self.request["resource_mask"],
                "resource_width_px": self.control_set["resource_space"]["width_px"],
            },
            candidate["support"],
        )

    def test_target_only_change_does_not_change_resource_projection(self) -> None:
        changed = copy.deepcopy(self.control_set)
        changed["control_points"][0]["target"] = [226, 263.5]
        set_id, resource_hash, target_hash = MODULE.set_validator.identity(changed)
        changed["set_id"] = set_id
        changed["resource_set_hash"] = resource_hash
        changed["target_set_hash"] = target_hash
        self.assertEqual("VALID", MODULE.set_validator.validate_candidate(changed).outcome)
        self.assertEqual(
            MODULE.project(self.control_set, self.request),
            MODULE.project(changed, self.request),
        )

    def test_invalid_resource_identity_fails_closed(self) -> None:
        control_set = copy.deepcopy(self.control_set)
        control_set["resource_set_hash"] = "sha256:" + "1" * 64
        with self.assertRaisesRegex(MODULE.ProjectionFailure, "CONTROL_POINT_SET_INVALID"):
            MODULE.project(control_set, self.request)

    def test_invalid_threshold_posture_fails_closed(self) -> None:
        request = copy.deepcopy(self.request)
        request["thresholds"]["minimum_gcps"] = 3
        with self.assertRaisesRegex(MODULE.ProjectionFailure, "MINIMUM_GCPS_INVALID"):
            MODULE.project(self.control_set, request)

    def test_invalid_resource_mask_fails_closed(self) -> None:
        request = copy.deepcopy(self.request)
        request["resource_mask"][4] = [0, 100]
        with self.assertRaisesRegex(MODULE.ProjectionFailure, "SPATIAL_COMPUTATION_INVALID"):
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
                "GeoreferenceSpatialDistributionProjection",
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
            self.assertTrue(
                all(
                    value is False or value is None
                    for value in result["governance"].values()
                )
            )


if __name__ == "__main__":
    unittest.main()
