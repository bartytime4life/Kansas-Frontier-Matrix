"""Soil serving rehearsal: admitted package -> decision -> stage -> activate -> /v1/soil answers.

Water, weather and soil share one private serving store but never a table, object or route.
"""
from datetime import datetime, timedelta, timezone
import json
import sqlite3
from threading import Thread
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from wsgiref.simple_server import WSGIRequestHandler, make_server

import pytest

from governed_api import main as api
from pipelines.domains.soil.uscrn_daily_validate import validate_candidate
from release.core import SOIL
from release.local_admin import activate, initialize, stage
from release.local_store import LocalReleaseStore
from tests.domains.soil.uscrn_daily_fixtures import acquired
from tools.local_data import uscrn_daily_pilot
from tools.local_data.manage import init_store
from tools.release import soil_release

OWNER = "@bartytime4life"


class Silent(WSGIRequestHandler):
    def log_message(self, *_):
        return None


def prepared(tmp_path):
    root = tmp_path / "store"
    init_store(root)
    candidate_id = uscrn_daily_pilot.stage(root, acquired())["candidate_id"]
    return root, soil_release.prepare(root, candidate_id, admitted_source=True)["package_id"]


def rehearsal(tmp_path, capsys):
    root, package_id = prepared(tmp_path)
    serving = tmp_path / "serving"
    decided = soil_release.decide(root, package_id, reviewer=OWNER, releaser=OWNER, valid_days=7,
                                  now=datetime.now(timezone.utc) - timedelta(minutes=1))
    run = lambda *argv: (soil_release.main([str(a) for a in argv]), json.loads(capsys.readouterr().out))
    assert run("stage", "--root", root, "--store", serving, "--package-id", package_id, "--actor", OWNER)[0] == 0
    code, active = run("activate", "--root", root, "--store", serving, "--decision", decided["decision_path"], "--expected-active", "none")
    assert (code, active["outcome"], active["package_id"], active["revision"]) == (0, "ACTIVATED", package_id, 1)
    return root, serving, package_id, decided, run


def get(port, path, method="GET"):
    try:
        with urlopen(Request(f"http://127.0.0.1:{port}{path}", method=method), timeout=5) as response:
            return response.status, json.load(response)
    except HTTPError as error:
        return error.code, json.load(error)


def serve(store):
    server = make_server("127.0.0.1", 0, api.app, handler_class=Silent)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, thread


@pytest.fixture
def served(tmp_path, capsys, monkeypatch):
    root, serving, package_id, decided, run = rehearsal(tmp_path, capsys)
    monkeypatch.setattr(api, "_RELEASE_STORE", LocalReleaseStore(str(serving)))
    server, thread = serve(serving)
    try:
        yield server.server_port, root, serving, package_id, decided, run
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)


def test_the_soil_layer_answers_once_released(served):
    port, _, _, package_id, _, _ = served
    status, layers = get(port, "/v1/soil/layers")
    assert status == 200 and layers["envelope"]["outcome"] == "ANSWER"
    data = layers["data"]
    assert (data["package_id"], data["source_id"]) == (package_id, "noaa-uscrn")
    assert sorted(s["id"] for s in data["stations"]) == ["03067", "53974"]
    assert len(data["observations"]) == 600
    assert "U.S. Climate Reference Network" in data["attribution"] and "may be revised" in data["attribution"]
    precision = layers["envelope"]["precision_actually_used"]
    assert precision["temporal"]["granularity"].startswith("Station local-standard-time days")
    assert precision["attribute"]["depths_cm"] == [5, 10, 20, 50, 100]
    # Withheld values stay null in the served layer.
    assert all(r["value"] is None for r in data["observations"] if r["withheld"])
    assert len(layers["envelope"]["evidence_refs"]) == 10
    status, one = get(port, "/v1/soil/evidence?station_id=53974")
    entries = one["data"]["entries"]
    assert status == 200 and [(e["station_id"], e["series"]) for e in entries] == [("53974", d) for d in (5, 10, 20, 50, 100)]
    status, boot = get(port, "/v1/soil/bootstrap")
    assert boot["data"]["layers"][0]["id"] == "uscrn-daily-soil-pilot"


def test_soil_routes_refuse_bad_queries_and_methods(served):
    port = served[0]
    assert get(port, "/v1/soil/layers?station_id=USW00003928")[0] == 400
    assert get(port, "/v1/soil/layers?other=1")[0] == 400
    assert get(port, "/v1/soil/layers?station_id=53974&station_id=03067")[0] == 400
    status, refused = get(port, "/v1/soil/layers", method="POST")
    assert (status, refused["envelope"]["reason_code"]) == (405, "METHOD_NOT_ALLOWED")


def test_water_and_weather_are_untouched_by_an_active_soil_package(served):
    port, _, serving, *_ = served
    for path in ("/v1/layers", "/v1/weather/layers"):
        status, body = get(port, path)
        assert (status, body["envelope"]["reason_code"]) == (200, "NO_APPROVED_SNAPSHOT")
    store = LocalReleaseStore(str(serving))
    assert store.active() is None and store.active("weather") is None
    assert not list((serving / "objects").iterdir()) and not list((serving / "weather-objects").iterdir())


