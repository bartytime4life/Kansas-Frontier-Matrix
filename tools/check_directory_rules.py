from pathlib import Path
BAD={"hydrology","soil","fauna","roads","archaeology","agriculture"}
found=[d.name for d in Path(".").iterdir() if d.is_dir() and d.name in BAD]
print("FAIL" if found else "PASS", found)
raise SystemExit(1 if found else 0)
