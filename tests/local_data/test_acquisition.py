"""Real filesystem / injected transport checks for bounded owner downloads."""
import hashlib
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError

from tools.local_data import acquisition as a
from tools.local_data import discover_3dep as d
from tools.local_data import discover_water as w
from tools.local_data import candidate_queue as q
from tools.local_data.manage import canonical, init_store


BODY = b"remote original bytes"


def job(**changes):
    result = {"source_id": "usgs-3dep", "dataset_id": "selected-object", "label": "Selected object",
              "source_url": "https://usgs-lidar-public.s3.amazonaws.com/KS_Test/ept-data/0-0-0-0.laz",
              "scope": "kansas", "expected_bytes": len(BODY), "approved_max_bytes": None,
              "sha256": hashlib.sha256(BODY).hexdigest(), "temporal_start": None, "temporal_end": None,
              "estimate_basis": "provider", "rights_url": None}
    return {**result, **changes}


class Response(io.BytesIO):
    def __init__(self, body=b"", *, status=200, headers=None, fail_after=None):
        super().__init__(body)
        self.status = status
        self.headers = {"Content-Length": str(len(body)), "ETag": '"v1"'} if headers is None else headers
        self.fail_after = fail_after

    def read(self, size=-1):
        if self.fail_after is not None:
            if self.tell() >= self.fail_after:
                raise OSError("network interrupted with private detail")
            size = min(size, self.fail_after - self.tell())
        return super().read(size)


def transport(body=BODY, *, etag='"v1"', fail_after=None, range_valid=True):
    def call(url, method, headers):
        if method == "HEAD":
            return Response(headers={"Content-Length": str(len(body)), "ETag": etag})
        offset = int(headers.get("Range", "bytes=0-")[6:-1])
        response_headers = {"Content-Length": str(len(body) - offset), "ETag": etag}
        if offset:
            response_headers["Content-Range"] = f"bytes {offset}-{len(body)-1}/{len(body)}"
        return Response(body[offset:], status=206 if offset and range_valid else 200,
                        headers=response_headers, fail_after=fail_after)
    return call


class AcquisitionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "store"
        init_store(self.root)

    def only(self, result):
        return result["jobs"][0]

    def test_complete_verifies_and_inventory_rechecks_tampering(self):
        result = self.only(a.acquire(self.root, job(), transport=transport()))
        self.assertEqual(result["state"], "complete")
        self.assertTrue(result["checksum_verified"])
        payload = a.cache_root(self.root) / a.job_id(job()) / "payload"
        payload.write_bytes(b"tampered")
        result = self.only(a.inventory(self.root))
        self.assertEqual(result["state"], "failed")
        self.assertFalse(result["checksum_verified"])

    def test_interruption_resumes_only_verified_range(self):
        first = self.only(a.acquire(self.root, job(), transport=transport(fail_after=5)))
        self.assertEqual(first["state"], "blocked")
        self.assertEqual(first["downloaded_bytes"], 5)
        calls = []
        def resume(url, method, headers):
            calls.append((method, headers))
            return transport()(url, method, headers)
        final = self.only(a.acquire(self.root, job(), transport=resume))
        self.assertEqual(final["state"], "complete")
        self.assertEqual(calls[1][1]["Range"], "bytes=5-")
        self.assertEqual(calls[1][1]["If-Range"], '"v1"')

    def test_changed_validator_preserves_partial_and_blocks_before_get(self):
        a.acquire(self.root, job(), transport=transport(fail_after=5))
        result = self.only(a.acquire(self.root, job(), transport=transport(etag='"v2"')))
        self.assertEqual(result["reason"], "RESUME_VALIDATOR_CHANGED_OR_MISSING")
        self.assertEqual(result["downloaded_bytes"], 5)

    def test_server_ignoring_range_does_not_append(self):
        a.acquire(self.root, job(), transport=transport(fail_after=5))
        result = self.only(a.acquire(self.root, job(), transport=transport(range_valid=False)))
        self.assertEqual(result["reason"], "RESUME_RESPONSE_INVALID")
        self.assertEqual(result["downloaded_bytes"], 5)

    def test_checksum_failure_never_marks_complete(self):
        bad = job(sha256="1" * 64)
        result = self.only(a.acquire(self.root, bad, transport=transport()))
        self.assertEqual(result["state"], "failed")
        self.assertEqual(result["reason"], "CHECKSUM_MISMATCH")
        self.assertFalse((a.cache_root(self.root) / a.job_id(bad) / "payload").exists())

    def test_unknown_size_blocks_without_network_until_explicit_bound(self):
        unknown = job(expected_bytes=None)
        result = self.only(a.acquire(self.root, unknown, transport=lambda *_: self.fail("network used")))
        self.assertEqual(result["reason"], "SIZE_SELECTION_REQUIRED")
        selected = job(expected_bytes=None, approved_max_bytes=64)
        self.assertEqual(self.only(a.acquire(self.root, selected, transport=transport()))["state"], "complete")

    def test_stream_beyond_approved_bound_never_writes_over_bound(self):
        selected = job(expected_bytes=None, approved_max_bytes=6)
        def unbounded(url, method, headers):
            return Response(b"" if method == "HEAD" else BODY, headers={"ETag": '"v1"'})
        result = self.only(a.acquire(self.root, selected, transport=unbounded))
        self.assertEqual(result["reason"], "TRANSFER_BYTE_LIMIT")
        self.assertLessEqual(result["downloaded_bytes"], 6)

    def test_aggregate_cap_counts_unrecognized_files_and_no_eviction(self):
        base = a.cache_root(self.root)
        base.mkdir(mode=0o700)
        existing = base / "owner-original"
        existing.write_bytes(b"keep" * 750)
        existing.chmod(0o600)
        selected = job(expected_bytes=2000)
        with patch.object(a, "CACHE_LIMIT", 4096), patch.object(a, "METADATA_RESERVE", 128):
            result = self.only(a.acquire(self.root, selected, transport=lambda *_: self.fail("network used")))
        self.assertEqual(result["reason"], "CACHE_CAP_REACHED")
        self.assertEqual(existing.read_bytes(), b"keep" * 750)

    def test_protection_and_eviction_never_touch_originals(self):
        original = self.root / "data/raw/original"
        original.write_bytes(BODY)
        a.acquire(self.root, job(), transport=transport())
        a.cache_action(self.root, a.job_id(job()), protect=True)
        with self.assertRaisesRegex(ValueError, "PROTECTED"):
            a.cache_action(self.root, a.job_id(job()))
        self.assertEqual(original.read_bytes(), BODY)
        other = job(dataset_id="other")
        a.acquire(self.root, other, transport=transport())
        result = a.cache_action(self.root, a.job_id(other))
        evicted = next(x for x in result["jobs"] if x["job_id"] == a.job_id(other))
        self.assertEqual(evicted["reason"], "CACHE_EVICTED")
        self.assertEqual(original.read_bytes(), BODY)

    def test_symlink_and_hardlink_cache_fail_closed(self):
        base = a.cache_root(self.root)
        base.mkdir(mode=0o700)
        original = self.root / "data/raw/original"
        original.write_bytes(BODY)
        original.chmod(0o600)
        link = base / "payload"
        link.symlink_to(original)
        with self.assertRaisesRegex(ValueError, "SYMLINK"):
            a.usage(self.root)
        link.unlink()
        os.link(original, link)
        with self.assertRaisesRegex(ValueError, "HARDLINK"):
            a.usage(self.root)

    def test_paid_arbitrary_credentials_and_redirects_denied(self):
        for url in ("https://usgs-lidar.s3.amazonaws.com/x", "https://evil.test/x",
                    "https://usgs-lidar-public.s3.amazonaws.com/x?token=secret",
                    "https://u:p@usgs-lidar-public.s3.amazonaws.com/x",
                    "https://usgs-lidar-public.s3.amazonaws.com/%2e%2e/x"):
            with self.subTest(url=url), self.assertRaises(ValueError):
                a.validate_url(url)
        with self.assertRaisesRegex(ValueError, "REDIRECT_DENIED"):
            a.NoRedirect().redirect_request(None, None, 302, "", {}, "https://evil.test")

    def test_provider_quota_is_visible_block_without_retry(self):
        calls = []
        def limited(url, method, headers):
            calls.append(method)
            raise HTTPError(url, 429, "quota", {}, None)
        result = self.only(a.acquire(self.root, job(), transport=limited))
        self.assertEqual(result["reason"], "PROVIDER_RATE_LIMITED")
        self.assertEqual(calls, ["HEAD"])

    def test_exclusive_lock_prevents_concurrent_aggregate_race(self):
        with a.locked(self.root):
            with self.assertRaisesRegex(ValueError, "WORKER_BUSY"):
                a.acquire(self.root, job(), transport=lambda *_: self.fail("network used"))

    def test_plan_is_offline_and_requires_exact_schema(self):
        path = Path(self.temp.name) / "plan.json"
        path.write_bytes(canonical({"schema_version": "kfm-acquisition-plan-v1", "jobs": [job()]}))
        self.assertEqual(a.load_plan(path), [job()])
        self.assertFalse(a.cache_root(self.root).exists())
        path.write_text('{"schema_version":"x","schema_version":"y","jobs":[]}')
        with self.assertRaisesRegex(ValueError, "DUPLICATE"):
            a.load_plan(path)

    def test_owner_selected_decimal_cap_and_unfamiliar_files_block_eviction(self):
        self.assertEqual(a.CACHE_LIMIT, 100_000_000_000)
        a.acquire(self.root, job(), transport=transport())
        foreign = a.cache_root(self.root) / a.job_id(job()) / "unregistered-original"
        foreign.write_bytes(BODY)
        foreign.chmod(0o600)
        with self.assertRaisesRegex(ValueError, "UNKNOWN_CACHE_FILES"):
            a.cache_action(self.root, a.job_id(job()))
        self.assertEqual(foreign.read_bytes(), BODY)

    def test_missing_and_interrupted_payloads_are_not_complete(self):
        a.acquire(self.root, job(), transport=transport())
        base = a.cache_root(self.root) / a.job_id(job())
        (base / "payload").unlink()
        self.assertEqual(self.only(a.inventory(self.root))["state"], "failed")
        state = json.loads((base / "state.json").read_text())
        state.update(state="running", downloaded_bytes=0)
        a.save_state(base / "state.json", state)
        (base / "payload.part").write_bytes(BODY[:3])
        (base / "payload.part").chmod(0o600)
        result = self.only(a.inventory(self.root))
        self.assertEqual(result["reason"], "INTERRUPTED_RESUME_REQUIRED")
        self.assertEqual(result["downloaded_bytes"], 3)

    def test_weak_validator_cannot_resume(self):
        a.acquire(self.root, job(), transport=transport(etag='W/"v1"', fail_after=5))
        result = self.only(a.acquire(self.root, job(), transport=transport(etag='W/"v1"')))
        self.assertEqual(result["reason"], "RESUME_VALIDATOR_CHANGED_OR_MISSING")

    def test_protected_cache_is_excluded_from_replaceable_count(self):
        a.acquire(self.root, job(), transport=transport())
        a.cache_action(self.root, a.job_id(job()), protect=True)
        used = a.usage(self.root)
        self.assertGreaterEqual(used["used_bytes"], len(BODY))
        self.assertEqual(used["replaceable_bytes"], 0)

    def test_calendar_and_reversed_dates_are_invalid(self):
        for value in ("2026-02-31", "2026-01-01T27:00:00Z", "0000-01-01"):
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, "TEMPORAL_VALUE"):
                a.validate_job(job(temporal_start=value))
        with self.assertRaisesRegex(ValueError, "REVERSED"):
            a.validate_job(job(temporal_start="2026-01-02", temporal_end="2026-01-01"))
        a.validate_job(job(temporal_start="2024-02-29", temporal_end="2024-03-01T00:00:00Z"))

    def test_unknown_payload_is_used_but_never_replaceable(self):
        base = a.cache_root(self.root)
        base.mkdir(mode=0o700)
        payload = base / "payload"
        payload.write_bytes(BODY)
        payload.chmod(0o600)
        used = a.usage(self.root)
        self.assertEqual(used["used_bytes"], len(BODY))
        self.assertEqual(used["replaceable_bytes"], 0)


