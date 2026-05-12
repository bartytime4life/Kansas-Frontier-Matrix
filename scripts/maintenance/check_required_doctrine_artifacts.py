#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

root = Path(__file__).resolve().parents[2]
registry_path = root / "control_plane" / "document_registry_doctrine_required.yaml"
reg_text = registry_path.read_text(encoding="utf-8")
required = [line.split(":", 1)[1].strip() for line in reg_text.splitlines() if line.strip().startswith("- filename:")]

artifacts_dir = root / "docs" / "doctrine" / "artifacts"
missing = [f for f in required if not (artifacts_dir / f).exists()]

result = {
    "check": "required_doctrine_artifacts",
    "registry": str(registry_path.relative_to(root)),
    "artifacts_dir": str(artifacts_dir.relative_to(root)),
    "required_count": len(required),
    "missing_count": len(missing),
    "missing": missing,
}

print(json.dumps(result, indent=2, sort_keys=True))
if missing:
    raise SystemExit(1)
