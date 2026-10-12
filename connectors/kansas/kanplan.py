"""Bounded, read-only KanPlan capture mechanics; no network on import.

Repository-adapted private-fixture implementation, not an admitted source.
Only SyntheticTransport is accepted. The HTTP placeholder always denies; there
is no switch, URL proxy, network side effect, or publication operation.
See docs/runbooks/kdot-kanplan-fixture-integration.md for the placement note.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
import hashlib
import json
import math
import re
import time
from typing import Any, Callable, Mapping, Protocol
from types import MappingProxyType

BASE = "https://kanplan.ksdot.gov/arcgis_web_adaptor/rest/services/"
# This is an acquisition allowlist, not a source-admission or rights register.
KNOWN_LAYERS = frozenset({
    "Transportation/State_System/FeatureServer/0",
    "Transportation/Functional_Classification/FeatureServer/1",
    "Transportation/Functional_Classification/FeatureServer/2",
    "Transportation/Functional_Classification/FeatureServer/3",
    "Transportation/Railroads/FeatureServer/0",
    "Transportation/Railroads/FeatureServer/1",
    "Transportation/AADT_Flow_Map/FeatureServer/0",
})
NORMALIZATION_PROFILE = "kfm-kanplan-fixture-json-v2"  # NOT RFC 8785 / KFM spec_hash.
MAX_SAFE_INT = 2**53 - 1


class CaptureError(ValueError):
    """Only finite local codes are exposed; upstream text/URLs are never echoed."""
    def __init__(self, code: str):
        super().__init__(code)
        self.code = code


def require(condition: bool, code: str) -> None:
    if not condition:
        raise CaptureError(code)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def normalized_bytes(value: Any) -> bytes:
    """Deterministic Python JSON profile, explicitly distinct from RFC 8785."""
    try:
        return json.dumps(value, sort_keys=True, separators=(",", ":"),
                          ensure_ascii=False, allow_nan=False).encode("utf-8")
    except (TypeError, ValueError, OverflowError, RecursionError) as exc:
        raise CaptureError("NON_JSON_OR_NONFINITE") from exc


def content_hash(value: Any) -> str:
    return digest(normalized_bytes(value))


def _pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        require(key not in result, "DUPLICATE_JSON_KEY")
        result[key] = value
    return result


def decode(data: bytes, maximum: int) -> dict[str, Any]:
    require(isinstance(data, bytes) and len(data) <= maximum, "RESPONSE_BYTE_BUDGET")
    try:
        value = json.loads(data.decode("utf-8"), object_pairs_hook=_pairs,
                           parse_constant=lambda _: (_ for _ in ()).throw(CaptureError("NONFINITE_JSON")))
    except CaptureError:
        raise
    except (UnicodeError, ValueError, RecursionError) as exc:
        raise CaptureError("INVALID_JSON") from exc
    require(isinstance(value, dict), "JSON_OBJECT_REQUIRED")
    require("error" not in value, "UPSTREAM_ERROR")
    # Also catches exponent overflow (1e999), which parse_constant does not catch.
    normalized_bytes(value)
    return value


def positive_int(value: Any, maximum: int = MAX_SAFE_INT) -> bool:
    return type(value) is int and 0 < value <= maximum


def finite_number(value: Any) -> bool:
    if type(value) not in (int, float):
        return False
    try:
        return math.isfinite(value)
    except OverflowError:
        return False


def validate_bbox(bbox: tuple[float, float, float, float]) -> None:
    require(isinstance(bbox, (tuple, list)) and len(bbox) == 4, "INVALID_BBOX")
    require(all(finite_number(v) for v in bbox), "INVALID_BBOX")
    w, s, e, n = bbox
    require(-180 <= w < e <= 180 and -85 <= s < n <= 85, "INVALID_BBOX")
    require((e - w) * (n - s) <= 25, "AOI_BUDGET")


@dataclass(frozen=True)
class Limits:
    max_requests: int = 40
    max_response_bytes: int = 2_000_000
    max_total_bytes: int = 12_000_000
    max_features: int = 2_000
    chunk_size: int = 200
    timeout_seconds: float = 10.0
    attempts: int = 3
    min_interval_seconds: float = 0.25

    def __post_init__(self) -> None:
        for name, ceiling in (("max_requests", 100), ("max_response_bytes", 4_000_000),
                              ("max_total_bytes", 32_000_000), ("max_features", 5_000),
                              ("chunk_size", 1_000), ("attempts", 3)):
            require(positive_int(getattr(self, name), ceiling), "INVALID_LIMITS")
        require(finite_number(self.timeout_seconds)
                and 0 < self.timeout_seconds <= 30, "INVALID_LIMITS")
        require(finite_number(self.min_interval_seconds)
                and 0 <= self.min_interval_seconds <= 10, "INVALID_LIMITS")


@dataclass(frozen=True)
class CaptureProfile:
    source_id: str
    relative_layer: str
    expected_metadata_hash: str
    bbox: tuple[float, float, float, float]
    acquired_fields: tuple[str, ...]
    required_types: Mapping[str, str]
    synthetic: bool = False

    def __post_init__(self) -> None:
        require(type(self.synthetic) is bool, "FIXTURE_MODE_TYPE")
        require(isinstance(self.relative_layer, str) and self.relative_layer in KNOWN_LAYERS,
                "LAYER_NOT_ALLOWLISTED")
        require(isinstance(self.source_id, str) and
                bool(re.fullmatch(r"src:[a-z0-9][a-z0-9:._-]{0,100}", self.source_id)), "SOURCE_ID")
        require(isinstance(self.expected_metadata_hash, str) and
                bool(re.fullmatch(r"[a-f0-9]{64}", self.expected_metadata_hash)), "METADATA_PIN_REQUIRED")
        validate_bbox(self.bbox)
        require(isinstance(self.acquired_fields, tuple) and
                all(isinstance(x, str) for x in self.acquired_fields), "FIELD_NAME")
        require(isinstance(self.required_types, Mapping), "FIELD_TYPE_DRIFT")
        require(0 < len(self.acquired_fields) <= 48 and len(set(self.acquired_fields)) == len(self.acquired_fields),
                "FIELD_BUDGET")
        require(all(re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{0,63}", x) for x in self.acquired_fields), "FIELD_NAME")
        require(set(self.required_types) <= set(self.acquired_fields), "REQUIRED_FIELD_NOT_ACQUIRED")
        require(not self.synthetic or self.source_id.startswith("src:fixture-"), "FIXTURE_ID_REQUIRED")
        object.__setattr__(self, "bbox", tuple(self.bbox))
        object.__setattr__(self, "required_types", MappingProxyType(dict(self.required_types)))

    @property
    def url(self) -> str:
        return BASE + self.relative_layer


class ByteTransport(Protocol):
    def __call__(self, url: str, params: Mapping[str, str], *, timeout: float, maximum: int) -> bytes: ...


class DormantReadOnlyHTTP:
    """No live implementation. Admission-bound acquisition needs separate review."""
    def __call__(self, url: str, params: Mapping[str, str], *, timeout: float, maximum: int) -> bytes:
        raise CaptureError("LIVE_SOURCE_NOT_ACTIVATED")


def metadata_fingerprint(metadata: Mapping[str, Any]) -> str:
    """Pin entire structural metadata projection; exclude cosmetic renderers.

    Editing information is compared separately before/after acquisition.
    Unknown metadata keys remain in preserved source bytes; no source raw copy is
    emitted by the preview. A changed known structural field requires review.
    """
    keys = ("id", "type", "geometryType", "objectIdField", "fields", "extent", "spatialReference",
            "hasZ", "hasM", "maxRecordCount", "capabilities", "advancedQueryCapabilities",
            "supportsCoordinatesQuantization", "isDataVersioned", "copyrightText",
            "description", "serviceItemId")
    return content_hash({k: metadata[k] for k in keys if k in metadata})


def validate_metadata(metadata: Mapping[str, Any], profile: CaptureProfile) -> str:
    require(type(metadata.get("id")) is int and
            metadata["id"] == int(profile.relative_layer.rsplit("/", 1)[1]), "LAYER_ID_DRIFT")
    require(metadata.get("type") == "Feature Layer" and metadata.get("geometryType") == "esriGeometryPolyline",
            "LAYER_TYPE_DRIFT")
    require("Query" in str(metadata.get("capabilities", "")).split(","), "QUERY_UNAVAILABLE")
    require(positive_int(metadata.get("maxRecordCount")), "RECORD_LIMIT_MISSING")
    fields = metadata.get("fields")
    require(isinstance(fields, list) and len(fields) <= 500, "METADATA_FIELDS")
    require(all(isinstance(f, dict) and isinstance(f.get("name"), str) for f in fields), "METADATA_FIELDS")
    require(len({f["name"] for f in fields}) == len(fields), "DUPLICATE_METADATA_FIELD")
    actual = {f["name"]: f.get("type") for f in fields}
    require(all(actual.get(k) == v for k, v in profile.required_types.items()), "FIELD_TYPE_DRIFT")
    require(set(profile.acquired_fields) <= set(actual), "MISSING_ACQUIRED_FIELD")
    # Restrictive flags cannot be silently omitted from a capture/public projection.
    flags = [k for k in actual if any(t in k.lower() for t in ("useonly", "internal", "restricted", "sensitive"))]
    require(set(flags) <= set(profile.acquired_fields), "RESTRICTIVE_FIELD_NOT_ACQUIRED")
    require(metadata_fingerprint(metadata) == profile.expected_metadata_hash, "SCHEMA_DRIFT")
    oid = metadata.get("objectIdField")
    require(isinstance(oid, str) and actual.get(oid) == "esriFieldTypeOID" and oid in profile.acquired_fields,
            "OID_FIELD")
    return oid


@dataclass
class Capture:
    profile: CaptureProfile
    metadata: dict[str, Any]
    features: list[dict[str, Any]]
    receipt: dict[str, Any]
    raw_responses: list[bytes] = field(repr=False)


def collect(profile: CaptureProfile, transport: ByteTransport, limits: Limits = Limits(), *,
            clock: Callable[[], str] = utc_now, sleep: Callable[[float], None] = time.sleep) -> Capture:
    """Reconcile count+IDs, bounded ID chunks, then count+IDs+metadata again.

    No result is called an atomic snapshot. Unstable/changing collections fail.
    An unchanged ID set cannot prove unchanged attributes on an upstream service
    lacking snapshot isolation; that limitation is carried in the receipt.
    """
    require(profile.synthetic and isinstance(transport, SyntheticTransport), "ADMISSION_BINDING_REQUIRED")
    started = clock()
    raw: list[bytes] = []
    trace: list[dict[str, Any]] = []
    requests = 0
    total_bytes = 0

    def get(operation: str, params: Mapping[str, str]) -> dict[str, Any]:
        nonlocal requests, total_bytes
        url = profile.url + ("/query" if operation != "metadata" else "")
        for attempt in range(limits.attempts):
            require(requests < limits.max_requests, "REQUEST_BUDGET")
            requests += 1
            if requests > 1:
                sleep(limits.min_interval_seconds)
            try:
                remaining = min(limits.max_response_bytes, limits.max_total_bytes - total_bytes)
                require(remaining > 0, "TOTAL_BYTE_BUDGET")
                body = transport(url, dict(params), timeout=limits.timeout_seconds, maximum=remaining)
                require(isinstance(body, bytes), "BYTE_TRANSPORT_REQUIRED")
                total_bytes += len(body)
                require(total_bytes <= limits.max_total_bytes, "TOTAL_BYTE_BUDGET")
                value = decode(body, limits.max_response_bytes)
                require(value.get("exceededTransferLimit") is None or
                        value["exceededTransferLimit"] is False, "TRANSFER_LIMIT")
                raw.append(body)
                trace.append({"operation": operation, "parameters": dict(params), "sha256": digest(body),
                              "bytes": len(body), "attempt": attempt + 1})
                return value
            except CaptureError as exc:
                if exc.code != "HTTP_TRANSIENT" or attempt + 1 >= limits.attempts:
                    raise
                sleep(min(2 ** attempt, 4))
        raise CaptureError("RETRY_BUDGET")

    metadata = get("metadata", {"f": "json"})
    oid = validate_metadata(metadata, profile)
    w, s, e, n = profile.bbox
    scope = {"f": "json", "where": "1=1", "geometry": f"{w},{s},{e},{n}", "geometryType": "esriGeometryEnvelope",
             "inSR": "4326", "spatialRel": "esriSpatialRelIntersects"}

    def count_and_ids() -> list[int]:
        count = get("count", {**scope, "returnCountOnly": "true"}).get("count")
        require(type(count) is int and 0 <= count <= limits.max_features, "FEATURE_BUDGET_OR_COUNT")
        result = get("ids", {**scope, "returnIdsOnly": "true"})
        ids = result.get("objectIds")
        require(result.get("objectIdFieldName") == oid, "OID_FIELD_DRIFT")
        require(isinstance(ids, list) and len(ids) == count, "COUNT_IDS_MISMATCH")
        require(all(positive_int(i) for i in ids), "INVALID_OBJECT_ID")
        require(len(set(ids)) == len(ids), "DUPLICATE_OBJECT_ID")
        return sorted(ids)

    ids = count_and_ids()
    features: list[dict[str, Any]] = []
    chunk = min(limits.chunk_size, metadata["maxRecordCount"])
    for start in range(0, len(ids), chunk):
        wanted = ids[start:start + chunk]
        page = get("features", {**scope, "objectIds": ",".join(map(str, wanted)),
                    "outFields": ",".join(profile.acquired_fields), "returnGeometry": "true",
                    "returnZ": "true", "returnM": "true", "returnTrueCurves": "true"})
        page_features = page.get("features")
        require(isinstance(page_features, list) and len(page_features) == len(wanted), "TRUNCATED_PAGE")
        require(page.get("geometryType") == metadata["geometryType"], "PAGE_GEOMETRY_TYPE")
        native_sr = metadata.get("spatialReference", metadata.get("extent", {}).get("spatialReference"))
        require(page.get("spatialReference") == native_sr, "PAGE_CRS_DRIFT")
        require(page.get("hasZ", False) == metadata.get("hasZ", False)
                and page.get("hasM", False) == metadata.get("hasM", False), "PAGE_DIMENSION_DRIFT")
        found: list[int] = []
        for feature in page_features:
            require(isinstance(feature, dict) and isinstance(feature.get("attributes"), dict), "FEATURE_SHAPE")
            require(set(feature["attributes"]) == set(profile.acquired_fields), "ATTRIBUTE_FIELDS_DRIFT")
            native_id = feature["attributes"].get(oid)
            require(positive_int(native_id), "INVALID_OBJECT_ID")
            found.append(native_id)
        require(sorted(found) == wanted, "CHUNK_ID_MISMATCH")
        features.extend(page_features)
    require(count_and_ids() == ids, "CAPTURE_CHANGED_IDS")
    after = get("metadata", {"f": "json"})
    validate_metadata(after, profile)
    require(metadata.get("editingInfo") == after.get("editingInfo"), "CAPTURE_CHANGED_EDIT_METADATA")
    features.sort(key=lambda f: f["attributes"][oid])
    normalized_hash = content_hash({"source_id": profile.source_id, "layer": profile.relative_layer,
                                   "metadata_hash": profile.expected_metadata_hash, "aoi": profile.bbox,
                                   "features": features})
    ended = clock()
    try:
        first = datetime.fromisoformat(started.replace("Z", "+00:00"))
        last = datetime.fromisoformat(ended.replace("Z", "+00:00"))
        require(first.utcoffset() is not None and last.utcoffset() is not None,
                "RETRIEVAL_TIME_ZONE")
        require(last >= first, "RETRIEVAL_TIME_ORDER")
    except (TypeError, AttributeError, ValueError) as exc:
        if isinstance(exc, CaptureError):
            raise
        raise CaptureError("RETRIEVAL_TIME_INVALID") from None
    receipt = {"outcome": "ANSWER", "synthetic": True, "source_id": profile.source_id,
               "scope": {"bbox_4326": list(profile.bbox), "relation": "intersects", "clipped": False},
               "retrieval_started": started, "retrieval_ended": ended, "expected_count": len(ids),
               "returned_count": len(features), "requests": requests, "bytes": total_bytes,
               "trace": trace, "normalization_profile": NORMALIZATION_PROFILE,
               "normalized_content_sha256": normalized_hash, "atomic_snapshot": False,
               "consistency": "count-and-id-set-reconciled; metadata compared; not snapshot isolation",
               "release_state": "not_released", "public_release_allowed": False}
    return Capture(profile, metadata, features, receipt, raw)


class SyntheticTransport:
    """No-network byte source for generated fixtures. Not an upstream emulator claim."""
    def __init__(self, metadata: dict[str, Any], features: list[dict[str, Any]]):
        self.metadata = json.loads(json.dumps(metadata))
        self.features = json.loads(json.dumps(features))
        self.calls: list[dict[str, Any]] = []

    def __call__(self, url: str, params: Mapping[str, str], *, timeout: float, maximum: int) -> bytes:
        self.calls.append({"url": url, "params": dict(params), "timeout": timeout, "maximum": maximum})
        oid = self.metadata["objectIdField"]
        if not url.endswith("/query"):
            value = self.metadata
        elif params.get("returnCountOnly") == "true":
            value = {"count": len(self.features)}
        elif params.get("returnIdsOnly") == "true":
            value = {"objectIdFieldName": oid, "objectIds": [f["attributes"][oid] for f in self.features]}
        else:
            ids = {int(x) for x in params["objectIds"].split(",")}
            value = {"geometryType": self.metadata["geometryType"],
                     "spatialReference": self.metadata["extent"]["spatialReference"],
                     "hasZ": self.metadata.get("hasZ", False), "hasM": self.metadata.get("hasM", False),
                     "features": [f for f in self.features if f["attributes"][oid] in ids]}
        data = normalized_bytes(value)
        require(len(data) <= maximum, "RESPONSE_BYTE_BUDGET")
        return data


def validate_capture(capture: Capture) -> None:
    """Rebind mutable candidate objects to their preserved synthetic response bytes.

    This detects accidental edits, not malicious rewriting of every digest. Hashes
    are not signatures, admission, rights, approval, or an atomic-snapshot claim.
    """
    require(isinstance(capture, Capture), "CAPTURE_SHAPE")
    profile, receipt = capture.profile, capture.receipt
    require(profile.synthetic is True and receipt.get("synthetic") is True,
            "REAL_DATA_NOT_ADMITTED")
    require(receipt.get("source_id") == profile.source_id and
            receipt.get("normalization_profile") == NORMALIZATION_PROFILE and
            receipt.get("release_state") == "not_released" and
            receipt.get("public_release_allowed") is False and
            receipt.get("atomic_snapshot") is False, "CAPTURE_POSTURE_DRIFT")
    trace = receipt.get("trace")
    require(isinstance(trace, list) and len(trace) == len(capture.raw_responses)
            and 6 <= len(trace) <= 100, "CAPTURE_TRACE_DRIFT")
    total = 0
    pages = []
    metadata = []
    for entry, raw in zip(trace, capture.raw_responses):
        require(isinstance(entry, dict) and isinstance(raw, bytes), "CAPTURE_TRACE_DRIFT")
        require(len(raw) == entry.get("bytes") and digest(raw) == entry.get("sha256"),
                "CAPTURE_RAW_INTEGRITY")
        total += len(raw)
        require(total <= 32_000_000, "CAPTURE_BYTE_BUDGET")
        value = decode(raw, 4_000_000)
        if entry.get("operation") == "features":
            require(isinstance(value.get("features"), list), "CAPTURE_TRACE_DRIFT")
            pages.extend(value["features"])
        elif entry.get("operation") == "metadata":
            metadata.append(value)
    require(total == receipt.get("bytes") and
            len(trace) <= receipt.get("requests", 0) <= 100, "CAPTURE_TRACE_DRIFT")
    require(len(metadata) == 2 and metadata[0] == capture.metadata, "CAPTURE_METADATA_DRIFT")
    oid = validate_metadata(metadata[0], profile)
    validate_metadata(metadata[1], profile)
    require(metadata[0].get("editingInfo") == metadata[1].get("editingInfo"),
            "CAPTURE_CHANGED_EDIT_METADATA")
    try:
        pages.sort(key=lambda f: f["attributes"][oid])
    except (KeyError, TypeError):
        raise CaptureError("CAPTURE_FEATURE_DRIFT") from None
    require(pages == capture.features and len(pages) <= 5_000, "CAPTURE_FEATURE_DRIFT")
    require(receipt.get("expected_count") == len(pages) == receipt.get("returned_count"),
            "CAPTURE_COUNT_DRIFT")
    require(receipt.get("scope") == {"bbox_4326": list(profile.bbox),
            "relation": "intersects", "clipped": False}, "CAPTURE_SCOPE_DRIFT")
    expected = content_hash({"source_id": profile.source_id, "layer": profile.relative_layer,
                            "metadata_hash": profile.expected_metadata_hash,
                            "aoi": profile.bbox, "features": pages})
    require(expected == receipt.get("normalized_content_sha256"), "CAPTURE_CONTENT_DRIFT")
