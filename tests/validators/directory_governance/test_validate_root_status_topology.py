from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = (
    REPO_ROOT
    / "tools/validators/directory_governance/validate_repository_topology.py"
)
SPEC = importlib.util.spec_from_file_location(
    "kfm_validate_repository_topology_root_status", MODULE_PATH
)
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


class RepositoryTopologyRootStatusTests(unittest.TestCase):
    @staticmethod
    def _findings(
        *,
        class_defaults: dict[str, object],
        roots: list[dict[str, object]],
    ) -> list[object]:
        paths = ("docs/README.md",)
        modes = {path: "100644" for path in paths}
        object_ids = {path: "a" * 40 for path in paths}
        blobs = {
            "control_plane/root_registry.yaml": json.dumps(
                {"class_defaults": class_defaults, "roots": roots}
            ).encode("utf-8")
        }
        return module._path_findings(paths, modes, object_ids, blobs)

    def test_absent_conditional_proposed_root_is_not_an_invariant(self) -> None:
        findings = self._findings(
            class_defaults={
                "canonical": {"status": "ACTIVE"},
                "conditional": {"status": "PROPOSED"},
            },
            roots=[
                {"class": "canonical", "path": "docs/"},
                {"class": "conditional", "path": "src/"},
            ],
        )

        identities = {(finding.rule_id, finding.subject) for finding in findings}
        self.assertNotIn(("KFM-TOPO-002", "src/"), identities)

    def test_absent_active_root_remains_a_fail_closed_invariant(self) -> None:
        findings = self._findings(
            class_defaults={"canonical": {"status": "ACTIVE"}},
            roots=[
                {"class": "canonical", "path": "docs/"},
                {"class": "canonical", "path": "packages/"},
            ],
        )

        finding = next(
            item
            for item in findings
            if (item.rule_id, item.subject) == ("KFM-TOPO-002", "packages/")
        )
        self.assertFalse(finding.baseline_allowed)
        self.assertEqual(("REGISTERED_ROOT_MISSING",), finding.evidence_members)

    def test_invalid_effective_status_fails_closed(self) -> None:
        with self.assertRaisesRegex(module.TopologyError, "status is invalid"):
            self._findings(
                class_defaults={"conditional": {"status": "MAYBE"}},
                roots=[{"class": "conditional", "path": "src/"}],
            )


if __name__ == "__main__":
    unittest.main()
