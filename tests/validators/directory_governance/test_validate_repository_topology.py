from __future__ import annotations

import importlib.util
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
import base64
import zlib
from datetime import date
from pathlib import Path
from unittest import mock
from contextlib import redirect_stdout


REPO_ROOT = Path(__file__).resolve().parents[3]
MODULE_PATH = (
    REPO_ROOT
    / "tools/validators/directory_governance/validate_repository_topology.py"
)
BASELINE_PATH = MODULE_PATH.with_name("repository_topology_baseline.json")
SPEC = importlib.util.spec_from_file_location(
    "kfm_validate_repository_topology", MODULE_PATH
)
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


def _entry(finding: object) -> dict[str, object]:
    entry = module._serialized_baseline_entry(finding)
    entry["evidence_members"] = finding.evidence_members
    return entry


class RepositoryTopologyTests(unittest.TestCase):
    def test_profile_has_exactly_twenty_stable_rule_ids(self) -> None:
        self.assertEqual(20, len(module.RULES))
        self.assertEqual(
            [f"KFM-TOPO-{number:03d}" for number in range(1, 21)],
            [rule.rule_id for rule in module.RULES],
        )
        self.assertEqual(20, len(module.RULE_BY_ID))

    def test_live_index_matches_the_exact_baseline(self) -> None:
        baseline_data = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
        baseline = module.load_baseline(BASELINE_PATH)
        findings, tracked_count = module.scan(REPO_ROOT)

        self.assertGreater(tracked_count, 0)
        self.assertGreater(len(findings), 0)
        self.assertEqual(
            {finding.fingerprint for finding in findings},
            set(baseline),
        )
        code, report = module.evaluate(
            findings,
            tracked_count,
            baseline,
            expires_on=baseline_data["expires_on"],
            as_of=date(2026, 8, 12),
        )
        self.assertEqual(0, code, report)
        self.assertEqual("PASS", report["outcome"])
        self.assertEqual(len(findings), report["counts"]["baselined_warning"])
        self.assertEqual([], report["baseline"]["stale_fingerprints"])
        self.assertFalse(report["authority"]["authorizes_repository_write"])

    def test_cli_json_is_deterministic(self) -> None:
        command = [
            sys.executable,
            str(MODULE_PATH),
            "--repo-root",
            str(REPO_ROOT),
            "--baseline",
            str(BASELINE_PATH),
        ]
        environment = os.environ.copy()
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        first = subprocess.run(
            command,
            cwd=REPO_ROOT,
            env=environment,
            capture_output=True,
            text=True,
            check=False,
        )
        second = subprocess.run(
            command,
            cwd=REPO_ROOT,
            env=environment,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(0, first.returncode, first.stdout + first.stderr)
        self.assertEqual(first.stdout, second.stdout)
        self.assertEqual(first.stderr, second.stderr)
        report = json.loads(first.stdout)
        self.assertEqual("PASS", report["outcome"])
        self.assertEqual(20, report["rule_count"])
        self.assertNotIn("duration", first.stdout)
        self.assertNotIn("timestamp", first.stdout)

    def test_baseline_accepts_exact_drift_and_rejects_growth_and_stale_entries(
        self,
    ) -> None:
        inherited = module._finding(
            "KFM-TOPO-003", "legacy-root-file.txt", "ROOT_FILE_NOT_ALLOWED"
        )
        baseline = {inherited.fingerprint: _entry(inherited)}

        code, report = module.evaluate(
            [inherited],
            1,
            baseline,
            expires_on="2026-11-10",
            as_of=date(2026, 8, 12),
        )
        self.assertEqual(0, code, report)
        self.assertEqual("PASS", report["outcome"])

        added = module._finding(
            "KFM-TOPO-003", "new-root-file.txt", "ROOT_FILE_NOT_ALLOWED"
        )
        code, report = module.evaluate(
            [inherited, added],
            2,
            baseline,
            expires_on="2026-11-10",
            as_of=date(2026, 8, 12),
        )
        self.assertEqual(1, code)
        self.assertEqual("FAIL_NEW_DRIFT", report["outcome"])
        self.assertEqual(1, report["counts"]["fail_new_drift"])

        code, report = module.evaluate(
            [],
            0,
            baseline,
            expires_on="2026-11-10",
            as_of=date(2026, 8, 12),
        )
        self.assertEqual(1, code)
        self.assertEqual("FAIL_INVARIANT", report["outcome"])
        self.assertEqual([inherited.fingerprint], report["baseline"]["stale_fingerprints"])

    def test_invariants_cannot_be_evaluated_or_loaded_as_waivers(self) -> None:
        invariant = module._finding(
            "KFM-TOPO-002", "unregistered/", "UNREGISTERED_ROOT"
        )
        code, report = module.evaluate(
            [invariant],
            1,
            {},
            expires_on="2026-11-10",
            as_of=date(2026, 8, 12),
        )
        self.assertEqual(1, code)
        self.assertEqual("FAIL_INVARIANT", report["outcome"])
        self.assertEqual(1, report["counts"]["fail_invariant"])

        payload = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
        payload["entries"] = [module._serialized_baseline_entry(invariant)]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "baseline.json"
            path.write_text(
                json.dumps(payload, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(module.TopologyError, "waive an invariant"):
                module.load_baseline(path)

        candidate = module.candidate_baseline(
            [invariant], expires_on="2026-11-10"
        )
        self.assertEqual([], candidate["entries"])

    def test_hard_path_safety_findings_cannot_be_baselined(self) -> None:
        root_registry = {"roots": [{"path": "docs/", "status": "ACTIVE"}]}
        paths = ("docs/link.md",)
        modes = {"docs/link.md": "120000"}
        blobs = {
            "control_plane/root_registry.yaml": json.dumps(root_registry).encode(
                "utf-8"
            )
        }
        object_ids = {path: "a" * 40 for path in paths}
        findings = module._path_findings(paths, modes, object_ids, blobs)
        path_finding = next(
            finding for finding in findings if finding.rule_id == "KFM-TOPO-001"
        )
        self.assertFalse(path_finding.baseline_allowed)
        candidate = module.candidate_baseline(
            [path_finding], expires_on="2026-11-10"
        )
        self.assertEqual([], candidate["entries"])

    def test_unmerged_or_duplicate_index_entries_fail_closed(self) -> None:
        conflict = b"100644 " + b"a" * 40 + b" 1\tdocs/a.md\0"
        with mock.patch.object(module, "_git", return_value=conflict):
            with self.assertRaisesRegex(module.TopologyError, "unmerged"):
                module.tracked_index(REPO_ROOT)

        duplicate = (
            b"100644 " + b"a" * 40 + b" 0\tdocs/a.md\0"
            + b"100644 " + b"b" * 40 + b" 0\tdocs/a.md\0"
        )
        with mock.patch.object(module, "_git", return_value=duplicate):
            with self.assertRaisesRegex(module.TopologyError, "duplicate path"):
                module.tracked_index(REPO_ROOT)

    def test_governance_json_rejects_duplicate_keys_and_root_paths(self) -> None:
        with self.assertRaisesRegex(module.TopologyError, "invalid indexed JSON"):
            module._blob_json(
                {"control_plane/root_registry.yaml": b'{"roots":[],"roots":[]}'},
                "control_plane/root_registry.yaml",
            )

        duplicate_roots = {
            "control_plane/root_registry.yaml": json.dumps(
                {
                    "roots": [
                        {"path": "docs/", "status": "ACTIVE"},
                        {"path": "docs", "status": "ACTIVE"},
                    ]
                }
            ).encode("utf-8")
        }
        with self.assertRaisesRegex(module.TopologyError, "duplicate or invalid"):
            module._registered_roots(duplicate_roots)

    def test_compressed_baseline_evidence_is_bounded(self) -> None:
        oversized = b"x" * (module.MAX_EVIDENCE_BYTES + 1)
        encoded = base64.b64encode(zlib.compress(oversized, level=9)).decode("ascii")
        with self.assertRaisesRegex(module.TopologyError, "compressed evidence"):
            module._decode_evidence_members(encoded, module._digest(oversized))

        payload = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
        payload["entries"] = [
            module._serialized_baseline_entry(
                module._finding("KFM-TOPO-003", f"legacy-{index}.txt", "legacy")
            )
            for index in range(3)
        ]
        payload["entries"].sort(key=lambda item: item["fingerprint"])
        prior_limit = module.MAX_BASELINE_EVIDENCE_BYTES
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "baseline.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            try:
                module.MAX_BASELINE_EVIDENCE_BYTES = 10
                with self.assertRaisesRegex(module.TopologyError, "aggregate limit"):
                    module.load_baseline(path)
            finally:
                module.MAX_BASELINE_EVIDENCE_BYTES = prior_limit

    def test_frozen_root_content_change_changes_the_fingerprint(self) -> None:
        paths = ("catalog/README.md",)
        modes = {paths[0]: "100644"}
        blobs = {
            "control_plane/root_registry.yaml": json.dumps(
                {"roots": [{"path": "catalog/", "status": "DEPRECATED"}]}
            ).encode("utf-8")
        }
        first = module._path_findings(
            paths, modes, {paths[0]: "a" * 40}, blobs
        )
        second = module._path_findings(
            paths, modes, {paths[0]: "b" * 40}, blobs
        )
        first_frozen = next(
            finding for finding in first if finding.rule_id == "KFM-TOPO-004"
        )
        second_frozen = next(
            finding for finding in second if finding.rule_id == "KFM-TOPO-004"
        )
        self.assertNotEqual(first_frozen.fingerprint, second_frozen.fingerprint)

    def test_emit_baseline_refuses_invariant_findings(self) -> None:
        invariant = module._finding(
            "KFM-TOPO-002", "unregistered/", "UNREGISTERED_ROOT"
        )
        output = io.StringIO()
        with mock.patch.object(module, "scan", return_value=((invariant,), 1)):
            with redirect_stdout(output):
                code = module.main(["--emit-baseline"])
        self.assertEqual(2, code)
        self.assertEqual("ERROR_VALIDATOR", json.loads(output.getvalue())["outcome"])

    def test_trusted_baseline_transition_allows_only_shrinkage(self) -> None:
        current_data = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
        current_entries = module.load_baseline(BASELINE_PATH)
        trusted_data = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
        trusted_entries = module.load_baseline(BASELINE_PATH)
        module.validate_baseline_transition(
            current_data, current_entries, trusted_data, trusted_entries
        )

        added = module._finding(
            "KFM-TOPO-003", "new-root-file.txt", "ROOT_FILE_NOT_ALLOWED"
        )
        added_entry = _entry(added)
        with self.assertRaisesRegex(module.TopologyError, "adds waiver"):
            module.validate_baseline_transition(
                current_data,
                {**current_entries, added.fingerprint: added_entry},
                trusted_data,
                trusted_entries,
            )

        extended_data = dict(current_data)
        extended_data["expires_on"] = "2027-01-01"
        with self.assertRaisesRegex(module.TopologyError, "extends expiry"):
            module.validate_baseline_transition(
                extended_data,
                current_entries,
                trusted_data,
                trusted_entries,
            )

        inherited_group = module._finding(
            "KFM-TOPO-009", "scaffold-only-leaf-directories", ["docs/a", "docs/b"]
        )
        repaired_group = module._finding(
            "KFM-TOPO-009", "scaffold-only-leaf-directories", ["docs/b"]
        )
        group_trusted = {inherited_group.fingerprint: _entry(inherited_group)}
        group_current = {repaired_group.fingerprint: _entry(repaired_group)}
        module.validate_baseline_transition(
            current_data,
            group_current,
            trusted_data,
            group_trusted,
        )
        code, report = module.evaluate(
            [repaired_group],
            1,
            group_current,
            expires_on=str(current_data["expires_on"]),
            as_of=date(2026, 8, 12),
        )
        self.assertEqual(0, code, report)
        self.assertEqual("PASS", report["outcome"])

    def test_artifact_fingerprints_bind_to_indexed_content(self) -> None:
        paths = ("artifacts/release/example/release_manifest.json",)
        modes = {paths[0]: "100644"}
        blobs = {
            "control_plane/root_registry.yaml": json.dumps(
                {"roots": [{"path": "artifacts/", "status": "COMPATIBILITY"}]}
            ).encode("utf-8")
        }
        first = module._path_findings(paths, modes, {paths[0]: "a" * 40}, blobs)
        second = module._path_findings(paths, modes, {paths[0]: "b" * 40}, blobs)
        for rule_id in ("KFM-TOPO-005", "KFM-TOPO-013"):
            first_finding = next(item for item in first if item.rule_id == rule_id)
            second_finding = next(item for item in second if item.rule_id == rule_id)
            self.assertNotEqual(first_finding.fingerprint, second_finding.fingerprint)

    def test_app_configuration_and_schema_inputs_fail_closed(self) -> None:
        fixed_paths = (
            "control_plane/path_alias_register.yaml",
            "control_plane/root_registry.yaml",
            "docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md",
            "docs/doctrine/directory-rules.md",
        )
        fixed = {path: (REPO_ROOT / path).read_bytes() for path in fixed_paths}
        config_path = "apps/web/config.json"
        config_blobs = dict(fixed)
        config_blobs[config_path] = b'{"source":"data/raw/private.json"}'
        findings = module._content_findings((config_path,), config_blobs)
        self.assertIn("KFM-TOPO-014", {finding.rule_id for finding in findings})

        constructed_path = "apps/web/main.py"
        constructed_blobs = dict(fixed)
        constructed_blobs[constructed_path] = b'PATH = Path("data") / "raw" / "private.json"\n'
        constructed = module._content_findings((constructed_path,), constructed_blobs)
        self.assertIn("KFM-TOPO-014", {finding.rule_id for finding in constructed})

        invalid_app = dict(fixed)
        invalid_app[config_path] = b"\xff"
        with self.assertRaisesRegex(module.TopologyError, "not UTF-8"):
            module._content_findings((config_path,), invalid_app)

        schema_path = "schemas/broken.schema.json"
        invalid_schema = dict(fixed)
        invalid_schema[schema_path] = b'{"$id":"a","$id":"b"}'
        with self.assertRaisesRegex(module.TopologyError, "cannot be inspected"):
            module._content_findings((schema_path,), invalid_schema)

        decoy_path = "artifacts/qa/decoy.json"
        decoy_blobs = dict(fixed)
        decoy_blobs[decoy_path] = (
            b'{"note":"generated_from generator generator_version sha256 edit_policy"}'
        )
        decoy = module._content_findings((decoy_path,), decoy_blobs)
        provenance = next(
            finding for finding in decoy if finding.rule_id == "KFM-TOPO-017"
        )
        self.assertTrue(provenance.evidence_sha256)

        invalid_values_path = "artifacts/qa/invalid-values.json"
        invalid_values_blobs = dict(fixed)
        invalid_values_blobs[invalid_values_path] = (
            b'{"generated_from":null,"generator":"","generator_version":null,'
            b'"sha256":"not-a-digest","edit_policy":false}'
        )
        invalid_values = module._content_findings(
            (invalid_values_path,), invalid_values_blobs
        )
        self.assertIn("KFM-TOPO-017", {finding.rule_id for finding in invalid_values})

    def test_high_value_synthetic_path_rules(self) -> None:
        registered_roots = {
            "artifacts",
            "catalog",
            "connectors",
            "data",
            "docs",
            "release",
            "src",
            "tools",
        }
        root_registry = {
            "roots": [
                {"path": root + "/", "status": "ACTIVE"}
                for root in sorted(registered_roots)
            ]
        }
        paths = tuple(
            sorted(
                {
                    "bad-root.json",
                    "artifacts/release/release_manifest.json",
                    "catalog/README.md",
                    "connectors/air/README.md",
                    "data/rogue/README.md",
                    "data/triplet(s)/.gitkeep",
                    "data/triplets/README.md",
                    "docs/standards/IIIF.md",
                    "docs/standards/iiif.md",
                    "release/manifest/.gitkeep",
                    "release/rogue/README.md",
                    "src/kfm/__init__.py",
                    "tools/bad.rego",
                    "unregistered/README.md",
                }
            )
        )
        modes = {path: "100644" for path in paths}
        modes["connectors/air/README.md"] = "120000"
        blobs = {
            "control_plane/root_registry.yaml": json.dumps(root_registry).encode(
                "utf-8"
            )
        }
        object_ids = {path: "a" * 40 for path in paths}
        findings = module._path_findings(paths, modes, object_ids, blobs)
        observed = {finding.rule_id for finding in findings}
        self.assertTrue(
            {f"KFM-TOPO-{number:03d}" for number in range(1, 14)}.issubset(
                observed
            ),
            sorted(observed),
        )

    def test_high_value_synthetic_content_rules_and_authority_binding(self) -> None:
        fixed_paths = (
            "control_plane/path_alias_register.yaml",
            "control_plane/root_registry.yaml",
            "docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md",
            "docs/doctrine/directory-rules.md",
        )
        blobs = {
            path: (REPO_ROOT / path).read_bytes()
            for path in fixed_paths
        }
        synthetic = {
            "apps/site/config.py": b'SOURCE = "data/raw/private.json"\n',
            "schemas/a.schema.json": b'{"$id":"kfm://schema/shared"}\n',
            "schemas/b.schema.json": b'{"$id":"kfm://schema/shared"}\n',
            "docs/a.md": b'doc_id: kfm://doc/shared\n',
            "docs/b.md": b'doc_id: kfm://doc/shared\n',
            "artifacts/qa/output.json": b'{"status":"placeholder"}\n',
            "policy/redaction/profiles.yaml": b'profiles: []\n',
        }
        blobs.update(synthetic)
        findings = module._content_findings(tuple(sorted(synthetic)), blobs)
        observed = {finding.rule_id for finding in findings}
        self.assertTrue(
            {
                "KFM-TOPO-014",
                "KFM-TOPO-015",
                "KFM-TOPO-016",
                "KFM-TOPO-017",
                "KFM-TOPO-018",
                "KFM-TOPO-020",
            }.issubset(observed),
            sorted(observed),
        )
        self.assertNotIn("KFM-TOPO-019", observed)

        blobs["docs/doctrine/directory-rules.md"] = b"tampered\n"
        tampered = module._content_findings(tuple(sorted(synthetic)), blobs)
        self.assertIn("KFM-TOPO-019", {finding.rule_id for finding in tampered})


if __name__ == "__main__":
    unittest.main()
