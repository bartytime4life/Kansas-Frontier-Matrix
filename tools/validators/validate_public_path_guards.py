import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FORBIDDEN = ["data/raw/", "data/work/", "data/quarantine/", "data/processed/"]
TARGETS = [
    "fixtures/ui/evidence_drawer_payload.valid.json",
    "fixtures/ai/focus_mode_response.answer.valid.json",
    "fixtures/release/release_manifest.valid.json",
]


def main() -> int:
    errors: list[str] = []
    for rel in TARGETS:
        text = json.dumps(json.loads((ROOT / rel).read_text())).lower()
        for bad in FORBIDDEN:
            if bad in text:
                errors.append(f"{rel} contains forbidden path fragment: {bad}")

    if errors:
        print("FAIL", errors)
        return 1
    print("PASS public-path guards validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
