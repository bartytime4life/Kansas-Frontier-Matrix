"""Raw local HTTP envelopes cannot bootstrap owner authority from spoofed headers."""
import io
import json
import threading
import unittest
from email.message import Message
from types import SimpleNamespace
from unittest.mock import Mock

from tools.local_data import basemap_cache, earth_engine_downloads, intake_service
from tools.local_data.loopback_session import session_matches, print_connection_links
from contextlib import redirect_stdout


def request(handler, path, port, origin, token=None, method="GET", server=None):
    h = handler.__new__(handler)
    h.path = path
    h.headers = Message()
    for key, value in {"Host": f"127.0.0.1:{port}", "Origin": origin,
                       "Content-Type": "application/json", "Content-Length": "2"}.items():
        if value is not None:
            h.headers[key] = value
    if token is not None:
        h.headers["X-KFM-Session"] = token
    h.rfile = io.BytesIO(b"{}")
    h.wfile = io.BytesIO()
    h.connection = SimpleNamespace(settimeout=Mock())
    h.server = server
    output = {}
    h.send_response = lambda code: output.update(code=code)
    h.send_header = lambda *_: None
    h.end_headers = lambda: None
    getattr(h, "do_" + method)()
    return output["code"], h.wfile.getvalue()


class SessionBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.token = "t" * 43
        self.origin = "http://127.0.0.1:4173"
        self.maps = SimpleNamespace(catalog=Mock(return_value={"records": []}),
                                    health=Mock(return_value={"state": "idle"}), start=Mock())
        self.manager = SimpleNamespace(token=self.token, public_maps=self.maps, active=None,
                                       lock=threading.RLock(), health=Mock(return_value={"sessionToken": self.token}),
                                       start=Mock(return_value={"queued": True}),
                                       library=SimpleNamespace(snapshot=Mock(return_value={"state": "idle"})))
        self.desk = SimpleNamespace(token=self.token, read_only=False, catalog_only=False, status=Mock(return_value={"job": {"state": "idle"}}),
                                    start=Mock(return_value={"state": "running"}))
        self.cache = SimpleNamespace(token=self.token, status=Mock(return_value={"sessionToken": self.token}),
                                     get=Mock(return_value=(b"tile", "image/png", "hit")), start=Mock())

    def test_duplicate_headers_and_retired_capability_are_rejected(self):
        headers = Message()
        headers["X-KFM-Session"] = self.token
        self.assertTrue(session_matches(headers, self.token))
        self.assertFalse(session_matches(headers, "n" * 43))
        headers["X-KFM-Session"] = self.token
        self.assertFalse(session_matches(headers, self.token))

    def test_operator_links_carry_capability_only_in_the_fragment(self):
        output = io.StringIO()
        with redirect_stdout(output):
            print_connection_links(self.token, "downloads", earth_engine_downloads.ORIGINS)
        from urllib.parse import urlsplit
        links = output.getvalue().splitlines()[1:]
        self.assertEqual(len(links), len(earth_engine_downloads.ORIGINS))
        for link in links:
            parsed = urlsplit(link)
            self.assertEqual(parsed.fragment, "kfm-downloads=" + self.token)
            self.assertNotIn(self.token, parsed.path + parsed.query)

    def test_spoofed_headers_cannot_read_tokens_or_private_get_routes(self):
        for token in (None, "", "wrong", "\u00e9" * 43):
            for path in ("/status", "/public-maps/status", "/public-maps/catalog", "/library"):
                with self.subTest(service="downloads", path=path, token=token):
                    code, body = request(earth_engine_downloads.handler(self.manager), path, 8769, self.origin, token)
                    self.assertEqual(code, 403)
                    self.assertNotIn(self.token.encode(), body)
            for origin in (None, self.origin, intake_service.SELF_ORIGIN):
                for path in ("/api/status", "/api/overview", "/api/items", "/api/extents", "/api/atlas/catalog", "/api/budget", "/api/release-plan"):
                    with self.subTest(service="intake", path=path, origin=origin):
                        code, body = request(intake_service.handler(self.desk), path, 8771, origin, token)
                        self.assertEqual(code, 403)
                        self.assertNotIn(self.token.encode(), body)
            for path in ("/status", "/resource?url=https%3A%2F%2Fexample.test"):
                code, body = request(basemap_cache.Handler, path, 8770, self.origin, token, server=SimpleNamespace(cache=self.cache))
                self.assertEqual(code, 403)
                self.assertNotIn(self.token.encode(), body)
        self.manager.health.assert_not_called()
        self.manager.library.snapshot.assert_not_called()
        self.maps.catalog.assert_not_called()
        self.cache.status.assert_not_called()
        self.cache.get.assert_not_called()
        self.desk.status.assert_not_called()

    def test_public_desk_shell_never_contains_the_capability(self):
        for path in ("/", "/?session=anything", "/desk.js", "/desk.css"):
            code, body = request(intake_service.handler(self.desk), path, 8771, None)
            self.assertEqual(code, 200)
            self.assertNotIn(self.token.encode(), body)
            self.assertNotIn(b"__KFM_SESSION__", body)

    def test_owner_capability_preserves_status_and_bounded_mutations(self):
        self.assertEqual(request(earth_engine_downloads.handler(self.manager), "/status", 8769, self.origin, self.token)[0], 200)
        self.assertEqual(request(intake_service.handler(self.desk), "/api/status", 8771, self.origin, self.token)[0], 200)
        self.assertEqual(request(basemap_cache.Handler, "/status", 8770, self.origin, self.token, server=SimpleNamespace(cache=self.cache))[0], 200)
        for token in (None, "wrong"):
            self.assertEqual(request(earth_engine_downloads.handler(self.manager), "/downloads", 8769, self.origin, token, "POST")[0], 403)
            self.assertEqual(request(intake_service.handler(self.desk), "/api/analyze", 8771, self.origin, token, "POST")[0], 403)
            self.assertEqual(request(basemap_cache.Handler, "/overview", 8770, self.origin, token, "POST", SimpleNamespace(cache=self.cache))[0], 403)
        self.manager.start.assert_not_called()
        self.desk.start.assert_not_called()
        self.cache.start.assert_not_called()
        self.assertEqual(request(earth_engine_downloads.handler(self.manager), "/downloads", 8769, self.origin, self.token, "POST")[0], 200)
        self.assertEqual(request(intake_service.handler(self.desk), "/api/analyze", 8771, self.origin, self.token, "POST")[0], 200)
        self.manager.start.assert_called_once_with({})
        self.desk.start.assert_called_once_with({})


if __name__ == "__main__":
    unittest.main()
