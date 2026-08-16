from __future__ import annotations
import importlib.util, json, sys, tempfile, unittest
from pathlib import Path

PATH = Path(__file__).resolve().parents[2] / "tools/release/rollback_apply.py"
SPEC = importlib.util.spec_from_file_location("rollback_apply", PATH)
assert SPEC and SPEC.loader
m = importlib.util.module_from_spec(SPEC); sys.modules[SPEC.name] = m; SPEC.loader.exec_module(m)


def emit(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, sort_keys=True, indent=2) + "\n", encoding="utf-8")


class RehearsalTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory(); self.root = Path(self.tmp.name)
        (self.root / m.MARKER).write_text("synthetic-only\n", encoding="utf-8")
        self.current, self.prior = "release:synthetic:v2", "release:synthetic:v1"
        self.cm = self.install(self.current, b"current\n", self.prior)
        self.pm = self.install(self.prior, b"prior\n", None)
        self.alias = {"status": "ACTIVE", "release_id": self.current}
        emit(self.root / "published/current.json", self.alias)
        self.scenario = self.make("ROLLBACK")

    def tearDown(self) -> None: self.tmp.cleanup()

    def install(self, rid: str, data: bytes, previous: str | None) -> dict:
        d = self.root / "releases" / rid; d.mkdir(parents=True)
        (d / "artifact.txt").write_bytes(data)
        manifest = {"release_id": rid, "previous_release_id": previous,
                    "artifacts": [{"path": "artifact.txt", "digest": m.digest_bytes(data)}]}
        emit(d / "manifest.json", manifest); return manifest

    def make(self, operation: str) -> dict:
        target = self.prior if operation == "ROLLBACK" else None
        return {"scenario_id": f"rehearsal:{operation.lower()}:001", "synthetic": True,
                "operation": operation, "affected_release_id": self.current,
                "target_release_id": target,
                "correction": {"correction_id": f"correction:{operation.lower()}:001",
                               "reason_code": "SYNTHETIC_DEFECT",
                               "decided_at": "2026-08-16T00:00:00Z"},
                "invalidations": list(m.INVALIDATIONS),
                "expected": {"current_alias_digest": m.digest_bytes(m.canonical(self.alias)),
                             "affected_manifest_digest": m.digest_bytes(m.canonical(self.cm)),
                             "target_manifest_digest": m.digest_bytes(m.canonical(self.pm)) if target else None}}

    def test_plan_is_deterministic_and_no_write(self):
        a = m.rehearse(self.root, self.scenario); b = m.rehearse(self.root, self.scenario)
        self.assertEqual(a, b); self.assertEqual(a["mode"], "PLAN")
        self.assertFalse((self.root / "corrections").exists())

    def test_rollback_switches_alias_preserves_history_and_invalidates(self):
        before = (self.root / "releases" / self.current / "manifest.json").read_bytes()
        report = m.rehearse(self.root, self.scenario, apply=True)
        alias = json.loads((self.root / "published/current.json").read_text())
        self.assertEqual(alias["release_id"], self.prior); self.assertEqual(report["outcome"], "PASS")
        self.assertEqual(before, (self.root / "releases" / self.current / "manifest.json").read_bytes())
        self.assertTrue((self.root / "corrections" / "correction:rollback:001.json").is_file())
        inv = json.loads((self.root / "invalidations" / "rehearsal:rollback:001.json").read_text())
        self.assertEqual(inv["invalidations"], list(m.INVALIDATIONS))

    def test_withdrawal_removes_current_alias_and_retains_release(self):
        report = m.rehearse(self.root, self.make("WITHDRAWAL"), apply=True)
        self.assertEqual(report["after"]["current_alias"]["status"], "WITHDRAWN")
        self.assertTrue((self.root / "releases" / self.current / "artifact.txt").is_file())

    def test_non_synthetic_denied(self):
        self.scenario["synthetic"] = False
        with self.assertRaises(m.RehearsalError) as c: m.rehearse(self.root, self.scenario, apply=True)
        self.assertEqual(c.exception.code, "NON_SYNTHETIC_INPUT_DENIED")

    def test_incomplete_invalidations_denied(self):
        self.scenario["invalidations"] = ["API_CACHE"]
        with self.assertRaises(m.RehearsalError) as c: m.rehearse(self.root, self.scenario, apply=True)
        self.assertEqual(c.exception.code, "INVALIDATION_SET_INCOMPLETE")

    def test_wrong_target_denied(self):
        self.scenario["target_release_id"] = "release:synthetic:missing"
        with self.assertRaises(m.RehearsalError) as c: m.rehearse(self.root, self.scenario, apply=True)
        self.assertEqual(c.exception.code, "REQUIRED_FILE_MISSING")

    def test_digest_mismatch_denied(self):
        (self.root / "releases" / self.current / "artifact.txt").write_text("tampered\n")
        with self.assertRaises(m.RehearsalError) as c: m.rehearse(self.root, self.scenario, apply=True)
        self.assertEqual(c.exception.code, "ARTIFACT_DIGEST_MISMATCH")

    def test_missing_marker_denied(self):
        (self.root / m.MARKER).unlink()
        with self.assertRaises(m.RehearsalError) as c: m.rehearse(self.root, self.scenario, apply=True)
        self.assertEqual(c.exception.code, "SYNTHETIC_MARKER_MISSING")


if __name__ == "__main__": unittest.main()
