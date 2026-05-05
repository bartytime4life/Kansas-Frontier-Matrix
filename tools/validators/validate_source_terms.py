import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main() -> int:
    errors: list[str] = []
    review = json.loads((ROOT / "fixtures/source/hydrology/source_terms_review.valid.json").read_text())
    receipt = json.loads((ROOT / "fixtures/source/hydrology/source_terms_check_receipt.wbd.no_network.valid.json").read_text())

    if review.get("rights_status") not in {"NEEDS_LEGAL_REVIEW", "CLEARED", "DENIED"}:
        errors.append("source_terms_review has invalid rights_status")
    if receipt.get("check_kind") != "TERMS_RIGHTS_ONLY":
        errors.append("source_terms_check_receipt must be TERMS_RIGHTS_ONLY")
    if receipt.get("network_mode") != "DISABLED":
        errors.append("source_terms_check_receipt network_mode must be DISABLED")
    if receipt.get("validation_result") not in {"ALLOW", "ABSTAIN", "DENY", "ERROR"}:
        errors.append("source_terms_check_receipt has invalid validation_result")

    if errors:
        print("FAIL", errors)
        return 1
    print("PASS source terms fixtures validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
