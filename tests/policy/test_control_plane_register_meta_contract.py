from datetime import date
from pathlib import Path

REQUIRED_FILES = [
    "control_plane/document_registry.yaml",
    "control_plane/source_authority_register.yaml",
    "control_plane/object_family_register.yaml",
    "control_plane/domain_lane_register.yaml",
    "control_plane/policy_gate_register.yaml",
    "control_plane/release_state_register.yaml",
    "control_plane/verification_backlog.yaml",
    "control_plane/contradiction_register.yaml",
    "control_plane/deprecation_register.yaml",
]

REQUIRED_META_KEYS = [
    "status:",
    "owner:",
    "last_reviewed:",
    "related_doctrine:",
]


def test_control_plane_register_meta_contract():
    for rel_path in REQUIRED_FILES:
        content = Path(rel_path).read_text(encoding="utf-8")
        assert content.startswith("meta:\n"), f"{rel_path} missing top-level meta block"
        header = "\n".join(content.splitlines()[:20])
        for key in REQUIRED_META_KEYS:
            assert key in header, f"{rel_path} missing meta key: {key}"
        assert "entries:" in content, f"{rel_path} missing entries body"


def test_control_plane_register_last_reviewed_is_iso_date() -> None:
    for rel_path in REQUIRED_FILES:
        content = Path(rel_path).read_text(encoding="utf-8")
        header = "\n".join(content.splitlines()[:20])
        marker = "last_reviewed:"
        assert marker in header, f"{rel_path} missing {marker}"
        value = [ln for ln in header.splitlines() if ln.strip().startswith(marker)][
            0
        ].split(":", 1)[1].strip()
        date.fromisoformat(value)


def test_control_plane_register_last_reviewed_not_future_date() -> None:
    today = date.today()
    for rel_path in REQUIRED_FILES:
        content = Path(rel_path).read_text(encoding="utf-8")
        header = "\n".join(content.splitlines()[:20])
        marker = "last_reviewed:"
        value = [ln for ln in header.splitlines() if ln.strip().startswith(marker)][
            0
        ].split(":", 1)[1].strip()
        reviewed = date.fromisoformat(value)
        assert reviewed <= today, f"{rel_path} has future last_reviewed: {reviewed}"


def test_control_plane_related_doctrine_paths_exist() -> None:
    for rel_path in REQUIRED_FILES:
        content = Path(rel_path).read_text(encoding="utf-8")
        lines = content.splitlines()[:25]
        doctrine_lines = [ln.strip() for ln in lines if ln.strip().startswith("- ")]
        doctrine_paths = [ln[2:] for ln in doctrine_lines if ln[2:].startswith("docs/")]
        assert doctrine_paths, f"{rel_path} missing related_doctrine entries"
        for doctrine_path in doctrine_paths:
            assert Path(doctrine_path).exists(), f"{rel_path} references missing doctrine path: {doctrine_path}"


def test_control_plane_register_status_value_allowed() -> None:
    allowed = {"PROPOSED", "CONFIRMED"}
    for rel_path in REQUIRED_FILES:
        content = Path(rel_path).read_text(encoding="utf-8")
        header = "\n".join(content.splitlines()[:20])
        marker = "status:"
        assert marker in header, f"{rel_path} missing {marker}"
        value = [ln for ln in header.splitlines() if ln.strip().startswith(marker)][0].split(":", 1)[1].strip()
        assert value in allowed, f"{rel_path} has unsupported status value: {value}"


def test_control_plane_register_owner_present_and_nonempty() -> None:
    for rel_path in REQUIRED_FILES:
        content = Path(rel_path).read_text(encoding="utf-8")
        header = "\n".join(content.splitlines()[:20])
        marker = "owner:"
        assert marker in header, f"{rel_path} missing {marker}"
        value = [ln for ln in header.splitlines() if ln.strip().startswith(marker)][0].split(":", 1)[1].strip()
        assert value, f"{rel_path} has empty owner value"


def test_control_plane_register_related_doctrine_present_and_nonempty() -> None:
    for rel_path in REQUIRED_FILES:
        content = Path(rel_path).read_text(encoding="utf-8")
        header_lines = content.splitlines()[:25]
        assert any(ln.strip().startswith("related_doctrine:") for ln in header_lines), (
            f"{rel_path} missing related_doctrine section"
        )
        doctrine_entries = [ln.strip() for ln in header_lines if ln.strip().startswith("- ")]
        assert doctrine_entries, f"{rel_path} has empty related_doctrine entries"
