from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import call, patch

from tools.experiments.geoparquet import run_gdal_3_13_2_consumer_probe as probe

from tools.experiments.geoparquet.run_gdal_3_13_2_consumer_probe import (
    COORDINATES,
    GDAL_SOURCE_TAG_COMMIT,
    GEOMETRY_TYPES,
    IDS,
    IMAGE_INDEX_SHA256,
    IMAGE_PLATFORM,
    IMAGE_PLATFORM_MANIFEST_SHA256,
    IMAGE_REFERENCE,
    LABELS,
    PARTIAL_REASONS,
    PROFILE,
    PYARROW_WHEEL_SHA256,
    SCOPE,
    SOURCE_PROFILE,
    _summary,
)
from tools.validators.release.validate_geoparquet_2_rc_gdal_consumer_probe import (
    validate,
)

EMPTY_SHA256 = "sha256:" + hashlib.sha256(b"").hexdigest()


def _digest(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def _command(path: str) -> list[str]:
    return [
        "docker",
        "run",
        "--network",
        "none",
        "--read-only",
        "--cap-drop",
        "ALL",
        "--security-opt",
        "no-new-privileges",
        IMAGE_REFERENCE,
        "ogr2ogr",
        "-t_srs",
        "OGC:CRS84",
        f"/probe/{path}",
    ]


def _write_packet(root: Path) -> tuple[Path, dict[str, object]]:
    baseline_path = root / "synthetic-geoparquet-1.1.0.parquet"
    candidate_path = root / "synthetic-geoparquet-2.0.0-rc.1.parquet"
    baseline_path.write_bytes(b"synthetic-1.1")
    candidate_path.write_bytes(b"synthetic-2.0-rc")
    crs = {"id": {"authority": "OGC", "code": "CRS84"}}
    source = {
        "profile": SOURCE_PROFILE,
        "outcome": "PARTIAL",
        "declared_default": "1.1.0",
        "candidate_version": "2.0.0-rc.1",
        "toolchain": {
            "pyarrow": "25.0.0",
            "wheel_sha256": PYARROW_WHEEL_SHA256,
        },
        "carriers": {
            "geoparquet_1_1": {
                "path": baseline_path.name,
                "sha256": _digest(baseline_path),
                "geometry_column": {
                    "physical_type": "BYTE_ARRAY",
                    "logical_type": "None",
                },
                "geo_metadata": {"columns": {"geometry": {"crs": crs}}},
            },
            "geoparquet_2_rc_geometry": {
                "path": candidate_path.name,
                "sha256": _digest(candidate_path),
                "geometry_column": {
                    "physical_type": "BYTE_ARRAY",
                    "logical_type": "Geometry(crs=)",
                },
                "geo_metadata": {"columns": {"geometry": {"crs": crs}}},
            },
        },
    }
    source_path = root / "manifest.json"
    source_path.write_text(json.dumps(source, sort_keys=True) + "\n", encoding="utf-8")

    carriers = {}
    for key, entry in source["carriers"].items():
        carriers[key] = {
            "path": entry["path"],
            "sha256": entry["sha256"],
            "command": _command(entry["path"]),
            "read_status": "PASS",
            "row_count": 4,
            "feature_ids": IDS,
            "labels": LABELS,
            "geometry_types": GEOMETRY_TYPES,
            "coordinates": COORDINATES,
            "stdout_sha256": EMPTY_SHA256,
            "stderr_sha256": EMPTY_SHA256,
        }
    packet = {
        "profile": PROFILE,
        "declared_default": "1.1.0",
        "candidate_version": "2.0.0-rc.1",
        "scope": SCOPE,
        "source_carrier_manifest": {
            "path": "manifest.json",
            "sha256": _digest(source_path),
            "profile": SOURCE_PROFILE,
            "outcome": "PARTIAL",
        },
        "toolchain": {
            "gdal": "3.13.2",
            "gdal_version_output": "GDAL 3.13.2 \"Iowa City\", released 2026/07/20",
            "gdal_source_tag_commit": GDAL_SOURCE_TAG_COMMIT,
            "image_reference": IMAGE_REFERENCE,
            "image_index_sha256": IMAGE_INDEX_SHA256,
            "image_platform": IMAGE_PLATFORM,
            "image_platform_manifest_sha256": IMAGE_PLATFORM_MANIFEST_SHA256,
            "image_id": "sha256:" + "1" * 64,
            "repo_digests": ["ghcr.io/osgeo/gdal@" + IMAGE_INDEX_SHA256],
        },
        "carriers": carriers,
        "checks": {
            "gdal_distribution_authenticated": "PASS",
            "parquet_driver": "PASS",
            "legacy_1_1_consumer_read": "PASS",
            "rc_geometry_consumer_read": "PASS",
            "crs84_same_crs_transform": "PASS",
            "pyarrow_to_gdal_consumer_read": "PASS",
            "gdal_producer_route": "NOT_RUN",
            "geospatial_row_group_pruning": "NOT_RUN",
        },
        "outcome": "PARTIAL",
        "reason_codes": list(PARTIAL_REASONS),
        "governance": {
            "default_changed": False,
            "adoption_authorized": False,
            "migration_authorized": False,
            "release_authorized": False,
            "deployment_authorized": False,
            "publication_authorized": False,
        },
    }
    packet_path = root / "gdal-consumer.json"
    packet_path.write_text(json.dumps(packet, sort_keys=True) + "\n", encoding="utf-8")
    return packet_path, packet


class GeoParquet2RcGdalConsumerProbeTests(unittest.TestCase):
    def test_runner_summarizes_exact_geojson_as_pass(self) -> None:
        features = []
        for feature_id, label, geometry_type, coordinates in zip(
            IDS, LABELS, GEOMETRY_TYPES, COORDINATES
        ):
            geometry = (
                None
                if geometry_type is None
                else {"type": geometry_type, "coordinates": coordinates}
            )
            features.append(
                {
                    "type": "Feature",
                    "properties": {"feature_id": feature_id, "label": label},
                    "geometry": geometry,
                }
            )
        completed = subprocess.CompletedProcess(
            args=["ogr2ogr"],
            returncode=0,
            stdout=json.dumps({"type": "FeatureCollection", "features": features}),
            stderr="",
        )
        entry = {"path": "carrier.parquet", "sha256": "sha256:" + "1" * 64}
        result = _summary(entry, _command("carrier.parquet"), completed)
        self.assertEqual(result["read_status"], "PASS")
        self.assertEqual(result["feature_ids"], IDS)

    def test_runner_classifies_nonzero_read_as_not_supported(self) -> None:
        completed = subprocess.CompletedProcess(
            args=["ogr2ogr"], returncode=1, stdout="", stderr="unsupported"
        )
        entry = {"path": "carrier.parquet", "sha256": "sha256:" + "1" * 64}
        result = _summary(entry, _command("carrier.parquet"), completed)
        self.assertEqual(result["read_status"], "NOT_SUPPORTED")

    def test_exact_partial_packet_validates(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            packet_path, _ = _write_packet(root)
            result = validate(root, packet_path)
        self.assertEqual(result.outcome, "PARTIAL")
        self.assertEqual(result.reason_codes, PARTIAL_REASONS)

    def test_explicit_rc_not_supported_is_hold(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            packet_path, packet = _write_packet(root)
            entry = packet["carriers"]["geoparquet_2_rc_geometry"]
            entry.update(
                {
                    "read_status": "NOT_SUPPORTED",
                    "row_count": None,
                    "feature_ids": [],
                    "labels": [],
                    "geometry_types": [],
                    "coordinates": [],
                }
            )
            packet["checks"].update(
                {
                    "rc_geometry_consumer_read": "NOT_SUPPORTED",
                    "crs84_same_crs_transform": "NOT_SUPPORTED",
                    "pyarrow_to_gdal_consumer_read": "NOT_SUPPORTED",
                }
            )
            packet["outcome"] = "HOLD"
            packet["reason_codes"] = [
                *PARTIAL_REASONS,
                "GDAL_2_RC_GEOMETRY_READ_NOT_SUPPORTED",
            ]
            packet_path.write_text(json.dumps(packet, sort_keys=True) + "\n", encoding="utf-8")
            result = validate(root, packet_path)
        self.assertEqual(result.outcome, "HOLD")
        self.assertIn("GDAL_2_RC_GEOMETRY_READ_NOT_SUPPORTED", result.reason_codes)

    def test_tampered_carrier_digest_errors(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            packet_path, _ = _write_packet(root)
            (root / "synthetic-geoparquet-2.0.0-rc.1.parquet").write_bytes(b"tamper")
            result = validate(root, packet_path)
        self.assertEqual(result.outcome, "ERROR")
        self.assertIn("CARRIER_DIGEST_MISMATCH", result.reason_codes)

    def test_symlinked_source_carrier_path_errors(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            packet_path, _ = _write_packet(root)
            candidate = root / "synthetic-geoparquet-2.0.0-rc.1.parquet"
            target = root / "redirected-carrier.parquet"
            target.write_bytes(candidate.read_bytes())
            candidate.unlink()
            try:
                candidate.symlink_to(target)
            except OSError:
                self.skipTest("symlinks unavailable")
            result = validate(root, packet_path)
        self.assertEqual(result.outcome, "ERROR")
        self.assertIn("SOURCE_CARRIER_PATH_INVALID", result.reason_codes)

    def test_success_with_changed_semantics_fails_validation(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            packet_path, packet = _write_packet(root)
            packet["carriers"]["geoparquet_1_1"]["feature_ids"] = [1, 2, 4, 3]
            packet_path.write_text(json.dumps(packet, sort_keys=True) + "\n", encoding="utf-8")
            result = validate(root, packet_path)
        self.assertEqual(result.outcome, "ERROR")
        self.assertIn("GDAL_CONSUMER_SEMANTIC_MISMATCH", result.reason_codes)

    def test_image_substitution_errors(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            packet_path, packet = _write_packet(root)
            packet["toolchain"]["image_reference"] = "ghcr.io/example/substitute@sha256:" + "0" * 64
            packet_path.write_text(json.dumps(packet, sort_keys=True) + "\n", encoding="utf-8")
            result = validate(root, packet_path)
        self.assertEqual(result.outcome, "ERROR")
        self.assertIn("GDAL_IMAGE_IDENTITY_MISMATCH", result.reason_codes)

    def test_governance_or_interoperable_claim_errors(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            packet_path, packet = _write_packet(root)
            packet["governance"]["adoption_authorized"] = True
            packet["outcome"] = "INTEROPERABLE_CANDIDATE"
            packet_path.write_text(json.dumps(packet, sort_keys=True) + "\n", encoding="utf-8")
            result = validate(root, packet_path)
        self.assertEqual(result.outcome, "ERROR")
        self.assertIn("GOVERNANCE_BOUNDARY_VIOLATION", result.reason_codes)
        self.assertIn("DECLARED_OUTCOME_MISMATCH", result.reason_codes)


class GdalImageAcquisitionTests(unittest.TestCase):
    header_timeout = (
        'Error response from daemon: Get "https://ghcr.io/v2/": '
        "net/http: request canceled while waiting for connection "
        "(Client.Timeout exceeded while awaiting headers)\n"
    )

    def setUp(self) -> None:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.command = ["docker", "pull", "--platform", IMAGE_PLATFORM, IMAGE_REFERENCE]

    def completed(self, code: int = 0, stderr: str = "", stdout: str = ""):
        return subprocess.CompletedProcess(self.command, code, stdout, stderr)

    def attempts(self):
        return json.loads((self.root / "gdal-image-pull-attempts.json").read_text())

    def test_command_deadline_terminates_a_synthetic_child(self) -> None:
        with self.assertRaises(subprocess.TimeoutExpired):
            probe._run([sys.executable, "-c", "import time; time.sleep(3)"], timeout=1)

    def test_success_needs_one_bounded_attempt(self) -> None:
        with patch.object(probe, "_run", return_value=self.completed()) as execute:
            with patch("time.sleep") as sleep:
                result = probe._pull_image(self.root)
        self.assertEqual(result.returncode, 0)
        execute.assert_called_once_with(self.command, timeout=120)
        sleep.assert_not_called()
        self.assertEqual(len(self.attempts()), 1)
        self.assertFalse(self.attempts()[0]["retry_scheduled"])

    def test_header_timeout_recovers_without_erasing_original_logs(self) -> None:
        results = [self.completed(1, self.header_timeout), self.completed(stdout="acquired")]
        with patch.object(probe, "_run", side_effect=results) as execute:
            with patch("time.sleep") as sleep:
                result = probe._pull_image(self.root)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(execute.call_args_list, [call(self.command, timeout=120)] * 2)
        sleep.assert_called_once_with(2)
        attempts = self.attempts()
        self.assertEqual([a["returncode"] for a in attempts], [1, 0])
        self.assertEqual([a["retry_scheduled"] for a in attempts], [True, False])
        for attempt in attempts:
            for stream in ("stdout", "stderr"):
                path = self.root / attempt[stream + "_path"]
                self.assertEqual(_digest(path), attempt[stream + "_sha256"])
        self.assertEqual(
            (self.root / attempts[0]["stderr_path"]).read_text(), self.header_timeout
        )
        self.assertEqual((self.root / "gdal-image-pull.stdout.txt").read_text(), "acquired")
        self.assertEqual((self.root / "gdal-image-pull.stderr.txt").read_text(), "")

    def test_repeated_transport_timeouts_stop_after_three_attempts(self) -> None:
        with patch.object(
            probe, "_run", return_value=self.completed(1, self.header_timeout)
        ) as execute:
            with patch("time.sleep") as sleep:
                result = probe._pull_image(self.root)
        self.assertEqual(result.returncode, 1)
        self.assertEqual(execute.call_count, 3)
        self.assertEqual(sleep.call_args_list, [call(2), call(4)])
        self.assertEqual(len(self.attempts()), 3)
        self.assertFalse(self.attempts()[-1]["retry_scheduled"])

    def test_subprocess_timeout_retains_partial_output_before_recovery(self) -> None:
        timeout = subprocess.TimeoutExpired(
            self.command, 120, output=b"partial\xff", stderr=b"slow"
        )
        with patch.object(probe, "_run", side_effect=[timeout, self.completed()]):
            with patch("time.sleep"):
                result = probe._pull_image(self.root)
        self.assertEqual(result.returncode, 0)
        first = self.attempts()[0]
        self.assertEqual(first["returncode"], 124)
        self.assertTrue(first["timed_out"])
        self.assertEqual((self.root / first["stdout_path"]).read_text(), "partial\ufffd")
        self.assertIn(
            "exceeded 120 seconds", (self.root / first["stderr_path"]).read_text()
        )

    def test_non_timeout_errors_stop_without_retry(self) -> None:
        for message in ("unauthorized", "manifest unknown", "digest mismatch", "unknown error"):
            with self.subTest(message=message):
                with patch.object(
                    probe, "_run", return_value=self.completed(1, message)
                ) as execute:
                    with patch("time.sleep") as sleep:
                        result = probe._pull_image(self.root)
                self.assertEqual(result.returncode, 1)
                execute.assert_called_once_with(self.command, timeout=120)
                sleep.assert_not_called()
                self.assertFalse(self.attempts()[0]["retryable"])

    def test_acquisition_exhaustion_stays_error_and_nonzero_cli_exit(self) -> None:
        _write_packet(self.root)
        output = self.root / "consumer"
        with patch.object(
            probe, "_run", return_value=self.completed(1, self.header_timeout)
        ) as execute:
            with patch("time.sleep"), patch("builtins.print"):
                status = probe.main([
                    "--root", str(self.root), "--manifest", str(self.root / "manifest.json"),
                    "--output", str(output),
                ])
        self.assertEqual(status, 1)
        self.assertEqual(execute.call_count, 3)
        result = json.loads((output / "manifest.json").read_text())
        self.assertEqual(result["outcome"], "ERROR")
        self.assertEqual(result["reason_codes"], ["GDAL_IMAGE_UNAVAILABLE"])
        self.assertEqual(result["checks"]["gdal_distribution_authenticated"], "ERROR")
        self.assertTrue(all(value is False for value in result["governance"].values()))

    def test_recovered_pull_does_not_retry_image_identity_mismatch(self) -> None:
        _write_packet(self.root)
        bad_identity = self.completed(
            stdout=json.dumps([
                {"Id": "sha256:" + "1" * 64, "Architecture": "arm64", "Os": "linux"}
            ])
        )
        with patch.object(
            probe, "_run",
            side_effect=[self.completed(1, self.header_timeout), self.completed(), bad_identity],
        ) as execute:
            with patch("time.sleep") as sleep:
                result = probe.run(self.root, self.root / "manifest.json", self.root / "consumer")
        self.assertEqual(result["outcome"], "ERROR")
        self.assertEqual(result["reason_codes"], ["GDAL_IMAGE_IDENTITY_MISMATCH"])
        self.assertEqual(execute.call_count, 3)
        sleep.assert_called_once_with(2)

    def test_recovered_pull_does_not_retry_semantic_failure(self) -> None:
        _write_packet(self.root)
        image = {
            "Id": "sha256:" + "1" * 64,
            "Architecture": "amd64",
            "Os": "linux",
            "RepoDigests": ["ghcr.io/osgeo/gdal@" + IMAGE_INDEX_SHA256],
        }
        results = [
            self.completed(1, self.header_timeout), self.completed(),
            self.completed(stdout=json.dumps([image])), self.completed(stdout="GDAL 3.13.2"),
            self.completed(stdout="Parquet -vector-"),
            self.completed(stdout='{"type":"FeatureCollection","features":[]}'),
            self.completed(stdout='{"type":"FeatureCollection","features":[]}'),
        ]
        with patch.object(probe, "_run", side_effect=results) as execute:
            with patch("time.sleep") as sleep:
                result = probe.run(self.root, self.root / "manifest.json", self.root / "consumer")
        self.assertEqual(result["outcome"], "FAIL")
        self.assertEqual(result["checks"]["pyarrow_to_gdal_consumer_read"], "FAIL")
        self.assertEqual(execute.call_count, 7)
        sleep.assert_called_once_with(2)


if __name__ == "__main__":
    unittest.main()
