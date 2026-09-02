from __future__ import annotations

import importlib.util
import io
import sys
import unittest
from contextlib import redirect_stdout
from datetime import date
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_DIR = REPO_ROOT / "tools/validators/directory_governance"
if str(VALIDATOR_DIR) not in sys.path:
    sys.path.insert(0, str(VALIDATOR_DIR))

TOPOLOGY_PATH = VALIDATOR_DIR / "validate_repository_topology.py"
TOPOLOGY_SPEC = importlib.util.spec_from_file_location(
    "validate_repository_topology", TOPOLOGY_PATH
)
assert TOPOLOGY_SPEC is not None and TOPOLOGY_SPEC.loader is not None
topology = importlib.util.module_from_spec(TOPOLOGY_SPEC)
sys.modules[TOPOLOGY_SPEC.name] = topology
TOPOLOGY_SPEC.loader.exec_module(topology)

DIAGNOSTIC_PATH = VALIDATOR_DIR / "render_repository_topology_diagnostics.py"
DIAGNOSTIC_SPEC = importlib.util.spec_from_file_location(
    "render_repository_topology_diagnostics", DIAGNOSTIC_PATH
)
assert DIAGNOSTIC_SPEC is not None and DIAGNOSTIC_SPEC.loader is not None
diagnostics = importlib.util.module_from_spec(DIAGNOSTIC_SPEC)
DIAGNOSTIC_SPEC.loader.exec_module(diagnostics)


def _entry(finding: object) -> dict[str, object]:
    return {
        "rule_id": finding.rule_id,
        "subject": finding.subject,
        "evidence_sha256": finding.evidence_sha256,
        "evidence_members": finding.evidence_members,
        "fingerprint": finding.fingerprint,
    }


class RepositoryTopologyDiagnosticTests(unittest.TestCase):
    def test_renders_failure_identities_without_evidence_members(self) -> None:
        secret = "SECRET-EVIDENCE-MEMBER"
        stale = topology._finding("KFM-TOPO-003", "old-root.txt", secret)
        new = topology._finding("KFM-TOPO-003", "new-root.txt", secret)
        invariant = topology._finding("KFM-TOPO-002", "rogue/", secret)
        baseline = {stale.fingerprint: _entry(stale)}

        code, report = topology.evaluate(
            [new, invariant],
            2,
            baseline,
            expires_on="2026-11-10",
            as_of=date(2026, 8, 15),
        )
        self.assertEqual(1, code)

        rendered = diagnostics.render_diagnostics(report, baseline, max_items=20)
        text = "\n".join(rendered)
        self.assertIn("FAIL_INVARIANT KFM-TOPO-002 subject=rogue/", text)
        self.assertIn("FAIL_NEW_DRIFT KFM-TOPO-003 subject=new-root.txt", text)
        self.assertIn("STALE_BASELINE KFM-TOPO-003 subject=old-root.txt", text)
        self.assertNotIn(secret, text)
        self.assertNotIn(stale.evidence_sha256, text)

    def test_output_is_deterministic_and_bounded(self) -> None:
        findings = [
            topology._finding("KFM-TOPO-003", f"root-{index}.txt", f"evidence-{index}")
            for index in range(4)
        ]
        code, report = topology.evaluate(
            list(reversed(findings)),
            4,
            {},
            expires_on="2026-11-10",
            as_of=date(2026, 8, 15),
        )
        self.assertEqual(1, code)

        first = diagnostics.render_diagnostics(report, {}, max_items=2)
        second = diagnostics.render_diagnostics(report, {}, max_items=2)
        self.assertEqual(first, second)
        self.assertEqual(3, len(first))
        self.assertEqual("... 2 additional failure identities omitted", first[-1])
        self.assertLess(first[0], first[1])

    def test_max_items_is_fail_closed(self) -> None:
        with self.assertRaises(topology.TopologyError):
            diagnostics.render_diagnostics({}, {}, max_items=0)
        with self.assertRaises(topology.TopologyError):
            diagnostics.render_diagnostics({}, {}, max_items=51)

    def test_known_trusted_baseline_errors_have_stable_reason_codes(self) -> None:
        cases = {
            "trusted baseline ref cannot be resolved": "TRUSTED_REF_UNRESOLVED",
            "trusted baseline is missing outside the governed bootstrap": "TRUSTED_BASELINE_MISSING",
            "baseline transition adds waiver fingerprints": "BASELINE_WAIVER_ADDED",
            "baseline transition extends expiry": "BASELINE_EXPIRY_EXTENDED",
        }
        for message, expected in cases.items():
            with self.subTest(message=message):
                self.assertEqual(
                    expected,
                    diagnostics.error_reason_code(
                        topology.TopologyError(message), stage="trusted-baseline"
                    ),
                )

    def test_unknown_error_text_is_not_exposed(self) -> None:
        secret = "SECRET-UNTRUSTED-REF-OR-PATH"
        output = io.StringIO()
        with mock.patch.object(
            diagnostics.topology,
            "scan",
            side_effect=topology.TopologyError(secret),
        ):
            with redirect_stdout(output):
                code = diagnostics.main([])

        self.assertEqual(2, code)
        rendered = output.getvalue()
        self.assertIn("ERROR_VALIDATOR: TopologyError reason=SCAN_ERROR", rendered)
        self.assertNotIn(secret, rendered)

    def test_unknown_trusted_error_uses_stage_reason_without_echoing_text(self) -> None:
        secret = "SECRET-TRUSTED-BASELINE-DETAIL"
        self.assertEqual(
            "TRUSTED_BASELINE_ERROR",
            diagnostics.error_reason_code(
                topology.TopologyError(secret), stage="trusted-baseline"
            ),
        )


if __name__ == "__main__":
    unittest.main()
