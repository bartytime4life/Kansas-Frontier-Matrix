"""Static input-closure regression profile for two documentation workflows.

Run with the repository's existing locked ``test-dependencies`` profile:
    python -m unittest discover --start-directory tests/validators \
        --pattern 'test_documentation_workflow_input_closure.py' --verbose

Keep this reviewed literal profile aligned with the workflows and their inputs.
It is not a GitHub glob/diff simulator, an exhaustive dependency analyzer, or
proof of hosted execution or required-check enforcement. Readiness-marker and
pytest-configuration paths are watched for creation/removal; listing them does
not assert that the corresponding file or deployed service already exists.
"""

from __future__ import annotations

from pathlib import Path
import unittest

import yaml
from yaml.constructor import ConstructorError


ROOT = Path(__file__).resolve().parents[2]
TEST_PATH = "tests/validators/test_documentation_workflow_input_closure.py"
TEST_STEP = "Test documentation workflow input closure"
TEST_COMMAND = (
    "python -m unittest discover --start-directory tests/validators "
    "--pattern 'test_documentation_workflow_input_closure.py' --verbose"
)
EVENTS = ("pull_request", "push")
REQUIRED_PATHS = {
    "docs-build": frozenset({
        "docs/**",
        "mkdocs.yml", "mkdocs.yaml", "docusaurus.config.*",
        "docs/requirements.txt", "requirements-docs.txt",
        "artifacts/docs/**",
        ".github/workflows/pages.yml", ".github/workflows/deploy-docs.yml",
        ".github/workflows/docs-build.yml",
    }),
    "docs-control-plane": frozenset({
        "control_plane/**", "docs/**", "pyproject.toml",
        # Declared root-distribution inputs for the existing project-test install.
        "README.md", "LICENSE", "src/kfm/**",
        "tools/ci/install_python_ci.py", "tools/ci/python-test.lock",
        "tools/validators/validate_adr_index.py",
        "tests/policy/test_control_plane_register_meta_contract.py",
        "tests/validators/test_validate_adr_index.py",
        # The meta-contract reads this schema and checks these support paths.
        "schemas/contracts/v1/governance/object_family_register.schema.json",
        "tools/validators/control_plane/validate_object_family_register.py",
        "tests/validators/test_validate_object_family_register.py",
        ".github/workflows/object-family-register.yml",
        # Pytest configuration can affect either explicitly selected test module.
        "conftest.py", "tests/conftest.py", "tests/policy/conftest.py",
        "tests/validators/conftest.py", "pytest.ini", "tox.ini", "setup.cfg",
        TEST_PATH,
        ".github/workflows/docs-build.yml",
        ".github/workflows/docs-control-plane.yml",
    }),
}


class UniqueBaseLoader(yaml.BaseLoader):
    """Preserve the Actions 'on' key and reject duplicate YAML mapping keys."""

    def construct_mapping(self, node, deep=False):
        result = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            if key in result:
                raise ConstructorError(
                    "while constructing a mapping", node.start_mark,
                    f"duplicate key: {key!r}", key_node.start_mark,
                )
            result[key] = self.construct_object(value_node, deep=deep)
        return result


def load_workflow(name: str) -> dict:
    path = ROOT / ".github" / "workflows" / f"{name}.yml"
    value = yaml.load(path.read_text(encoding="utf-8"), Loader=UniqueBaseLoader)
    if not isinstance(value, dict):
        raise ValueError("workflow root must be a mapping")
    return value


def checked_paths(workflow: dict, event: str, required: frozenset[str]) -> set[str]:
    """Require the reviewed positive input profile without simulating globs."""
    trigger = workflow.get("on", {}).get(event)
    if not isinstance(trigger, dict) or "paths-ignore" in trigger:
        raise ValueError("positive paths mapping required")
    paths = trigger.get("paths")
    if (
        not isinstance(paths, list) or not paths
        or any(not isinstance(p, str) or not p or p.startswith("!") for p in paths)
    ):
        raise ValueError("nonempty positive paths list required")
    if len(paths) != len(set(paths)):
        raise ValueError("duplicate path filter")
    missing = sorted(required - set(paths))
    if missing:
        raise ValueError("missing trigger inputs: " + ", ".join(missing))
    broad = {"*", "**", "**/*", ".github/**", ".github/workflows/**",
             "**/*.md", "**/*.markdown"}
    if broad.intersection(paths):
        raise ValueError("blanket fan-out filter is outside this profile")
    return set(paths)


