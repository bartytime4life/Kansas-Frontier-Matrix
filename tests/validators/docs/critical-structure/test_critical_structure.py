from __future__ import annotations

import importlib.util
import json
import socket
import subprocess
import sys
import tempfile
import unittest
import urllib.request
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[4]
MODULE_PATH = (
    REPO_ROOT
    / "tools/validators/docs/critical-structure/check_critical_structure.py"
)
SPEC = importlib.util.spec_from_file_location(
    "kfm_docs_critical_structure", MODULE_PATH
)
assert SPEC is not None and SPEC.loader is not None
critical_structure = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = critical_structure
SPEC.loader.exec_module(critical_structure)


class CriticalStructureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write(self, relative_path: str, content: str) -> Path:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def test_repaired_contributor_contract_passes_live_profile(self) -> None:
        result = critical_structure.check_paths(
            REPO_ROOT, ("CONTRIBUTING.md",)
        )

        self.assertEqual("DOC_CRITICAL_STRUCTURE_PASS", result.outcome)
        self.assertEqual((), result.findings)
        self.assertFalse(result.to_payload()["non_effects"]["writes"])

    def test_self_insertion_shape_fails_with_stable_reason_codes(self) -> None:
        self.write(
            "CONTRIBUTING.md",
            "# Contributing to Kansas Frontier Matrix\n\n"
            "## Status\n\n"
            "| authority | accepted [ADR-0029]# Contributing to Kansas Frontier Matrix\n\n"
            "## Status\n",
        )

        first = critical_structure.check_paths(
            self.root, ("CONTRIBUTING.md",)
        )
        second = critical_structure.check_paths(
            self.root, ("CONTRIBUTING.md",)
        )

        self.assertEqual("DOC_CRITICAL_STRUCTURE_FAIL", first.outcome)
        self.assertEqual(first.to_json(), second.to_json())
        self.assertEqual(
            [
                "TITLE_OCCURRENCE_COUNT",
                "INTERRUPTED_LINK_OR_HEADING",
                "DUPLICATE_H2",
            ],
            [finding.code for finding in first.findings],
        )

    def test_fenced_and_commented_headings_are_inert(self) -> None:
        self.write(
            "docs/example.md",
            "# Example\n\n## Visible\n\n"
            "```markdown\n# Inert\n## Visible\n```\n\n"
            "<!--\n# Inert comment\n## Visible\n-->\n",
        )

        result = critical_structure.check_paths(
            self.root, ("docs/example.md",)
        )

        self.assertEqual("DOC_CRITICAL_STRUCTURE_PASS", result.outcome)

    def test_inline_comment_token_is_inert(self) -> None:
        self.write(
            "docs/example.md",
            "# Example\n\n## Visible\n\nThe literal `<!--` is not a comment.\n",
        )

        result = critical_structure.check_paths(
            self.root, ("docs/example.md",)
        )

        self.assertEqual("DOC_CRITICAL_STRUCTURE_PASS", result.outcome)

    def test_unclosed_boundaries_and_missing_newline_fail(self) -> None:
        self.write("docs/fence.md", "# Fence\n\n```text\nnot closed")
        self.write("docs/comment.md", "# Comment\n\n<!-- not closed\n")

        fence = critical_structure.check_paths(
            self.root, ("docs/fence.md",)
        )
        comment = critical_structure.check_paths(
            self.root, ("docs/comment.md",)
        )

        self.assertEqual(
            {"FINAL_NEWLINE_MISSING", "UNCLOSED_FENCE"},
            {finding.code for finding in fence.findings},
        )
        self.assertEqual(
            {"UNCLOSED_HTML_COMMENT"},
            {finding.code for finding in comment.findings},
        )

    def test_contributor_title_is_pinned(self) -> None:
        self.write("CONTRIBUTING.md", "# Different title\n\n## Status\n")

        result = critical_structure.check_paths(
            self.root, ("CONTRIBUTING.md",)
        )

        self.assertEqual(
            ["H1_TITLE_MISMATCH"],
            [finding.code for finding in result.findings],
        )

    def test_missing_and_multiple_atx_h1_documents_fail(self) -> None:
        self.write("docs/missing.md", "## Status\n")
        self.write("docs/multiple.md", "# First\n\n# Second\n")

        missing = critical_structure.check_paths(
            self.root, ("docs/missing.md",)
        )
        multiple = critical_structure.check_paths(
            self.root, ("docs/multiple.md",)
        )

        self.assertEqual(
            ["H1_COUNT"], [finding.code for finding in missing.findings]
        )
        self.assertEqual(
            ["H1_COUNT"], [finding.code for finding in multiple.findings]
        )

    def test_conflict_marker_fails_outside_inert_regions(self) -> None:
        self.write(
            "docs/conflict.md",
            "# Conflict\n\n<<<<<<< branch-a\nvalue\n=======\nother\n>>>>>>> branch-b\n",
        )
        self.write(
            "docs/inert.md",
            "# Inert\n\n```text\n<<<<<<< example\n```\n\n"
            "The literal `>>>>>>> example` is inert.\n",
        )

        conflict = critical_structure.check_paths(
            self.root, ("docs/conflict.md",)
        )
        inert = critical_structure.check_paths(self.root, ("docs/inert.md",))

        self.assertEqual(
            [
                "MERGE_CONFLICT_MARKER",
                "MERGE_CONFLICT_MARKER",
            ],
            [finding.code for finding in conflict.findings],
        )
        self.assertEqual("DOC_CRITICAL_STRUCTURE_PASS", inert.outcome)

    def test_repeated_lower_level_heading_is_allowed(self) -> None:
        self.write(
            "docs/example.md",
            "# Example\n\n## One\n\n### Repeated\n\n## Two\n\n### Repeated\n",
        )

        result = critical_structure.check_paths(
            self.root, ("docs/example.md",)
        )

        self.assertEqual("DOC_CRITICAL_STRUCTURE_PASS", result.outcome)

    def test_inline_code_delimiters_must_have_equal_run_lengths(self) -> None:
        self.write(
            "CONTRIBUTING.md",
            "# Contributing to Kansas Frontier Matrix\n\n"
            "## Status\n\n"
            "`` # Contributing to Kansas Frontier Matrix ```\n",
        )

        result = critical_structure.check_paths(
            self.root, ("CONTRIBUTING.md",)
        )

        self.assertEqual(
            ["TITLE_OCCURRENCE_COUNT"],
            [finding.code for finding in result.findings],
        )

    def test_inline_code_keeps_distinct_h2_titles_distinct(self) -> None:
        self.write(
            "docs/example.md",
            "# Example\n\n## Run `alpha`\n\n## Run `beta`\n",
        )

        result = critical_structure.check_paths(
            self.root, ("docs/example.md",)
        )

        self.assertEqual("DOC_CRITICAL_STRUCTURE_PASS", result.outcome)

    def test_invalid_backtick_fence_cannot_hide_duplicate_title(self) -> None:
        self.write(
            "CONTRIBUTING.md",
            "# Contributing to Kansas Frontier Matrix\n\n"
            "``` bad`\n"
            "# Contributing to Kansas Frontier Matrix\n"
            "```\n",
        )
        self.write(
            "docs/same-line.md",
            "# Example\n\n```literal```\n",
        )

        bypass = critical_structure.check_paths(
            self.root, ("CONTRIBUTING.md",)
        )
        same_line = critical_structure.check_paths(
            self.root, ("docs/same-line.md",)
        )

        self.assertIn("H1_COUNT", {item.code for item in bypass.findings})
        self.assertEqual("DOC_CRITICAL_STRUCTURE_PASS", same_line.outcome)

    def test_html_comment_cannot_turn_invalid_text_into_a_fence(self) -> None:
        self.write(
            "CONTRIBUTING.md",
            "# Contributing to Kansas Frontier Matrix\n\n"
            "<!-- explanation --> ```\n"
            "# Contributing to Kansas Frontier Matrix\n"
            "```\n",
        )

        result = critical_structure.check_paths(
            self.root, ("CONTRIBUTING.md",)
        )

        self.assertIn("H1_COUNT", {item.code for item in result.findings})

    def test_tab_indentation_is_not_atx_or_fence_indentation(self) -> None:
        self.write(
            "docs/heading.md",
            "# Example\n\n\t# Indented code, not a heading\n",
        )
        self.write(
            "CONTRIBUTING.md",
            "# Contributing to Kansas Frontier Matrix\n\n"
            "\t```\n"
            "# Contributing to Kansas Frontier Matrix\n"
            "\t```\n",
        )

        heading = critical_structure.check_paths(
            self.root, ("docs/heading.md",)
        )
        bypass = critical_structure.check_paths(
            self.root, ("CONTRIBUTING.md",)
        )

        self.assertEqual("DOC_CRITICAL_STRUCTURE_PASS", heading.outcome)
        self.assertIn("H1_COUNT", {item.code for item in bypass.findings})

    def test_escaped_backticks_cannot_hide_duplicate_title(self) -> None:
        self.write(
            "CONTRIBUTING.md",
            "# Contributing to Kansas Frontier Matrix\n\n"
            "\\` # Contributing to Kansas Frontier Matrix \\`\n",
        )

        result = critical_structure.check_paths(
            self.root, ("CONTRIBUTING.md",)
        )

        self.assertEqual(
            ["TITLE_OCCURRENCE_COUNT"],
            [finding.code for finding in result.findings],
        )

    def test_many_unmatched_backtick_runs_remain_bounded(self) -> None:
        payload = " ".join("`" * length for length in range(1, 513))
        self.write("docs/example.md", f"# Example\n\n{payload}\n")

        result = critical_structure.check_paths(
            self.root, ("docs/example.md",)
        )

        self.assertEqual("DOC_CRITICAL_STRUCTURE_PASS", result.outcome)

    def test_inline_code_title_token_is_inert(self) -> None:
        self.write(
            "CONTRIBUTING.md",
            "# Contributing to Kansas Frontier Matrix\n\n"
            "## Status\n\n"
            "The literal `# Contributing to Kansas Frontier Matrix` is an example.\n",
        )

        result = critical_structure.check_paths(
            self.root, ("CONTRIBUTING.md",)
        )

        self.assertEqual("DOC_CRITICAL_STRUCTURE_PASS", result.outcome)

    def test_network_entrypoints_are_never_used(self) -> None:
        self.write("docs/example.md", "# Example\n\n## Status\n")
        with mock.patch.object(
            socket,
            "create_connection",
            side_effect=AssertionError("network used"),
        ), mock.patch.object(
            urllib.request,
            "urlopen",
            side_effect=AssertionError("network used"),
        ):
            result = critical_structure.check_paths(
                self.root, ("docs/example.md",)
            )

        self.assertEqual("DOC_CRITICAL_STRUCTURE_PASS", result.outcome)

    def test_cli_json_and_exit_polarity_are_deterministic(self) -> None:
        self.write("docs/example.md", "# Example\n\n## Repeat\n## Repeat\n")
        command = [
            sys.executable,
            str(MODULE_PATH),
            "--repo-root",
            str(self.root),
            "--format",
            "json",
            "docs/example.md",
        ]

        first = subprocess.run(command, check=False, capture_output=True, text=True)
        second = subprocess.run(command, check=False, capture_output=True, text=True)

        self.assertEqual(1, first.returncode)
        self.assertEqual(first.stdout, second.stdout)
        payload = json.loads(first.stdout)
        self.assertEqual("DOC_CRITICAL_STRUCTURE_FAIL", payload["outcome"])
        self.assertEqual("DUPLICATE_H2", payload["findings"][0]["code"])

    def test_symlink_and_escape_inputs_fail_closed(self) -> None:
        target = self.write("docs/target.md", "# Target\n")
        link = self.root / "docs/link.md"
        try:
            link.symlink_to(target)
        except (NotImplementedError, OSError):
            self.skipTest("symbolic links are unavailable on this platform")

        with self.assertRaisesRegex(
            critical_structure.StructureCheckError, "Symbolic-link"
        ):
            critical_structure.check_paths(self.root, ("docs/link.md",))
        with self.assertRaisesRegex(
            critical_structure.StructureCheckError,
            "normalized and repository-relative",
        ):
            critical_structure.check_paths(self.root, ("../outside.md",))

    def test_type_encoding_size_and_malformed_paths_fail_closed(self) -> None:
        self.write("docs/example.txt", "# Example\n")
        (self.root / "docs/invalid.md").write_bytes(b"# Invalid\n\xff")
        (self.root / "docs/large.md").write_bytes(
            b"# Large\n" + b"x" * critical_structure.MAX_MARKDOWN_BYTES
        )

        cases = (
            ("docs/example.txt", "not Markdown"),
            ("docs/invalid.md", "not readable UTF-8"),
            ("docs/large.md", "exceeds"),
            ("docs/line\nbreak.md", "empty or malformed"),
            ("/absolute.md", "normalized and repository-relative"),
        )
        for path, message in cases:
            with self.subTest(path=path), self.assertRaisesRegex(
                critical_structure.StructureCheckError, message
            ):
                critical_structure.check_paths(self.root, (path,))

    def test_cli_operational_error_uses_exit_two(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(MODULE_PATH),
                "--repo-root",
                str(self.root),
                "--format",
                "json",
                "docs/missing.md",
            ],
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertEqual(2, completed.returncode)
        self.assertEqual("ERROR", json.loads(completed.stdout)["outcome"])


if __name__ == "__main__":
    unittest.main()
