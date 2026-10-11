"""Offline fetcher for the USCRN daily soil pilot fixtures (no network)."""
from pathlib import Path

from connectors.noaa.src.noaa import uscrn_daily
from connectors.noaa.src.noaa.uscrn_daily_capture import capture

FIXTURES = Path(__file__).resolve().parents[3] / "fixtures/domains/soil/uscrn_daily"
END = "2026-10-10"
CAPTURED_AT = "2026-10-11T12:00:00Z"


def fixture_bytes(key, mutate=None):
    name = key if key == uscrn_daily.HEADERS_KEY else key.split("/", 1)[1].lower()
    text = (FIXTURES / name).read_text()
    return (mutate(key, text) if mutate else text).encode()


def fetcher(mutate=None):
    calls = []

    def fetch(key, limit):
        calls.append((key, limit))
        return fixture_bytes(key, mutate), {"source_url": uscrn_daily.object_url(key), "retrieved_at": CAPTURED_AT,
                                            "last_modified": "Sun, 11 Oct 2026 06:00:00 GMT", "etag": '"fixture"'}
    fetch.calls = calls
    return fetch


def acquired(mutate=None, end=END):
    return capture(end, fetcher=fetcher(mutate), clock=lambda: CAPTURED_AT)
