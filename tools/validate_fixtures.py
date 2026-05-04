import json
from pathlib import Path

OUTCOMES = {"ANSWER", "ABSTAIN", "DENY", "ERROR"}
POLICY_DECISIONS = {"ALLOW", "ABSTAIN", "DENY", "ERROR"}
RELEASE_STATES = {"DRAFT", "QUARANTINED", "PROCESSED", "CATALOGED", "REVIEWED", "RELEASE_CANDIDATE", "PUBLISHED", "SUPERSEDED", "WITHDRAWN"}
SENSITIVE = {"PUBLIC_SAFE", "GENERALIZED", "REDACTED", "RESTRICTED", "STEWARD_ONLY"}


def load(path: str):
    return json.loads(Path(path).read_text())


def validate_valid_fixtures(errors: list[str]) -> None:
    valid_files = sorted(Path("fixtures").rglob("*.valid.json"))
    for path in valid_files:
        obj = json.loads(path.read_text())
        if obj.get("knowledge_character") != "SYNTHETIC_TEST":
            errors.append(f"{path}: knowledge_character must be SYNTHETIC_TEST")
        if "sensitivity" in obj and obj["sensitivity"] not in SENSITIVE:
            errors.append(f"{path}: invalid sensitivity {obj['sensitivity']}")

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

    release_manifest = load("fixtures/release/release_manifest.valid.json")
    if release_manifest.get("release_state") not in RELEASE_STATES:
        errors.append("fixtures/release/release_manifest.valid.json: invalid release_state")
    if not release_manifest.get("rollback_target"):
        errors.append("fixtures/release/release_manifest.valid.json: missing rollback_target")
    if not release_manifest.get("correction_route"):
        errors.append("fixtures/release/release_manifest.valid.json: missing correction_route")


def validate_invalid_fixtures(errors: list[str]) -> None:
    missing_ref = load("fixtures/invalid/missing_evidence_ref.json")
    if missing_ref.get("evidence_refs"):
        errors.append("fixtures/invalid/missing_evidence_ref.json should not provide evidence_refs")

    raw_path = load("fixtures/invalid/public_layer_points_raw.json")
    if "data/raw" not in raw_path.get("artifact_path", ""):
        errors.append("fixtures/invalid/public_layer_points_raw.json must point to data/raw")

    focus_no_cite = load("fixtures/invalid/focus_answer_without_citation.json")
    if focus_no_cite.get("outcome") != "ANSWER" or focus_no_cite.get("citations"):
        errors.append("fixtures/invalid/focus_answer_without_citation.json must be ANSWER without citations")

    bad_policy = load("fixtures/invalid/policy_unknown_public_release.json")
    if bad_policy.get("decision") in POLICY_DECISIONS:
        errors.append("fixtures/invalid/policy_unknown_public_release.json must stay non-enum")

    sensitive = load("fixtures/invalid/sensitive_exact_coords.json")
    if sensitive.get("sensitivity") != "RESTRICTED":
        errors.append("fixtures/invalid/sensitive_exact_coords.json must remain RESTRICTED")

    no_rollback = load("fixtures/invalid/release_without_rollback.json")
    if no_rollback.get("rollback_target"):
        errors.append("fixtures/invalid/release_without_rollback.json should omit rollback_target")


def main() -> int:
    errors: list[str] = []
    validate_valid_fixtures(errors)
    validate_invalid_fixtures(errors)
    if errors:
        print("FAIL", errors)
        return 1
    print("PASS", "valid fixtures pass and invalid fixtures remain intentionally invalid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
