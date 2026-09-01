from __future__ import annotations

import json
from pathlib import Path
import unittest

M17_ROOT = Path(__file__).resolve().parents[2] / "artifacts/qa/validation/milestone-17"


class M17SupplyChainEvidenceTests(unittest.TestCase):
    def test_m17_supply_chain_evidence_snapshot_is_well_formed(self) -> None:
        report = json.loads(
            (
                M17_ROOT / "dependency_supply_chain_evidence.json"
            ).read_text(encoding="utf-8")
        )

        self.assertEqual(
            report["repository"]["full_name"],
            "bartytime4life/Kansas-Frontier-Matrix",
        )
        self.assertEqual(
            report["execution_start_snapshot"]["current_main"]["sha"],
            "db23a8bfa9fa126e87009a41240576619ccaac02",
        )
        self.assertEqual(
            report["execution_start_snapshot"]["overlap"]["open_pull_requests"][0][
                "number"
            ],
            4079,
        )
        self.assertEqual(report["first_slice"]["artifact_class"], "dependency-scan")
        self.assertEqual(
            report["first_slice"]["validation_contract"]["current_main_result"],
            "PASS",
        )

        outcomes = report["inventory"]["material_outcomes"]
        self.assertTrue(
            any(
                item["path"] == ".github/workflows/dependency-scan.yml"
                and item["classification"] == "IMPLEMENTED"
                for item in outcomes
            )
        )
        self.assertTrue(
            any(
                item["path"] == ".github/workflows/security.yml"
                and item["classification"] == "PARTIAL"
                for item in outcomes
            )
        )
        self.assertTrue(
            all(item["classification"] in {"IMPLEMENTED", "PARTIAL"} for item in outcomes)
        )

        unexecuted = report["first_slice"]["explicitly_unexecuted"]
        self.assertLessEqual(
            {item["status"] for item in unexecuted},
            {"NOT_RUN", "NOT_INSPECTED"},
        )
