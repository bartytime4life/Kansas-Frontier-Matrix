"""Shared types and bounded local helpers for KFM catalog-health validation."""
from __future__ import annotations

import hashlib
import ipaddress
import json
import math
import re
import urllib.parse
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping

REPO_ROOT = Path(__file__).resolve().parents[3]
FIXTURE_ROOT = REPO_ROOT / "fixtures/data/catalog_health"
PROFILE = "kfm.catalog-health.stac-item.v1"
SCOPE = "catalog-record-health-only"
VALIDATOR = {"name": "validate_catalog_health", "version": "1.0.0"}
MAX_RECORD_BYTES = 1_048_576
MAX_ASSET_BYTES = 16_777_216
MAX_ASSETS = 128
MAX_LINKS = 256
MAX_JSON_NODES = 50_000
MAX_JSON_DEPTH = 64
HEAD_TIMEOUT_SECONDS = 5.0
SHA256_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
REQUIRED_RELS = frozenset({"derived_from", "checksum", "commit", "manifest_uri"})
ERROR_CODES = frozenset(
    {
        "CAT_FILE_NOT_FOUND",
        "CAT_FILE_READ_ERROR",
        "CAT_FILE_TOO_LARGE",
        "CAT_INPUT_SYMLINK_DENIED",
        "CAT_JSON_COMPLEXITY_LIMIT",
        "CAT_JSON_DUPLICATE_KEY",
        "CAT_JSON_INVALID",
        "CAT_JSON_NONFINITE_NUMBER",
        "CAT_JSON_NOT_UTF8",
        "CAT_NETWORK_KILL_SWITCH",
        "CAT_ROOT_NOT_OBJECT",
    }
)


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str
    severity: str


@dataclass(frozen=True)
class HeadResult:
    status: int
    headers: Mapping[str, str]


@dataclass(frozen=True)
class ValidationResult:
    report: Mapping[str, Any]

    @property
    def outcome(self) -> str:
        return str(self.report["outcome"])

    @property
    def findings(self) -> tuple[Finding, ...]:
        return tuple(Finding(**item) for item in self.report["findings"])

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS"

    @property
    def error(self) -> bool:
        return self.outcome == "ERROR"


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


def _parse_float(value: str) -> float:
    number = float(value)
    if not math.isfinite(number):
        raise NonFiniteNumberError
    return number


def _within_json_limits(value: Any) -> bool:
    stack: list[tuple[Any, int]] = [(value, 0)]
    count = 0
    while stack:
        item, depth = stack.pop()
        count += 1
        if count > MAX_JSON_NODES or depth > MAX_JSON_DEPTH:
            return False
        if isinstance(item, dict):
            stack.extend((child, depth + 1) for child in item.values())
        elif isinstance(item, list):
            stack.extend((child, depth + 1) for child in item)
    return True


def read_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("CAT_INPUT_SYMLINK_DENIED", "/", "blocking")]
        if not path.is_file():
            return None, [Finding("CAT_FILE_NOT_FOUND", "/", "blocking")]
        if path.stat().st_size > MAX_RECORD_BYTES:
            return None, [Finding("CAT_FILE_TOO_LARGE", "/", "blocking")]
        with path.open("r", encoding="utf-8") as stream:
            value = json.load(
                stream,
                object_pairs_hook=_unique_object,
                parse_constant=_reject_nonfinite,
                parse_float=_parse_float,
            )
    except UnicodeDecodeError:
        return None, [Finding("CAT_JSON_NOT_UTF8", "/", "blocking")]
    except DuplicateKeyError:
        return None, [Finding("CAT_JSON_DUPLICATE_KEY", "/", "blocking")]
    except NonFiniteNumberError:
        return None, [Finding("CAT_JSON_NONFINITE_NUMBER", "/", "blocking")]
    except json.JSONDecodeError:
        return None, [Finding("CAT_JSON_INVALID", "/", "blocking")]
    except OSError:
        return None, [Finding("CAT_FILE_READ_ERROR", "/", "blocking")]
    except (RecursionError, ValueError):
        return None, [Finding("CAT_JSON_COMPLEXITY_LIMIT", "/", "blocking")]
    if not isinstance(value, dict):
        return None, [Finding("CAT_ROOT_NOT_OBJECT", "/", "blocking")]
    if not _within_json_limits(value):
        return None, [Finding("CAT_JSON_COMPLEXITY_LIMIT", "/", "blocking")]
    return value, []


def mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, dict) else {}


