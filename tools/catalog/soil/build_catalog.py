#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys
import tempfile
from pathlib import Path
from typing import Any
from urllib.parse import quote

KANSAS_BBOX = [-102.1, 36.9, -94.6, 40.1]
ALLOWED_RIGHTS = {"open", "public", "public_aggregate", "public_safe", "public_reviewed"}


def _safe_id(value: str) -> str:
    clean = re.sub(r"[^A-Za-z0-9._-]", "_", value or "")
    return clean or "bundle"


def _atomic_write(path: Path, payload: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, dir=str(path.parent)) as tmp:
        tmp.write(payload)
        tmp_name = tmp.name
    os.replace(tmp_name, path)


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def _load_and_normalize(path: Path) -> tuple[dict[str, Any], dict[str, Any] | None]:
    obj = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(obj, dict):
        raise ValueError("receipt file must be a JSON object")
    if "run_receipt" in obj:
        run_receipt = obj.get("run_receipt")
        if not isinstance(run_receipt, dict):
            raise ValueError("run_receipt wrapper must contain object")
        evidence_bundle = obj.get("evidence_bundle") if isinstance(obj.get("evidence_bundle"), dict) else None
        return run_receipt, evidence_bundle
    return obj, obj.get("evidence_bundle") if isinstance(obj.get("evidence_bundle"), dict) else None


def _extract(run_receipt: dict[str, Any], evidence_bundle: dict[str, Any] | None) -> dict[str, Any]:
    decision = ((run_receipt.get("validation_summary") or {}).get("decision"))
    if decision != "pass":
        raise ValueError("blocked: validation_summary.decision must be pass")

    artifacts = run_receipt.get("artifacts") if isinstance(run_receipt.get("artifacts"), dict) else {}
    evidence_ref = artifacts.get("evidence_bundle_ref") or run_receipt.get("evidence_bundle_ref")
    if not evidence_ref:
        raise ValueError("blocked: missing evidence_bundle_ref")

    signatures = run_receipt.get("signatures")
    if not isinstance(signatures, list) or len(signatures) == 0:
        raise ValueError("blocked: missing signatures")

    rights_status = str(run_receipt.get("rights_status") or (evidence_bundle or {}).get("rights_status") or "").strip()
    if not rights_status or rights_status == "unknown" or rights_status not in ALLOWED_RIGHTS:
        raise ValueError("blocked: unknown or disallowed rights_status")

    policy_label = str(run_receipt.get("policy_label") or (evidence_bundle or {}).get("policy_label") or "").strip()
    if not policy_label:
        raise ValueError("blocked: missing policy_label")

    sensitivity = str(run_receipt.get("sensitivity") or (evidence_bundle or {}).get("sensitivity") or "public").strip()
    if sensitivity in {"restricted", "private"}:
        raise ValueError("blocked: sensitivity not public-safe")

    bundle_id = str((evidence_bundle or {}).get("bundle_id") or run_receipt.get("bundle_id") or evidence_ref)
    if not bundle_id:
        raise ValueError("blocked: missing bundle_id")

    return {
        "decision": decision,
        "evidence_ref": str(evidence_ref),
        "bundle_id": bundle_id,
        "safe_bundle_id": _safe_id(bundle_id),
        "rights_status": rights_status,
        "policy_label": policy_label,
        "sensitivity": sensitivity,
    }


