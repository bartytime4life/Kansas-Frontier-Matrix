#!/usr/bin/env python3
import argparse
import hashlib
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import jsonschema


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump_json(path: Path, payload: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def stable_id(prefix: str, *parts: str):
    digest = hashlib.sha256("|".join(parts).encode("utf-8")).hexdigest()[:12]
    return f"{prefix}-{digest}"


def validate_schema(doc: dict, schema_path: Path):
    jsonschema.validate(instance=doc, schema=load_json(schema_path))


def gate_eval(qa: dict, receipt_exists: bool, evidence_exists: bool, attestation: dict | None):
    m = qa.get("metrics", {})
    hard_deny = qa.get("aqs_flags_summary", {}).get("hard_denial_rows_in_baseline", 0) > 0
    gates = {
        "gate_a_nowcast_gt_35": {"triggered": m.get("nowcast_max", 0) > 35, "threshold_ug_m3": 35},
        "gate_b_nowcast_vs_baseline_sigma_gt_2": {"triggered": m.get("nowcast_vs_baseline_sigma", 0) > 2, "threshold_sigma": 2},
        "gate_c_station_coverage_lt_75": {"triggered": m.get("station_coverage_pct", 100) < 75, "threshold_pct": 75},
        "gate_d_signed_attestation": {"present": bool(attestation), "required_for_override_or_publication": True},
        "aqs_hard_denial_rows_in_baseline": {"triggered": hard_deny},
        "run_receipt_present": {"triggered": not receipt_exists},
        "evidence_bundle_present": {"triggered": not evidence_exists},
    }
    deny = any([
        gates["gate_a_nowcast_gt_35"]["triggered"],
        gates["gate_b_nowcast_vs_baseline_sigma_gt_2"]["triggered"],
        gates["gate_c_station_coverage_lt_75"]["triggered"],
        gates["aqs_hard_denial_rows_in_baseline"]["triggered"],
        gates["run_receipt_present"]["triggered"],
        gates["evidence_bundle_present"]["triggered"],
    ])
    return deny, gates


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--qa-summary", required=True)
    p.add_argument("--run-receipt", required=True)
    p.add_argument("--out-dir", required=True)
    p.add_argument("--evidence-bundle")
    p.add_argument("--attestation")
    p.add_argument("--allow-quarantine-output", action="store_true")
    args = p.parse_args()

    qa_path = Path(args.qa_summary)
    receipt_path = Path(args.run_receipt)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    qa = load_json(qa_path)
    validate_schema(qa, Path("schemas/contracts/v1/air/qa_summary.schema.json"))

    receipt_exists = receipt_path.exists()
    receipt = load_json(receipt_path) if receipt_exists else None
    att = load_json(Path(args.attestation)) if args.attestation else None

    evidence_path = Path(args.evidence_bundle) if args.evidence_bundle else out_dir / "evidence_bundle.json"
    evidence_exists = evidence_path.exists()
    if not evidence_exists and args.evidence_bundle:
        print("DENY missing evidence bundle", file=sys.stderr)

    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    if not evidence_exists and not args.evidence_bundle:
        evidence = {
            "schema_version": "v1", "bundle_id": stable_id("eb", qa_path.as_posix(), str(qa.get("time_window", {}))),
            "domain": "atmosphere.air", "created_at": now,
            "qa_summary_ref": qa_path.as_posix(), "run_receipt_ref": receipt_path.as_posix(),
            "sources": [{"source_id": "fixture-air", "source_class": "fixture", "note": "Fixture-backed source; NowCast is operational evidence, not validated AQS truth."}],
            "measurements": {"parameter": "pm25", "units": "ug_m3", "averaging_window": qa["aggregation"]["averaging_window"], "nowcast_truth_status": "operational_evidence_not_validated_aqs_truth"},
            "provenance": {"run_id": receipt.get("run_id", "missing") if receipt else "missing", "method": "fixture_release_candidate_builder"}
        }
        dump_json(evidence_path, evidence)
        evidence_exists = True
    evidence = load_json(evidence_path) if evidence_exists else None

    deny, gates = gate_eval(qa, receipt_exists, evidence_exists, att)
    decision_val = "approved_for_catalog"
    if deny:
        decision_val = "quarantine"

    decision = {
        "schema_version": "v1",
        "decision_id": stable_id("pd", qa_path.as_posix(), evidence_path.as_posix(), decision_val),
        "domain": "atmosphere.air",
        "input_qa_summary_ref": qa_path.as_posix(),
        "input_evidence_bundle_ref": evidence_path.as_posix(),
        "run_receipt_ref": receipt_path.as_posix(),
        "decision": decision_val,
        "gates": gates,
        "decided_at": now,
    }
    dump_json(out_dir / "promotion_decision.json", decision)
    validate_schema(decision, Path("schemas/contracts/v1/air/promotion_decision.schema.json"))

    if deny:
        if args.allow_quarantine_output:
            return 0
        return 1

    catalog_dir = out_dir / "catalog_candidate"
    stac_path = catalog_dir / "stac_item.json"
    dcat_path = catalog_dir / "dcat_dataset.json"
    prov_path = catalog_dir / "prov.jsonld"
    triplet_path = catalog_dir / "triplets.jsonl"

    stac = {"id": stable_id("stac", decision["decision_id"]), "type": "Feature", "properties": {"qa_summary_ref": qa_path.as_posix(), "evidence_bundle_ref": evidence_path.as_posix()}}
    dcat = {"id": stable_id("dcat", decision["decision_id"]), "type": "dcat:Dataset", "qa_summary_ref": qa_path.as_posix(), "run_receipt_ref": receipt_path.as_posix()}
    prov = {"@context": "https://www.w3.org/ns/prov#", "entity": {"qa_summary": qa_path.as_posix(), "evidence_bundle": evidence_path.as_posix(), "run_receipt": receipt_path.as_posix()}}

    dump_json(stac_path, stac)
    dump_json(dcat_path, dcat)
    dump_json(prov_path, prov)
    triplet_path.write_text(json.dumps({"s": stac["id"], "p": "derivedFrom", "o": evidence["bundle_id"]}, sort_keys=True) + "\n", encoding="utf-8")

    manifest = {
        "schema_version": "v1",
        "release_id": stable_id("rm", decision["decision_id"]),
        "domain": "atmosphere.air",
        "promotion_decision_ref": (out_dir / "promotion_decision.json").as_posix(),
        "evidence_bundle_ref": evidence_path.as_posix(),
        "run_receipt_ref": receipt_path.as_posix(),
        "catalog_refs": [stac_path.as_posix(), dcat_path.as_posix(), prov_path.as_posix(), triplet_path.as_posix()],
        "artifact_refs": [evidence_path.as_posix(), (out_dir / "promotion_decision.json").as_posix()],
        "public_readiness": {"status": "catalog_candidate", "attestation_required_for_published": True},
    }

    if manifest["public_readiness"]["status"] == "published":
        if decision["decision"] != "approved_for_catalog" or not att:
            raise SystemExit("published status blocked without approval and Gate D attestation")

    dump_json(out_dir / "release_manifest.json", manifest)
    validate_schema(load_json(evidence_path), Path("schemas/contracts/v1/air/evidence_bundle.schema.json"))
    validate_schema(manifest, Path("schemas/contracts/v1/air/release_manifest.schema.json"))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
