import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main() -> int:
    errors: list[str] = []
    allowed = {"ALLOW", "ABSTAIN", "DENY", "ERROR"}

    for path in sorted((ROOT / "fixtures/source/hydrology").glob("source_activation_decision*.valid.json")):
        data = json.loads(path.read_text())
        decision = data.get("decision")
        if decision not in allowed:
            errors.append(f"{path.name} invalid decision: {decision}")

    if errors:
        print("FAIL", errors)
        return 1
    print("PASS source activation decisions validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
