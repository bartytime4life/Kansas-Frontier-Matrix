"""Weather hosted staging and the owner cycle (ADR-0045): stage on the Site, never activate there."""
from datetime import datetime, timezone
import json

import pytest

from tests.domains.atmosphere.ghcnd_daily_fixtures import END, acquired
from tools.local_data import ghcnd_daily_pilot
from tools.local_data.manage import init_store
from tools.release import weather_release

OWNER = "@bartytime4life"
NOW = datetime(2026, 10, 11, 13, 0, tzinfo=timezone.utc)
SITE = "https://kfm.example.test"


class FakeResponse:
    def __init__(self, body):
        self.body = json.dumps(body).encode()

    def read(self, _limit):
        return self.body

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False


class SiteOpener:
    """Answers the weather status and stage routes and records each request."""

    def __init__(self, active, *, activated=False):
        self.active, self.activated, self.requests = active, activated, []

    def open(self, request, timeout):
        self.requests.append(request)
        if request.full_url.endswith("/status"):
            return FakeResponse({"active_package_id": self.active, "previous_package_id": None, "revision": 1})
        package_id = json.loads(request.data)["manifest"]["package_id"]
        return FakeResponse({"package_id": package_id, "state": "STAGED", "activated": self.activated})


def store(tmp_path):
    root = tmp_path / "store"
    init_store(root)
    return root


def snapshot_path(root, package_id):
    return root / "release/candidates/atmosphere" / package_id.split(":")[1] / "snapshot.json"


def cycle(root, **options):
    return weather_release.cycle(root, end_date=END, owner=OWNER, valid_days=7, clock=lambda: NOW,
                                 acquire=options.pop("acquire", lambda _end: acquired()), **options)


def test_stage_hosted_posts_to_the_weather_route_and_never_activates(tmp_path, monkeypatch):
    root = store(tmp_path)
    candidate_id = ghcnd_daily_pilot.stage(root, acquired())["candidate_id"]
    package_id = weather_release.prepare(root, candidate_id, admitted_source=True)["package_id"]
    monkeypatch.setenv("KFM_WATER_WORKER_TOKEN", "t" * 40)
    opener = SiteOpener(None)
    result = weather_release.stage_hosted(root, package_id, SITE, opener=opener)
    assert result == {"outcome": "STAGED_HOSTED", "package_id": package_id, "site": "kfm.example.test", "activated": False}
    [request] = opener.requests
    assert request.full_url == "https://kfm.example.test/api/governed/weather-admin/stage"
    assert request.data == snapshot_path(root, package_id).read_bytes()
    with pytest.raises(ValueError, match="HOSTED_STAGING_UNEXPECTED_RESPONSE"):
        weather_release.stage_hosted(root, package_id, SITE, opener=SiteOpener(None, activated=True))
    with pytest.raises(ValueError, match="SITE_URL_INVALID"):
        weather_release.stage_hosted(root, package_id, "http://kfm.example.test", opener=opener)


def test_cycle_runs_capture_to_decision_without_activating(tmp_path):
    root = store(tmp_path)
    result = cycle(root)
    assert (result["outcome"], result["staged_hosted"], result["activated"], result["rollback_target"]) == ("DECIDED", False, False, None)
    decision = json.loads((root / result["decision_path"]).read_text())
    assert (decision["package_id"], decision["policy_ref"]) == (result["package_id"], "kfm://adr/0045")
    assert not (root / "release/active").exists()


def test_cycle_binds_the_site_active_weather_package_and_stages_there(tmp_path, monkeypatch):
    monkeypatch.setenv("KFM_WATER_WORKER_TOKEN", "t" * 40)
    active = "sha256:" + "b" * 64
    root, opener = store(tmp_path), SiteOpener(active)
    result = cycle(root, site_url=SITE, opener=opener)
    assert (result["outcome"], result["staged_hosted"], result["next"]) == ("STAGED_HOSTED", True, SITE + "/governed/weather-release")
    assert json.loads(snapshot_path(root, result["package_id"]).read_text())["manifest"]["rollback_target"] == active
    assert [(r.get_method(), r.full_url.rsplit("/", 2)[1:]) for r in opener.requests] == [
        ("GET", ["weather-admin", "status"]), ("POST", ["weather-admin", "stage"])]


def test_cycle_checks_the_site_before_capturing_and_stops_at_quarantine(tmp_path, monkeypatch):
    root, captured = store(tmp_path), []
    monkeypatch.delenv("KFM_WATER_WORKER_TOKEN", raising=False)
    with pytest.raises(ValueError, match="WATER_WORKER_TOKEN_REQUIRED"):
        cycle(root, acquire=lambda _end: captured.append(1), site_url=SITE, opener=SiteOpener(None))
    monkeypatch.setenv("KFM_WATER_WORKER_TOKEN", "t" * 40)
    with pytest.raises(ValueError, match="HOSTED_UNEXPECTED_RESPONSE"):
        cycle(root, acquire=lambda _end: captured.append(1), site_url=SITE, opener=SiteOpener("water"))
    assert captured == []
    bad = acquired(lambda key, text: text.replace(",TMAX,250,", ",TMAX,25x,", 1) if key.endswith("USW00003928.csv.gz") else text)
    with pytest.raises(ValueError, match="CAPTURE_NOT_READY"):
        cycle(root, acquire=lambda _end: bad)
    assert not (root / "release").exists()


def test_the_admin_route_prefix_is_an_allowlist():
    with pytest.raises(ValueError, match="ADMIN_ROUTE_INVALID"):
        weather_release._site_call("kfm.example.test", "status", admin="../water-admin")


def test_cli_cycle_reports_errors_as_reason_codes(tmp_path, capsys, monkeypatch):
    monkeypatch.setattr(weather_release, "capture", lambda _end: acquired())
    monkeypatch.setattr(weather_release, "datetime", type("Clock", (), {"now": staticmethod(lambda tz=None: NOW)}))
    code = weather_release.main(["cycle", "--root", str(tmp_path / "store"), "--end-date", END, "--owner", OWNER])
    result = json.loads(capsys.readouterr().out)
    assert (code, result["outcome"], result["end_date"]) == (0, "DECIDED", END)
    code = weather_release.main(["cycle", "--root", str(tmp_path / "store"), "--end-date", "2026-13-01", "--owner", OWNER,
                                 "--rollback-target", "active"])
    assert (code, json.loads(capsys.readouterr().out)["reason_code"]) == (1, "ROLLBACK_TARGET_INVALID")


def test_stage_hosted_refuses_a_package_without_its_stored_capture(tmp_path, monkeypatch):
    import shutil
    root = store(tmp_path)
    candidate_id = ghcnd_daily_pilot.stage(root, acquired())["candidate_id"]
    package_id = weather_release.prepare(root, candidate_id, admitted_source=True)["package_id"]
    shutil.rmtree(root / "data/quarantine" / ghcnd_daily_pilot.LANE / "runs")
    monkeypatch.setenv("KFM_WATER_WORKER_TOKEN", "t" * 40)
    opener = SiteOpener(None)
    with pytest.raises(ValueError, match="CAPTURE_NOT_IN_STORE"):
        weather_release.stage_hosted(root, package_id, SITE, opener=opener)
    assert opener.requests == []
