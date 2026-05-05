import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main() -> int:
    errors: list[str] = []
    evidence_ref = json.loads((ROOT / "fixtures/evidence/evidence_ref.valid.json").read_text())
    bundle = json.loads((ROOT / "fixtures/evidence/evidence_bundle.valid.json").read_text())

    if evidence_ref.get("bundle_id") != bundle.get("id"):
        errors.append("evidence_ref.bundle_id must match evidence_bundle.id")
    if evidence_ref.get("id") not in bundle.get("evidence_refs", []):
        errors.append("evidence_ref.id must be listed in evidence_bundle.evidence_refs")

    if errors:
        print("FAIL", errors)
        return 1
    print("PASS evidence closure validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
