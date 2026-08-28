from __future__ import annotations

import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest

from tools.validators.e2e_readiness import (
    ACCEPTED_PLAYWRIGHT_CONFIGS,
    EXPECTED_EXPLORER_SCRIPTS,
    EXPECTED_ROOT_HOLDS,
    inspect_readiness,
    main,
    render_report,
)


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]


def _write(path: Path, content: str = "") -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def _build_repository(root: Path) -> None:
    _write(
        root / "package.json",
        json.dumps(
            {
                "packageManager": "pnpm@11.17.0",
                "engines": {"node": ">=22.13 <23"},
                "scripts": EXPECTED_ROOT_HOLDS,
            }
        ),
    )
    _write(root / "pnpm-workspace.yaml", 'packages:\n  - "apps/*"\n  - "packages/*"\n')
    _write(root / "pnpm-lock.yaml", "lockfileVersion: '9.0'\n")
    _write(
        root / "apps/explorer-web/package.json",
        json.dumps(
            {
                "name": "explorer-web",
                "private": True,
                "engines": {"node": ">=22.13 <23"},
                "scripts": EXPECTED_EXPLORER_SCRIPTS,
            }
        ),
    )
    for relative in (
        "apps/explorer-web/README.md",
        "apps/explorer-web/index.html",
        "apps/explorer-web/src/features/shell/index.tsx",
        "apps/explorer-web/src/main.ts",
        "apps/explorer-web/tests/shell-baseline.test.ts",
        "apps/governed-api/README.md",
        "tests/e2e/README.md",
        "tests/e2e/__init__.py",
        "tests/e2e/agriculture/.gitkeep",
        "tests/e2e/agriculture/README.md",
    ):
        _write(root / relative)
    _write(
        root / "tests/e2e/test_hydrology_proof_slice.py",
        "# bounded placeholder\n\n"
        "def test_proof_slice_placeholder():\n"
        "    assert True\n",
    )
    _write(
        root / ".github/workflows/ui-build.yml",
        "UI_MANIFEST: apps/explorer-web/package.json\n"
        "UI_WORKSPACE: explorer-web\n"
        'run: pnpm --filter "${UI_WORKSPACE}" build\n'
        'run: pnpm --filter "${UI_WORKSPACE}" test\n',
    )
    _write(
        root / ".github/workflows/api-test.yml",
        "run: make governed-api-smoke\n",
    )
    _write(
        root / ".github/workflows/e2e-smoke.yml",
        "run: python tools/validators/e2e_readiness.py\n",
    )
    _write(root / "Makefile", "test:\n\tpython -m unittest\n")


