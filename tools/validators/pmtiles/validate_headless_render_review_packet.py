#!/usr/bin/env python3
"""Validate a fixture-only headless PMTiles render review packet.

Success proves bounded local screenshot/metrics/sidecar integrity only. It does
not prove a published PMTiles carrier, MapLibre boot, style health, policy,
release, deployment, publication, or public-use readiness.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import struct
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

METRICS_PROFILE = "kfm.pmtiles.headless-render-review-metrics.v1"
SIDECAR_PROFILE = "kfm.pmtiles.headless-render-review-sidecar.v1"
REQUIRED_FILES = (
    "headless-render.png",
    "metrics.json",
    "sidecar.json",
)
EXPECTED_HOLDS = (
    "PUBLISHED_PMTILES_NOT_LOADED",
    "CRYPTOGRAPHIC_VERIFICATION_UNWIRED",
    "MAPLIBRE_RUNTIME_UNADMITTED",
    "STYLE_HEALTH_NOT_EVALUATED",
    "RELEASE_AUTHORIZATION_NOT_EVALUATED",
)
MAX_SCREENSHOT_BYTES = 5 * 1024 * 1024
MAX_JSON_BYTES = 64 * 1024
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
SHA256_PREFIX = "sha256:"
ZERO_HASH = SHA256_PREFIX + ("0" * 64)

METRICS_FIELDS = frozenset(
    {
        "profile",
        "status",
        "execution_mode",
        "outcome",
        "code",
        "source_kind",
        "viewport",
        "browser",
        "archive",
        "render",
        "timing",
        "external_request_count",
        "maplibre_boot_state",
        "style_health",
        "publication_state",
        "authority",
        "holds",
    }
)
SIDECAR_FIELDS = frozenset(
    {
        "profile",
        "status",
        "execution_mode",
        "source_kind",
        "artifacts",
        "maplibre_boot_state",
        "style_health",
        "publication_state",
        "authority",
        "holds",
        "review_only",
    }
)


class _DuplicateKeyError(ValueError):
    pass


class _NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str


def _reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in pairs:
        if key in value:
            raise _DuplicateKeyError(key)
        value[key] = item
    return value


def _reject_nonfinite(_value: str) -> object:
    raise _NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise _NonFiniteNumberError
    return parsed


def _load_json(path: Path) -> tuple[dict[str, object] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("HEADLESS_RENDER_REVIEW_SYMLINK_DENIED")]
        if not path.is_file():
            return None, [Finding("HEADLESS_RENDER_REVIEW_ARTIFACT_NOT_FILE")]
        if path.stat().st_size > MAX_JSON_BYTES:
            return None, [Finding("HEADLESS_RENDER_REVIEW_JSON_TOO_LARGE")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_nonfinite,
            parse_float=_parse_finite_float,
        )
    except _DuplicateKeyError:
        return None, [Finding("HEADLESS_RENDER_REVIEW_DUPLICATE_KEY")]
    except _NonFiniteNumberError:
        return None, [Finding("HEADLESS_RENDER_REVIEW_NONFINITE_NUMBER")]
    except (UnicodeError, json.JSONDecodeError):
        return None, [Finding("HEADLESS_RENDER_REVIEW_JSON_INVALID")]
    except (OSError, RecursionError, ValueError):
        return None, [Finding("HEADLESS_RENDER_REVIEW_JSON_UNREADABLE")]
    if not isinstance(value, dict):
        return None, [Finding("HEADLESS_RENDER_REVIEW_JSON_ROOT_INVALID")]
    return value, []


def _sha256(value: bytes) -> str:
    return SHA256_PREFIX + hashlib.sha256(value).hexdigest()


def _valid_hash(value: object) -> bool:
    return (
        isinstance(value, str)
        and len(value) == len(SHA256_PREFIX) + 64
        and value.startswith(SHA256_PREFIX)
        and all(character in "0123456789abcdef" for character in value[7:])
        and value != ZERO_HASH
    )


def _is_number(value: object) -> bool:
    return (
        not isinstance(value, bool)
        and isinstance(value, (int, float))
        and math.isfinite(float(value))
    )


def _common_posture(value: dict[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if value.get("status") != "PROPOSED_INACTIVE":
        findings.add(Finding("HEADLESS_RENDER_REVIEW_STATUS_INVALID"))
    if value.get("execution_mode") != "SYNTHETIC_FIXTURE_ONLY":
        findings.add(Finding("HEADLESS_RENDER_REVIEW_EXECUTION_MODE_INVALID"))
    if value.get("source_kind") != "SYNTHETIC_FIXTURE":
        findings.add(Finding("HEADLESS_RENDER_REVIEW_SOURCE_KIND_INVALID"))
    if value.get("maplibre_boot_state") != "HOLD":
        findings.add(Finding("HEADLESS_RENDER_REVIEW_MAPLIBRE_OVERCLAIM"))
    if value.get("style_health") != "NOT_EVALUATED":
        findings.add(Finding("HEADLESS_RENDER_REVIEW_STYLE_OVERCLAIM"))
    if value.get("publication_state") != "NOT_EVALUATED":
        findings.add(Finding("HEADLESS_RENDER_REVIEW_PUBLICATION_OVERCLAIM"))
    if value.get("authority") != "NONE":
        findings.add(Finding("HEADLESS_RENDER_REVIEW_AUTHORITY_OVERCLAIM"))
    if value.get("holds") != list(EXPECTED_HOLDS):
        findings.add(Finding("HEADLESS_RENDER_REVIEW_HOLDS_INVALID"))
    return sorted(findings)


def _validate_metrics(value: object) -> list[Finding]:
    if not isinstance(value, dict) or set(value) != METRICS_FIELDS:
        return [Finding("HEADLESS_RENDER_REVIEW_METRICS_SHAPE_INVALID")]
    findings: set[Finding] = set(_common_posture(value))
    if value.get("profile") != METRICS_PROFILE:
        findings.add(Finding("HEADLESS_RENDER_REVIEW_METRICS_PROFILE_INVALID"))
    if (
        value.get("outcome") != "PASS"
        or value.get("code") != "HEADLESS_RENDER_REVIEW_PACKET_PASS"
    ):
        findings.add(Finding("HEADLESS_RENDER_REVIEW_OUTCOME_INVALID"))
    if value.get("external_request_count") != 0:
        findings.add(Finding("HEADLESS_RENDER_REVIEW_EXTERNAL_REQUEST"))
    if value.get("viewport") != {
        "width": 390,
        "height": 844,
        "device_scale_factor": 3,
        "has_touch": True,
        "is_mobile": True,
    }:
        findings.add(Finding("HEADLESS_RENDER_REVIEW_VIEWPORT_INVALID"))
    if value.get("browser") != {"engine": "chromium", "headless": True}:
        findings.add(Finding("HEADLESS_RENDER_REVIEW_BROWSER_INVALID"))
    if value.get("archive") != {
        "name": "mobile-base.pmtiles",
        "archive_bytes": 347,
        "tile_bytes": 70,
    }:
        findings.add(Finding("HEADLESS_RENDER_REVIEW_ARCHIVE_INVALID"))
    if value.get("render") != {
        "decoded": True,
        "rendered": True,
        "width": 1,
        "height": 1,
        "pixel_rgba": [17, 34, 51, 255],
    }:
        findings.add(Finding("HEADLESS_RENDER_REVIEW_RENDER_INVALID"))
    timing = value.get("timing")
    if (
        not isinstance(timing, dict)
        or set(timing) != {"verify_ms", "decode_render_ms"}
        or any(
            not _is_number(timing.get(field))
            or not 0 <= float(timing[field]) <= 2500
            for field in ("verify_ms", "decode_render_ms")
        )
    ):
        findings.add(Finding("HEADLESS_RENDER_REVIEW_TIMING_INVALID"))
    return sorted(findings)


def _validate_png(path: Path) -> list[Finding]:
    try:
        if path.is_symlink():
            return [Finding("HEADLESS_RENDER_REVIEW_SYMLINK_DENIED")]
        if not path.is_file():
            return [Finding("HEADLESS_RENDER_REVIEW_ARTIFACT_NOT_FILE")]
        size = path.stat().st_size
        if not 24 <= size <= MAX_SCREENSHOT_BYTES:
            return [Finding("HEADLESS_RENDER_REVIEW_SCREENSHOT_SIZE_INVALID")]
        header = path.read_bytes()[:24]
    except OSError:
        return [Finding("HEADLESS_RENDER_REVIEW_SCREENSHOT_UNREADABLE")]
    if (
        header[:8] != PNG_SIGNATURE
        or header[8:12] != struct.pack(">I", 13)
        or header[12:16] != b"IHDR"
    ):
        return [Finding("HEADLESS_RENDER_REVIEW_SCREENSHOT_INVALID")]
    width, height = struct.unpack(">II", header[16:24])
    if not 0 < width <= 10000 or not 0 < height <= 10000:
        return [Finding("HEADLESS_RENDER_REVIEW_SCREENSHOT_DIMENSIONS_INVALID")]
    return []


def _validate_sidecar(
    value: object,
    directory: Path,
) -> list[Finding]:
    if not isinstance(value, dict) or set(value) != SIDECAR_FIELDS:
        return [Finding("HEADLESS_RENDER_REVIEW_SIDECAR_SHAPE_INVALID")]
    findings: set[Finding] = set(_common_posture(value))
    if value.get("profile") != SIDECAR_PROFILE:
        findings.add(Finding("HEADLESS_RENDER_REVIEW_SIDECAR_PROFILE_INVALID"))
    if value.get("review_only") is not True:
        findings.add(Finding("HEADLESS_RENDER_REVIEW_REVIEW_POSTURE_INVALID"))
    artifacts = value.get("artifacts")
    expected = (
        ("headless-render.png", "SCREENSHOT", "image/png"),
        ("metrics.json", "METRICS", "application/json"),
    )
    if not isinstance(artifacts, list) or len(artifacts) != len(expected):
        findings.add(Finding("HEADLESS_RENDER_REVIEW_ARTIFACT_LIST_INVALID"))
        return sorted(findings)
    digests: set[str] = set()
    for artifact, (name, role, media_type) in zip(artifacts, expected, strict=True):
        if (
            not isinstance(artifact, dict)
            or set(artifact) != {"name", "role", "media_type", "sha256"}
            or artifact.get("name") != name
            or artifact.get("role") != role
            or artifact.get("media_type") != media_type
            or not _valid_hash(artifact.get("sha256"))
        ):
            findings.add(Finding("HEADLESS_RENDER_REVIEW_ARTIFACT_ENTRY_INVALID"))
            continue
        digest = str(artifact["sha256"])
        if digest in digests:
            findings.add(Finding("HEADLESS_RENDER_REVIEW_ARTIFACT_DIGEST_REUSED"))
        digests.add(digest)
        try:
            actual = _sha256((directory / name).read_bytes())
        except OSError:
            findings.add(Finding("HEADLESS_RENDER_REVIEW_ARTIFACT_UNREADABLE"))
            continue
        if digest != actual:
            findings.add(Finding("HEADLESS_RENDER_REVIEW_ARTIFACT_DIGEST_MISMATCH"))
    return sorted(findings)


def validate_directory(directory: Path) -> list[Finding]:
    try:
        if directory.is_symlink():
            return [Finding("HEADLESS_RENDER_REVIEW_DIRECTORY_SYMLINK_DENIED")]
        if not directory.is_dir():
            return [Finding("HEADLESS_RENDER_REVIEW_DIRECTORY_INVALID")]
        names = tuple(sorted(path.name for path in directory.iterdir()))
    except OSError:
        return [Finding("HEADLESS_RENDER_REVIEW_DIRECTORY_UNREADABLE")]
    if names != tuple(sorted(REQUIRED_FILES)):
        return [Finding("HEADLESS_RENDER_REVIEW_FILE_SET_INVALID")]

    screenshot = directory / "headless-render.png"
    metrics, metric_findings = _load_json(directory / "metrics.json")
    sidecar, sidecar_findings = _load_json(directory / "sidecar.json")
    findings: set[Finding] = set(_validate_png(screenshot))
    findings.update(metric_findings)
    findings.update(sidecar_findings)
    if metrics is not None:
        findings.update(_validate_metrics(metrics))
    if sidecar is not None:
        findings.update(_validate_sidecar(sidecar, directory))
    return sorted(findings)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate one fixture-only headless PMTiles review packet."
    )
    parser.add_argument("directory", type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    findings = validate_directory(args.directory)
    if findings:
        for finding in findings:
            print(f"HEADLESS_RENDER_REVIEW_PACKET_INVALID code={finding.code}")
        return 1
    print(
        "HEADLESS_RENDER_REVIEW_PACKET_VALID artifacts=3 authority=NONE "
        "source=SYNTHETIC_FIXTURE style=NOT_EVALUATED "
        "publication=NOT_EVALUATED"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
