"""Strict local I/O and bounded subprocess helpers for promotion verification."""
from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

MAX_BYTES = 8 * 1024 * 1024
MAX_OUTPUT = 256 * 1024
TIMEOUT = 30
HASH_PREFIX = "sha256:"
STATUS_RANK = {"PASS": 0, "ABSTAIN": 1, "DENY": 2, "ERROR": 3}


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str
    status: str


@dataclass(frozen=True)
class ProcessResult:
    status: str
    exit_code: int | None
    stdout_sha256: str | None
    stderr_sha256: str | None
    finding: Finding | None = None
    payload: dict[str, Any] | None = None


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_nonfinite(value: str) -> None:
    raise NonFiniteNumberError(value)


def pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def sha_bytes(value: bytes) -> str:
    return HASH_PREFIX + hashlib.sha256(value).hexdigest()


def sha_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while chunk := stream.read(1024 * 1024):
            digest.update(chunk)
    return HASH_PREFIX + digest.hexdigest()


def canonical_hash(value: Mapping[str, Any]) -> str:
    payload = copy.deepcopy(dict(value))
    payload.pop("spec_hash", None)
    encoded = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return sha_bytes(encoded)


def read_json(path: Path) -> tuple[Any | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/", "ERROR")]
        if not path.is_file():
            return None, [Finding("INPUT_NOT_FILE", "/", "ERROR")]
        if path.stat().st_size > MAX_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", "/", "ERROR")]
        return json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_nonfinite,
        ), []
    except UnicodeError:
        return None, [Finding("JSON_NOT_UTF8", "/", "ERROR")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/", "ERROR")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/", "ERROR")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/", "ERROR")]
    except OSError:
        return None, [Finding("INPUT_UNREADABLE", "/", "ERROR")]


def resolve(root: Path, relative: str, *, directory: bool = False) -> tuple[Path | None, Finding | None]:
    rel = Path(relative)
    if rel.is_absolute() or any(part in {"", ".", ".."} for part in rel.parts):
        return None, Finding("REFERENCE_PATH_UNSAFE", "/", "DENY")
    base = root.resolve()
    current = base
    try:
        for part in rel.parts:
            current /= part
            if current.is_symlink():
                return None, Finding("REFERENCE_SYMLINK_DENIED", "/", "DENY")
        resolved = current.resolve(strict=True)
        resolved.relative_to(base)
    except FileNotFoundError:
        return None, Finding("REFERENCE_NOT_FOUND", "/", "ABSTAIN")
    except (OSError, ValueError):
        return None, Finding("REFERENCE_PATH_UNSAFE", "/", "DENY")
    if directory and not resolved.is_dir():
        return None, Finding("REFERENCE_NOT_DIRECTORY", "/", "DENY")
    if not directory and not resolved.is_file():
        return None, Finding("REFERENCE_NOT_FILE", "/", "DENY")
    return resolved, None


def schema_findings(value: Any, schema_path: Path) -> list[Finding]:
    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = sorted(
            Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(value),
            key=lambda error: (pointer(error.absolute_path), str(error.validator)),
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("EXECUTION_SCHEMA_UNAVAILABLE", "/", "ERROR")]
    return [Finding("EXECUTION_SCHEMA_INVALID", pointer(error.absolute_path), "DENY") for error in errors[:100]]


def _command(path: Path, args: Sequence[str]) -> list[str]:
    return [sys.executable, str(path), *args] if path.suffix == ".py" else [str(path), *args]


def _environment(repo_root: Path) -> dict[str, str]:
    return {
        "HOME": os.environ.get("HOME", str(repo_root)),
        "LANG": "C.UTF-8",
        "LC_ALL": "C.UTF-8",
        "PATH": os.environ.get("PATH", ""),
        "PYTHONDONTWRITEBYTECODE": "1",
        "PYTHONHASHSEED": "0",
        "TZ": "UTC",
    }


