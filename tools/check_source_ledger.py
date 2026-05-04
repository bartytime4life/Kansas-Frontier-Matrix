from pathlib import Path

SOURCE_LEDGER = Path("docs/sources/SOURCE_LEDGER.md")
REQUIRED_HEADING = "# Source Ledger"
REQUIRED_PHRASE = "needs verification"
REQUIRED_REASON = "not directly inspectable"


def main() -> int:
    if not SOURCE_LEDGER.exists():
        print("FAIL", f"missing file: {SOURCE_LEDGER}")
        return 1

    text = SOURCE_LEDGER.read_text(encoding="utf-8")
    text_lower = text.lower()

    errors: list[str] = []
    if REQUIRED_HEADING not in text:
        errors.append("missing '# Source Ledger' heading")
    if REQUIRED_PHRASE not in text_lower:
        errors.append("missing 'NEEDS VERIFICATION' status marker")
    if REQUIRED_REASON not in text_lower:
        errors.append("missing reason: source not directly inspectable")

    if errors:
        print("FAIL", errors)
        return 1

    print("PASS", "source ledger contains verification posture")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
