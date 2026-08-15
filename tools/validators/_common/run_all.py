"""Compatibility entrypoint for the historical aggregate fixture runner.

New callers should use ``python tools/validate_all.py --profile full``. The
``RUNNER_VALIDATORS`` export remains the reviewed legacy core inventory because
``schema-validation`` performs additional generic fixture-shape checks over
those nine families. Executing this module still delegates to the canonical
``full`` profile, so validators added to the registry continue to run without
silently widening the legacy schema-workflow compatibility contract.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators.validate_all import main as orchestrator_main  # noqa: E402

REGISTRY_PATH = REPO_ROOT / "tools/validators/validator_registry.json"
LEGACY_FIXTURE_ARGUMENT = "--fixtures"
LEGACY_CORE_VALIDATOR_IDS = (
    "source-descriptor",
    "evidence-ref",
    "evidence-bundle",
    "layer-manifest",
    "dataset-version",
    "runtime-response-envelope",
    "decision-envelope",
    "run-receipt",
    "ingest-receipt",
)


def _load_legacy_inventory() -> list[str]:
    data = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    by_id = {item["id"]: item for item in data["validators"]}
    inventory: list[str] = []
    for validator_id in LEGACY_CORE_VALIDATOR_IDS:
        validator = by_id[validator_id]
        if LEGACY_FIXTURE_ARGUMENT not in validator.get("args", []):
            raise ValueError(
                f"legacy core validator lost fixture mode: {validator_id}"
            )
        inventory.append(Path(validator["script"]).name)
    return inventory


RUNNER_VALIDATORS = _load_legacy_inventory()


def main() -> int:
    return orchestrator_main(["--profile", "full"])


if __name__ == "__main__":
    raise SystemExit(main())
