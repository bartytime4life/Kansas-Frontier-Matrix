"""Immutable, bounded snapshot carrier mechanics; no admission or activation.

Artifacts are preserved JSON text, so Python and Worker verification hashes the
same UTF-8 bytes without silently recanonicalizing measurement precision.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
import re
from typing import Callable
from connectors_core.captured_json import canonical_bytes, decode_object, digest_bytes, utc_time
from hashing import compute_spec_hash

MAX_PACKAGE_BYTES = 8 * 1024 * 1024
ARTIFACTS = ("candidate.json", "catalog.json", "evidence.json", "validation.json")
DIGEST = re.compile(r"^sha256:[a-f0-9]{64}$")
REVIEW_REQUIREMENTS = ["source_admission", "rights", "sensitivity", "policy", "independent_review", "release"]
MANIFEST_KEYS = {"profile", "package_id", "candidate_id", "source_id", "start", "end", "created_at", "artifacts", "review_requirements", "rollback_target"}


def _instant_interval(start: str, end: str) -> bool:
    return 0 < (utc_time(end) - utc_time(start)).total_seconds() <= 86400


def _thirty_day_interval(start: str, end: str) -> bool:
    if not all(isinstance(v, str) and len(v) == 10 for v in (start, end)):
        return False
    return (date.fromisoformat(end) - date.fromisoformat(start)).days == 29


@dataclass(frozen=True)
class SnapshotProfile:
    """What a snapshot family fixes. The caller names the expected profile; it is
    never inferred from the package, so a package from one family fails another's checks."""
    profile: str
    source_id: str
    station_ids: frozenset
    evidence_prefix: str
    max_observations: int
    interval_ok: Callable[[str, str], bool]
    # A profile with series splits each station's evidence into one bundle per
    # value of ``series_field`` (the resolver caps a bundle at 128 members).
    series_field: str | None = None
    series_values: tuple = ()  # integers
    series_label: str = ""

    def evidence_keys(self) -> list[tuple]:
        """(station_id, series) for every evidence entry the profile requires; series is None without series."""
        return [(station, value) for station in sorted(self.station_ids) for value in (self.series_values or (None,))]

    def entry_ref(self, station_id: str, series, candidate_id: str) -> str:
        middle = "" if series is None else self.series_label.format(series) + "/"
        return self.evidence_prefix + station_id + "/" + middle + candidate_id.split(":")[1]

    def entry_records(self, observations: list, station_id: str, series) -> list:
        return [r for r in observations if r["station_id"] == station_id
                and (series is None or r[self.series_field] == series)]


WATER = SnapshotProfile("kfm.water-snapshot/v1", "usgs-nwis", frozenset({"USGS-06892518", "USGS-07156900"}),
                        "kfm://water/station/", 4000, _instant_interval)
# GHCN-Daily pilot: four first-order stations, 30 observation days, 3 elements.
WEATHER = SnapshotProfile("kfm.weather-snapshot/v1", "noaa-ghcnd",
                          frozenset({"USW00003928", "USW00013985", "USW00013996", "USW00023065"}),
                          "kfm://weather/station/", 360, _thirty_day_interval)
# USCRN daily soil pilot: two reference stations, 30 days, moisture and temperature
# at five depths; one evidence bundle per station and depth (61 members each).
SOIL = SnapshotProfile("kfm.soil-snapshot/v1", "noaa-uscrn", frozenset({"03067", "53974"}),
                       "kfm://soil/station/", 600, _thirty_day_interval,
                       series_field="depth_cm", series_values=(5, 10, 20, 50, 100), series_label="depth-{}cm")


def prepare_snapshot(candidate: dict, catalog: dict, evidence: dict, validation: dict, *, rollback_target=None,
                     profile: SnapshotProfile = WATER) -> dict:
    if rollback_target is not None and not DIGEST.fullmatch(rollback_target):
        raise ValueError("INVALID_ROLLBACK_TARGET")
    values = dict(zip(ARTIFACTS, (candidate, catalog, evidence, validation)))
    artifacts = {name: canonical_bytes(value).decode("utf-8") for name, value in values.items()}
    manifest = {"profile": profile.profile, "candidate_id": candidate["candidate_id"],
                "source_id": profile.source_id, "start": candidate["start"], "end": candidate["end"],
                "created_at": candidate["retrieved_at"], "artifacts": {name: digest_bytes(text.encode()) for name, text in artifacts.items()},
                "review_requirements": REVIEW_REQUIREMENTS, "rollback_target": rollback_target}
    manifest["package_id"] = compute_spec_hash(manifest)
    snapshot = {"manifest": manifest, "artifacts": artifacts}
    validate_snapshot(canonical_bytes(snapshot), profile=profile)
    return snapshot


