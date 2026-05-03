import json
from datetime import datetime, timezone
from pathlib import Path

FIXTURE = Path("fixtures/release/release_manifest.valid.json")
OUTPUT = Path("release/dry_runs/promotion_dry_run_receipt.json")


def main() -> int:
    manifest = json.loads(FIXTURE.read_text())
    errors = []

    if not manifest.get("rollback_target"):
        errors.append("missing rollback_target")
    if not manifest.get("correction_route"):
        errors.append("missing correction_route")
    if manifest.get("release_state") not in {"RELEASE_CANDIDATE", "PUBLISHED", "SUPERSEDED", "WITHDRAWN"}:
        errors.append("release_state not promotable in dry run")

    receipt = {
        "id": "promotion-dry-run-001",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "source_manifest": str(FIXTURE),
        "result": "PASS" if not errors else "FAIL",
        "errors": errors,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(receipt, indent=2))

    if errors:
        print("FAIL", errors)
        return 1
    print("PASS", f"dry run receipt written to {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
