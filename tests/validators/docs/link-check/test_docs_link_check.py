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
MODULE_PATH = REPO_ROOT / "tools/validators/docs/link-check/check_links.py"
SPEC = importlib.util.spec_from_file_location("kfm_docs_link_check", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
link_check = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = link_check
SPEC.loader.exec_module(link_check)


class DocsLinkCheckTests(unittest.TestCase):
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

    def run_check(self, *paths: str):
        return link_check.check_paths(
            self.root,
            paths,
            scope="synthetic_fixture",
        )

    def test_accepts_local_files_directories_images_and_anchors(self) -> None:
        self.write(
            "docs/source.md",
            "# Source\n\n[heading](target.md#target-heading)\n"
            "[explicit](target.md#named-anchor)\n"
            "[directory](child/)\n![image](assets/pixel.png)\n",
        )
        self.write(
            "docs/target.md",
            '<a id="named-anchor"></a>\n\n# Target Heading\n',
        )
        self.write("docs/child/README.md", "# Child\n")
        self.write("docs/assets/pixel.png", "synthetic-not-a-real-image\n")

        result = self.run_check("docs/source.md")

        self.assertEqual(result.outcome, "DOC_LINK_CHECK_PASS")
        self.assertEqual(result.checked_local_targets, 4)
        self.assertEqual(result.findings, ())

    def test_rejects_missing_target_and_missing_anchor_deterministically(self) -> None:
        self.write(
            "docs/source.md",
            "# Source\n\n[missing](absent.md)\n[anchor](target.md#absent)\n",
        )
        self.write("docs/target.md", "# Present\n")

        first = self.run_check("docs/source.md")
        second = self.run_check("docs/source.md")

        self.assertEqual(first.exit_code, 1)
        self.assertEqual(first.to_json(), second.to_json())
        self.assertEqual(
            [finding.outcome for finding in first.findings],
            ["LOCAL_TARGET_MISSING", "ANCHOR_MISSING"],
        )

    def test_rejects_case_mismatch_and_path_escape(self) -> None:
        self.write(
            "docs/source.md",
            "# Source\n\n[case](Target.md)\n[escape](../../outside.md)\n",
        )
        self.write("docs/target.md", "# Target\n")
        outside = self.root.parent / "outside.md"
        outside.write_text("# Outside\n", encoding="utf-8")
        self.addCleanup(outside.unlink, missing_ok=True)

        result = self.run_check("docs/source.md")

        self.assertEqual(
            [finding.outcome for finding in result.findings],
            ["LOCAL_TARGET_MISSING", "PATH_ESCAPE"],
        )

    def test_external_targets_are_unverified_and_never_requested(self) -> None:
        self.write(
            "docs/source.md",
            "# Source\n\n[web](https://example.invalid/path)\n"
            "![remote](https://example.invalid/image.png)\n",
        )
        with mock.patch.object(
            socket, "create_connection", side_effect=AssertionError("network used")
        ), mock.patch.object(
            urllib.request, "urlopen", side_effect=AssertionError("network used")
        ):
            result = self.run_check("docs/source.md")

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.external_targets_unverified, 2)
        self.assertEqual(
            {finding.outcome for finding in result.findings},
            {"EXTERNAL_TARGET_UNVERIFIED"},
        )
        self.assertEqual(
            {finding.target for finding in result.findings},
            {"https://example.invalid"},
        )
        self.assertNotIn("/path", result.to_json())
        self.assertNotIn("/image.png", result.to_json())

    def test_ignores_fenced_code_inline_code_and_html_comments(self) -> None:
        self.write(
            "docs/source.md",
            "# Source\n\n`[inline](missing.md)`\n\n"
            "```markdown\n[fenced](missing.md)\n```\n"
            "<!-- [comment](missing.md) -->\n",
        )

        result = self.run_check("docs/source.md")

        self.assertEqual(result.outcome, "DOC_LINK_CHECK_PASS")
        self.assertEqual(result.checked_local_targets, 0)

    def test_duplicate_heading_slugs_match_github_suffixes(self) -> None:
        self.write("docs/source.md", "[second](target.md#repeat-1)\n")
        self.write("docs/target.md", "# Repeat\n\n# Repeat\n")

        self.assertEqual(self.run_check("docs/source.md").exit_code, 0)

    def test_accepts_full_collapsed_shortcut_and_image_references(self) -> None:
        self.write(
            "docs/source.md",
            "[full][Target   Ref]\n"
            "[Target Ref][]\n"
            "[target ref]\n"
            "![image][image ref]\n\n"
            "[target ref]: target.md#target-heading \"optional title\"\n"
            "[image ref]: assets/pixel.png\n",
        )
        self.write("docs/target.md", "# Target Heading\n")
        self.write("docs/assets/pixel.png", "synthetic-not-a-real-image\n")

        result = self.run_check("docs/source.md")

        self.assertEqual(result.outcome, "DOC_LINK_CHECK_PASS")
        self.assertEqual(result.checked_local_targets, 4)
        self.assertEqual(result.findings, ())

    def test_reference_definitions_are_first_wins(self) -> None:
        self.write(
            "docs/source.md",
            "[first definition][duplicate]\n\n"
            "[duplicate]: target.md\n"
            "[DUPLICATE]: missing.md\n",
        )
        self.write("docs/target.md", "# Target\n")

        result = self.run_check("docs/source.md")

        self.assertEqual(result.outcome, "DOC_LINK_CHECK_PASS")
        self.assertEqual(result.checked_local_targets, 1)

    def test_reference_targets_fail_with_existing_local_outcomes(self) -> None:
        self.write(
            "docs/source.md",
            "[missing file][missing-ref]\n"
            "[missing anchor][anchor-ref]\n\n"
            "[missing-ref]: absent.md\n"
            "[anchor-ref]: target.md#absent\n",
        )
        self.write("docs/target.md", "# Present\n")

        result = self.run_check("docs/source.md")

        self.assertEqual(result.exit_code, 1)
        self.assertEqual(
            [finding.outcome for finding in result.findings],
            ["LOCAL_TARGET_MISSING", "ANCHOR_MISSING"],
        )

    def test_external_reference_targets_are_unverified_without_network(self) -> None:
        self.write(
            "docs/source.md",
            "[web][external]\n![remote][external image]\n\n"
            "[external]: https://example.invalid/path\n"
            "[external image]: https://example.invalid/image.png\n",
        )
        with mock.patch.object(
            socket, "create_connection", side_effect=AssertionError("network used")
        ), mock.patch.object(
            urllib.request, "urlopen", side_effect=AssertionError("network used")
        ):
            result = self.run_check("docs/source.md")

        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.external_targets_unverified, 2)
        self.assertEqual(
            {finding.outcome for finding in result.findings},
            {"EXTERNAL_TARGET_UNVERIFIED"},
        )
        self.assertNotIn("/path", result.to_json())
        self.assertNotIn("/image.png", result.to_json())

    def test_undefined_reference_like_citations_remain_out_of_scope(self) -> None:
        self.write(
            "docs/source.md",
            "[DOM-AIR][ENCY]\n[plain bracketed text]\n[^footnote]\n",
        )

        result = self.run_check("docs/source.md")

        self.assertEqual(result.outcome, "DOC_LINK_CHECK_PASS")
        self.assertEqual(result.checked_local_targets, 0)

    def test_github_heading_slugs_preserve_markup_content_and_spaces(self) -> None:
        self.write(
            "docs/source.md",
            "[inline code](target.md#2-focusmodepayload-semantic-shape)\n"
            "[em dash](target.md#appendix-a--no-loss-preservation)\n"
            "[slash](target.md#input--output-boundary)\n"
            "[arrow](target.md#plan--payload-crosswalk)\n"
            "[ampersand](target.md#contracts--schemas)\n"
            "[styled](target.md#diagram--linked-heading)\n"
            "[code placeholder](target.md#phase-payload)\n"
            "[duplicate](target.md#plan--payload-crosswalk-1)\n",
        )
        self.write(
            "docs/target.md",
            "# 2. `FocusModePayload` semantic shape\n\n"
            "# Appendix A — No-loss preservation\n\n"
            "# Input / output boundary\n\n"
            "# Plan → payload crosswalk\n\n"
            "# Contracts & schemas\n\n"
            "# ![Diagram](synthetic.png) & [linked heading](https://example.invalid)\n\n"
            "# `<phase>` payload\n\n"
            "# Plan → payload crosswalk\n",
        )

        result = self.run_check("docs/source.md")

        self.assertEqual(result.outcome, "DOC_LINK_CHECK_PASS")
        self.assertEqual(result.checked_local_targets, 8)
        self.assertEqual(result.findings, ())

    def test_inline_code_does_not_create_an_explicit_html_anchor(self) -> None:
        self.write("docs/source.md", "[anchor](target.md#not-an-anchor)\n")
        self.write(
            "docs/target.md",
            "# Target\n\n`<a id=\"not-an-anchor\"></a>`\n",
        )

        result = self.run_check("docs/source.md")

        self.assertEqual(result.exit_code, 1)
        self.assertEqual(
            [finding.outcome for finding in result.findings],
            ["ANCHOR_MISSING"],
        )

    def test_cli_emits_stable_json_and_exit_polarity(self) -> None:
        self.write("docs/source.md", "[missing](absent.md)\n")
        command = [
            sys.executable,
            str(MODULE_PATH),
            "--repo-root",
            str(self.root),
            "--format",
            "json",
            "docs/source.md",
        ]

        completed = subprocess.run(command, check=False, capture_output=True, text=True)
        payload = json.loads(completed.stdout)

        self.assertEqual(completed.returncode, 1)
        self.assertEqual(payload["outcome"], "DOC_LINK_CHECK_FAIL")
        self.assertEqual(payload["findings"][0]["source"], "docs/source.md")

    def test_git_diff_spec_is_strict(self) -> None:
        with self.assertRaisesRegex(link_check.LinkCheckError, "Git diff spec"):
            link_check.discover_git_diff(self.root, "--name-only")

    def test_empty_changed_markdown_scope_is_explicit(self) -> None:
        result = link_check.check_paths(
            self.root,
            (),
            scope="changed_markdown_empty",
        )

        self.assertEqual(result.outcome, "DOC_LINK_CHECK_PASS")
        self.assertEqual(result.checked_documents, 0)
        self.assertEqual(result.scope, "changed_markdown_empty")

    def test_symbolic_link_inputs_fail_closed(self) -> None:
        target = self.write("docs/target.md", "# Target\n")
        link = self.root / "docs/link.md"
        try:
            link.symlink_to(target)
        except (NotImplementedError, OSError):
            self.skipTest("symbolic links are unavailable on this platform")

        with self.assertRaisesRegex(link_check.LinkCheckError, "Symbolic-link"):
            self.run_check("docs/link.md")

    def test_git_diff_discovers_changed_markdown_only(self) -> None:
        def git(*arguments: str) -> str:
            completed = subprocess.run(
                ["git", "-C", str(self.root), *arguments],
                check=True,
                capture_output=True,
                text=True,
            )
            return completed.stdout.strip()

        git("init", "--quiet")
        self.write("docs/source.md", "# Initial\n")
        self.write("docs/ignored.txt", "initial\n")
        git("add", ".")
        git(
            "-c",
            "user.name=KFM Test",
            "-c",
            "user.email=kfm-test@example.invalid",
            "commit",
            "--quiet",
            "-m",
            "base",
        )
        base_sha = git("rev-parse", "HEAD")

        self.write("docs/source.md", "# Changed\n")
        self.write("docs/ignored.txt", "changed\n")
        git("add", ".")
        git(
            "-c",
            "user.name=KFM Test",
            "-c",
            "user.email=kfm-test@example.invalid",
            "commit",
            "--quiet",
            "-m",
            "head",
        )

        paths = link_check.discover_git_diff(self.root, f"{base_sha}...HEAD")

        self.assertEqual(paths, ("docs/source.md",))


if __name__ == "__main__":
    unittest.main()