class DocumentationWorkflowInputClosureTests(unittest.TestCase):
    def test_reviewed_inputs_are_watched_on_both_events(self):
        for name, required in REQUIRED_PATHS.items():
            workflow = load_workflow(name)
            for event in EVENTS:
                with self.subTest(workflow=name, event=event):
                    try:
                        actual = checked_paths(workflow, event, required)
                    except ValueError as error:
                        self.fail(str(error))
                    self.assertEqual(actual, required)

    def test_docs_build_does_not_watch_unrelated_markdown(self):
        workflow = load_workflow("docs-build")
        for event in EVENTS:
            with self.subTest(event=event):
                paths = workflow["on"][event]["paths"]
                self.assertFalse({"**/*.md", "**/*.markdown"}.intersection(paths))

    def test_names_dispatch_main_scope_and_read_only_permissions_are_preserved(self):
        for name in REQUIRED_PATHS:
            with self.subTest(workflow=name):
                workflow = load_workflow(name)
                self.assertEqual(workflow["name"], name)
                self.assertEqual(set(workflow["on"]), {*EVENTS, "workflow_dispatch"})
                self.assertEqual(workflow["on"]["push"]["branches"], ["main"])
                self.assertEqual(workflow["permissions"], {"contents": "read"})
                self.assertEqual(workflow["concurrency"]["cancel-in-progress"], "true")

    def test_regression_test_is_wired_once_after_locked_parser_install(self):
        workflow = load_workflow("docs-control-plane")
        steps = workflow["jobs"]["validate-control-plane-yaml"]["steps"]
        matches = [i for i, step in enumerate(steps) if step["name"] == TEST_STEP]
        self.assertEqual(len(matches), 1)
        index = matches[0]
        self.assertEqual(steps[index].get("run"), TEST_COMMAND)
        self.assertNotIn("if", steps[index])
        self.assertNotIn("continue-on-error", steps[index])
        self.assertIn(
            "python tools/ci/install_python_ci.py test-dependencies",
            [step.get("run") for step in steps[:index]],
        )

    def test_each_required_input_removal_is_rejected(self):
        for name, required in REQUIRED_PATHS.items():
            for event in EVENTS:
                for removed in sorted(required):
                    with self.subTest(workflow=name, event=event, removed=removed):
                        workflow = {"on": {event: {"paths": sorted(required - {removed})}}}
                        with self.assertRaisesRegex(ValueError, "missing trigger inputs"):
                            checked_paths(workflow, event, required)

    def test_invalid_or_exclusion_filters_cannot_mask_missing_inputs(self):
        required = frozenset({"tools/ci/python-test.lock"})
        for paths in (None, [], "tools/ci/python-test.lock", [None], ["!tools/**"],
                      ["tools/ci/python-test.lock", "tools/ci/python-test.lock"]):
            with self.subTest(paths=paths), self.assertRaises(ValueError):
                checked_paths({"on": {"push": {"paths": paths}}}, "push", required)
        trigger = {"paths": sorted(required), "paths-ignore": ["tools/**"]}
        with self.assertRaises(ValueError):
            checked_paths({"on": {"push": trigger}}, "push", required)

    def test_blanket_workflow_filters_are_rejected(self):
        for pattern in ("*", "**", "**/*", ".github/**", ".github/workflows/**",
                        "**/*.md", "**/*.markdown"):
            with self.subTest(pattern=pattern), self.assertRaisesRegex(ValueError, "blanket"):
                checked_paths({"on": {"push": {"paths": ["needed", pattern]}}},
                              "push", frozenset({"needed"}))

    def test_yaml_on_key_is_not_coerced_to_boolean(self):
        value = yaml.load("on:\n  workflow_dispatch:\n", Loader=UniqueBaseLoader)
        self.assertIn("on", value)
        self.assertNotIn(True, value)

    def test_duplicate_yaml_keys_are_rejected(self):
        for text in ("on: {}\non: {}\n", "on:\n  push: {}\n  push: {}\n"):
            with self.subTest(text=text), self.assertRaises(ConstructorError):
                yaml.load(text, Loader=UniqueBaseLoader)


if __name__ == "__main__":
    unittest.main()
