from pathlib import Path
t=Path("docs/sources/SOURCE_LEDGER.md").read_text()
ok="not directly inspectable" in t.lower()
print("PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
