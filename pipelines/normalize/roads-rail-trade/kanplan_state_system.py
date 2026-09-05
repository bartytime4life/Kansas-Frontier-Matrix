"""One private-fixture source -> geometry -> evidence -> report circle.

The transport snapshot is a HANDOFF profile, not a new normative KFM contract.
Existing EvidenceRef/EvidenceBundle keys and map-selection profile are reused.
No routine here emits a release decision, publishes data, or grants rights.
"""
from __future__ import annotations
import copy
from dataclasses import dataclass, field
import math
import re
from typing import Any
from uuid import UUID
from connectors.kansas.kanplan import (
    Capture, CaptureError, CaptureProfile, Limits, SyntheticTransport, collect,
    content_hash, decode, digest, finite_number, metadata_fingerprint,
    normalized_bytes, require, validate_bbox, validate_capture,
)
from packages.geo.src.geo.esri_polyline import (
    GeometryError, polyline_to_geojson, intersects_bbox, geodesic_length_m,
)

NOTICE = "SYNTHETIC PRIVATE FIXTURE — NOT KDOT DATA — NOT RELEASED — NOT A KANSAS ROAD MAP"
PROFILE = "kfm.transportation.handoff.v1"
SELECTION_PROFILE = "kfm.explorer.map-feature-selection.v1"
FIXTURE_SPEC = {"name": "private-transportation-fixture", "version": "0.2.0"}
# This ASCII string-only object has identical sorted JSON and RFC 8785 bytes.
# It identifies this fixture specification, not the content of a production bundle.
SPEC_HASH = digest(normalized_bytes(FIXTURE_SPEC))
PUBLIC_KEYS = {"route_id", "native_id", "source_id", "dataset_version", "evidence_ref", "source_role", "notice"}
SUSPICIOUS_VALUE = re.compile(r"(?i)(bearer\s|(?:token|api[_-]?key|password|secret)\s*[:=]|sk-[a-z0-9]{16,})")


@dataclass
class Candidate:
    dataset_version: str
    display: dict[str, Any]
    analytical: list[dict[str, Any]]
    bundles: dict[str, dict[str, Any]]
    receipt: dict[str, Any]
    manifest: dict[str, Any]
    raw_responses: list[bytes] = field(default_factory=list, repr=False)


def _business_ids(records: list[dict[str, Any]]) -> None:
    seen: set[str] = set()
    global_ids: set[str] = set()
    for feature in records:
        attrs = feature["attributes"]
        value = attrs.get("Id")
        require(isinstance(value, str) and len(value) <= 100, "BUSINESS_ID_MISSING")
        try:
            identifier = str(UUID(value.strip("{}")))
        except (ValueError, AttributeError):
            raise CaptureError("BUSINESS_ID_INVALID") from None
        require(UUID(identifier).int != 0 and identifier not in seen, "BUSINESS_ID_ZERO_OR_DUPLICATE")
        seen.add(identifier)
        # A GlobalID-looking field is not presumed stable; reject null/zero when present.
        if "GlobalID" in attrs:
            try:
                require(isinstance(attrs["GlobalID"], str), "GLOBAL_ID_INVALID")
                gid = UUID(attrs["GlobalID"].strip("{}"))
                require(gid.int != 0, "GLOBAL_ID_ZERO")
                require(str(gid) not in global_ids, "GLOBAL_ID_DUPLICATE")
                global_ids.add(str(gid))
            except (ValueError, TypeError, AttributeError):
                raise CaptureError("GLOBAL_ID_INVALID") from None


def _public_route(attrs: dict[str, Any]) -> str:
    for key, value in attrs.items():
        if any(t in key.lower() for t in ("useonly", "internal", "restricted", "sensitive")):
            require(value in (False, 0, "N", "No"), "RESTRICTIVE_INDICATOR_REVIEW")
    route = attrs.get("RouteId")
    require(isinstance(route, str) and 0 < len(route) <= 256, "ROUTE_ID_INVALID")
    require(not SUSPICIOUS_VALUE.search(route) and not any(ord(c) < 32 for c in route), "CREDENTIAL_OR_CONTROL_TEXT")
    return route  # UI MUST use textContent. Source text is never HTML or instructions.


