from __future__ import annotations

import copy
import importlib.util
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = (
    REPO_ROOT
    / "tools/validators/directory_governance/validate_repository_topology.py"
)
SPEC = importlib.util.spec_from_file_location(
    "kfm_validate_repository_topology_output_security", MODULE_PATH
)
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


DIAGNOSTIC_SPEC = importlib.util.spec_from_file_location(
    "kfm_repository_topology_safe_diagnostics",
    MODULE_PATH.with_name("render_repository_topology_diagnostics.py"),
)
assert DIAGNOSTIC_SPEC is not None and DIAGNOSTIC_SPEC.loader is not None
diagnostics = importlib.util.module_from_spec(DIAGNOSTIC_SPEC)
# Reuse this test module's exact validator instance without leaking an import
# alias into other tests or substituting another implementation.
with mock.patch.dict(sys.modules, {"validate_repository_topology": module}):
    DIAGNOSTIC_SPEC.loader.exec_module(diagnostics)


class RepositoryTopologyOutputSecurityTests(unittest.TestCase):
    def test_trusted_baseline_enforcement_returns_no_caller_data(self) -> None:
        candidate_ref = "refs/heads/internal-baseline"
        resolved_sha = "a" * 40
        with (
            mock.patch.object(
                module,
                "_git",
                side_effect=[
                    (resolved_sha + "\n").encode("ascii"),
                    b"{}",
                ],
            ),
            mock.patch.object(module, "_load_baseline_bytes", return_value=({}, {})),
            mock.patch.object(module, "validate_baseline_transition") as transition,
        ):
            result = module.enforce_trusted_baseline(
                Path("."),
                {"generated_from_ref": "main@not-bootstrap"},
                {},
                candidate_ref,
            )

        self.assertIsNone(result)
        transition.assert_called_once()

    def test_cli_redacts_trusted_transition_without_echo(self) -> None:
        candidate_ref = "refs/heads/internal-baseline"
        resolved_sha = "b" * 40
        current_data = {
            "expires_on": "2026-11-10",
            "generated_from_ref": "main@not-bootstrap",
        }
        output = io.StringIO()

        with tempfile.TemporaryDirectory() as directory:
            baseline_path = Path(directory) / "baseline.json"
            baseline_path.write_text("{}\n", encoding="utf-8")
            with (
                mock.patch.object(module, "scan", return_value=((), 0)),
                mock.patch.object(
                    module,
                    "_load_baseline_bytes",
                    side_effect=[(current_data, {}), ({}, {})],
                ),
                mock.patch.object(
                    module,
                    "_git",
                    side_effect=[
                        (resolved_sha + "\n").encode("ascii"),
                        b"{}",
                    ],
                ),
                mock.patch.object(module, "validate_baseline_transition"),
                redirect_stdout(output),
            ):
                code = module.main(
                    [
                        "--repo-root",
                        str(REPO_ROOT),
                        "--baseline",
                        str(baseline_path),
                        "--trusted-baseline-ref",
                        candidate_ref,
                    ]
                )

        rendered = output.getvalue()
        report = json.loads(rendered)
        self.assertEqual(0, code, rendered)
        self.assertEqual("PASS", report["outcome"])
        self.assertEqual("[REDACTED]", report["baseline"]["trusted_transition"])
        self.assertNotIn(candidate_ref, rendered)
        self.assertNotIn(resolved_sha, rendered)

    def test_text_summary_never_receives_trusted_ref_data(self) -> None:
        candidate_ref = "refs/heads/internal-baseline"
        resolved_sha = "c" * 40
        current_data = {
            "expires_on": "2026-11-10",
            "generated_from_ref": "main@not-bootstrap",
        }
        output = io.StringIO()

        with tempfile.TemporaryDirectory() as directory:
            baseline_path = Path(directory) / "baseline.json"
            baseline_path.write_text("{}\n", encoding="utf-8")
            with (
                mock.patch.object(module, "scan", return_value=((), 0)),
                mock.patch.object(
                    module,
                    "_load_baseline_bytes",
                    side_effect=[(current_data, {}), ({}, {})],
                ),
                mock.patch.object(
                    module,
                    "_git",
                    side_effect=[
                        (resolved_sha + "\n").encode("ascii"),
                        b"{}",
                    ],
                ),
                mock.patch.object(module, "validate_baseline_transition"),
                redirect_stdout(output),
            ):
                code = module.main(
                    [
                        "--repo-root",
                        str(REPO_ROOT),
                        "--baseline",
                        str(baseline_path),
                        "--trusted-baseline-ref",
                        candidate_ref,
                        "--format",
                        "text",
                    ]
                )

        rendered = output.getvalue()
        self.assertEqual(0, code, rendered)
        self.assertTrue(rendered.startswith("PASS:"), rendered)
        self.assertNotIn(candidate_ref, rendered)
        self.assertNotIn(resolved_sha, rendered)

    def test_text_error_reports_only_exception_type(self) -> None:
        candidate_ref = "refs/heads/internal-baseline"
        resolved_sha = "d" * 40
        current_data = {
            "expires_on": "2026-11-10",
            "generated_from_ref": "main@not-bootstrap",
        }
        output = io.StringIO()

        with tempfile.TemporaryDirectory() as directory:
            baseline_path = Path(directory) / "baseline.json"
            baseline_path.write_text("{}\n", encoding="utf-8")
            with (
                mock.patch.object(module, "scan", return_value=((), 0)),
                mock.patch.object(
                    module,
                    "_load_baseline_bytes",
                    return_value=(current_data, {}),
                ),
                mock.patch.object(
                    module,
                    "enforce_trusted_baseline",
                    side_effect=module.TopologyError(
                        f"rejected {candidate_ref} at {resolved_sha}"
                    ),
                ),
                redirect_stdout(output),
            ):
                code = module.main(
                    [
                        "--repo-root",
                        str(REPO_ROOT),
                        "--baseline",
                        str(baseline_path),
                        "--trusted-baseline-ref",
                        candidate_ref,
                        "--format",
                        "text",
                    ]
                )

        rendered = output.getvalue()
        self.assertEqual(2, code, rendered)
        self.assertEqual("ERROR_VALIDATOR: TopologyError\n", rendered)
        self.assertNotIn(candidate_ref, rendered)
        self.assertNotIn(resolved_sha, rendered)


