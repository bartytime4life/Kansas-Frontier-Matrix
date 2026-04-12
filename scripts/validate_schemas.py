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

required_contract_schemas = [
    "schemas/contracts/v1/source/source_descriptor.schema.json",
    "schemas/contracts/v1/data/dataset_version.schema.json",
    "schemas/contracts/v1/policy/decision_envelope.schema.json",
    "schemas/contracts/v1/release/release_manifest.schema.json",
    "schemas/contracts/v1/evidence/evidence_bundle.schema.json",
    "schemas/contracts/v1/runtime/runtime_response_envelope.schema.json",
    "schemas/contracts/v1/correction/correction_notice.schema.json",
    "schemas/contracts/v1/common/run_receipt.schema.json",
    "schemas/contracts/v1/common/ai_receipt.schema.json",
]

for rel in required_contract_schemas:
    path = root / rel
    if not path.exists():
        errors.append(f"{rel}: missing required schema")
        continue
    schema = json.loads(path.read_text(encoding="utf-8"))
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        errors.append(f"{rel}: unexpected $schema")
    if schema == {}:
        errors.append(f"{rel}: schema is placeholder")

if errors:
    print("validate-schemas: FAILED")
    for err in errors:
        print(f" - {err}")
    sys.exit(1)

print(f"validate-schemas: OK ({len(json_files)} json files parsed)")
