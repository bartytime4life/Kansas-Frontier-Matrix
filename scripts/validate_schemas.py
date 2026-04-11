from pathlib import Path
import json
import sys

root = Path(__file__).resolve().parents[1]
json_files = sorted(root.rglob("*.json"))
errors = []

for path in json_files:
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{path.relative_to(root)}: invalid json ({exc})")

schema_path = root / "schemas/contracts/v1/correction/correction_notice.schema.json"
if schema_path.exists():
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        errors.append("schemas/contracts/v1/correction/correction_notice.schema.json: unexpected $schema")

if errors:
    print("validate-schemas: FAILED")
    for err in errors:
        print(f" - {err}")
    sys.exit(1)

print(f"validate-schemas: OK ({len(json_files)} json files parsed)")
