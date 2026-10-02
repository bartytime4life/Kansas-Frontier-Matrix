#!/usr/bin/env python3
"""Build a deterministic, fixture-first WBD HUC12 ingest candidate.

The executable consumes an already captured source package. It performs no
network access and writes no KFM lifecycle state. Its only output is one
machine-readable candidate envelope on stdout or at an explicitly supplied
output path.
"""
from __future__ import annotations

import argparse
import bisect
import copy
import errno
import hashlib
import importlib.util
import json
import math
import os
import stat
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence
from urllib.parse import parse_qsl, urlsplit

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[4]
SOURCE_SCHEMA = (
    REPO_ROOT
    / "schemas/contracts/v1/domains/hydrology/wbd_huc12_source_package.schema.json"
)
OUTPUT_SCHEMA = (
    REPO_ROOT
    / "schemas/contracts/v1/domains/hydrology/wbd_huc12_ingest_candidate.schema.json"
)
MATERIAL_VALIDATOR_PATH = (
    REPO_ROOT
    / "tools/validators/domains/hydrology/wbd_huc12_material_change/"
    "validate_wbd_huc12_material_change.py"
)
MAX_INPUT_BYTES = 8 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100
HASH_PREFIX = "sha256:"
SOURCE_DESCRIPTOR_REF = "data/registry/hydrology/sources/wbd_huc12.yaml"
ALLOWED_TARGETS = [
    "data/quarantine/hydrology/wbd_huc12/",
    "data/raw/hydrology/wbd_huc12/",
]
QUERY_ORIGIN = "hydro.nationalmap.gov"
QUERY_PATH = "/arcgis/rest/services/wbd/MapServer/6/query"


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class BuildResult:
    output: dict[str, Any] | None
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.output is not None and not self.findings


