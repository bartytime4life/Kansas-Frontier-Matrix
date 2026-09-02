"""Guard generic cross-lane workflow and test-lane propagation.

The checks use only repository text and synthetic mutations. They do not run a
workflow, access a network, or grant review, release, or publication authority.
"""

from __future__ import annotations

import fnmatch
import json
import re
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "tests/joins/README.md"
CONTRACT_README = ROOT / "contracts/joins/README.md"
CONTRACT = ROOT / "contracts/joins/cross_lane_join_assessment.md"
RECEIPT = ROOT / "data/receipts/generated/genrec-full-atlas-crosswalk-validator-20260830.json"
WORKFLOWS = (
    ROOT / ".github/workflows/cross-lane-join-assessment.yml",
    ROOT / ".github/workflows/soil-hydrology-public-safe-context.yml",
    ROOT / ".github/workflows/soil-agriculture-public-safe-context.yml",
    ROOT / ".github/workflows/fauna-habitat-public-safe-assignment.yml",
)
REQUIRED_TRIGGER_PATHS = (
    "control_plane/domain_lane_register.yaml",
    "fixtures/contracts/v1/joins/cross_lane_join_assessment/**",
    "tests/joins/**",
)
CROSS_LANE_TEST_GLOB = "tests/joins/test_cross_lane_*.py"
CUMULATIVE_REVIEW_PATH_COUNT = 20
_TRIGGER_RE = re.compile(
    r"(?m)^  (pull_request|push|workflow_dispatch):(?:\n|$)"
)
_TRIGGER_PATH_RE = re.compile(r'(?m)^      - "([^"]+)"$')
_DOCUMENTED_GUARD_RE = re.compile(r"`(test_cross_lane_[a-z0-9_]+\.py)`")
_CONTRACT_PROOF_RE = re.compile(
    r"(?m)^  - \.\./\.\./tests/joins/(test_[a-z0-9_]+\.py)$"
)
REQUIRED_JOIN_CONTRACT_LINKS = (
    "./cross_lane_join_assessment.md",
    "../cross_domain/fauna_habitat/public_safe_assignment_profile.md",
    "../cross_domain/soil_agriculture/public_safe_context_profile.md",
    "../cross_domain/soil_hydrology/public_safe_context_profile.md",
)


def _trigger_sections(source: str) -> dict[str, str]:
    matches = list(_TRIGGER_RE.finditer(source))
    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(source)
        sections[match.group(1)] = source[match.start() : end]
    return sections


def _propagation_findings(source: str) -> list[str]:
    findings: list[str] = []
    sections = _trigger_sections(source)

    for trigger in ("pull_request", "push"):
        section = sections.get(trigger)
        if section is None:
            findings.append(f"{trigger}: trigger missing")
            continue
        if trigger == "push" and "    branches: [main]\n" not in section:
            findings.append("push: main branch replay missing")
        for path in REQUIRED_TRIGGER_PATHS:
            if f'      - "{path}"\n' not in section:
                findings.append(f"{trigger}: missing path {path}")

    for test_path in (
        "tests/joins/test_join_candidates.py",
        "tests/joins/test_cross_lane_*.py",
    ):
        if f"          {test_path}\n" not in source:
            findings.append(f"pytest: missing collection {test_path}")

    return findings


def _receipt_trigger_findings(workflow_source: str, receipt_source: str) -> list[str]:
    payload = json.loads(receipt_source)
    artifact_paths = payload.get("artifact_paths")
    if not isinstance(artifact_paths, list) or not all(
        isinstance(path, str) and path for path in artifact_paths
    ):
        return ["receipt: artifact_paths must be a non-empty string list"]

    findings: list[str] = []
    sections = _trigger_sections(workflow_source)
    for trigger in ("pull_request", "push"):
        section = sections.get(trigger)
        if section is None:
            findings.append(f"{trigger}: trigger missing")
            continue
        patterns = _TRIGGER_PATH_RE.findall(section)
        for artifact_path in artifact_paths:
            if not any(
                fnmatch.fnmatchcase(artifact_path, pattern) for pattern in patterns
            ):
                findings.append(
                    f"{trigger}: receipt artifact not covered {artifact_path}"
                )

    return findings


