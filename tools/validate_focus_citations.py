import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE_DIR = ROOT / "fixtures/ai"
REASON_REQUIRED_OUTCOMES = {"ABSTAIN", "DENY", "ERROR"}


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _evaluate(obj: dict, valid_citations: set[str]) -> list[str]:
    errors: list[str] = []
    outcome = obj.get("outcome")
    reason = obj.get("reason")
    citations = obj.get("citations", [])

    if outcome == "ANSWER":
        if not citations:
            errors.append("ANSWER must include citations")
        unresolved = [c for c in citations if c not in valid_citations]
        if unresolved:
            errors.append(f"unresolved citations {unresolved}")

    if outcome in REASON_REQUIRED_OUTCOMES:
        if not isinstance(reason, str) or not reason.strip():
            errors.append(f"{outcome} must include non-empty reason code")

    return errors


def main() -> int:
    errors: list[str] = []
    bundle = _load(ROOT / "fixtures/evidence/evidence_bundle.valid.json")
    valid_citations = set(bundle.get("evidence_refs", [])) | {bundle.get("id")}

    for p in sorted(FIXTURE_DIR.glob("focus_citation_*.json")):
        evaluation_errors = _evaluate(_load(p), valid_citations)
        is_invalid_fixture = ".invalid" in p.name

        if is_invalid_fixture and not evaluation_errors:
            errors.append(f"{p}: expected invalid fixture but validation passed")
        if not is_invalid_fixture and evaluation_errors:
            errors.append(f"{p}: expected valid fixture but failed: {evaluation_errors}")

    if errors:
        print("FAIL", errors)
        return 1

    print("PASS", "focus citation validation checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
