from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/ci/validate_codeql_source_boundary.py"
SPEC = importlib.util.spec_from_file_location(
    "kfm_validate_codeql_source_boundary", MODULE_PATH
)
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


class ValidateCodeqlSourceBoundaryTests(unittest.TestCase):
    def test_current_workflow_matrix_is_explicit_and_source_backed(self) -> None:
        workflow_path = REPO_ROOT / ".github/workflows/codeql.yml"
        workflow_text = workflow_path.read_text(encoding="utf-8")
        entries = module.extract_matrix_entries(workflow_text)
        self.assertEqual(module.EXPECTED_MATRIX, frozenset(entries))

        tracked = module.tracked_checked_out_files(REPO_ROOT)
        for language, build_mode in entries:
            with self.subTest(language=language):
                module.validate_workflow_contract(
                    workflow_text,
                    language=language,
                    build_mode=build_mode,
                )
                report = module.evaluate_paths(
                    tracked,
                    language=language,
                    build_mode=build_mode,
                    workflow=".github/workflows/codeql.yml",
                )
                self.assertGreater(report.source_count, 0)

    def test_missing_source_fails_with_official_guidance(self) -> None:
        with self.assertRaises(module.BoundaryFailure) as caught:
            module.evaluate_paths(
                ("README.md",),
                language="python",
                build_mode="none",
                workflow=".github/workflows/codeql.yml",
            )
        self.assertEqual("NO_TRACKED_SOURCE", caught.exception.reason)
        self.assertEqual(module.EXIT_NO_SOURCE, caught.exception.exit_code)
        self.assertEqual(
            module.TROUBLESHOOTING_URL,
            caught.exception.as_record()["docs"],
        )

    def test_language_without_policy_fails_closed(self) -> None:
        with self.assertRaises(module.BoundaryFailure) as caught:
            module.evaluate_paths(
                ("src/main.go",),
                language="go",
                build_mode="autobuild",
                workflow=".github/workflows/codeql.yml",
            )
        self.assertEqual("LANGUAGE_POLICY_MISSING", caught.exception.reason)
        self.assertEqual(module.EXIT_CONFIGURATION, caught.exception.exit_code)

    def test_inadmissible_build_mode_fails_closed(self) -> None:
        with self.assertRaises(module.BoundaryFailure) as caught:
            module.evaluate_paths(
                ("src/app.ts",),
                language="javascript-typescript",
                build_mode="autobuild",
                workflow=".github/workflows/codeql.yml",
            )
        self.assertEqual("BUILD_MODE_NOT_ADMITTED", caught.exception.reason)

    def test_generated_or_vendor_source_does_not_satisfy_boundary(self) -> None:
        for path in ("vendor/tool.py", "node_modules/pkg/index.ts", "dist/app.js"):
            with self.subTest(path=path):
                with self.assertRaises(module.BoundaryFailure) as caught:
                    module.evaluate_paths(
                        (path,),
                        language=(
                            "python" if path.endswith(".py") else "javascript-typescript"
                        ),
                        build_mode="none",
                        workflow=".github/workflows/codeql.yml",
                    )
                self.assertEqual("NO_TRACKED_SOURCE", caught.exception.reason)

    def test_actions_policy_is_limited_to_workflow_sources(self) -> None:
        with self.assertRaises(module.BoundaryFailure):
            module.evaluate_paths(
                ("docs/example.yml",),
                language="actions",
                build_mode="none",
                workflow=".github/workflows/codeql.yml",
            )
        report = module.evaluate_paths(
            (".github/workflows/example.yml",),
            language="actions",
            build_mode="none",
            workflow=".github/workflows/codeql.yml",
        )
        self.assertEqual(1, report.source_count)

    def test_workflow_contract_rejects_preflight_after_initialization(self) -> None:
        workflow = """
strategy:
  matrix:
    include:
      - language: python
        build-mode: none
steps:
  - name: Check out analyzed revision
    run: true
  - name: Test CodeQL source boundary helper
    run: true
  - name: Initialize CodeQL
    run: true
  - name: Validate CodeQL source boundary
    run: python tools/ci/validate_codeql_source_boundary.py --language "${{ matrix.language }}" --build-mode "${{ matrix.build-mode }}"
  - name: Analyze source
    run: true
"""
        with self.assertRaises(module.BoundaryFailure) as caught:
            module.validate_workflow_contract(
                workflow,
                language="python",
                build_mode="none",
            )
        self.assertEqual("WORKFLOW_STEP_ORDER_ERROR", caught.exception.reason)

    def test_cli_reads_only_checked_out_tracked_files(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp)
            (repo / "tools/ci").mkdir(parents=True)
            (repo / "tests/ci").mkdir(parents=True)
            (repo / ".github/workflows").mkdir(parents=True)
            helper_path = repo / "tools/ci/validate_codeql_source_boundary.py"
            helper_path.write_text(MODULE_PATH.read_text(encoding="utf-8"), encoding="utf-8")
            (repo / "tests/ci/test_validate_codeql_source_boundary.py").write_text(
                "# tracked test source\n", encoding="utf-8"
            )
            workflow_path = repo / ".github/workflows/codeql.yml"
            workflow_path.write_text(
                """
strategy:
  matrix:
    include:
      - language: python
        build-mode: none
steps:
  - name: Check out analyzed revision
    run: true
  - name: Test CodeQL source boundary helper
    run: true
  - name: Validate CodeQL source boundary
    run: python tools/ci/validate_codeql_source_boundary.py --language "${{ matrix.language }}" --build-mode "${{ matrix.build-mode }}"
  - name: Initialize CodeQL
    run: true
  - name: Analyze source
    run: true
""".lstrip(),
                encoding="utf-8",
            )
            subprocess.run(("git", "init", "-q", str(repo)), check=True)
            subprocess.run(
                (
                    "git",
                    "-C",
                    str(repo),
                    "add",
                    ".github/workflows/codeql.yml",
                    "tools/ci/validate_codeql_source_boundary.py",
                    "tests/ci/test_validate_codeql_source_boundary.py",
                ),
                check=True,
            )
            (repo / "untracked.py").write_text(
                "# must not affect the tracked inventory\n", encoding="utf-8"
            )

            exit_code = module.main(
                (
                    "--repo-root",
                    str(repo),
                    "--workflow",
                    ".github/workflows/codeql.yml",
                    "--language",
                    "python",
                    "--build-mode",
                    "none",
                )
            )
            self.assertEqual(0, exit_code)
            tracked = module.tracked_checked_out_files(repo)
            self.assertNotIn("untracked.py", tracked)


if __name__ == "__main__":
    unittest.main()
