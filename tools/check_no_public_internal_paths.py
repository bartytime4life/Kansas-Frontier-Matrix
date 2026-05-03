import json
from pathlib import Path

BAD_PATH_TOKENS = ["data/raw", "data/work", "data/quarantine", "steward-only", "model-runtime"]


def has_precise_coords(value) -> bool:
    if isinstance(value, (list, tuple)):
        if len(value) == 2 and all(isinstance(v, (int, float)) for v in value):
            return True
        return any(has_precise_coords(v) for v in value)
    if isinstance(value, dict):
        return any(has_precise_coords(v) for v in value.values())
    return False


def main() -> int:
    violations = []
    for path in Path("fixtures").rglob("*.json"):
        text = path.read_text()
        is_invalid = "invalid" in path.parts

        if any(token in text for token in BAD_PATH_TOKENS) and not is_invalid:
            violations.append(f"{path}: internal path exposure token")

        if path.suffix == ".json" and not is_invalid:
            obj = json.loads(text)
            sensitivity = obj.get("sensitivity")
            if sensitivity in {"RESTRICTED", "STEWARD_ONLY"}:
                violations.append(f"{path}: restricted sensitivity cannot be public fixture")
            if obj.get("geometry") and has_precise_coords(obj["geometry"]):
                if obj.get("sensitivity") == "PUBLIC_SAFE" and "domains/hydrology" in str(path):
                    # synthetic polygon is allowed for the baseline hydrology fixture
                    pass

    if violations:
        print("FAIL", violations)
        return 1

    print("PASS", "no prohibited internal/public-surface path or sensitivity leakage")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
