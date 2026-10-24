from __future__ import annotations
import importlib.util, json, sys, tempfile, unittest
from pathlib import Path
from unittest.mock import patch

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

    def test_apply_ignores_preexisting_temporary_siblings(self):
        sentinel = self.root / "sentinel.txt"
        sentinel.write_text("synthetic sentinel\n", encoding="utf-8")
        outputs = [
            self.root / "published/current.json",
            self.root / "corrections/correction:rollback:001.json",
            self.root / "invalidations/rehearsal:rollback:001.json",
        ]
        for output in outputs:
            output.parent.mkdir(parents=True, exist_ok=True)
            output.with_name(output.name + ".tmp").symlink_to(sentinel)

        self.assertEqual(m.rehearse(self.root, self.scenario, apply=True)["outcome"], "PASS")
        self.assertEqual(sentinel.read_text(encoding="utf-8"), "synthetic sentinel\n")
        for output in outputs:
            self.assertFalse(output.is_symlink())
            self.assertIsInstance(json.loads(output.read_text(encoding="utf-8")), dict)
            self.assertTrue(output.with_name(output.name + ".tmp").is_symlink())
            self.assertEqual(list(output.parent.glob(f".{output.name}.*.tmp")), [])

    def test_failed_replace_preserves_destination_and_removes_own_temporary(self):
        output = self.root / "published/current.json"
        before = output.read_bytes()
        with patch.object(m.os, "replace", side_effect=OSError("synthetic failure")):
            with self.assertRaises(OSError):
                m.write_json(output, {"fixture": "synthetic"})
        self.assertEqual(output.read_bytes(), before)
        self.assertEqual(list(output.parent.glob(".current.json.*.tmp")), [])

        report = m.rehearse(self.root, self.scenario, apply=True)
        self.assertEqual(json.loads(output.read_text()), report["after"]["current_alias"])
        self.assertEqual(list(output.parent.glob(".current.json.*.tmp")), [])

    def test_safe_rejects_live_and_dangling_leaf_and_parent_links(self):
        for directory in (False, True):
            for dangling in (False, True):
                with self.subTest(directory=directory, dangling=dangling):
                    target = self.root / f"target-{directory}-{dangling}"
                    if not dangling:
                        if directory:
                            target.mkdir()
                            (target / "child.json").write_bytes(b"sentinel\n")
                        else:
                            target.write_bytes(b"sentinel\n")
                    link = self.root / f"link-{directory}-{dangling}"
                    link.symlink_to(target.name, target_is_directory=directory)
                    relative = link.name + ("/child.json" if directory else "")
                    with self.assertRaises(m.RehearsalError) as caught:
                        m.safe(self.root, relative)
                    self.assertEqual(caught.exception.code, "UNSAFE_SYMLINK")
                    self.assertTrue(link.is_symlink())
                    if dangling:
                        self.assertFalse(target.exists())
                    else:
                        sentinel = target / "child.json" if directory else target
                        self.assertEqual(sentinel.read_bytes(), b"sentinel\n")

    def test_safe_accepts_regular_files_and_missing_output_paths(self):
        for relative in ("published/current.json",
                         f"releases/{self.current}/artifact.txt",
                         "corrections/new/note.json"):
            with self.subTest(relative=relative):
                self.assertEqual(m.safe(self.root, relative), self.root / relative)
        self.assertFalse((self.root / "corrections").exists())

    def test_symlinked_alias_is_denied_before_writes_and_can_recover(self):
        alias = self.root / "published/current.json"
        original = alias.read_bytes()
        for dangling in (False, True):
            with self.subTest(dangling=dangling):
                target = self.root / f"alias-target-{dangling}.json"
                if not dangling:
                    target.write_bytes(original)
                alias.unlink()
                alias.symlink_to(target)
                with self.assertRaises(m.RehearsalError) as caught:
                    m.rehearse(self.root, self.scenario, apply=True)
                self.assertEqual(caught.exception.code, "UNSAFE_SYMLINK")
                self.assertTrue(alias.is_symlink())
                self.assertFalse((self.root / "corrections").exists())
                self.assertFalse((self.root / "invalidations").exists())
                if dangling:
                    self.assertFalse(target.exists())
                else:
                    self.assertEqual(target.read_bytes(), original)
                alias.unlink()
                alias.write_bytes(original)
        self.assertEqual(m.rehearse(self.root, self.scenario, apply=True)["outcome"], "PASS")

    def assert_symlinked_output_denied_and_recoverable(self, directory):
        history = {p.relative_to(self.root): p.read_bytes()
                   for p in (self.root / "releases").rglob("*") if p.is_file()}
        for operation in ("ROLLBACK", "WITHDRAWAL"):
            scenario = self.make(operation)
            name = (scenario["correction"]["correction_id"] if directory == "corrections"
                    else scenario["scenario_id"]) + ".json"
            output = self.root / directory / name
            for dangling in (False, True):
                with self.subTest(directory=directory, operation=operation, dangling=dangling):
                    emit(self.root / "published/current.json", self.alias)
                    output.parent.mkdir(parents=True, exist_ok=True)
                    if output.exists():
                        output.unlink()
                    target = self.root / f"target-{directory}-{operation}-{dangling}.json"
                    if not dangling:
                        target.write_bytes(b"sentinel\n")
                    output.symlink_to(target)
                    with self.assertRaises(m.RehearsalError) as caught:
                        m.rehearse(self.root, scenario, apply=True)
                    self.assertEqual(caught.exception.code, "UNSAFE_SYMLINK")
                    self.assertTrue(output.is_symlink())
                    # Apply is sequential: a later denial may follow earlier writes.
                    output.unlink()
                    emit(self.root / "published/current.json", self.alias)
                    report = m.rehearse(self.root, scenario, apply=True)
                    self.assertEqual(report["outcome"], "PASS")
                    self.assertFalse(output.is_symlink())
                    self.assertTrue(output.is_file())
                    if dangling:
                        self.assertFalse(target.exists())
                    else:
                        self.assertEqual(target.read_bytes(), b"sentinel\n")
                    self.assertEqual(history, {p.relative_to(self.root): p.read_bytes()
                                              for p in (self.root / "releases").rglob("*")
                                              if p.is_file()})
                    self.assertEqual(list(self.root.rglob(".*.tmp")), [])

    def test_symlinked_correction_output_is_denied_and_can_recover(self):
        self.assert_symlinked_output_denied_and_recoverable("corrections")

    def test_symlinked_invalidation_output_is_denied_and_can_recover(self):
        self.assert_symlinked_output_denied_and_recoverable("invalidations")


if __name__ == "__main__": unittest.main()
