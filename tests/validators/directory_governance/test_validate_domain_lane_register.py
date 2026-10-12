from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = (
    ROOT / "tools/validators/directory_governance/validate_domain_lane_register.py"
)
REGISTER_PATH = ROOT / "control_plane/domain_lane_register.yaml"

spec = importlib.util.spec_from_file_location("domain_lane_register_validator", VALIDATOR_PATH)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)


def load() -> dict[str, object]:
    value, findings = validator.load(REGISTER_PATH)
    assert not findings
    assert isinstance(value, dict)
    return value


def write(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, separators=(",", ":")) + "\n", encoding="utf-8")


def codes(result: object) -> set[str]:
    return {finding.code for finding in result.findings}


class DomainLaneRegisterTests(unittest.TestCase):
    def candidate(self, value: object):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.yaml"
            write(path, value)
            return validator.validate(
                path,
                check_repository=False,
                check_bindings=False,
            )

    def test_current_projection(self) -> None:
        result = validator.validate(
            REGISTER_PATH,
            check_repository=False,
            check_bindings=False,
        )
        self.assertTrue(result.ok, result.findings)
        self.assertEqual(result.outcome, "PASS")

    def test_schema_self_check(self) -> None:
        schema = json.loads(validator.SCHEMA.read_text(encoding="utf-8"))
        validator.Draft202012Validator.check_schema(schema)

    def test_legacy_meta_profile_compatibility(self) -> None:
        content = REGISTER_PATH.read_text(encoding="utf-8")
        self.assertTrue(content.startswith("meta:\n"))
        header = content.splitlines()[:25]
        for marker in ("status:", "owner:", "last_reviewed:", "related_doctrine:"):
            self.assertTrue(any(marker in line for line in header), marker)
        doctrine_paths = [
            line.strip()[2:]
            for line in header
            if line.strip().startswith("- docs/")
        ]
        self.assertEqual(
            doctrine_paths,
            ["docs/doctrine/directory-rules.md", "docs/registers/DOMAIN_LANE.md"],
        )
        self.assertIn("entries:", content)

    def test_lane_set_drift(self) -> None:
        value = load()
        value["entries"] = value["entries"][:-1]
        result = self.candidate(value)
        self.assertIn("CANONICAL_LANE_MISSING", codes(result))
        self.assertEqual(result.outcome, "FAIL_NEW_DRIFT")

        value = load()
        extra = copy.deepcopy(value["entries"][0])
        extra.update(
            lane_id="invented",
            display_name="Invented",
            documentation_path="docs/domains/invented/",
            code_alias="invented",
        )
        value["entries"].append(extra)
        value["entries"].sort(key=lambda entry: entry["lane_id"])
        self.assertIn("UNEXPECTED_DOMAIN_LANE", codes(self.candidate(value)))

    def test_order_path_and_alias(self) -> None:
        value = load()
        value["entries"] = list(reversed(value["entries"]))
        self.assertIn("LANES_NOT_CANONICAL", codes(self.candidate(value)))

        value = load()
        value["entries"][0]["documentation_path"] = "docs/domains/wrong/"
        self.assertIn("DOCUMENTATION_PATH_MISMATCH", codes(self.candidate(value)))

        value = load()
        value["entries"][0]["code_alias"] = "wrong"
        self.assertIn("CODE_ALIAS_MISMATCH", codes(self.candidate(value)))

    def test_owner_overclaim(self) -> None:
        value = load()
        value["lane_defaults"]["owner_identity"] = "@invented"
        self.assertIn("OWNER_IDENTITY_OVERCLAIM", codes(self.candidate(value)))

    def test_cross_cutting_and_aliases(self) -> None:
        value = load()
        value["cross_cutting_exclusions"].pop()
        self.assertIn("CROSS_CUTTING_SET_MISMATCH", codes(self.candidate(value)))

        value = load()
        value["unresolved_aliases"]["air"] = "invented"
        self.assertIn("ALIAS_SET_MISMATCH", codes(self.candidate(value)))

    def test_duplicate_yaml_key(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.yaml"
            path.write_text("meta: {}\nmeta: {}\n", encoding="utf-8")
            self.assertIn(
                "YAML_DUPLICATE_KEY",
                codes(
                    validator.validate(
                        path,
                        check_repository=False,
                        check_bindings=False,
                    )
                ),
            )

    def test_yaml_alias_denied(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.yaml"
            path.write_text("meta: &meta {}\ncopy: *meta\n", encoding="utf-8")
            self.assertIn(
                "YAML_ALIAS_DENIED",
                codes(
                    validator.validate(
                        path,
                        check_repository=False,
                        check_bindings=False,
                    )
                ),
            )

    def test_repository_boundaries(self) -> None:
        value = load()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for entry in value["entries"]:
                (root / entry["documentation_path"]).mkdir(parents=True)
            self.assertTrue(
                validator.validate(
                    REGISTER_PATH,
                    repo_root=root,
                    check_bindings=False,
                ).ok
            )
            (root / "hydrology").mkdir()
            result = validator.validate(
                REGISTER_PATH,
                repo_root=root,
                check_bindings=False,
            )
            self.assertIn("DOMAIN_ROOT_PRESENT", codes(result))
            self.assertEqual(result.outcome, "FAIL_NEW_DRIFT")

    def test_missing_docs_hold(self) -> None:
        value = load()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for entry in value["entries"][1:]:
                (root / entry["documentation_path"]).mkdir(parents=True)
            result = validator.validate(
                REGISTER_PATH,
                repo_root=root,
                check_bindings=False,
            )
        self.assertIn("DOMAIN_DOCUMENTATION_MISSING", codes(result))
        self.assertEqual(result.outcome, "HOLD_UNRESOLVED")

    def test_authority_bindings(self) -> None:
        value = load()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            files = {
                "docs/doctrine/directory-rules.md": b"doctrine\n",
                "docs/registers/DOMAIN_LANE.md": b"narrative\n",
                "control_plane/root_registry.yaml": b"{}\n",
                "docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md": b"adr\n",
            }
            for relative, raw in files.items():
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(raw)
            value["doctrine"]["sha256"] = (
                "sha256:"
                + hashlib.sha256(files["docs/doctrine/directory-rules.md"]).hexdigest()
            )
            for key, relative in (
                ("narrative_register", "docs/registers/DOMAIN_LANE.md"),
                ("root_registry", "control_plane/root_registry.yaml"),
            ):
                raw = files[relative]
                value[key]["git_blob"] = hashlib.sha1(
                    f"blob {len(raw)}\0".encode() + raw
                ).hexdigest()
            candidate = root / "candidate.yaml"
            write(candidate, value)
            self.assertNotIn(
                "AUTHORITY_DIGEST_MISMATCH",
                codes(
                    validator.validate(
                        candidate,
                        repo_root=root,
                        check_repository=False,
                    )
                ),
            )
            (root / "docs/registers/DOMAIN_LANE.md").write_text(
                "changed\n",
                encoding="utf-8",
            )
            self.assertIn(
                "AUTHORITY_DIGEST_MISMATCH",
                codes(
                    validator.validate(
                        candidate,
                        repo_root=root,
                        check_repository=False,
                    )
                ),
            )

    def test_non_echo(self) -> None:
        value = load()
        marker = "@secret-do-not-echo"
        value["lane_defaults"]["owner_identity"] = marker
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "candidate.yaml"
            write(path, value)
            payload = validator.serialize(
                path,
                validator.validate(
                    path,
                    check_repository=False,
                    check_bindings=False,
                ),
            )
        self.assertNotIn(marker, payload)
        self.assertIn("OWNER_IDENTITY_OVERCLAIM", payload)

    def test_cli_deterministic(self) -> None:
        command = [
            sys.executable,
            str(VALIDATOR_PATH),
            str(REGISTER_PATH),
            "--no-repository-checks",
            "--no-binding-checks",
        ]
        first = subprocess.run(command, capture_output=True, text=True)
        second = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(first.returncode, 0)
        self.assertEqual(first.stdout, second.stdout)


if __name__ == "__main__":
    unittest.main()
