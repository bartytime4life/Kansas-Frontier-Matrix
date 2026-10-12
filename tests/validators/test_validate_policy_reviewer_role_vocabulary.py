import importlib.util
from pathlib import Path
import unittest

PATH = Path(__file__).resolve().parents[2] / "tools/validators/policy/validate_policy_reviewer_role_vocabulary.py"
spec = importlib.util.spec_from_file_location("reviewer_vocab", PATH)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class ReviewerRoleVocabularyTests(unittest.TestCase):
    def test_registry_passes(self):
        import json
        self.assertEqual("PASS", mod.validate(json.loads(mod.REGISTRY.read_text())))

    def test_duplicate_role_denied(self):
        record = {"roles":[{"code":"A_ROLE","review_scopes":["policy"]},{"code":"A_ROLE","review_scopes":["policy"]}],"governance":{k:False for k in mod.AUTHORITY_FLAGS}}
        self.assertEqual("DENY", mod.validate(record))

    def test_authority_leak_denied(self):
        record = {"roles":[{"code":"A_ROLE","review_scopes":["policy"]}],"governance":{k:False for k in mod.AUTHORITY_FLAGS}}
        record["governance"]["release_authorized"] = True
        self.assertEqual("DENY", mod.validate(record))


if __name__ == "__main__":
    unittest.main()
