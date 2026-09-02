"""Regression tests for the bounded accessibility workflow surfaces."""

from __future__ import annotations

from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[2]
WORKFLOW_PATH = REPO_ROOT / ".github/workflows/accessibility.yml"
EXPECTED_BROWSER_SPECS = (
    "tests/browser/citation-pill.spec.ts",
    "tests/browser/evidence-drawer.spec.ts",
    "tests/browser/evidence-tooltip.spec.ts",
    "tests/browser/focus-composed-claim.spec.ts",
    "tests/browser/map-evidence-drawer.spec.ts",
    "tests/browser/map-runtime-trust-status.spec.ts",
    "tests/browser/time-banner.spec.ts",
    "tests/browser/workspace-navigation.spec.ts",
)


def _workflow() -> dict[str, object]:
    return yaml.safe_load(WORKFLOW_PATH.read_text(encoding="utf-8"))


def _keyboard_steps() -> list[dict[str, object]]:
    workflow = _workflow()
    return workflow["jobs"]["keyboard-navigation"]["steps"]


def test_preserves_check_names_and_scoped_hold() -> None:
    workflow = _workflow()

    assert workflow["name"] == "accessibility"
    assert set(workflow["jobs"]) == {"axe", "keyboard-navigation"}
    assert "WORKFLOW_HOLD" in WORKFLOW_PATH.read_text(encoding="utf-8")
    assert "TODO keyboard-navigation" not in WORKFLOW_PATH.read_text(encoding="utf-8")


def test_keyboard_job_runs_exact_public_safe_browser_specs() -> None:
    steps = _keyboard_steps()
    command = next(
        str(step["run"])
        for step in steps
        if step.get("name") == "Run bounded Explorer keyboard and focus smoke"
    )

    assert "pnpm --filter explorer-web exec playwright test" in command
    assert "--config=playwright.config.ts" in command
    assert tuple(
        token for token in command.split() if token.endswith(".spec.ts")
    ) == EXPECTED_BROWSER_SPECS
    for relative_path in EXPECTED_BROWSER_SPECS:
        assert (REPO_ROOT / "apps/explorer-web" / relative_path).is_file()


def test_keyboard_job_is_read_only_pinned_and_non_publishing() -> None:
    workflow = _workflow()
    keyboard = workflow["jobs"]["keyboard-navigation"]
    rendered = WORKFLOW_PATH.read_text(encoding="utf-8")

    assert workflow["permissions"] == {"contents": "read"}
    assert keyboard["env"]["KFM_NO_NETWORK"] == "1"
    assert keyboard["timeout-minutes"] == 15
    assert "persist-credentials: false" in rendered
    assert "actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1" in rendered
    assert "actions/setup-node@820762786026740c76f36085b0efc47a31fe5020" in rendered
    for forbidden in (
        "secrets.",
        "pull-requests: write",
        "contents: write",
        "actions/upload-artifact",
        "github-script",
    ):
        assert forbidden not in rendered
