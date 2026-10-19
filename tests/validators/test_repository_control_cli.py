"""The repository-control CLI: exit codes, outputs and strict-JSON input handling."""
from __future__ import annotations

import io
import json
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory

from jsonschema import Draft202012Validator, FormatChecker

from tools.validators.repository_control import validate_repository_control as cli
from tools.validators.repository_control._model import (
    InputError,
    compute_state_digest,
    load_json,
)

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "control_plane/repository_control_state.yaml"
FIXTURES = ROOT / "tests/fixtures/governance/repository_control"
OUTCOME_SCHEMA = ROOT / "schemas/contracts/v1/governance/ci_outcome.schema.json"


def run(*argv: str | Path) -> tuple[int, str, str]:
    out, err = io.StringIO(), io.StringIO()
    with redirect_stdout(out), redirect_stderr(err):
        code = cli.main([str(a) for a in argv])
    return code, out.getvalue(), err.getvalue()


class CommandTests(unittest.TestCase):
    def setUp(self):
        self.temporary = TemporaryDirectory()
        self.dir = Path(self.temporary.name)
        self.addCleanup(self.temporary.cleanup)

    def write(self, name: str, content: str | bytes) -> Path:
        path = self.dir / name
        path.write_bytes(content.encode() if isinstance(content, str) else content)
        return path

    def test_digest_prints_the_state_digest(self):
        code, out, _ = run("digest", "--state", STATE)
        self.assertEqual((code, out.strip()), (0, compute_state_digest(load_json(STATE))))

    def test_validate_state_passes_the_tracked_state_and_lists_findings_otherwise(self):
        self.assertEqual(run("validate-state", "--state", STATE)[:2], (0, "PASS: STATE_VALID\n"))
        broken = json.loads(STATE.read_text(encoding="utf-8"))
        del broken["permissions"]
        code, out, err = run("validate-state", "--state", self.write("broken.json", json.dumps(broken)))
        self.assertEqual((code, out), (1, ""))
        self.assertRegex(err, r"^[A-Z_]+: ")

    def test_evaluate_prints_and_writes_a_schema_valid_outcome_with_its_exit_code(self):
        outcome_path = self.dir / "nested/outcome.json"
        code, out, _ = run("evaluate", "--state", STATE, "--context", FIXTURES / "context_expected_hold.json",
                           "--outcome-json", outcome_path)
        self.assertEqual(code, 3)
        lines = out.splitlines()
        self.assertTrue(lines[0].startswith("EXPECTED_READINESS_HOLD: "))
        written = json.loads(outcome_path.read_text(encoding="utf-8"))
        self.assertEqual(json.loads(lines[-1]), written, "stdout and the outcome file carry the same record")
        Draft202012Validator(json.loads(OUTCOME_SCHEMA.read_text(encoding="utf-8")), format_checker=FormatChecker()).validate(written)
        code, out, _ = run("evaluate", "--state", STATE, "--context", FIXTURES / "context_pr_1829_terminal_divergence.json")
        self.assertEqual(code, 1)
        self.assertTrue(out.startswith("REGRESSION: TERMINAL_STATE_DIVERGENCE"))
        self.assertIn("\n- ", out, "findings are listed")

    def test_exit_codes_cover_the_whole_outcome_vocabulary(self):
        self.assertEqual({o: cli._exit(o) for o in ("PASS", "NOT_APPLICABLE", "SKIPPED_EXPLICIT", "REGRESSION", "UNKNOWN",
                                                       "EXPECTED_READINESS_HOLD")},
                         {"PASS": 0, "NOT_APPLICABLE": 0, "SKIPPED_EXPLICIT": 3, "REGRESSION": 1, "UNKNOWN": 2,
                          "EXPECTED_READINESS_HOLD": 3})

    def test_unusable_state_or_context_is_a_regression_not_a_traceback(self):
        cases = {
            "duplicate.json": '{"a": 1, "a": 2}',
            "nested_duplicate.json": '{"a": {"b": 1, "b": 1}}',
            "nan.json": '{"a": NaN}',
            "infinity.json": '{"a": -Infinity}',
            "overflow.json": '{"a": 1e400}',
            "negative_overflow.json": '{"a": [-1.5e999]}',
            "utf8.json": b'{"a": "\xff"}',
            "deep.json": '{"a": ' + "[" * 100_000 + "]" * 100_000 + "}",
            "huge_int.json": '{"a": ' + "9" * 5000 + "}",
            "list.json": "[]",
            "truncated.json": '{"a": ',
        }
        for name, content in cases.items():
            path = self.write(name, content)
            with self.subTest(name=name):
                code, out, err = run("digest", "--state", path)
                self.assertEqual((code, out), (1, ""))
                self.assertTrue(err.startswith("REGRESSION: STATE_INPUT_INVALID\n"))
                code, _, err = run("evaluate", "--state", STATE, "--context", path)
                self.assertEqual(code, 1)
                self.assertTrue(err.startswith("REGRESSION: CONTEXT_INPUT_INVALID\n"))
        code, _, err = run("validate-state", "--state", self.dir / "missing.json")
        self.assertEqual((code, err.splitlines()[0]), (1, "REGRESSION: STATE_INPUT_INVALID"))

    def test_strict_loader_names_the_offending_key_or_constant(self):
        with self.assertRaisesRegex(InputError, "duplicate JSON key: a"):
            load_json(self.write("d.json", '{"a": 1, "a": 2}'))
        with self.assertRaisesRegex(InputError, "non-standard JSON constant: NaN"):
            load_json(self.write("n.json", '{"a": NaN}'))
        with self.assertRaisesRegex(InputError, "non-finite value: 1e400"):
            load_json(self.write("o.json", '{"a": 1e400}'))
        self.assertEqual(load_json(self.write("ok.json", '{"a": [1.5, 1e308, {"b": null}]}')), {"a": [1.5, 1e308, {"b": None}]})


if __name__ == "__main__":
    unittest.main()
