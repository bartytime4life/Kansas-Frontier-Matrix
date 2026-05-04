import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from apps.api.kfm_mock_api import focus_decision, get_drawer, get_evidence_bundle

OUTCOMES = {"ANSWER", "ABSTAIN", "DENY", "ERROR"}


def check(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    errors: list[str] = []

    payload, code = get_evidence_bundle("evb-hydro-001")
    check(code == 200 and payload.get("id") == "evb-hydro-001", "known evidence contract mismatch", errors)

    payload, code = get_evidence_bundle("missing")
    check(code == 404 and payload.get("outcome") == "ABSTAIN", "missing evidence should ABSTAIN/404", errors)

    payload, code = get_drawer("missing")
    check(code == 404 and payload.get("outcome") == "ABSTAIN", "missing drawer should ABSTAIN/404", errors)

    answer_payload, answer_code = focus_decision({"question": "Hydrology"})
    check(answer_code == 200 and answer_payload.get("outcome") == "ANSWER", "focus answer outcome mismatch", errors)
    check(bool(answer_payload.get("citations")), "focus ANSWER requires citations", errors)

    deny_payload, deny_code = focus_decision({"question": "sensitive route"})
    check(deny_code == 200 and deny_payload.get("outcome") == "DENY", "sensitive focus should DENY", errors)

    abstain_payload, abstain_code = focus_decision({"question": "   "})
    check(abstain_code == 400 and abstain_payload.get("outcome") == "ABSTAIN", "empty focus should ABSTAIN/400", errors)

    for payload in [answer_payload, deny_payload, abstain_payload]:
        check(payload.get("outcome") in OUTCOMES, "non-finite outcome returned", errors)

    if errors:
        print("FAIL", errors)
        return 1

    print("PASS", "api contract checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
