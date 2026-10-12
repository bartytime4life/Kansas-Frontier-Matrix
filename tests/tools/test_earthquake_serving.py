"""Earthquake serving rehearsal: admitted package -> decision -> stage -> activate -> /v1/earthquakes answers.

Water, weather, soil, storm events and earthquakes share one private serving store but never a table, object or route.
"""
from datetime import datetime, timedelta, timezone
import json
import shutil
import sqlite3
from threading import Thread
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from wsgiref.simple_server import WSGIRequestHandler, make_server

import pytest

from governed_api import main as api
from pipelines.domains.hazards.earthquake_validate import validate_candidate
from release.earthquake_projection import project
from release.local_admin import activate, initialize, stage
from release.local_store import LocalReleaseStore
from tests.domains.hazards.earthquake_fixtures import acquired
from tools.local_data import earthquake_pilot
from tools.local_data.manage import init_store
from tools.release import earthquake_release

OWNER = "@bartytime4life"


class Silent(WSGIRequestHandler):
    def log_message(self, *_):
        return None


def prepared(tmp_path):
    root = tmp_path / "store"
    init_store(root)
    candidate_id = earthquake_pilot.stage(root, acquired())["candidate_id"]
    return root, earthquake_release.prepare(root, candidate_id, admitted_source=True)["package_id"]


def snapshot(root, package_id):
    return (root / "release/candidates/earthquakes" / package_id.split(":")[1] / "snapshot.json").read_bytes()


def rehearsal(tmp_path, capsys):
    root, package_id = prepared(tmp_path)
    serving = tmp_path / "serving"
    decided = earthquake_release.decide(root, package_id, reviewer=OWNER, releaser=OWNER, valid_days=7,
                                        now=datetime.now(timezone.utc) - timedelta(minutes=1))
    run = lambda *argv: (earthquake_release.main([str(a) for a in argv]), json.loads(capsys.readouterr().out))
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


def test_the_earthquake_layer_answers_once_released(served):
    port, _, _, package_id, _, _ = served
    status, layers = get(port, "/v1/earthquakes/layers")
    assert status == 200 and layers["envelope"]["outcome"] == "ANSWER"
    data = layers["data"]
    assert (data["package_id"], data["source_id"], data["data_year"], data["year_state"], data["life_safety"]) == (
        package_id, "usgs-earthquakes", 2025, "OPEN", "not_for_life_safety")
    assert [r["event_id"] for r in data["observations"]] == ["us7000p001", "ok2025b002", "us7000p004", "ok2025p005", "us7000p006"]
    assert data["bounds"] == [-102.1, 36.9, -94.5, 40.1]
    assert (data["dataset"]["scope"], data["dataset"]["withheld_counts"]) == ("data_year", {"STATUS_DELETED": 1})
    assert "ComCat" in data["attribution"] and "not shaking estimates or alerts" in data["attribution"]
    precision = layers["envelope"]["precision_actually_used"]
    assert "not the state boundary" in precision["spatial"]["accuracy"]
    assert precision["temporal"]["observation_interval"] == {"start": "2025-01-01", "end": "2025-12-31"}
    assert len(layers["envelope"]["evidence_refs"]) == 3
    assert data["selection"]["months"] == [1, 2, 5] and data["selection"]["observation_count"] == 5
    status, may = get(port, "/v1/earthquakes/evidence?month=5")
    assert status == 200 and [(e["month"], e["part"]) for e in may["data"]["entries"]] == [(5, 1)]
    status, may_layers = get(port, "/v1/earthquakes/layers?month=5")
    assert [r["event_id"] for r in may_layers["data"]["observations"]] == ["us7000p004", "ok2025p005", "us7000p006"]
    # The year summary is labeled as such; the selection describes exactly the returned records.
    assert may_layers["data"]["dataset"]["observation_count"] == 5
    assert may_layers["data"]["selection"] == {"months": [5], "observation_count": 3,
                                               "review_status": {"automatic": 1, "reviewed": 2}, "context_margin_count": 1,
                                               "magnitude_range": [2.1, 2.8], "latest_event_date": "2025-05-27"}
    status, boot = get(port, "/v1/earthquakes/bootstrap")
    assert (boot["data"]["layers"][0]["id"], boot["data"]["months"]) == ("usgs-earthquakes-ks", [1, 2, 5])


def test_a_month_without_events_abstains(served):
    status, body = get(served[0], "/v1/earthquakes/layers?month=3")
    assert (status, body["envelope"]["outcome"], body["envelope"]["reason_code"]) == (200, "ABSTAIN", "EVIDENCE_NOT_FOUND")


@pytest.mark.parametrize("query", ["month=13", "month=0", "month=05", "month=+5", "month=%205", "month=", "other=1", "month=5&month=6"])
def test_earthquake_routes_refuse_bad_queries(served, query):
    status, body = get(served[0], "/v1/earthquakes/layers?" + query)
    assert (status, body["envelope"]["reason_code"]) == (400, "INVALID_QUERY")


def test_earthquake_routes_refuse_other_methods(served):
    status, refused = get(served[0], "/v1/earthquakes/layers", method="POST")
    assert (status, refused["envelope"]["reason_code"]) == (405, "METHOD_NOT_ALLOWED")


