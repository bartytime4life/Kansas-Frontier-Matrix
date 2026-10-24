from __future__ import annotations

import importlib.util
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/validators/validate_all.py"
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

    def test_live_registry_registers_dataset_version_without_broadening_profiles(self) -> None:
        registry = orchestrator.load_registry(
            REPO_ROOT / "tools/validators/validator_registry.json",
            REPO_ROOT,
        )
        spec = registry.by_id["dataset-version"]

        self.assertEqual(
            spec.script,
            "tools/validators/data/validate_dataset_version.py",
        )
        self.assertEqual(spec.args, ("--fixtures",))
        self.assertIn("dataset-version", registry.profiles["full"])
        self.assertNotIn("dataset-version", registry.profiles["focused"])
        self.assertNotIn("dataset-version", registry.profiles["release-dry-run"])

        representative_paths = (
            ".github/workflows/dataset-version.yml",
            "contracts/data/dataset_version.md",
            "schemas/contracts/v1/data/dataset_version.schema.json",
            "fixtures/contracts/v1/data/dataset_version/valid/valid_retrieval_snapshot.json",
            "tests/validators/data/test_validate_dataset_version.py",
            "tools/validators/data/validate_dataset_version.py",
            "tools/validators/validate_dataset_version.py",
        )
        for path in representative_paths:
            with self.subTest(path=path):
                selected, mode = orchestrator.select_validators(
                    registry,
                    profile="changed-area",
                    changed_paths=(path,),
                )
                self.assertEqual(mode, "changed-area")
                self.assertIn(
                    "dataset-version",
                    {item.validator_id for item in selected},
                )

        from tools.validators._common import run_all as legacy_runner

        self.assertIn(
            "validate_dataset_version.py",
            legacy_runner.RUNNER_VALIDATORS,
        )

    def test_live_registry_registers_release_manifest_in_release_profiles(self) -> None:
        registry = orchestrator.load_registry(
            REPO_ROOT / "tools/validators/validator_registry.json",
            REPO_ROOT,
        )
        spec = registry.by_id["release-manifest"]

        self.assertEqual(
            spec.script,
            "tools/validators/release/validate_release_manifest.py",
        )
        self.assertEqual(spec.args, ("--fixtures",))
        self.assertNotIn("release-manifest", registry.profiles["focused"])
        self.assertIn("release-manifest", registry.profiles["release-dry-run"])
        self.assertIn("release-manifest", registry.profiles["full"])
        self.assertGreater(
            registry.profiles["release-dry-run"].index("release-manifest"),
            registry.profiles["release-dry-run"].index(
                "catalog-distribution-mapping-profile"
            ),
        )
        self.assertGreater(
            registry.profiles["full"].index("release-manifest"),
            registry.profiles["full"].index(
                "catalog-distribution-mapping-profile"
            ),
        )

        representative_paths = (
            ".github/workflows/release-manifest.yml",
            ".github/workflows/release-dry-run.yml",
            "contracts/release/release_manifest.md",
            "schemas/contracts/v1/release/release_manifest.schema.json",
            "fixtures/release/release_manifest/cases.json",
            "tests/validators/test_validate_release_manifest.py",
            "tools/validators/release/validate_release_manifest.py",
            "docs/intake/exploratory/pass7-release-manifest-profile.md",
            "docs/runbooks/VALIDATOR_ORCHESTRATOR.md",
            "packages/hashing/src/hashing/__init__.py",
            "data/receipts/generated/genrec-pass7-release-manifest-20260808.json",
        )
        for path in representative_paths:
            with self.subTest(path=path):
                selected, mode = orchestrator.select_validators(
                    registry,
                    profile="changed-area",
                    changed_paths=(path,),
                )
                self.assertEqual(mode, "changed-area")
                self.assertIn(
                    "release-manifest",
                    {item.validator_id for item in selected},
                )

        code, report = orchestrator.orchestrate(
            registry,
            repo_root=REPO_ROOT,
            profile="release-dry-run",
            requested_ids=("release-manifest",),
        )
        self.assertEqual(code, 0)
        self.assertEqual(report["outcome"], "PASS")
        self.assertEqual(report["selected_count"], 1)
        self.assertEqual(
            report["results"][0]["validator_id"],
            "release-manifest",
        )

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

    def test_changed_area_without_match_fails_when_required(self) -> None:
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
            require_match=True,
        )

        self.assertEqual(code, 1)
        self.assertEqual(report["outcome"], "FAIL")
        self.assertEqual(report["reason_code"], "NO_MATCHING_VALIDATORS")
        self.assertEqual(report["selection"]["require_match"], True)
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

    def test_legacy_inventory_selects_only_fixture_capable_validators(self) -> None:
        from tools.validators._common import run_all as legacy_runner

        fixture_validator = self._entry(
            "fixture-check", self._script("validate_fixture.py", 0)
        )
        guardrail_validator = self._entry(
            "guardrail-check", self._script("validate_guardrail.py", 0)
        )
        guardrail_validator["args"] = []
        registry_path = self._registry([fixture_validator, guardrail_validator])

        with mock.patch.object(legacy_runner, "REGISTRY_PATH", registry_path):
            self.assertEqual(
                legacy_runner._load_legacy_inventory(),
                ["validate_fixture.py"],
            )

    def test_unparseable_registry_json_is_a_configuration_error(self) -> None:
        path = self.root / "tools/validators/validator_registry.json"
        cases = {
            "deep": "[" * 100_000 + "]" * 100_000,
            "int-digits": '{"a": ' + "1" * 5000 + "}",
            "overflow": '{"a": 1e400}',
            "nan": '{"a": NaN}',
            "duplicate": '{"a": 1, "a": 2}',
            "not-utf8": b"\xff",
            "array": "[]",
        }
        for name, body in cases.items():
            with self.subTest(name):
                if isinstance(body, bytes):
                    path.write_bytes(body)
                else:
                    path.write_text(body, encoding="utf-8")
                with self.assertRaises(orchestrator.RegistryError):
                    self._load(path)

    def test_cli_reports_configuration_errors_as_json_exit_two(self) -> None:
        self._registry([self._entry("alpha-check", self._script("validate_alpha.py", 0))])
        changed = self.root / "changed.txt"
        changed.write_bytes(b"tools/\xff.py\n")
        (self.root / "tools/validators/validator_registry.json").write_text("[" * 100_000, encoding="utf-8")
        argvs = (
            ["--validate-registry"],
            ["--profile", "focused", "--require-match"],
        )
        for argv in argvs:
            with self.subTest(argv), mock.patch("sys.stderr", new_callable=io.StringIO) as err:
                self.assertEqual(orchestrator.main([*argv, "--repo-root", str(self.root)]), 2)
            self.assertEqual(json.loads(err.getvalue())["reason_code"], "ORCHESTRATOR_CONFIGURATION_ERROR")
        self._registry([self._entry("alpha-check", self._script("validate_alpha.py", 0))])
        with mock.patch("sys.stderr", new_callable=io.StringIO) as err:
            code = orchestrator.main(["--profile", "changed-area", "--changed-path-file", str(changed),
                                      "--repo-root", str(self.root)])
        self.assertEqual(code, 2)
        self.assertIn("not UTF-8", json.loads(err.getvalue())["detail"])

    def test_cli_list_validate_and_output_round_trip(self) -> None:
        self._registry([self._entry("alpha-check", self._script("validate_alpha.py", 0))])
        root = ["--repo-root", str(self.root)]
        with mock.patch("sys.stdout", new_callable=io.StringIO) as out:
            self.assertEqual(orchestrator.main(["--list", *root]), 0)
        self.assertEqual(json.loads(out.getvalue())["validators"], ["alpha-check"])
        with mock.patch("sys.stdout", new_callable=io.StringIO) as out:
            self.assertEqual(orchestrator.main(["--validate-registry", *root]), 0)
        self.assertEqual(json.loads(out.getvalue())["reason_code"], "REGISTRY_VALID")
        output = self.root / "reports/report.json"
        with mock.patch("sys.stdout", new_callable=io.StringIO) as out:
            self.assertEqual(orchestrator.main(["--profile", "focused", "--output", str(output), "--quiet", *root]), 0)
        self.assertEqual(out.getvalue(), "")
        self.assertEqual(json.loads(output.read_text(encoding="utf-8"))["outcome"], "PASS")
        self.assertFalse(output.with_name("report.json.tmp").exists())

    def test_output_symlinks_are_denied_even_when_dangling(self) -> None:
        self._registry([self._entry("alpha-check", self._script("validate_alpha.py", 0))])
        victim = self.root / "victim.txt"
        for name, link in (("output", "out.json"), ("temporary", "out.json.tmp")):
            with self.subTest(name):
                output = self.root / "out.json"
                for leftover in (output, output.with_name("out.json.tmp")):
                    if leftover.is_symlink() or leftover.exists():
                        leftover.unlink()
                (self.root / link).symlink_to(victim)
                with mock.patch("sys.stderr", new_callable=io.StringIO) as err:
                    code = orchestrator.main(["--profile", "focused", "--output", str(output), "--quiet",
                                              "--repo-root", str(self.root)])
                self.assertEqual(code, 2)
                self.assertIn("symlink is denied", json.loads(err.getvalue())["detail"])
                self.assertFalse(victim.exists())

    def test_timeout_and_selection_errors_fail_closed(self) -> None:
        slow = self.root / "tools/validators/validate_slow.py"
        slow.write_text("import time\ntime.sleep(5)\n", encoding="utf-8")
        entry = self._entry("slow-check", "tools/validators/validate_slow.py", timeout=1)
        registry = self._load(self._registry([entry]))
        code, report = orchestrator.orchestrate(registry, repo_root=self.root, profile="focused",
                                                include_timing=True)
        self.assertEqual(code, 2)
        self.assertEqual(report["results"][0]["reason_code"], "VALIDATOR_TIMEOUT")
        self.assertIsNone(report["results"][0]["return_code"])
        self.assertIn("total_duration_ms", report)
        for kwargs, message in (
            ({"requested_ids": ["slow-check", "slow-check"]}, "duplicates"),
            ({"requested_ids": ["nope-check"]}, "unknown explicit"),
            ({"require_match": True}, "require_match"),
        ):
            with self.subTest(message), self.assertRaisesRegex(orchestrator.RegistryError, message):
                orchestrator.orchestrate(registry, repo_root=self.root, profile="focused", **kwargs)

    def test_registry_and_changed_path_shape_errors(self) -> None:
        script = self._script("validate_alpha.py", 0)
        good = self._entry("alpha-check", script)
        cases = {
            "root keys": ({"extra": 1}, None, "root keys"),
            "schema": ({"schema_version": "v0"}, None, "schema_version"),
            "registry id": ({"registry_id": "http://x"}, None, "registry_id"),
            "validators empty": ({"validators": []}, None, "non-empty"),
            "entry keys": (None, {**good, "extra": 1}, "v1 contract"),
            "id": (None, {**good, "id": "Bad"}, ".id is invalid"),
            "description": (None, {**good, "description": " "}, "description"),
            "script traversal": (None, {**good, "script": "tools/validators/../x.py"}, "normalized"),
            "script location": (None, {**good, "script": "tools/other.py"}, "required location"),
            "script backslash": (None, {**good, "script": "tools\\validators\\x.py"}, "backslashes"),
            "script suffix": (None, {**good, "script": "tools/validators/x.sh"}, "Python"),
            "args": (None, {**good, "args": [""]}, "args"),
            "args duplicate": (None, {**good, "args": ["a", "a"]}, "duplicate"),
            "globs empty": (None, {**good, "path_globs": []}, "path_globs"),
            "globs duplicate": (None, {**good, "path_globs": ["a", "a"]}, "duplicates"),
            "timeout bool": (None, {**good, "timeout_seconds": True}, "timeout"),
            "timeout range": (None, {**good, "timeout_seconds": 601}, "timeout"),
        }
        path = self.root / "tools/validators/validator_registry.json"
        for name, (root_change, entry, message) in cases.items():
            with self.subTest(name):
                self._registry([entry or good])
                if root_change is not None:
                    data = json.loads(path.read_text(encoding="utf-8"))
                    data.update(root_change)
                    path.write_text(json.dumps(data), encoding="utf-8")
                with self.assertRaisesRegex(orchestrator.RegistryError, message):
                    self._load(path)
        for profiles, message in (
            ({"focused": ["alpha-check"], "changed-area": [], "full": ["alpha-check"]}, "must contain"),
            ({"focused": ["ghost-check"], "changed-area": [], "release-dry-run": ["alpha-check"],
              "full": ["alpha-check"]}, "unknown validators"),
            ({"focused": [], "changed-area": [], "release-dry-run": ["alpha-check"],
              "full": ["alpha-check"]}, "non-empty"),
        ):
            with self.subTest(message), self.assertRaisesRegex(orchestrator.RegistryError, message):
                self._load(self._registry([good], profiles=profiles))
        for value in ("/abs/path", "a/../b", "a\\b"):
            with self.subTest(value), self.assertRaises(orchestrator.RegistryError):
                orchestrator.normalize_changed_paths([value])
        self.assertEqual(orchestrator.normalize_changed_paths([" b ", "a", "", "a"]), ("a", "b"))


if __name__ == "__main__":
    unittest.main()
