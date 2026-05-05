import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECEIPT = ROOT / "release/dry_runs/synthetic_release_dry_run_receipt.json"

GATES = [
    ["tools/validate_fixtures.py"],
    ["tools/validate_schema_conformance.py"],
    ["tools/validate_api_contracts.py"],
    ["tools/check_directory_rules.py"],
    ["tools/check_no_public_internal_paths.py"],
    ["tools/validators/validate_evidence_closure.py"],
    ["tools/validators/validate_activation_decisions.py"],
    ["tools/validators/validate_source_terms.py"],
]


def run_gate(args: list[str]) -> dict:
    proc = subprocess.run([sys.executable, str(ROOT / args[0]), *args[1:]], capture_output=True, text=True)
    return {
        "gate": args[0],
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip(),
        "status": "PASS" if proc.returncode == 0 else "FAIL",
    }


def main() -> int:
    gate_results = [run_gate(g) for g in GATES]
    failed = [g for g in gate_results if g["status"] == "FAIL"]

    receipt = {
        "id": "synthetic-release-dry-run-001",
        "mode": "SYNTHETIC_NO_NETWORK",
        "publish_decision": "REFUSE",
        "result": "PASS" if not failed else "FAIL",
        "gates": gate_results,
        "reason": "DRY_RUN_ONLY_REFUSES_PUBLISH",
    }

    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")

    if failed:
        print("FAIL", f"{len(failed)} gates failed; publish refused; receipt={RECEIPT}")
        return 1

    print("PASS", f"all gates passed; publish refused by policy; receipt={RECEIPT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
