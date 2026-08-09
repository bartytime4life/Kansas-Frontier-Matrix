"""Deterministic, read-only local JSON Schema registry construction.

The canonical schemas remain outside this package.  Callers provide an explicit
schema root, and this module indexes local ``*.schema.json`` files without
network access or writes.  Registry construction proves only local shape and
identity mechanics; it grants no contract, policy, review, release, or
publication authority.
"""

from __future__ import annotations

import hashlib
import json
import math
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path, PurePosixPath
from typing import Any

from referencing import Registry, Resource

SNAPSHOT_PROFILE = "kfm.schema-registry.snapshot.v1"
DEFAULT_MAX_SCHEMA_BYTES = 2 * 1024 * 1024
DEFAULT_MAX_TOTAL_BYTES = 128 * 1024 * 1024
DEFAULT_MAX_SCHEMAS = 10_000


class RegistryErrorCode(StrEnum):
    """Stable fail-closed build outcomes."""

    ROOT_NOT_FOUND = "ROOT_NOT_FOUND"
    ROOT_NOT_DIRECTORY = "ROOT_NOT_DIRECTORY"
    ROOT_SYMLINK_DENIED = "ROOT_SYMLINK_DENIED"
    PATH_ESCAPE = "PATH_ESCAPE"
    SYMLINK_DENIED = "SYMLINK_DENIED"
    SCHEMA_LIMIT_EXCEEDED = "SCHEMA_LIMIT_EXCEEDED"
    TOTAL_BYTES_EXCEEDED = "TOTAL_BYTES_EXCEEDED"
    FILE_TOO_LARGE = "FILE_TOO_LARGE"
    FILE_UNREADABLE = "FILE_UNREADABLE"
    JSON_INVALID = "JSON_INVALID"
    JSON_DUPLICATE_KEY = "JSON_DUPLICATE_KEY"
    JSON_NONFINITE_NUMBER = "JSON_NONFINITE_NUMBER"
    JSON_ROOT_INVALID = "JSON_ROOT_INVALID"
    SCHEMA_ID_INVALID = "SCHEMA_ID_INVALID"
    DUPLICATE_ID = "DUPLICATE_ID"


class LookupOutcome(StrEnum):
    """Finite outcomes for one local schema-id lookup."""

    RESOLVED = "RESOLVED"
    UNRESOLVED = "UNRESOLVED"


class SchemaRegistryError(ValueError):
    """One bounded registry-construction failure."""

    def __init__(
        self,
        code: RegistryErrorCode,
        *,
        path: str | None = None,
        detail: str,
    ) -> None:
        self.code = code
        self.path = path
        self.detail = detail
        super().__init__(f"{code}: {detail}")

    def as_dict(self) -> dict[str, str]:
        result = {"code": self.code.value, "detail": self.detail}
        if self.path is not None:
            result["path"] = self.path
        return result


@dataclass(frozen=True, slots=True)
class SchemaRecord:
    """Immutable index record for one schema with a usable ``$id``."""

    schema_id: str
    relative_path: str
    sha256: str
    canonical_json: str

    def document(self) -> dict[str, Any]:
        """Return a fresh decoded schema document for an isolated caller."""

        value = json.loads(self.canonical_json)
        if not isinstance(value, dict):
            raise AssertionError("schema record root is not an object")
        return value

    def as_dict(self) -> dict[str, str]:
        return {
            "schema_id": self.schema_id,
            "path": self.relative_path,
            "sha256": self.sha256,
        }


@dataclass(frozen=True, slots=True)
class SkippedSchema:
    """One local schema file omitted from the id registry for a visible reason."""

    relative_path: str
    reason: str
    sha256: str

    def as_dict(self) -> dict[str, str]:
        return {
            "path": self.relative_path,
            "reason": self.reason,
            "sha256": self.sha256,
        }


@dataclass(frozen=True, slots=True)
class LookupResult:
    """Typed local lookup result; resolution is not policy or release approval."""

    outcome: LookupOutcome
    record: SchemaRecord | None