class DiagnosticLogSafetyTests(unittest.TestCase):
    """Synthetic report projection tests; these do not prove a repository scan."""

    @staticmethod
    def _finding(subject: str = "docs/example.md") -> dict[str, str]:
        return {
            "disposition": "FAIL_NEW_DRIFT",
            "rule_id": "KFM-TOPO-003",
            "subject": subject,
            "fingerprint": "sha256:" + "a" * 64,
        }

    def _line(self, finding: dict[str, str]) -> str:
        lines = diagnostics.render_diagnostics(
            {"findings": [finding]}, {}, max_items=20,
        )
        self.assertEqual(1, len(lines))
        return lines[0]

    def _assert_safe(self, line: str) -> None:
        self.assertTrue(all(32 <= ord(char) <= 126 for char in line), repr(line))
        self.assertEqual([line], line.splitlines())
        self.assertNotIn("::", line)
        self.assertNotIn("##[", line)

    def test_plain_identity_output_is_byte_compatible(self) -> None:
        for subject in ("docs/example.md", "doc-id:kfm://doc/example", "old_root-1.txt"):
            with self.subTest(subject=subject):
                row = self._finding(subject)
                self.assertEqual(
                    f"FAIL_NEW_DRIFT KFM-TOPO-003 subject={subject} "
                    f"fingerprint={row['fingerprint']}", self._line(row),
                )

    def test_control_and_unicode_subjects_round_trip_on_one_ascii_line(self) -> None:
        characters = [chr(value) for value in range(32)] + [
            chr(value) for value in range(127, 160)
        ] + ["\u200b", "\u2028", "\u2029", "\u202e", "\u2066", "\u2069", "é", "😀", "\ud800"]
        for char in characters:
            with self.subTest(character=repr(char)):
                subject = "before" + char + "after"
                line = self._line(self._finding(subject))
                self._assert_safe(line)
                token = line.split(" subject=", 1)[1].rsplit(" fingerprint=", 1)[0]
                self.assertEqual(subject, json.loads(token))

    def test_inline_runner_commands_are_data_even_without_a_newline(self) -> None:
        for subject in (
            "docs/::warning::forged", "prefix##[error]forged",
            "\n::group::forged\r::endgroup::", "::stop-commands::sentinel",
            "::add-mask::secret", "##[section]forged",
        ):
            with self.subTest(subject=subject):
                line = self._line(self._finding(subject))
                self._assert_safe(line)
                token = line.split(" subject=", 1)[1].rsplit(" fingerprint=", 1)[0]
                self.assertEqual(subject, json.loads(token))

    def test_every_finding_identity_field_is_encoded(self) -> None:
        for field in ("rule_id", "subject", "fingerprint"):
            with self.subTest(field=field):
                row = self._finding()
                row[field] = "\r\n::error::forged\x1b[2J"
                self._assert_safe(self._line(row))

    def test_stale_baseline_identity_fields_are_also_encoded(self) -> None:
        for field in ("rule_id", "subject", "fingerprint"):
            with self.subTest(field=field):
                row = self._finding()
                row[field] = "\n##[error]forged\u202e"
                fingerprint = row["fingerprint"]
                report = {"baseline": {"stale_fingerprints": [fingerprint]}}
                baseline = {fingerprint: row}
                lines = diagnostics.render_diagnostics(report, baseline, max_items=20)
                self.assertEqual(1, len(lines))
                self.assertTrue(lines[0].startswith("STALE_BASELINE "))
                self._assert_safe(lines[0])

    def test_quotes_backslashes_and_delimiters_keep_distinct_identity(self) -> None:
        subjects = ["path\nname", r"path\nname", "path name", 'path"name',
                    "path fingerprint=sha256:forged", "docs/::error::x", r"docs/\u003a\u003aerror"]
        rendered = set()
        for subject in subjects:
            line = self._line(self._finding(subject))
            self._assert_safe(line)
            token = line.split(" subject=", 1)[1].rsplit(" fingerprint=", 1)[0]
            self.assertEqual(subject, json.loads(token))
            rendered.add(line)
        self.assertEqual(len(subjects), len(rendered))

    def test_limit_and_sort_apply_before_display_encoding(self) -> None:
        rows = [self._finding("z"), self._finding("a\n"), self._finding("a")]
        report = {"findings": rows + [copy.deepcopy(rows[0])]}
        before = copy.deepcopy(report)
        first = diagnostics.render_diagnostics(report, {}, max_items=2)
        self.assertEqual(3, len(first))
        self.assertIn(" subject=a fingerprint=", first[0])
        self.assertIn(' subject="a\\n" fingerprint=', first[1])
        self.assertEqual("... 1 additional failure identities omitted", first[2])
        report["findings"].reverse()
        self.assertEqual(first, diagnostics.render_diagnostics(report, {}, max_items=2))
        report["findings"].reverse()
        self.assertEqual(before, report)

    def test_projection_preserves_inputs_and_omits_evidence(self) -> None:
        row = self._finding("unsafe\nsubject")
        row["evidence_members"] = ["PRIVATE-EVIDENCE"]
        row["evidence_sha256"] = "PRIVATE-DIGEST"
        report = {"findings": [row], "baseline": {"stale_fingerprints": [row["fingerprint"]]}}
        baseline = {row["fingerprint"]: copy.deepcopy(row)}
        before = copy.deepcopy((report, baseline))
        lines = diagnostics.render_diagnostics(report, baseline, max_items=20)
        self.assertEqual(before, (report, baseline))
        self.assertEqual(2, len(lines))
        for line in lines:
            self._assert_safe(line)
            self.assertNotIn("PRIVATE-", line)

    def test_malformed_identity_still_fails_closed(self) -> None:
        for field in ("rule_id", "subject", "fingerprint"):
            for value in (None, "", 42):
                with self.subTest(field=field, value=value):
                    row = self._finding()
                    row[field] = value
                    with self.assertRaisesRegex(
                        diagnostics.topology.TopologyError,
                        "report finding identity is malformed",
                    ):
                        self._line(row)

    def test_main_preserves_underlying_status_with_safe_output(self) -> None:
        for code, outcome in ((0, "PASS"), (1, "FAIL_NEW_DRIFT"), (2, "ERROR_VALIDATOR")):
            with self.subTest(code=code), tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / "baseline.json"
                path.write_bytes(b"{}\n")
                report = {
                    "outcome": outcome, "tracked_path_count": 1,
                    "counts": {"fail_invariant": 0, "fail_new_drift": 1, "baselined_warning": 0},
                    "findings": [self._finding("\n::error::forged")],
                    "baseline": {"stale_fingerprints": []},
                }
                output = io.StringIO()
                with (
                    mock.patch.object(diagnostics.topology, "scan", return_value=([], 1)),
                    mock.patch.object(diagnostics.topology, "_load_baseline_bytes",
                                      return_value=({"expires_on": "2026-11-10"}, {})),
                    mock.patch.object(diagnostics.topology, "evaluate", return_value=(code, report)),
                    mock.patch.dict("os.environ", {"KFM_TRUSTED_BASE_REF": ""}),
                    redirect_stdout(output),
                ):
                    result = diagnostics.main(["--baseline", str(path)])
                self.assertEqual(code, result)
                lines = output.getvalue().splitlines()
                self.assertEqual(2, len(lines))
                for line in lines:
                    self._assert_safe(line)
                self.assertTrue(lines[0].startswith(outcome + ":"))
                self.assertEqual(b"{}\n", path.read_bytes())


if __name__ == "__main__":
    unittest.main()
