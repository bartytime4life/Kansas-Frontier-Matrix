"""Exercise public-map requests through the actual loopback HTTP handler."""
import io
import json
from email.message import Message
from types import SimpleNamespace
import threading
import unittest
from unittest.mock import Mock

from tools.local_data import earth_engine_downloads as service


class PublicMapControlTests(unittest.TestCase):
    def setUp(self):
        self.maps = SimpleNamespace(catalog=Mock(return_value={"records": []}), health=Mock(return_value={"schema": "kfm-public-map-download-control/v1"}),
                                    start=Mock(return_value={"id": "job"}), cancel=Mock(return_value={"cancelling": "job"}), refresh=Mock(return_value={"state": "running"}),
                                    enqueue=Mock(return_value={"batchId": "b" * 32}), cancel_queue=Mock(return_value={"cancelledQueued": 0}))
        self.manager = SimpleNamespace(token="test-token", public_maps=self.maps, active=None, lock=threading.RLock(), start=Mock(), health=Mock(return_value={"configured": False}))

    def request(self, method, path, body=None, headers=None):
        Handler = service.handler(self.manager)
        h = Handler.__new__(Handler)
        encoded = json.dumps({} if body is None else body).encode()
        h.headers = Message()
        values = {"Host": "127.0.0.1:8769", "Origin": "http://127.0.0.1:4173", "X-KFM-Session": "test-token", "Content-Type": "application/json", "Content-Length": str(len(encoded))}
        values.update(headers or {})
        for key, value in values.items(): h.headers[key] = value
        h.path = path
        h.rfile = io.BytesIO(encoded); h.wfile = io.BytesIO(); h.connection = SimpleNamespace(settimeout=Mock())
        h.send_response = Mock(); h.send_header = Mock(); h.end_headers = Mock()
        getattr(h, "do_" + method)()
        return h.send_response.call_args.args[0], json.loads(h.wfile.getvalue())

    def test_catalog_status_and_downloads_are_separate_from_earth_engine(self):
        self.assertEqual(self.request("GET", "/public-maps/catalog"), (200, {"records": []}))
        status, body = self.request("GET", "/public-maps/status")
        self.assertEqual(status, 200); self.assertEqual(body["sessionToken"], "test-token")
        selection = {"requestId": "a" * 32, "assetId": "kgs-m118-pdf", "maxBytes": 40_000_000}
        self.assertEqual(self.request("POST", "/public-maps/downloads", selection)[0], 200)
        self.maps.start.assert_called_once_with(selection)
        self.manager.start.assert_not_called()
        self.assertEqual(self.request("POST", "/public-maps/cancel", {"id": "job"})[0], 200)
        self.maps.cancel.assert_called_once_with("job")

    def test_origin_session_and_request_envelope_precede_all_side_effects(self):
        for headers in [{"Origin": "https://unapproved.example"}, {"X-KFM-Session": "wrong"}, {"Host": "unapproved.example"}]:
            self.assertEqual(self.request("POST", "/public-maps/refresh", headers=headers)[0], 403)
        self.assertEqual(self.request("POST", "/public-maps/refresh", {"unexpected": True})[0], 400)
        self.assertEqual(self.request("POST", "/public-maps/downloads", headers={"Content-Length": "16385"})[0], 400)
        self.assertEqual(self.request("POST", "/public-maps/downloads", headers={"Transfer-Encoding": "chunked"})[0], 415)
        self.maps.refresh.assert_not_called(); self.maps.start.assert_not_called()
        self.assertEqual(self.request("POST", "/public-maps/refresh")[0], 200)

    def test_active_earth_engine_transfer_blocks_map_transfer(self):
        self.manager.active = "earth-engine-job"
        status, body = self.request("POST", "/public-maps/downloads")
        self.assertEqual(status, 400); self.assertEqual(body["error"], "DOWNLOAD_ALREADY_RUNNING")
        self.maps.start.assert_not_called()


    def test_queue_routes_require_the_session_and_respect_earth_engine_transfers(self):
        selection = {"requestId": "a" * 32, "assetIds": ["publisher-noaa-storm-events-2024-details"], "maxBytes": 80_000_000}
        self.assertEqual(self.request("POST", "/public-maps/queue", selection, headers={"X-KFM-Session": "wrong"})[0], 403)
        self.maps.enqueue.assert_not_called()
        self.assertEqual(self.request("POST", "/public-maps/queue", selection)[0], 200)
        self.maps.enqueue.assert_called_once_with(selection)
        self.assertEqual(self.request("POST", "/public-maps/queue/cancel", {"unexpected": True})[0], 400)
        self.assertEqual(self.request("POST", "/public-maps/queue/cancel")[0], 200)
        self.maps.cancel_queue.assert_called_once_with()
        self.manager.active = "earth-engine-job"
        status, body = self.request("POST", "/public-maps/queue", selection)
        self.assertEqual((status, body["error"]), (400, "DOWNLOAD_ALREADY_RUNNING"))
        self.assertEqual(self.maps.enqueue.call_count, 1)


if __name__ == "__main__": unittest.main()
