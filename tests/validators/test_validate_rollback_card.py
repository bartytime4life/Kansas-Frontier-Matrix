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
    r"(?:validator|entry\s*point)[^\n;|]*\bplaceholders?\b",
    r"(?i)(?=[^\n]*validate_rollback_card\.py)"
    r"(?=[^\n]*(?:\bplaceholders?\b|\bstubs?\b|do not use|revert))[^\n]*",
)

STALE_RELEASE_PACKAGE_ROLLBACK_GUIDANCE_PATTERNS = (
    r"(?i)(?=[^\n]*\brollbackcard\b)(?=[^\n]*\bvalidator\b)"
    r"(?=[^\n]*(?:\babsent\b|\bplaceholders?\b|notimplementederror))[^\n]*",
)


def tracked_markdown_paths() -> tuple[Path, ...]:
    result = subprocess.run(
        ["git", "ls-files", "-z", "--", "*.md"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError(
            "could not enumerate repository-owned Markdown: "
            + result.stderr.strip()
        )
    paths = tuple(
        REPO_ROOT / relative_path
        for relative_path in result.stdout.split("\0")
        if relative_path
    )
    if not paths:
        raise AssertionError("repository-owned Markdown inventory is empty")
    return paths


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

    def test_compatibility_entrypoint_matches_canonical_file_modes(self) -> None:
        scenarios = (
            (
                "valid-candidate",
                "fixtures/release/rollback_card/valid/valid_hold.json",
                0,
                '"outcome":"PASS"',
            ),
            (
                "missing-candidate",
                "does-not-exist-rollback-card.json",
                1,
                '"code":"FILE_NOT_FOUND"',
            ),
            (
                "invalid-candidate",
                (
                    "fixtures/release/rollback_card/invalid/"
                    "invalid_time_order.json"
                ),
                1,
                '"code":"EFFECTIVE_BEFORE_DECISION"',
            ),
        )
        for name, candidate, expected_returncode, expected_marker in scenarios:
            with self.subTest(name=name):
                canonical = subprocess.run(
                    [
                        sys.executable,
                        "tools/validators/release/validate_rollback_card.py",
                        candidate,
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
                        candidate,
                    ],
                    cwd=REPO_ROOT,
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertEqual(expected_returncode, canonical.returncode)
                self.assertIn(expected_marker, canonical.stdout)
                self.assertEqual(canonical.returncode, compatibility.returncode)
                self.assertEqual(canonical.stdout, compatibility.stdout)
                self.assertEqual(canonical.stderr, compatibility.stderr)

    def test_compatibility_entrypoint_preserves_fail_closed_batch_mode(self) -> None:
        candidates = (
            "fixtures/release/rollback_card/valid/valid_hold.json",
            (
                "fixtures/release/rollback_card/invalid/"
                "invalid_time_order.json"
            ),
        )
        canonical = subprocess.run(
            [
                sys.executable,
                "tools/validators/release/validate_rollback_card.py",
                *candidates,
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
                *candidates,
            ],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(1, canonical.returncode)
        records = [json.loads(line) for line in canonical.stdout.splitlines()]
        self.assertEqual(2, len(records))
        self.assertEqual(sorted(candidates), [record["file"] for record in records])
        self.assertEqual(["FAIL", "PASS"], [record["outcome"] for record in records])
        self.assertEqual(canonical.returncode, compatibility.returncode)
        self.assertEqual(canonical.stdout, compatibility.stdout)
        self.assertEqual(canonical.stderr, compatibility.stderr)

    def test_compatibility_entrypoint_preserves_cli_argument_controls(self) -> None:
        scenarios = (
            (
                "help",
                ("--help",),
                0,
                "stdout",
                "usage: validate_rollback_card.py",
            ),
            (
                "missing-mode",
                (),
                2,
                "stderr",
                "provide one or more files or use --fixtures",
            ),
            (
                "conflicting-modes",
                (
                    "--fixtures",
                    "fixtures/release/rollback_card/valid/valid_hold.json",
                ),
                2,
                "stderr",
                "--fixtures cannot be combined with explicit files",
            ),
            (
                "option-terminator",
                ("--", "--fixtures"),
                1,
                "stdout",
                '"code":"FILE_NOT_FOUND"',
            ),
        )
        for name, arguments, expected_returncode, stream, expected_marker in scenarios:
            with self.subTest(name=name):
                canonical = subprocess.run(
                    [
                        sys.executable,
                        "tools/validators/release/validate_rollback_card.py",
                        *arguments,
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
                        *arguments,
                    ],
                    cwd=REPO_ROOT,
                    capture_output=True,
                    text=True,
                    check=False,
                )

                self.assertEqual(expected_returncode, canonical.returncode)
                self.assertIn(expected_marker, getattr(canonical, stream))
                self.assertEqual(canonical.returncode, compatibility.returncode)
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
            "docs/runbooks/fauna/ROLLBACK_DRILL.md": (
                "generic legacy validator entry point remains a placeholder",
            ),
            "docs/architecture/publication/ROLLBACK.md": (
                "| Generic validator entrypoint | **CONFIRMED placeholder** |",
                "production pipeline and generic validator placeholders",
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
                self.assertNotIn(r"\n\n##", guidance)
                for stale_claim in stale_claims:
                    self.assertNotIn(stale_claim, guidance)
                for stale_pattern in STALE_COMPATIBILITY_GUIDANCE_PATTERNS:
                    self.assertNotRegex(guidance, stale_pattern)

    def test_all_rollback_guidance_rejects_stale_compatibility_claims(
        self,
    ) -> None:
        rollback_guidance_paths = []
        release_package_root = REPO_ROOT / "packages/release"
        for path in tracked_markdown_paths():
            guidance = path.read_text(encoding="utf-8")
            is_release_package_guidance = (
                path.is_relative_to(release_package_root)
                and "rollbackcard" in guidance.casefold()
            )
            if (
                "rollback" in path.as_posix().casefold()
                or "tools/validators/validate_rollback_card.py" in guidance
                or is_release_package_guidance
            ):
                rollback_guidance_paths.append(path)

        self.assertGreaterEqual(len(rollback_guidance_paths), 13)
        required_paths = (
            REPO_ROOT
            / "docs/intake/exploratory/"
            "publication-validator-compatibility-source-map.md",
            REPO_ROOT / "packages/release/README.md",
            REPO_ROOT / "packages/release/src/README.md",
            REPO_ROOT / "packages/release/src/release/README.md",
        )
        for required_path in required_paths:
            self.assertIn(required_path, rollback_guidance_paths)
        for path in rollback_guidance_paths:
            with self.subTest(path=path.relative_to(REPO_ROOT).as_posix()):
                guidance = path.read_text(encoding="utf-8")
                for stale_pattern in STALE_COMPATIBILITY_GUIDANCE_PATTERNS:
                    self.assertNotRegex(guidance, stale_pattern)
                if path.is_relative_to(release_package_root):
                    for stale_pattern in (
                        STALE_RELEASE_PACKAGE_ROLLBACK_GUIDANCE_PATTERNS
                    ):
                        self.assertNotRegex(guidance, stale_pattern)

    def test_guidance_inventory_excludes_untracked_markdown(self) -> None:
        with tempfile.TemporaryDirectory(
            prefix=".rollback-guidance-untracked-",
            dir=REPO_ROOT,
        ) as directory:
            untracked_guidance = Path(directory) / "ROLLBACK.md"
            untracked_guidance.write_text(
                "The generic validator remains a placeholder.\n",
                encoding="utf-8",
            )
            self.assertNotIn(untracked_guidance, tracked_markdown_paths())

    def test_workflow_runs_for_repository_markdown_changes(self) -> None:
        workflow = (
            REPO_ROOT / ".github/workflows/rollback-card.yml"
        ).read_text(encoding="utf-8")
        self.assertRegex(workflow, r'(?m)^\s+- "\*\*/\*\.md"$')

    def test_stale_operator_guidance_patterns_are_non_vacuous(self) -> None:
        stale_variants = (
            "- the generic compatibility validator remains a placeholder;",
            "- the compatibility entry point is still just a placeholder.",
            "- replace the production pipeline and generic validator placeholders.",
            "| Generic validator shortcut | "
            "`python tools/validators/validate_rollback_card.py` | "
            "Do not use |",
            "`tools/validators/validate_rollback_card.py` must remain a stub.",
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
        release_package_stale_variants = (
            "| `RollbackCard` | Declared validator absent; other validator placeholder |",
            "RollbackCard has a different validator that raises NotImplementedError.",
            "RollbackCard contract/schema/validator is still a placeholder validator.",
        )
        for stale_variant in release_package_stale_variants:
            with self.subTest(stale_variant=stale_variant):
                self.assertTrue(
                    any(
                        re.search(pattern, stale_variant)
                        for pattern in (
                            STALE_RELEASE_PACKAGE_ROLLBACK_GUIDANCE_PATTERNS
                        )
                    )
                )
        bounded_validator = (
            "RollbackCard has a bounded validator and no execution authority."
        )
        self.assertFalse(
            any(
                re.search(pattern, bounded_validator)
                for pattern in STALE_RELEASE_PACKAGE_ROLLBACK_GUIDANCE_PATTERNS
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
