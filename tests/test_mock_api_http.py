import http.client
import json
import threading
import time
import unittest
from http.server import HTTPServer

from apps.api.kfm_mock_api import Handler


class MockApiHttpTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(("127.0.0.1", 8011), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        time.sleep(0.05)

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.thread.join(timeout=1)

    def request(self, method, path, body=None):
        conn = http.client.HTTPConnection("127.0.0.1", 8011, timeout=2)
        headers = {"Content-Type": "application/json"}
        payload = json.dumps(body).encode() if body is not None else None
        conn.request(method, path, body=payload, headers=headers)
        res = conn.getresponse()
        data = json.loads(res.read().decode())
        conn.close()
        return res.status, data

    def test_healthz(self):
        status, data = self.request("GET", "/healthz")
        self.assertEqual(status, 200)
        self.assertEqual(data["status"], "ok")

    def test_unknown_evidence(self):
        status, data = self.request("GET", "/v1/evidence/nope")
        self.assertEqual(status, 404)
        self.assertEqual(data["outcome"], "ABSTAIN")

    def test_focus_empty(self):
        status, data = self.request("POST", "/v1/focus", {"question": "   "})
        self.assertEqual(status, 400)
        self.assertEqual(data["outcome"], "ABSTAIN")

    def test_focus_answer(self):
        status, data = self.request("POST", "/v1/focus", {"question": "Hydrology summary"})
        self.assertEqual(status, 200)
        self.assertEqual(data["outcome"], "ANSWER")
        self.assertTrue(data["citations"])
