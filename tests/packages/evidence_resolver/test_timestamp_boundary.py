"""RFC 3339 offset rejection through the candidate and fixture runtime seams."""

from __future__ import annotations

import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "packages/evidence-resolver/src"))

from evidence_resolver import hydrology_fixture_adapter as adapter  # noqa: E402
from evidence_resolver.core import (  # noqa: E402
    ResolutionCandidate,
    evaluate_resolution_candidate,
    result_json,
)
from evidence_resolver.runtime_projection import (  # noqa: E402
    posture_json,
    project_runtime_posture,
)
from tests.packages.evidence_resolver import (  # noqa: E402
    test_hydrology_fixture_adapter as fixtures,
)

RESOLVED_FIXTURE = (
    REPO_ROOT / "fixtures/packages/evidence_resolver/v1alpha1/valid/resolved.json"
)


class TimestampBoundaryTests(unittest.TestCase):
    def _request(self, timestamp: str) -> dict[str, object]:
        request = json.loads(RESOLVED_FIXTURE.read_text(encoding="utf-8"))["request"]
        request["bundle_candidate"]["sensitivity"]["applied_at"] = timestamp
        return request

    def assertTimestampError(
        self, result: ResolutionCandidate, timestamp: str
    ) -> None:
        self.assertEqual("ERROR", result.status)
        self.assertEqual(
            ["schema/evidence-bundle-invalid"],
            [issue.code for issue in result.issues],
        )
        self.assertIsNone(result.bundle_id)
        runtime = project_runtime_posture(result)
        self.assertEqual("ERROR", runtime.disposition)
        self.assertFalse(runtime.as_dict()["authoritative"])
        self.assertFalse(runtime.as_dict()["renderable"])
        self.assertEqual((), runtime.required_next_checks)
        self.assertNotIn(timestamp, result_json(result))
        self.assertNotIn(timestamp, posture_json(runtime))

    def test_offsets_reject_overflowing_components(self) -> None:
        # fromisoformat normalizes +00:60 to +01:00; RFC 3339 does not.
        for sign in ("+", "-"):
            for hour in ("00", "01", "12", "22"):
                for minute in ("60", "99"):
                    timestamp = f"2026-09-05T12:00:00{sign}{hour}:{minute}"
                    with self.subTest(timestamp=timestamp):
                        request = self._request(timestamp)
                        result = evaluate_resolution_candidate(request)
                        self.assertTimestampError(result, timestamp)
                        self.assertEqual(
                            result_json(result),
                            result_json(evaluate_resolution_candidate(request)),
                        )

    def test_supported_forms_remain_non_authoritative_candidates(self) -> None:
        timestamps = (
            "2026-09-05T12:00:00Z",
            "2026-09-05t12:00:00z",
            "2026-09-05T12:00:00.123456789Z",
            "2024-02-29T12:00:00+00:00",
            "2026-09-05T12:00:00-00:00",
            "2026-09-05T12:00:00+05:30",
            "2026-09-05T12:00:00-05:45",
            "2026-09-05T12:00:00+00:59",
            "2026-09-05T12:00:00-00:59",
            "2026-09-05T12:00:00+23:59",
            "2026-09-05T12:00:00-23:59",
        )
        for timestamp in timestamps:
            with self.subTest(timestamp=timestamp):
                request = self._request(timestamp)
                original = json.dumps(request, sort_keys=True)
                result = evaluate_resolution_candidate(request)
                self.assertEqual("RESOLVED", result.status)
                self.assertEqual((), result.issues)
                runtime = project_runtime_posture(result)
                self.assertEqual("CONTINUE_GOVERNED_CHECKS", runtime.disposition)
                self.assertFalse(runtime.as_dict()["authoritative"])
                self.assertFalse(runtime.as_dict()["renderable"])
                self.assertEqual(original, json.dumps(request, sort_keys=True))

    def test_invalid_timestamp_is_error_for_every_policy_context(self) -> None:
        timestamp = "2026-09-05T12:00:00+00:60"
        for policy in ("ANSWER", "ABSTAIN", "DENY", "ERROR"):
            with self.subTest(policy=policy):
                request = self._request(timestamp)
                request["lookup_context"]["policy_outcome"] = policy
                self.assertTimestampError(
                    evaluate_resolution_candidate(request), timestamp
                )

    def test_other_invalid_forms_remain_errors(self) -> None:
        timestamps = (
            "2026-09-05T12:00:00+24:00",
            "2026-09-05T12:00:00-24:00",
            "2026-09-05T12:00:00+99:00",
            "2026-09-05T12:00:00+5:30",
            "2026-09-05T12:00:00+0530",
            "2026-09-05T12:00:00",
            "2026-09-05 12:00:00Z",
            "2026-02-29T12:00:00Z",
            "2026-09-05T24:00:00Z",
            "2026-09-05T12:60:00Z",
        )
        for timestamp in timestamps:
            with self.subTest(timestamp=timestamp):
                self.assertTimestampError(
                    evaluate_resolution_candidate(self._request(timestamp)), timestamp
                )

    def test_fixture_adapter_rejects_timestamp_after_matching_digest(self) -> None:
        # Reuse the existing adapter's synthetic request and digest helpers;
        # mutate only disposable copies, never the checked-in bundle/manifest.
        root = Path(self.enterContext(tempfile.TemporaryDirectory()))
        for relative in (fixtures.MANIFEST_RELATIVE, fixtures.BUNDLE_RELATIVE):
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(REPO_ROOT / relative, target)
        self.enterContext(mock.patch.object(adapter, "_REPOSITORY_ROOT", root))
        bundle_path = root / fixtures.BUNDLE_RELATIVE
        manifest_path = root / fixtures.MANIFEST_RELATIVE
        bundle = json.loads(bundle_path.read_text(encoding="utf-8"))
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        for timestamp in (
            "2026-09-05T12:00:00+00:60",
            "2026-09-05T12:00:00-01:99",
        ):
            with self.subTest(timestamp=timestamp):
                bundle["sensitivity"]["applied_at"] = timestamp
                bundle_path.write_text(json.dumps(bundle) + "\n", encoding="utf-8")
                manifest["entries"][0]["expected_digest"] = fixtures._digest(bundle)
                manifest_path.write_text(
                    json.dumps(manifest) + "\n", encoding="utf-8"
                )
                failed = adapter.resolve_hydrology_fixture("hb1", fixtures._request())
                self.assertTimestampError(failed.candidate, timestamp)
                self.assertEqual("ERROR", failed.runtime.disposition)
                self.assertIn(
                    "fixture_bundle_digest_binding", failed.candidate.checks_performed
                )
                self.assertNotIn(
                    "shared_hydrology_evidence_bundle_shape",
                    failed.candidate.checks_performed,
                )
                self.assertNotIn(str(root), result_json(failed.candidate))
                self.assertNotIn(
                    fixtures.BUNDLE_RELATIVE.as_posix(), result_json(failed.candidate)
                )


if __name__ == "__main__":
    unittest.main()
