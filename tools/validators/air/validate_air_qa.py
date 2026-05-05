#!/usr/bin/env python3
import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

try:
    import jsonschema
except Exception:
    jsonschema = None


def local_policy_denies(doc):
    denies = []
    m = doc.get("metrics", {})
    if m.get("nowcast_max", 0) > 35:
        denies.append("gate_a_nowcast_max_exceeds_35")
    if m.get("nowcast_vs_baseline_sigma", 0) > 2:
        denies.append("gate_b_nowcast_vs_baseline_sigma_exceeds_2")
    if m.get("station_coverage_pct", 100) < 75:
        denies.append("gate_c_station_coverage_below_75")
    if doc.get("aqs_flags_summary", {}).get("hard_denial_rows_in_baseline", 0) > 0:
        denies.append("aqs_hard_denial_rows_present_in_baseline")
    if doc.get("decision") == "candidate":
        flags = doc.get("flags", {})
        if not flags.get("run_receipt_ref"):
            denies.append("missing_run_receipt_ref_for_public_promotion")
        if not flags.get("evidence_bundle_ref"):
            denies.append("missing_evidence_bundle_ref_for_public_promotion")
    return denies


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputs", nargs="+")
    parser.add_argument("--schema", default="schemas/contracts/v1/air/qa_summary.schema.json")
    parser.add_argument("--policy", default="policy/air/air_qa.rego")
    args = parser.parse_args()

    schema = json.loads(Path(args.schema).read_text(encoding="utf-8"))
    ok = True
    opa = shutil.which("conftest")

    for p in args.inputs:
        path = Path(p)
        doc = json.loads(path.read_text(encoding="utf-8"))

        if jsonschema is None:
            print(f"DENY {p} schema=unavailable(jsonschema missing)")
            ok = False
            continue

        try:
            jsonschema.validate(instance=doc, schema=schema)
        except jsonschema.ValidationError as exc:
            print(f"DENY {p} schema={exc.message}")
            ok = False
            continue

        denies = []
        if opa:
            proc = subprocess.run(
                [opa, "test", "--policy", args.policy, p], capture_output=True, text=True
            )
            if proc.returncode != 0:
                denies = local_policy_denies(doc)
            else:
                denies = local_policy_denies(doc)
        else:
            denies = local_policy_denies(doc)

        if denies:
            print(f"DENY {p} policy={';'.join(denies)}")
            ok = False
        else:
            print(f"PASS {p}")

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
