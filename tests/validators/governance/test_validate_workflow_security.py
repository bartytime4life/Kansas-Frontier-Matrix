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
from contextlib import ExitStack, redirect_stdout
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

    def _duplicate_key_cases(self) -> dict[str, tuple[str, str]]:
        """Synthetic parser controls; none establishes GitHub runtime semantics."""
        safe = self._safe_workflow()
        credential = "          persist-credentials: false"
        step = "      - uses: actions/checkout@" + "a" * 40
        return {
            "persist-false-true": (safe.replace(credential, credential + "\n          persist-credentials: true # duplicate"), "persist-credentials"),
            "persist-true-false": (safe.replace(credential, "          persist-credentials: true\n" + credential + " # duplicate"), "persist-credentials"),
            "persist-same-value": (safe.replace(credential, credential + "\n" + credential + " # duplicate"), "persist-credentials"),
            "job-permissions-inline": (safe.replace("    steps:", "    permissions: {contents: read}\n    permissions: {contents: write} # duplicate\n    steps:"), "permissions"),
            "job-permissions-block": (safe.replace("    steps:", "    permissions:\n      contents: read\n    permissions: # duplicate\n      contents: write\n    steps:"), "permissions"),
            "permission-member": (safe.replace("    steps:", "    permissions:\n      contents: write\n      contents: read # duplicate\n    steps:"), "contents"),
            "with-block": (safe.replace(credential, credential + "\n        with: # duplicate\n          persist-credentials: true"), "with"),
            "with-empty-override": (safe.replace(credential, credential + "\n        with: {} # duplicate"), "with"),
            "step-first-key": (safe.replace(step, step + "\n        uses: actions/checkout@" + "a" * 40 + " # duplicate"), "uses"),
            "run-first-key": (safe.replace("      - run: python -m unittest", "      - run: echo first\n        run: echo second # duplicate"), "run"),
            "after-leading-run": (safe.replace("      - run: python -m unittest", "      - run: echo safe\n        env:\n          FLAG: first\n        env: # duplicate\n          FLAG: second"), "env"),
            "duplicate-job-id": (safe + safe.split("jobs:\n", 1)[1].replace("  validate:", "  validate: # duplicate", 1), "validate"),
            "duplicate-steps": (safe + "    steps: # duplicate\n" + safe.split("    steps:\n", 1)[1], "steps"),
            "duplicate-trigger": (safe.replace("  pull_request:", "  pull_request:\n  pull_request: # duplicate"), "pull_request"),
        }

    def test_duplicate_mapping_keys_fail_with_exact_invariant_diagnostics(self) -> None:
        for name, (text, key) in self._duplicate_key_cases().items():
            with self.subTest(case=name):
                self._write("duplicate.yml", text)
                findings, count = module.scan(self.root)
                self.assertEqual(1, count)
                self.assertEqual(1, len(findings), findings)
                finding = findings[0]
                line = next(i + 1 for i, value in enumerate(text.strip().splitlines()) if "# duplicate" in value)
                self.assertEqual("KFM-WF-001", finding.rule_id)
                self.assertEqual(line, finding.line)
                self.assertEqual(f"yaml-line={line}", finding.subject)
                self.assertEqual(module._digest(f"DUPLICATE_MAPPING_KEY:{key}"), finding.evidence_sha256)
                code, report = module.evaluate(findings, count, {}, as_of=date(2026, 9, 10))
                self.assertEqual((1, "FAIL_INVARIANT"), (code, report["outcome"]))
                self.assertEqual("FAIL_INVARIANT", report["findings"][0]["disposition"])

    def test_duplicate_inline_security_members_fail_closed(self) -> None:
        safe = self._safe_workflow()
        for key, text in {
            "with": safe.replace("        with:\n          persist-credentials: false", "        with: {persist-credentials: false, persist-credentials: true}"),
            "permissions": safe.replace("    steps:", "    permissions: {contents: read, contents: write}\n    steps:"),
        }.items():
            with self.subTest(key=key):
                self._write("inline.yml", text)
                findings, count = module.scan(self.root)
                self.assertEqual(1, len(findings), findings)
                self.assertEqual("KFM-WF-001", findings[0].rule_id)
                self.assertEqual(module._digest(f"AMBIGUOUS_INLINE_MAPPING:{key}"), findings[0].evidence_sha256)
                code, report = module.evaluate(findings, count, {})
                self.assertEqual((1, "FAIL_INVARIANT"), (code, report["outcome"]))

    def test_duplicate_scope_controls_remain_pass(self) -> None:
        safe = self._safe_workflow()
        checkout = safe.split("    steps:\n", 1)[1].split("      - run:", 1)[0]
        job = safe.split("jobs:\n", 1)[1].replace("  validate:", "  other:", 1)
        cases = {
            "unique": safe,
            "separate-jobs": safe + job,
            "separate-steps": safe.replace("      - run:", checkout + "      - run:"),
            "separate-child-maps": safe.replace("        with:", "        env:\n          FLAG: first\n        with:\n          FLAG: second"),
            "empty-dash-items": safe.replace("      - uses:", "      -\n        uses:").replace("      - run:", "      -\n        run:"),
            "inline-unique": safe.replace("        with:\n          persist-credentials: false", "        with: {persist-credentials: 'false'}"),
            "comments": safe.replace("          persist-credentials: false", "          persist-credentials: false\n          # persist-credentials: true\n          # with: {}"),
        }
        for key in ("path", "cache-dependency-path"):
            cases[key] = safe.replace("          persist-credentials: false", "          persist-credentials: false\n          " + key + ": |\n            entry: first\n            entry: second")
        for marker in ("|", "|-", "|+", ">", ">-", ">+"):
            cases["run-" + marker] = safe.replace("      - run: python -m unittest", "      - run: " + marker + "\n          entry: first\n          entry: second")
        for name, text in cases.items():
            with self.subTest(case=name):
                self._write("safe.yml", text)
                findings, count = module.scan(self.root)
                self.assertEqual((), findings)
                code, report = module.evaluate(findings, count, {})
                self.assertEqual((0, "PASS"), (code, report["outcome"]))

    def test_top_level_duplicate_fingerprint_remains_stable(self) -> None:
        text = self._safe_workflow() + "name: shadowed\n"
        self._write("top.yml", text)
        findings, _ = module.scan(self.root)
        line = len(text.strip().splitlines())
        self.assertEqual((module._finding("KFM-WF-001", ".github/workflows/top.yml", f"yaml-line={line}", "DUPLICATE_TOP_LEVEL_KEY:name", line),), findings)

    def test_duplicate_invariant_cannot_be_baselined(self) -> None:
        text, _ = self._duplicate_key_cases()["persist-false-true"]
        self._write("duplicate.yml", text)
        findings, count = module.scan(self.root)
        self.assertEqual(1, len(findings))
        finding = findings[0]
        self.assertEqual("KFM-WF-001", finding.rule_id)
        self.assertFalse(module.RULE_BY_ID[finding.rule_id].baseline_allowed)
        payload = module.candidate_baseline(findings, owner="test", closure_ref="fixture", generated_from_ref="fixture", expires_on="2026-12-31")
        self.assertEqual([], payload["entries"])
        entry = {key: getattr(finding, key) for key in ("evidence_sha256", "fingerprint", "path", "rule_id", "subject")}
        entry["expires_on"] = "2026-12-31"
        payload["entries"] = [entry]
        baseline = self.root / "forged-baseline.json"
        baseline.write_text(json.dumps(payload), encoding="utf-8")
        with self.assertRaisesRegex(module.BaselineError, "waive an invariant"):
            module.load_baseline(baseline)
        code, report = module.evaluate(findings, count, {finding.fingerprint: entry})
        self.assertEqual((1, "FAIL_INVARIANT"), (code, report["outcome"]))
        output = io.StringIO()
        with redirect_stdout(output):
            code = module.main(["--repo-root", str(self.root), "--emit-baseline"])
        self.assertEqual((2, "ERROR_VALIDATOR"), (code, json.loads(output.getvalue())["outcome"]))

    def test_duplicate_cli_exit_and_json_are_deterministic(self) -> None:
        for name in ("persist-false-true", "job-permissions-inline", "with-block"):
            with self.subTest(case=name):
                text, _ = self._duplicate_key_cases()[name]
                self._write("duplicate.yml", text)
                command = [sys.executable, "-B", str(MODULE_PATH), "--repo-root", str(self.root), "--no-baseline"]
                first = subprocess.run(command, capture_output=True, text=True, check=False, timeout=10)
                second = subprocess.run(command, capture_output=True, text=True, check=False, timeout=10)
                self.assertEqual((1, 1), (first.returncode, second.returncode))
                self.assertEqual("", first.stderr + second.stderr)
                self.assertEqual(first.stdout, second.stdout)
                report = json.loads(first.stdout)
                self.assertEqual("FAIL_INVARIANT", report["outcome"])
                self.assertEqual(["KFM-WF-001"], [item["rule_id"] for item in report["findings"]])
                self.assertTrue(all(value is False for value in report["authority"].values()))

    def test_duplicate_scan_remains_read_only_local_and_non_executing(self) -> None:
        text, _ = self._duplicate_key_cases()["persist-false-true"]
        self._write("duplicate.yml", text.replace("python -m unittest", "echo should-not-run > sentinel.txt"))
        before = {path.relative_to(self.root): path.read_bytes() for path in self.root.rglob("*") if path.is_file()}
        original_open = io.open

        def read_only_open(file, mode="r", *args, **kwargs):
            self.assertFalse(any(flag in mode for flag in "wax+"), mode)
            return original_open(file, mode, *args, **kwargs)

        with ExitStack() as stack:
            for target in ("socket.socket", "socket.create_connection", "urllib.request.urlopen", "subprocess.Popen", "os.system"):
                blocked = stack.enter_context(mock.patch(target, side_effect=AssertionError("forbidden scanner side effect")))
                stack.callback(blocked.assert_not_called)
            stack.enter_context(mock.patch("io.open", side_effect=read_only_open))
            stack.enter_context(mock.patch("builtins.open", side_effect=read_only_open))
            output = io.StringIO()
            with redirect_stdout(output):
                code = module.main(["--repo-root", str(self.root), "--no-baseline"])
            self.assertEqual((1, "FAIL_INVARIANT"), (code, json.loads(output.getvalue())["outcome"]))
        after = {path.relative_to(self.root): path.read_bytes() for path in self.root.rglob("*") if path.is_file()}
        self.assertEqual(before, after)



if __name__ == "__main__":
    unittest.main()
