from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators.fixture_root_contract import REQUIRED_H2, validate_repository


def _readme(directory_count: int = 2) -> str:
    headings: list[str] = []
    for heading in REQUIRED_H2:
        headings.append(f"## {heading}")
        if heading == "Direct-child directory map":
            headings.extend(
                [
                    "",
                    "```text",
                    "fixtures/",
                    "├── README.md",
                    "├── alpha/",
                    "└── beta/",
                    "```",
                ]
            )
        else:
            headings.extend(["", "Bounded test content."])
    return (
        "<!-- [KFM_META_BLOCK_V2]\n"
        "doc_id: kfm://doc/fixtures-readme\n"
        "title: Fixture Root\n"
        "type: readme\n"
        "version: v1\n"
        "status: draft\n"
        "current_path: fixtures/README.md\n"
        "owning_root: fixtures/\n"
        "root_id: root.fixtures\n"
        "readme_profile: ROOT_FULL\n"
        "[/KFM_META_BLOCK_V2] -->\n\n"
        "# `fixtures/` — Canonical Reusable Fixture Root\n\n"
        "| Field | Current repository-grounded result |\n"
        "|---|---|\n"
        f"| Direct-child snapshot | `README.md` plus {directory_count} directories |\n\n"
        + "\n\n".join(headings)
        + "\n"
    )


def _root_registry() -> dict[str, object]:
    return {
        "entry_defaults": {},
        "class_defaults": {
            "canonical": {"status": "ACTIVE", "canonical_target": None}
        },
        "roots": [
            {
                "allowed_artifact_kinds": ["test_fixture"],
                "class": "canonical",
                "exposure": "public",
                "mutation": "versioned",
                "path": "fixtures/",
                "prohibited_artifact_kinds": ["data_instance", "release_decision"],
                "responsibility": (
                    "Reusable synthetic, valid, invalid, and golden test inputs "
                    "and expected outputs"
                ),
                "retention": "repository_lifetime",
                "root_id": "root.fixtures",
                "validation_profiles": ["synthetic_public_safe_only"],
            }
        ],
    }


def _validator_registry() -> dict[str, object]:
    ids = [f"validator-{index}" for index in range(8)]
    non_fixture_ids = ["repository-topology", "workflow-security"]
    return {
        "profiles": {"full": [*ids, *non_fixture_ids]},
        "validators": [
            {
                "id": validator_id,
                "script": f"tools/validators/validate_{index}.py",
                "args": ["--fixtures"],
            }
            for index, validator_id in enumerate(ids)
        ] + [
            {
                "id": validator_id,
                "script": f"tools/validators/validate_{validator_id}.py",
                "args": [],
            }
            for validator_id in non_fixture_ids
        ],
    }


class FixtureRootContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for path in ("fixtures/alpha", "fixtures/beta", "control_plane", "tools/validators"):
            (self.root / path).mkdir(parents=True, exist_ok=True)
        (self.root / "fixtures/README.md").write_text(_readme(), encoding="utf-8")
        (self.root / "control_plane/root_registry.yaml").write_text(
            json.dumps(_root_registry(), sort_keys=True), encoding="utf-8"
        )
        registry = _validator_registry()
        (self.root / "tools/validators/validator_registry.json").write_text(
            json.dumps(registry, sort_keys=True), encoding="utf-8"
        )
        for index in range(8):
            (self.root / f"tools/validators/validate_{index}.py").write_text(
                "# synthetic validator\n", encoding="utf-8"
            )
        for validator_id in ("repository-topology", "workflow-security"):
            (self.root / f"tools/validators/validate_{validator_id}.py").write_text(
                "# synthetic non-fixture validator\n", encoding="utf-8"
            )
        (self.root / "Makefile").write_text(
            'fixtures:\n\t@echo "TODO: regenerate deterministic fixtures"\n',
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def codes(self) -> set[str]:
        return {finding.code for finding in validate_repository(self.root).findings}

    def test_valid_contract_passes(self) -> None:
        result = validate_repository(self.root)
        self.assertTrue(result.ok, result.findings)
        self.assertEqual(result.outcome, "PASS")
        self.assertEqual(result.direct_child_directories, 2)
        self.assertEqual(result.aggregate_validators, 10)

    def test_root_full_heading_order_fails_closed(self) -> None:
        path = self.root / "fixtures/README.md"
        text = path.read_text(encoding="utf-8").replace(
            "## Root class and authority owner",
            "## Adoption and conformance status",
            1,
        )
        path.write_text(text, encoding="utf-8")
        self.assertIn("ROOT_FULL_HEADING_ORDER", self.codes())

    def test_direct_child_drift_is_detected(self) -> None:
        (self.root / "fixtures/gamma").mkdir()
        codes = self.codes()
        self.assertIn("DIRECT_CHILD_COUNT_MISMATCH", codes)
        self.assertIn("DIRECT_CHILD_MAP_MISMATCH", codes)

    def test_root_registry_mismatch_is_detected(self) -> None:
        path = self.root / "control_plane/root_registry.yaml"
        payload = json.loads(path.read_text(encoding="utf-8"))
        payload["roots"][0]["exposure"] = "internal"
        path.write_text(json.dumps(payload), encoding="utf-8")
        self.assertIn("ROOT_REGISTRY_FIELD_MISMATCH", self.codes())

    def test_makefile_marker_change_is_detected(self) -> None:
        (self.root / "Makefile").write_text(
            "fixtures:\n\tpython tools/regenerate.py\n", encoding="utf-8"
        )
        self.assertIn("FIXTURES_TARGET_SEMANTICS_CHANGED", self.codes())

    def test_aggregate_inventory_count_is_detected(self) -> None:
        path = self.root / "tools/validators/validator_registry.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        payload["profiles"]["full"].pop()
        path.write_text(json.dumps(payload), encoding="utf-8")
        self.assertIn("AGGREGATE_PROFILE_COUNT_MISMATCH", self.codes())


if __name__ == "__main__":
    unittest.main()
