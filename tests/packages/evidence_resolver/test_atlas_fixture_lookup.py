"""Real fixed-file Atlas lookup, negative boundaries and compatibility proof."""

from __future__ import annotations

from dataclasses import FrozenInstanceError
import hashlib
import json
import os
from pathlib import Path
import shutil
import socket
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
import urllib.request

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "packages/evidence-resolver/src"))

from evidence_resolver import atlas_fixture_lookup as atlas  # noqa: E402
from evidence_resolver import hydrology_fixture_adapter as files  # noqa: E402
from evidence_resolver.core import evaluate_resolution_candidate, loads_bounded  # noqa: E402
from evidence_resolver.verification_history import canonical_spec_hash, validate_history  # noqa: E402


class AtlasFixtureLookupTests(unittest.TestCase):
    def isolated(self) -> Path:
        root = Path(self.enterContext(tempfile.TemporaryDirectory()))
        for relative in (str(atlas._MANIFEST_PATH), *(p for _, p, _ in atlas._ARTIFACTS)):
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(REPO_ROOT / relative, target)
        self.enterContext(mock.patch.object(files, "_REPOSITORY_ROOT", root))
        return root

    def lookup(self):
        return atlas.lookup_atlas_fixture(atlas.CANDIDATE_ID)

    def assert_closed(self, result):
        self.assertIn(result.status, {"ERROR", "NOT_FOUND"})
        self.assertIsNone(result.packet)
        diagnostic = result.as_dict()
        self.assertFalse(diagnostic["authoritative"])
        self.assertFalse(diagnostic["renderable"])
        encoded = json.dumps(diagnostic)
        for forbidden in ("protected-sentinel", "fixtures/", "https://", "claim_scope"):
            self.assertNotIn(forbidden, encoded)

    def test_original_bytes_are_bound_without_resolution_authority(self):
        result = self.lookup()
        self.assertEqual("FOUND", result.status)
        packet = result.packet
        self.assertIsNotNone(packet)
        self.assertEqual(atlas.CANDIDATE_ID, packet.candidate_id)
        self.assertEqual("overlay:synthetic-kansas-promotion-proof", packet.subject_ref)
        self.assertEqual("evidence:synthetic:promotion-proof:v1", packet.evidence_ref)
        for (role, path, digest) in atlas._ARTIFACTS:
            raw = getattr(packet, role + "_bytes")
            self.assertEqual((REPO_ROOT / path).read_bytes(), raw)
            self.assertEqual(digest, "sha256:" + hashlib.sha256(raw).hexdigest())
        self.assertEqual("atlas-lookup/verification-profile-review-required",
                         result.as_dict()["resolution_hold"])
        self.assertFalse(result.as_dict()["authoritative"])
        self.assertFalse(result.as_dict()["renderable"])
        self.assertNotIn("packet", result.as_dict())
        with self.assertRaises(FrozenInstanceError):
            packet.subject_ref = "forged"

    def test_lookup_is_deterministic_and_keeps_no_mutable_result(self):
        first, second = self.lookup(), self.lookup()
        self.assertEqual(first, second)
        self.assertIsNot(first.packet, second.packet)
        first.as_dict()["checks_performed"].clear()
        self.assertTrue(first.checks_performed)

    def test_unknown_or_stale_selector_performs_no_file_reads(self):
        with mock.patch.object(files, "_read_repository_file", side_effect=AssertionError("read")):
            for value in ("hb1", "atlas-candidate:synthetic-kansas-proof-v0", "unknown"):
                with self.subTest(value=value):
                    result = atlas.lookup_atlas_fixture(value)
                    self.assertEqual("NOT_FOUND", result.status)
                    self.assert_closed(result)

    def test_paths_bundles_urls_and_authority_input_are_rejected_before_io(self):
        invalid = (None, [], 1, True, "", "../protected-sentinel", "/etc/passwd",
                   "https://example.invalid", "x\\y", "x\n", "a" * 4097,
                   {"candidate_id": atlas.CANDIDATE_ID, "bundle_candidate": {}},
                   {"policy_outcome": "ANSWER", "review": "REVIEWED", "release": "RELEASED"})
        with mock.patch.object(files, "_read_repository_file", side_effect=AssertionError("read")):
            for value in invalid:
                with self.subTest(value=repr(value)[:60]):
                    result = atlas.lookup_atlas_fixture(value)
                    self.assertEqual(("atlas-lookup/selector-invalid",), result.issues)
                    self.assert_closed(result)

    def test_manifest_cannot_change_any_identity_scope_path_or_digest(self):
        root = self.isolated()
        original = atlas._manifest_contract()
        for key in original:
            for mode in ("missing", "changed"):
                with self.subTest(key=key, mode=mode):
                    changed = json.loads(json.dumps(original))
                    if mode == "missing":
                        del changed[key]
                    else:
                        changed[key] = "protected-sentinel"
                    (root / atlas._MANIFEST_PATH).write_text(json.dumps(changed))
                    result = self.lookup()
                    self.assertEqual(("atlas-lookup/manifest-binding-invalid",), result.issues)
                    self.assert_closed(result)
        changed = dict(original, policy_outcome="ANSWER")
        (root / atlas._MANIFEST_PATH).write_text(json.dumps(changed))
        self.assert_closed(self.lookup())

    def test_manifest_json_rejects_duplicates_nonfinite_and_oversize(self):
        root = self.isolated()
        for raw in (b'{"entries":1,"entries":2}', b'{"x":NaN}', b'\xff', b'[]',
                    b' ' * (atlas.MAX_FIXTURE_BYTES + 1)):
            with self.subTest(raw=raw[:30]):
                (root / atlas._MANIFEST_PATH).write_bytes(raw)
                self.assert_closed(self.lookup())

    def test_tampering_any_payload_discards_the_entire_packet(self):
        root = self.isolated()
        for role, path, _ in atlas._ARTIFACTS:
            with self.subTest(role=role):
                original = (root / path).read_bytes()
                (root / path).write_bytes(original + b" ")
                result = self.lookup()
                self.assertEqual(("atlas-lookup/digest-mismatch",), result.issues)
                self.assert_closed(result)
                (root / path).write_bytes(original)

    def test_missing_and_static_symlink_files_fail_closed(self):
        root = self.isolated()
        for path in (str(atlas._MANIFEST_PATH), *(p for _, p, _ in atlas._ARTIFACTS)):
            target = root / path
            for symlink in (False, True):
                with self.subTest(path=path, symlink=symlink):
                    target.unlink()
                    if symlink:
                        target.symlink_to(REPO_ROOT / path)
                    self.assert_closed(self.lookup())
                    if symlink:
                        target.unlink()
                    shutil.copy2(REPO_ROOT / path, target)

    def test_file_and_parent_symlink_swaps_after_check_are_rejected(self):
        for parent_swap in (False, True):
            with self.subTest(parent_swap=parent_swap):
                root = self.isolated()
                target = root / atlas._ARTIFACTS[2][1]
                original = Path.is_file
                def swap(path):
                    result = original(path)
                    if path == target:
                        selected = target.parent if parent_swap else target
                        moved = selected.with_name(selected.name + "-moved")
                        selected.rename(moved)
                        selected.symlink_to(moved, target_is_directory=parent_swap)
                    return result
                with mock.patch.object(Path, "is_file", swap):
                    self.assert_closed(self.lookup())

    def test_fifo_swap_never_reads_a_special_file(self):
        root = self.isolated()
        target = root / atlas._ARTIFACTS[2][1]
        original_is_file, original_read = Path.is_file, os.read
        def swap(path):
            result = original_is_file(path)
            if path == target:
                path.unlink()
                os.mkfifo(path)
            return result
        def read(fd, size):
            self.assertTrue(files.stat.S_ISREG(os.fstat(fd).st_mode))
            return original_read(fd, size)
        with mock.patch.object(Path, "is_file", swap), mock.patch.object(os, "read", read):
            self.assert_closed(self.lookup())

    def test_growth_after_fstat_is_bounded(self):
        root = self.isolated()
        target = root / atlas._ARTIFACTS[2][1]
        inode = target.stat().st_ino
        original = os.fstat
        def grow(fd):
            result = original(fd)
            if result.st_ino == inode:
                with target.open("ab") as handle:
                    handle.write(b" " * files.MAX_INPUT_BYTES)
            return result
        with mock.patch.object(os, "fstat", grow):
            self.assert_closed(self.lookup())

    def test_short_reads_still_bind_complete_bytes(self):
        original = os.read
        with mock.patch.object(os, "read", side_effect=lambda fd, size: original(fd, min(size, 7))):
            self.assertEqual("FOUND", self.lookup().status)

    def test_descriptors_close_on_success_and_read_error(self):
        for fail_read in (False, True):
            opened = []
            original_open, original_read = os.open, os.read
            def record(*args, **kwargs):
                fd = original_open(*args, **kwargs)
                opened.append(fd)
                return fd
            def read(fd, size):
                if fail_read:
                    raise OSError("protected-sentinel")
                return original_read(fd, size)
            with mock.patch.object(os, "open", record), mock.patch.object(os, "read", read):
                result = self.lookup()
            self.assertTrue(opened)
            for fd in opened:
                with self.assertRaises(OSError):
                    os.fstat(fd)
            if fail_read:
                self.assert_closed(result)
            else:
                self.assertEqual("FOUND", result.status)

    def test_unsupported_descriptor_platform_has_no_fallback(self):
        with mock.patch.object(files, "_HAS_DESCRIPTOR_READ", False), \
                mock.patch.object(os, "open", side_effect=AssertionError("no fallback")):
            result = self.lookup()
            self.assertEqual(("fixture-adapter/descriptor-read-unsupported",), result.issues)
            self.assert_closed(result)

    def test_identity_time_and_scope_checks_survive_matching_test_only_digests(self):
        changes = (
            ("carrier", lambda x: x["kfm"].update(candidate_id="protected-sentinel")),
            ("carrier", lambda x: x["kfm"]["temporal"].update(end="2026-04-14T00:00:00Z")),
            ("carrier", lambda x: x["features"][0].update(id="wrong-feature")),
            ("reference", lambda x: x.update(subject_spec_hash="sha256:" + "0" * 64)),
            ("bundle", lambda x: x["evidence_refs"][0].update(ref="other-subject")),
            ("bundle", lambda x: x.update(bundle_id="other-bundle")),
            ("bundle", lambda x: x["checksums"].update(carrier="sha256:" + "0" * 64)),
        )
        for role, mutate in changes:
            with self.subTest(role=role):
                root = self.isolated()
                artifacts = list(atlas._ARTIFACTS)
                index = next(i for i, item in enumerate(artifacts) if item[0] == role)
                _, path, _ = artifacts[index]
                value = json.loads((root / path).read_bytes())
                mutate(value)
                raw = (json.dumps(value) + "\n").encode()
                (root / path).write_bytes(raw)
                artifacts[index] = (role, path, "sha256:" + hashlib.sha256(raw).hexdigest())
                with mock.patch.object(atlas, "_ARTIFACTS", tuple(artifacts)):
                    (root / atlas._MANIFEST_PATH).write_text(json.dumps(atlas._manifest_contract()))
                    result = self.lookup()
                    self.assertEqual(("atlas-lookup/packet-binding-invalid",), result.issues)
                    self.assert_closed(result)

    def test_actual_verification_profile_cannot_silently_rename_atlas_subject(self):
        request = json.loads((REPO_ROOT / "fixtures/packages/evidence_resolver/v1alpha1/valid/resolved.json").read_bytes())["request"]
        packet = self.lookup().packet
        request["bundle_candidate"] = loads_bounded(packet.bundle_bytes)
        request["evidence_ref"] = {"ref": packet.subject_ref, "kind": "artifact", "bundle_ref": packet.evidence_ref}
        request["lookup_context"]["bundle_id"] = packet.evidence_ref
        history = request["verification_history"]
        history["subject_ref"] = packet.subject_ref
        history["spec_hash"] = canonical_spec_hash(history)
        self.assertTrue(validate_history(history))
        self.assertEqual("ERROR", evaluate_resolution_candidate(request).status)
        history["subject_ref"] = "kfm://synthetic/atlas/alias"
        history["spec_hash"] = canonical_spec_hash(history)
        result = evaluate_resolution_candidate(request)
        self.assertEqual("UNRESOLVED", result.status)
        self.assertIn("verification/subject-mismatch", {x.code for x in result.issues})
        self.assertEqual(packet.subject_ref, loads_bounded(packet.bundle_bytes)["evidence_refs"][0]["ref"])

    def test_no_network_process_or_model_call(self):
        with mock.patch.object(socket, "socket", side_effect=AssertionError("socket denied")), \
                mock.patch.object(socket, "create_connection", side_effect=AssertionError("network denied")), \
                mock.patch.object(socket, "getaddrinfo", side_effect=AssertionError("DNS denied")), \
                mock.patch.object(urllib.request, "urlopen", side_effect=AssertionError("URL denied")), \
                mock.patch.object(subprocess, "Popen", side_effect=AssertionError("process denied")):
            self.assertEqual("FOUND", self.lookup().status)


if __name__ == "__main__":
    unittest.main()
