"""Storm Events serving rehearsal: admitted package -> decision -> stage -> activate -> /v1/storm-events answers.

Water, weather, soil and storm events share one private serving store but never a table, object or route.
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
from pipelines.domains.hazards.storm_events_validate import validate_candidate
from release.local_admin import activate, initialize, stage
from release.local_store import LocalReleaseStore
from tests.domains.hazards.storm_events_fixtures import acquired
from tools.local_data import storm_events_pilot
from tools.local_data.manage import init_store
from tools.release import storm_events_release

OWNER = "@bartytime4life"


class Silent(WSGIRequestHandler):
    def log_message(self, *_):
        return None


def prepared(tmp_path):
    root = tmp_path / "store"
    init_store(root)
    candidate_id = storm_events_pilot.stage(root, acquired())["candidate_id"]
    return root, storm_events_release.prepare(root, candidate_id, admitted_source=True)["package_id"]


def rehearsal(tmp_path, capsys):
    root, package_id = prepared(tmp_path)
    serving = tmp_path / "serving"
    decided = storm_events_release.decide(root, package_id, reviewer=OWNER, releaser=OWNER, valid_days=7,
                                          now=datetime.now(timezone.utc) - timedelta(minutes=1))
    run = lambda *argv: (storm_events_release.main([str(a) for a in argv]), json.loads(capsys.readouterr().out))
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


def serve():
    server = make_server("127.0.0.1", 0, api.app, handler_class=Silent)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, thread


@pytest.fixture
def served(tmp_path, capsys, monkeypatch):
    root, serving, package_id, decided, run = rehearsal(tmp_path, capsys)
    monkeypatch.setattr(api, "_RELEASE_STORE", LocalReleaseStore(str(serving)))
    server, thread = serve()
    try:
        yield server.server_port, root, serving, package_id, decided, run
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)


def test_the_storm_events_layer_answers_once_released(served):
    port, _, _, package_id, _, _ = served
    status, layers = get(port, "/v1/storm-events/layers")
    assert status == 200 and layers["envelope"]["outcome"] == "ANSWER"
    data = layers["data"]
    assert (data["package_id"], data["source_id"], data["data_year"], data["life_safety"]) == (
        package_id, "noaa-storm-events", 2025, "not_for_life_safety")
    assert [r["event_id"] for r in data["observations"]] == [9000101, 9000102, 9000103, 9000104, 9000105, 9000106]
    assert data["dataset"]["narratives"] == "excluded" and data["dataset"]["withheld_rows"] == 2
    assert "Storm Events Database" in data["attribution"] and "not warnings" in data["attribution"]
    precision = layers["envelope"]["precision_actually_used"]
    assert precision["spatial"]["representation"].startswith("county or forecast zone")
    assert precision["temporal"]["observation_interval"] == {"start": "2025-01-01", "end": "2025-12-31"}
    assert len(layers["envelope"]["evidence_refs"]) == 6
    assert "Synthetic narrative" not in json.dumps(layers)
    status, may = get(port, "/v1/storm-events/evidence?month=5")
    assert status == 200 and [(e["month"], e["part"]) for e in may["data"]["entries"]] == [(5, 1)]
    status, may_layers = get(port, "/v1/storm-events/layers?month=5")
    assert [r["event_id"] for r in may_layers["data"]["observations"]] == [9000102]
    status, boot = get(port, "/v1/storm-events/bootstrap")
    assert (boot["data"]["layers"][0]["id"], boot["data"]["months"]) == ("noaa-storm-events-ks", [1, 4, 5, 6, 7, 8])


def test_a_month_without_events_abstains(served):
    status, body = get(served[0], "/v1/storm-events/layers?month=2")
    assert (status, body["envelope"]["outcome"], body["envelope"]["reason_code"]) == (200, "ABSTAIN", "EVIDENCE_NOT_FOUND")


@pytest.mark.parametrize("query", ["month=13", "month=0", "month=05", "month=+5", "month=%205", "month=", "other=1", "month=5&month=6"])
def test_storm_events_routes_refuse_bad_queries(served, query):
    status, body = get(served[0], "/v1/storm-events/layers?" + query)
    assert (status, body["envelope"]["reason_code"]) == (400, "INVALID_QUERY")


def test_storm_events_routes_refuse_other_methods(served):
    status, refused = get(served[0], "/v1/storm-events/layers", method="POST")
    assert (status, refused["envelope"]["reason_code"]) == (405, "METHOD_NOT_ALLOWED")


def test_other_families_are_untouched_by_an_active_storm_events_package(served):
    port, _, serving, *_ = served
    for path in ("/v1/layers", "/v1/weather/layers", "/v1/soil/layers"):
        status, body = get(port, path)
        assert (status, body["envelope"]["reason_code"]) == (200, "NO_APPROVED_SNAPSHOT")
    store = LocalReleaseStore(str(serving))
    assert store.active() is None and store.active("weather") is None and store.active("soil") is None
    for objects in ("objects", "weather-objects", "soil-objects"):
        assert not list((serving / objects).iterdir())


def test_activation_is_compare_and_swap_and_family_bound(served):
    _, root, serving, package_id, decided, run = served
    code, conflict = run("activate", "--root", root, "--store", serving, "--decision", decided["decision_path"], "--expected-active", "none")
    assert (code, conflict["reason_code"]) == (1, "ACTIVATION_CONFLICT")
    decision = json.loads((root / decided["decision_path"]).read_text())
    raw = (root / "release/candidates/storm-events" / package_id.split(":")[1] / "snapshot.json").read_bytes()
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    # A storm events package cannot be staged as another family.
    for family in ("water", "weather", "soil"):
        with pytest.raises(ValueError, match="MANIFEST_PROFILE_INVALID"):
            stage(serving, raw, actor=OWNER, now=now, validator=validate_candidate, family=family)
    # The soil path never finds it: storm events objects live in their own directory.
    with pytest.raises(FileNotFoundError):
        activate(serving, package_id, decision, expected_active=None, now=now, validator=validate_candidate, family="soil")


def test_a_soil_decision_cannot_activate_a_storm_events_package(served):
    _, root, serving, package_id, decided, run = served
    decision = json.loads((root / decided["decision_path"]).read_text())
    forged = root / "release/decisions/storm-events/forged.json"
    forged.write_text(json.dumps({**decision, "profile": "kfm.soil-release-decision/v1"}))
    code, refused = run("rollback", "--root", root, "--store", serving, "--decision", "release/decisions/storm-events/forged.json",
                        "--expected-active", package_id)
    assert (code, refused["reason_code"]) == (1, "DECISION_PROFILE_INVALID")


def test_stage_requires_the_package_to_match_its_stored_capture(tmp_path, capsys):
    import shutil
    root, package_id = prepared(tmp_path)
    shutil.rmtree(root / "data/quarantine" / storm_events_pilot.LANE / "runs")
    code = storm_events_release.main(["stage", "--root", str(root), "--store", str(tmp_path / "serving"),
                                      "--package-id", package_id, "--actor", OWNER])
    assert (code, json.loads(capsys.readouterr().out)["reason_code"]) == (1, "CAPTURE_NOT_IN_STORE")
    assert not (tmp_path / "serving").exists()


def test_an_expired_storm_events_decision_stops_serving(tmp_path, capsys):
    _, serving, *_ = rehearsal(tmp_path, capsys)
    raw, decision = LocalReleaseStore(str(serving)).active("storm_events")
    from release.storm_events_projection import project
    later = (datetime.now(timezone.utc) + timedelta(days=8)).strftime("%Y-%m-%dT%H:%M:%SZ")
    assert project(raw, decision, view="layers", now=later)["envelope"]["reason_code"] == "RELEASE_TIME_INVALID"


def test_freshness_is_the_age_of_the_file_vintage(tmp_path):
    from release.storm_events_projection import project
    root, package_id = prepared(tmp_path)
    decision = storm_events_release.build_decision(package_id, reviewer=OWNER, releaser=OWNER, valid_days=30,
                                                   now=datetime(2025, 11, 10, 0, 0, tzinfo=timezone.utc))
    raw = (root / "release/candidates/storm-events" / package_id.split(":")[1] / "snapshot.json").read_bytes()
    fresh = lambda now: project(raw, decision, view="bootstrap", now=now)["envelope"]["freshness"]
    # The fixture vintage is 2025-10-20; 45 days later it is still current, 46 days later stale.
    assert fresh("2025-12-04T23:59:59Z") == "current"
    assert fresh("2025-12-05T00:00:00Z") == "stale-accepted"


def test_no_active_storm_events_package_abstains(tmp_path, monkeypatch):
    serving = tmp_path / "serving"
    serving.mkdir(mode=0o700)
    initialize(serving)
    monkeypatch.setattr(api, "_RELEASE_STORE", LocalReleaseStore(str(serving)))
    server, thread = serve()
    try:
        status, body = get(server.server_port, "/v1/storm-events/layers")
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)
    assert (status, body["envelope"]["outcome"], body["envelope"]["reason_code"]) == (200, "ABSTAIN", "NO_APPROVED_SNAPSHOT")


def test_a_partial_storm_events_schema_is_a_store_failure_not_an_empty_store(tmp_path):
    serving = tmp_path / "serving"
    serving.mkdir(mode=0o700)
    initialize(serving)
    with sqlite3.connect(serving / "activation.sqlite") as connection:
        connection.execute("DROP TABLE storm_events_packages")
    with pytest.raises(sqlite3.OperationalError):
        LocalReleaseStore(str(serving)).active("storm_events")
    # A store from before storm events existed (no storm events tables at all) has nothing active.
    with sqlite3.connect(serving / "activation.sqlite") as connection:
        connection.execute("DROP TABLE storm_events_active")
        connection.execute("DROP TABLE storm_events_activation_events")
    assert LocalReleaseStore(str(serving)).active("storm_events") is None
    assert LocalReleaseStore(str(serving)).active("soil") is None
