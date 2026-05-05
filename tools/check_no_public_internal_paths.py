import json
from pathlib import Path

BAD_PATH_TOKENS = [
    "data/raw",
    "data/work",
    "data/quarantine",
    "steward-only",
    "model-runtime",
    "proof-pack",
    "review-only",
]

# Internal/operational fixture lanes are intentionally allowed to reference
# non-public lifecycle zones for governance tests.
INTERNAL_FIXTURE_MARKERS = {
    "raw_capture_receipts",
    "quarantine",
    "work",
    "processed_support",
    "internal",
}


def is_public_surface_fixture(path: Path) -> bool:
    if "invalid" in path.parts:
        return False
    if "release" in path.parts or "ui" in path.parts or "map" in path.parts or "runtime" in path.parts:
        return True
    if "domains" in path.parts and "hydrology" in path.parts:
        return not any(marker in path.parts for marker in INTERNAL_FIXTURE_MARKERS)
    return True


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

        if not is_public_surface_fixture(path):
            continue

        if any(token in text for token in BAD_PATH_TOKENS):
            violations.append(f"{path}: internal path exposure token")
            continue

        obj = json.loads(text)
        sensitivity = obj.get("sensitivity")
        if sensitivity in {"RESTRICTED", "STEWARD_ONLY"}:
            violations.append(f"{path}: restricted sensitivity cannot be public fixture")
        if obj.get("geometry") and has_precise_coords(obj["geometry"]):
            if obj.get("sensitivity") == "PUBLIC_SAFE" and "domains/hydrology" in str(path):
                # synthetic polygon is allowed for baseline hydrology public-safe fixture.
                pass

    if violations:
        print("FAIL", violations)
        return 1

    print("PASS", "no prohibited internal/public-surface path or sensitivity leakage")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
