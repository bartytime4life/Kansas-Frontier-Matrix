"""Replay three committed synthetic capture packets into validated in-memory candidates.

This fixed allowlist is a fixture harness, not a declaration executor or a source
scheduler. It performs no retrieval, storage, admission, promotion, or release.
Install the project-test and connectors-core dependency profiles before use.
"""
from __future__ import annotations

import argparse
import base64
import binascii
from importlib import import_module
import re
from pathlib import Path
import sys

from connectors_core.captured_json import canonical_bytes, decode_object, digest_bytes
from tools.local_data.file_io import read_regular

ROOT = Path(__file__).resolve().parents[1]
PACKET_LIMIT = 1024 * 1024
DIGEST = re.compile(r"sha256:[a-f0-9]{64}\Z")
# Explicit bindings only; declarations and directory scans never execute code.
PIPELINES = {
    "earthquake": ("hazards/earthquakes", "pipelines.domains.hazards.earthquake"),
    "storm-events": ("hazards/storm_events", "pipelines.domains.hazards.storm_events"),
    "water-observations": ("hydrology/usgs_water_replay", "pipelines.domains.hydrology"),
}
PACKET_KEYS = {"fixture_only", "pipeline", "manifest", "objects_base64", "expected_candidate_id"}


def fixture_path(name: str) -> Path:
    if name not in PIPELINES:
        raise ValueError("FIXTURE_PIPELINE_UNKNOWN")
    return ROOT / "fixtures/domains" / PIPELINES[name][0] / "replay.json"


def replay_packet(name: str, raw: bytes) -> dict:
    """Validate a bounded test packet, replay preserved bytes, and check its golden identity.

    ``fixture_only`` is a test-packet label, not proof of external provenance.
    The CLI reads only the fixed committed packets. Library callers supply bytes
    and receive in-memory results; they acquire no source or release authority.
    """
    fixture_path(name)  # Refuse unknown names before parsing or importing a transform.
    packet = decode_object(raw, limit=PACKET_LIMIT)
    if (set(packet) != PACKET_KEYS or packet["fixture_only"] is not True
            or packet["pipeline"] != name or not isinstance(packet["manifest"], dict)
            or not isinstance(packet["expected_candidate_id"], str)
            or not DIGEST.fullmatch(packet["expected_candidate_id"])):
        raise ValueError("FIXTURE_PACKET_INVALID")
    encoded = packet["objects_base64"]
    if not isinstance(encoded, dict) or not 1 <= len(encoded) <= 16:
        raise ValueError("FIXTURE_OBJECTS_INVALID")
    objects = {}
    for key, value in encoded.items():
        if not DIGEST.fullmatch(key) or not isinstance(value, str):
            raise ValueError("FIXTURE_OBJECTS_INVALID")
        try:
            body = base64.b64decode(value, validate=True)
        except (ValueError, binascii.Error):
            raise ValueError("FIXTURE_BASE64_INVALID") from None
        if digest_bytes(body) != key:
            raise ValueError("FIXTURE_OBJECT_DIGEST_MISMATCH")
        objects[key] = body
    pages = packet["manifest"].get("pages")
    if (not isinstance(pages, list) or not 1 <= len(pages) <= 16
            or any(not isinstance(page, dict) or type(page.get("bytes")) is not int
                   or page["bytes"] < 0 or not isinstance(page.get("sha256"), str) for page in pages)
            or set(objects) != {page["sha256"] for page in pages if page["bytes"] > 0}):
        raise ValueError("FIXTURE_OBJECT_CLOSURE_INVALID")
    prefix = PIPELINES[name][1]
    normalize_module = prefix + (".normalize" if name == "water-observations" else "_normalize")
    validate_module = prefix + (".validate" if name == "water-observations" else "_validate")
    candidate = import_module(normalize_module).normalize_capture(packet["manifest"], objects)
    validation = import_module(validate_module).validate_candidate(candidate)
    if candidate["candidate_id"] != packet["expected_candidate_id"]:
        raise ValueError("FIXTURE_REPLAY_IDENTITY_MISMATCH")
    return {"fixture_only": True, "pipeline": name, "fixture_sha256": digest_bytes(raw),
            "candidate": candidate, "validation": validation}


def replay_fixture(name: str) -> dict:
    """Read one fixed regular fixture packet without writing lifecycle artifacts."""
    return replay_packet(name, read_regular(fixture_path(name), PACKET_LIMIT))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pipeline", choices=sorted(PIPELINES))
    args = parser.parse_args(argv)
    try:
        result = replay_fixture(args.pipeline)
    except (ValueError, OSError) as exc:
        reason = str(exc) if isinstance(exc, ValueError) else "FIXTURE_READ_FAILED"
        print(canonical_bytes({"outcome": "FAIL", "reason": reason}).decode(), file=sys.stderr)
        return 1
    print(canonical_bytes(result).decode())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