def _load_material_validator() -> Any:
    spec = importlib.util.spec_from_file_location(
        "kfm_wbd_huc12_material_change_runtime", MATERIAL_VALIDATOR_PATH
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("material-change validator unavailable")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


MATERIAL = _load_material_validator()


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_nonfinite(value: str) -> None:
    raise NonFiniteNumberError(value)


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError(value)
    return parsed


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(item).replace("~", "~0").replace("/", "~1") for item in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def read_json_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink() or any(parent.is_symlink() for parent in path.parents):
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        descriptor = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
        with os.fdopen(descriptor, "rb") as stream:
            before = os.fstat(stream.fileno())
            if not stat.S_ISREG(before.st_mode):
                return None, [Finding("INPUT_NOT_FILE", "/")]
            if before.st_size > MAX_INPUT_BYTES:
                return None, [Finding("INPUT_TOO_LARGE", "/")]
            payload = stream.read(MAX_INPUT_BYTES + 1)
            if len(payload) > MAX_INPUT_BYTES:
                return None, [Finding("INPUT_TOO_LARGE", "/")]
            after = os.fstat(stream.fileno())
            if (before.st_size, before.st_mtime_ns, before.st_ctime_ns) != (
                after.st_size, after.st_mtime_ns, after.st_ctime_ns
            ):
                return None, [Finding("INPUT_CHANGED_DURING_READ", "/")]
        value = json.loads(
            payload.decode("utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_nonfinite,
            parse_float=_finite_float,
        )
    except UnicodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except (ValueError, RecursionError):
        return None, [Finding("JSON_INVALID", "/")]
    except (FileNotFoundError, NotADirectoryError):
        return None, [Finding("INPUT_NOT_FILE", "/")]
    except OSError as error:
        if error.errno == errno.ELOOP:
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        return None, [Finding("INPUT_UNREADABLE", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def canonical_hash(value: Mapping[str, Any], *, exclude: str = "spec_hash") -> str:
    body = copy.deepcopy(dict(value))
    body.pop(exclude, None)
    encoded = json.dumps(
        body,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return HASH_PREFIX + hashlib.sha256(encoded).hexdigest()


def canonical_body_hash(value: object) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return HASH_PREFIX + hashlib.sha256(encoded).hexdigest()


def _schema_findings(
    value: Mapping[str, Any], schema_path: Path, *, prefix: str
) -> list[Finding]:
    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(
            schema,
            format_checker=FormatChecker(),
        )
        ordered: list[tuple[str, str]] = []
        total = 0
        for error in validator.iter_errors(value):
            total += 1
            bisect.insort(ordered, (_pointer(error.absolute_path), str(error.validator)))
            if len(ordered) > MAX_SCHEMA_FINDINGS:
                ordered.pop()
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding(f"{prefix}_SCHEMA_UNAVAILABLE", "/")]
    findings = [
        Finding(f"{prefix}_SCHEMA_INVALID", path)
        for path, _validator in ordered
    ]
    if total > MAX_SCHEMA_FINDINGS:
        findings.append(Finding(f"{prefix}_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _property(properties: Mapping[str, Any], *names: str) -> Any:
    for name in names:
        if name in properties:
            return properties[name]
    return None


def _request_scope_findings(package: Mapping[str, Any]) -> list[Finding]:
    request = package["request"]
    expected_where = f"huc12='{package['huc12']}'"
    findings: list[Finding] = []
    if request["where_clause"] != expected_where:
        findings.append(Finding("REQUEST_WHERE_MISMATCH", "/request/where_clause"))
    try:
        url = urlsplit(request["url"])
        query = parse_qsl(
            url.query, keep_blank_values=True, strict_parsing=True, max_num_fields=3
        )
    except ValueError:
        query = []
        url = None
    if (
        url is None
        or url.scheme != "https"
        or url.netloc != QUERY_ORIGIN
        or url.path != QUERY_PATH
        or url.geturl() != request["url"]
        or url.fragment
        or sorted(query) != sorted([
            ("where", expected_where),
            ("outFields", ",".join(request["out_fields"])),
            ("f", "geojson"),
        ])
    ):
        findings.append(Finding("REQUEST_URL_SCOPE_INVALID", "/request/url"))
    return findings


def _normalize_feature(
    raw: Mapping[str, Any], expected_huc12: str, request: Mapping[str, Any]
) -> tuple[dict[str, Any] | None, list[Finding]]:
    findings: list[Finding] = []
    properties = raw.get("properties")
    geometry = raw.get("geometry")
    if not isinstance(properties, dict):
        return None, [Finding("FEATURE_PROPERTIES_INVALID", "/response/feature_collection/features")]
    if not isinstance(geometry, dict):
        return None, [Finding("FEATURE_GEOMETRY_INVALID", "/response/feature_collection/features")]

    huc12 = _property(properties, "huc12", "HUC12")
    areasqkm = _property(properties, "areasqkm", "AREASQKM")
    if huc12 != expected_huc12:
        findings.append(Finding("FEATURE_HUC12_MISMATCH", "/response/feature_collection/features"))
    if isinstance(areasqkm, bool) or not isinstance(areasqkm, (int, float)):
        findings.append(Finding("FEATURE_AREA_INVALID", "/response/feature_collection/features"))
    elif not math.isfinite(float(areasqkm)) or float(areasqkm) < 0:
        findings.append(Finding("FEATURE_AREA_INVALID", "/response/feature_collection/features"))
    if findings:
        return None, findings

    feature = {
        "huc12": huc12,
        "areasqkm": float(areasqkm),
        "geometry": copy.deepcopy(geometry),
        "source_metadata": {
            "load_date": _property(properties, "load_date", "LoadDate"),
            "last_edit_date": _property(
                properties, "last_edit_date", "lastEditDate", "LastEditDate"
            ),
            "etag": request.get("etag"),
        },
    }
    try:
        fingerprint = MATERIAL.canonical_feature_fingerprint(feature, 6)
    except (KeyError, TypeError, ValueError):
        return None, [Finding("FEATURE_GEOMETRY_INVALID", "/response/feature_collection/features")]
    return {"feature": feature, "fingerprint": fingerprint}, []


def _select_current_snapshot(
    package: Mapping[str, Any]
) -> tuple[dict[str, Any] | None, list[Finding]]:
    response = package["response"]
    request = package["request"]
    status = request["http_status"]
    if status == 304:
        return None, []
    collection = response["feature_collection"]
    features = collection["features"]
    expected_huc12 = package["huc12"]
    matches: list[Mapping[str, Any]] = []
    for raw in features:
        if not isinstance(raw, dict):
            return None, [Finding("FEATURE_INVALID", "/response/feature_collection/features")]
        properties = raw.get("properties")
        if isinstance(properties, dict) and _property(properties, "huc12", "HUC12") == expected_huc12:
            matches.append(raw)
    if len(matches) > 1:
        return None, [Finding("FEATURE_DUPLICATE_HUC12", "/response/feature_collection/features")]
    if not matches:
        return None, []
    return _normalize_feature(matches[0], expected_huc12, request)


def _assessment(
    package: Mapping[str, Any], current: dict[str, Any] | None
) -> tuple[dict[str, Any] | None, list[Finding]]:
    request = package["request"]
    if request["http_status"] == 304:
        return None, []
    prior = copy.deepcopy(package.get("prior_snapshot"))
    if prior is None and current is None:
        return None, [Finding("FEATURE_NOT_FOUND_WITHOUT_PRIOR", "/response/feature_collection/features")]
    digest = package["response"]["body_sha256"][len(HASH_PREFIX) :]
    candidate = {
        "object_type": "WbdHuc12MaterialChangeAssessment",
        "schema_version": "1.0.0",
        "assessment_id": f"huc12-change:{package['huc12']}:{digest[:16]}",
        "assessed_at": package["observed_at"],
        "source_descriptor_ref": SOURCE_DESCRIPTOR_REF,
        "huc12": package["huc12"],
        "normalization": {
            "crs": "EPSG:4326",
            "coordinate_precision": 6,
            "normalize_ring_direction": True,
            "sort_rings": True,
        },
        "prior": prior,
        "current": current,
        "decision": {},
        "governance": {
            "fixture_only": True,
            "network_fetch": False,
            "source_activation": False,
            "lifecycle_write": False,
            "promotion_allowed": False,
            "publication_allowed": False,
        },
        "spec_hash": "",
    }
    candidate["decision"] = MATERIAL.expected_decision(candidate)
    candidate["spec_hash"] = MATERIAL.canonical_spec_hash(candidate)
    validation = MATERIAL.validate_payload(candidate)
    if not validation.ok:
        return None, [
            Finding(f"ASSESSMENT_{finding.code}", finding.path)
            for finding in validation.findings
        ]
    return candidate, []


def build_candidate(package: Mapping[str, Any]) -> BuildResult:
    findings = _schema_findings(package, SOURCE_SCHEMA, prefix="SOURCE_PACKAGE")
    if findings:
        return BuildResult(None, tuple(sorted(set(findings))))

    try:
        expected_hash = canonical_hash(package)
    except (TypeError, ValueError, OverflowError, RecursionError):
        return BuildResult(None, (Finding("SOURCE_PACKAGE_CANONICALIZATION_INVALID", "/"),))
    if package.get("spec_hash") != expected_hash:
        findings.append(Finding("SOURCE_PACKAGE_SPEC_HASH_MISMATCH", "/spec_hash"))

    response = package["response"]
    request = package["request"]
    collection = response["feature_collection"]
    expected_body_hash = (
        None if collection is None else canonical_body_hash(collection)
    )
    if request["http_status"] == 304:
        if collection is not None or response["body_sha256"] is not None:
            findings.append(Finding("HTTP_NOT_MODIFIED_BODY_PRESENT", "/response"))
        if package.get("prior_snapshot") is None:
            findings.append(Finding("HTTP_NOT_MODIFIED_PRIOR_MISSING", "/prior_snapshot"))
    else:
        if collection is None:
            findings.append(Finding("HTTP_OK_BODY_MISSING", "/response/feature_collection"))
        elif response["body_sha256"] != expected_body_hash:
            findings.append(Finding("RESPONSE_BODY_HASH_MISMATCH", "/response/body_sha256"))

    findings.extend(_request_scope_findings(package))

    if findings:
        return BuildResult(None, tuple(sorted(set(findings))))

    current, current_findings = _select_current_snapshot(package)
    findings.extend(current_findings)
    if findings:
        return BuildResult(None, tuple(sorted(set(findings))))

    assessment, assessment_findings = _assessment(package, current)
    findings.extend(assessment_findings)
    if findings:
        return BuildResult(None, tuple(sorted(set(findings))))

    if request["http_status"] == 304:
        disposition = "NO_CHANGE_RECEIPT"
        reason_codes = ["HTTP_NOT_MODIFIED"]
    else:
        assert assessment is not None
        outcome = assessment["decision"]["outcome"]
        if outcome == "NO_CHANGE":
            disposition = "NO_CHANGE_RECEIPT"
            reason_codes = ["CONTENT_UNCHANGED"]
        else:
            disposition = "RAW_CANDIDATE"
            reason_codes = [{
                "ADD": "FEATURE_ADDED",
                "REMOVE": "FEATURE_REMOVED",
                "MATERIAL_CHANGE": "FEATURE_MATERIAL_CHANGE",
            }[outcome]]

    input_digest = package["spec_hash"][len(HASH_PREFIX) :]
    output: dict[str, Any] = {
        "object_type": "WbdHuc12IngestCandidate",
        "schema_version": "1.0.0",
        "candidate_id": f"wbd-huc12-ingest:{package['huc12']}:{input_digest[:24]}",
        "created_at": package["observed_at"],
        "source_descriptor_ref": SOURCE_DESCRIPTOR_REF,
        "source_package_id": package["package_id"],
        "source_package_spec_hash": package["spec_hash"],
        "huc12": package["huc12"],
        "request_evidence": {
            "url": request["url"],
            "where_clause": request["where_clause"],
            "out_fields": request["out_fields"],
            "http_status": request["http_status"],
            "etag": request.get("etag"),
            "last_modified": request.get("last_modified"),
            "content_type": request.get("content_type"),
            "body_sha256": response.get("body_sha256"),
        },
        "assessment": assessment,
        "disposition": disposition,
        "reason_codes": reason_codes,
        "allowed_lifecycle_targets": ALLOWED_TARGETS,
        "governance": {
            "fixture_only": True,
            "network_fetch": False,
            "source_activation": False,
            "lifecycle_write": False,
            "promotion_allowed": False,
            "release_allowed": False,
            "publication_allowed": False,
        },
        "spec_hash": "",
    }
    output["spec_hash"] = canonical_hash(output)
    output_findings = _schema_findings(output, OUTPUT_SCHEMA, prefix="OUTPUT")
    if output_findings:
        return BuildResult(None, tuple(sorted(set(output_findings))))
    return BuildResult(output, ())


def _serialize_findings(findings: Sequence[Finding]) -> str:
    return json.dumps(
        {
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in sorted(findings)
            ],
            "ok": False,
            "scope": "fixture-first-wbd-huc12-ingest-candidate",
            "authority": {
                "network_fetch": False,
                "source_activation": False,
                "lifecycle_write": False,
                "promotion": False,
                "publication": False,
            },
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build a deterministic fixture-first WBD HUC12 ingest candidate."
    )
    parser.add_argument("source_package", type=Path)
    parser.add_argument(
        "--output",
        type=Path,
        help="optional explicit output path; parent must already exist",
    )
    return parser


def write_output(path: Path, serialized: str) -> None:
    """Create one review artifact outside the repository, never through a symlink."""
    if path.name in {"", ".", ".."}:
        raise OSError("OUTPUT_PATH_UNSAFE")
    candidate = path if path.is_absolute() else Path.cwd() / path
    try:
        if any(parent.is_symlink() for parent in (candidate.parent, *candidate.parent.parents)):
            raise OSError("OUTPUT_PATH_UNSAFE")
        parent = candidate.parent.resolve(strict=True)
        if not parent.is_dir() or parent.is_relative_to(REPO_ROOT.resolve(strict=True)):
            raise OSError("OUTPUT_PATH_UNSAFE")
        descriptor, temporary = tempfile.mkstemp(dir=parent, prefix=".wbd-candidate-")
        try:
            with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                stream.write(serialized + "\n")
                stream.flush()
                os.fsync(stream.fileno())
            os.link(temporary, parent / candidate.name)
        finally:
            Path(temporary).unlink(missing_ok=True)
    except (OSError, RuntimeError) as error:
        raise OSError("OUTPUT_PATH_UNSAFE") from error


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    package, input_findings = read_json_object(args.source_package)
    if package is None:
        print(_serialize_findings(input_findings))
        return 2
    result = build_candidate(package)
    if not result.ok:
        print(_serialize_findings(result.findings))
        return 1
    assert result.output is not None
    serialized = json.dumps(
        result.output,
        sort_keys=True,
        separators=(",", ":"),
    )
    if args.output is not None:
        try:
            write_output(args.output, serialized)
        except OSError:
            print(
                _serialize_findings(
                    [Finding("OUTPUT_PATH_UNSAFE", "/")]
                )
            )
            return 2
    print(serialized)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
