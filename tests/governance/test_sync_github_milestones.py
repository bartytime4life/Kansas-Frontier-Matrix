import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / "scripts/maintenance/sync_github_milestones.py"
MANIFEST = ROOT / "scripts/maintenance/github_milestones_m13_m24.json"
SPEC = importlib.util.spec_from_file_location("sync_github_milestones", TOOL)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class GitHubMilestoneManifestTests(unittest.TestCase):
    def test_repository_manifest_is_valid_and_complete(self):
        manifest = MODULE.load_manifest(MANIFEST)
        self.assertEqual(manifest["repository"], "bartytime4life/Kansas-Frontier-Matrix")
        self.assertEqual(
            tuple(item["id"] for item in manifest["milestones"]),
            tuple(f"M{number}" for number in range(13, 25)),
        )
        self.assertEqual(len(manifest["milestones"]), 12)
        self.assertEqual(
            sorted(
                issue
                for item in manifest["milestones"]
                for issue in item["issues"]
            ),
            [2768, 2874, 2898, 2899, 2906, 2907, 2957, 2975, 2990, 3022],
        )

    def test_duplicate_json_key_is_rejected(self):
        content = '{"schema_version":"a","schema_version":"b"}'
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "manifest.json"
            path.write_text(content, encoding="utf-8")
            with self.assertRaises(MODULE.ManifestError):
                MODULE.load_manifest(path)

    def test_duplicate_issue_mapping_is_rejected(self):
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
        data["milestones"][1]["issues"].append(data["milestones"][0]["issues"][0])
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "manifest.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaisesRegex(MODULE.ManifestError, "at most one milestone"):
                MODULE.load_manifest(path)

    def test_title_must_match_milestone_id(self):
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
        data["milestones"][0]["title"] = "M14 — Wrong prefix"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "manifest.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaisesRegex(MODULE.ManifestError, "title prefix"):
                MODULE.load_manifest(path)

    def test_default_validate_path_never_constructs_network_client(self):
        with mock.patch.object(MODULE, "GitHubClient") as client:
            exit_code = MODULE.main(["--manifest", str(MANIFEST), "validate"])
        self.assertEqual(exit_code, 0)
        client.assert_not_called()


class GitHubMilestonePlanTests(unittest.TestCase):
    def setUp(self):
        self.manifest = MODULE.load_manifest(MANIFEST)

    def test_empty_remote_state_plans_twelve_creates(self):
        actions = MODULE.build_plan(self.manifest, [])
        creates = [row for row in actions if row["action"] == "CREATE_MILESTONE"]
        self.assertEqual(len(creates), 12)

    def test_conflicting_remote_milestone_prefix_holds(self):
        remote = [
            {
                "number": 13,
                "title": "M13 — Different authority",
                "description": "conflict",
                "state": "open",
            }
        ]
        with self.assertRaisesRegex(MODULE.Hold, "different title"):
            MODULE.build_plan(self.manifest, remote)

    def test_closed_existing_milestone_holds(self):
        first = self.manifest["milestones"][0]
        remote = [
            {
                "number": 13,
                "title": first["title"],
                "description": first["description"],
                "state": "closed",
            }
        ]
        with self.assertRaisesRegex(MODULE.Hold, "not open"):
            MODULE.build_plan(self.manifest, remote)

    def test_issue_with_different_milestone_is_not_reassigned(self):
        first = self.manifest["milestones"][0]
        issues = {
            first["issues"][0]: {
                "number": first["issues"][0],
                "state": "open",
                "milestone": {"number": 99, "title": "Existing decision"},
            }
        }
        with self.assertRaisesRegex(MODULE.Hold, "already belongs"):
            MODULE.build_plan(self.manifest, [], issues)

    def test_open_unassigned_issue_plans_assignment(self):
        issue_payloads = {
            issue: {"number": issue, "state": "open", "milestone": None}
            for item in self.manifest["milestones"]
            for issue in item["issues"]
        }
        actions = MODULE.build_plan(self.manifest, [], issue_payloads)
        assignments = [row for row in actions if row["action"] == "ASSIGN_ISSUE"]
        self.assertEqual(len(assignments), 10)


if __name__ == "__main__":
    unittest.main()
