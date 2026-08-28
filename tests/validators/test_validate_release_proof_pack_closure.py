from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
import unittest

REPO_ROOT = Path(__file__).resolve().parents[2]
PATH = REPO_ROOT / "tools/validators/release/validate_release_proof_pack_closure.py"
spec = importlib.util.spec_from_file_location("release_pack", PATH)
assert spec is not None and spec.loader is not None
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
spec.loader.exec_module(mod)

ORCHESTRATOR_PATH = REPO_ROOT / "tools/validators/validate_all.py"
orchestrator_spec = importlib.util.spec_from_file_location(
    "kfm_release_pack_orchestrator", ORCHESTRATOR_PATH
)
assert orchestrator_spec is not None and orchestrator_spec.loader is not None
orchestrator = importlib.util.module_from_spec(orchestrator_spec)
sys.modules[orchestrator_spec.name] = orchestrator
orchestrator_spec.loader.exec_module(orchestrator)


class ReleaseProofPackClosureTests(unittest.TestCase):
    def test_complete_candidate_passes(self):
        record = {
            "object_type": "ReleaseProofPackClosure",
            "closure_id": "x",
            "candidate_state": "CANDIDATE",
            "release_manifest_ref": "manifest:1",
            "receipt_refs": ["receipt:1"],
            "proof_refs": ["proof:1"],
            "catalog_refs": ["catalog:1"],
            "review_refs": ["review:1"],
            "correction_ref": "correction:1",
            "rollback_ref": "rollback:1",
            "outcome": "PASS",
            "governance": {k: False for k in mod.AUTHORITY_FLAGS},
        }
        self.assertEqual("PASS", mod.validate(record))

    def test_empty_review_refs_denied(self):
        record = {
            "object_type": "ReleaseProofPackClosure",
            "closure_id": "x",
            "candidate_state": "CANDIDATE",
            "release_manifest_ref": "manifest:1",
            "receipt_refs": ["receipt:1"],
            "proof_refs": ["proof:1"],
            "catalog_refs": ["catalog:1"],
            "review_refs": [],
            "correction_ref": "correction:1",
            "rollback_ref": "rollback:1",
            "outcome": "PASS",
            "governance": {k: False for k in mod.AUTHORITY_FLAGS},
        }
        self.assertEqual("DENY", mod.validate(record))

    def test_authority_leak_denied(self):
        record = {
            "object_type": "ReleaseProofPackClosure",
            "closure_id": "x",
            "candidate_state": "HELD",
            "release_manifest_ref": "manifest:1",
            "receipt_refs": ["receipt:1"],
            "proof_refs": ["proof:1"],
            "catalog_refs": ["catalog:1"],
            "review_refs": ["review:1"],
            "correction_ref": "correction:1",
            "rollback_ref": "rollback:1",
            "outcome": "ABSTAIN",
            "governance": {k: False for k in mod.AUTHORITY_FLAGS},
        }
        record["governance"]["publication_authorized"] = True
        self.assertEqual("DENY", mod.validate(record))

    def test_registry_coordinates_release_proof_pack_closure(self):
        registry = orchestrator.load_registry(
            REPO_ROOT / "tools/validators/validator_registry.json",
            REPO_ROOT,
        )
        validator = registry.by_id["release-proof-pack-closure"]

        self.assertEqual(
            validator.script,
            "tools/validators/release/validate_release_proof_pack_closure.py",
        )
        self.assertEqual(validator.args, ("--fixtures",))
        self.assertNotIn(
            "release-proof-pack-closure", registry.profiles["focused"]
        )
        self.assertIn(
            "release-proof-pack-closure", registry.profiles["release-dry-run"]
        )
        self.assertIn("release-proof-pack-closure", registry.profiles["full"])
        self.assertGreater(
            registry.profiles["release-dry-run"].index(
                "release-proof-pack-closure"
            ),
            registry.profiles["release-dry-run"].index("release-manifest"),
        )
        self.assertGreater(
            registry.profiles["full"].index("release-proof-pack-closure"),
            registry.profiles["full"].index("release-manifest"),
        )

        representative_paths = (
            ".github/workflows/release-proof-pack-closure.yml",
            "contracts/release/release_proof_pack_closure.md",
            "schemas/contracts/v1/release/release_proof_pack_closure.schema.json",
            "fixtures/contracts/v1/release/release_proof_pack_closure/cases.json",
            "tests/validators/test_validate_release_proof_pack_closure.py",
            "tools/validators/release/validate_release_proof_pack_closure.py",
            "docs/intake/exploratory/pass9-release-proof-pack-closure-source-map.md",
        )
        for path in representative_paths:
            with self.subTest(path=path):
                selected, mode = orchestrator.select_validators(
                    registry,
                    profile="changed-area",
                    changed_paths=(path,),
                )
                self.assertEqual(mode, "changed-area")
                self.assertIn(
                    "release-proof-pack-closure",
                    {item.validator_id for item in selected},
                )

        code, report = orchestrator.orchestrate(
            registry,
            repo_root=REPO_ROOT,
            profile="release-dry-run",
            requested_ids=("release-proof-pack-closure",),
        )
        self.assertEqual(code, 0)
        self.assertEqual(report["outcome"], "PASS")
        self.assertEqual(report["selected_count"], 1)
        self.assertEqual(
            report["results"][0]["validator_id"],
            "release-proof-pack-closure",
        )


if __name__ == "__main__":
    unittest.main()