class DiscoveryTests(unittest.TestCase):
    def test_metadata_enumeration_never_guesses_dates_or_payload_sizes(self):
        listing = b'<ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/"><IsTruncated>false</IsTruncated><CommonPrefixes><Prefix>KS_Test_2010/</Prefix></CommonPrefixes></ListBucketResult>'
        calls = []
        def fetch(url):
            calls.append(url)
            return listing if "?" in url else b'{"dataType":"laszip","points":100,"bounds":[1.5,2,3,4,5,6]}'
        discovery, inventory, objects = d.discover(transport=fetch)
        self.assertEqual(len(calls), 2)
        self.assertEqual(discovery["project_count"], 1)
        self.assertTrue(discovery["complete_for_prefix"])
        self.assertFalse(discovery["complete_for_state"])
        self.assertIsNone(inventory["jobs"][0]["temporal_start"])
        self.assertIsNone(inventory["jobs"][0]["expected_bytes"])
        self.assertFalse(inventory["jobs"][0]["checksum_verified"])
        self.assertEqual(sum(len(value) for value in objects.values()), discovery["metadata_bytes_captured"])

    def test_listing_truncation_and_remote_prefix_injection(self):
        listing = '<ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/"><IsTruncated>true</IsTruncated></ListBucketResult>'
        result, _, _ = d.discover(transport=lambda _: listing.encode())
        self.assertFalse(result["complete_for_prefix"])
        bad = listing.replace('</ListBucketResult>', '<CommonPrefixes><Prefix>KS_../secret/</Prefix></CommonPrefixes></ListBucketResult>')
        with self.assertRaisesRegex(ValueError, "PREFIX"):
            d.discover(transport=lambda _: bad.encode())

    def test_water_period_envelopes_do_not_prove_gaps_and_next_scope_is_checked(self):
        page = {"type": "FeatureCollection", "features": [{"id": "series1", "properties": {
            "monitoring_location_id": "USGS-06892518", "begin": "1900-01-01", "end": "2026-01-01"},
            "geometry": None}], "links": []}
        result, _ = w.discover(transport=lambda _: canonical(page))
        self.assertTrue(result["complete_for_query"])
        self.assertFalse(result["records"][0]["gaps_verified"])
        page["links"] = [{"rel": "next", "href": "https://evil.test/"}]
        with self.assertRaisesRegex(ValueError, "URL_DENIED"):
            w.discover(transport=lambda _: canonical(page))

    def test_catalog_queue_has_full_options_but_never_claims_download(self):
        result = q.queue(q.ROOT / "configs/examples/acquisition-candidates.json")
        self.assertEqual(len(result["jobs"]), 26)
        self.assertEqual({j["scope"] for j in result["jobs"]}, {"kansas", "global"})
        self.assertTrue(all(j["state"] == "blocked" and j["downloaded_bytes"] == 0 for j in result["jobs"]))
        self.assertEqual(result["cache"]["limit_bytes"], 100_000_000_000)


if __name__ == "__main__":
    unittest.main()
