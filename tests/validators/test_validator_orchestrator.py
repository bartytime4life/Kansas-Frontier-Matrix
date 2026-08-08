from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[2] / "tools/validators/validate_all.py"
SPEC = importlib.util.spec_from_file_location("kfm_validator_orchestrator", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
orchestrator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = orchestrator
SPEC.loader.exec_module(orchestrator)


class ValidatorOrchestratorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "tools/validators").mkdir(parents=True)

    def _script(self, name: str, exit_code: int, stdout: str = "") -> str:
        path = self.root / "tools/validators" / name
        path.write_text(
            "from __future__ import annotations\n"
            f"print({stdout!r})\n"
            f"raise SystemExit({exit_code})\n",
            encoding="utf-8",
        )
        return path.relative_to(self.root).as_posix()

    def _registry(self, validators: list[dict[str, object]], profiles: dict[str, list[str]] | None = None) -> Path:
        ids = [str(item["id"]) for item in validators]
        if profiles is None:
            profiles = {
                "focused": ids[:1],
                "changed-area": [],
                "release-dry-run": ids[-1:],
                "full": ids,
            }
        path = self.root / "tools/validators/validator_registry.json"
        path.write_text(
            json.dumps(
                {
                    "schema_version": orchestrator.REGISTRY_SCHEMA_VERSION,
                    "registry_id": "kfm://test/validator-registry/v1",
                    "profiles": profiles,
                    "validators": validators,
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        return path

    def _entry(
        self,
        validator_id: str,
        script: str,
        *,
        glob: str = "contracts/**",
        timeout: int = 10,
    ) -> dict[str, object]:
        return {
            "id": validator_id,
            "description": f"Synthetic {validator_id} validator.",
            "script": script,
            "args": ["--fixtures"],
            "path_globs": [glob],
            "timeout_seconds": timeout,
            "artifact_refs": [],
        }

    def _load(self, path: Path):
        return orchestrator.load_registry(path, self.root)

    def test_full_profile_pass_report_is_byte_stable_without_timing(self) -> None:
        first = self._entry("alpha-check", self._script("validate_alpha.py", 0, "PASS alpha"))
        second = self._entry("beta-check", self._script("validate_beta.py", 0, "PASS beta"))
        registry = self._load(self._registry([first, second]))

        code_a, report_a = orchestrator.orchestrate(
            registry,
            repo_root=self.root,
            profile="full",
        )
        code_b, report_b = orchestrator.orchestrate(
            registry,
            repo_root=self.root,
            profile="full",
        )

        self.assertEqual(code_a, 0)
        self.assertEqual(code_b, 0)
        self.assertEqual(report_a, report_b)
        self.assertEqual(report_a["outcome"], "PASS")
        self.assertEqual([item["validator_id"] for item in report_a["results"]], ["alpha-check", "beta-check"])
        self.assertFalse(report_a["timing_included"])
        self.assertNotIn("total_duration_ms", report_a)

    def test_child_exit_one_maps_to_validation_failure(self) -> None:
        entry = self._entry("reject-check", self._script("validate_reject.py", 1, "FAIL synthetic"))
        registry = self._load(self._registry([entry]))

        code, report = orchestrator.orchestrate(registry, repo_root=self.root, profile="full")

        self.assertEqual(code, 1)
        self.assertEqual(report["outcome"], "FAIL")
        self.assertEqual(report["results"][0]["reason_code"], "VALIDATOR_REJECTED")

    def test_child_exit_two_maps_to_orchestrator_error(self) -> None:
        entry = self._entry("error-check", self._script("validate_error.py", 2, "ERROR synthetic"))
        registry = self._load(self._registry([entry]))

        code, report = orchestrator.orchestrate(registry, repo_root=self.root, profile="full")

        self.assertEqual(code, 2)
        self.assertEqual(report["outcome"], "ERROR")
        self.assertEqual(report["results"][0]["reason_code"], "VALIDATOR_ERROR")

    def test_changed_area_selects_only_matching_validator(self) -> None:
        alpha = self._entry(
            "alpha-check",
            self._script("validate_alpha.py", 0),
            glob="contracts/alpha/**",
        )
        beta = self._entry(
            "beta-check",
            self._script("validate_beta.py", 0),
            glob="contracts/beta/**",
        )
        registry = self._load(self._registry([alpha, beta]))

        code, report = orchestrator.orchestrate(
            registry,
            repo_root=self.root,
            profile="changed-area",
            changed_paths=("contracts/beta/example.md",),
        )

        self.assertEqual(code, 0)
        self.assertEqual(report["selected_count"], 1)
        self.assertEqual(report["results"][0]["validator_id"], "beta-check")
        self.assertEqual(report["selection"]["mode"], "changed-area")

    def test_changed_area_without_match_abstains_without_false_pass_claim(self) -> None:
        entry = self._entry(
            "alpha-check",
            self._script("validate_alpha.py", 0),
            glob="contracts/alpha/**",
        )
        registry = self._load(self._registry([entry]))

        code, report = orchestrator.orchestrate(
            registry,
            repo_root=self.root,
            profile="changed-area",
            changed_paths=("docs/example.md",),
        )

        self.assertEqual(code, 0)
        self.assertEqual(report["outcome"], "ABSTAIN")
        self.assertEqual(report["reason_code"], "NO_MATCHING_VALIDATORS")
        self.assertEqual(report["selected_count"], 0)

    def test_duplicate_validator_id_is_rejected(self) -> None:
        script = self._script("validate_alpha.py", 0)
        entries = [self._entry("alpha-check", script), self._entry("alpha-check", script)]
        path = self._registry(entries, profiles={
            "focused": ["alpha-check"],
            "changed-area": [],
            "release-dry-run": ["alpha-check"],
            "full": ["alpha-check", "alpha-check"],
        })

        with self.assertRaisesRegex(orchestrator.RegistryError, "duplicate validator id"):
            self._load(path)

    def test_missing_script_is_rejected_before_execution(self) -> None:
        entry = self._entry("missing-check", "tools/validators/validate_missing.py")
        path = self._registry([entry])

        with self.assertRaisesRegex(orchestrator.RegistryError, "script is missing"):
            self._load(path)

    def test_full_profile_must_cover_registry_exactly_once(self) -> None:
        alpha = self._entry("alpha-check", self._script("validate_alpha.py", 0))
        beta = self._entry("beta-check", self._script("validate_beta.py", 0))
        path = self._registry(
            [alpha, beta],
            profiles={
                "focused": ["alpha-check"],
                "changed-area": [],
                "release-dry-run": ["beta-check"],
                "full": ["alpha-check"],
            },
        )

        with self.assertRaisesRegex(orchestrator.RegistryError, "profiles.full"):
            self._load(path)

    def test_explicit_validator_selection_preserves_requested_order(self) -> None:
        alpha = self._entry("alpha-check", self._script("validate_alpha.py", 0))
        beta = self._entry("beta-check", self._script("validate_beta.py", 0))
        registry = self._load(self._registry([alpha, beta]))

        code, report = orchestrator.orchestrate(
            registry,
            repo_root=self.root,
            profile="full",
            requested_ids=("beta-check", "alpha-check"),
        )

        self.assertEqual(code, 0)
        self.assertEqual(report["selection"]["mode"], "explicit")
        self.assertEqual(
            [item["validator_id"] for item in report["results"]],
            ["beta-check", "alpha-check"],
        )


if __name__ == "__main__":
    unittest.main()
