import copy
import importlib.util
import io
import json
from pathlib import Path
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

PATH = Path(__file__).resolve().parents[2] / "tools/validators/policy/validate_policy_reviewer_role_vocabulary.py"
spec = importlib.util.spec_from_file_location("reviewer_vocab", PATH)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

REGISTRY = json.loads(mod.REGISTRY.read_text())


def mutated(change):
    """The tracked registry with exactly one change, so a DENY can only come from that change."""
    record = copy.deepcopy(REGISTRY)
    change(record)
    return record


def role(record, index=2):
    return record["roles"][index]


class ReviewerRoleVocabularyTests(unittest.TestCase):
    def test_registry_passes(self):
        self.assertEqual("PASS", mod.validate(REGISTRY))

    def test_duplicate_role_denied(self):
        self.assertEqual("DENY", mod.validate(mutated(lambda r: r["roles"].insert(3, copy.deepcopy(role(r))))))

    def test_authority_leak_denied(self):
        self.assertEqual("DENY", mod.validate(mutated(lambda r: r["governance"].update(release_authorized=True))))

    def test_each_single_defect_is_denied(self):
        defects = {
            "role carries authority": lambda r: role(r).update(records_approval=True),
            "role names a person": lambda r: role(r).update(approver="alice"),
            "role description missing": lambda r: role(r).pop("description"),
            "role description too long": lambda r: role(r).update(description="x" * 241),
            # Each stays in sorted position, so only the code pattern can reject it.
            "role code has a hyphen": lambda r: role(r).update(code="POLICY-STEWARD"),
            "role code has lowercase": lambda r: role(r).update(code="POLICY_Steward"),
            "roles out of order": lambda r: r["roles"].reverse(),
            "scope unknown": lambda r: role(r).update(review_scopes=["publication"]),
            "scopes unsorted": lambda r: role(r, 0).update(review_scopes=["policy", "domain"]),
            "scope not a string": lambda r: role(r).update(review_scopes=[["policy"]]),
            "scopes mixed types": lambda r: role(r).update(review_scopes=[1, "policy"]),
            "alias shadows a later code": lambda r: role(r, 0).update(aliases=["POLICY_STEWARD"]),
            "alias repeats its own code": lambda r: role(r).update(aliases=["POLICY_STEWARD"]),
            "alias overlaps another alias": lambda r: (role(r, 0).update(aliases=["STEWARD"]), role(r).update(aliases=["STEWARD"])),
            "aliases not a list": lambda r: role(r).update(aliases="POLICY"),
            "aliases an integer": lambda r: role(r).update(aliases=5),
            "alias not a string": lambda r: role(r).update(aliases=[["x"]]),
            "alias empty": lambda r: role(r).update(aliases=[""]),
            "alias blank": lambda r: role(r).update(aliases=[" "]),
            "alias kebab-case": lambda r: role(r).update(aliases=["policy-steward"]),
            "alias is an address": lambda r: role(r).update(aliases=["alice@example.com"]),
            "status activated": lambda r: r.update(status="ACTIVE"),
            "wrong vocabulary": lambda r: r.update(vocabulary_id="policy-reviewer-role-vocabulary:v2"),
            "extra top-level key": lambda r: r.update(approvals=[]),
            "identity missing": lambda r: r.pop("object_type"),
            "governance flag missing": lambda r: r["governance"].pop("assigns_people"),
            "governance flag truthy": lambda r: r["governance"].update(assigns_people=0),
        }
        for name, change in defects.items():
            with self.subTest(name):
                self.assertEqual("DENY", mod.validate(mutated(change)))

    def test_distinct_aliases_are_allowed(self):
        record = mutated(lambda r: (role(r, 0).update(aliases=["DOMAIN_REVIEWER"]), role(r).update(aliases=["POLICY_REVIEWER"])))
        self.assertEqual("PASS", mod.validate(record))

    def test_non_object_inputs(self):
        self.assertEqual("ERROR", mod.validate([REGISTRY]))
        for record in ({}, {"roles": [], "governance": {}}, mutated(lambda r: r["roles"].insert(0, "POLICY_STEWARD"))):
            with self.subTest(record=str(record)[:40]):
                self.assertEqual("DENY", mod.validate(record))

    def test_fixture_denials_are_complete_records(self):
        """Each DENY fixture must be a whole vocabulary, so it fails for its named defect and not for a missing section."""
        cases = json.loads(mod.FIXTURES.read_text())["cases"]
        denials = [case for case in cases if case["expected"] == "DENY"]
        self.assertGreaterEqual(len(denials), 5)
        for case in denials:
            with self.subTest(case["name"]):
                self.assertEqual(set(case["record"]), set(REGISTRY))

    def test_cli_modes(self):
        for argv, expected in ((["--registry"], "PASS\n"), (["--fixtures"], "PASS 6 cases\n")):
            out = io.StringIO()
            with self.subTest(argv=argv), patch("sys.argv", ["validator", *argv]), redirect_stdout(out):
                try:
                    mod.main()
                except SystemExit as exit_:
                    self.assertEqual(exit_.code, 0)
                self.assertEqual(out.getvalue(), expected)
        with patch("sys.argv", ["validator"]), patch("sys.stderr", io.StringIO()), self.assertRaises(SystemExit) as exit_:
            mod.main()
        self.assertEqual(exit_.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
