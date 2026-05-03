import json
from pathlib import Path
rm=json.loads(Path("fixtures/release/release_manifest.valid.json").read_text())
print("PASS" if rm.get("rollback_target") else "FAIL")
