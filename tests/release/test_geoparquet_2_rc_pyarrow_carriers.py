from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import pyarrow.parquet as pq

from tools.experiments.geoparquet.generate_pyarrow_25_carriers import _write, generate
from tools.validators.release.validate_geoparquet_2_rc_pyarrow_carriers import (
    EXPECTED_REASONS,
    ROOT,
    validate,
)


CARRIERS = (
    "synthetic-geoparquet-1.1.0.parquet",
    "synthetic-geoparquet-2.0.0-rc.1.parquet",
)


def _rebind_carrier(root: Path, name: str) -> None:
    manifest_path = root / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    path = root / name
    entry = next(
        item for item in manifest["carriers"].values() if item["path"] == name
    )
    entry["sha256"] = f"sha256:{hashlib.sha256(path.read_bytes()).hexdigest()}"
    entry["size_bytes"] = path.stat().st_size
    manifest_path.write_text(json.dumps(manifest) + "\n", encoding="utf-8")


class GeoParquet2RcPyArrowCarrierProbeTests(unittest.TestCase):
    def test_generated_carriers_validate_as_partial(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            generate(root)
            result = validate(root, root / "manifest.json")
        self.assertEqual(result.outcome, "PARTIAL")
        self.assertEqual(result.reason_codes, EXPECTED_REASONS)

    def test_readable_carriers_with_missing_columns_error(self) -> None:
        for carrier in CARRIERS:
            for column in ("geometry", "feature_id"):
                with (
                    self.subTest(carrier=carrier, column=column),
                    tempfile.TemporaryDirectory() as temp,
                ):
                    root = Path(temp)
                    generate(root)
                    path = root / carrier
                    _write(pq.read_table(path).drop([column]), path)
                    _rebind_carrier(root, carrier)
                    self.assertNotIn(column, pq.ParquetFile(path).schema.names)
                    result = validate(root, root / "manifest.json")
                    self.assertEqual(result.outcome, "ERROR")
                    self.assertIn("CARRIER_UNREADABLE", result.reason_codes)

    def test_readable_carriers_with_malformed_metadata_error(self) -> None:
        cases = {
            "absent": None,
            "invalid_utf8": b"\xff",
            "invalid_json": b"{",
            "non_object": b"[]",
            "missing_columns": b"{}",
            "invalid_columns": b'{"columns":null}',
            "missing_geometry": b'{"columns":{}}',
            "invalid_geometry": b'{"columns":{"geometry":null}}',
        }
        for carrier in CARRIERS:
            for label, geo in cases.items():
                with (
                    self.subTest(carrier=carrier, metadata=label),
                    tempfile.TemporaryDirectory() as temp,
                ):
                    root = Path(temp)
                    generate(root)
                    path = root / carrier
                    table = pq.read_table(path)
                    metadata = dict(table.schema.metadata or {})
                    if geo is None:
                        metadata.pop(b"geo")
                    else:
                        metadata[b"geo"] = geo
                    _write(table.replace_schema_metadata(metadata), path)
                    _rebind_carrier(root, carrier)
                    self.assertEqual(pq.ParquetFile(path).metadata.num_rows, 4)
                    result = validate(root, root / "manifest.json")
                    self.assertEqual(result.outcome, "ERROR")
                    self.assertIn("CARRIER_UNREADABLE", result.reason_codes)

    def test_truncated_carriers_error(self) -> None:
        for carrier in CARRIERS:
            with (
                self.subTest(carrier=carrier),
                tempfile.TemporaryDirectory() as temp,
            ):
                root = Path(temp)
                generate(root)
                path = root / carrier
                path.write_bytes(path.read_bytes()[:100])
                _rebind_carrier(root, carrier)
                result = validate(root, root / "manifest.json")
                self.assertEqual(result.outcome, "ERROR")
                self.assertEqual(result.reason_codes, ("CARRIER_UNREADABLE",))

    def test_carrier_shape_error_preserves_digest_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            generate(root)
            path = root / "synthetic-geoparquet-1.1.0.parquet"
            _write(pq.read_table(path).drop(["geometry"]), path)
            result = validate(root, root / "manifest.json")
        self.assertEqual(result.outcome, "ERROR")
        self.assertEqual(
            result.reason_codes, ("CARRIER_DIGEST_MISMATCH", "CARRIER_UNREADABLE")
        )

    def test_malformed_carrier_cli_emits_finite_json_without_traceback(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            generate(root)
            path = root / "synthetic-geoparquet-1.1.0.parquet"
            _write(pq.read_table(path).drop(["geometry"]), path)
            _rebind_carrier(root, path.name)
            completed = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "tools/validators/release/validate_geoparquet_2_rc_pyarrow_carriers.py"),
                    "--root", str(root),
                    "--manifest", str(root / "manifest.json"),
                ],
                capture_output=True,
                text=True,
                check=False,
                timeout=30,
            )
        self.assertEqual(completed.returncode, 1)
        self.assertEqual(completed.stderr, "")
        self.assertEqual(
            json.loads(completed.stdout),
            {"outcome": "ERROR", "reason_codes": ["CARRIER_UNREADABLE"]},
        )

    def test_tampered_carrier_digest_errors(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            generate(root)
            path = root / "synthetic-geoparquet-2.0.0-rc.1.parquet"
            path.write_bytes(path.read_bytes() + b"tamper")
            result = validate(root, root / "manifest.json")
        self.assertEqual(result.outcome, "ERROR")
        self.assertIn("CARRIER_DIGEST_MISMATCH", result.reason_codes)

    def test_symlinked_carrier_path_errors_without_following_target(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            generate(root)
            candidate = root / "synthetic-geoparquet-2.0.0-rc.1.parquet"
            target = root / "redirected-carrier.parquet"
            target.write_bytes(candidate.read_bytes())
            candidate.unlink()
            try:
                candidate.symlink_to(target)
            except OSError:
                self.skipTest("symlinks unavailable")
            result = validate(root, root / "manifest.json")
        self.assertEqual(result.outcome, "ERROR")
        self.assertIn("CARRIER_PATH_INVALID", result.reason_codes)

    def test_governance_claim_errors(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manifest = generate(root)
            manifest["governance"]["adoption_authorized"] = True
            (root / "manifest.json").write_text(
                json.dumps(manifest, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            result = validate(root, root / "manifest.json")
        self.assertEqual(result.outcome, "ERROR")
        self.assertIn("GOVERNANCE_BOUNDARY_VIOLATION", result.reason_codes)

    def test_declared_interoperable_outcome_errors(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manifest = generate(root)
            manifest["outcome"] = "INTEROPERABLE_CANDIDATE"
            (root / "manifest.json").write_text(
                json.dumps(manifest, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            result = validate(root, root / "manifest.json")
        self.assertEqual(result.outcome, "ERROR")
        self.assertIn("DECLARED_OUTCOME_MISMATCH", result.reason_codes)

    def test_crs_declaration_conflict_errors(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manifest = generate(root)
            manifest["carriers"]["geoparquet_2_rc_geometry"]["geo_metadata"][
                "columns"
            ]["geometry"]["crs"] = {
                "id": {"authority": "EPSG", "code": 3857}
            }
            (root / "manifest.json").write_text(
                json.dumps(manifest, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            result = validate(root, root / "manifest.json")
        self.assertEqual(result.outcome, "ERROR")
        self.assertIn(
            "CARRIER_METADATA_DECLARATION_MISMATCH", result.reason_codes
        )


if __name__ == "__main__":
    unittest.main()
