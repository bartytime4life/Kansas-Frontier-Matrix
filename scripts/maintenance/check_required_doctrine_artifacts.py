#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[2]
reg_text = (root / "control_plane" / "document_registry_doctrine_required.yaml").read_text(encoding="utf-8")
required = [line.split(":",1)[1].strip() for line in reg_text.splitlines() if "filename:" in line]
artifacts_dir = root / "docs" / "doctrine" / "artifacts"
missing = [f for f in required if not (artifacts_dir / f).exists()]

if missing:
    print("MISSING")
    for m in missing:
        print(m)
    raise SystemExit(1)
print("OK")
