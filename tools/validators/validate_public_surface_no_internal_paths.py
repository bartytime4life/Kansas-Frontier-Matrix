import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FORBIDDEN = [
    "data/raw/",
    "data/work/",
    "data/quarantine/",
    "canonical",
    "proof-pack",
    "direct_model",
    "unpublished",
    "review-only",
    "steward-only",
]
TARGETS = [
    "fixtures/ui/evidence_drawer_payload.valid.json",
    "fixtures/ai/focus_mode_response.answer.valid.json",
    "fixtures/release/release_manifest.valid.json",
]


def main() -> int:
    errors = []
    for rel in TARGETS:
        text = (ROOT / rel).read_text(encoding="utf-8").lower()
        for bad in FORBIDDEN:
            if bad in text:
                errors.append(f"{rel} contains forbidden path fragment: {bad}")
    if errors:
        print("FAIL", errors)
        return 1
    print("PASS public surfaces avoid internal paths")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
