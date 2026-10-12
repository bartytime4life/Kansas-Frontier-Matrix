"""Offline fetcher for the USGS earthquake pilot fixtures (no network)."""
import json
from pathlib import Path

from connectors.usgs.src.usgs.earthquake_capture import capture, object_url

FIXTURES = Path(__file__).resolve().parents[3] / "fixtures/domains/hazards/earthquakes"
YEAR = 2025
CAPTURED_AT = "2025-11-01T12:00:00Z"


def fixture_bytes(key, mutate=None):
    """A month's committed page as bytes, or b"" (HTTP 204) when the month has no fixture.

    ``mutate(key, document)`` sees None for a month with no fixture and may return a document for it."""
    path = FIXTURES / f"{key}.geojson"
    document = json.loads(path.read_text()) if path.is_file() else None
    if mutate:
        document = mutate(key, document)
    return b"" if document is None else json.dumps(document).encode()


def fetcher(mutate=None):
    calls = []

    def fetch(key, limit):
        calls.append((key, limit))
        raw = fixture_bytes(key, mutate)
        return raw, {"source_url": object_url(key), "status": 200 if raw else 204, "retrieved_at": CAPTURED_AT,
                     "last_modified": None, "etag": None}
    fetch.calls = calls
    return fetch


def acquired(mutate=None, year=YEAR, clock=CAPTURED_AT):
    return capture(year, fetcher=fetcher(mutate), clock=lambda: clock)
