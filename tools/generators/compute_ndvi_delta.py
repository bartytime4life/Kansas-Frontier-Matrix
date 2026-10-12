#!/usr/bin/env python3
"""Compute a deterministic, fixture-safe NDVI delta candidate.

The module consumes caller-supplied reflectance observations only.  It never
opens a network connection, reads raster assets, or writes lifecycle data.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

MAX_INPUT_BYTES = 2 * 1024 * 1024
NDVI_SCALE = 1_000_000
INPUT_KEYS = {"profile", "cell_id", "thresholds", "baseline", "recent"}
THRESHOLD_KEYS = {
    "max_scene_cloud_fraction_bps",
    "min_baseline_clear_observations",
    "min_recent_clear_observations",
    "vegetation_floor_millionths",
    "delta_threshold_millionths",
}
OBSERVATION_KEYS = {
    "observation_id",
    "nir_scaled_int",
    "red_scaled_int",
    "scene_cloud_fraction_bps",
    "pixel_cloud_masked",
}


class InputError(ValueError):
    """Raised when a computation request is malformed or ambiguous."""


def _require_exact_keys(value: Mapping[str, Any], expected: set[str], label: str) -> None:
    if set(value) != expected:
        missing = sorted(expected - set(value))
        extra = sorted(set(value) - expected)
        raise InputError(f"{label} keys differ; missing={missing}, extra={extra}")


def _require_int(value: Any, minimum: int, maximum: int, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise InputError(f"{label} must be an integer")
    if not minimum <= value <= maximum:
        raise InputError(f"{label} must be between {minimum} and {maximum}")
    return value


def _round_ratio_half_away(numerator: int, denominator: int) -> int:
    if denominator <= 0:
        raise InputError("NDVI denominator must be positive")
    sign = -1 if numerator < 0 else 1
    quotient, remainder = divmod(abs(numerator), denominator)
    if remainder * 2 >= denominator:
        quotient += 1
    return sign * quotient


def ndvi_millionths(nir_scaled_int: int, red_scaled_int: int) -> int:
    """Return (NIR-red)/(NIR+red) in signed millionths."""

    nir = _require_int(nir_scaled_int, 0, 10_000, "nir_scaled_int")
    red = _require_int(red_scaled_int, 0, 10_000, "red_scaled_int")
    return _round_ratio_half_away((nir - red) * NDVI_SCALE, nir + red)


def _median_integer_half_away(values: Sequence[int]) -> int:
    if not values:
        raise InputError("median requires at least one value")
    ordered = sorted(values)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[middle]
    return _round_ratio_half_away(ordered[middle - 1] + ordered[middle], 2)


def _validated_observations(value: Any, window: str) -> list[dict[str, Any]]:
    if not isinstance(value, list) or not 1 <= len(value) <= 64:
        raise InputError(f"{window} must contain 1..64 observations")
    observations: list[dict[str, Any]] = []
    identifiers: set[str] = set()
    for index, raw in enumerate(value):
        if not isinstance(raw, dict):
            raise InputError(f"{window}[{index}] must be an object")
        _require_exact_keys(raw, OBSERVATION_KEYS, f"{window}[{index}]")
        identifier = raw["observation_id"]
        if not isinstance(identifier, str) or not 6 <= len(identifier) <= 128:
            raise InputError(f"{window}[{index}].observation_id is invalid")
        if identifier in identifiers:
            raise InputError(f"{window} observation identifiers must be unique")
        identifiers.add(identifier)
        nir = _require_int(raw["nir_scaled_int"], 0, 10_000, "nir_scaled_int")
        red = _require_int(raw["red_scaled_int"], 0, 10_000, "red_scaled_int")
        cloud = _require_int(
            raw["scene_cloud_fraction_bps"], 0, 10_000, "scene_cloud_fraction_bps"
        )
        masked = raw["pixel_cloud_masked"]
        if not isinstance(masked, bool):
            raise InputError("pixel_cloud_masked must be Boolean")
        observations.append(
            {
                "observation_id": identifier,
                "nir_scaled_int": nir,
                "red_scaled_int": red,
                "scene_cloud_fraction_bps": cloud,
                "pixel_cloud_masked": masked,
            }
        )
    return sorted(observations, key=lambda item: item["observation_id"])


def _window_summary(
    observations: Sequence[Mapping[str, Any]], max_scene_cloud_fraction_bps: int
) -> dict[str, Any]:
    accepted: list[tuple[str, int]] = []
    rejected_ids: list[str] = []
    for observation in observations:
        identifier = str(observation["observation_id"])
        if observation["pixel_cloud_masked"] or (
            int(observation["scene_cloud_fraction_bps"]) >= max_scene_cloud_fraction_bps
        ):
            rejected_ids.append(identifier)
            continue
        if int(observation["nir_scaled_int"]) + int(observation["red_scaled_int"]) == 0:
            raise InputError(f"clear observation {identifier} has a zero NDVI denominator")
        accepted.append(
            (
                identifier,
                ndvi_millionths(
                    int(observation["nir_scaled_int"]), int(observation["red_scaled_int"])
                ),
            )
        )
    return {
        "accepted_observation_ids": [identifier for identifier, _ in accepted],
        "rejected_cloud_observation_ids": rejected_ids,
        "clear_observation_count": len(accepted),
        "median_ndvi_millionths": (
            _median_integer_half_away([value for _, value in accepted]) if accepted else None
        ),
    }


def _canonical_digest(value: Mapping[str, Any]) -> str:
    encoded = json.dumps(
        value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def compute_ndvi_delta(request: Mapping[str, Any]) -> dict[str, Any]:
    """Compute one deterministic cell-level NDVI delta candidate."""

    if not isinstance(request, dict):
        raise InputError("request must be an object")
    _require_exact_keys(request, INPUT_KEYS, "request")
    if request["profile"] != "kfm.ndvi-delta.synthetic.v1":
        raise InputError("profile is not supported")
    cell_id = request["cell_id"]
    if not isinstance(cell_id, str) or not 8 <= len(cell_id) <= 160:
        raise InputError("cell_id is invalid")

    thresholds = request["thresholds"]
    if not isinstance(thresholds, dict):
        raise InputError("thresholds must be an object")
    _require_exact_keys(thresholds, THRESHOLD_KEYS, "thresholds")
    checked_thresholds = {
        "max_scene_cloud_fraction_bps": _require_int(
            thresholds["max_scene_cloud_fraction_bps"],
            1,
            10_000,
            "max_scene_cloud_fraction_bps",
        ),
        "min_baseline_clear_observations": _require_int(
            thresholds["min_baseline_clear_observations"],
            1,
            64,
            "min_baseline_clear_observations",
        ),
        "min_recent_clear_observations": _require_int(
            thresholds["min_recent_clear_observations"],
            1,
            64,
            "min_recent_clear_observations",
        ),
        "vegetation_floor_millionths": _require_int(
            thresholds["vegetation_floor_millionths"],
            -NDVI_SCALE,
            NDVI_SCALE,
            "vegetation_floor_millionths",
        ),
        "delta_threshold_millionths": _require_int(
            thresholds["delta_threshold_millionths"],
            1,
            2 * NDVI_SCALE,
            "delta_threshold_millionths",
        ),
    }
    baseline = _validated_observations(request["baseline"], "baseline")
    recent = _validated_observations(request["recent"], "recent")
    if {item["observation_id"] for item in baseline} & {
        item["observation_id"] for item in recent
    }:
        raise InputError("baseline and recent observation identifiers must be disjoint")

    baseline_summary = _window_summary(
        baseline, checked_thresholds["max_scene_cloud_fraction_bps"]
    )
    recent_summary = _window_summary(recent, checked_thresholds["max_scene_cloud_fraction_bps"])
    baseline_ready = (
        baseline_summary["clear_observation_count"]
        >= checked_thresholds["min_baseline_clear_observations"]
    )
    recent_ready = (
        recent_summary["clear_observation_count"]
        >= checked_thresholds["min_recent_clear_observations"]
    )

    delta: int | None = None
    reasons: list[str] = []
    if not baseline_ready:
        reasons.append("BASELINE_CLEAR_OBSERVATIONS_INSUFFICIENT")
    if not recent_ready:
        reasons.append("RECENT_CLEAR_OBSERVATIONS_INSUFFICIENT")
    if reasons:
        classification = "INSUFFICIENT_CLEAR_OBSERVATIONS"
    else:
        baseline_median = int(baseline_summary["median_ndvi_millionths"])
        recent_median = int(recent_summary["median_ndvi_millionths"])
        delta = recent_median - baseline_median
        if baseline_median < checked_thresholds["vegetation_floor_millionths"]:
            classification = "SUPPRESSED_NON_VEGETATED"
            reasons.append("BASELINE_BELOW_VEGETATION_FLOOR")
        elif delta >= checked_thresholds["delta_threshold_millionths"]:
            classification = "GAIN_CANDIDATE"
        elif delta <= -checked_thresholds["delta_threshold_millionths"]:
            classification = "LOSS_CANDIDATE"
        else:
            classification = "STABLE"

    canonical_request = {
        "profile": request["profile"],
        "cell_id": cell_id,
        "thresholds": checked_thresholds,
        "baseline": baseline,
        "recent": recent,
    }
    result: dict[str, Any] = {
        "object_type": "NdviDeltaComputation",
        "schema_version": "1.0.0",
        "profile": "kfm.ndvi-delta.synthetic.v1",
        "cell_id": cell_id,
        "input_digest": _canonical_digest(canonical_request),
        "thresholds": checked_thresholds,
        "baseline": baseline_summary,
        "recent": recent_summary,
        "delta_ndvi_millionths": delta,
        "classification": classification,
        "reasons": sorted(reasons),
        "governance": {
            "execution_mode": "FIXTURE_OR_CAPTURED_INPUT_ONLY",
            "network_attempted": False,
            "raster_opened": False,
            "source_activated": False,
            "raw_admitted": False,
            "evidence_resolved": False,
            "promotion_authorized": False,
            "release_authorized": False,
            "publication_authorized": False,
            "public_use_authorized": False,
        },
    }
    result["result_digest"] = _canonical_digest(result)
    return result


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise InputError(f"duplicate JSON member: {key}")
        result[key] = value
    return result


def _reject_nonfinite(value: str) -> None:
    raise InputError(f"non-finite JSON number: {value}")


def load_request(path: Path) -> dict[str, Any]:
    if path.is_symlink() or not path.is_file():
        raise InputError("input must be a regular non-symlink file")
    if path.stat().st_size > MAX_INPUT_BYTES:
        raise InputError("input exceeds the 2 MiB limit")
    try:
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_nonfinite,
        )
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise InputError(f"input is not readable strict UTF-8 JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise InputError("input root must be an object")
    return value


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        result = compute_ndvi_delta(load_request(args.input))
    except InputError as exc:
        parser.exit(2, f"error: {exc}\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
