#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


TRIPLET_KEYS = ("stac", "dcat", "prov")


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _extract_triplet(payload: dict[str, Any]) -> dict[str, dict[str, Any]]:
    if isinstance(payload.get("catalog_refs"), dict):
        refs = payload["catalog_refs"]
    elif isinstance(payload.get("catalog"), dict) and isinstance(payload["catalog"].get("refs"), dict):
        refs = payload["catalog"]["refs"]
    else:
        refs = {}

    triplet: dict[str, dict[str, Any]] = {}
    for key in TRIPLET_KEYS:
        value = refs.get(key)
        if isinstance(value, dict):
            triplet[key] = value
    return triplet


def _extract_release_ref(payload: dict[str, Any]) -> str | None:
    for candidate in (
        payload.get("release_ref"),
        payload.get("release", {}).get("ref") if isinstance(payload.get("release"), dict) else None,
    ):
        if isinstance(candidate, str) and candidate:
            return candidate
    return None


def _field(value: dict[str, Any], name: str) -> str | None:
    raw = value.get(name)
    return raw if isinstance(raw, str) and raw else None


def build_report(decision: dict[str, Any], record: dict[str, Any]) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    errors: list[str] = []

    decision_triplet = _extract_triplet(decision)
    record_triplet = _extract_triplet(record)
    triplet = decision_triplet or record_triplet

    decision_record_consistent = True
    for key in TRIPLET_KEYS:
        d_value = decision_triplet.get(key)
        r_value = record_triplet.get(key)
        if d_value and r_value:
            for field_name in ("subject_id", "version", "release_ref"):
                d_field = _field(d_value, field_name)
                r_field = _field(r_value, field_name)
                if d_field is not None and r_field is not None and d_field != r_field:
                    decision_record_consistent = False

    if not decision_record_consistent:
        errors.append("decision/record catalog triplet mismatch detected")
    checks.append(
        {
            "name": "decision_record_triplet_alignment",
            "ok": decision_record_consistent,
        }
    )

    missing_refs = [key for key in TRIPLET_KEYS if key not in triplet]
    if missing_refs:
        errors.append(f"missing catalog refs: {', '.join(missing_refs)}")
    checks.append(
        {
            "name": "triplet_ref_presence",
            "ok": not missing_refs,
            "missing": missing_refs,
        }
    )

    subjects = {_field(triplet.get(key, {}), "subject_id") for key in TRIPLET_KEYS if key in triplet}
    subjects.discard(None)
    subject_ok = len(subjects) == 1 and len(triplet) == 3
    if not subject_ok:
        errors.append("subject alignment failed across stac/dcat/prov")
    checks.append({"name": "subject_alignment", "ok": subject_ok, "subjects": sorted(subjects)})

    versions = {_field(triplet.get(key, {}), "version") for key in TRIPLET_KEYS if key in triplet}
    versions.discard(None)
    version_ok = len(versions) == 1 and len(triplet) == 3
    if not version_ok:
        errors.append("version alignment failed across stac/dcat/prov")
    checks.append({"name": "version_alignment", "ok": version_ok, "versions": sorted(versions)})

    decision_release_ref = _extract_release_ref(decision)
    record_release_ref = _extract_release_ref(record)
    triplet_release_refs = {
        _field(triplet.get(key, {}), "release_ref") for key in TRIPLET_KEYS if key in triplet
    }
    triplet_release_refs.discard(None)

    release_ok = (
        decision_release_ref is not None
        and record_release_ref is not None
        and len(triplet_release_refs) == 1
        and decision_release_ref == record_release_ref == next(iter(triplet_release_refs))
    )

    if not release_ok:
        errors.append("release-ref alignment failed between decision, record, and catalog triplet")

    checks.append(
        {
            "name": "release_ref_alignment",
            "ok": release_ok,
            "decision_release_ref": decision_release_ref,
            "record_release_ref": record_release_ref,
            "triplet_release_refs": sorted(triplet_release_refs),
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
    parser = argparse.ArgumentParser(description="Cross-link STAC/DCAT/PROV refs for catalog closure.")
    parser.add_argument("--decision", required=True, type=Path, help="Path to decision JSON")
    parser.add_argument("--record", required=True, type=Path, help="Path to promotion record JSON")
    parser.add_argument("--output", required=True, type=Path, help="Path to output report JSON")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    decision = _read_json(args.decision)
    record = _read_json(args.record)
    report = build_report(decision, record)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
