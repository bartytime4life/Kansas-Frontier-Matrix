"""Offline tests for the restored local operator; no Google login or transfers."""
import hashlib
import io
import json
from email.message import Message
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch
from urllib.parse import parse_qs, urlencode, urlsplit

from connectors.google.earth_engine import download as source
from tools.local_data import earth_engine_auth as auth
from tools.local_data import earth_engine_downloads as operator
from tools.local_data.manage import init_store


def selection(dataset="ee-cdl", year=2024, maximum=32_000_000):
    return {"dataset": dataset, "year": year, "maxBytes": maximum}


class Info:
    def __init__(self, value): self.value = value
    def getInfo(self): return self.value


class Collection:
    def __init__(self, metadata): self.metadata = metadata
    def filter(self, *_): return self
    def filterBounds(self, *_): return self
    def filterDate(self, *_): return self
    def sort(self, *_): return self
    def geometry(self): return self
    def size(self): return Info(len(self.metadata["ids"]))
    def aggregate_array(self, field):
        return self.metadata[{"system:id": "ids", "system:index": "labels", "system:time_start": "times"}[field]]


def fake_ee(asset, labels):
    collection = Collection({"ids": [asset + "/" + name for name in labels], "labels": labels, "times": [0] * len(labels)})
    return SimpleNamespace(FeatureCollection=lambda _: collection, ImageCollection=lambda _: collection,
        Filter=SimpleNamespace(eq=lambda *_: None, gte=lambda *_: None, lt=lambda *_: None), Dictionary=Info)


class SourceTests(unittest.TestCase):
    def test_catalog_selection_requires_exact_fields_known_years_and_owner_limit(self):
        self.assertEqual(len(source.SPECS), 17)
        self.assertEqual(source.selection(selection())["period"], "2024")
        self.assertEqual(source.selection(selection("ee-3dep", None))["period"], "fixed")
        for value in [selection(year=True), selection(year=2025), selection(maximum=True), selection(maximum=source.MAX_BYTES + 1),
                      selection("other"), selection("ee-3dep", 2024), {**selection(), "path": "/outside"}]:
            with self.subTest(value=value), self.assertRaises(ValueError): source.selection(value)

    def test_grid_caps_and_exact_calendar_periods(self):
        self.assertEqual(len(source.expected_dates("ee-prism-daily", 2024)), 366)
        self.assertEqual(len(source.expected_dates("ee-prism-monthly", 1895)), 12)
        windows = source.tiles([0, 0, 1500, 1500], [1, 0, 0, 0, -1, 1500])
        self.assertEqual(len(windows), 4)
        self.assertEqual(sum(x["dimensions"][0] * x["dimensions"][1] for x in windows), 1500 * 1500)
        for bounds in [[0, 0, 0, 1], [float("nan"), 0, 1, 1], [0, 0, 100000, 100000]]:
            with self.assertRaises(ValueError): source.tiles(bounds, [1, 0, 0, 0, -1, 100000])

    def test_inventory_capture_preserves_source_ids_and_unreviewed_role(self):
        plan = selection("ee-landsat-mss", 1973)
        files, updates = {}, []
        ee = fake_ee(source.SPECS[plan["dataset"]][0], ["first", "second"])
        metadata = source.capture(plan, ee, lambda name, body: files.update({name: body}), lambda **fields: updates.append(fields), lambda: False)
        self.assertEqual(set(files), {"source-inventory.json"})
        self.assertEqual(len(metadata["source_inventory"]), 2)
        self.assertEqual(metadata["admission"], "NOT_ADMITTED")
        self.assertEqual(metadata["review"], "UNREVIEWED")
        self.assertFalse(updates[-1]["mapReady"])

    def test_incomplete_period_and_cancel_fail_before_any_capture(self):
        write = Mock()
        ee = fake_ee(source.SPECS["ee-prism-monthly"][0], ["202401"])
        with self.assertRaisesRegex(ValueError, "SOURCE_PERIOD_INCOMPLETE"):
            source.capture(selection("ee-prism-monthly", 2024), ee, write, Mock(), lambda: False)
        with self.assertRaisesRegex(ValueError, "CANCELLED"):
            source.capture(selection(), None, write, Mock(), lambda: True)
        write.assert_not_called()

    def test_download_rejects_arbitrary_hosts_redirects_oversize_and_non_tiff(self):
        with patch.object(source, "build_opener") as opener:
            for url in ["http://earthengine.googleapis.com/v1/test", "https://evil.example/v1/test", "https://earthengine.googleapis.com/private"]:
                with self.assertRaisesRegex(ValueError, "DOWNLOAD_ORIGIN_REJECTED"): source.fetch_tile(url, 8)
            opener.assert_not_called()
        with self.assertRaisesRegex(ValueError, "REDIRECT"): source.NoRedirect().redirect_request()
        for payload, length, accepted in [(b"II*\0abcd", "8", True), (b"II*\0abcde", None, False), (b"bad", "3", False)]:
            response = io.BytesIO(payload); response.status = 200
            response.headers = {} if length is None else {"Content-Length": length}
            with patch.object(source, "build_opener", return_value=SimpleNamespace(open=lambda *_a, **_kw: response)):
                if accepted: self.assertEqual(source.fetch_tile("https://earthengine.googleapis.com/v1/test", 8), payload)
                else:
                    with self.assertRaises(ValueError): source.fetch_tile("https://earthengine.googleapis.com/v1/test", 8)


class OperatorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.root = Path(self.tmp.name) / "store"
        init_store(self.root)
        self.manager = operator.Downloads(self.root)

    def tearDown(self): self.tmp.cleanup()

    def start(self, request_id="a" * 32):
        with patch.object(self.manager, "health", return_value={"configured": True}), patch.object(operator.threading, "Thread") as thread:
            result = self.manager.start({"selection": selection(), "requestId": request_id})
            self.assertEqual(thread.call_count, 1)
            return result

    def test_unconfigured_start_never_creates_a_job(self):
        with patch.object(self.manager, "health", return_value={"configured": False}):
            with self.assertRaisesRegex(ValueError, "SETUP_REQUIRED"): self.manager.start({"selection": selection(), "requestId": "a" * 32})
        self.assertEqual(self.manager.jobs, {})

    def test_idempotent_start_single_active_job_conflict_and_cancellation(self):
        first = self.start()
        self.assertEqual(self.manager.start({"selection": selection(), "requestId": first["id"]}), first)
        self.assertTrue(Path(first["destination"]).is_dir())
        for request, message in [({"selection": selection(year=2023), "requestId": first["id"]}, "REQUEST_ID_CONFLICT"),
                                 ({"selection": selection(), "requestId": "b" * 32}, "DOWNLOAD_ALREADY_RUNNING")]:
            with self.assertRaisesRegex(ValueError, message): self.manager.start(request)
        with self.assertRaisesRegex(ValueError, "NO_ACTIVE_DOWNLOAD"): self.manager.cancel("b" * 32)
        self.manager.cancel(first["id"]); self.assertTrue(self.manager.cancel_event.is_set())

    def test_restart_marks_interrupted_without_losing_captured_files(self):
        first = self.start(); original = Path(first["destination"]) / "source-inventory.json"
        original.write_text("original")
        restored = operator.Downloads(self.root)
        self.assertEqual(restored.jobs[first["id"]]["state"], "interrupted")
        self.assertEqual(original.read_text(), "original")
        self.assertIsNone(restored.active)

    def test_partial_capture_receipt_retains_exact_hash_and_never_becomes_map_ready(self):
        first = self.start(); payload = b"II*\0synthetic"
        def capture(_request, _ee, write, _update, _cancelled):
            write("tile-0000.tif", payload)
            raise ValueError("CANCELLED")
        ee = SimpleNamespace(data=SimpleNamespace(setDeadline=Mock()), Initialize=Mock())
        with patch.dict("sys.modules", {"ee": ee}), patch.object(operator, "ee_credentials", return_value=None), \
             patch.object(self.manager, "configuration", return_value={"project": "example-project"}), patch.object(operator, "capture", side_effect=capture):
            self.manager.run(first["id"], Path(first["destination"]))
        receipt = json.loads((self.manager.receipts / (first["id"] + ".json")).read_bytes())
        self.assertEqual(receipt["job"]["state"], "cancelled")
        self.assertEqual(receipt["files"][0]["sha256"], hashlib.sha256(payload).hexdigest())
        self.assertFalse(receipt["job"]["mapReady"])
        self.assertFalse(receipt["providerChecksumVerified"])
        self.assertEqual(receipt["release"], "NOT_RELEASED")
        self.assertIsNone(self.manager.active)

    def test_status_omits_private_credential_contents(self):
        with patch.object(operator.importlib.util, "find_spec", return_value=None), patch.object(Path, "home", return_value=self.root):
            status = self.manager.health()
        self.assertFalse(status["configured"])
        self.assertFalse(status["credentialsPresent"])
        self.assertEqual(status["authentication"], "idle")
        self.assertEqual(status["jobs"], [])
        self.assertEqual(status["destination"], str(self.manager.raw))


