from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from tools.validators.control_plane.validate_program_baseline import (
    BASELINE_PATH,
    FIXTURE_ROOT,
    REPO_ROOT,
    SCHEMA_PATH,
    _check_base_path_status,
    _check_supersedes_ancestry,
    _read_pinned_blob,
    adr_index_counts,
    run_fixture_profile,
    validate_baseline,
    validate_candidate,
)

PRIOR_BASE_SHA = "6aa1ce50dfc4e818e5f33d47fff24b6d06a1c91e"


def _init_repo(root: Path) -> None:
    subprocess.run(["git", "init", "-q"], cwd=root, check=True)
    subprocess.run(["git", "config", "user.email", "fixture@example.invalid"], cwd=root, check=True)
    subprocess.run(["git", "config", "user.name", "KFM fixture"], cwd=root, check=True)


def _commit(root: Path, relative: str, content: bytes, message: str) -> str:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)
    subprocess.run(["git", "add", relative], cwd=root, check=True)
    subprocess.run(["git", "commit", "-q", "-m", message], cwd=root, check=True)
    return subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def _codes(findings: list) -> list[str]:
    return sorted({item.code for item in findings})


SYNTHETIC_INDEX = """# Index

<!-- ADR_INDEX_TABLE_START -->
| ID | Record | Effective status | Source metadata | Supersedes | Superseded by |
| --- | --- | --- | --- | --- | --- |
| `ADR-0001` | [One](./ADR-0001-one.md) | `accepted` | `accepted` | — | — |
| `ADR-0002` | [Two](./ADR-0002-two.md) | `proposed` | `draft` | — | `ADR-0004` |
| `ADR-0003` | [Three](./ADR-0003-three.md) | `rejected` | `rejected` | — | — |
| `ADR-0004` | [Four](./ADR-0004-four.md) | `proposed` | `legacy-proposed` | `ADR-0002` | — |
| `ADR-0005` | [Five](./ADR-0005-five.md) | `superseded` | `superseded` | — | — |
<!-- ADR_INDEX_TABLE_END -->

Prose mentioning | `ADR-0009` | `accepted` | outside the table is ignored.

<!-- ADR_SCAFFOLD_TABLE_START -->
| File | Classification | Decision status |
| --- | --- | --- |
| [`ADR-XXXX-a.md`](./ADR-XXXX-a.md) | explicit placeholder | `not-assigned` |
| [`ADR-b.md`](./ADR-b.md) | slug-only scaffold | `not-assigned` |
<!-- ADR_SCAFFOLD_TABLE_END -->
"""


