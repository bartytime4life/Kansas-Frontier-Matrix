"""Owner release rehearsal: admitted package -> decision -> stage -> activate -> governed API answers."""
import json
from datetime import datetime, timedelta, timezone
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


class SiteOpener:
    """Answers the status and stage routes in order and records each request."""

    def __init__(self, active):
        self.active, self.requests = active, []

    def open(self, request, timeout):
        self.requests.append(request)
        if request.full_url.endswith("/status"):
            return FakeResponse({"active_package_id": self.active, "previous_package_id": None, "revision": 1})
        package_id = json.loads(request.data)["manifest"]["package_id"]
        return FakeResponse({"package_id": package_id, "state": "STAGED", "activated": False})


def cycle(tmp_path, *, acquire=acquired, now=None, **options):
    root = tmp_path / "store"
    init_store(root)
    now = now or datetime(2026, 9, 30, 19, 0, tzinfo=timezone.utc)
    return root, water_release.cycle(root, start="2026-09-30T00:00:00Z", end="2026-09-30T18:00:00Z", owner=OWNER,
                                     valid_days=7, clock=lambda: now, acquire=lambda *_: acquire(), **options)


def snapshot(root, package_id):
    return json.loads((root / "release/candidates/hydrology" / package_id.split(":")[1] / "snapshot.json").read_text())


def test_cycle_runs_capture_to_decision_without_activating(tmp_path):
    root, result = cycle(tmp_path)
    assert (result["outcome"], result["staged_hosted"], result["activated"], result["rollback_target"]) == ("DECIDED", False, False, None)
    decision = json.loads((root / result["decision_path"]).read_text())
    assert (decision["package_id"], decision["policy_ref"], decision["reviewer"]) == (result["package_id"], "kfm://adr/0044", OWNER)
    assert snapshot(root, result["package_id"])["manifest"]["candidate_id"] == result["candidate_id"]
    assert not (root / "release/active").exists()


def test_cycle_binds_the_site_active_package_and_stages_there(tmp_path, monkeypatch):
    monkeypatch.setenv("KFM_WATER_WORKER_TOKEN", "t" * 40)
    active = "sha256:" + "a" * 64
    opener = SiteOpener(active)
    root, result = cycle(tmp_path, site_url="https://kfm.example.test", opener=opener)
    assert (result["outcome"], result["staged_hosted"], result["activated"]) == ("STAGED_HOSTED", True, False)
    assert result["next"] == "https://kfm.example.test/governed/water-release"
    assert snapshot(root, result["package_id"])["manifest"]["rollback_target"] == active == result["rollback_target"]
    assert [(r.get_method(), r.full_url.rsplit("/", 1)[1]) for r in opener.requests] == [("GET", "status"), ("POST", "stage")]


def test_cycle_decides_after_the_capture_it_packages(tmp_path):
    # A live capture is stamped when it finishes (the fixture's retrieved_at is 18:01Z);
    # a decision timed before that would fail the gate with RELEASE_TIME_INVALID.
    events = []

    def clock():
        events.append("clock")
        return datetime(2026, 9, 30, 18, 1, 5, tzinfo=timezone.utc)
    root = tmp_path / "store"
    init_store(root)
    result = water_release.cycle(root, start="2026-09-29T18:00:00Z", end="2026-09-30T18:00:00Z", owner=OWNER,
                                 valid_days=7, clock=clock, acquire=lambda *_: events.append("capture") or acquired())
    assert events == ["capture", "clock"]
    decision = json.loads((root / result["decision_path"]).read_text())
    assert snapshot(root, result["package_id"])["manifest"]["created_at"] <= decision["reviewed_at"]


def test_cycle_checks_the_site_before_capturing(tmp_path, monkeypatch):
    captured = []
    monkeypatch.delenv("KFM_WATER_WORKER_TOKEN", raising=False)
    with pytest.raises(ValueError, match="WATER_WORKER_TOKEN_REQUIRED"):
        cycle(tmp_path, acquire=lambda: captured.append(1), site_url="https://kfm.example.test", opener=SiteOpener(None))
    monkeypatch.setenv("KFM_WATER_WORKER_TOKEN", "t" * 40)
    bad = SiteOpener("not-a-digest")
    with pytest.raises(ValueError, match="HOSTED_UNEXPECTED_RESPONSE"):
        cycle(tmp_path, acquire=lambda: captured.append(1), site_url="https://kfm.example.test", opener=bad)
    assert captured == []