def array(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def string_list(value: Any) -> bool:
    return (
        isinstance(value, list)
        and bool(value)
        and all(text(item) for item in value)
        and len(value) == len(set(value))
    )


def canonical_digest(value: Mapping[str, Any]) -> str:
    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def safe_host(host: str | None) -> bool:
    if not host:
        return False
    host = host.rstrip(".").lower()
    if host == "localhost" or host.endswith((".localhost", ".local", ".internal")):
        return False
    try:
        address = ipaddress.ip_address(host)
    except ValueError:
        return True
    return not any(
        (
            address.is_private,
            address.is_loopback,
            address.is_link_local,
            address.is_multicast,
            address.is_reserved,
            address.is_unspecified,
        )
    )


def safe_href(value: Any) -> bool:
    if not text(value) or any(ord(char) < 32 for char in value):
        return False
    parsed = urllib.parse.urlsplit(value)
    if parsed.username or parsed.password:
        return False
    if not parsed.scheme:
        return not value.startswith(("/", "\\"))
    if parsed.scheme.lower() == "https":
        return safe_host(parsed.hostname)
    return parsed.scheme.lower() in {"urn", "git", "sha256"}


def bbox_valid(value: Any) -> bool:
    if not isinstance(value, list) or len(value) not in {4, 6}:
        return False
    return all(isinstance(item, (int, float)) and math.isfinite(item) for item in value)


def has_time(properties: Mapping[str, Any]) -> bool:
    if text(properties.get("datetime")):
        return True
    return text(properties.get("start_datetime")) and text(
        properties.get("end_datetime")
    )


def local_path(asset_root: Path, href: str) -> tuple[Path | None, str | None]:
    parsed = urllib.parse.urlsplit(href)
    if parsed.scheme or parsed.netloc or parsed.query or parsed.fragment:
        return None, "CAT_ASSET_HREF_INVALID"
    raw = urllib.parse.unquote(parsed.path)
    parts = Path(raw).parts
    if not raw or raw.startswith(("/", "\\")) or ".." in parts:
        return None, "CAT_ASSET_PATH_ESCAPE"
    try:
        root = asset_root.resolve(strict=True)
        current = root
        for part in parts:
            current = current / part
            if current.is_symlink():
                return None, "CAT_ASSET_SYMLINK_DENIED"
        resolved = root.joinpath(*parts).resolve(strict=True)
        resolved.relative_to(root)
    except FileNotFoundError:
        return None, "CAT_ASSET_NOT_FOUND"
    except ValueError:
        return None, "CAT_ASSET_PATH_ESCAPE"
    except OSError:
        return None, "CAT_ASSET_READ_ERROR"
    return resolved, None


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()


def outcome(findings: Iterable[Finding]) -> str:
    values = tuple(findings)
    if any(item.code in ERROR_CODES for item in values):
        return "ERROR"
    if any(item.severity == "blocking" for item in values):
        return "FAIL"
    if values:
        return "HOLD"
    return "PASS"


def make_report(
    path: Path,
    record: Mapping[str, Any] | None,
    findings: Iterable[Finding],
    *,
    network_mode: str,
    network: Mapping[str, int] | None = None,
    summary: Mapping[str, int] | None = None,
) -> ValidationResult:
    ordered = tuple(sorted(set(findings)))
    report = {
        "object_type": "CatalogHealthReport",
        "schema_version": "1.0.0",
        "profile": PROFILE,
        "validator": VALIDATOR,
        "target": {
            "file": display_path(path),
            "record_id": record.get("id") if record and text(record.get("id")) else None,
            "record_digest": canonical_digest(record) if record is not None else None,
        },
        "network": {
            "mode": network_mode,
            "attempted": int((network or {}).get("attempted", 0)),
            "succeeded": int((network or {}).get("succeeded", 0)),
        },
        "summary": {
            "assets_total": int((summary or {}).get("assets_total", 0)),
            "assets_local_verified": int((summary or {}).get("assets_local_verified", 0)),
            "assets_remote_reachable": int((summary or {}).get("assets_remote_reachable", 0)),
            "assets_embargoed": int((summary or {}).get("assets_embargoed", 0)),
            "assets_held": int((summary or {}).get("assets_held", 0)),
        },
        "outcome": outcome(ordered),
        "findings": [
            {"code": item.code, "field": item.field, "severity": item.severity}
            for item in ordered
        ],
        "scope": SCOPE,
        "authority_created": False,
    }
    return ValidationResult(report)


def serialize(result: ValidationResult) -> str:
    return json.dumps(
        result.report,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )
