"""Actual loopback HTTP rehearsal with explicitly synthetic release metadata."""
from datetime import datetime, timezone
import json
import sqlite3
from threading import Thread
from urllib.request import urlopen
from wsgiref.simple_server import make_server, WSGIRequestHandler

from connectors_core.captured_json import canonical_bytes
from governed_api import main, water
from release.local_admin import stage, activate
from release.local_store import LocalReleaseStore
from pipelines.domains.hydrology.validate import validate_candidate
from tests.packages.release.test_water_snapshot import synthetic_snapshot, synthetic_decision, NOW


def test_http_selection_evidence_withdrawal_and_health(tmp_path, monkeypatch):
    snapshot = synthetic_snapshot(cleared=True)
    root = tmp_path / "synthetic-serving"
    package_id = stage(root, canonical_bytes(snapshot), actor="synthetic-owner", now=NOW, validator=validate_candidate)
    activate(root, package_id, synthetic_decision(snapshot), expected_active=None, now=NOW, validator=validate_candidate)
    monkeypatch.setattr(main, "_RELEASE_STORE", LocalReleaseStore(str(root)))
    class Clock:
        @staticmethod
        def now(tz):
            return datetime(2026, 9, 30, 19, tzinfo=timezone.utc)
    monkeypatch.setattr(water, "datetime", Clock)
    class Silent(WSGIRequestHandler):
        def log_message(self, *_):
            return None
    with make_server("127.0.0.1", 0, main.app, handler_class=Silent) as server:
        thread = Thread(target=server.serve_forever, daemon=True); thread.start()
        base = f"http://127.0.0.1:{server.server_port}"
        def get(path):
            with urlopen(base + path, timeout=2) as response:
                assert response.headers["Cache-Control"] == "no-store"
                return json.load(response)
        try:
            layers = get("/v1/layers?station_id=USGS-06892518")
            evidence = get("/v1/evidence?station_id=USGS-06892518")
            assert layers["data"]["package_id"] == evidence["data"]["package_id"] == package_id
            assert [s["id"] for s in layers["data"]["stations"]] == ["USGS-06892518"]
            with sqlite3.connect(root / "activation.sqlite") as db:
                db.execute("UPDATE water_packages SET state='WITHDRAWN'")
            assert "data" not in get("/v1/layers")
            assert get("/healthz")["evidence_readiness"] == "NOT_ESTABLISHED"
        finally:
            server.shutdown(); thread.join(timeout=2)
            assert not thread.is_alive()
