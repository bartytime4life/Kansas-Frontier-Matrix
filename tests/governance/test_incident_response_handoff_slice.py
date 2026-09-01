import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DECISION = ROOT / "docs/security/incident-response-handoff-decision.md"
TOPOLOGY = ROOT / "docs/architecture/deployment-topology.md"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class IncidentResponseHandoffSliceTests(unittest.TestCase):
    def test_handoff_inventory_records_overlap_map_and_current_main(self) -> None:
        decision = read_text(DECISION)
        topology = read_text(TOPOLOGY)

        for token in (
            "Milestone inventory and overlap map",
            "main@db23a8bfa9fa126e87009a41240576619ccaac02",
            "docs/security/INCIDENT_RESPONSE.md",
            "docs/runbooks/INCIDENT_RESPONSE.md",
            "docs/security/incident-response-handoff-decision.md",
            "docs/architecture/deployment-topology.md",
            "issue #2900",
            "issue #3380",
            "PR #4080",
            "IMPLEMENTED",
            "PARTIAL",
            "SUPERSEDED",
            "NOT_INSPECTED",
        ):
            self.assertIn(token, decision)

        self.assertIn("incident-response-handoff-decision.md", topology)
        self.assertIn("#2900", topology)

    def test_handoff_tabletop_slice_stays_synthetic_and_reversible(self) -> None:
        decision = read_text(DECISION)

        for token in (
            "`REPORTED`",
            "`ACKNOWLEDGED`",
            "`TRIAGED`",
            "`TRANSFERRED`",
            "`ACTIVE`",
            "`MONITORING`",
            "`CLOSED`",
            "`CORRECTED`",
            "`ABSTAIN`",
            "`ACCESS_DENIED`",
            "`STALE_RUNBOOK`",
            "evidence custody",
            "CorrectionNotice",
            "RollbackCard",
            "rotated or revoked through the issuing authority",
            "Forward correction uses",
            "rollback restores",
            "This slice is synthetic only",
            "does not mirror logs, screenshots, credentials",
            "payloads into public history",
        ):
            self.assertIn(token, decision)