def test_cycle_stops_at_a_quarantined_capture(tmp_path):
    def conflicting(records):
        other = dict(records[0], properties={**records[0]["properties"], "value": "99"})
        return [*records, other]
    with pytest.raises(ValueError, match="CAPTURE_NOT_READY"):
        cycle(tmp_path, acquire=lambda: acquired(conflicting))
    assert not (tmp_path / "store/release").exists()


def test_cycle_refuses_conflicting_rollback_sources(tmp_path):
    with pytest.raises(ValueError, match="ROLLBACK_TARGET_FROM_SITE"):
        cycle(tmp_path, site_url="https://kfm.example.test", rollback_target="sha256:" + "a" * 64)
    with pytest.raises(ValueError, match="ROLLBACK_TARGET_INVALID"):
        cycle(tmp_path, rollback_target="active")


def test_a_second_cycle_replaces_the_first_through_compare_and_swap(tmp_path, capsys):
    # Activation checks decisions against the real clock, so decide a minute ago.
    decided_at = datetime.now(timezone.utc) - timedelta(minutes=1)
    root, first = cycle(tmp_path, now=decided_at)
    second = water_release.cycle(root, start="2026-09-30T00:00:00Z", end="2026-09-30T18:00:00Z", owner=OWNER, valid_days=7,
                                 clock=lambda: decided_at + timedelta(seconds=30), rollback_target=first["package_id"],
                                 acquire=lambda *_: acquired())
    serving = tmp_path / "serving"
    for result in (first, second):
        code, _ = run(capsys, "stage", "--root", root, "--store", serving, "--package-id", result["package_id"], "--actor", OWNER)
        assert code == 0
        expected = result["rollback_target"] or "none"
        code, active = run(capsys, "activate", "--root", root, "--store", serving, "--decision", result["decision_path"],
                           "--expected-active", expected)
        assert (code, active["package_id"]) == (0, result["package_id"])
    assert active["revision"] == 2


def test_cycle_cli_rejects_a_plain_http_site_before_any_network(tmp_path, capsys, monkeypatch):
    monkeypatch.setattr(water_release, "capture", lambda *_: pytest.fail("captured before checking the Site"))
    code, refused = run(capsys, "cycle", "--root", tmp_path / "store", "--start", "2026-09-30T00:00:00Z",
                        "--end", "2026-09-30T18:00:00Z", "--owner", OWNER, "--site-url", "http://kfm.example.test")
    assert (code, refused) == (1, {"outcome": "ERROR", "reason_code": "SITE_URL_INVALID"})


def test_cycle_cli_defaults_to_the_24_hours_before_the_current_hour(tmp_path, capsys, monkeypatch):
    windows = []
    monkeypatch.setattr(water_release, "capture", lambda start, end: windows.append((start, end)) or acquired())
    code, result = run(capsys, "cycle", "--root", tmp_path / "store", "--owner", OWNER)
    assert (code, result["outcome"], result["activated"]) == (0, "DECIDED", False)
    [(start, end)] = windows
    assert end.endswith(":00:00Z") and (result["start"], result["end"]) == (start, end)
    parse = lambda value: datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
    assert parse(end) - parse(start) == timedelta(hours=24)


# Release-time integrity (as soil and weather, #5051): a resealed package is refused before any decision.
NOW = datetime(2026, 10, 11, 13, 0, tzinfo=timezone.utc)


def _snapshot_path(root, package_id):
    return root / "release/candidates/hydrology" / package_id.split(":")[1] / "snapshot.json"


