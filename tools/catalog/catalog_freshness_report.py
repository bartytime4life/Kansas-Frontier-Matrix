#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Any


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _first_str(*values: Any) -> str | None:
    for value in values:
        if isinstance(value, str) and value.strip():
            return value
    return None


def _parse_date(raw: str | None) -> datetime | None:
    if raw is None:
        return None
    try:
        return datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError:
        return None


def _extract_timestamp(payload: dict[str, Any]) -> str | None:
    props = payload.get("properties") if isinstance(payload.get("properties"), dict) else {}
    return _first_str(
        payload.get("updated"),
        payload.get("modified"),
        payload.get("generated_at"),
        props.get("updated"),
        props.get("modified"),
        props.get("generated_at"),
        props.get("kfm:generated_at"),
    )


def build_report(stac: dict[str, Any], dcat: dict[str, Any], prov: dict[str, Any], max_spread_days: int) -> dict[str, Any]:
    raw = {
        "stac": _extract_timestamp(stac),
        "dcat": _extract_timestamp(dcat),
        "prov": _extract_timestamp(prov),
    }
    parsed = {k: _parse_date(v) for k, v in raw.items()}

    errors: list[str] = []
    checks: list[dict[str, Any]] = []

    complete = all(parsed.values())
    if not complete:
        errors.append("missing or invalid freshness timestamp in mounted catalog records")
    checks.append({"name": "timestamp_presence", "ok": complete, "timestamps": raw})

    spread_ok = False
    spread_days: float | None = None
    if complete:
        values = list(parsed.values())
        assert all(v is not None for v in values)
        oldest = min(values)
        newest = max(values)
        spread_days = (newest - oldest).total_seconds() / 86400
        spread_ok = spread_days <= max_spread_days
        if not spread_ok:
            errors.append("catalog freshness spread exceeds max-spread-days threshold")
    checks.append(
        {
            "name": "freshness_spread",
            "ok": spread_ok,
            "spread_days": spread_days,
            "max_spread_days": max_spread_days,
        }
    )

    status = "pass" if not errors else "fail"
    return {
        "status": status,
        "blocking": status == "fail",
        "checks": checks,
        "errors": errors,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build freshness report from mounted STAC/DCAT/PROV records.")
    parser.add_argument("--stac", type=Path, required=True)
    parser.add_argument("--dcat", type=Path, required=True)
    parser.add_argument("--prov", type=Path, required=True)
    parser.add_argument("--max-spread-days", type=int, default=30)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = build_report(
        _read_json(args.stac),
        _read_json(args.dcat),
        _read_json(args.prov),
        args.max_spread_days,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
