import json
from datetime import date
from pathlib import Path

META_PROFILE_FILES = [
    "control_plane/document_registry.yaml",
    "control_plane/source_authority_register.yaml",
    "control_plane/domain_lane_register.yaml",
    "control_plane/policy_gate_register.yaml",
    "control_plane/release_state_register.yaml",
    "control_plane/verification_backlog.yaml",
    "control_plane/contradiction_register.yaml",
    "control_plane/deprecation_register.yaml",
]

SCHEMA_PROFILE_FILES = {
    "control_plane/object_family_register.yaml": {
        "schema": "schemas/contracts/v1/governance/object_family_register.schema.json",
        "validator": "tools/validators/control_plane/validate_object_family_register.py",
        "tests": "tests/validators/test_validate_object_family_register.py",
        "workflow": ".github/workflows/object-family-register.yml",
    }
}

REQUIRED_FILES = [*META_PROFILE_FILES, *SCHEMA_PROFILE_FILES]

REQUIRED_META_KEYS = [
    "status:",
    "owner:",
    "last_reviewed:",
    "related_doctrine:",
]


def _legacy_header(content: str, line_count: int = 20) -> str:
    return "\n".join(content.splitlines()[:line_count])


def _legacy_meta_value(content: str, marker: str) -> str:
    header = _legacy_header(content)
    matching = [line for line in header.splitlines() if line.strip().startswith(marker)]
    assert matching, f"missing {marker}"
    return matching[0].split(":", 1)[1].strip()


def _schema_profile(rel_path: str) -> tuple[dict[str, object], dict[str, object]]:
    support = SCHEMA_PROFILE_FILES[rel_path]
    for role, support_path in support.items():
        assert Path(support_path).is_file(), (
            f"{rel_path} missing dedicated {role} support: {support_path}"
        )

    payload = json.loads(Path(rel_path).read_text(encoding="utf-8"))
    schema = json.loads(Path(support["schema"]).read_text(encoding="utf-8"))
    assert isinstance(payload, dict), f"{rel_path} must contain a mapping"
    assert isinstance(schema, dict), f"{support['schema']} must contain a mapping"

    x_kfm = schema.get("x-kfm")
    assert isinstance(x_kfm, dict), f"{support['schema']} missing x-kfm binding"
    assert x_kfm.get("instance") == rel_path
    assert x_kfm.get("validator") == support["validator"]
    assert x_kfm.get("tests") == support["tests"]

    contract_doc = x_kfm.get("contract_doc")
    assert isinstance(contract_doc, str) and contract_doc
    assert Path(contract_doc).is_file(), (
        f"{rel_path} references missing contract document: {contract_doc}"
    )
    return payload, schema


def test_control_plane_required_register_files_exist() -> None:
    for rel_path in REQUIRED_FILES:
        assert Path(rel_path).is_file(), (
            f"required control-plane register is missing: {rel_path}"
        )


def test_control_plane_register_meta_contract():
    for rel_path in META_PROFILE_FILES:
        content = Path(rel_path).read_text(encoding="utf-8")
        assert content.startswith("meta:\n"), f"{rel_path} missing top-level meta block"
        header = _legacy_header(content)
        for key in REQUIRED_META_KEYS:
            assert key in header, f"{rel_path} missing meta key: {key}"
        assert "entries:" in content, f"{rel_path} missing entries body"


def test_schema_governed_register_contract() -> None:
    allowed_statuses = {"PROPOSED", "CONFIRMED"}
    today = date.today()

    for rel_path in SCHEMA_PROFILE_FILES:
        payload, _schema = _schema_profile(rel_path)
        assert payload.get("registry") == Path(rel_path).stem
        assert payload.get("status") in allowed_statuses

        owner = payload.get("owner_role")
        assert isinstance(owner, str) and owner, f"{rel_path} has empty owner_role"

        reviewed_value = payload.get("updated_at")
        assert isinstance(reviewed_value, str), f"{rel_path} missing updated_at"
        reviewed = date.fromisoformat(reviewed_value)
        assert reviewed <= today, f"{rel_path} has future updated_at: {reviewed}"

        entries = payload.get("entries")
        assert isinstance(entries, list) and entries, f"{rel_path} has no entries"


def test_control_plane_register_last_reviewed_is_iso_date() -> None:
    for rel_path in META_PROFILE_FILES:
        content = Path(rel_path).read_text(encoding="utf-8")
        date.fromisoformat(_legacy_meta_value(content, "last_reviewed:"))


def test_control_plane_register_last_reviewed_not_future_date() -> None:
    today = date.today()
    for rel_path in META_PROFILE_FILES:
        content = Path(rel_path).read_text(encoding="utf-8")
        reviewed = date.fromisoformat(_legacy_meta_value(content, "last_reviewed:"))
        assert reviewed <= today, f"{rel_path} has future last_reviewed: {reviewed}"


def test_control_plane_related_doctrine_paths_exist() -> None:
    for rel_path in META_PROFILE_FILES:
        content = Path(rel_path).read_text(encoding="utf-8")
        lines = content.splitlines()[:25]
        doctrine_lines = [line.strip() for line in lines if line.strip().startswith("- ")]
        doctrine_paths = [
            line[2:] for line in doctrine_lines if line[2:].startswith("docs/")
        ]
        assert doctrine_paths, f"{rel_path} missing related_doctrine entries"
        for doctrine_path in doctrine_paths:
            assert Path(doctrine_path).exists(), (
                f"{rel_path} references missing doctrine path: {doctrine_path}"
            )


def test_control_plane_register_status_value_allowed() -> None:
    allowed = {"PROPOSED", "CONFIRMED"}
    for rel_path in META_PROFILE_FILES:
        content = Path(rel_path).read_text(encoding="utf-8")
        value = _legacy_meta_value(content, "status:")
        assert value in allowed, f"{rel_path} has unsupported status value: {value}"


def test_control_plane_register_owner_present_and_nonempty() -> None:
    for rel_path in META_PROFILE_FILES:
        content = Path(rel_path).read_text(encoding="utf-8")
        value = _legacy_meta_value(content, "owner:")
        assert value, f"{rel_path} has empty owner value"


def test_control_plane_register_related_doctrine_present_and_nonempty() -> None:
    for rel_path in META_PROFILE_FILES:
        content = Path(rel_path).read_text(encoding="utf-8")
        header_lines = content.splitlines()[:25]
        assert any(
            line.strip().startswith("related_doctrine:") for line in header_lines
        ), f"{rel_path} missing related_doctrine section"
        doctrine_entries = [
            line.strip() for line in header_lines if line.strip().startswith("- ")
        ]
        assert doctrine_entries, f"{rel_path} has empty related_doctrine entries"
