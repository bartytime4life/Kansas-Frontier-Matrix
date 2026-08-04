import subprocess
import sys
from pathlib import Path


# Execute the bounded top-level validators that expose deterministic fixture mode.
# Placeholder validator stubs intentionally raising NotImplementedError are excluded.
RUNNER_VALIDATORS = [
    "validate_source_descriptor.py",
    "validate_evidence_ref.py",
    "validate_evidence_bundle.py",
    "validate_runtime_response_envelope.py",
    "validate_decision_envelope.py",
    "validate_run_receipt.py",
    "validate_ingest_receipt.py",
]


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    for filename in RUNNER_VALIDATORS:
        script = root / filename
        cmd = [sys.executable, str(script), "--fixtures"]
        result = subprocess.run(cmd)
        if result.returncode != 0:
            return result.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