def _overlap_scope_findings(receipt_source: str) -> list[str]:
    payload = json.loads(receipt_source)
    artifact_paths = payload.get("artifact_paths", [])
    gates = payload.get("validation_gates", [])
    gate = next(
        (
            item
            for item in gates
            if item.get("gate") == "active-work-and-overlap-reconciliation"
        ),
        None,
    )
    if gate is None:
        return ["receipt: active-work-and-overlap-reconciliation gate missing"]

    reason = gate.get("reason", "")
    required_scope = (
        f"all {CUMULATIVE_REVIEW_PATH_COUNT} cumulative branch paths",
        f"all {len(artifact_paths)} receipt-bound artifacts",
    )
    return [
        f"overlap gate: missing scope {scope}"
        for scope in required_scope
        if scope not in reason
    ]


def _missing_documented_guards(source: str) -> list[str]:
    actual = {path.name for path in README.parent.glob("test_cross_lane_*.py")}
    documented = set(_DOCUMENTED_GUARD_RE.findall(source))
    return sorted(actual - documented)


def _missing_join_contract_links(source: str) -> list[str]:
    return sorted(
        link for link in REQUIRED_JOIN_CONTRACT_LINKS if f"]({link})" not in source
    )


def _missing_contract_proof_links(
    contract_source: str, receipt_source: str
) -> list[str]:
    payload = json.loads(receipt_source)
    expected = {
        path
        for path in payload.get("artifact_paths", [])
        if isinstance(path, str)
        and path.startswith("tests/joins/test_")
        and path.endswith(".py")
    }
    linked = {
        f"tests/joins/{name}"
        for name in _CONTRACT_PROOF_RE.findall(contract_source)
    }
    return sorted(expected - linked)


def _local_command_findings(source: str) -> list[str]:
    expected = f"  {CROSS_LANE_TEST_GLOB} \\\n"
    if expected not in source:
        return ["local command: cross-lane pytest glob must be unquoted"]
    return []


def _drop_trigger_line(source: str, trigger: str, line: str) -> str:
    section = _trigger_sections(source)[trigger]
    assert line in section
    mutated_section = section.replace(line, "", 1)
    return source.replace(section, mutated_section, 1)


@pytest.mark.parametrize("workflow", WORKFLOWS, ids=lambda path: path.stem)
def test_cross_lane_workflows_propagate_all_dependencies(workflow: Path) -> None:
    assert _propagation_findings(workflow.read_text(encoding="utf-8")) == []


def test_cross_lane_receipt_validator_triggers_for_every_bound_artifact() -> None:
    assert _receipt_trigger_findings(
        WORKFLOWS[0].read_text(encoding="utf-8"),
        RECEIPT.read_text(encoding="utf-8"),
    ) == []


def test_receipt_overlap_gate_covers_complete_review_unit() -> None:
    assert _overlap_scope_findings(RECEIPT.read_text(encoding="utf-8")) == []


@pytest.mark.parametrize(
    ("complete_scope", "partial_scope"),
    (
        ("all 20 cumulative branch paths", "the latest three changed paths"),
        ("all 19 receipt-bound artifacts", "selected receipt artifacts"),
    ),
)
def test_synthetic_partial_overlap_scope_is_detected(
    complete_scope: str, partial_scope: str
) -> None:
    source = RECEIPT.read_text(encoding="utf-8")
    assert complete_scope in source
    mutated = source.replace(complete_scope, partial_scope, 1)
    assert f"overlap gate: missing scope {complete_scope}" in _overlap_scope_findings(
        mutated
    )


def test_readme_documents_every_cross_lane_guard() -> None:
    assert _missing_documented_guards(README.read_text(encoding="utf-8")) == []


def test_join_contract_readme_routes_current_generic_and_pair_profiles() -> None:
    assert _missing_join_contract_links(
        CONTRACT_README.read_text(encoding="utf-8")
    ) == []


def test_contract_links_every_receipt_bound_join_proof() -> None:
    assert _missing_contract_proof_links(
        CONTRACT.read_text(encoding="utf-8"),
        RECEIPT.read_text(encoding="utf-8"),
    ) == []


