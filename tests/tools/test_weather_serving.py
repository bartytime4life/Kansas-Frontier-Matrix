"""Weather serving rehearsal: admitted package -> decision -> stage -> activate -> /v1/weather answers.

Water and weather share one private serving store but never a table, object or route.
"""
from datetime import datetime, timedelta, timezone
import json
from threading import Thread
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from wsgiref.simple_server import WSGIRequestHandler, make_server

import pytest

from governed_api import main as api
from pipelines.domains.atmosphere.ghcnd_daily_validate import validate_candidate
from release.local_admin import activate, stage
from release.local_store import LocalReleaseStore
from tests.domains.atmosphere.ghcnd_daily_fixtures import acquired
from tools.local_data import ghcnd_daily_pilot
from tools.local_data.manage import init_store
from tools.release import weather_release

OWNER = "@bartytime4life"


class Silent(WSGIRequestHandler):
    def log_message(self, *_):
        return None


def rehearsal(tmp_path, capsys):
    root, serving = tmp_path / "store", tmp_path / "serving"
    init_store(root)
    candidate_id = ghcnd_daily_pilot.stage(root, acquired())["candidate_id"]
    package_id = weather_release.prepare(root, candidate_id, admitted_source=True)["package_id"]
    decided = weather_release.decide(root, package_id, reviewer=OWNER, releaser=OWNER, valid_days=7,
                                     now=datetime.now(timezone.utc) - timedelta(minutes=1))
    run = lambda *argv: (weather_release.main([str(a) for a in argv]), json.loads(capsys.readouterr().out))
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


@pytest.fixture
def served(tmp_path, capsys, monkeypatch):
    root, serving, package_id, decided, run = rehearsal(tmp_path, capsys)
    monkeypatch.setattr(api, "_RELEASE_STORE", LocalReleaseStore(str(serving)))
    with make_server("127.0.0.1", 0, api.app, handler_class=Silent) as server:
        thread = Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            yield server.server_port, root, serving, package_id, decided, run
        finally:
            server.shutdown()
            thread.join(timeout=2)


def test_the_weather_layer_answers_once_released(served):
    port, _, _, package_id, _, _ = served
    status, layers = get(port, "/v1/weather/layers")
    assert status == 200 and layers["envelope"]["outcome"] == "ANSWER"
    data = layers["data"]
    assert (data["package_id"], data["source_id"]) == (package_id, "noaa-ghcnd")
    assert sorted(s["id"] for s in data["stations"]) == ["USW00003928", "USW00013985", "USW00013996", "USW00023065"]
    assert "Menne et al. (2012)" in data["attribution"]
    precision = layers["envelope"]["precision_actually_used"]
    assert precision["temporal"]["granularity"].startswith("Station-local observation days")
    # Withheld values stay null in the served layer.
    assert all(r["value"] is None for r in data["observations"] if r["withheld"])
    status, one = get(port, "/v1/weather/evidence?station_id=USW00013996")
    assert status == 200 and [e["station_id"] for e in one["data"]["entries"]] == ["USW00013996"]
    status, boot = get(port, "/v1/weather/bootstrap")
    assert boot["data"]["layers"][0]["id"] == "ghcnd-daily-pilot"


def test_weather_routes_refuse_bad_queries_and_methods(served):
    port = served[0]
    assert get(port, "/v1/weather/layers?station_id=USGS-06892518")[0] == 400
    assert get(port, "/v1/weather/layers?other=1")[0] == 400
    status, refused = get(port, "/v1/weather/layers", method="POST")
    assert (status, refused["envelope"]["reason_code"]) == (405, "METHOD_NOT_ALLOWED")


def test_water_is_untouched_by_an_active_weather_package(served):
    port, _, serving, *_ = served
    status, water = get(port, "/v1/layers")
    assert (status, water["envelope"]["reason_code"]) == (200, "NO_APPROVED_SNAPSHOT")
    assert LocalReleaseStore(str(serving)).active() is None
    assert not list((serving / "objects").iterdir())


def test_activation_is_compare_and_swap_and_family_bound(served):
    _, root, serving, package_id, decided, run = served
    code, conflict = run("activate", "--root", root, "--store", serving, "--decision", decided["decision_path"], "--expected-active", "none")
    assert (code, conflict["reason_code"]) == (1, "ACTIVATION_CONFLICT")
    decision = json.loads((root / decided["decision_path"]).read_text())
    raw = (root / "release/candidates/atmosphere" / package_id.split(":")[1] / "snapshot.json").read_bytes()
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    # A weather package cannot be staged or activated as water.
    with pytest.raises(ValueError, match="MANIFEST_PROFILE_INVALID"):
        stage(serving, raw, actor=OWNER, now=now, validator=validate_candidate)
    # The water path never finds it: weather objects live in their own directory.
    with pytest.raises(FileNotFoundError):
        activate(serving, package_id, decision, expected_active=None, now=now, validator=validate_candidate)
    with pytest.raises(ValueError, match="RELEASE_FAMILY_INVALID"):
        LocalReleaseStore(str(serving)).active("climate")


def test_an_expired_weather_decision_stops_serving(tmp_path, capsys, monkeypatch):
    root, serving, package_id, decided, _ = rehearsal(tmp_path, capsys)
    raw, decision = LocalReleaseStore(str(serving)).active("weather")
    from release.weather_projection import project
    later = (datetime.now(timezone.utc) + timedelta(days=8)).strftime("%Y-%m-%dT%H:%M:%SZ")
    assert project(raw, decision, view="layers", now=later)["envelope"]["reason_code"] == "RELEASE_TIME_INVALID"


def test_no_active_weather_package_abstains(tmp_path, monkeypatch):
    serving = tmp_path / "serving"
    serving.mkdir(mode=0o700)
    from release.local_admin import initialize
    initialize(serving)
    monkeypatch.setattr(api, "_RELEASE_STORE", LocalReleaseStore(str(serving)))
    with make_server("127.0.0.1", 0, api.app, handler_class=Silent) as server:
        thread = Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            status, body = get(server.server_port, "/v1/weather/layers")
        finally:
            server.shutdown()
            thread.join(timeout=2)
    assert (status, body["envelope"]["outcome"], body["envelope"]["reason_code"]) == (200, "ABSTAIN", "NO_APPROVED_SNAPSHOT")
