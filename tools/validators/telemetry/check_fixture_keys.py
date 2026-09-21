"""Reject unsafe JSON keys in the four fixture-only telemetry profiles.

This is a bounded repository fixture check, not an operational redactor or
policy evaluator. It never inspects a producer, emitted event, or sink.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/telemetry"
MAX_JSON_BYTES = 5 * 1024 * 1024
MAX_JSON_FILES = 1_000
FORBIDDEN = {
    "prompts": frozenset(
        {
            "prompt", "prompts", "messages", "input_text", "inputText",
            "output_text", "outputText", "chain_of_thought", "chainOfThought",
            "reasoning_content", "reasoningContent", "raw_prompt", "rawPrompt",
        }
    ),
    "coordinates": frozenset(
        {"lat", "lon", "latitude", "longitude", "coordinates", "geometry", "bbox", "wkt"}
    ),
}


class InvalidJson(ValueError):
    pass


def _object_pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise InvalidJson("JSON_DUPLICATE_KEY")
        result[key] = value
    return result


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise InvalidJson("JSON_NONFINITE_NUMBER")
    return parsed


def _nonfinite_constant(_value: str) -> object:
    raise InvalidJson("JSON_NONFINITE_NUMBER")


def _normalized(key: str) -> str:
    return unicodedata.normalize("NFKC", key).casefold()


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


def scan_tree(root: Path, category: str) -> tuple[Finding, ...]:
    if category not in FORBIDDEN:
        raise ValueError("unknown fixture key category")
    if not root.is_dir() or root.is_symlink():
        return (Finding("FIXTURE_ROOT_INVALID", "."),)

    forbidden = {_normalized(key) for key in FORBIDDEN[category]}
    paths = sorted(root.rglob("*.json"))
    if not paths:
        return (Finding("NO_JSON_FIXTURES", "."),)
    if len(paths) > MAX_JSON_FILES:
        return (Finding("TOO_MANY_JSON_FIXTURES", "."),)

    findings: set[Finding] = set()
    for path in paths:
        relative = path.relative_to(root).as_posix()
        if path.is_symlink() or not path.is_file():
            findings.add(Finding("FIXTURE_NOT_REGULAR", relative))
            continue
        try:
            if path.stat().st_size > MAX_JSON_BYTES:
                findings.add(Finding("FIXTURE_TOO_LARGE", relative))
                continue
        except OSError:
            findings.add(Finding("FIXTURE_UNREADABLE", relative))
            continue
        try:
            document = json.loads(
                path.read_text(encoding="utf-8"),
                object_pairs_hook=_object_pairs,
                parse_float=_finite_float,
                parse_constant=_nonfinite_constant,
            )
        except InvalidJson as exc:
            findings.add(Finding(str(exc), relative))
            continue
        except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
            findings.add(Finding("JSON_INVALID", relative))
            continue

        def walk(value: object, pointer: str = "$") -> None:
            if isinstance(value, dict):
                for index, (key, child) in enumerate(value.items()):
                    # Indices avoid reflecting untrusted field names into CI logs.
                    child_pointer = f"{pointer}/{index}"
                    if _normalized(key) in forbidden:
                        findings.add(Finding("FORBIDDEN_KEY", relative + ":" + child_pointer))
                    walk(child, child_pointer)
            elif isinstance(value, list):
                for index, child in enumerate(value):
                    walk(child, f"{pointer}/{index}")

        walk(document)
    return tuple(sorted(findings))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("category", choices=sorted(FORBIDDEN))
    args = parser.parse_args()
    findings = scan_tree(FIXTURE_ROOT, args.category)
    for finding in findings:
        print(f"{finding.code} {finding.path}")
    if findings:
        return 1
    print(f"PASS: fixture-only telemetry {args.category} keys absent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
