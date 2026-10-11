#!/usr/bin/env python3
"""Generate the Site's GHCN-Daily weather fixtures from the Python release code.

The Site's tests/governed-weather.test.mjs must reproduce the Python projection
outputs (bootstrap/layers/evidence) from the same snapshot and decision, so the
two implementations are held to one contract. Inputs are the synthetic
fixtures/domains/atmosphere/ghcnd_daily files; nothing here is a real release.

Usage: --check (default) compares with the committed Site fixtures; --write
rewrites them after an intended change.
"""
from pathlib import Path
import argparse
import gzip
import struct
import sys
import zlib

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from connectors_core.captured_json import canonical_bytes
from pipelines.domains.atmosphere.ghcnd_daily_admission import load_admission
from pipelines.domains.atmosphere.ghcnd_daily_normalize import normalize_capture
from pipelines.domains.atmosphere.ghcnd_daily_package import prepare_weather_package
from policy_runtime.core import WEATHER_DECISION_PROFILE
from release.weather_projection import project
from connectors.noaa.src.noaa.ghcnd_daily_capture import STATION_LIST_KEY, capture
from tests.domains.atmosphere.ghcnd_daily_fixtures import CAPTURED_AT, END, fetcher

SITE_FIXTURES = ROOT / "apps/site/source/tests/fixtures/governed-weather"
EVALUATED_AT = "2026-10-11T13:00:00Z"


KEEP_DAYS = ("20261004", "20261005", "20261009", "20261010")


def _sparse(key: str, text: str) -> str:
    """Keep a few days per station so the Site fixtures stay small.

    The 30-day window and four stations are unchanged; Goodland (data only to
    2026-10-05) stays STALE, and one quality-flagged TMAX stays withheld.
    """
    if key == "ghcnd-stations.txt":
        return text
    rows = [row for row in text.splitlines() if row.split(",")[1] in KEEP_DAYS]
    text = "\n".join(rows) + "\n"
    return text.replace("USW00003928,20261010,TMAX,160,,,W,", "USW00003928,20261010,TMAX,160,,I,W,")


def _stored_gzip(raw: bytes) -> bytes:
    """gzip with stored (uncompressed) deflate blocks and a fixed header.

    gzip.compress writes a different OS byte on Python 3.11/3.12 and 3.13, and every
    capture digest chains from these bytes, so the fixtures must not depend on it.
    """
    chunks = [raw[i:i + 65535] for i in range(0, len(raw), 65535)] or [b""]
    blocks = b"".join(bytes([i == len(chunks) - 1]) + struct.pack("<HH", len(c), len(c) ^ 0xFFFF) + c
                      for i, c in enumerate(chunks))
    return b"\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\xff" + blocks + struct.pack("<II", zlib.crc32(raw), len(raw) & 0xFFFFFFFF)


def _acquired():
    fetch = fetcher(_sparse)

    def deterministic(key, limit):
        raw, meta = fetch(key, limit)
        return (raw if key == STATION_LIST_KEY else _stored_gzip(gzip.decompress(raw))), meta
    return capture(END, fetcher=deterministic, clock=lambda: CAPTURED_AT)


def generated() -> dict[str, bytes]:
    source = _acquired()
    candidate = normalize_capture(source.manifest, source.objects)
    admitted = prepare_weather_package(candidate, admission=load_admission())
    decision = {"profile": WEATHER_DECISION_PROFILE, "package_id": admitted["manifest"]["package_id"],
                "decision": "APPROVED", "reviewed_at": "2026-10-11T12:30:00Z", "released_at": "2026-10-11T12:45:00Z",
                "expires_at": "2026-10-18T12:45:00Z", "correction_state": "ACTIVE", "correction_ref": None,
                "reviewer": "synthetic-owner", "releaser": "synthetic-owner"}
    for name in ("source_admission", "rights", "sensitivity", "policy", "review", "release"):
        decision[name + "_ref"] = "kfm://synthetic/" + name
    values = {"admitted-snapshot.json": admitted, "owner-decision.json": decision}
    for view in ("bootstrap", "layers", "evidence"):
        values[view + ".json"] = project(canonical_bytes(admitted), decision, view=view, now=EVALUATED_AT)
        if values[view + ".json"]["envelope"]["outcome"] != "ANSWER":
            raise ValueError("FIXTURE_PROJECTION_NOT_ANSWER")
    return {name: canonical_bytes(value) for name, value in values.items()}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args(argv)
    values = generated()
    if args.write:
        SITE_FIXTURES.mkdir(parents=True, exist_ok=True)
        for name, raw in values.items():
            (SITE_FIXTURES / name).write_bytes(raw)
        print(f"wrote {len(values)} fixtures")
        return 0
    drift = sorted(name for name, raw in values.items()
                   if not (SITE_FIXTURES / name).is_file() or (SITE_FIXTURES / name).read_bytes() != raw)
    extra = sorted(p.name for p in SITE_FIXTURES.iterdir() if p.name not in values) if SITE_FIXTURES.is_dir() else []
    print({"outcome": "PASS" if not drift and not extra else "FAIL", "drift": drift, "unexpected": extra})
    return 0 if not drift and not extra else 1


if __name__ == "__main__":
    raise SystemExit(main())
