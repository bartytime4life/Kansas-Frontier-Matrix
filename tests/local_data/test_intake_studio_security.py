"""Wire-level header and same-origin checks using synthetic local records."""

import http.client
import io
import json
import os
import tempfile
import threading
import unittest
from contextlib import contextmanager
from pathlib import Path
from unittest.mock import patch
from urllib.parse import quote

from tests.local_data.test_intake_studio import fake_extract
from tools.local_data.intake_studio.intake_server import Handler, Server, Store


@contextmanager
def serving(server):
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield server
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


def serialized_response(body, kind="application/json", attachment=None):
    # Exercise the real stdlib HTTP serializer without opening a socket, so
    # delimiter regressions also run under the strict no-network target.
    handler = Handler.__new__(Handler)
    handler.request_version = "HTTP/1.0"
    handler.requestline = "GET / HTTP/1.0"
    handler.command = "GET"
    handler.wfile = io.BytesIO()
    handler.respond(200, body, kind, attachment)
    return handler.wfile.getvalue().split(b"\r\n\r\n", 1)


class HeaderTests(unittest.TestCase):
    def test_response_sinks_remove_literal_header_delimiters(self):
        # Deliberately call the common responder with values more permissive
        # than production routes, whose MIME and attachment names are fixed.
        for attack in [
            "\r\nX-Injected: yes",
            "\rX-Injected: yes",
            "\nX-Injected: yes",
            "\r\n\r\nHTTP/1.0 200 OK\r\nX-Injected: yes",
            "\x00\r\nX-Injected: yes",
        ]:
            with self.subTest(attack=repr(attack)):
                headers, body = serialized_response(
                    b"synthetic body", "text/plain" + attack, 'name"' + attack
                )
                lines = headers.split(b"\r\n")
                self.assertEqual(body, b"synthetic body")
                self.assertEqual(sum(line.startswith(b"HTTP/") for line in lines), 1)
                self.assertEqual(
                    sum(line.startswith(b"Content-Type:") for line in lines), 1
                )
                self.assertEqual(
                    sum(line.startswith(b"Content-Disposition:") for line in lines), 1
                )
                self.assertFalse(any(line.startswith(b"X-Injected:") for line in lines))
                self.assertNotIn(b"\x00", headers)
                for line in lines:
                    self.assertNotIn(b"\r", line)
                    self.assertNotIn(b"\n", line)

    def test_filename_controls_and_quotes_are_not_header_syntax(self):
        headers, body = serialized_response(
            b"body", attachment='a"' + "".join(map(chr, range(32))) + "\x7fb.zip"
        )
        disposition = next(
            line
            for line in headers.split(b"\r\n")
            if line.startswith(b"Content-Disposition:")
        )
        self.assertEqual(
            disposition, b'Content-Disposition: attachment; filename="a_b.zip"'
        )
        self.assertEqual(body, b"body")

    @unittest.skipIf(
        os.environ.get("KFM_NO_NETWORK") == "1",
        "Loopback HTTP is tested separately; keep the no-network guard enforced",
    )
    def test_production_routes_do_not_reflect_upload_names_into_headers(self):
        with tempfile.TemporaryDirectory() as root:
            store = Store(root, Path(root) / "missing-runtime")
            with serving(Server(0, store)) as server:

                def request(method, path, body=None, headers=None):
                    connection = http.client.HTTPConnection(
                        *server.server_address, timeout=5
                    )
                    self.addCleanup(connection.close)
                    connection.request(method, path, body=body, headers=headers or {})
                    response = connection.getresponse()
                    return response.status, dict(response.getheaders()), response.read()

                auth = {"X-KFM-Token": server.token}
                name = 'photo.png"\r\nX-Injected: yes\r\nContent-Type: text/html'
                with patch(
                    "tools.local_data.intake_studio.intake_server.subprocess.run",
                    side_effect=fake_extract,
                ):
                    status, _, body = request(
                        "POST",
                        "/api/upload?name=" + quote(name, safe=""),
                        b"\x89PNG\r\n\x1a\nsynthetic",
                        auth,
                    )
                self.assertEqual(status, 201)
                record = json.loads(body)["file"]
                for path, mime, attachment in [
                    (
                        f"/api/files/{record['id']}/original",
                        "application/octet-stream",
                        f"original-{record['id'][:8]}.png",
                    ),
                    (
                        f"/api/files/{record['id']}/export",
                        "application/zip",
                        f"kfm-held-review-{record['id'][:8]}.zip",
                    ),
                    ("/app.js", "text/javascript", None),
                ]:
                    with self.subTest(path=path):
                        status, headers, _ = request("GET", path, headers=auth)
                        self.assertEqual(status, 200)
                        # Python/platform MIME databases can also use application/javascript.
                        self.assertIn(
                            headers["Content-Type"],
                            [mime, "application/javascript"]
                            if path == "/app.js"
                            else [mime],
                        )
                        self.assertNotIn("X-Injected", headers)
                        self.assertEqual(headers["Cache-Control"], "no-store")
                        self.assertEqual(headers["X-Content-Type-Options"], "nosniff")
                        self.assertIn(
                            "frame-ancestors 'none'", headers["Content-Security-Policy"]
                        )
                        if attachment:
                            self.assertEqual(
                                headers["Content-Disposition"],
                                f'attachment; filename="{attachment}"',
                            )
                for headers in [
                    {},
                    {**auth, "Origin": "https://example.invalid"},
                    {**auth, "Host": "example.invalid"},
                    {**auth, "Sec-Fetch-Site": "cross-site"},
                ]:
                    with self.subTest(headers=headers):
                        status, _, _ = request(
                            "POST", f"/api/files/{record['id']}/review", b"{}", headers
                        )
                        self.assertEqual(status, 403)
                for path in [
                    "/api/files/%0d%0aX-Injected:yes/export",
                    "/%0d%0aX-Injected:yes",
                ]:
                    status, headers, _ = request("GET", path, headers=auth)
                    self.assertEqual(status, 404)
                    self.assertNotIn("X-Injected", headers)


if __name__ == "__main__":
    unittest.main()
