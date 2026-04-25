#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

DEFAULT_MARKERS = ["TODO", "UNKNOWN", "NEEDS VERIFICATION"]
DEFAULT_EXCLUDES = {".git", ".pytest_cache", "__pycache__"}


def iter_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in DEFAULT_EXCLUDES for part in path.parts):
            continue
        files.append(path)
    return files


def count_markers(path: Path, markers: list[str]) -> dict[str, int] | None:
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return None

    counts = {marker: text.count(marker) for marker in markers}
    if sum(counts.values()) == 0:
        return None
    return counts


def main() -> int:
    parser = argparse.ArgumentParser(description="Report placeholder marker counts and top files.")
    parser.add_argument("--root", default=".", help="Repository root path")
    parser.add_argument("--top", type=int, default=10, help="How many top files to include")
    parser.add_argument("--format", choices=["text", "json"], default="text", help="Output format")
    parser.add_argument(
        "--marker",
        action="append",
        dest="markers",
        default=None,
        help="Marker to count (repeatable). Defaults to TODO/UNKNOWN/NEEDS VERIFICATION.",
    )
    parser.add_argument(
        "--max-overall",
        type=int,
        default=None,
        help="Fail with exit code 1 when total marker count exceeds this value.",
    )
    parser.add_argument(
        "--max-marker",
        action="append",
        default=None,
        help="Per-marker threshold in the form MARKER=COUNT (repeatable).",
    )
    args = parser.parse_args()

    root = Path(args.root)
    if not root.is_dir():
        print(f"report_placeholder_markers: invalid root path (expected directory): {root}", file=sys.stderr)
        return 2

    markers = args.markers if args.markers else list(DEFAULT_MARKERS)
    marker_thresholds: dict[str, int] = {}
    for raw in args.max_marker or []:
        marker, sep, value = raw.partition("=")
        if not sep or not marker or not value:
            print(f"report_placeholder_markers: invalid --max-marker value: {raw}", file=sys.stderr)
            return 2
        try:
            marker_thresholds[marker] = int(value)
        except ValueError:
            print(f"report_placeholder_markers: invalid threshold count in --max-marker: {raw}", file=sys.stderr)
            return 2
    per_file: list[dict[str, object]] = []
    totals = {marker: 0 for marker in markers}

    for file_path in iter_files(root):
        counts = count_markers(file_path, markers)
        if counts is None:
            continue

        total = sum(counts.values())
        for marker, value in counts.items():
            totals[marker] += value

        per_file.append(
            {
                "path": str(file_path.relative_to(root)),
                "total": total,
                "counts": counts,
            }
        )

    per_file.sort(key=lambda item: (int(item["total"]), str(item["path"])), reverse=True)
    top_files = per_file[: max(args.top, 0)]

    if args.format == "json":
        payload = {
            "root": str(root),
            "markers": markers,
            "totals": totals,
            "files_with_markers": len(per_file),
            "top_files": top_files,
        }
        print(json.dumps(payload, indent=2, sort_keys=True))
        return 0

    print(f"report_placeholder_markers: scanned root={root}")
    for marker in markers:
        print(f"{marker}: {totals[marker]}")
    print(f"files_with_markers: {len(per_file)}")

    if top_files:
        print(f"top_files (limit={max(args.top, 0)}):")
        for item in top_files:
            marker_details = ", ".join(
                f"{marker}={item['counts'][marker]}" for marker in markers if item["counts"][marker] > 0
            )
            print(f"- {item['path']}: total={item['total']} ({marker_details})")
    else:
        print("top_files: none")

    overall_total = sum(totals.values())
    threshold_errors: list[str] = []

    if args.max_overall is not None and overall_total > args.max_overall:
        threshold_errors.append(
            f"overall marker total {overall_total} exceeds configured max-overall {args.max_overall}"
        )

    for marker, limit in marker_thresholds.items():
        marker_total = totals.get(marker, 0)
        if marker_total > limit:
            threshold_errors.append(
                f"marker '{marker}' count {marker_total} exceeds configured max {limit}"
            )

    if threshold_errors:
        print("report_placeholder_markers: threshold check failed", file=sys.stderr)
        for err in threshold_errors:
            print(f"- {err}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
