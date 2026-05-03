import json
from pathlib import Path

OUTCOMES = {"ANSWER", "ABSTAIN", "DENY", "ERROR"}
POLICY_DECISIONS = {"ALLOW", "ABSTAIN", "DENY", "ERROR"}
RELEASE_STATES = {"DRAFT", "QUARANTINED", "PROCESSED", "CATALOGED", "REVIEWED", "RELEASE_CANDIDATE", "PUBLISHED", "SUPERSEDED", "WITHDRAWN"}

errors = []
valid_files = sorted(Path("fixtures").rglob("*.valid.json"))

for path in valid_files:
    obj = json.loads(path.read_text())
    if obj.get("knowledge_character") != "SYNTHETIC_TEST":
        errors.append(f"{path}: knowledge_character must be SYNTHETIC_TEST")

for path in Path("fixtures/ai").glob("focus_mode_response.*.valid.json"):
    obj = json.loads(path.read_text())
    outcome = obj.get("outcome")
    if outcome not in OUTCOMES:
        errors.append(f"{path}: invalid outcome {outcome}")
    if outcome == "ANSWER" and not obj.get("citations"):
        errors.append(f"{path}: ANSWER requires citations")

for path in Path("fixtures/policy").glob("*.valid.json"):
    decision = json.loads(path.read_text()).get("decision")
    if decision not in POLICY_DECISIONS:
        errors.append(f"{path}: invalid policy decision {decision}")

release_manifest = json.loads(Path("fixtures/release/release_manifest.valid.json").read_text())
if release_manifest.get("release_state") not in RELEASE_STATES:
    errors.append("fixtures/release/release_manifest.valid.json: invalid release_state")
if not release_manifest.get("rollback_target"):
    errors.append("fixtures/release/release_manifest.valid.json: missing rollback_target")
if not release_manifest.get("correction_route"):
    errors.append("fixtures/release/release_manifest.valid.json: missing correction_route")

if errors:
    print("FAIL", errors)
    raise SystemExit(1)
print("PASS", f"validated {len(valid_files)} valid fixtures")