class EnvelopeTests(unittest.TestCase):
    def test_options_rejects_malformed_headers_without_reflecting_them(self):
        Handler = operator.handler(SimpleNamespace())
        origin = "http://127.0.0.1:4173"
        host = f"127.0.0.1:{operator.PORT}"
        def request(origin_value=origin, host_value=host):
            h = Handler.__new__(Handler); h.headers = Message(); h.path = "/status"
            h.request_version = "HTTP/1.1"; h.requestline = "OPTIONS /status HTTP/1.1"; h.command = "OPTIONS"
            if origin_value is not None: h.headers["Origin"] = origin_value
            if host_value is not None: h.headers["Host"] = host_value
            h.wfile = io.BytesIO()
            h.do_OPTIONS()
            return h.wfile.getvalue()
        accepted = request()
        self.assertIn(b" 204 ", accepted.split(b"\r\n", 1)[0])
        self.assertIn(b"Access-Control-Allow-Origin: " + origin.encode() + b"\r\n", accepted)
        self.assertIn(b"Access-Control-Allow-Private-Network: true\r\n", accepted)
        for bad_origin, bad_host in [(None, host), ("https://evil.example", host),
                                      (origin + "\r\nX-Injected: true", host),
                                      (origin, None), (origin, "localhost:8769"),
                                      (origin, host + "\r\nX-Injected: true")]:
            with self.subTest(origin=bad_origin, host=bad_host):
                rejected = request(bad_origin, bad_host)
                self.assertIn(b" 403 ", rejected.split(b"\r\n", 1)[0])
                self.assertNotIn(b"X-Injected:", rejected)
                if bad_origin != origin: self.assertNotIn(b"Access-Control-Allow-Origin:", rejected)
        # Even an accidental unsafe allowlist entry must never become a response header.
        for suffix in ("\rX-Injected: true", "\nX-Injected: true", "\r\nX-Injected: true"):
            unsafe = origin + suffix
            with patch.object(operator, "ORIGINS", {origin, unsafe}):
                rejected = request(unsafe)
                self.assertIn(b" 403 ", rejected.split(b"\r\n", 1)[0])
                self.assertNotIn(b"Access-Control-Allow-Origin:", rejected)
                self.assertNotIn(b"X-Injected:", rejected)

    def test_origin_host_session_and_body_limits_precede_actions(self):
        manager = SimpleNamespace(token="test-token", health=Mock(return_value={"configured": False}), start=Mock(return_value={"queued": True}), cancel=Mock())
        Handler = operator.handler(manager)
        def request(method="GET", path="/status", headers=None, body=b"{}"):
            h = Handler.__new__(Handler); h.headers = Message(); h.path = path
            values = {"Host": f"127.0.0.1:{operator.PORT}", "Origin": "http://127.0.0.1:4173", "X-KFM-Session": manager.token,
                      "Content-Type": "application/json", "Content-Length": str(len(body)), **(headers or {})}
            for key, value in values.items(): h.headers[key] = value
            h.rfile = io.BytesIO(body); h.wfile = io.BytesIO(); h.connection = SimpleNamespace(settimeout=Mock())
            result = {}; h.send_response = lambda code: result.update(status=code); h.send_header = lambda *_: None; h.end_headers = lambda: None
            getattr(h, "do_" + method)(); return result["status"]
        self.assertEqual(request(), 200)
        for headers in [{"Origin": "https://evil.example"}, {"Host": "evil.example"}, {"Origin": "http://127.0.0.1:4173\r\nX: injected"}, {"X-KFM-Session": "wrong"}]:
            self.assertEqual(request("POST", "/downloads", headers), 403)
        self.assertEqual(request("POST", "/downloads", {"Content-Length": "16385"}), 400)
        self.assertEqual(request("POST", "/downloads", {"Transfer-Encoding": "chunked"}), 415)
        manager.start.assert_not_called()
        self.assertEqual(request("POST", "/downloads"), 200); manager.start.assert_called_once_with({})


class SignInTests(unittest.TestCase):
    def test_pkce_state_one_time_claim_and_expiry_without_provider_calls(self):
        oauth = SimpleNamespace(get_authorization_url=Mock(return_value="https://accounts.google.com/o/oauth2/auth?code_challenge=synthetic"))
        signin = auth.SignIn(Path("/not-used"))
        with patch.dict("sys.modules", {"ee": SimpleNamespace(oauth=oauth)}):
            first = signin.start({"project": "example-project"})
            self.assertEqual(signin.start({"project": "example-project"}), first)
            self.assertEqual(oauth.get_authorization_url.call_count, 1)
            self.assertEqual(len(oauth.get_authorization_url.call_args.args[0]), 43)
            state = parse_qs(urlsplit(first["url"]).query)["state"][0]
            with self.assertRaisesRegex(ValueError, "OAUTH_STATE"): signin.claim("state=wrong&code=test")
            claimed = signin.claim(urlencode({"state": state, "code": "test-code"}))
            self.assertEqual(claimed[1], "test-code"); self.assertEqual(signin.status(), "validating")
            with self.assertRaisesRegex(ValueError, "OAUTH_STATE"): signin.claim(urlencode({"state": state, "code": "test-code"}))
            another = auth.SignIn(Path("/not-used")); another.start({"project": "example-project"})
            with patch.object(auth.time, "monotonic", return_value=another.pending["expires"] + 1):
                self.assertEqual(another.status(), "expired"); self.assertIsNone(another.pending)


if __name__ == "__main__": unittest.main()
