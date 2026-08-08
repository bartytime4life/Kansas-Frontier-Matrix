"""Compatibility entrypoint for the historical aggregate fixture runner.

New callers should use ``python tools/validate_all.py --profile full``.  The
``RUNNER_VALIDATORS`` export and the literal ``"--fixtures"`` remain because
the existing validator-suite workflow verifies that compatibility surface.
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


def _load_legacy_inventory() -> list[str]:
    data = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    by_id = {item["id"]: item for item in data["validators"]}
    return [Path(by_id[item]["script"]).name for item in data["profiles"]["full"]]


RUNNER_VALIDATORS = _load_legacy_inventory()


def main() -> int:
    return orchestrator_main(["--profile", "full"])


if __name__ == "__main__":
    raise SystemExit(main())
