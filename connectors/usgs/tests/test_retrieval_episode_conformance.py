"""Every episode shape fetch.py can emit must pass the repository contract validator.

Requires the root project dependencies (jsonschema, rfc8785); run after
``python tools/ci/install_python_ci.py project-test``. Offline and synthetic.
"""
import importlib.util
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "connectors/usgs/src"
for path in (SRC, ROOT / "packages/hashing/src"):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from hashing import compute_spec_hash  # noqa: E402
from usgs import earthquake, fetch  # noqa: E402

SPEC = importlib.util.spec_from_file_location(
    "kfm_retrieval_episode_validator",
    ROOT / "tools/validators/source/validate_source_retrieval_episode.py")
validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)

START, END = "2026-09-22T18:00:00Z", "2026-09-22T18:00:02Z"
JSON = (("Content-Type", "application/json"),)
BODY = json.dumps({"type": "FeatureCollection", "features": [],
                   "metadata": {"status": 200, "count": 0}}).encode()
EXPECTED_OUTCOME = {"CAPTURED": "PASS", "RETRY_REQUIRED": "ABSTAIN",
                    "BLOCKED": "DENY", "ERROR": "ERROR"}


def emitted():
    common = dict(source_url=earthquake.live_url(), attempted_at=START, completed_at=END,
                  spec_hash=compute_spec_hash)
    yield fetch.classify_response(status=200, body=BODY, headers=JSON + (
        ("Content-Length", str(len(BODY))), ("ETag", 'W/"v1"'),
        ("Last-Modified", "Tue, 22 Sep 2026 17:59:00 GMT")), **common)
    yield fetch.classify_response(status=200, body=BODY, headers=JSON, max_bytes=1, **common)
    yield fetch.classify_response(status=200, body=BODY, headers=JSON + (
        ("Content-Length", "1"),), **common)
    yield fetch.classify_response(status=200, body=BODY, headers=JSON + (
        ("Content-Encoding", "br"),), **common)
    yield fetch.classify_response(status=200, body=BODY, headers=(), **common)
    for status in (206, 302, 304, 401, 403, 404, 429, 451, 500, 503):
        yield fetch.classify_response(status=status, body=b"x", headers=JSON, **common)
    for failure in sorted(fetch.FAILURES):
        yield fetch.classify_response(failure=failure, retry_count=3, **common)


class ConformanceTests(unittest.TestCase):
    def test_every_category_passes_contract_semantics(self):
        categories = set()
        for retrieval in emitted():
            episode = retrieval.episode
            category = episode["transport"]["category"]
            categories.add(category)
            with self.subTest(category=category, status=episode["transport"]["http_status"]):
                result = validator.validate_payload(episode)
                findings = [f.code for f in result.findings]
                reasons = episode["result"]["reason_codes"]
                self.assertEqual(findings, [] if reasons == ["RETRIEVAL_BODY_CAPTURED"]
                                 else reasons)
                self.assertEqual(result.outcome,
                                 EXPECTED_OUTCOME[episode["result"]["status"]])
                self.assertEqual(episode["result"], validator.recompute_result(episode))
        self.assertEqual(categories, set(fetch.RESULTS) - {"NOT_MODIFIED"})

    def test_result_table_matches_validator(self):
        for category, (status, reason) in fetch.RESULTS.items():
            with self.subTest(category=category):
                self.assertEqual(
                    validator.recompute_result({"method": "GET",
                                                "transport": {"category": category}}),
                    {"status": status, "reason_codes": [reason]})


if __name__ == "__main__":
    unittest.main()