def _write(root, snapshot):
    from connectors_core.captured_json import canonical_bytes
    package_id = snapshot["manifest"]["package_id"]
    path = _snapshot_path(root, package_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(canonical_bytes(snapshot))
    return package_id


def _values(root, package_id):
    snapshot = json.loads(_snapshot_path(root, package_id).read_text())
    return snapshot, {name: json.loads(text) for name, text in snapshot["artifacts"].items()}


def test_decide_requires_the_candidate_to_match_its_stored_capture(tmp_path):
    # A value is changed consistently in the observation and its revision history, every digest and
    # the receipt are rebuilt by the normal package builder; only the stored capture disagrees.
    from connectors_core.captured_json import canonical_bytes, digest_bytes
    from pipelines.domains.hydrology.admission import load_admission
    from pipelines.domains.hydrology.package import prepare_water_package
    root, preparation = prepared(tmp_path, admitted=True)
    _, values = _values(root, preparation["package_id"])
    candidate = values["candidate.json"]
    target = candidate["observations"][0]["id"]
    for record in candidate["observations"] + candidate["revision_history"]:
        if record["id"] == target:
            record["value"] = record["value"] + 1
            record["record_digest"] = digest_bytes(canonical_bytes({k: v for k, v in record.items() if k != "record_digest"}))
    candidate["candidate_id"] = digest_bytes(canonical_bytes({k: v for k, v in candidate.items() if k != "candidate_id"}))
    package_id = _write(root, prepare_water_package(candidate, admission=load_admission()))
    with pytest.raises(ValueError, match="CANDIDATE_CAPTURE_MISMATCH"):
        water_release.decide(root, package_id, reviewer=OWNER, releaser=OWNER, valid_days=7, now=NOW)
    assert not (root / "release/decisions").exists()


def test_decide_refuses_a_receipt_that_differs_from_revalidation(tmp_path, monkeypatch):
    from connectors_core.captured_json import canonical_bytes, digest_bytes
    from pipelines.domains.hydrology import package as water_package
    from pipelines.domains.hydrology.admission import load_admission
    root, preparation = prepared(tmp_path, admitted=True)
    _, values = _values(root, preparation["package_id"])

    def miscounting(_candidate):
        report = {k: v for k, v in values["validation.json"].items() if k != "receipt_digest"}
        report["observations"] += 1
        report["receipt_digest"] = digest_bytes(canonical_bytes(report))
        return report
    monkeypatch.setattr(water_package, "validate_candidate", miscounting)
    package_id = _write(root, water_package.prepare_water_package(values["candidate.json"], admission=load_admission()))
    with pytest.raises(ValueError, match="VALIDATION_RECEIPT_MISMATCH"):
        water_release.decide(root, package_id, reviewer=OWNER, releaser=OWNER, valid_days=7, now=NOW)


def test_a_held_package_resealed_as_admitted_cannot_be_self_released(tmp_path):
    from connectors_core.captured_json import canonical_bytes, digest_bytes
    from hashing import compute_spec_hash
    from pipelines.domains.hydrology.admission import load_admission
    root, preparation = prepared(tmp_path, admitted=False)
    snapshot, values = _values(root, preparation["package_id"])
    evidence = values["evidence.json"]
    for entry in evidence["entries"]:
        bundle = entry["bundle"]
        bundle["rights"] = {"license": load_admission()["license"]}
        bundle["sensitivity"] = {**bundle["sensitivity"], "level": "public", "reason": "forged"}
        bundle["spec_hash"] = {"value": compute_spec_hash({k: v for k, v in bundle.items() if k != "spec_hash"})}
    text = canonical_bytes(evidence).decode()
    manifest = snapshot["manifest"]
    manifest["artifacts"]["evidence.json"] = digest_bytes(text.encode())
    snapshot["artifacts"]["evidence.json"] = text
    manifest["package_id"] = compute_spec_hash({k: v for k, v in manifest.items() if k != "package_id"})
    package_id = _write(root, snapshot)
    with pytest.raises(ValueError, match="PACKAGE_NOT_REPRODUCIBLE"):
        water_release.decide(root, package_id, reviewer=OWNER, releaser=OWNER, valid_days=7, now=NOW)
    assert not (root / "release/decisions").exists()


def test_decide_and_hosted_staging_need_the_stored_capture(tmp_path, monkeypatch):
    import shutil
    root, preparation = prepared(tmp_path, admitted=True)
    shutil.rmtree(root / "data/quarantine/usgs-nwis/runs")
    with pytest.raises(ValueError, match="CAPTURE_NOT_IN_STORE"):
        water_release.decide(root, preparation["package_id"], reviewer=OWNER, releaser=OWNER, valid_days=7, now=NOW)
    monkeypatch.setenv("KFM_WATER_WORKER_TOKEN", "t" * 40)
    opener = FakeOpener({})
    with pytest.raises(ValueError, match="CAPTURE_NOT_IN_STORE"):
        water_release.stage_hosted(root, preparation["package_id"], "https://kfm.example.test", opener=opener)
    assert opener.requests == []
