from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.experiments.geoparquet.generate_pyarrow_25_carriers import generate
from tools.validators.release.validate_geoparquet_2_rc_pyarrow_carriers import (
    EXPECTED_REASONS,
    validate,
)


class GeoParquet2RcPyArrowCarrierProbeTests(unittest.TestCase):
    def test_generated_carriers_validate_as_partial(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            generate(root)
            result = validate(root, root / "manifest.json")
        self.assertEqual(result.outcome, "PARTIAL")
        self.assertEqual(result.reason_codes, EXPECTED_REASONS)

    def test_tampered_carrier_digest_errors(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            generate(root)
            path = root / "synthetic-geoparquet-2.0.0-rc.1.parquet"
            path.write_bytes(path.read_bytes() + b"tamper")
            result = validate(root, root / "manifest.json")
        self.assertEqual(result.outcome, "ERROR")
        self.assertIn("CARRIER_DIGEST_MISMATCH", result.reason_codes)

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