@dataclass(frozen=True, slots=True)
class RegistrySnapshot:
    """Deterministic index over one explicit local schema root."""

    records: tuple[SchemaRecord, ...]
    skipped: tuple[SkippedSchema, ...]
    snapshot_sha256: str

    @property
    def schema_ids(self) -> tuple[str, ...]:
        return tuple(record.schema_id for record in self.records)

    def lookup(self, schema_id: str) -> LookupResult:
        for record in self.records:
            if record.schema_id == schema_id:
                return LookupResult(LookupOutcome.RESOLVED, record)
        return LookupResult(LookupOutcome.UNRESOLVED, None)

    def to_referencing_registry(self) -> Registry:
        resources = (
            (record.schema_id, Resource.from_contents(record.document()))
            for record in self.records
        )
        return Registry().with_resources(resources)

    def as_dict(self) -> dict[str, object]:
        return {
            "profile": SNAPSHOT_PROFILE,
            "record_count": len(self.records),
            "skipped_count": len(self.skipped),
            "records": [record.as_dict() for record in self.records],
            "skipped": [item.as_dict() for item in self.skipped],
            "snapshot_sha256": self.snapshot_sha256,
            "authority": "helper_only",
        }


class _DuplicateKeyError(ValueError):
    pass


class _NonFiniteNumberError(ValueError):
    pass


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise _DuplicateKeyError
        result[key] = value
    return result


def _reject_nonfinite(_value: str) -> Any:
    raise _NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise _NonFiniteNumberError
    return parsed


def _sha256_bytes(value: bytes) -> str:
    return f"sha256:{hashlib.sha256(value).hexdigest()}"


def _canonical_json(value: dict[str, Any]) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def _relative_path(root: Path, path: Path) -> str:
    try:
        relative = path.resolve(strict=True).relative_to(root)
    except (OSError, ValueError) as exc:
        raise SchemaRegistryError(
            RegistryErrorCode.PATH_ESCAPE,
            detail="schema path does not remain inside the admitted root",
        ) from exc
    value = PurePosixPath(relative.as_posix())
    if not value.parts or any(part in {".", ".."} for part in value.parts):
        raise SchemaRegistryError(
            RegistryErrorCode.PATH_ESCAPE,
            detail="schema path is not a canonical relative path",
        )
    return value.as_posix()


def _load_schema(path: Path, relative_path: str, raw: bytes) -> dict[str, Any]:
    try:
        text = raw.decode("utf-8")
    except UnicodeError as exc:
        raise SchemaRegistryError(
            RegistryErrorCode.FILE_UNREADABLE,
            path=relative_path,
            detail="schema file is not valid UTF-8",
        ) from exc

    try:
        value = json.loads(
            text,
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_nonfinite,
            parse_float=_parse_finite_float,
        )
    except _DuplicateKeyError as exc:
        raise SchemaRegistryError(
            RegistryErrorCode.JSON_DUPLICATE_KEY,
            path=relative_path,
            detail="schema JSON repeats a member name",
        ) from exc
    except _NonFiniteNumberError as exc:
        raise SchemaRegistryError(
            RegistryErrorCode.JSON_NONFINITE_NUMBER,
            path=relative_path,
            detail="schema JSON contains a non-finite number",
        ) from exc
    except (json.JSONDecodeError, RecursionError, ValueError) as exc:
        raise SchemaRegistryError(
            RegistryErrorCode.JSON_INVALID,
            path=relative_path,
            detail="schema file is not valid bounded JSON",
        ) from exc

    if not isinstance(value, dict):
        raise SchemaRegistryError(
            RegistryErrorCode.JSON_ROOT_INVALID,
            path=relative_path,
            detail="schema JSON root must be an object",
        )
    return value