@pytest.mark.parametrize(
    "proof_path",
    (
        "tests/joins/test_cross_lane_source_role_schema_guard.py",
        "tests/joins/test_cross_lane_workflow_propagation.py",
    ),
)
def test_synthetic_missing_contract_proof_link_is_detected(
    proof_path: str,
) -> None:
    source = CONTRACT.read_text(encoding="utf-8")
    link = f"  - ../../{proof_path}\n"
    assert link in source
    mutated = source.replace(link, "", 1)
    assert proof_path in _missing_contract_proof_links(
        mutated,
        RECEIPT.read_text(encoding="utf-8"),
    )


def test_readme_local_command_expands_cross_lane_pytest_glob() -> None:
    assert _local_command_findings(README.read_text(encoding="utf-8")) == []


def test_synthetic_quoted_local_pytest_glob_is_detected() -> None:
    source = README.read_text(encoding="utf-8")
    unquoted = f"  {CROSS_LANE_TEST_GLOB} \\\n"
    assert unquoted in source
    mutated = source.replace(
        unquoted,
        f"  '{CROSS_LANE_TEST_GLOB}' \\\n",
        1,
    )
    assert _local_command_findings(mutated) == [
        "local command: cross-lane pytest glob must be unquoted"
    ]


def test_synthetic_missing_join_contract_link_is_detected() -> None:
    source = CONTRACT_README.read_text(encoding="utf-8")
    link = "../cross_domain/soil_hydrology/public_safe_context_profile.md"
    assert f"]({link})" in source
    mutated = source.replace(f"]({link})", "](omitted-profile.md)", 1)
    assert link in _missing_join_contract_links(mutated)


def test_synthetic_missing_readme_guard_is_detected() -> None:
    source = README.read_text(encoding="utf-8")
    guard = "test_cross_lane_domain_alias_guard.py"
    assert f"`{guard}`" in source
    mutated = source.replace(f"`{guard}`", "`omitted_guard.py`", 1)
    assert guard in _missing_documented_guards(mutated)


@pytest.mark.parametrize(
    ("trigger", "line", "expected"),
    (
        (
            "push",
            '      - "control_plane/domain_lane_register.yaml"\n',
            "push: missing path control_plane/domain_lane_register.yaml",
        ),
        (
            "push",
            '      - "fixtures/contracts/v1/joins/cross_lane_join_assessment/**"\n',
            "push: missing path fixtures/contracts/v1/joins/cross_lane_join_assessment/**",
        ),
        (
            "pull_request",
            '      - "tests/joins/**"\n',
            "pull_request: missing path tests/joins/**",
        ),
    ),
)
def test_synthetic_missing_dependency_is_detected(
    trigger: str, line: str, expected: str
) -> None:
    source = WORKFLOWS[0].read_text(encoding="utf-8")
    mutated = _drop_trigger_line(source, trigger, line)
    assert expected in _propagation_findings(mutated)


@pytest.mark.parametrize(
    ("trigger", "artifact_path"),
    (
        ("pull_request", ".github/workflows/fauna-habitat-public-safe-assignment.yml"),
        ("push", "contracts/joins/README.md"),
    ),
)
def test_synthetic_untriggered_receipt_artifact_is_detected(
    trigger: str, artifact_path: str
) -> None:
    source = WORKFLOWS[0].read_text(encoding="utf-8")
    mutated = _drop_trigger_line(source, trigger, f'      - "{artifact_path}"\n')
    expected = f"{trigger}: receipt artifact not covered {artifact_path}"
    assert expected in _receipt_trigger_findings(
        mutated,
        RECEIPT.read_text(encoding="utf-8"),
    )


def test_synthetic_missing_guard_collection_is_detected() -> None:
    source = WORKFLOWS[0].read_text(encoding="utf-8")
    mutated = source.replace(
        "          tests/joins/test_cross_lane_*.py\n",
        "",
        1,
    )
    assert (
        "pytest: missing collection tests/joins/test_cross_lane_*.py"
        in _propagation_findings(mutated)
    )
