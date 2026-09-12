"""Keep topology tests inside the existing Make discovery boundary.

This is a read-only routing check, not a topology scan or a new test runner.
The original root-status assertions live in test_validate_root_status_topology.py.
"""
from __future__ import annotations

import fnmatch
from pathlib import Path
import re
import shlex
import unittest


REPO_ROOT = Path(__file__).resolve().parents[3]
TEST_DIRECTORY = "tests/validators/directory_governance"
ROOT_STATUS_MODULE = "test_validate_root_status_topology.py"


def native_pattern(makefile: str) -> str:
    """Read the explicit command; unfamiliar/ambiguous wiring fails the test.

    This deliberately handles the current tabbed, semicolon-delimited recipe,
    not arbitrary Make syntax. Recipe refactoring must update this check too.
    """
    recipes = re.findall(r"(?m)^repository-topology:\n((?:\t[^\n]*\n)+)", makefile)
    if len(recipes) != 1:
        raise ValueError("expected one explicit repository-topology recipe")
    patterns = []
    for command in recipes[0].replace("\\\n", " ").split(";"):
        tokens = shlex.split(command)
        if "--start-directory" not in tokens:
            continue
        start = tokens.index("--start-directory")
        if start + 1 >= len(tokens) or tokens[start + 1] != TEST_DIRECTORY:
            continue
        if tokens.count("--pattern") != 1:
            raise ValueError("expected one native discovery pattern")
        index = tokens.index("--pattern")
        if index + 1 >= len(tokens) or tokens[index + 1].startswith("-"):
            raise ValueError("missing native discovery pattern")
        patterns.append(tokens[index + 1])
    if len(patterns) != 1:
        raise ValueError("expected one native topology discovery command")
    return patterns[0]


class RepositoryTopologyDiscoveryTests(unittest.TestCase):
    def test_native_target_includes_all_topology_test_modules(self) -> None:
        pattern = native_pattern((REPO_ROOT / "Makefile").read_text(encoding="utf-8"))
        names = sorted(path.name for path in (REPO_ROOT / TEST_DIRECTORY).glob("test_*topology*.py"))
        self.assertIn(ROOT_STATUS_MODULE, names, "required root-status regressions are missing")
        omitted = [name for name in names if not fnmatch.fnmatchcase(name, pattern)]
        self.assertEqual([], omitted, "topology tests would silently escape native discovery")

    def test_legacy_filename_reproduces_the_discovery_gap(self) -> None:
        pattern = "test_validate_*topology.py"
        self.assertFalse(fnmatch.fnmatchcase("test_repository_topology_root_status.py", pattern))
        self.assertTrue(fnmatch.fnmatchcase(ROOT_STATUS_MODULE, pattern))

    def test_absent_or_ambiguous_wiring_fails_closed(self) -> None:
        command = "\tpython -m unittest discover --start-directory " + TEST_DIRECTORY
        valid = "repository-topology:\n" + command + " --pattern 'test_validate_*topology.py'\n"
        malformed = (
            "", valid + valid,
            "repository-topology:\n\techo no-discovery\n",
            "repository-topology:\n" + command + "\n",
            valid + command + " --pattern 'test_*.py'\n",
        )
        for text in malformed:
            with self.subTest(text=text), self.assertRaises(ValueError):
                native_pattern(text)

    def test_other_discovery_lane_does_not_supply_the_native_pattern(self) -> None:
        text = (
            "repository-topology:\n"
            "\tpython -m unittest discover --start-directory tests/ci --pattern 'test_*.py'; \\\n"
            "\tpython -m unittest discover --start-directory " + TEST_DIRECTORY
            + " --pattern 'test_validate_*topology.py';\n"
        )
        self.assertEqual("test_validate_*topology.py", native_pattern(text))


if __name__ == "__main__":
    unittest.main()
