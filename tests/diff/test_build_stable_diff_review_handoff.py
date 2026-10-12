"""Deterministic proof for the stable-diff review-handoff builder.

The tests prove local artifact/report/summary/context binding only. They do not
resolve evidence, decide policy, authenticate reviewers, approve promotion,
release, publish, or authorize public use.
"""
from __future__ import annotations

import copy
import hashlib
import json
import os
import tempfile
import unittest
from pathlib import Path

from tools.ci.build_stable_diff_review_handoff import (
    CONTEXT_SCHEMA_VERSION,
    HandoffError,
    _canonical_bytes,
    build_review_handoff,
)
from tools.ci.render_stable_diff_summary import render_stable_diff_summary
from tools.diff.stable_diff import compare_paths


def _write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, allow_nan=False, ensure_ascii=False, indent=2, sort_keys=True)
        + "\n",
        encoding="utf-8",
        newline="\n",
    )


def _sha256(raw: bytes) -> str:
    return "sha256:" + hashlib.sha256(raw).hexdigest()


class StableDiffReviewHandoffTests(unittest.TestCase):
    def setUp(self) -> None:
        self._prior_cwd = Path.cwd()
        self._temp = tempfile.TemporaryDirectory()
        self.addCleanup(self._temp.cleanup)
        self.root = Path(self._temp.name)
        os.chdir(self.root)
        self.addCleanup(os.chdir, self._prior_cwd)

        self.left = Path("fixtures/review/left.json")
        self.right = Path("fixtures/review/right.json")
        self.report = Path("artifacts/qa/stable-diff.json")
        self.summary = Path("artifacts/qa/stable-diff.md")
        self.context = Path("fixtures/review/context.json")
        self.output = Path("artifacts/qa/stable-diff-review-handoff.json")

    def _context(self, *, policy_keys: list[str] | None = None) -> dict[str, object]:
        return {
            "schema_version": CONTEXT_SCHEMA_VERSION,
            "candidate_ref": "kfm://candidate/synthetic-review/v1",
            "author_ref": "urn:kfm:actor:synthetic-author",
            "review_scope": "contract",
            "evidence_refs": ["urn:kfm:evidence:synthetic-1"],
            "basis_refs": [
                (
                    "repo:contracts/synthetic.md@sha256:"
                    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                )
            ],
            "policy_relevant_keys": (
                ["policy_state", "rights_state"]
                if policy_keys is None
                else policy_keys
            ),
            "required_reviewer_roles": [
                "contract_steward",
                "policy_steward",
            ],
            "rollback_target_ref": "urn:kfm:rollback:synthetic-1",
        }

    def _prepare(
        self,
        *,
        left: dict[str, object] | None = None,
        right: dict[str, object] | None = None,
        fail_on_change: bool = False,
        policy_keys: list[str] | None = None,
    ) -> tuple[dict[str, object], int]:
        left_value = left or {
            "policy_state": "old",
            "removed": "gone",
            "stable": "same",
        }
        right_value = right or {
            "added": "new",
            "policy_state": "new",
            "stable": "same",
        }
        _write_json(self.left, left_value)
        _write_json(self.right, right_value)
        report, exit_code = compare_paths(
            self.left,
            self.right,
            fail_on_change=fail_on_change,
        )
        _write_json(self.report, report)
        rendered = render_stable_diff_summary(self.report)
        self.summary.parent.mkdir(parents=True, exist_ok=True)
        self.summary.write_text(
            rendered.markdown,
            encoding="utf-8",
            newline="\n",
        )
        _write_json(self.context, self._context(policy_keys=policy_keys))
        return report, exit_code

    def _build(self) -> tuple[dict[str, object], int]:
        return build_review_handoff(
            left_path=self.left,
            right_path=self.right,
            report_path=self.report,
            summary_path=self.summary,
            context_path=self.context,
            output_path=self.output,
        )

    def test_changed_artifacts_emit_deterministic_review_required_handoff(self) -> None:
        report, _ = self._prepare()

        first, first_exit = self._build()
        first_bytes = self.output.read_bytes()
        second, second_exit = self._build()
        second_bytes = self.output.read_bytes()

        self.assertEqual(first_exit, 0)
        self.assertEqual(second_exit, 0)
        self.assertEqual(first, second)
        self.assertEqual(first_bytes, second_bytes)
        self.assertEqual(first["disposition"], "REVIEW_REQUIRED")
        self.assertEqual(first["bundle_summary"]["status"], "changed")
        self.assertEqual(first["bundle_summary"]["added"], report["summary"]["added"])
        self.assertEqual(first["policy_impact"]["classification"], "POTENTIAL")
        self.assertEqual(first["policy_impact"]["impacted_keys"], ["policy_state"])
        self.assertFalse(first["authority_created"])
        self.assertFalse(first["trust_boundary"]["review_authenticated"])
        self.assertEqual(
            first["review_binding"]["subject_ref"],
            first["handoff_id"],
        )

        digest_payload = copy.deepcopy(first)
        digest_payload.pop("handoff_id")
        digest_payload.pop("handoff_sha256")
        digest_payload["review_binding"].pop("subject_ref")
        self.assertEqual(first["handoff_sha256"], _sha256(_canonical_bytes(digest_payload)))

    def test_blocking_change_emits_hold_and_exit_one(self) -> None:
        self._prepare(fail_on_change=True)

        handoff, exit_code = self._build()

        self.assertEqual(exit_code, 1)
        self.assertEqual(handoff["disposition"], "HOLD")
        self.assertTrue(handoff["bundle_summary"]["blocking"])
        self.assertFalse(handoff["trust_boundary"]["promotion_authorized"])

    def test_same_artifacts_emit_no_change_and_no_policy_impact(self) -> None:
        value = {"policy_state": "same", "stable": True}
        self._prepare(left=value, right=value)

        handoff, exit_code = self._build()

        self.assertEqual(exit_code, 0)
        self.assertEqual(handoff["disposition"], "NO_CHANGE")
        self.assertEqual(handoff["policy_impact"]["classification"], "NONE")
        self.assertEqual(handoff["bundle_summary"]["total_changed_keys"], 0)

    def test_empty_policy_key_declaration_is_unknown_not_no_impact(self) -> None:
        self._prepare(policy_keys=[])

        handoff, _ = self._build()

        self.assertEqual(handoff["policy_impact"]["classification"], "UNKNOWN")
        self.assertEqual(handoff["policy_impact"]["impacted_keys"], [])

    def test_nonintersecting_policy_keys_are_bounded_no_declared_impact(self) -> None:
        self._prepare(policy_keys=["rights_state"])

        handoff, _ = self._build()

        self.assertEqual(
            handoff["policy_impact"]["classification"],
            "NO_DECLARED_IMPACT",
        )
        self.assertFalse(handoff["policy_impact"]["authority_created"])

    def test_stale_report_is_rejected_after_artifact_mutation(self) -> None:
        self._prepare()
        _write_json(
            self.right,
            {
                "policy_state": "newer",
                "stable": "same",
                "unexpected": "new-key",
            },
        )

        with self.assertRaisesRegex(
            HandoffError,
            "REPORT_ARTIFACT_BINDING_MISMATCH",
        ):
            self._build()

    def test_tampered_summary_is_rejected(self) -> None:
        self._prepare()
        self.summary.write_text(
            self.summary.read_text(encoding="utf-8") + "tampered\n",
            encoding="utf-8",
            newline="\n",
        )

        with self.assertRaisesRegex(
            HandoffError,
            "SUMMARY_REPORT_BINDING_MISMATCH",
        ):
            self._build()

    def test_noncanonical_context_array_is_rejected(self) -> None:
        self._prepare()
        context = self._context()
        context["required_reviewer_roles"] = [
            "policy_steward",
            "contract_steward",
        ]
        _write_json(self.context, context)

        with self.assertRaisesRegex(HandoffError, "ARRAY_NOT_CANONICAL"):
            self._build()

    def test_error_diff_report_fails_closed_before_review_handoff(self) -> None:
        self._prepare()
        error_report = {
            "tool": "stable-diff",
            "status": "error",
            "blocking": True,
            "left": self.left.as_posix(),
            "right": self.right.as_posix(),
            "summary": {"added": [], "removed": [], "changed": []},
            "error": {"code": "LEFT_JSON_INVALID", "message": "safe failure"},
        }
        _write_json(self.report, error_report)

        with self.assertRaisesRegex(HandoffError, "DIFF_REPORT_ERROR"):
            self._build()

    def test_input_binding_hashes_match_exact_files(self) -> None:
        self._prepare()

        handoff, _ = self._build()

        for name, path in (
            ("left", self.left),
            ("right", self.right),
            ("report", self.report),
            ("summary", self.summary),
            ("context", self.context),
        ):
            self.assertEqual(
                handoff["input_binding"][name]["sha256"],
                _sha256(path.read_bytes()),
            )
            self.assertEqual(
                handoff["input_binding"][name]["path"],
                path.as_posix(),
            )


if __name__ == "__main__":
    unittest.main()
