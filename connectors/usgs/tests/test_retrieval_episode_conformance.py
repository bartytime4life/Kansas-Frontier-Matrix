"""Every episode shape fetch.py can emit must pass the repository contract validator.

Requires the root project dependencies (jsonschema, rfc8785); run after
``python tools/ci/install_python_ci.py project-test``. Offline and synthetic.
"""
import importlib.util
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
for path in (ROOT / "connectors/usgs/tests", ROOT / "packages/hashing/src"):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import test_fetch_admit as support  # noqa: E402  (also puts usgs and connectors_core on the path)
from connectors_core import core as cc  # noqa: E402
from hashing import compute_spec_hash  # noqa: E402
from usgs import earthquake, fetch  # noqa: E402

SPEC = importlib.util.spec_from_file_location(
    "kfm_retrieval_episode_validator",
    ROOT / "tools/validators/source/validate_source_retrieval_episode.py")
validator = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = validator
SPEC.loader.exec_module(validator)

EXPECTED_OUTCOME = {"CAPTURED": "PASS", "RETRY_REQUIRED": "ABSTAIN",
                    "BLOCKED": "DENY", "ERROR": "ERROR"}


class Cancelled:
    def is_cancelled(self):
        return True


def run(*outcomes, **kwargs):
    clock = support.Clock()
    kwargs.setdefault("retry_policy", cc.RetryPolicy(max_attempts=2))
    return fetch.retrieve(earthquake.live_url(), transport=support.Transport(clock, *outcomes),
                          clock=clock, sleeper=support.Sleeper(clock),
                          spec_hash=compute_spec_hash, **kwargs)


def emitted():
    response, data = support.response, support.body()
    yield run(response(payload=data, headers={
        "ETag": 'W/"v1"', "Last-Modified": "Tue, 22 Sep 2026 17:59:00 GMT"}))
    yield run(response(503, b"busy"), response())
    yield run(response(payload=data), max_bytes=len(data) - 1)
    yield run(response(headers={"Content-Type": "text/html"}))
    yield run(response(headers={"Content-Length": "1"}))
    yield run(response(url="https://earthquake.usgs.gov/elsewhere"))
    for status in (302, 304, 401, 403, 404, 451):
        yield run(response(status, b"" if status == 304 else b"x"))
    for status in (206, 429, 500, 503):
        yield run(response(status, b"x"), response(status, b"x"))
    yield run(TimeoutError(), TimeoutError())
    yield run(cancellation=Cancelled())


class ConformanceTests(unittest.TestCase):
    def test_every_emitted_episode_passes_contract_semantics(self):
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
                self.assertEqual(result.outcome, EXPECTED_OUTCOME[episode["result"]["status"]])
                self.assertEqual(episode["result"], validator.recompute_result(episode))
        self.assertEqual(categories, {"SUCCESS", "RESPONSE_TOO_LARGE", "INVALID_RESPONSE_METADATA",
                                      "UNSAFE_METADATA", "AUTH_REQUIRED", "ACCESS_DENIED",
                                      "NOT_FOUND", "RETRY_EXHAUSTED", "CANCELLED"})


if __name__ == "__main__":
    unittest.main()