def validate_snapshot(raw: bytes, profile: SnapshotProfile = WATER) -> tuple[dict, dict]:
    snapshot = decode_object(raw, limit=MAX_PACKAGE_BYTES)
    if set(snapshot) != {"manifest", "artifacts"}:
        raise ValueError("SNAPSHOT_SHAPE_INVALID")
    manifest, texts = snapshot["manifest"], snapshot["artifacts"]
    if not isinstance(manifest, dict) or set(manifest) != MANIFEST_KEYS:
        raise ValueError("MANIFEST_SHAPE_INVALID")
    if (manifest["profile"] != profile.profile or manifest["source_id"] != profile.source_id
            or manifest["review_requirements"] != REVIEW_REQUIREMENTS
            or manifest["rollback_target"] is not None and not DIGEST.fullmatch(manifest["rollback_target"])):
        raise ValueError("MANIFEST_PROFILE_INVALID")
    if manifest["package_id"] != compute_spec_hash({k: v for k, v in manifest.items() if k != "package_id"}):
        raise ValueError("PACKAGE_DIGEST_MISMATCH")
    try:
        interval_ok = profile.interval_ok(manifest["start"], manifest["end"])
    except (ValueError, TypeError):
        interval_ok = False
    if not interval_ok:
        raise ValueError("SNAPSHOT_INTERVAL_INVALID")
    utc_time(manifest["created_at"])
    if (not isinstance(texts, dict) or set(texts) != set(ARTIFACTS)
            or not isinstance(manifest["artifacts"], dict) or set(manifest["artifacts"]) != set(ARTIFACTS)):
        raise ValueError("ARTIFACT_CLOSURE_INVALID")
    values = {}
    for name in ARTIFACTS:
        if not isinstance(texts[name], str):
            raise ValueError("ARTIFACT_TEXT_REQUIRED")
        payload = texts[name].encode("utf-8")
        if digest_bytes(payload) != manifest["artifacts"][name]:
            raise ValueError("ARTIFACT_DIGEST_MISMATCH")
        values[name] = decode_object(payload, limit=MAX_PACKAGE_BYTES)
    candidate, catalog, evidence, validation = [values[name] for name in ARTIFACTS]
    if any(item.get("candidate_id") != manifest["candidate_id"] for item in (candidate, catalog, evidence, validation)):
        raise ValueError("CANDIDATE_BINDING_MISMATCH")
    if (digest_bytes(canonical_bytes({k: v for k, v in candidate.items() if k != "candidate_id"})) != manifest["candidate_id"]
            or candidate.get("start") != manifest["start"] or candidate.get("end") != manifest["end"]
            or candidate.get("retrieved_at") != manifest["created_at"]):
        raise ValueError("CANDIDATE_IDENTITY_MISMATCH")
    if (validation.get("outcome") != "PASS"
            or validation.get("receipt_digest") != digest_bytes(canonical_bytes({k: v for k, v in validation.items() if k != "receipt_digest"}))):
        raise ValueError("VALIDATION_RECEIPT_INVALID")
    # Authority is read separately from owner-controlled release metadata.
    if candidate.get("release_state") != "UNRELEASED" or catalog.get("authoritative") is not False:
        raise ValueError("CARRIER_CANNOT_SELF_APPROVE")
    if not isinstance(candidate.get("observations"), list) or len(candidate["observations"]) > profile.max_observations:
        raise ValueError("OBSERVATION_LIMIT")
    if not isinstance(evidence.get("entries"), list) or len(evidence["entries"]) != len(profile.evidence_keys()):
        raise ValueError("EVIDENCE_CLOSURE_INVALID")
    if {e["station_id"] for e in evidence["entries"]} != {s["id"] for s in candidate["stations"]}:
        raise ValueError("STATION_EVIDENCE_MISMATCH")
    if profile.series_field is not None:
        keys = [(e["station_id"], e.get("series")) for e in evidence["entries"]]
        if (any(type(series) is not int for _, series in keys) or len(set(keys)) != len(keys)
                or set(keys) != set(profile.evidence_keys())):
            raise ValueError("SERIES_EVIDENCE_MISMATCH")
    stations = candidate["stations"]
    if len(stations) != len(profile.station_ids) or {s["id"] for s in stations} != profile.station_ids:
        raise ValueError("STATION_SCOPE_INVALID")
    for entry in evidence["entries"]:
        station = next(s for s in stations if s["id"] == entry["station_id"])
        series = entry["series"] if profile.series_field is not None else None
        records = profile.entry_records(candidate["observations"], station["id"], series)
        bundle = entry["bundle"]
        ref = entry["evidence_ref"]
        expected_ref = profile.entry_ref(station["id"], series, candidate["candidate_id"])
        if ref != {"ref": expected_ref, "kind": "dataset", "bundle_ref": bundle["bundle_id"]}:
            raise ValueError("DATASET_EVIDENCE_MISMATCH")
        members = [ref] + [{"ref": r["evidence_ref"], "kind": "measurement", "bundle_ref": bundle["bundle_id"]} for r in records]
        if bundle["evidence_refs"] != members or len(members) > 128:
            raise ValueError("MEASUREMENT_EVIDENCE_MISMATCH")
        if bundle["checksums"] != {"candidate": candidate["candidate_id"], "validation": validation["receipt_digest"]}:
            raise ValueError("BUNDLE_CONTENT_BINDING_MISMATCH")
        if bundle["source_records"] != sorted({station["page_digest"], *[r["page_digest"] for r in records]}):
            raise ValueError("SOURCE_RECORD_BINDING_MISMATCH")
        if entry["verification_history"]["subject_ref"] != expected_ref:
            raise ValueError("HISTORY_SUBJECT_MISMATCH")
    return manifest, values