def test_activation_is_compare_and_swap_and_family_bound(served):
    _, root, serving, package_id, decided, run = served
    code, conflict = run("activate", "--root", root, "--store", serving, "--decision", decided["decision_path"], "--expected-active", "none")
    assert (code, conflict["reason_code"]) == (1, "ACTIVATION_CONFLICT")
    decision = json.loads((root / decided["decision_path"]).read_text())
    raw = (root / "release/candidates/soil" / package_id.split(":")[1] / "snapshot.json").read_bytes()
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    # A soil package cannot be staged as water or weather.
    for family in ("water", "weather"):
        with pytest.raises(ValueError, match="MANIFEST_PROFILE_INVALID"):
            stage(serving, raw, actor=OWNER, now=now, validator=validate_candidate, family=family)
    # The weather path never finds it: soil objects live in their own directory.
    with pytest.raises(FileNotFoundError):
        activate(serving, package_id, decision, expected_active=None, now=now, validator=validate_candidate, family="weather")


def test_a_weather_decision_cannot_activate_a_soil_package(served):
    _, root, serving, package_id, decided, run = served
    decision = json.loads((root / decided["decision_path"]).read_text())
    forged = root / "release/decisions/soil/forged.json"
    forged.write_text(json.dumps({**decision, "profile": "kfm.weather-release-decision/v1"}))
    code, refused = run("rollback", "--root", root, "--store", serving, "--decision", "release/decisions/soil/forged.json",
                        "--expected-active", package_id)
    assert (code, refused["reason_code"]) == (1, "DECISION_PROFILE_INVALID")


def test_stage_requires_the_package_to_match_its_stored_capture(tmp_path, capsys):
    import shutil
    root, package_id = prepared(tmp_path)
    shutil.rmtree(root / "data/quarantine" / uscrn_daily_pilot.LANE / "runs")
    code = soil_release.main(["stage", "--root", str(root), "--store", str(tmp_path / "serving"),
                              "--package-id", package_id, "--actor", OWNER])
    assert (code, json.loads(capsys.readouterr().out)["reason_code"]) == (1, "CAPTURE_NOT_IN_STORE")
    assert not (tmp_path / "serving").exists()


def test_an_expired_soil_decision_stops_serving(tmp_path, capsys):
    _, serving, *_ = rehearsal(tmp_path, capsys)
    raw, decision = LocalReleaseStore(str(serving)).active("soil")
    from release.soil_projection import project
    later = (datetime.now(timezone.utc) + timedelta(days=8)).strftime("%Y-%m-%dT%H:%M:%SZ")
    assert project(raw, decision, view="layers", now=later)["envelope"]["reason_code"] == "RELEASE_TIME_INVALID"


def test_no_active_soil_package_abstains(tmp_path, monkeypatch):
    serving = tmp_path / "serving"
    serving.mkdir(mode=0o700)
    initialize(serving)
    monkeypatch.setattr(api, "_RELEASE_STORE", LocalReleaseStore(str(serving)))
    server, thread = serve(serving)
    try:
        status, body = get(server.server_port, "/v1/soil/layers")
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)
    assert (status, body["envelope"]["outcome"], body["envelope"]["reason_code"]) == (200, "ABSTAIN", "NO_APPROVED_SNAPSHOT")


def test_freshness_uses_the_station_local_day_and_soil_moisture(tmp_path):
    from release.soil_projection import STANDARD_OFFSET_HOURS, project
    assert set(STANDARD_OFFSET_HOURS) == SOIL.station_ids
    root, package_id = prepared(tmp_path)
    decision = soil_release.build_decision(package_id, reviewer=OWNER, releaser=OWNER, valid_days=7,
                                           now=datetime(2026, 10, 11, 13, 0, tzinfo=timezone.utc))
    raw = (root / "release/candidates/soil" / package_id.split(":")[1] / "snapshot.json").read_bytes()
    fresh = lambda now, station=None: project(raw, decision, view="layers", now=now, station_id=station)["envelope"]["freshness"]
    # Manhattan's latest moisture value is 2026-10-10. At 03:00Z on the 14th it is still the 13th in Kansas (UTC-6).
    assert fresh("2026-10-14T03:00:00Z", "53974") == "current"
    assert fresh("2026-10-14T03:00:00Z") == "current"
    # From 06:00Z it is the 14th locally, 4 days after the last value.
    assert fresh("2026-10-14T06:00:00Z", "53974") == "stale-accepted"
    # Oakley's moisture stopped on 2026-10-05 and stays stale.
    assert fresh("2026-10-12T03:00:00Z", "03067") == "stale-accepted"


def test_a_partial_soil_schema_is_a_store_failure_not_an_empty_store(tmp_path):
    serving = tmp_path / "serving"
    serving.mkdir(mode=0o700)
    initialize(serving)
    with sqlite3.connect(serving / "activation.sqlite") as connection:
        connection.execute("DROP TABLE soil_packages")
    with pytest.raises(sqlite3.OperationalError):
        LocalReleaseStore(str(serving)).active("soil")
    # A store from before soil existed (no soil tables at all) has nothing active.
    with sqlite3.connect(serving / "activation.sqlite") as connection:
        connection.execute("DROP TABLE soil_active")
        connection.execute("DROP TABLE soil_activation_events")
    assert LocalReleaseStore(str(serving)).active("soil") is None
    assert LocalReleaseStore(str(serving)).active("weather") is None
