from __future__ import annotations

import copy
import hashlib
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "schemas/contracts/v1/runtime/place_name_search_projection.schema.json"
FIXTURE_ROOT = ROOT / "fixtures/contracts/v1/runtime/place_name_search_projection"
MAX_BYTES = 1_048_576


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class Result:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def error(self) -> bool:
        return any(
            item.code.startswith(("FILE_", "JSON_", "INPUT_", "SCHEMA_UNAVAILABLE"))
            for item in self.findings
        )


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out:
            raise DuplicateKeyError
        out[key] = value
    return out


def _reject(_: str) -> None:
    raise NonFiniteNumberError


def _finite(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def read_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject,
            parse_float=_finite,
        )
    except UnicodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
    if not isinstance(value, dict):
        return None, [Finding("JSON_ROOT_INVALID", "/")]
    return value, []


def arr(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def obj(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def canonical_strings(values: list[Any]) -> bool:
    return all(isinstance(item, str) for item in values) and values == sorted(set(values))


def canonical_spec_hash(candidate: Mapping[str, Any]) -> str:
    projected = dict(candidate)
    projected.pop("spec_hash", None)
    payload = json.dumps(
        projected, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = sorted(
            Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(candidate),
            key=lambda item: (pointer(item.absolute_path), str(item.validator)),
        )[:100]
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    return [Finding("SCHEMA_INVALID", pointer(error.absolute_path)) for error in errors]


def _set_path(value: dict[str, Any], raw_path: str, replacement: Any) -> None:
    parts = raw_path.split("/")[1:]
    target: Any = value
    for raw in parts[:-1]:
        token = raw.replace("~1", "/").replace("~0", "~")
        target = target[int(token)] if isinstance(target, list) else target[token]
    token = parts[-1].replace("~1", "/").replace("~0", "~")
    if isinstance(target, list):
        target.append(copy.deepcopy(replacement)) if token == "-" else target.__setitem__(int(token), copy.deepcopy(replacement))
    else:
        target[token] = copy.deepcopy(replacement)


def apply_patch(base: Mapping[str, Any], operations: list[Any], recompute_hash: bool = True) -> dict[str, Any]:
    value = copy.deepcopy(dict(base))
    for operation in operations:
        if not isinstance(operation, dict) or operation.get("op") not in {"add", "replace"}:
            raise ValueError("unsupported fixture patch")
        raw_path = operation.get("path")
        if not isinstance(raw_path, str) or not raw_path.startswith("/"):
            raise ValueError("invalid fixture patch path")
        _set_path(value, raw_path, operation.get("value"))
    if recompute_hash:
        value["spec_hash"] = canonical_spec_hash(value)
    return value


def load_fixture_bundle() -> dict[str, Any]:
    names = {
        "base": "base_current.json",
        "valid": "valid_cases.json",
        "invalid": "invalid_cases.json",
    }
    bundle: dict[str, Any] = {}
    for key, name in names.items():
        value, findings = read_object(FIXTURE_ROOT / name)
        if value is None or findings:
            raise ValueError(f"fixture {key} unavailable")
        bundle[key] = value
    return bundle


def materialize_fixture(case: Mapping[str, Any], bundle: Mapping[str, Any] | None = None) -> dict[str, Any]:
    source = dict(bundle or load_fixture_bundle())
    base = source["base"]
    if "base_valid" in case:
        valid_case = obj(source["valid"]).get(case.get("base_valid"))
        if not isinstance(valid_case, dict):
            raise ValueError("valid fixture base unavailable")
        base = apply_patch(base, arr(valid_case.get("patch")))
    return apply_patch(
        base,
        arr(case.get("patch")),
        recompute_hash=case.get("recompute_hash") is not False,
    )