class E2EReadinessTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        _build_repository(self.root)

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def _codes(self) -> set[str]:
        return {item.code for item in inspect_readiness(self.root).findings}

    def test_synthetic_current_boundary_passes_as_an_explicit_hold(self) -> None:
        report = inspect_readiness(self.root)

        self.assertTrue(report.ok, report.findings)
        self.assertEqual(
            render_report(report)[1:],
            (
                "WORKFLOW_SKIPPED_EXPLICIT: run-e2e-smoke",
                "WORKFLOW_HOLD: no accepted Explorer Web plus Governed API E2E "
                "command or deterministic fixture suite",
            ),
        )

    def test_current_repository_matches_the_bounded_readiness_contract(self) -> None:
        report = inspect_readiness(REPOSITORY_ROOT)

        self.assertTrue(report.ok, report.findings)
        self.assertGreaterEqual(len(report.inspected_files), 18)

    def test_old_todo_explorer_mapping_fails_closed(self) -> None:
        path = self.root / "apps/explorer-web/package.json"
        manifest = json.loads(path.read_text(encoding="utf-8"))
        manifest["scripts"] = {"dev": "echo TODO", "build": "echo TODO", "test": "echo TODO"}
        path.write_text(json.dumps(manifest), encoding="utf-8")

        self.assertIn("EXPLORER_SCRIPT_MAPPING_CHANGED", self._codes())

    def test_surfaced_e2e_script_requires_deliberate_wiring(self) -> None:
        path = self.root / "apps/explorer-web/package.json"
        manifest = json.loads(path.read_text(encoding="utf-8"))
        manifest["scripts"]["test:e2e"] = "playwright test"
        path.write_text(json.dumps(manifest), encoding="utf-8")

        codes = self._codes()
        self.assertIn("E2E_SCRIPT_SURFACED", codes)
        self.assertIn("EXPLORER_SCRIPT_MAPPING_CHANGED", codes)

    def test_surfaced_root_e2e_script_requires_deliberate_wiring(self) -> None:
        path = self.root / "package.json"
        manifest = json.loads(path.read_text(encoding="utf-8"))
        manifest["scripts"]["test:e2e"] = "playwright test"
        path.write_text(json.dumps(manifest), encoding="utf-8")

        self.assertIn("E2E_SCRIPT_SURFACED", self._codes())

    def test_surfaced_e2e_file_requires_deliberate_wiring(self) -> None:
        _write(self.root / "apps/explorer-web/tests/new.e2e.ts", "protected body\n")

        report = inspect_readiness(self.root)

        self.assertIn("E2E_IMPLEMENTATION_SURFACED", {item.code for item in report.findings})
        self.assertNotIn("protected body", "\n".join(render_report(report)))

    def test_accepted_playwright_config_does_not_trigger_surfaced_finding(self) -> None:
        for relative in ACCEPTED_PLAYWRIGHT_CONFIGS:
            _write(self.root / relative, "// accepted playwright config\n")

        self.assertNotIn("E2E_IMPLEMENTATION_SURFACED", self._codes())

    def test_unaccepted_playwright_config_fails_closed(self) -> None:
        _write(
            self.root / "apps/explorer-web/playwright.config.extra.ts",
            "// unaccepted playwright config\n",
        )

        self.assertIn("E2E_IMPLEMENTATION_SURFACED", self._codes())

    def test_changed_hydrology_placeholder_fails_closed(self) -> None:
        _write(
            self.root / "tests/e2e/test_hydrology_proof_slice.py",
            "def test_proof_slice():\n    assert 2 + 2 == 4\n",
        )

        self.assertIn("E2E_PLACEHOLDER_CHANGED", self._codes())

    def test_e2e_inventory_addition_fails_closed(self) -> None:
        _write(self.root / "tests/e2e/test_new_journey.py", "def test_journey():\n    pass\n")

        self.assertIn("E2E_INVENTORY_CHANGED", self._codes())

    def test_missing_ui_build_command_fails_closed(self) -> None:
        _write(
            self.root / ".github/workflows/ui-build.yml",
            "UI_MANIFEST: apps/explorer-web/package.json\n"
            "UI_WORKSPACE: explorer-web\n",
        )

        self.assertIn("REQUIRED_MARKER_MISSING", self._codes())

    def test_missing_workflow_invocation_fails_closed(self) -> None:
        _write(self.root / ".github/workflows/e2e-smoke.yml", "run: echo hold\n")

        self.assertIn("REQUIRED_MARKER_MISSING", self._codes())

    def test_symlink_input_is_denied(self) -> None:
        target = self.root / "outside.json"
        _write(target, "{}")
        manifest = self.root / "apps/explorer-web/package.json"
        manifest.unlink()
        manifest.symlink_to(target)

        self.assertIn("INPUT_SYMLINK_DENIED", self._codes())

    def test_cli_output_and_exit_polarity_are_deterministic(self) -> None:
        outputs: list[str] = []
        for _ in range(2):
            stream = io.StringIO()
            with contextlib.redirect_stdout(stream):
                self.assertEqual(main(["--repo-root", str(self.root)]), 0)
            outputs.append(stream.getvalue())

        self.assertEqual(outputs[0], outputs[1])
        self.assertIn("E2E_READINESS_CONFIRMED", outputs[0])
        _write(self.root / "tests/e2e/unexpected.py", "SECRET_CANARY\n")
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            self.assertEqual(main(["--repo-root", str(self.root)]), 1)
        self.assertNotIn("SECRET_CANARY", stream.getvalue())
        self.assertIn("E2E_INVENTORY_CHANGED", stream.getvalue())


if __name__ == "__main__":
    unittest.main()
