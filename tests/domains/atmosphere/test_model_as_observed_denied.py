"""Atmosphere model-as-observed policy tests stay held until their subjects exist.

Planned intent (docs/domains/atmosphere/MISSING_OR_PLANNED_FILES.md): Negative test: model field as observation -> DENY.

Its policies (model_is_not_observation.rego, model-as-observed-deny.rego) are
default-deny scaffolds. Each check fails with
MODEL_AS_OBSERVED_DENIAL_NOT_IMPLEMENTED when its subject gains content, so the
real tests must land in the same change.

Validator-level denial already exists:
tools/validators/domains/atmosphere/validate_observed_modeled_separation.py, tested by
test_observed_modeled_separation.py (test_observation_and_model_cannot_substitute_for_each_other).
This hold covers the policy layer.
"""
from __future__ import annotations

import json
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
REASON = "MODEL_AS_OBSERVED_DENIAL_NOT_IMPLEMENTED"
POLICIES = (
    "policy/domains/atmosphere/model_is_not_observation.rego",
    "policy/domains/atmosphere/model-as-observed-deny.rego",
)


class HeldTests(unittest.TestCase):
    def test_policies_are_still_default_deny_scaffolds(self) -> None:
        for relative in POLICIES:
            lines = (REPO_ROOT / relative).read_text(encoding="utf-8").splitlines()
            rules = [line.strip() for line in lines if line.strip() and not line.strip().startswith("#")]
            self.assertTrue(rules and rules[0].startswith("package "), relative)
            self.assertEqual(rules[1:], ["default allow := false"],
                             f"{REASON}: {relative} now has rules. Replace this hold with tests that "
                             "exercise each rule on allowed and denied inputs.")


if __name__ == "__main__":
    unittest.main()
