from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.validators.release.validate_rollback_card import (
    FIXTURE_ROOT,
    REPO_ROOT,
    SCHEMA_PATH,
    validate_rollback_card,
)


STALE_COMPATIBILITY_GUIDANCE_PATTERNS = (
    r"(?i)(?:generic|compatibility)[^\n;|]*"
    r"(?:validator|entry\s*point)[^\n;|]*\bplaceholder\b",
    r"(?i)(?=[^\n]*validate_rollback_card\.py)"
    r"(?=[^\n]*(?:\bplaceholder\b|do not use))[^\n]*",
)


class RollbackCardValidatorTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_schema_metadata_matches_reviewed_release_profile(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        self.assertEqual(
            {
                "contract_doc": "contracts/release/rollback_card.md",
                "fixtures_root": "fixtures/release/rollback_card/",
                "validator": "tools/validators/release/validate_rollback_card.py",
                "policy": "policy/release/",
                "status": "PROPOSED",
                "authority": "candidate_shape_and_local_consistency_only",
                "non_effects": [
                    "does_not_execute_rollback",
                    "does_not_authorize_release_mutation",
                    "does_not_erase_history",
                    "does_not_publish",
                ],
            },
            schema["x-kfm"],
        )

    def test_valid_fixtures_pass(self) -> None:
        files = sorted((FIXTURE_ROOT / "valid").glob("valid_*.json"))
        self.assertGreaterEqual(len(files), 3)
        for path in files:
            with self.subTest(path=path.name):
                self.assertTrue(validate_rollback_card(path).ok)

    def test_invalid_fixtures_match_reviewed_codes(self) -> None:
        lane = FIXTURE_ROOT / "invalid"
        manifest = json.loads(
            (lane / "expected_findings_manifest.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertGreaterEqual(len(manifest), 6)
        for name, expected in sorted(manifest.items()):
            with self.subTest(path=name):
                result = validate_rollback_card(lane / name)
                self.assertFalse(result.ok)
                self.assertEqual(
                    sorted(set(expected)),
                    sorted({item.code for item in result.findings}),
                )

    def test_fixture_cli_profile_passes(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                "tools/validators/release/validate_rollback_card.py",
                "--fixtures",
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn('"outcome":"PASS"', result.stdout)
        self.assertNotIn("kfm://release/example/v2", result.stdout)

    def test_compatibility_entrypoint_delegates_to_canonical_profile(self) -> None:
        canonical = subprocess.run(
            [
                sys.executable,
                "tools/validators/release/validate_rollback_card.py",
                "--fixtures",
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        compatibility = subprocess.run(
            [
                sys.executable,
                "tools/validators/validate_rollback_card.py",
                "--fixtures",
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, canonical.returncode, canonical.stdout + canonical.stderr)
        self.assertEqual(
            canonical.returncode,
            compatibility.returncode,
            compatibility.stdout + compatibility.stderr,
        )
        self.assertEqual(canonical.stdout, compatibility.stdout)
        self.assertEqual(canonical.stderr, compatibility.stderr)

    def test_operator_guidance_describes_compatibility_delegate(self) -> None:
        stale_claims_by_path = {
            "docs/runbooks/atmosphere/RELEASE_ROLLBACK_RUNBOOK.md": (
                "compatibility-looking entry point remains a placeholder",
            ),
            "docs/runbooks/atmosphere/ROLLBACK_RUNBOOK.md": (
                "generic validator entrypoint are placeholders",
                "`tools/validators/validate_rollback_card.py` raises "
                "`NotImplementedError`",
            ),
            "docs/runbooks/flora/ROLLBACK_RUNBOOK.md": (
                "generic validator entrypoint are placeholders",
                "known `NotImplementedError` placeholder",
            ),
            "docs/runbooks/archaeology/ROLLBACK_RUNBOOK.md": (
                "generic validator entrypoint are placeholders",
                "`tools/validators/validate_rollback_card.py` raises "
                "`NotImplementedError`",
            ),
            "docs/architecture/publication/ROLLBACK.md": (
                "| Generic validator entrypoint | **CONFIRMED placeholder** |",
            ),
            "docs/architecture/release-discipline.md": (),
            "docs/adr/ADR-0015-data-published-_domain_-current-alias-is-governed-by-rollback_card.md": (
                "| Generic RollbackCard entrypoint | **CONFIRMED placeholder** |",
            ),
            "packages/release/README.md": (
                "schema-declared validator is absent, while a different "
                "validator raises `NotImplementedError`",
            ),
            "packages/release/src/README.md": (
                "Schema-declared validator is absent; another validator is "
                "placeholder-only.",
                "different validator is a `NotImplementedError` placeholder",
            ),
            "policy/data/README.md": (
                "root compatibility entry point and rollback apply helper "
                "remain placeholders",
                "root shim and rollback apply helper remain placeholders",
            ),
        }

        for relative_path, stale_claims in sorted(
            stale_claims_by_path.items()
        ):
            with self.subTest(path=relative_path):
                guidance = (REPO_ROOT / relative_path).read_text(
                    encoding="utf-8"
                )
                normalized = guidance.casefold()
                self.assertIn("delegat", normalized)
                self.assertIn("canonical", normalized)
                for stale_claim in stale_claims:
                    self.assertNotIn(stale_claim, guidance)
                for stale_pattern in STALE_COMPATIBILITY_GUIDANCE_PATTERNS:
                    self.assertNotRegex(guidance, stale_pattern)

    def test_stale_operator_guidance_patterns_are_non_vacuous(self) -> None:
        stale_variants = (
            "- the generic compatibility validator remains a placeholder;",
            "- the compatibility entry point is still just a placeholder.",
            "| Generic validator shortcut | "
            "`python tools/validators/validate_rollback_card.py` | "
            "Do not use |",
        )
        for stale_variant in stale_variants:
            with self.subTest(stale_variant=stale_variant):
                self.assertTrue(
                    any(
                        re.search(pattern, stale_variant)
                        for pattern in STALE_COMPATIBILITY_GUIDANCE_PATTERNS
                    )
                )
        production_hold = "the production rollback pipeline remains a placeholder"
        self.assertFalse(
            any(
                re.search(pattern, production_hold)
                for pattern in STALE_COMPATIBILITY_GUIDANCE_PATTERNS
            )
        )

    def test_duplicate_keys_fail_closed_without_echo(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text(
                '{"object_type":"RollbackCard","object_type":"x"}',
                encoding="utf-8",
            )
            result = validate_rollback_card(path)
        self.assertEqual(
            ["JSON_DUPLICATE_KEY"],
            sorted({item.code for item in result.findings}),
        )

    def test_nonfinite_number_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nonfinite.json"
            path.write_text('{"value":NaN}', encoding="utf-8")
            result = validate_rollback_card(path)
        self.assertEqual(
            ["JSON_NONFINITE_NUMBER"],
            sorted({item.code for item in result.findings}),
        )

    def test_missing_file_fails_closed(self) -> None:
        result = validate_rollback_card(
            Path("does-not-exist-rollback-card.json")
        )
        self.assertEqual(
            ["FILE_NOT_FOUND"],
            sorted({item.code for item in result.findings}),
        )


if __name__ == "__main__":
    unittest.main()
