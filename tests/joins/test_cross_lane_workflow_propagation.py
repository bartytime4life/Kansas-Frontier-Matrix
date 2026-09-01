"""Guard generic cross-lane workflow dependency propagation.

The checks use only repository text and synthetic mutations. They do not run a
workflow, access a network, or grant review, release, or publication authority.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]
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
_TRIGGER_RE = re.compile(
    r"(?m)^  (pull_request|push|workflow_dispatch):(?:\n|$)"
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


def _drop_trigger_line(source: str, trigger: str, line: str) -> str:
    section = _trigger_sections(source)[trigger]
    assert line in section
    mutated_section = section.replace(line, "", 1)
    return source.replace(section, mutated_section, 1)


@pytest.mark.parametrize("workflow", WORKFLOWS, ids=lambda path: path.stem)
def test_cross_lane_workflows_propagate_all_dependencies(workflow: Path) -> None:
    assert _propagation_findings(workflow.read_text(encoding="utf-8")) == []


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
