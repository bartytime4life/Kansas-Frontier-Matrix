from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
SCRIPT = ROOT / "tools/validators/domains/people-dna-land/validate_schema.py"


class PeopleDnaLandSchemaValidatorTests(unittest.TestCase):
    def run_validator(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_canonical_domain_schemas_are_structurally_valid(self) -> None:
        result = self.run_validator()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("OK ", result.stdout)

    def test_invalid_draft_2020_12_schema_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "invalid.schema.json"
            path.write_text(
                json.dumps(
                    {
                        "$schema": "https://json-schema.org/draft/2020-12/schema",
                        "type": 17,
                    }
                ),
                encoding="utf-8",
            )
            result = self.run_validator(str(path))

        self.assertEqual(result.returncode, 1)
        self.assertIn("FAIL ", result.stdout)

    def test_symlinked_schema_path_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            target = root / "target.schema.json"
            target.write_text(
                '{"$schema":"https://json-schema.org/draft/2020-12/schema"}',
                encoding="utf-8",
            )
            path = root / "linked.schema.json"
            path.symlink_to(target)
            result = self.run_validator(str(path))

        self.assertEqual(result.returncode, 1)
        self.assertIn(
            "schema path must be a regular non-symlink file",
            result.stdout,
        )

    def test_schema_below_symlinked_directory_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            target_dir = root / "target"
            target_dir.mkdir()
            target = target_dir / "target.schema.json"
            target.write_text(
                '{"$schema":"https://json-schema.org/draft/2020-12/schema"}',
                encoding="utf-8",
            )
            linked_dir = root / "linked"
            linked_dir.symlink_to(target_dir, target_is_directory=True)
            result = self.run_validator(str(linked_dir / target.name))

        self.assertEqual(result.returncode, 1)
        self.assertIn(
            "schema path must be a regular non-symlink file",
            result.stdout,
        )

    def test_oversized_schema_fails_before_parsing(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "oversized.schema.json"
            path.write_bytes(b" " * ((2 * 1024 * 1024) + 1))
            result = self.run_validator(str(path))

        self.assertEqual(result.returncode, 1)
        self.assertIn(
            "schema exceeds maximum size of 2097152 bytes",
            result.stdout,
        )

    def test_duplicate_json_member_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "duplicate.schema.json"
            path.write_text(
                '{"$schema":"https://json-schema.org/draft/2020-12/schema",'
                '"type":"object","type":"string"}',
                encoding="utf-8",
            )
            result = self.run_validator(str(path))

        self.assertEqual(result.returncode, 1)
        self.assertIn("duplicate JSON object key: type", result.stdout)


if __name__ == "__main__":
    unittest.main()
