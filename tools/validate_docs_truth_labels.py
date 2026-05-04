from pathlib import Path

CHECKS = {
    "docs/doctrine/truth-posture.md": ["CONFIRMED", "PROPOSED", "UNKNOWN", "NEEDS VERIFICATION", "DENY", "ABSTAIN", "ERROR"],
    "docs/doctrine/trust-membrane.md": ["public unit of value", "inspectable claim"],
    "README.md": ["Kansas-first", "map-first", "evidence-first", "auditable", "reversible"],
}


def main() -> int:
    errors = []
    for path, tokens in CHECKS.items():
        p = Path(path)
        if not p.exists():
            errors.append(f"missing doc: {path}")
            continue
        text = p.read_text().lower()
        for token in tokens:
            if token.lower() not in text:
                errors.append(f"{path}: missing token '{token}'")

    if errors:
        print("FAIL", errors)
        return 1

    print("PASS", "documentation truth-label posture checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
