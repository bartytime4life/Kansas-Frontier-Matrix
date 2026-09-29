from pathlib import Path
import tempfile
import unittest

from tools.validators.e2e_readiness import inspect_readiness


ACCEPTED_PROOF_SLICE_TEST = (
    "import subprocess, sys\n\n"
    "def test_lane():\n"
    "    result = subprocess.run([sys.executable, 'tools/readiness/run_lane.py', 'proof-slice'])\n"
    "    assert result.returncode == 0\n"
)


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
            ACCEPTED_PROOF_SLICE_TEST,
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

    def test_reverting_to_a_vacuous_placeholder_is_rejected(self) -> None:
        (self.root / "tests/e2e/test_hydrology_proof_slice.py").write_text(
            "def test_proof_slice_placeholder():\n    assert True\n",
            encoding="utf-8",
        )
        self.assertIn("E2E_PROOF_SLICE_TEST_VACUOUS", inspect_readiness(self.root).findings)

    def test_proof_slice_test_must_invoke_the_lane(self) -> None:
        (self.root / "tests/e2e/test_hydrology_proof_slice.py").write_text(
            "def test_something():\n    assert 1 + 1 == 2\n",
            encoding="utf-8",
        )
        self.assertIn("E2E_PROOF_SLICE_LANE_NOT_INVOKED", inspect_readiness(self.root).findings)

    def test_lane_named_only_in_text_is_not_an_invocation(self) -> None:
        (self.root / "tests/e2e/test_hydrology_proof_slice.py").write_text(
            '"""Runs tools/readiness/run_lane.py proof-slice."""\n'
            "# tools/readiness/run_lane.py proof-slice\n"
            "def test_something():\n"
            '    """tools/readiness/run_lane.py proof-slice"""\n'
            "    assert 1 + 1 == 2\n",
            encoding="utf-8",
        )
        self.assertIn("E2E_PROOF_SLICE_LANE_NOT_INVOKED", inspect_readiness(self.root).findings)

    def test_lane_markers_passed_to_an_unrelated_call_are_not_an_invocation(self) -> None:
        (self.root / "tests/e2e/test_hydrology_proof_slice.py").write_text(
            "def test_something():\n"
            '    print("tools/readiness/run_lane.py", "proof-slice")\n'
            '    assert ["tools/readiness/run_lane.py", "proof-slice"]\n',
            encoding="utf-8",
        )
        self.assertIn("E2E_PROOF_SLICE_LANE_NOT_INVOKED", inspect_readiness(self.root).findings)

    def test_subprocess_call_with_other_lane_is_not_an_invocation(self) -> None:
        (self.root / "tests/e2e/test_hydrology_proof_slice.py").write_text(
            "import subprocess\n"
            "def test_something():\n"
            '    subprocess.run(["python", "tools/readiness/run_lane.py", "fixtures", "proof-slice"])\n'
            "    assert True\n",
            encoding="utf-8",
        )
        self.assertIn("E2E_PROOF_SLICE_LANE_NOT_INVOKED", inspect_readiness(self.root).findings)

    def test_unparseable_proof_slice_test_is_rejected(self) -> None:
        (self.root / "tests/e2e/test_hydrology_proof_slice.py").write_text("def (:\n", encoding="utf-8")
        self.assertIn("E2E_PROOF_SLICE_TEST_INVALID", inspect_readiness(self.root).findings)

    def test_committed_repository_passes(self) -> None:
        repository = Path(__file__).resolve().parents[2]
        self.assertEqual(inspect_readiness(repository).findings, ())


if __name__ == "__main__":
    unittest.main()
