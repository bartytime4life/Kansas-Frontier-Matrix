#!/usr/bin/env python3
"""KFM STAC validator.

Validates STAC JSON files and enforces KFM temporal indexing rules.

Outputs:
  - validation_report.json
  - temporal_index_report.json
  - run_receipt.json

Exit codes:
  0 = ANSWER: validation passed
  1 = DENY: validation completed with violations
  2 = ERROR: validator/runtime error
  3 = ABSTAIN: no STAC objects found (unless --allow-empty)
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Optional

TOOL_VERSION = "0.1.0"
OUTCOME_ANSWER = "ANSWER"
OUTCOME_ABSTAIN = "ABSTAIN"
OUTCOME_DENY = "DENY"
OUTCOME_ERROR = "ERROR"

UTC_Z_RE = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z$"
)
# High-confidence timestamps in asset hrefs. Date-only filenames are intentionally
# ignored by default because they are often product IDs rather than acquisition time.
ASSET_TS_PATTERNS = (
    re.compile(r"(?P<ts>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z)"),
    re.compile(r"(?P<ts>\d{8}T\d{6}(?:\.\d+)?Z)"),
)


@dataclass
class Finding:
    severity: str
    code: str
    path: str
    message: str
    stac_id: Optional[str] = None
    field: Optional[str] = None
    value: Any = None

    def as_dict(self) -> dict[str, Any]:
        out = {
            "severity": self.severity,
            "code": self.code,
            "path": self.path,
            "message": self.message,
        }
        if self.stac_id is not None:
            out["id"] = self.stac_id
        if self.field is not None:
            out["field"] = self.field
        if self.value is not None:
            out["value"] = self.value
        return out


@dataclass
class ItemTime:
    item_id: str
    path: str
    collection: Optional[str]
    start: datetime
    end: datetime
    mode: str
    asset_count: int

    def midpoint(self) -> datetime:
        return self.start + (self.end - self.start) / 2

    def as_dict(self) -> dict[str, Any]:
        return {
            "id": self.item_id,
            "path": self.path,
            "collection": self.collection,
            "start": to_z(self.start),
            "end": to_z(self.end),
            "mode": self.mode,
            "asset_count": self.asset_count,
        }


@dataclass
class ScanState:
    root: Path
    started_at: str
    counts: dict[str, int] = field(
        default_factory=lambda: {
            "json_files": 0,
            "items": 0,
            "collections": 0,
            "catalogs": 0,
            "unknown_json": 0,
            "assets": 0,
        }
    )
    extensions: dict[str, int] = field(default_factory=dict)
    findings: list[Finding] = field(default_factory=list)
    items: list[ItemTime] = field(default_factory=list)
    collections: dict[str, dict[str, Any]] = field(default_factory=dict)
    assets_without_detected_time: list[dict[str, Any]] = field(default_factory=list)
    asset_time_drifts: list[dict[str, Any]] = field(default_factory=list)
    collection_extent_checks: list[dict[str, Any]] = field(default_factory=list)
    schema_results: list[dict[str, Any]] = field(default_factory=list)

    def error(self, code: str, path: Path | str, message: str, **kwargs: Any) -> None:
        self.findings.append(
            Finding("error", code, str(path), message, **kwargs)
        )

    def warning(self, code: str, path: Path | str, message: str, **kwargs: Any) -> None:
        self.findings.append(
            Finding("warning", code, str(path), message, **kwargs)
        )

    @property
    def errors(self) -> list[Finding]:
        return [f for f in self.findings if f.severity == "error"]

    @property
    def warnings(self) -> list[Finding]:
        return [f for f in self.findings if f.severity == "warning"]


def to_z(dt: datetime) -> str:
    """Serialize an aware datetime as UTC with trailing Z."""
    return dt.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def parse_utc_z(value: Any) -> Optional[datetime]:
    if not isinstance(value, str) or not UTC_Z_RE.match(value):
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)
    except ValueError:
        return None


def parse_asset_timestamp(value: str) -> Optional[datetime]:
    for pattern in ASSET_TS_PATTERNS:
        match = pattern.search(value)
        if not match:
            continue
        raw = match.group("ts")
        if re.match(r"^\d{8}T\d{6}(?:\.\d+)?Z$", raw):
            # Normalize compact STAC/GDAL-ish timestamp: 20260506T131415Z.
            raw = (
                f"{raw[0:4]}-{raw[4:6]}-{raw[6:8]}T"
                f"{raw[9:11]}:{raw[11:13]}:{raw[13:]}"
            )
        return parse_utc_z(raw)
    return None


def load_json(path: Path) -> tuple[Optional[dict[str, Any]], Optional[str]]:
    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as exc:  # noqa: BLE001 - report exact load failures
        return None, str(exc)
    if not isinstance(data, dict):
        return None, "top-level JSON value is not an object"
    return data, None


def iter_json_files(root: Path) -> Iterable[Path]:
    if root.is_file():
        if root.suffix.lower() == ".json":
            yield root
        return
    yield from sorted(root.rglob("*.json"))


def stac_kind(doc: dict[str, Any]) -> Optional[str]:
    doc_type = doc.get("type")
    if doc_type == "Feature":
        return "item"
    if doc_type == "Collection":
        return "collection"
    if doc_type == "Catalog":
        return "catalog"
    if "stac_version" in doc:
        return "unknown_stac"
    return None


def record_extensions(state: ScanState, doc: dict[str, Any]) -> None:
    exts = doc.get("stac_extensions", [])
    if not isinstance(exts, list):
        return
    for ext in exts:
        if isinstance(ext, str):
            state.extensions[ext] = state.extensions.get(ext, 0) + 1


def validate_schema(state: ScanState, path: Path, doc: dict[str, Any]) -> None:
    try:
        from pystac.validation import validate_dict  # type: ignore
    except Exception as exc:  # noqa: BLE001
        state.error(
            "schema-validator-unavailable",
            path,
            "PySTAC validation is unavailable. Install with: pip install 'pystac[validation]'.",
            value=str(exc),
        )
        return

    try:
        result = validate_dict(doc, href=str(path.resolve()))
        state.schema_results.append(
            {"path": str(path), "status": "pass", "result_count": len(result)}
        )
    except Exception as exc:  # noqa: BLE001 - PySTAC can raise several validation exceptions
        state.schema_results.append({"path": str(path), "status": "fail"})
        state.error(
            "stac-schema-validation-failed",
            path,
            str(exc),
            stac_id=doc.get("id") if isinstance(doc.get("id"), str) else None,
        )


def check_common_stac_fields(state: ScanState, path: Path, doc: dict[str, Any]) -> None:
    if not isinstance(doc.get("stac_version"), str) or not doc.get("stac_version"):
        state.error(
            "missing-stac-version",
            path,
            "STAC object is missing a non-empty stac_version.",
            stac_id=doc.get("id") if isinstance(doc.get("id"), str) else None,
            field="stac_version",
        )
    record_extensions(state, doc)


def check_item(
    state: ScanState,
    path: Path,
    doc: dict[str, Any],
    *,
    asset_time_drift_seconds: int,
    allow_datetime_and_range: bool,
) -> None:
    item_id = doc.get("id") if isinstance(doc.get("id"), str) else None
    props = doc.get("properties")
    assets = doc.get("assets")
    collection = doc.get("collection") if isinstance(doc.get("collection"), str) else None

    if not item_id:
        state.error("missing-item-id", path, "Item id must be a non-empty string.", field="id")
    if doc.get("type") != "Feature":
        state.error("invalid-item-type", path, 'Item type must be "Feature".', stac_id=item_id, field="type")
    if "geometry" not in doc:
        state.error("missing-geometry", path, "Item must include geometry, even when null.", stac_id=item_id, field="geometry")
    if "bbox" not in doc:
        state.error("missing-bbox", path, "Item must include bbox.", stac_id=item_id, field="bbox")
    if not isinstance(props, dict):
        state.error("missing-properties", path, "Item properties must be an object.", stac_id=item_id, field="properties")
        props = {}
    if not isinstance(assets, dict) or len(assets) == 0:
        state.error("missing-assets", path, "Item must contain at least one asset.", stac_id=item_id, field="assets")
        assets = {}

    state.counts["assets"] += len(assets)

    item_time = check_item_time(
        state,
        path,
        item_id or "<missing-id>",
        collection,
        props,
        len(assets),
        allow_datetime_and_range=allow_datetime_and_range,
    )
    if item_time is not None:
        state.items.append(item_time)
        check_asset_times(
            state,
            path,
            item_id or "<missing-id>",
            item_time,
            assets,
            drift_seconds=asset_time_drift_seconds,
        )


def check_item_time(
    state: ScanState,
    path: Path,
    item_id: str,
    collection: Optional[str],
    props: dict[str, Any],
    asset_count: int,
    *,
    allow_datetime_and_range: bool,
) -> Optional[ItemTime]:
    has_datetime_key = "datetime" in props
    datetime_value = props.get("datetime")
    start_value = props.get("start_datetime")
    end_value = props.get("end_datetime")
    has_range = start_value is not None or end_value is not None

    if not has_datetime_key and not has_range:
        state.error(
            "missing-time",
            path,
            "Item must have properties.datetime or properties.start_datetime/properties.end_datetime.",
            stac_id=item_id,
            field="properties.datetime",
        )
        return None

    if datetime_value is not None:
        if has_range and not allow_datetime_and_range:
            state.error(
                "temporal-mode-conflict",
                path,
                "KFM expects exactly one temporal mode: datetime OR start_datetime/end_datetime.",
                stac_id=item_id,
                field="properties.datetime",
            )
        dt = parse_utc_z(datetime_value)
        if dt is None:
            state.error(
                "invalid-datetime",
                path,
                "properties.datetime must be RFC 3339 UTC with trailing Z.",
                stac_id=item_id,
                field="properties.datetime",
                value=datetime_value,
            )
            return None
        return ItemTime(item_id, str(path), collection, dt, dt, "datetime", asset_count)

    # datetime is null or absent, so require a bounded range.
    start = parse_utc_z(start_value)
    end = parse_utc_z(end_value)
    if start is None:
        state.error(
            "invalid-start-datetime",
            path,
            "properties.start_datetime must be RFC 3339 UTC with trailing Z when datetime is null or absent.",
            stac_id=item_id,
            field="properties.start_datetime",
            value=start_value,
        )
    if end is None:
        state.error(
            "invalid-end-datetime",
            path,
            "properties.end_datetime must be RFC 3339 UTC with trailing Z when datetime is null or absent.",
            stac_id=item_id,
            field="properties.end_datetime",
            value=end_value,
        )
    if start is None or end is None:
        return None
    if end < start:
        state.error(
            "temporal-range-inverted",
            path,
            "properties.end_datetime must be greater than or equal to properties.start_datetime.",
            stac_id=item_id,
            field="properties.end_datetime",
            value={"start_datetime": start_value, "end_datetime": end_value},
        )
        return None
    return ItemTime(item_id, str(path), collection, start, end, "range", asset_count)


def check_asset_times(
    state: ScanState,
    path: Path,
    item_id: str,
    item_time: ItemTime,
    assets: dict[str, Any],
    *,
    drift_seconds: int,
) -> None:
    for asset_key, asset in assets.items():
        if not isinstance(asset, dict):
            continue
        href = asset.get("href")
        if not isinstance(href, str):
            state.warning(
                "asset-missing-href",
                path,
                "Asset has no href; cannot compare asset timestamp.",
                stac_id=item_id,
                field=f"assets.{asset_key}.href",
            )
            continue
        asset_dt = parse_asset_timestamp(href)
        if asset_dt is None:
            state.assets_without_detected_time.append(
                {"item_id": item_id, "asset_key": asset_key, "path": str(path), "href": href}
            )
            continue

        if item_time.mode == "range":
            in_range = item_time.start <= asset_dt <= item_time.end
            drift = 0 if in_range else min(
                abs((asset_dt - item_time.start).total_seconds()),
                abs((asset_dt - item_time.end).total_seconds()),
            )
        else:
            drift = abs((asset_dt - item_time.start).total_seconds())

        if drift > drift_seconds:
            drift_record = {
                "item_id": item_id,
                "asset_key": asset_key,
                "path": str(path),
                "href": href,
                "asset_time": to_z(asset_dt),
                "item_start": to_z(item_time.start),
                "item_end": to_z(item_time.end),
                "drift_seconds": int(drift),
                "allowed_drift_seconds": drift_seconds,
            }
            state.asset_time_drifts.append(drift_record)
            state.error(
                "asset-time-drift",
                path,
                "Timestamp parsed from asset href is outside the allowed drift from item temporal metadata.",
                stac_id=item_id,
                field=f"assets.{asset_key}.href",
                value=drift_record,
            )


def check_collection(state: ScanState, path: Path, doc: dict[str, Any]) -> None:
    collection_id = doc.get("id") if isinstance(doc.get("id"), str) else None
    if not collection_id:
        state.error("missing-collection-id", path, "Collection id must be a non-empty string.", field="id")
        return
    if not isinstance(doc.get("license"), str) or not doc.get("license"):
        state.error("missing-license", path, "Collection must declare a non-empty license.", stac_id=collection_id, field="license")

    extent = doc.get("extent")
    if not isinstance(extent, dict):
        state.error("missing-extent", path, "Collection must include extent.", stac_id=collection_id, field="extent")
        state.collections[collection_id] = {"path": str(path), "temporal_intervals": []}
        return

    spatial = extent.get("spatial")
    temporal = extent.get("temporal")
    if not isinstance(spatial, dict) or not isinstance(spatial.get("bbox"), list) or not spatial.get("bbox"):
        state.error("missing-spatial-extent", path, "Collection extent.spatial.bbox must be non-empty.", stac_id=collection_id, field="extent.spatial.bbox")

    temporal_intervals: list[tuple[Optional[datetime], Optional[datetime]]] = []
    if not isinstance(temporal, dict) or not isinstance(temporal.get("interval"), list) or not temporal.get("interval"):
        state.error("missing-temporal-extent", path, "Collection extent.temporal.interval must be non-empty.", stac_id=collection_id, field="extent.temporal.interval")
    else:
        for idx, raw_interval in enumerate(temporal.get("interval", [])):
            parsed = parse_collection_interval(raw_interval)
            if parsed is None:
                state.error(
                    "invalid-temporal-extent",
                    path,
                    "Collection temporal intervals must be [start, end] with UTC Z timestamps or null open bounds.",
                    stac_id=collection_id,
                    field=f"extent.temporal.interval.{idx}",
                    value=raw_interval,
                )
                continue
            start, end = parsed
            if start is not None and end is not None and end < start:
                state.error(
                    "temporal-extent-inverted",
                    path,
                    "Collection temporal interval end must be greater than or equal to start.",
                    stac_id=collection_id,
                    field=f"extent.temporal.interval.{idx}",
                    value=raw_interval,
                )
                continue
            temporal_intervals.append(parsed)

    state.collections[collection_id] = {
        "path": str(path),
        "temporal_intervals": temporal_intervals,
    }


def parse_collection_interval(raw: Any) -> Optional[tuple[Optional[datetime], Optional[datetime]]]:
    if not isinstance(raw, list) or len(raw) != 2:
        return None
    start_raw, end_raw = raw
    start = None if start_raw is None else parse_utc_z(start_raw)
    end = None if end_raw is None else parse_utc_z(end_raw)
    if start_raw is not None and start is None:
        return None
    if end_raw is not None and end is None:
        return None
    return start, end


def check_collection_coverage(state: ScanState) -> None:
    by_collection: dict[str, list[ItemTime]] = {}
    for item in state.items:
        if item.collection:
            by_collection.setdefault(item.collection, []).append(item)

    for collection_id, items in by_collection.items():
        collection = state.collections.get(collection_id)
        if collection is None:
            state.warning(
                "collection-not-found",
                state.root,
                "Items reference a collection id that was not found in the scanned tree.",
                stac_id=collection_id,
                value={"item_count": len(items)},
            )
            continue

        intervals = collection.get("temporal_intervals") or []
        item_min = min(item.start for item in items)
        item_max = max(item.end for item in items)
        covered = any(
            (start is None or item_min >= start) and (end is None or item_max <= end)
            for start, end in intervals
        )
        check = {
            "collection_id": collection_id,
            "collection_path": collection["path"],
            "item_count": len(items),
            "item_min_start": to_z(item_min),
            "item_max_end": to_z(item_max),
            "covered": covered,
            "intervals": [
                [None if start is None else to_z(start), None if end is None else to_z(end)]
                for start, end in intervals
            ],
        }
        state.collection_extent_checks.append(check)
        if not covered:
            state.error(
                "collection-temporal-extent-undercoverage",
                collection["path"],
                "Collection temporal extent does not cover all scanned member Items.",
                stac_id=collection_id,
                field="extent.temporal.interval",
                value=check,
            )


def build_validation_report(state: ScanState, finished_at: str) -> dict[str, Any]:
    return {
        "schema_version": "kfm.stac.validation_report.v1",
        "tool_version": TOOL_VERSION,
        "root": str(state.root),
        "checked_at": finished_at,
        "passed": not state.errors,
        "counts": state.counts,
        "extension_coverage": dict(sorted(state.extensions.items())),
        "schema_results": state.schema_results,
        "errors": [f.as_dict() for f in state.errors],
        "warnings": [f.as_dict() for f in state.warnings],
    }


def build_temporal_report(state: ScanState, recent: int, finished_at: str) -> dict[str, Any]:
    newest = sorted(state.items, key=lambda x: x.end, reverse=True)[:recent]
    return {
        "schema_version": "kfm.stac.temporal_index_report.v1",
        "tool_version": TOOL_VERSION,
        "root": str(state.root),
        "checked_at": finished_at,
        "newest_items": [item.as_dict() for item in newest],
        "items_indexed": len(state.items),
        "missing_or_invalid_time": [
            f.as_dict()
            for f in state.findings
            if f.code
            in {
                "missing-time",
                "invalid-datetime",
                "invalid-start-datetime",
                "invalid-end-datetime",
                "temporal-range-inverted",
                "temporal-mode-conflict",
            }
        ],
        "assets_without_detected_time": state.assets_without_detected_time,
        "asset_time_drifts": state.asset_time_drifts,
        "collection_extent_checks": state.collection_extent_checks,
    }


def build_receipt(
    *,
    state: ScanState,
    outcome: str,
    started_monotonic: float,
    finished_at: str,
    args: argparse.Namespace,
    exit_code: int,
) -> dict[str, Any]:
    policy = {
        "tool_version": TOOL_VERSION,
        "root": str(state.root),
        "skip_schema": args.skip_schema,
        "allow_non_stac_json": args.allow_non_stac_json,
        "allow_datetime_and_range": args.allow_datetime_and_range,
        "asset_time_drift_seconds": args.asset_time_drift_seconds,
        "fail_on_warnings": args.fail_on_warnings,
    }
    spec_hash = hashlib.sha256(
        json.dumps(policy, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    return {
        "schema_version": "kfm.run_receipt.v1",
        "tool": "tools/validators/stac_validate.py",
        "tool_version": TOOL_VERSION,
        "outcome": outcome,
        "exit_code": exit_code,
        "input_path": str(state.root),
        "reports_dir": str(args.reports_dir),
        "spec_hash": spec_hash,
        "started_at": state.started_at,
        "finished_at": finished_at,
        "wall_ms": int((time.monotonic() - started_monotonic) * 1000),
        "counts": state.counts,
        "error_count": len(state.errors),
        "warning_count": len(state.warnings),
    }


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=True)
        f.write("\n")


def emit_github_annotations(state: ScanState) -> None:
    if os.environ.get("GITHUB_ACTIONS") != "true":
        return
    for finding in state.findings:
        level = "error" if finding.severity == "error" else "warning"
        msg = finding.message.replace("\n", " ").replace("%", "%25").replace("\r", "%0D")
        print(
            f"::{level} file={finding.path},title={finding.code}::{msg}",
            file=sys.stderr,
        )


def scan(args: argparse.Namespace) -> ScanState:
    root = Path(args.root)
    state = ScanState(root=root, started_at=to_z(datetime.now(timezone.utc)))

    if not root.exists():
        state.error("input-path-not-found", root, "Input path does not exist.")
        return state

    for path in iter_json_files(root):
        rel_path = path.relative_to(root) if root.is_dir() else path
        display_path = root / rel_path if root.is_dir() else path
        state.counts["json_files"] += 1
        doc, err = load_json(path)
        if doc is None:
            state.error("json-load-failed", display_path, f"Could not read JSON: {err}")
            continue

        kind = stac_kind(doc)
        if kind is None:
            state.counts["unknown_json"] += 1
            if not args.allow_non_stac_json:
                state.error(
                    "non-stac-json",
                    display_path,
                    "JSON file is not a STAC Catalog, Collection, or Item.",
                )
            else:
                state.warning(
                    "non-stac-json-skipped",
                    display_path,
                    "JSON file is not a STAC Catalog, Collection, or Item; skipped.",
                )
            continue
        if kind == "unknown_stac":
            state.counts["unknown_json"] += 1
            state.error(
                "unknown-stac-object",
                display_path,
                "JSON contains stac_version but is not a recognized STAC Catalog, Collection, or Item.",
                stac_id=doc.get("id") if isinstance(doc.get("id"), str) else None,
            )
            continue

        check_common_stac_fields(state, display_path, doc)
        if not args.skip_schema:
            validate_schema(state, display_path, doc)

        if kind == "item":
            state.counts["items"] += 1
            check_item(
                state,
                display_path,
                doc,
                asset_time_drift_seconds=args.asset_time_drift_seconds,
                allow_datetime_and_range=args.allow_datetime_and_range,
            )
        elif kind == "collection":
            state.counts["collections"] += 1
            check_collection(state, display_path, doc)
        elif kind == "catalog":
            state.counts["catalogs"] += 1

    check_collection_coverage(state)
    return state


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate STAC conformance and KFM temporal indexing rules.")
    parser.add_argument("root", nargs="?", default="data/catalog/stac", help="STAC catalog file or directory to scan.")
    parser.add_argument("--reports-dir", default="artifacts/stac-validation", help="Directory for JSON reports.")
    parser.add_argument("--recent", type=int, default=50, help="Number of newest items to include in temporal report.")
    parser.add_argument("--asset-time-drift-seconds", type=int, default=3600, help="Allowed drift for high-confidence timestamps parsed from asset hrefs.")
    parser.add_argument("--skip-schema", action="store_true", help="Skip PySTAC JSON-schema validation. Intended for local smoke tests only.")
    parser.add_argument("--allow-empty", action="store_true", help="Return ANSWER when no STAC objects are found.")
    parser.add_argument("--allow-non-stac-json", action="store_true", help="Skip unrelated JSON files under the root instead of failing.")
    parser.add_argument("--allow-datetime-and-range", action="store_true", help="Allow Items to include both datetime and start/end range metadata.")
    parser.add_argument("--fail-on-warnings", action="store_true", help="Treat warnings as DENY.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    started_monotonic = time.monotonic()
    args = parse_args(argv)
    args.reports_dir = Path(args.reports_dir)

    try:
        state = scan(args)
        finished_at = to_z(datetime.now(timezone.utc))

        stac_object_count = state.counts["items"] + state.counts["collections"] + state.counts["catalogs"]
        if stac_object_count == 0 and not args.allow_empty:
            state.error(
                "no-stac-objects-found",
                state.root,
                "No STAC Catalog, Collection, or Item JSON objects were found.",
            )
            outcome = OUTCOME_ABSTAIN
            exit_code = 3
        elif state.errors or (args.fail_on_warnings and state.warnings):
            outcome = OUTCOME_DENY
            exit_code = 1
        else:
            outcome = OUTCOME_ANSWER
            exit_code = 0

        validation_report = build_validation_report(state, finished_at)
        temporal_report = build_temporal_report(state, args.recent, finished_at)
        receipt = build_receipt(
            state=state,
            outcome=outcome,
            started_monotonic=started_monotonic,
            finished_at=finished_at,
            args=args,
            exit_code=exit_code,
        )

        write_json(args.reports_dir / "validation_report.json", validation_report)
        write_json(args.reports_dir / "temporal_index_report.json", temporal_report)
        write_json(args.reports_dir / "run_receipt.json", receipt)
        emit_github_annotations(state)

        print(
            f"KFM STAC validation outcome={outcome} "
            f"items={state.counts['items']} collections={state.counts['collections']} "
            f"catalogs={state.counts['catalogs']} errors={len(state.errors)} warnings={len(state.warnings)} "
            f"reports={args.reports_dir}"
        )
        return exit_code
    except Exception as exc:  # noqa: BLE001 - write ERROR receipt whenever possible
        finished_at = to_z(datetime.now(timezone.utc))
        fallback_state = ScanState(root=Path(args.root), started_at=finished_at)
        fallback_state.error("validator-runtime-error", args.root, str(exc))
        args.reports_dir.mkdir(parents=True, exist_ok=True)
        receipt = build_receipt(
            state=fallback_state,
            outcome=OUTCOME_ERROR,
            started_monotonic=started_monotonic,
            finished_at=finished_at,
            args=args,
            exit_code=2,
        )
        write_json(args.reports_dir / "run_receipt.json", receipt)
        write_json(args.reports_dir / "validation_report.json", build_validation_report(fallback_state, finished_at))
        write_json(args.reports_dir / "temporal_index_report.json", build_temporal_report(fallback_state, args.recent, finished_at))
        print(f"KFM STAC validation outcome={OUTCOME_ERROR} error={exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
