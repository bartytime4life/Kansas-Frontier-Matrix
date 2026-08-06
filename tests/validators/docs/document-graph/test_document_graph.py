from __future__ import annotations

import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_PATCH_ROOT = Path(__file__).resolve().parents[4]
VALIDATOR_DIR = (
    REPO_PATCH_ROOT
    / "tools"
    / "validators"
    / "docs"
    / "document-graph"
)
VALIDATOR_PATH = VALIDATOR_DIR / "check_document_graph.py"
FIXTURE_ROOT = Path(__file__).parent / "fixtures" / "valid_repo"

spec = importlib.util.spec_from_file_location("kfm_document_graph", VALIDATOR_PATH)
if spec is None or spec.loader is None:  # pragma: no cover - import failure is fatal
    raise RuntimeError("could not load document-graph validator")
document_graph = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = document_graph
spec.loader.exec_module(document_graph)


class DocumentGraphTests(unittest.TestCase):
    maxDiff = None

    def _copy_fixture(self) -> tuple[tempfile.TemporaryDirectory[str], Path]:
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name) / "repo"
        shutil.copytree(FIXTURE_ROOT, root)
        return temporary, root

    def _build(
        self,
        root: Path,
        *,
        warnings_as_errors: bool = False,
    ):
        return document_graph.build_document_graph(
            repo_root=root,
            inputs=("README.md", "docs"),
            entrypoints=("README.md",),
            registry_path="control_plane/document_registry.yaml",
            warnings_as_errors=warnings_as_errors,
        )

    @staticmethod
    def _codes(result) -> set[str]:
        return {finding.code for finding in result.findings}

    def test_valid_fixture_builds_reachable_graph_with_backlinks(self) -> None:
        result = self._build(FIXTURE_ROOT)

        self.assertEqual(result.outcome, "DOC_GRAPH_PASS")
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.counts["documents"], 4)
        self.assertEqual(result.counts["edges"], 8)
        self.assertEqual(result.counts["reachable_documents"], 4)
        self.assertEqual(result.counts["orphan_documents"], 0)
        self.assertEqual(result.findings, ())

        documents = {str(item["path"]): item for item in result.documents}
        beta = documents["docs/domains/beta.md"]
        self.assertTrue(beta["reachable"])
        self.assertIn("docs/README.md", beta["backlinks"])
        self.assertIn("docs/architecture/alpha.md", beta["backlinks"])
        self.assertEqual(beta["registry_state"], "registered")

    def test_json_and_digest_are_deterministic(self) -> None:
        first = self._build(FIXTURE_ROOT)
        second = self._build(FIXTURE_ROOT)

        self.assertEqual(first.graph_digest, second.graph_digest)
        self.assertEqual(first.to_json(), second.to_json())
        payload = json.loads(first.to_json())
        self.assertEqual(payload["profile"], "kfm.docs.document-graph.v1")
        self.assertEqual(payload["outcome"], "DOC_GRAPH_PASS")
        self.assertTrue(payload["graph_digest"].startswith("sha256:"))

    def test_valid_fixture_matches_reviewed_snapshot(self) -> None:
        expected = json.loads(
            (FIXTURE_ROOT / "expected_document_graph.json").read_text(encoding="utf-8")
        )
        actual = json.loads(self._build(FIXTURE_ROOT).to_json())

        self.assertEqual(actual, expected)

    def test_markdown_workbench_contains_mocs_and_backlink_index(self) -> None:
        report = self._build(FIXTURE_ROOT).to_markdown()

        self.assertIn("# KFM Documentation Graph Workbench", report)
        self.assertIn("## Generated Maps of Content", report)
        self.assertIn("## Backlink Index", report)
        self.assertIn("docs/domains/beta.md", report)
        self.assertIn("not doctrine", report)

    def test_link_parser_ignores_fenced_and_inline_code(self) -> None:
        text = """
[visible](docs/README.md)

```markdown
[ignored](missing.md)
```

`[also ignored](missing-two.md)`
[reference][docs]
[docs]: docs/README.md
"""
        targets = [target for _line, target in document_graph.extract_links(text)]

        self.assertEqual(targets, ["docs/README.md", "docs/README.md"])

    def test_duplicate_document_identity_fails_closed(self) -> None:
        temporary, root = self._copy_fixture()
        self.addCleanup(temporary.cleanup)
        beta = root / "docs" / "domains" / "beta.md"
        beta.write_text(
            beta.read_text(encoding="utf-8").replace(
                "kfm://doc/fixture-beta", "kfm://doc/fixture-alpha"
            ),
            encoding="utf-8",
        )

        result = self._build(root)

        self.assertEqual(result.outcome, "DOC_GRAPH_FAIL")
        self.assertIn("DUPLICATE_DOC_ID", self._codes(result))

    def test_missing_metadata_path_relationship_fails_closed(self) -> None:
        temporary, root = self._copy_fixture()
        self.addCleanup(temporary.cleanup)
        beta = root / "docs" / "domains" / "beta.md"
        content = beta.read_text(encoding="utf-8").replace(
            "policy_label: public\n",
            "policy_label: public\nrelated:\n  - docs/missing.md\n",
        )
        beta.write_text(content, encoding="utf-8")

        result = self._build(root)

        self.assertEqual(result.outcome, "DOC_GRAPH_FAIL")
        self.assertIn("RELATED_TARGET_MISSING", self._codes(result))

    def test_missing_metadata_document_identity_relationship_fails_closed(self) -> None:
        temporary, root = self._copy_fixture()
        self.addCleanup(temporary.cleanup)
        beta = root / "docs" / "domains" / "beta.md"
        content = beta.read_text(encoding="utf-8").replace(
            "policy_label: public\n",
            "policy_label: public\nrelated:\n  - kfm://doc/not-present\n",
        )
        beta.write_text(content, encoding="utf-8")

        result = self._build(root)

        self.assertEqual(result.outcome, "DOC_GRAPH_FAIL")
        self.assertIn("RELATED_DOC_ID_MISSING", self._codes(result))

    def test_registry_identity_mismatch_fails_closed(self) -> None:
        temporary, root = self._copy_fixture()
        self.addCleanup(temporary.cleanup)
        registry = root / "control_plane" / "document_registry.yaml"
        registry.write_text(
            registry.read_text(encoding="utf-8").replace(
                "kfm://doc/fixture-beta", "kfm://doc/registry-beta"
            ),
            encoding="utf-8",
        )

        result = self._build(root)

        self.assertEqual(result.outcome, "DOC_GRAPH_FAIL")
        self.assertIn("REGISTRY_DOC_ID_MISMATCH", self._codes(result))

    def test_registry_non_markdown_entry_is_outside_graph_without_failure(self) -> None:
        temporary, root = self._copy_fixture()
        self.addCleanup(temporary.cleanup)
        registry = root / "control_plane" / "document_registry.yaml"
        registry.write_text(
            registry.read_text(encoding="utf-8")
            + "\n  - doc_id: kfm://registry/non-markdown\n"
            + "    path: control_plane/document_registry.yaml\n"
            + "    kind: machine_register\n"
            + "    authority: fixture\n"
            + "    status: active\n",
            encoding="utf-8",
        )

        result = self._build(root)

        self.assertEqual(result.outcome, "DOC_GRAPH_PASS")
        self.assertEqual(result.counts["registered_markdown_documents"], 4)

    def test_orphan_and_unreachable_document_are_visible_warnings(self) -> None:
        temporary, root = self._copy_fixture()
        self.addCleanup(temporary.cleanup)
        orphan = root / "docs" / "orphan.md"
        orphan.write_text("# Orphan fixture\n", encoding="utf-8")

        result = self._build(root)

        self.assertEqual(result.outcome, "DOC_GRAPH_WARN")
        self.assertIn("DOC_ORPHANED", self._codes(result))
        self.assertIn("DOC_UNREACHABLE", self._codes(result))
        self.assertEqual(result.exit_code, 0)

    def test_current_warnings_can_be_promoted_to_failures(self) -> None:
        temporary, root = self._copy_fixture()
        self.addCleanup(temporary.cleanup)
        (root / "docs" / "orphan.md").write_text("# Orphan fixture\n", encoding="utf-8")

        result = self._build(root, warnings_as_errors=True)

        self.assertEqual(result.outcome, "DOC_GRAPH_FAIL")
        self.assertEqual(result.exit_code, 1)
        self.assertTrue(
            all(
                finding.severity == "FAIL"
                for finding in result.findings
                if finding.code in {"DOC_ORPHANED", "DOC_UNREACHABLE"}
            )
        )

    def test_ratchet_downgrades_unchanged_failure_but_keeps_changed_failure(self) -> None:
        finding = document_graph.Finding(
            "FAIL",
            "DUPLICATE_DOC_ID",
            "docs/a.md",
            ("docs/b.md",),
            "duplicate",
        )

        historical = document_graph._ratchet_findings(
            (finding,), frozenset({"docs/c.md"}), git_diff_active=True
        )
        current = document_graph._ratchet_findings(
            (finding,), frozenset({"docs/b.md"}), git_diff_active=True
        )

        self.assertEqual(historical[0].severity, "WARN")
        self.assertTrue(historical[0].historical)
        self.assertEqual(current[0].severity, "FAIL")
        self.assertFalse(current[0].historical)

    def test_path_escape_in_metadata_fails_closed(self) -> None:
        temporary, root = self._copy_fixture()
        self.addCleanup(temporary.cleanup)
        alpha = root / "docs" / "architecture" / "alpha.md"
        alpha.write_text(
            alpha.read_text(encoding="utf-8").replace(
                "  - kfm://doc/fixture-beta\n",
                "  - kfm://doc/fixture-beta\n  - ../../../../outside.md\n",
            ),
            encoding="utf-8",
        )

        result = self._build(root)

        self.assertEqual(result.outcome, "DOC_GRAPH_FAIL")
        self.assertIn("PATH_ESCAPE", self._codes(result))

    @unittest.skipUnless(hasattr(Path, "symlink_to"), "symlinks unavailable")
    def test_symbolic_link_in_scope_is_denied(self) -> None:
        temporary, root = self._copy_fixture()
        self.addCleanup(temporary.cleanup)
        target = root / "docs" / "domains" / "beta.md"
        link = root / "docs" / "linked.md"
        try:
            link.symlink_to(target)
        except OSError as error:
            self.skipTest(f"symlink creation unavailable: {error}")

        with self.assertRaises(document_graph.DocumentGraphError):
            self._build(root)

    def test_cli_emits_json_and_expected_exit_codes(self) -> None:
        valid = subprocess.run(
            [
                sys.executable,
                str(VALIDATOR_PATH),
                "--repo-root",
                str(FIXTURE_ROOT),
                "--entrypoint",
                "README.md",
                "--registry",
                "control_plane/document_registry.yaml",
                "--format",
                "json",
                "README.md",
                "docs",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(valid.returncode, 0, valid.stderr)
        self.assertEqual(json.loads(valid.stdout)["outcome"], "DOC_GRAPH_PASS")

        temporary, root = self._copy_fixture()
        self.addCleanup(temporary.cleanup)
        beta = root / "docs" / "domains" / "beta.md"
        beta.write_text(
            beta.read_text(encoding="utf-8").replace(
                "kfm://doc/fixture-beta", "kfm://doc/fixture-alpha"
            ),
            encoding="utf-8",
        )
        invalid = subprocess.run(
            [
                sys.executable,
                str(VALIDATOR_PATH),
                "--repo-root",
                str(root),
                "--entrypoint",
                "README.md",
                "--registry",
                "control_plane/document_registry.yaml",
                "--format",
                "json",
                "README.md",
                "docs",
            ],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(invalid.returncode, 1, invalid.stderr)
        self.assertEqual(json.loads(invalid.stdout)["outcome"], "DOC_GRAPH_FAIL")

    def test_source_contains_no_network_client(self) -> None:
        source = "\n".join(
            path.read_text(encoding="utf-8")
            for path in sorted(VALIDATOR_DIR.glob("*.py"))
        )
        forbidden = ("urllib.request", "requests.", "httpx.", "socket.", "urlopen(")
        for token in forbidden:
            self.assertNotIn(token, source)


if __name__ == "__main__":
    unittest.main()
