import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from apps.api.kfm_mock_api import focus_decision, get_drawer, get_evidence_bundle

OUTCOMES = {"ANSWER", "ABSTAIN", "DENY", "ERROR"}


def main() -> int:
    errors = []

    payload, code = get_evidence_bundle("evb-hydro-001")
    if code != 200 or payload.get("id") != "evb-hydro-001":
        errors.append("known evidence contract mismatch")

    payload, code = get_evidence_bundle("missing")
    if code != 404 or payload.get("outcome") != "ABSTAIN":
        errors.append("missing evidence should ABSTAIN/404")

    payload, code = get_drawer("missing")
    if code != 404 or payload.get("outcome") != "ABSTAIN":
        errors.append("missing drawer should ABSTAIN/404")

    payload, code = focus_decision({"question": "Hydrology"})
    if code != 200 or payload.get("outcome") != "ANSWER" or not payload.get("citations"):
        errors.append("focus ANSWER requires citations")

    payload, code = focus_decision({"question": "sensitive route"})
    if code != 200 or payload.get("outcome") != "DENY":
        errors.append("sensitive focus should DENY")

    payload, code = focus_decision({"question": "   "})
    if code != 400 or payload.get("outcome") != "ABSTAIN":
        errors.append("empty focus should ABSTAIN/400")

    if any(o.get("outcome") not in OUTCOMES for o in [focus_decision({"question":"Hydrology"})[0], focus_decision({"question":"sensitive route"})[0], focus_decision({"question":" "})[0]]):
        errors.append("non-finite outcome returned")

    if errors:
        print("FAIL", errors)
        return 1
    print("PASS", "api contract checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
