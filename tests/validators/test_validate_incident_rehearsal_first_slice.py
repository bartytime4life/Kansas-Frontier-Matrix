from __future__ import annotations

import unittest
from pathlib import Path


DOC = (
    Path(__file__).resolve().parents[2]
    / "docs/security/incident-response-handoff-decision.md"
)


class IncidentRehearsalFirstSliceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.text = DOC.read_text(encoding="utf-8")

    def test_records_inventory_overlap_and_contract(self) -> None:
        for snippet in (
            "## M34 evidence and first slice",
            "docs/security/INCIDENT_RESPONSE.md",
            "docs/runbooks/INCIDENT_RESPONSE.md",
            "docs/runbooks/rollback-rehearsal.md",
            "tests/release/test_synthetic_rollback_rehearsal.py",
            "tools/release/rollback_apply.py",
            "#3380",
            "#3398",
            "#4069",
            "### Validation and rollback contract",
            "python -m unittest -q tests.release.test_synthetic_rollback_rehearsal",
        ):
            self.assertIn(snippet, self.text)

        for outcome in ("IMPLEMENTED", "PARTIAL", "SUPERSEDED", "ABSENT"):
            self.assertIn(outcome, self.text)

    def test_change_history_includes_m34_slice(self) -> None:
        self.assertIn("v1.1", self.text)
        self.assertIn(
            "Added the M34 evidence inventory, overlap map, first synthetic rehearsal slice, and validation / rollback contract.",
            self.text,
        )


if __name__ == "__main__":
    unittest.main()
