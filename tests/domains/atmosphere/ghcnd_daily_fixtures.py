"""Offline fetcher for the GHCN-Daily pilot fixtures (no network)."""
import gzip
from pathlib import Path

from connectors.noaa.src.noaa import ghcnd
from connectors.noaa.src.noaa.ghcnd_daily_capture import STATION_LIST_KEY, capture

FIXTURES = Path(__file__).resolve().parents[3] / "fixtures/domains/atmosphere/ghcnd_daily"
END = "2026-10-10"
CAPTURED_AT = "2026-10-11T12:00:00Z"


def fixture_bytes(key, mutate=None):
    if key == STATION_LIST_KEY:
        text = (FIXTURES / "ghcnd-stations-excerpt.txt").read_text()
    else:
        text = (FIXTURES / key.removeprefix("by_station/").removesuffix(".gz").lower()).read_text()
    if mutate:
        text = mutate(key, text)
    return text.encode() if key == STATION_LIST_KEY else gzip.compress(text.encode(), mtime=0)


def fetcher(mutate=None):
    calls = []

    def fetch(key, limit):
        calls.append((key, limit))
        return fixture_bytes(key, mutate), {"source_url": ghcnd.object_url(key), "retrieved_at": CAPTURED_AT,
                                            "last_modified": "Sun, 11 Oct 2026 06:00:00 GMT", "etag": '"fixture"',
                                            "provider_checksum": None}
    fetch.calls = calls
    return fetch


def acquired(mutate=None, end=END):
    return capture(end, fetcher=fetcher(mutate), clock=lambda: CAPTURED_AT)