def test_other_families_are_untouched_by_an_active_earthquake_package(served):
    port, _, serving, *_ = served
    for path in ("/v1/layers", "/v1/weather/layers", "/v1/soil/layers", "/v1/storm-events/layers"):
        status, body = get(port, path)
        assert (status, body["envelope"]["reason_code"]) == (200, "NO_APPROVED_SNAPSHOT")
    store = LocalReleaseStore(str(serving))
    assert all(store.active(family) is None for family in ("water", "weather", "soil", "storm_events"))
    for objects in ("objects", "weather-objects", "soil-objects", "storm-events-objects"):
        assert not list((serving / objects).iterdir())


def test_activation_is_compare_and_swap_and_family_bound(served):
    _, root, serving, package_id, decided, run = served
    code, conflict = run("activate", "--root", root, "--store", serving, "--decision", decided["decision_path"], "--expected-active", "none")
    assert (code, conflict["reason_code"]) == (1, "ACTIVATION_CONFLICT")
    decision = json.loads((root / decided["decision_path"]).read_text())
    raw = snapshot(root, package_id)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    # An earthquake package cannot be staged as another family.
    for family in ("water", "weather", "soil", "storm_events"):
        with pytest.raises(ValueError, match="MANIFEST_PROFILE_INVALID"):
            stage(serving, raw, actor=OWNER, now=now, validator=validate_candidate, family=family)
    # The storm events path never finds it: earthquake objects live in their own directory.
    with pytest.raises(FileNotFoundError):
        activate(serving, package_id, decision, expected_active=None, now=now, validator=validate_candidate, family="storm_events")


def test_a_storm_events_decision_cannot_activate_an_earthquake_package(served):
    _, root, serving, package_id, decided, run = served
    decision = json.loads((root / decided["decision_path"]).read_text())
    forged = root / "release/decisions/earthquakes/forged.json"
    forged.write_text(json.dumps({**decision, "profile": "kfm.storm-events-release-decision/v1"}))
    code, refused = run("rollback", "--root", root, "--store", serving, "--decision", "release/decisions/earthquakes/forged.json",
                        "--expected-active", package_id)
    assert (code, refused["reason_code"]) == (1, "DECISION_PROFILE_INVALID")


def test_stage_requires_the_package_to_match_its_stored_capture(tmp_path, capsys):
    root, package_id = prepared(tmp_path)
    shutil.rmtree(root / "data/quarantine" / earthquake_pilot.LANE / "runs")
    code = earthquake_release.main(["stage", "--root", str(root), "--store", str(tmp_path / "serving"),
                                    "--package-id", package_id, "--actor", OWNER])
    assert (code, json.loads(capsys.readouterr().out)["reason_code"]) == (1, "CAPTURE_NOT_IN_STORE")
    assert not (tmp_path / "serving").exists()


def test_an_expired_earthquake_decision_stops_serving(tmp_path, capsys):
    _, serving, *_ = rehearsal(tmp_path, capsys)
    raw, decision = LocalReleaseStore(str(serving)).active("earthquakes")
    later = (datetime.now(timezone.utc) + timedelta(days=8)).strftime("%Y-%m-%dT%H:%M:%SZ")
    assert project(raw, decision, view="layers", now=later)["envelope"]["reason_code"] == "RELEASE_TIME_INVALID"


def test_freshness_is_the_age_of_the_capture(tmp_path):
    root, package_id = prepared(tmp_path)
    decision = earthquake_release.build_decision(package_id, reviewer=OWNER, releaser=OWNER, valid_days=30,
                                                 now=datetime(2025, 11, 10, 0, 0, tzinfo=timezone.utc))
    fresh = lambda now: project(snapshot(root, package_id), decision, view="bootstrap", now=now)["envelope"]["freshness"]
    # The fixture capture is 2025-11-01T12:00:00Z: current for 30 days, then stale-accepted.
    assert fresh("2025-12-01T12:00:00Z") == "current"
    assert fresh("2025-12-01T12:00:01Z") == "stale-accepted"


def test_no_active_earthquake_package_abstains(tmp_path, monkeypatch):
    serving = tmp_path / "serving"
    serving.mkdir(mode=0o700)
    initialize(serving)
    monkeypatch.setattr(api, "_RELEASE_STORE", LocalReleaseStore(str(serving)))
    server, thread = serve()
    try:
        status, body = get(server.server_port, "/v1/earthquakes/layers")
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)
    assert (status, body["envelope"]["outcome"], body["envelope"]["reason_code"]) == (200, "ABSTAIN", "NO_APPROVED_SNAPSHOT")


def test_a_partial_earthquake_schema_is_a_store_failure_not_an_empty_store(tmp_path):
    serving = tmp_path / "serving"
    serving.mkdir(mode=0o700)
    initialize(serving)
    with sqlite3.connect(serving / "activation.sqlite") as connection:
        connection.execute("DROP TABLE earthquakes_packages")
    with pytest.raises(sqlite3.OperationalError):
        LocalReleaseStore(str(serving)).active("earthquakes")
    # A store from before earthquakes existed (no earthquake tables at all) has nothing active.
    with sqlite3.connect(serving / "activation.sqlite") as connection:
        connection.execute("DROP TABLE earthquakes_active")
        connection.execute("DROP TABLE earthquakes_activation_events")
    assert LocalReleaseStore(str(serving)).active("earthquakes") is None
    assert LocalReleaseStore(str(serving)).active("storm_events") is None