class ProgramBaselineValidatorTests(unittest.TestCase):
    def test_schema_is_valid_draft_2020_12(self) -> None:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)

    def test_current_program_baseline_passes(self) -> None:
        result = validate_baseline(BASELINE_PATH)
        self.assertTrue(result.ok, result.findings)

    def test_fixture_profile_has_exact_positive_and_negative_polarity(self) -> None:
        document = json.loads((FIXTURE_ROOT / "cases.json").read_text(encoding="utf-8"))
        self.assertEqual(18, len(document["cases"]))
        self.assertEqual([], document["cases"][0]["expected_codes"])
        self.assertTrue(all(case["expected_codes"] for case in document["cases"][1:]))
        self.assertEqual(0, run_fixture_profile())

    def test_profile_carries_every_non_pass_observation_as_unresolved(self) -> None:
        baseline = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
        unresolved = set(baseline["unresolved_items"])
        self.assertIn("human_review_pending", unresolved)
        for item in baseline["validation_observations"]:
            if item["run_state"] in {"NOT_RUN", "SKIPPED"}:
                self.assertEqual(item["run_state"], item["outcome"])
            if item["outcome"] != "PASS":
                self.assertIn(f"{item['id']}_{item['outcome'].lower()}", unresolved)

    def test_profile_binds_sorted_review_queue_and_tracker_staleness(self) -> None:
        baseline = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
        open_prs = baseline["base"]["open_pull_requests"]
        self.assertEqual(sorted(set(open_prs)), open_prs)
        self.assertEqual([2768, 2874, 3365], [item["number"] for item in baseline["tracker_snapshot"]])
        for item in baseline["tracker_snapshot"]:
            self.assertEqual(
                item["recorded_baseline_sha"] != baseline["base"]["sha"],
                item["stale_at_base"],
            )

    def test_profile_supersedes_prior_baseline_and_rolls_back_to_its_own_base(self) -> None:
        baseline = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
        self.assertEqual(
            {"baseline_id": "kfm-program-baseline-main-6aa1ce50dfc4", "base_sha": PRIOR_BASE_SHA},
            baseline["supersedes"],
        )
        self.assertEqual("PRESENT", baseline["placement"]["base_path_status"])
        self.assertEqual(f"git:{baseline['base']['sha']}", baseline["correction"]["rollback_target"])

    def test_retired_v1_profile_fails_with_one_stable_code(self) -> None:
        candidate = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
        candidate["schema_version"] = "1.0.0"
        candidate["profile"] = "kfm.program-baseline.m01.v1"
        result = validate_candidate(candidate, check_paths=False, check_git=False)
        self.assertEqual(["PROFILE_VERSION_UNSUPPORTED"], [item.code for item in result.findings])

    def test_unresolved_rule_tracks_each_non_pass_outcome(self) -> None:
        candidate = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
        index = next(
            position
            for position, item in enumerate(candidate["validation_observations"])
            if item["outcome"] == "PASS"
        )
        observation = candidate["validation_observations"][index]
        observation.update({"run_state": "SKIPPED", "outcome": "SKIPPED"})
        missing = validate_candidate(candidate, check_paths=False, check_git=False)
        self.assertEqual(["REQUIRED_UNRESOLVED_ITEM_MISSING"], _codes(list(missing.findings)))
        candidate["unresolved_items"] = sorted(
            candidate["unresolved_items"] + [f"{observation['id']}_skipped"]
        )
        carried = validate_candidate(candidate, check_paths=False, check_git=False)
        self.assertTrue(carried.ok, carried.findings)
        observation.update({"run_state": "EXECUTED", "outcome": "PASS"})
        stale = validate_candidate(candidate, check_paths=False, check_git=False)
        self.assertEqual(["UNRESOLVED_ITEM_STALE"], _codes(list(stale.findings)))

    def test_adr_index_counts_follow_effective_status_column(self) -> None:
        counts = adr_index_counts(SYNTHETIC_INDEX.encode("utf-8"))
        self.assertIsNotNone(counts)
        self.assertEqual(frozenset({"ADR-0001"}), counts.accepted_ids)
        self.assertEqual(2, counts.proposed_count)
        self.assertEqual(2, counts.scaffold_count)

    def test_adr_index_counts_fail_closed_on_malformed_tables(self) -> None:
        malformed = {
            "missing_marker": SYNTHETIC_INDEX.replace("<!-- ADR_INDEX_TABLE_END -->", ""),
            "unknown_status": SYNTHETIC_INDEX.replace("| `rejected` | `rejected` |", "| `withdrawn` | `rejected` |"),
            "duplicate_id": SYNTHETIC_INDEX.replace("`ADR-0004`", "`ADR-0001`"),
            "wrong_header": SYNTHETIC_INDEX.replace("| ID | Record |", "| Id | Record |"),
            "missing_scaffold_table": SYNTHETIC_INDEX.replace("<!-- ADR_SCAFFOLD_TABLE_START -->", ""),
            "not_utf8": None,
        }
        for name, text in malformed.items():
            with self.subTest(name=name):
                data = b"\xff\xfe" if text is None else text.encode("utf-8")
                self.assertIsNone(adr_index_counts(data))

    def test_adr_index_rule_reproduces_prior_hand_recorded_counts(self) -> None:
        blob = subprocess.run(
            ["git", "show", f"{PRIOR_BASE_SHA}:docs/adr/INDEX.md"],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
        ).stdout
        counts = adr_index_counts(blob)
        self.assertIsNotNone(counts)
        self.assertEqual(
            (frozenset({"ADR-0006", "ADR-0007", "ADR-0029"}), 33, 12),
            (counts.accepted_ids, counts.proposed_count, counts.scaffold_count),
        )

    def test_base_path_status_agrees_with_pinned_tree(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            _init_repo(root)
            before = _commit(root, "control_plane/README.md", b"readme\n", "before")
            after = _commit(root, "control_plane/program_baseline.json", b"{}\n", "after")
            outcomes = {}
            for label, sha in (("before", before), ("after", after)):
                for status in ("ABSENT", "PRESENT"):
                    findings = []
                    _check_base_path_status(
                        root,
                        base_sha=sha,
                        canonical_path="control_plane/program_baseline.json",
                        status=status,
                        findings=findings,
                    )
                    outcomes[(label, status)] = _codes(findings)
        self.assertEqual([], outcomes[("before", "ABSENT")])
        self.assertEqual(["BASE_PATH_STATUS_MISMATCH"], outcomes[("before", "PRESENT")])
        self.assertEqual([], outcomes[("after", "PRESENT")])
        self.assertEqual(["BASE_PATH_STATUS_MISMATCH"], outcomes[("after", "ABSENT")])

    def test_supersedes_requires_git_ancestry(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            _init_repo(root)
            first = _commit(root, "control_plane/a.json", b"a\n", "first")
            second = _commit(root, "control_plane/b.json", b"b\n", "second")
            subprocess.run(["git", "checkout", "-q", "-b", "side", first], cwd=root, check=True)
            side = _commit(root, "control_plane/c.json", b"c\n", "side")
            outcomes = {}
            for label, superseded, base in (
                ("ancestor", first, second),
                ("descendant", second, first),
                ("unrelated", side, second),
                ("unknown", "1" * 40, second),
            ):
                findings = []
                _check_supersedes_ancestry(
                    root,
                    superseded_sha=superseded,
                    base_sha=base,
                    findings=findings,
                )
                outcomes[label] = _codes(findings)
        self.assertEqual([], outcomes["ancestor"])
        self.assertEqual(["SUPERSEDED_BASE_NOT_ANCESTOR"], outcomes["descendant"])
        self.assertEqual(["SUPERSEDED_BASE_NOT_ANCESTOR"], outcomes["unrelated"])
        self.assertEqual(["SUPERSEDED_BASE_COMMIT_NOT_FOUND"], outcomes["unknown"])

    def test_profile_keeps_drive_lineage_non_authoritative_and_unmodified(self) -> None:
        baseline = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
        self.assertEqual(3, len(baseline["drive_lineage"]))
        self.assertTrue(
            all(
                item["repository_authority"] is False and item["mutated"] is False
                for item in baseline["drive_lineage"]
            )
        )

    def test_unknown_field_fails_schema(self) -> None:
        candidate = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
        candidate["self_approval"] = True
        result = validate_candidate(candidate, check_paths=False, check_git=False)
        self.assertIn("SCHEMA_INVALID", {item.code for item in result.findings})

    def test_duplicate_keys_and_nonfinite_numbers_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            duplicate = Path(directory) / "duplicate.json"
            duplicate.write_text('{"schema_version":"1.0.0","schema_version":"2.0.0"}', encoding="utf-8")
            nonfinite = Path(directory) / "nonfinite.json"
            nonfinite.write_text('{"value":NaN}', encoding="utf-8")
            duplicate_result = validate_baseline(duplicate, check_paths=False, check_git=False)
            nonfinite_result = validate_baseline(nonfinite, check_paths=False, check_git=False)
        self.assertEqual(["JSON_DUPLICATE_KEY"], sorted({item.code for item in duplicate_result.findings}))
        self.assertEqual(["JSON_NONFINITE_NUMBER"], sorted({item.code for item in nonfinite_result.findings}))

    def test_pinned_digest_replay_ignores_later_worktree_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            _init_repo(root)
            path = root / "control_plane/example.json"
            path.parent.mkdir(parents=True)
            path.write_bytes(b"pinned-program-baseline-bytes\n")
            subprocess.run(["git", "add", "control_plane/example.json"], cwd=root, check=True)
            subprocess.run(["git", "commit", "-q", "-m", "fixture baseline"], cwd=root, check=True)
            base_sha = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                cwd=root,
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip()
            path.write_bytes(b"later-worktree-bytes\n")
            findings = []
            observed = _read_pinned_blob(
                "control_plane/example.json",
                base_sha=base_sha,
                repo_root=root,
                field="/fixture/path",
                expected_prefixes=("control_plane/",),
                findings=findings,
            )
        self.assertEqual(b"pinned-program-baseline-bytes\n", observed)
        self.assertEqual([], findings)

    def test_cli_does_not_echo_untrusted_values(self) -> None:
        marker = "synthetic-sensitive-marker-must-not-echo"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "untrusted.json"
            path.write_text(json.dumps({"unexpected": marker}), encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable,
                    "tools/validators/control_plane/validate_program_baseline.py",
                    str(path),
                    "--skip-path-existence",
                    "--skip-git-commit",
                ],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertEqual(1, result.returncode)
        self.assertNotIn(marker, result.stdout + result.stderr)
        self.assertIn("SCHEMA_INVALID", result.stdout)


if __name__ == "__main__":
    unittest.main()
