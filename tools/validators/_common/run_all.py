"""Compatibility entrypoint for the historical aggregate fixture runner.

New callers should use ``python tools/validate_all.py --profile full``. The
``RUNNER_VALIDATORS`` export remains the reviewed legacy core inventory because
``schema-validation`` performs additional generic fixture-shape checks over
those nine families. Executing this module uses the canonical orchestrator with
an explicit nine-validator selection; catalog and repository guardrail
validators remain in the canonical ``full`` profile without silently widening
historical ``make schemas`` semantics.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators.validate_all import load_registry, orchestrate  # noqa: E402

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
    present_core = [item for item in LEGACY_CORE_VALIDATOR_IDS if item in by_id]
    if present_core and len(present_core) != len(LEGACY_CORE_VALIDATOR_IDS):
        missing = sorted(set(LEGACY_CORE_VALIDATOR_IDS) - set(present_core))
        raise ValueError(f"legacy core validator inventory is incomplete: {missing}")

    validator_ids = (
        LEGACY_CORE_VALIDATOR_IDS
        if present_core
        else tuple(
            item["id"]
            for item in data["validators"]
            if LEGACY_FIXTURE_ARGUMENT in item.get("args", [])
        )
    )
    inventory: list[str] = []
    for validator_id in validator_ids:
        validator = by_id[validator_id]
        if LEGACY_FIXTURE_ARGUMENT not in validator.get("args", []):
            raise ValueError(
                f"legacy core validator lost fixture mode: {validator_id}"
            )
        inventory.append(Path(validator["script"]).name)
    return inventory


RUNNER_VALIDATORS = _load_legacy_inventory()


def main() -> int:
    registry = load_registry(REGISTRY_PATH, REPO_ROOT)
    code, report = orchestrate(
        registry,
        repo_root=REPO_ROOT,
        profile="full",
        requested_ids=LEGACY_CORE_VALIDATOR_IDS,
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
