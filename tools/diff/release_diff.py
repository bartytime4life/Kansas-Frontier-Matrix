#!/usr/bin/env python3
"""Compare two local ReleaseManifest candidates without deciding release status.

The companion schema still has a permissive legacy profile. This comparator
requires only a typed ReleaseManifest and an unambiguous artifact-ref list; it
does not validate the contract, resolve references, or approve publication.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.diff import stable_diff as diff  # noqa: E402


TOOL_NAME = "release-manifest-diff"
MAX_INPUT_BYTES = 8 * 1024 * 1024
MAX_ARTIFACTS = 10_000


def _artifacts(value: dict[str, Any], label: str) -> dict[str, Any]:
    prefix = label.upper()
    if value.get("object_type") != "ReleaseManifest":
        raise diff.InputError(
            f"{prefix}_NOT_RELEASE_MANIFEST",
            f"{label} input must declare object_type ReleaseManifest.",
        )
    items = value.get("artifacts")
    if not isinstance(items, list) or not 1 <= len(items) <= MAX_ARTIFACTS:
        raise diff.InputError(
            f"{prefix}_ARTIFACTS_INVALID",
            f"{label} input must contain 1 to {MAX_ARTIFACTS} artifacts.",
        )
    indexed: dict[str, Any] = {}
    for item in items:
        if not isinstance(item, dict):
            raise diff.InputError(
                f"{prefix}_ARTIFACT_INVALID", f"{label} artifact must be an object."
            )
        ref = item.get("artifact_ref")
        if (
            not isinstance(ref, str)
            or not 3 <= len(ref) <= 640
            or any(char.isspace() for char in ref)
        ):
            raise diff.InputError(
                f"{prefix}_ARTIFACT_REF_INVALID",
                f"{label} artifact must have a bounded, nonblank reference.",
            )
        if ref in indexed:
            raise diff.InputError(
                f"{prefix}_ARTIFACT_REF_DUPLICATE",
                f"{label} artifact references must be unique.",
            )
        indexed[ref] = item
    return indexed


def _load(path: Path, label: str) -> tuple[dict[str, Any], dict[str, Any]]:
    try:
        if path.is_file() and path.stat().st_size > MAX_INPUT_BYTES:
            raise diff.InputError(
                f"{label.upper()}_TOO_LARGE",
                f"{label} input exceeds {MAX_INPUT_BYTES} bytes.",
            )
    except OSError as exc:
        raise diff.InputError(
            f"{label.upper()}_READ_ERROR", f"{label} input could not be read."
        ) from exc
    # Reuse the existing duplicate-key, nonfinite, UTF-8 and JSON error handling.
    try:
        value = diff._load_object(path, label)
    except RecursionError as exc:
        raise diff.InputError(
            f"{label.upper()}_NESTING_LIMIT", f"{label} input is too deeply nested."
        ) from exc
    return value, _artifacts(value, label)


def compare_paths(
    left: Path, right: Path, *, fail_on_change: bool = False
) -> tuple[dict[str, Any], int]:
    """Return field/ref changes without artifact payloads or policy decisions."""
    report: dict[str, Any] = {
        "tool": TOOL_NAME,
        "status": "error",
        "blocking": True,
        "left": str(left),
        "right": str(right),
        "summary": {"added": [], "removed": [], "changed": []},
        "artifacts": {"added": [], "removed": [], "changed": []},
    }
    try:
        left_value, left_artifacts = _load(left, "left")
        right_value, right_artifacts = _load(right, "right")
    except diff.InputError as exc:
        report["error"] = {"code": exc.code, "message": exc.message}
        return report, diff.EXIT_ERROR

    try:
        report["summary"] = diff._summary(left_value, right_value)
        left_refs, right_refs = set(left_artifacts), set(right_artifacts)
        report["artifacts"] = {
            "added": sorted(right_refs - left_refs),
            "removed": sorted(left_refs - right_refs),
            "changed": sorted(
                ref for ref in left_refs & right_refs
                if diff._canonical_value(left_artifacts[ref])
                != diff._canonical_value(right_artifacts[ref])
            ),
        }
    except RecursionError:
        report["summary"] = {"added": [], "removed": [], "changed": []}
        report["error"] = {
            "code": "COMPARE_NESTING_LIMIT",
            "message": "Input nesting is too deep to compare safely.",
        }
        return report, diff.EXIT_ERROR
    changed = any(report["summary"].values())
    report["status"] = "changed" if changed else "same"
    report["blocking"] = changed and fail_on_change
    return report, diff.EXIT_CHANGED if report["blocking"] else diff.EXIT_OK


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--left", required=True, type=Path)
    parser.add_argument("--right", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--fail-on-change", action="store_true")
    args = parser.parse_args(argv)
    report, exit_code = compare_paths(
        args.left, args.right, fail_on_change=args.fail_on_change
    )
    if args.output is not None:
        try:
            collision = args.output.resolve() in {
                args.left.resolve(), args.right.resolve()
            } or (
                args.output.exists() and any(
                    args.output.samefile(path) for path in (args.left, args.right)
                    if path.exists()
                )
            )
            if args.output.is_symlink() or collision:
                report["status"] = "error"
                report["blocking"] = True
                report["error"] = {
                    "code": "OUTPUT_PATH_UNSAFE",
                    "message": "Output must not be an input or a symbolic link.",
                }
                print(json.dumps(report, ensure_ascii=True, sort_keys=True, indent=2))
                return diff.EXIT_ERROR
        except (OSError, RuntimeError):
            report["status"] = "error"
            report["blocking"] = True
            report["error"] = {
                "code": "OUTPUT_PATH_UNSAFE",
                "message": "Output path could not be checked safely.",
            }
            print(json.dumps(report, ensure_ascii=True, sort_keys=True, indent=2))
            return diff.EXIT_ERROR
    rendered = json.dumps(report, ensure_ascii=True, sort_keys=True, indent=2) + "\n"
    if args.output is None:
        print(rendered, end="")
        return exit_code
    try:
        args.output.write_text(rendered, encoding="utf-8", newline="\n")
    except OSError:
        report["status"] = "error"
        report["blocking"] = True
        report["error"] = {
            "code": "OUTPUT_WRITE_ERROR",
            "message": "Output report could not be written.",
        }
        print(json.dumps(report, ensure_ascii=True, sort_keys=True, indent=2))
        return diff.EXIT_ERROR
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
