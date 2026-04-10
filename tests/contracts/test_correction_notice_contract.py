import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "schemas/contracts/v1/correction/correction_notice.schema.json"
VALID_FIXTURE = ROOT / "schemas/tests/fixtures/contracts/v1/valid/correction_notice.supersession.valid.json"
INVALID_FIXTURE = ROOT / "schemas/tests/fixtures/contracts/v1/invalid/correction_notice.supersession.missing_replacement.invalid.json"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate_contract_floor(payload: dict) -> list[str]:
    errors: list[str] = []

    required = {
        "kind",
        "schema_version",
        "correction_id",
        "correction_type",
        "targets",
        "affected_surface_classes",
        "cause",
        "public_note",
    }
    missing = sorted(required - set(payload))
    if missing:
        errors.append(f"missing required fields: {', '.join(missing)}")

    if payload.get("kind") != "CorrectionNotice":
        errors.append("kind must be CorrectionNotice")

    if payload.get("schema_version") != "v1":
        errors.append("schema_version must be v1")

    correction_type = payload.get("correction_type")
    if correction_type == "SUPERSEDE" and not payload.get("replacement_releases"):
        errors.append("SUPERSEDE correction requires replacement_releases")

    if correction_type == "WITHDRAW" and payload.get("replacement_releases"):
        errors.append("WITHDRAW correction must not include replacement_releases")

    cause = payload.get("cause", {})
    if isinstance(cause, dict):
        if not cause.get("reason_code"):
            errors.append("cause.reason_code is required")
        if not cause.get("issued_at"):
            errors.append("cause.issued_at is required")
    else:
        errors.append("cause must be an object")

    return errors


class CorrectionNoticeContractTests(unittest.TestCase):
    def test_schema_is_not_placeholder(self):
        schema = load_json(SCHEMA_PATH)
        self.assertEqual(schema.get("$schema"), "https://json-schema.org/draft/2020-12/schema")
        self.assertEqual(schema.get("title"), "CorrectionNotice")
        self.assertEqual(schema.get("type"), "object")
        self.assertIn("required", schema)

    def test_valid_fixture_satisfies_contract_floor(self):
        payload = load_json(VALID_FIXTURE)
        self.assertEqual(validate_contract_floor(payload), [])

    def test_invalid_fixture_fails_contract_floor(self):
        payload = load_json(INVALID_FIXTURE)
        errors = validate_contract_floor(payload)
        self.assertIn("SUPERSEDE correction requires replacement_releases", errors)


if __name__ == "__main__":
    unittest.main()
