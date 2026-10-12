"""Conservatively lint SQL window ordering in a closed fixture profile.

The validator never executes SQL and imports no database or network client. A
PASS proves only that recognized OVER clauses carry the declared simple primary
ordering field and final tie-breaker under the local ANSI-subset grammar.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/validation/window_ordering_lint_profile.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/validation/window_ordering_lint_profile/cases.json"
MAX_FILE_BYTES = 1_048_576
ABSTAIN_CODES = {"NAMED_WINDOW_DEFINITION_UNRESOLVED", "ORDER_EXPRESSION_UNSUPPORTED"}
ERROR_CODES = {"SQL_LEXICAL_ERROR", "SQL_PARENTHESIS_ERROR", "SQL_PARSE_ERROR"}
FRAME_TOKENS = {"ROWS", "RANGE", "GROUPS", "EXCLUDE"}
IDENTIFIER = re.compile(r"^[A-Za-z_][A-Za-z0-9_$]*(?:\.[A-Za-z_][A-Za-z0-9_$]*)*$")
OVER_TOKEN = re.compile(r"\bOVER\b", re.IGNORECASE)


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when a JSON number is not finite."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def codes(self) -> list[str]:
        return sorted({finding.code for finding in self.findings})


def _pairs(items: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in items:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _nonfinite(_value: str) -> object:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def load_json_object(path: Path) -> tuple[dict[str, object] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_nonfinite,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return None, [Finding("JSON_INVALID", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def canonical_hash(value: object) -> str:
    payload = json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def query_digest(sql: str) -> str:
    return "sha256:" + hashlib.sha256(sql.encode("utf-8")).hexdigest()


def compute_profile_hash(candidate: Mapping[str, object]) -> str:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("profile_spec_hash", None)
    return canonical_hash(subject)


def _load_schema() -> dict[str, object]:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def _schema_findings(candidate: object) -> list[Finding]:
    validator = Draft202012Validator(_load_schema(), format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(candidate), key=lambda error: (tuple(str(part) for part in error.absolute_path), str(error.validator)))
    return [Finding("SCHEMA_INVALID", "/" + "/".join(str(part) for part in error.absolute_path)) for error in errors[:100]]


def _is_utc(value: object) -> bool:
    if not isinstance(value, str) or not value.endswith("Z"):
        return False
    try:
        datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return False
    return True


def _mask_sql(sql: str) -> tuple[str | None, str | None]:
    """Blank strings, quoted identifiers, and comments while preserving length."""

    chars = list(sql)
    masked = list(sql)
    index = 0
    length = len(chars)
    while index < length:
        char = chars[index]
        next_char = chars[index + 1] if index + 1 < length else ""
        if char == "-" and next_char == "-":
            masked[index] = masked[index + 1] = " "
            index += 2
            while index < length and chars[index] not in "\r\n":
                masked[index] = " "
                index += 1
            continue
        if char == "/" and next_char == "*":
            masked[index] = masked[index + 1] = " "
            index += 2
            closed = False
            while index < length:
                if chars[index] == "*" and index + 1 < length and chars[index + 1] == "/":
                    masked[index] = masked[index + 1] = " "
                    index += 2
                    closed = True
                    break
                masked[index] = " "
                index += 1
            if not closed:
                return None, "SQL_LEXICAL_ERROR"
            continue
        if char in {"'", '"', "`"}:
            quote = char
            masked[index] = " "
            index += 1
            closed = False
            while index < length:
                masked[index] = " "
                if chars[index] == quote:
                    if index + 1 < length and chars[index + 1] == quote:
                        masked[index + 1] = " "
                        index += 2
                        continue
                    index += 1
                    closed = True
                    break
                index += 1
            if not closed:
                return None, "SQL_LEXICAL_ERROR"
            continue
        if char == "[":
            masked[index] = " "
            index += 1
            closed = False
            while index < length:
                masked[index] = " "
                if chars[index] == "]":
                    if index + 1 < length and chars[index + 1] == "]":
                        masked[index + 1] = " "
                        index += 2
                        continue
                    index += 1
                    closed = True
                    break
                index += 1
            if not closed:
                return None, "SQL_LEXICAL_ERROR"
            continue
        index += 1
    return "".join(masked), None


def _matching_paren(masked: str, start: int) -> int | None:
    depth = 0
    for index in range(start, len(masked)):
        if masked[index] == "(":
            depth += 1
        elif masked[index] == ")":
            depth -= 1
            if depth == 0:
                return index
            if depth < 0:
                return None
    return None


def _top_level_tokens(value: str) -> list[tuple[str, int, int]]:
    tokens: list[tuple[str, int, int]] = []
    depth = 0
    index = 0
    while index < len(value):
        char = value[index]
        if char == "(":
            depth += 1
            index += 1
            continue
        if char == ")":
            depth -= 1
            index += 1
            continue
        if depth == 0 and (char.isalpha() or char == "_"):
            end = index + 1
            while end < len(value) and (value[end].isalnum() or value[end] in "_$"):
                end += 1
            tokens.append((value[index:end].upper(), index, end))
            index = end
            continue
        index += 1
    return tokens


def _split_top_level(value: str) -> list[str] | None:
    parts: list[str] = []
    start = 0
    depth = 0
    for index, char in enumerate(value):
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth < 0:
                return None
        elif char == "," and depth == 0:
            parts.append(value[start:index].strip())
            start = index + 1
    if depth != 0:
        return None
    parts.append(value[start:].strip())
    return parts if all(parts) else None


def _normalized_identifier(value: str) -> str | None:
    stripped = re.sub(r"\s+NULLS\s+(?:FIRST|LAST)\s*$", "", value.strip(), flags=re.IGNORECASE)
    stripped = re.sub(r"\s+(?:ASC|DESC)\s*$", "", stripped, flags=re.IGNORECASE)
    if not IDENTIFIER.fullmatch(stripped):
        return None
    return stripped.rsplit(".", 1)[-1].lower()


def _window_clause_findings(content: str, index: int, primary: str, tie_breaker: str) -> set[Finding]:
    findings: set[Finding] = set()
    tokens = _top_level_tokens(content)
    order_start: int | None = None
    order_end = len(content)
    for position, token in enumerate(tokens[:-1]):
        if token[0] == "ORDER" and tokens[position + 1][0] == "BY":
            order_start = tokens[position + 1][2]
            for later in tokens[position + 2:]:
                if later[0] in FRAME_TOKENS:
                    order_end = later[1]
                    break
            break
    field = f"/sql/over/{index}"
    if order_start is None:
        return {Finding("WINDOW_ORDER_BY_REQUIRED", field)}
    parts = _split_top_level(content[order_start:order_end])
    if parts is None:
        return {Finding("SQL_PARSE_ERROR", field)}
    keys = [_normalized_identifier(part) for part in parts]
    if any(key is None for key in keys):
        return {Finding("ORDER_EXPRESSION_UNSUPPORTED", field)}
    normalized = [key for key in keys if key is not None]
    if len(normalized) != len(set(normalized)):
        findings.add(Finding("DUPLICATE_ORDER_KEY", field))
    if normalized[0] != primary:
        findings.add(Finding("PRIMARY_ORDER_KEY_NOT_FIRST", field))
    if tie_breaker not in normalized:
        findings.add(Finding("TIE_BREAKER_MISSING", field))
    elif normalized[-1] != tie_breaker:
        findings.add(Finding("TIE_BREAKER_NOT_LAST", field))
    return findings


def _lint_sql(sql: str, requirements: Mapping[str, object]) -> set[Finding]:
    masked, lexical_error = _mask_sql(sql)
    if lexical_error is not None:
        return {Finding(lexical_error, "/sql")}
    assert masked is not None
    stripped = masked.strip()
    semicolons = [index for index, char in enumerate(stripped) if char == ";"]
    findings: set[Finding] = set()
    if semicolons and (len(semicolons) > 1 or semicolons[0] != len(stripped) - 1):
        findings.add(Finding("MULTIPLE_STATEMENTS_UNSUPPORTED", "/sql"))

    matches = list(OVER_TOKEN.finditer(masked))
    window_count = len(matches)
    minimum = requirements["minimum_window_count"]
    maximum = requirements["maximum_window_count"]
    assert isinstance(minimum, int) and isinstance(maximum, int)
    if window_count == 0:
        findings.add(Finding("WINDOW_CLAUSE_REQUIRED", "/sql"))
    if not minimum <= window_count <= maximum:
        findings.add(Finding("WINDOW_COUNT_OUT_OF_RANGE", "/requirements"))

    primary = _normalized_identifier(str(requirements["primary_order_key"]))
    tie_breaker = _normalized_identifier(str(requirements["tie_breaker_key"]))
    assert primary is not None and tie_breaker is not None
    if primary == tie_breaker:
        findings.add(Finding("REQUIREMENT_KEYS_NOT_DISTINCT", "/requirements"))
        return findings

    for window_index, match in enumerate(matches):
        position = match.end()
        while position < len(masked) and masked[position].isspace():
            position += 1
        field = f"/sql/over/{window_index}"
        if position >= len(masked):
            findings.add(Finding("SQL_PARSE_ERROR", field))
            continue
        if masked[position] != "(":
            findings.add(Finding("NAMED_WINDOW_DEFINITION_UNRESOLVED", field))
            continue
        end = _matching_paren(masked, position)
        if end is None:
            findings.add(Finding("SQL_PARENTHESIS_ERROR", field))
            continue
        findings.update(_window_clause_findings(masked[position + 1:end], window_index, primary, tie_breaker))
    return findings


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate["profile_spec_hash"] != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if candidate["query_digest"] != query_digest(candidate["sql"]):
        findings.add(Finding("QUERY_DIGEST_MISMATCH", "/query_digest"))
    if not _is_utc(candidate["observed_at"]):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/observed_at"))
    requirements = candidate["requirements"]
    assert isinstance(requirements, Mapping)
    if requirements["minimum_window_count"] > requirements["maximum_window_count"]:
        findings.add(Finding("WINDOW_COUNT_RANGE_INCOHERENT", "/requirements"))
    findings.update(_lint_sql(candidate["sql"], requirements))
    return sorted(findings)


def validate_candidate(candidate: object) -> ValidationResult:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult("ERROR", tuple(schema_findings))
    assert isinstance(candidate, dict)
    findings = _semantic_findings(candidate)
    codes = {finding.code for finding in findings}
    if not codes:
        outcome = "PASS"
    elif codes & ERROR_CODES:
        outcome = "ERROR"
    elif codes <= ABSTAIN_CODES:
        outcome = "ABSTAIN"
    else:
        outcome = "DENY"
    return ValidationResult(outcome, tuple(findings))


def _merge_patch(base: object, patch: object) -> object:
    if not isinstance(patch, dict):
        return copy.deepcopy(patch)
    target = copy.deepcopy(base) if isinstance(base, dict) else {}
    for key, value in patch.items():
        target[key] = _merge_patch(target.get(key), value)
    return target


def materialize_fixture_case(manifest: Mapping[str, object], entry: Mapping[str, object]) -> dict[str, object]:
    candidate = _merge_patch(manifest["base_candidate"], entry.get("patch", {}))
    assert isinstance(candidate, dict)
    candidate["query_digest"] = query_digest(candidate["sql"])
    if entry.get("tamper") == "query_digest":
        candidate["query_digest"] = "sha256:" + "f" * 64
    candidate["profile_spec_hash"] = compute_profile_hash(candidate)
    if entry.get("tamper") == "profile_hash":
        candidate["profile_spec_hash"] = "sha256:" + "f" * 64
    return candidate


def validate_fixture_manifest(path: Path = FIXTURE_PATH) -> list[dict[str, object]]:
    manifest, load_findings = load_json_object(path)
    if manifest is None:
        return [{"name": "fixture_manifest", "ok": False, "observed": {"outcome": "ERROR", "codes": sorted({item.code for item in load_findings})}}]
    results: list[dict[str, object]] = []
    for entry in manifest["cases"]:
        candidate = materialize_fixture_case(manifest, entry)
        result = validate_candidate(candidate)
        observed = {"outcome": result.outcome, "codes": result.codes}
        expected = entry["expected"]
        results.append({"name": entry["name"], "ok": observed == expected, "expected": expected, "observed": observed})
    return results


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate fixture-only SQL window ordering lint candidates.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fixtures", action="store_true")
    group.add_argument("--input", type=Path)
    args = parser.parse_args(argv)
    if args.fixtures:
        results = validate_fixture_manifest()
        print(json.dumps(results, indent=2, sort_keys=True))
        return 0 if all(item["ok"] for item in results) else 1
    candidate, findings = load_json_object(args.input)
    result = ValidationResult("ERROR", tuple(sorted(findings))) if candidate is None else validate_candidate(candidate)
    print(json.dumps({"outcome": result.outcome, "codes": result.codes}, indent=2, sort_keys=True))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
