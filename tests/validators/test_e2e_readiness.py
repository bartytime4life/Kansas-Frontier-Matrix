from pathlib import Path
import tempfile
import unittest

from tools.validators.e2e_readiness import inspect_readiness


class E2ERetirementReadinessTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for relative in (
            "package.json",
            "Makefile",
            "apps/governed-api/README.md",
            "tests/e2e/README.md",
            "tests/e2e/__init__.py",
            "tests/e2e/agriculture/.gitkeep",
            "tests/e2e/agriculture/README.md",
        ):
            path = self.root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("\n", encoding="utf-8")
        (self.root / "tests/e2e/test_hydrology_proof_slice.py").write_text(
            "# placeholder\n\ndef test_proof_slice_placeholder():\n    assert True\n",
            encoding="utf-8",
        )

    def test_current_hold_is_explicit(self) -> None:
        self.assertTrue(inspect_readiness(self.root).ok)

    def test_retired_application_cannot_reappear_silently(self) -> None:
        (self.root / "apps/explorer-web").mkdir()
        self.assertIn(
            "RETIRED_APP_RESURFACED:apps/explorer-web",
            inspect_readiness(self.root).findings,
        )

    def test_new_e2e_implementation_requires_review(self) -> None:
        (self.root / "tests/e2e/test_live.py").write_text("pass\n", encoding="utf-8")
        self.assertIn(
            "E2E_IMPLEMENTATION_SURFACED:test_live.py",
            inspect_readiness(self.root).findings,
        )

    def test_placeholder_change_requires_review(self) -> None:
        (self.root / "tests/e2e/test_hydrology_proof_slice.py").write_text(
            "def test_proof_slice_placeholder():\n    assert False\n",
            encoding="utf-8",
        )
        self.assertIn("E2E_PLACEHOLDER_CHANGED", inspect_readiness(self.root).findings)


if __name__ == "__main__":
    unittest.main()