def run_tool(repo_root: Path, path: Path, args: Sequence[str], *, deny_code: str, error_path: str) -> ProcessResult:
    try:
        completed = subprocess.run(
            _command(path, args),
            cwd=repo_root,
            env=_environment(repo_root),
            check=False,
            capture_output=True,
            timeout=TIMEOUT,
        )
    except subprocess.TimeoutExpired:
        return ProcessResult("ERROR", None, None, None, Finding("TOOL_TIMEOUT", error_path, "ERROR"))
    except OSError:
        return ProcessResult("ERROR", None, None, None, Finding("TOOL_EXECUTION_ERROR", error_path, "ERROR"))
    if max(len(completed.stdout), len(completed.stderr)) > MAX_OUTPUT:
        return ProcessResult("ERROR", completed.returncode, None, None, Finding("TOOL_OUTPUT_TOO_LARGE", error_path, "ERROR"))
    return ProcessResult(
        "PASS" if completed.returncode == 0 else "DENY",
        completed.returncode,
        sha_bytes(completed.stdout),
        sha_bytes(completed.stderr),
        None if completed.returncode == 0 else Finding(deny_code, error_path, "DENY"),
    )


def run_validator(repo_root: Path, path: Path, target: Path, *, deny_code: str, error_code: str) -> ProcessResult:
    try:
        completed = subprocess.run(
            _command(path, [str(target)]),
            cwd=repo_root,
            env=_environment(repo_root),
            check=False,
            capture_output=True,
            timeout=TIMEOUT,
        )
    except subprocess.TimeoutExpired:
        return ProcessResult("ERROR", None, None, None, Finding("TOOL_TIMEOUT", "/validators", "ERROR"))
    except OSError:
        return ProcessResult("ERROR", None, None, None, Finding("TOOL_EXECUTION_ERROR", "/validators", "ERROR"))
    if max(len(completed.stdout), len(completed.stderr)) > MAX_OUTPUT:
        return ProcessResult("ERROR", completed.returncode, None, None, Finding("TOOL_OUTPUT_TOO_LARGE", "/validators", "ERROR"))
    stdout_hash = sha_bytes(completed.stdout)
    stderr_hash = sha_bytes(completed.stderr)
    lines = [line for line in completed.stdout.decode("utf-8", "replace").splitlines() if line.strip()]
    try:
        payload = json.loads(lines[-1]) if lines else {}
    except json.JSONDecodeError:
        return ProcessResult("ERROR", completed.returncode, stdout_hash, stderr_hash, Finding(error_code, "/validators", "ERROR"))
    raw = payload.get("status", payload.get("outcome")) if isinstance(payload, dict) else None
    status = "DENY" if raw == "FAIL" else raw
    if status not in {"PASS", "ABSTAIN", "DENY", "ERROR"}:
        return ProcessResult("ERROR", completed.returncode, stdout_hash, stderr_hash, Finding(error_code, "/validators", "ERROR"))
    if completed.returncode == 2 or status == "ERROR":
        return ProcessResult("ERROR", completed.returncode, stdout_hash, stderr_hash, Finding(error_code, "/validators", "ERROR"), payload)
    if completed.returncode != 0 or status != "PASS":
        finite = "ABSTAIN" if status == "ABSTAIN" else "DENY"
        return ProcessResult(finite, completed.returncode, stdout_hash, stderr_hash, Finding(deny_code, "/validators", finite), payload)
    return ProcessResult("PASS", 0, stdout_hash, stderr_hash, None, payload)


def tool_digest(path: Path, pointer_value: str) -> tuple[str | None, Finding | None]:
    try:
        if path.is_symlink() or not path.is_file():
            return None, Finding("TOOL_BINARY_UNSAFE", pointer_value, "DENY")
        return sha_file(path), None
    except OSError:
        return None, Finding("TOOL_BINARY_UNREADABLE", pointer_value, "ERROR")
