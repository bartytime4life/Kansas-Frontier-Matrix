"""Offline fetcher for the Storm Events pilot fixtures (no network)."""
from pathlib import Path
import struct
import zlib

from connectors.noaa.src.noaa.storm_events_capture import LISTING_KEY, capture, object_url

FIXTURES = Path(__file__).resolve().parents[3] / "fixtures/domains/hazards/storm_events"
YEAR = 2025
CAPTURED_AT = "2025-11-01T12:00:00Z"
DETAILS = "StormEvents_details-ftp_v1.0_d2025_c20251020.csv.gz"


def stored_gzip(raw: bytes) -> bytes:
    """gzip with stored deflate blocks and a fixed header, identical on every Python version."""
    chunks = [raw[i:i + 65535] for i in range(0, len(raw), 65535)] or [b""]
    blocks = b"".join(bytes([i == len(chunks) - 1]) + struct.pack("<HH", len(c), len(c) ^ 0xFFFF) + c
                      for i, c in enumerate(chunks))
    return b"\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\xff" + blocks + struct.pack("<II", zlib.crc32(raw), len(raw) & 0xFFFFFFFF)


def fixture_bytes(key, mutate=None):
    if key == LISTING_KEY:
        text = (FIXTURES / "listing.html").read_text()
        return (mutate(key, text) if mutate else text).encode()
    text = (FIXTURES / "stormevents_details_d2025.csv").read_text()
    return stored_gzip((mutate(key, text) if mutate else text).encode())


def fetcher(mutate=None):
    calls = []

    def fetch(key, limit):
        calls.append((key, limit))
        return fixture_bytes(key, mutate), {"source_url": object_url(key), "retrieved_at": CAPTURED_AT,
                                            "last_modified": "Mon, 20 Oct 2025 10:00:00 GMT", "etag": '"fixture"'}
    fetch.calls = calls
    return fetch


def acquired(mutate=None, year=YEAR):
    return capture(year, fetcher=fetcher(mutate), clock=lambda: CAPTURED_AT)