def compile_fixture(capture: Capture) -> Candidate:
    validate_capture(capture)
    require(capture.profile.synthetic and capture.profile.source_id.startswith("src:fixture-")
            and capture.receipt.get("synthetic") is True, "REAL_DATA_NOT_ADMITTED")
    require(capture.profile.relative_layer == "Transportation/State_System/FeatureServer/0", "FIRST_SLICE_STATE_ONLY")
    _business_ids(capture.features)
    sr = capture.metadata.get("spatialReference", capture.metadata.get("extent", {}).get("spatialReference"))
    records = []
    total_vertices = 0
    for feature in capture.features:
        attrs = feature["attributes"]
        route = _public_route(attrs)
        for measure in ("FromMeasure", "ToMeasure"):
            value = attrs.get(measure)
            require(value is None or finite_number(value), "LRS_MEASURE_INVALID")
        if attrs.get("FromMeasure") is not None and attrs.get("ToMeasure") is not None:
            require(attrs["FromMeasure"] <= attrs["ToMeasure"], "LRS_MEASURE_ORDER")
        geojson, transform = polyline_to_geojson(feature.get("geometry"), sr,
                              has_z=capture.metadata.get("hasZ", False), has_m=capture.metadata.get("hasM", False))
        total_vertices += transform["native_vertices"]
        require(total_vertices <= 100_000, "DATASET_VERTEX_BUDGET")
        require(intersects_bbox(geojson, capture.profile.bbox), "FEATURE_OUTSIDE_CAPTURE_AOI")
        records.append({"native_id": attrs["OBJECTID"], "business_id": attrs["Id"], "route_id": route,
                        "native_geometry": copy.deepcopy(feature["geometry"]),
                        "native_attributes": copy.deepcopy(attrs), "display_geometry": geojson,
                        "geometry_derived_length_m": geodesic_length_m(geojson),
                        "route_measure_units": "UNKNOWN; not altitude; not assumed miles",
                        "reported_adjusted_traveled_mileage": None, "transform": transform})
    version = "dv:transport:" + content_hash({"source": capture.profile.source_id,
                    "source_content": capture.receipt["normalized_content_sha256"],
                    "records": records, "fixture_spec": FIXTURE_SPEC})
    display_features = []
    bundles: dict[str, dict[str, Any]] = {}
    for record in records:
        native_id = record["native_id"]
        feature_id = "transport:" + version.rsplit(":", 1)[1] + ":" + str(native_id)
        capture_identity = content_hash(capture.receipt)
        evidence_identity = content_hash({"capture": capture_identity, "dataset": version})
        evidence_ref = "ev:transport:" + evidence_identity + ":" + str(native_id)
        bundle_id = "eb:transport:" + evidence_identity + ":" + str(native_id)
        record.update(feature_id=feature_id, evidence_ref=evidence_ref)
        props = {"route_id": record["route_id"], "native_id": str(native_id),
                 "source_id": capture.profile.source_id, "dataset_version": version,
                 "evidence_ref": evidence_ref, "source_role": "fixture_only", "notice": NOTICE}
        display_features.append({"type": "Feature", "id": feature_id,
                                 "geometry": record["display_geometry"], "properties": props})
        bundles[evidence_ref] = {
            "bundle_id": bundle_id,
            "claim_scope": "Private synthetic fixture record only; no Kansas transportation claim.",
            "evidence_refs": [{"ref": evidence_ref, "kind": "record", "bundle_ref": bundle_id}],
            "source_records": [capture.profile.source_id + ":0:" + version.rsplit(":", 1)[1] + ":" + str(native_id)],
            "citations": [f"KFM authored synthetic State System-shaped fixture; OBJECTID {native_id}; {version}; NOT KDOT."],
            "rights": {"license": "Authored synthetic test material; private evaluation only; no KDOT permission implied."},
            "sensitivity": {"level": "public", "reason": "Wholly synthetic, no real person or infrastructure",
                            "applied_at": capture.receipt["retrieval_ended"]},
            "transforms": ["Strict Esri polyline to CRS84; Z/M retained analytically, dropped for display; no simplification."],
            "checksums": {"source_capture_content": "sha256:" + capture.receipt["normalized_content_sha256"],
                          "display_feature": "sha256:" + content_hash(display_features[-1]),
                          "capture_receipt": "sha256:" + content_hash(capture.receipt)},
            "spec_hash": {"value": "sha256:" + SPEC_HASH}}
    display = {"type": "FeatureCollection", "features": display_features}
    manifest = {"profile": PROFILE, "mode": "private_fixture", "notice": NOTICE,
                "dataset_version": version, "source_id": capture.profile.source_id,
                "release_state": "not_released", "release_version": None,
                "public_delivery_allowed": False, "rights_revoked": False, "withdrawn": False,
                "source_role": "fixture_only", "aoi": list(capture.profile.bbox),
                "observation_time": None, "source_edit_time": capture.metadata.get("editingInfo"),
                "retrieval_window": [capture.receipt["retrieval_started"], capture.receipt["retrieval_ended"]],
                "kfm_release_time": None, "supported_years": [],
                "display_sha256": content_hash(display), "bundle_index_sha256": content_hash(bundles),
                "analytical_sha256": content_hash(records), "feature_count": len(records),
                "correction_ref": None, "rollback_ref": None,
                "lineage": {"capture_sha256": content_hash(capture.receipt), "transform_spec_sha256": SPEC_HASH},
                "limitations": [NOTICE, "Count/ID reconciliation is not atomic snapshot isolation.",
                    "Source geometry length is not KDOT adjusted traveled mileage.",
                    "Record lengths are whole selected features, not clipped lengths within the AOI.",
                    "Source publication, observation/count year and historical validity are unknown.",
                    "No county boundaries, complete road coverage, routing, clearance, safety or live traffic claims."]}
    return Candidate(version, display, records, bundles, copy.deepcopy(capture.receipt), manifest, list(capture.raw_responses))


