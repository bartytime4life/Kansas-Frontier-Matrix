import importlib.util
from pathlib import Path
import unittest

PATH = Path(__file__).resolve().parents[2] / "tools/validators/release/validate_release_proof_pack_closure.py"
spec = importlib.util.spec_from_file_location("release_pack", PATH)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class ReleaseProofPackClosureTests(unittest.TestCase):
    def test_complete_candidate_passes(self):
        record = {"object_type":"ReleaseProofPackClosure","closure_id":"x","candidate_state":"CANDIDATE","release_manifest_ref":"manifest:1","receipt_refs":["receipt:1"],"proof_refs":["proof:1"],"catalog_refs":["catalog:1"],"review_refs":["review:1"],"correction_ref":"correction:1","rollback_ref":"rollback:1","outcome":"PASS","governance":{k:False for k in mod.AUTHORITY_FLAGS}}
        self.assertEqual("PASS", mod.validate(record))

    def test_empty_review_refs_denied(self):
        record = {"object_type":"ReleaseProofPackClosure","closure_id":"x","candidate_state":"CANDIDATE","release_manifest_ref":"manifest:1","receipt_refs":["receipt:1"],"proof_refs":["proof:1"],"catalog_refs":["catalog:1"],"review_refs":[],"correction_ref":"correction:1","rollback_ref":"rollback:1","outcome":"PASS","governance":{k:False for k in mod.AUTHORITY_FLAGS}}
        self.assertEqual("DENY", mod.validate(record))

    def test_authority_leak_denied(self):
        record = {"object_type":"ReleaseProofPackClosure","closure_id":"x","candidate_state":"HELD","release_manifest_ref":"manifest:1","receipt_refs":["receipt:1"],"proof_refs":["proof:1"],"catalog_refs":["catalog:1"],"review_refs":["review:1"],"correction_ref":"correction:1","rollback_ref":"rollback:1","outcome":"ABSTAIN","governance":{k:False for k in mod.AUTHORITY_FLAGS}}
        record["governance"]["publication_authorized"] = True
        self.assertEqual("DENY", mod.validate(record))


if __name__ == "__main__":
    unittest.main()