def build_registry_snapshot(
    schema_root: Path,
    *,
    max_schema_bytes: int = DEFAULT_MAX_SCHEMA_BYTES,
    max_total_bytes: int = DEFAULT_MAX_TOTAL_BYTES,
    max_schemas: int = DEFAULT_MAX_SCHEMAS,
) -> RegistrySnapshot:
    """Build a deterministic local index from one explicit schema root.

    Schemas without ``$id`` are preserved as visible ``MISSING_ID`` skips to
    match the repository's current local-resolver behavior.  Duplicate ids,
    malformed JSON, symlinks, path escape, and resource-limit violations fail
    closed with stable error codes.
    """

    root = Path(schema_root)
    if root.is_symlink():
        raise SchemaRegistryError(
            RegistryErrorCode.ROOT_SYMLINK_DENIED,
            detail="schema root must not be a symbolic link",
        )
    if not root.exists():
        raise SchemaRegistryError(
            RegistryErrorCode.ROOT_NOT_FOUND,
            detail="schema root was not found",
        )
    if not root.is_dir():
        raise SchemaRegistryError(
            RegistryErrorCode.ROOT_NOT_DIRECTORY,
            detail="schema root is not a directory",
        )
    try:
        resolved_root = root.resolve(strict=True)
    except OSError as exc:
        raise SchemaRegistryError(
            RegistryErrorCode.FILE_UNREADABLE,
            detail="schema root could not be resolved safely",
        ) from exc

    for candidate in sorted(resolved_root.rglob("*"), key=lambda value: value.as_posix()):
        if candidate.is_symlink():
            relative = candidate.relative_to(resolved_root).as_posix()
            raise SchemaRegistryError(
                RegistryErrorCode.SYMLINK_DENIED,
                path=relative,
                detail="symbolic links are denied inside the schema root",
            )

    schema_paths = sorted(
        (
            path
            for path in resolved_root.rglob("*.schema.json")
            if path.is_file()
        ),
        key=lambda value: value.relative_to(resolved_root).as_posix(),
    )
    if len(schema_paths) > max_schemas:
        raise SchemaRegistryError(
            RegistryErrorCode.SCHEMA_LIMIT_EXCEEDED,
            detail="schema file count exceeds the configured limit",
        )

    by_id: dict[str, SchemaRecord] = {}
    skipped: list[SkippedSchema] = []
    total_bytes = 0

    for path in schema_paths:
        relative = _relative_path(resolved_root, path)
        try:
            size = path.stat().st_size
        except OSError as exc:
            raise SchemaRegistryError(
                RegistryErrorCode.FILE_UNREADABLE,
                path=relative,
                detail="schema file metadata could not be read",
            ) from exc
        if size > max_schema_bytes:
            raise SchemaRegistryError(
                RegistryErrorCode.FILE_TOO_LARGE,
                path=relative,
                detail="schema file exceeds the configured per-file limit",
            )
        total_bytes += size
        if total_bytes > max_total_bytes:
            raise SchemaRegistryError(
                RegistryErrorCode.TOTAL_BYTES_EXCEEDED,
                detail="schema corpus exceeds the configured total-byte limit",
            )
        try:
            raw = path.read_bytes()
        except OSError as exc:
            raise SchemaRegistryError(
                RegistryErrorCode.FILE_UNREADABLE,
                path=relative,
                detail="schema file could not be read",
            ) from exc

        document = _load_schema(path, relative, raw)
        digest = _sha256_bytes(raw)
        schema_id = document.get("$id")
        if schema_id is None:
            skipped.append(SkippedSchema(relative, "MISSING_ID", digest))
            continue
        if not isinstance(schema_id, str) or not schema_id.strip():
            raise SchemaRegistryError(
                RegistryErrorCode.SCHEMA_ID_INVALID,
                path=relative,
                detail="schema $id must be a non-empty string when present",
            )
        if schema_id in by_id:
            raise SchemaRegistryError(
                RegistryErrorCode.DUPLICATE_ID,
                path=relative,
                detail="more than one schema claims the same $id",
            )
        by_id[schema_id] = SchemaRecord(
            schema_id=schema_id,
            relative_path=relative,
            sha256=digest,
            canonical_json=_canonical_json(document),
        )

    records = tuple(sorted(by_id.values(), key=lambda record: record.schema_id))
    skipped_tuple = tuple(sorted(skipped, key=lambda item: item.relative_path))
    digest_payload = {
        "profile": SNAPSHOT_PROFILE,
        "records": [record.as_dict() for record in records],
        "skipped": [item.as_dict() for item in skipped_tuple],
    }
    snapshot_sha256 = _sha256_bytes(_canonical_json(digest_payload).encode("utf-8"))
    return RegistrySnapshot(records, skipped_tuple, snapshot_sha256)


def build_referencing_registry(schema_root: Path) -> Registry:
    """Build the runtime ``referencing.Registry`` from a strict local snapshot."""

    return build_registry_snapshot(schema_root).to_referencing_registry()