def validate_candidate(candidate: Candidate) -> None:
    m = candidate.manifest
    require(m.get("profile") == PROFILE and m.get("mode") == "private_fixture", "PROFILE_DENIED")
    require(m.get("source_role") == "fixture_only" and m.get("notice") == NOTICE, "FIXTURE_LABEL_REQUIRED")
    require(m.get("release_state") == "not_released" and m.get("public_delivery_allowed") is False,
            "UNAUTHORIZED_RELEASE_ASSERTION")
    require(m.get("dataset_version") == candidate.dataset_version, "VERSION_MISMATCH")
    require(content_hash(candidate.display) == m.get("display_sha256")
            and content_hash(candidate.bundles) == m.get("bundle_index_sha256")
            and content_hash(candidate.analytical) == m.get("analytical_sha256")
            and content_hash(candidate.receipt) == m.get("lineage", {}).get("capture_sha256"), "INTEGRITY_FAILURE")
    trace = candidate.receipt.get("trace", [])
    require(len(candidate.raw_responses) == len(trace), "CAPTURE_RAW_INTEGRITY")
    require(all(isinstance(raw, bytes) and digest(raw) == entry.get("sha256")
                and len(raw) == entry.get("bytes")
                for raw, entry in zip(candidate.raw_responses, trace)), "CAPTURE_RAW_INTEGRITY")
    ids: set[str] = set()
    for f in candidate.display.get("features", []):
        require(set(f["properties"]) == PUBLIC_KEYS, "PUBLIC_PROPERTY_ALLOWLIST")
        require(f["id"] not in ids, "DUPLICATE_DERIVED_ID")
        ids.add(f["id"])
        ref = f["properties"]["evidence_ref"]
        require(ref in candidate.bundles, "EVIDENCE_CLOSURE")
        bundle = candidate.bundles[ref]
        require(bundle.get("evidence_refs") == [{"ref": ref, "kind": "record",
                "bundle_ref": bundle.get("bundle_id")}], "EVIDENCE_CLOSURE")
        require(bundle.get("checksums", {}).get("display_feature") ==
                "sha256:" + content_hash(f), "EVIDENCE_FEATURE_BINDING")
    require(ids == {r["feature_id"] for r in candidate.analytical}
            and len(ids) == m.get("feature_count"), "ANALYTICAL_DISPLAY_IDENTITY")


