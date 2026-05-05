import unittest
from pathlib import Path


class PolicyHomeTests(unittest.TestCase):
    def test_policy_root_exists_as_canonical_home(self):
        self.assertTrue(Path("policy").is_dir())

    def test_policies_root_allows_only_readme_or_migration_notes(self):
        root = Path("policies")
        if not root.exists():
            self.skipTest("policies/ root not present")

        violations = []
        for p in root.rglob("*"):
            if p.is_dir():
                continue
            rel = p.relative_to(root).as_posix()
            name = p.name.lower()
            if name == "readme.md":
                continue
            if "migration" in name or "migrate" in name:
                continue
            violations.append(rel)

        self.assertEqual(
            violations,
            [],
            msg=f"non-compatible files under policies/: {violations}; canonical policy files must live under policy/",
        )


if __name__ == "__main__":
    unittest.main()
