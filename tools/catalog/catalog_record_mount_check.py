#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


TRIPLET = ("stac", "dcat", "prov")


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _first_str(*values: Any) -> str | None:
    for value in values:
        if isinstance(value, str) and value.strip():
            return value
    return None


def _extract_fields(payload: dict[str, Any], lane: str) -> dict[str, str | None]:
    props = payload.get("properties") if isinstance(payload.get("properties"), dict) else {}

    subject = _first_str(
        payload.get("subject_id"),
        payload.get("subject"),
        payload.get("id") if lane == "dcat" else None,
        props.get("subject_id"),
        props.get("kfm:subject_id"),
    )
    version = _first_str(
        payload.get("version"),
        props.get("version"),
        props.get("kfm:version"),
    )
    release_ref = _first_str(
        payload.get("release_ref"),
        props.get("release_ref"),
        props.get("kfm:release_ref"),
    )
    return {"subject_id": subject, "version": version, "release_ref": release_ref}


def _alignment_ok(values: dict[str, str | None]) -> tuple[bool, list[str], list[str]]:
    present = {k: v for k, v in values.items() if v is not None}
    uniques = sorted(set(present.values()))
    return len(values) == len(present) == 3 and len(uniques) == 1, sorted(present.keys()), uniques


def build_report(stac: dict[str, Any], dcat: dict[str, Any], prov: dict[str, Any]) -> dict[str, Any]:
    extracted = {
        "stac": _extract_fields(stac, "stac"),
        "dcat": _extract_fields(dcat, "dcat"),
        "prov": _extract_fields(prov, "prov"),
    }

    checks: list[dict[str, Any]] = []
    errors: list[str] = []

    for field in ("subject_id", "version", "release_ref"):
        values = {lane: extracted[lane][field] for lane in TRIPLET}
        ok, present_lanes, unique_values = _alignment_ok(values)
        if not ok:
            errors.append(f"{field} alignment failed across mounted stac/dcat/prov records")
        checks.append(
            {
                "name": f"mounted_{field}_alignment",
                "ok": ok,
                "values": values,
                "present_lanes": present_lanes,
                "unique_values": unique_values,
            }
        )

    status = "pass" if not errors else "fail"
    return {
        "status": status,
        "blocking": status == "fail",
        "checks": checks,
        "errors": errors,
        "extracted": extracted,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check alignment across mounted STAC/DCAT/PROV records.")
    parser.add_argument("--stac", type=Path, required=True, help="Path to STAC JSON")
    parser.add_argument("--dcat", type=Path, required=True, help="Path to DCAT JSON")
    parser.add_argument("--prov", type=Path, required=True, help="Path to PROV JSON")
    parser.add_argument("--output", type=Path, required=True, help="Path to write report JSON")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = build_report(_read_json(args.stac), _read_json(args.dcat), _read_json(args.prov))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