def permitted_fixture(candidate: Candidate, context: str) -> None:
    validate_candidate(candidate)
    require(context == "private_fixture", "PUBLIC_DELIVERY_DENIED")
    require(candidate.manifest.get("rights_revoked") is False and
            candidate.manifest.get("withdrawn") is False,
            "WITHDRAWN_OR_RIGHTS_REVOKED")


def resolve_fixture(candidate: Candidate, feature_id: str, *, context: str = "public") -> dict:
    try:
        permitted_fixture(candidate, context)
        records = [r for r in candidate.analytical if r["feature_id"] == feature_id]
        if not records:
            return {"outcome": "ABSTAIN", "reason": "FEATURE_UNAVAILABLE", "bundle": None}
        return {"outcome": "ANSWER", "reason": "PRIVATE_FIXTURE_ONLY",
                "bundle": copy.deepcopy(candidate.bundles[records[0]["evidence_ref"]]),
                "dataset_version": candidate.dataset_version, "release_state": "not_released", "notice": NOTICE}
    except (CaptureError, GeometryError) as exc:
        return {"outcome": "DENY", "reason": exc.code, "bundle": None}


def report_fixture(candidate: Candidate, *, bbox: tuple[float, float, float, float],
                   route: str | None = None, year: int | None = None, context: str = "public") -> dict:
    permitted_fixture(candidate, context)
    validate_bbox(bbox)
    coverage = candidate.manifest["aoi"]
    require(coverage[0] <= bbox[0] < bbox[2] <= coverage[2] and coverage[1] <= bbox[1] < bbox[3] <= coverage[3],
            "REPORT_SCOPE_NOT_COVERED")
    require(year is None, "NO_SUPPORTED_COUNT_YEAR")
    require(route is None or isinstance(route, str) and len(route) <= 256, "FILTER_INVALID")
    selected = [r for r in candidate.analytical if (route is None or r["route_id"] == route)
                and intersects_bbox(r["display_geometry"], bbox)]
    body = {"profile": "kfm.transportation.report-handoff.v1", "notice": NOTICE,
            "dataset_version": candidate.dataset_version, "release_version": None,
            "aoi": {"crs": "OGC:CRS84", "bbox": list(bbox), "selection_rule": "line intersects rectangle; no clipping"},
            "filter": {"route_id_equals": route}, "supported_time": None,
            "method": "Deduplicated analytical records, never renderer/tile fragments.",
            "unique_feature_count": len(selected), "count_unit": "source feature records",
            "whole_feature_geometry_length_m": sum(r["geometry_derived_length_m"] for r in selected),
            "length_method": "WGS84 ellipsoidal length of whole intersecting features; not reported traveled mileage",
            "aadt_total": None, "aadt_rule": "No segment AADT sum; AADT is not present in this slice.",
            "feature_ids": sorted(r["feature_id"] for r in selected),
            "evidence_refs": sorted(r["evidence_ref"] for r in selected),
            "citations": [c for r in selected for c in candidate.bundles[r["evidence_ref"]]["citations"]],
            "input_manifest_sha256": content_hash(candidate.manifest), "export_permission": "private synthetic evaluation only",
            "limitations": candidate.manifest["limitations"], "annotations": []}
    return {**body, "report_sha256": content_hash(body)}


def candidate_refresh(previous: Candidate, current: Candidate, *, terms_changed: bool = False,
                      source_withdrawn: bool = False) -> dict:
    """Pure comparison, not a watcher, schedule, publication or activation."""
    validate_candidate(previous)
    validate_candidate(current)
    if source_withdrawn or current.manifest.get("rights_revoked") or current.manifest.get("withdrawn"):
        return {"outcome": "DENY", "reason": "WITHDRAWAL_REVIEW", "publish": False}
    if terms_changed:
        return {"outcome": "DENY", "reason": "TERMS_REVIEW", "publish": False}
    changed = previous.dataset_version != current.dataset_version
    return {"outcome": "ANSWER", "reason": "CANDIDATE_CHANGED" if changed else "NO_MATERIAL_CONTENT_CHANGE",
            "publish": False, "previous": previous.dataset_version, "candidate": current.dataset_version}


def rollback_check(target: Candidate, *, revoked_versions: set[str], context: str = "public") -> dict:
    try:
        permitted_fixture(target, context)
        require(target.dataset_version not in revoked_versions, "ROLLBACK_TARGET_REVOKED")
        return {"outcome": "ANSWER", "reason": "PRIVATE_FIXTURE_RESTORE_ONLY", "publish": False,
                "target": target.dataset_version}
    except (CaptureError, GeometryError) as exc:
        return {"outcome": "DENY", "reason": exc.code, "publish": False}


def aadt_observation(attributes: dict[str, Any]) -> dict:
    """Future-slice validator only. Count year never falls back to edit/retrieval."""
    value, year = attributes.get("AADTCount"), attributes.get("AADTCountYear")
    require(value is None or finite_number(value) and value >= 0, "AADT_VALUE_INVALID")
    require(year is None or type(year) is int and 1900 <= year <= 2100, "AADT_YEAR_INVALID")
    count_date = attributes.get("AADTCountDate")
    require(count_date is None or type(count_date) is int and 0 <= count_date <= 4_133_980_800_000, "AADT_DATE_INVALID")
    return {"value": value, "unit": "vehicles/day (annual average)", "count_year": year,
            "count_date_ms": count_date, "supported_for_year_filter": year is not None,
            "methodology": "NEEDS VERIFICATION", "live_traffic": False, "speed": None}


def build_fixture() -> Candidate:
    """Explicit no-network test run. Never consumed by a production application."""
    from pathlib import Path
    root = Path(__file__).resolve().parents[3]
    fixture = root / "fixtures/synthetic/kanplan"
    metadata = decode((fixture / "state-metadata.synthetic.json").read_bytes(), 100_000)
    input_features = decode((fixture / "state-features.synthetic.json").read_bytes(), 100_000)
    require(input_features.get("synthetic") is True, "FIXTURE_LABEL_REQUIRED")
    profile = CaptureProfile(
        "src:fixture-kanplan-state", "Transportation/State_System/FeatureServer/0",
        metadata_fingerprint(metadata), (0.0, 0.0, 0.05, 0.05),
        tuple(f["name"] for f in metadata["fields"]),
        {"OBJECTID": "esriFieldTypeOID", "Id": "esriFieldTypeString",
         "RouteId": "esriFieldTypeString", "FromMeasure": "esriFieldTypeDouble",
         "ToMeasure": "esriFieldTypeDouble"}, True)
    capture = collect(profile, SyntheticTransport(metadata, input_features["features"]),
                      Limits(chunk_size=1), clock=lambda: "2026-09-05T00:00:00Z",
                      sleep=lambda _: None)
    candidate = compile_fixture(capture)
    validate_candidate(candidate)
    return candidate


def main() -> None:
    """Write only a new caller-selected private fixture directory, never a release."""
    import argparse
    import json
    from pathlib import Path
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument("--fixture-output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[3]
    output = args.fixture_output.resolve()
    require(output != root and root not in output.parents, "OUTPUT_MUST_BE_OUTSIDE_REPOSITORY")
    candidate = build_fixture()  # Validate before making any output directory.
    report = report_fixture(candidate, bbox=(0, 0, .05, .05), context="private_fixture")
    output.mkdir(mode=0o700, parents=True, exist_ok=False)
    files = {"display.geojson": candidate.display, "evidence-bundles.json": candidate.bundles,
             "capture-receipt.json": candidate.receipt, "manifest.json": candidate.manifest,
             "analytical.private.json": candidate.analytical, "report.json": report}
    raw_dir = output / "raw.private"
    raw_dir.mkdir(mode=0o700)
    for index, raw in enumerate(candidate.raw_responses):
        (raw_dir / f"response-{index:03d}.json").write_bytes(raw)
    for name, value in files.items():
        (output / name).write_bytes(normalized_bytes(value) + b"\n")
    print(json.dumps({"outcome": "ANSWER", "mode": "private_fixture",
                      "dataset_version": candidate.dataset_version,
                      "features": len(candidate.analytical), "published": False}))


if __name__ == "__main__":
    main()
