from datetime import datetime, timedelta, timezone
from pathlib import Path
import pytest
from tools.local_data.water_job import run
from tools.local_data.water_pilot import main
from tests.domains.hydrology.test_usgs_water_normalizer import acquired


def test_candidate_job_has_no_activation_or_publication_side_effects(tmp_path):
    calls = []
    def provider(start, end):
        calls.append((start, end)); return acquired()
    result = run(tmp_path / "data", now=datetime(2026,9,30,18,42,tzinfo=timezone.utc), acquire=provider)
    assert calls == [("2026-09-29T18:00:00Z", "2026-09-30T18:00:00Z")]
    assert result["authority"] == "CANDIDATE_ONLY"
    assert not result["published"] and not result["released"]
    assert not result["package"]["activated"]
    assert not list(tmp_path.rglob("activation.sqlite"))
    assert not list(tmp_path.rglob("*decision*.json"))


def test_worker_operation_allowlist_precedes_filesystem_write(tmp_path):
    with pytest.raises(SystemExit) as result:
        main(["--root", str(tmp_path/"absent"), "replay", "--capture-id", "sha256:"+"0"*64], allowed_operations={"capture"})
    assert result.value.code == 2
    assert not (tmp_path/"absent").exists()


def test_job_rejects_naive_clock_before_store_initialization(tmp_path):
    root = tmp_path / "data"

    with pytest.raises(ValueError, match="WATER_JOB_NOW_NOT_TIMEZONE_AWARE"):
        run(root, now=datetime(2026, 9, 30, 18, 42))

    assert not root.exists()


def test_job_normalizes_aware_clock_before_acquisition(tmp_path):
    calls = []

    def provider(start, end):
        calls.append((start, end))
        return acquired()

    run(
        tmp_path / "data",
        now=datetime(2026, 9, 30, 13, 42, tzinfo=timezone(timedelta(hours=-5))),
        acquire=provider,
    )

    assert calls == [("2026-09-29T18:00:00Z", "2026-09-30T18:00:00Z")]
