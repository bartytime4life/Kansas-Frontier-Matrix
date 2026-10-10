"""Owner release rehearsal: admitted package -> decision -> stage -> activate -> governed API answers."""
import json
from threading import Thread
from urllib.request import urlopen
from wsgiref.simple_server import WSGIRequestHandler, make_server

import pytest
from governed_api import main as api
from release.local_store import LocalReleaseStore

from tests.domains.hydrology.test_usgs_water_normalizer import acquired
from tools.local_data.manage import init_store
from tools.local_data.water_pilot import stage as stage_capture
from tools.release import water_release
from tools.release.water_snapshot import prepare

OWNER = "@bartytime4life"


def run(capsys, *argv):
    code = water_release.main([str(a) for a in argv])
    return code, json.loads(capsys.readouterr().out)


def prepared(tmp_path, *, admitted):
    root = tmp_path / "store"
    init_store(root)
    candidate_id = stage_capture(root, acquired())["candidate_id"]
    return root, prepare(root, candidate_id, admitted_source=admitted)


def test_owner_releases_admitted_package_and_governed_api_answers(tmp_path, capsys, monkeypatch):
    root, preparation = prepared(tmp_path, admitted=True)
    assert preparation["reason_code"] == "RELEASE_DECISION_REQUIRED"
    package_id = preparation["package_id"]
    serving = tmp_path / "serving"

    code, decided = run(capsys, "decide", "--root", root, "--package-id", package_id, "--reviewer", OWNER, "--releaser", OWNER)
    assert (code, decided["outcome"], decided["activated"]) == (0, "DECIDED", False)
    decision = json.loads((root / decided["decision_path"]).read_text())
    assert decision["policy_ref"] == "kfm://adr/0044"

    code, staged = run(capsys, "stage", "--root", root, "--store", serving, "--package-id", package_id, "--actor", OWNER)
    assert (code, staged["outcome"]) == (0, "STAGED")
    code, active = run(capsys, "activate", "--root", root, "--store", serving, "--decision", decided["decision_path"], "--expected-active", "none")
    assert (code, active["outcome"], active["package_id"], active["revision"]) == (0, "ACTIVATED", package_id, 1)

    # A second activation with a stale expectation is refused instead of overwriting.
    code, conflict = run(capsys, "activate", "--root", root, "--store", serving, "--decision", decided["decision_path"], "--expected-active", "none")
    assert (code, conflict["reason_code"]) == (1, "ACTIVATION_CONFLICT")

    monkeypatch.setattr(api, "_RELEASE_STORE", LocalReleaseStore(str(serving)))

    class Silent(WSGIRequestHandler):
        def log_message(self, *_):
            return None

    with make_server("127.0.0.1", 0, api.app, handler_class=Silent) as server:
        thread = Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            with urlopen(f"http://127.0.0.1:{server.server_port}/v1/layers", timeout=2) as response:
                layers = json.load(response)
        finally:
            server.shutdown()
            thread.join(timeout=2)
    assert layers["envelope"]["outcome"] == "ANSWER"
    assert layers["data"]["package_id"] == package_id
    assert sorted(s["id"] for s in layers["data"]["stations"]) == ["USGS-06892518", "USGS-07156900"]


def test_unadmitted_package_cannot_be_self_released(tmp_path, capsys):
    root, preparation = prepared(tmp_path, admitted=False)
    assert preparation["reason_code"] == "REVIEW_REQUIRED"
    code, refused = run(capsys, "decide", "--root", root, "--package-id", preparation["package_id"],
                        "--reviewer", OWNER, "--releaser", OWNER)
    assert (code, refused) == (1, {"outcome": "ERROR", "reason_code": "INDEPENDENT_REVIEW_REQUIRED"})
    assert not (root / "release/decisions").exists()


def test_decision_validity_is_bounded(tmp_path, capsys):
    root, preparation = prepared(tmp_path, admitted=True)
    code, refused = run(capsys, "decide", "--root", root, "--package-id", preparation["package_id"],
                        "--reviewer", OWNER, "--releaser", OWNER, "--valid-days", 31)
    assert (code, refused["reason_code"]) == (1, "VALID_DAYS_OUT_OF_RANGE")


class FakeResponse:
    def __init__(self, body):
        self.body = json.dumps(body).encode()

    def read(self, _limit):
        return self.body

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False


class FakeOpener:
    def __init__(self, body):
        self.body, self.requests = body, []

    def open(self, request, timeout):
        self.requests.append(request)
        return FakeResponse(self.body)


def test_stage_hosted_posts_the_prepared_package_and_never_activates(tmp_path, monkeypatch):
    root, preparation = prepared(tmp_path, admitted=True)
    package_id = preparation["package_id"]
    monkeypatch.setenv("KFM_WATER_WORKER_TOKEN", "t" * 40)
    monkeypatch.setenv("KFM_SITES_BYPASS_TOKEN", "bypass")
    opener = FakeOpener({"package_id": package_id, "state": "STAGED", "activated": False})
    result = water_release.stage_hosted(root, package_id, "https://kfm.example.test", opener=opener)
    assert result == {"outcome": "STAGED_HOSTED", "package_id": package_id, "site": "kfm.example.test", "activated": False}
    [request] = opener.requests
    assert request.full_url == "https://kfm.example.test/api/governed/water-admin/stage"
    assert request.get_header("Authorization") == "Bearer " + "t" * 40
    assert request.get_header("Oai-sites-authorization") == "Bearer bypass"
    assert request.data == (root / "release/candidates/hydrology" / package_id.split(":")[1] / "snapshot.json").read_bytes()


def test_stage_hosted_refuses_unsafe_urls_missing_tokens_and_activation_claims(tmp_path, monkeypatch):
    root, preparation = prepared(tmp_path, admitted=True)
    package_id = preparation["package_id"]
    monkeypatch.setenv("KFM_WATER_WORKER_TOKEN", "t" * 40)
    for url in ("http://kfm.example.test", "https://kfm.example.test/other", "https://kfm.example.test/?x=1"):
        with pytest.raises(ValueError, match="SITE_URL_INVALID"):
            water_release.stage_hosted(root, package_id, url, opener=FakeOpener({}))
    activated = FakeOpener({"package_id": package_id, "state": "STAGED", "activated": True})
    with pytest.raises(ValueError, match="HOSTED_STAGING_UNEXPECTED_RESPONSE"):
        water_release.stage_hosted(root, package_id, "https://kfm.example.test", opener=activated)
    monkeypatch.setenv("KFM_WATER_WORKER_TOKEN", "short")
    with pytest.raises(ValueError, match="WATER_WORKER_TOKEN_REQUIRED"):
        water_release.stage_hosted(root, package_id, "https://kfm.example.test", opener=FakeOpener({}))