def _bbox_and_geometry(run_receipt: dict[str, Any]) -> tuple[list[float], dict[str, Any], str | None]:
    bbox = run_receipt.get("bbox")
    geometry_source = None
    if not (isinstance(bbox, list) and len(bbox) == 4):
        bbox = KANSAS_BBOX
        geometry_source = "PROPOSED_fixture_fallback"
    minx, miny, maxx, maxy = [float(x) for x in bbox]
    geometry = {
        "type": "Polygon",
        "coordinates": [[[minx, miny], [maxx, miny], [maxx, maxy], [minx, maxy], [minx, miny]]],
    }
    return [minx, miny, maxx, maxy], geometry, geometry_source


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt", required=True)
    parser.add_argument("--out-root", required=True)
    args = parser.parse_args(argv)

    receipt_path = Path(args.receipt)
    out_root = Path(args.out_root)

    try:
        run_receipt, evidence_bundle = _load_and_normalize(receipt_path)
        meta = _extract(run_receipt, evidence_bundle)
        bbox, geometry, geometry_source = _bbox_and_geometry(run_receipt)

        val = run_receipt.get("validation_summary") if isinstance(run_receipt.get("validation_summary"), dict) else {}
        metrics = run_receipt.get("metrics") if isinstance(run_receipt.get("metrics"), dict) else {}

        props: dict[str, Any] = {
            "kfm:domain": "soil",
            "kfm:evidence_bundle_ref": meta["evidence_ref"],
            "kfm:run_receipt_ref": run_receipt.get("run_receipt_ref") or run_receipt.get("run_receipt_id"),
            "kfm:decision": "pass",
            "kfm:rights_status": meta["rights_status"],
            "kfm:policy_label": meta["policy_label"],
            "kfm:sensitivity": meta["sensitivity"],
            "soil:source": run_receipt.get("soil_source", "SMAP_L4+Mesonet"),
            "soil:aggregation": run_receipt.get("soil_aggregation", "county"),
            "soil:masked_pct": metrics.get("masked_pct"),
            "soil:zscore_30d_max": metrics.get("zscore_30d_max"),
            "soil:station_grid_residual_max": metrics.get("station_grid_residual_max"),
        }
        if geometry_source:
            props["kfm:geometry_source"] = geometry_source
        tw = val.get("time_window") if isinstance(val.get("time_window"), dict) else {}
        if tw.get("start") and tw.get("end"):
            props["start_datetime"] = tw["start"]
            props["end_datetime"] = tw["end"]
        else:
            props["datetime"] = run_receipt.get("datetime") or run_receipt.get("timestamp")

        sid = meta["safe_bundle_id"]
        stac_path = out_root / "catalog" / "stac" / "soil" / f"{sid}.json"
        dcat_path = out_root / "catalog" / "dcat" / "soil" / f"{sid}.jsonld"
        prov_path = out_root / "catalog" / "prov" / "soil" / f"{sid}.jsonld"
        nt_path = out_root / "triplets" / "soil" / f"{sid}.nt"
        receipt_out = out_root / "receipts" / "soil" / f"{sid}.promotion_receipt.json"

        stac = {
            "type": "Feature",
            "stac_version": "1.0.0",
            "id": sid,
            "collection": "soil-moisture",
            "bbox": bbox,
            "geometry": geometry,
            "properties": props,
            "assets": {
                "receipt": {"href": str(receipt_out), "type": "application/json"},
                "evidence_bundle": {"href": meta["evidence_ref"], "type": "application/json"},
            },
        }

        dcat = {
            "@context": {
                "dcat": "http://www.w3.org/ns/dcat#",
                "dct": "http://purl.org/dc/terms/",
                "prov": "http://www.w3.org/ns/prov#",
                "kfm": "https://kfm.example/ns/",
                "soil": "https://kfm.example/soil/",
            },
            "@type": "dcat:Dataset",
            "@id": f"kfm://bundle/{quote(meta['bundle_id'], safe='')}",
            "dct:title": f"KFM Soil Moisture Dataset {sid}",
            "dct:identifier": meta["bundle_id"],
            "dct:license": meta["rights_status"],
            "dct:accessRights": meta["policy_label"],
            "dct:temporal": {"start": tw.get("start"), "end": tw.get("end")},
            "dcat:theme": "soil moisture",
            "prov:wasGeneratedBy": run_receipt.get("process") or "soil.smap_mesonet.ingest",
        }

        prov = {
            "@context": {"prov": "http://www.w3.org/ns/prov#", "kfm": "https://kfm.example/ns/"},
            "@graph": [
                {"@id": f"kfm://bundle/{quote(meta['bundle_id'], safe='')}", "@type": "prov:Entity", "kfm:evidence_bundle_ref": meta["evidence_ref"]},
                {"@id": f"kfm://activity/{quote(str(run_receipt.get('process') or 'soil.smap_mesonet.ingest'), safe='')}", "@type": "prov:Activity", "prov:used": run_receipt.get("source_refs", [])},
                {"@id": "kfm://agent/kfm-ci-steward", "@type": "prov:Agent"},
                {"@id": "kfm://relation/generated", "prov:entity": f"kfm://bundle/{quote(meta['bundle_id'], safe='')}", "prov:activity": f"kfm://activity/{quote(str(run_receipt.get('process') or 'soil.smap_mesonet.ingest'), safe='')}"},
                {"@id": "kfm://relation/associated", "prov:activity": f"kfm://activity/{quote(str(run_receipt.get('process') or 'soil.smap_mesonet.ingest'), safe='')}", "prov:agent": "kfm://agent/kfm-ci-steward"},
            ],
        }

        b_uri = f"<kfm://bundle/{quote(meta['bundle_id'], safe='')}>"
        facts = [
            f"{b_uri} <kfm://predicate/hasDecision> \"pass\" .",
            f"{b_uri} <kfm://predicate/hasDomain> \"soil\" .",
            f"{b_uri} <kfm://predicate/hasEvidenceBundleRef> \"{meta['evidence_ref']}\" .",
            f"{b_uri} <kfm://predicate/hasMetricMaskedPct> \"{metrics.get('masked_pct')}\" .",
            f"{b_uri} <kfm://predicate/hasMetricResidual> \"{metrics.get('station_grid_residual_max')}\" .",
            f"{b_uri} <kfm://predicate/hasMetricZscore30dMax> \"{metrics.get('zscore_30d_max')}\" .",
            f"{b_uri} <kfm://predicate/hasPolicyLabel> \"{meta['policy_label']}\" .",
            f"{b_uri} <kfm://predicate/hasRightsStatus> \"{meta['rights_status']}\" .",
            f"{b_uri} <kfm://predicate/wasGeneratedBy> \"{run_receipt.get('process') or 'soil.smap_mesonet.ingest'}\" .",
        ]
        facts.sort()

        _atomic_write(stac_path, json.dumps(stac, sort_keys=True, indent=2) + "\n")
        _atomic_write(dcat_path, json.dumps(dcat, sort_keys=True, indent=2) + "\n")
        _atomic_write(prov_path, json.dumps(prov, sort_keys=True, indent=2) + "\n")
        _atomic_write(nt_path, "\n".join(facts) + "\n")

        generated = {
            "stac": {"path": str(stac_path), "sha256": _sha256_file(stac_path)},
            "dcat": {"path": str(dcat_path), "sha256": _sha256_file(dcat_path)},
            "prov": {"path": str(prov_path), "sha256": _sha256_file(prov_path)},
            "triplets": {"path": str(nt_path), "sha256": _sha256_file(nt_path)},
        }

        promotion_receipt = {
            "schema_version": "kfm.v1",
            "receipt_type": "PromotionReceipt",
            "from_state": "PROCESSED",
            "to_states": ["CATALOG", "TRIPLET"],
            "decision": "pass",
            "bundle_id": meta["bundle_id"],
            "source_run_receipt_ref": run_receipt.get("run_receipt_ref") or run_receipt.get("run_receipt_id") or _sha256_file(receipt_path),
            "generated_artifacts": generated,
            "policy_checks": {"rights_status": meta["rights_status"], "policy_label": meta["policy_label"], "sensitivity": meta["sensitivity"]},
            "created": dt.datetime.now(dt.timezone.utc).isoformat(),
        }
        _atomic_write(receipt_out, json.dumps(promotion_receipt, sort_keys=True, indent=2) + "\n")

        summary = {
            "promotion_allowed": True,
            "bundle_id": meta["bundle_id"],
            "outputs": {
                **generated,
                "promotion_receipt": {"path": str(receipt_out), "sha256": _sha256_file(receipt_out)},
            },
            "state_transition": "PROCESSED->CATALOG/TRIPLET",
        }
        print(json.dumps(summary, sort_keys=True))
        return 0
    except Exception as exc:
        print(f"catalog generation blocked: {exc}", file=sys.stderr)
        print(json.dumps({"promotion_allowed": False, "error": str(exc), "state_transition": "PROCESSED->CATALOG/TRIPLET"}, sort_keys=True))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
