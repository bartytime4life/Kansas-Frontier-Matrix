"""The connector gate entry point runs only its bounded static scanner."""

from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SOURCE = (
    Path(__file__).resolve().parents[2]
    / "tools/validators/validate_connector_gate.py"
)
SPEC = importlib.util.spec_from_file_location("kfm_connector_gate_entrypoint", SOURCE)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ConnectorGateEntrypointTests(unittest.TestCase):
    def test_static_scan_passes_allowed_source_and_denies_publish_write(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "connectors/sample/fetch.py"
            source.parent.mkdir(parents=True)
            with patch.object(MODULE, "ROOT", root):
                source.write_text(
                    'from pathlib import Path\nPath("data/raw/item").write_text("x")\n'
                )
                self.assertEqual(MODULE.scan_repository()["outcome"], "PASS")
                source.write_text(
                    'from pathlib import Path\nPath("data/published/item").write_text("x")\n'
                )
                result = MODULE.scan_repository()
                self.assertEqual(result["outcome"], "DENY")
                self.assertGreater(result["finding_count"], 0)

    def test_empty_inventory_is_error_and_cli_does_not_claim_admission(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            with patch.object(MODULE, "ROOT", Path(directory)):
                output = io.StringIO()
                with contextlib.redirect_stdout(output):
                    self.assertEqual(MODULE.main(["--scan-repository"]), 1)
        report = json.loads(output.getvalue())
        self.assertEqual(report["reason"], "CONNECTOR_SOURCE_INVENTORY_EMPTY")
        self.assertEqual(report["authority"], "NONE")
        self.assertNotIn("admission", output.getvalue())

    def test_read_failure_is_error_without_source_echo(self) -> None:
        with patch.object(MODULE, "iter_connector_source_files", side_effect=OSError):
            result = MODULE.scan_repository()
        self.assertEqual(result["outcome"], "ERROR")
        self.assertEqual(result["reason"], "CONNECTOR_SOURCE_SCAN_UNAVAILABLE")


if __name__ == "__main__":
    unittest.main()
