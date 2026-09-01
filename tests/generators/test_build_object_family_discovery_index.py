from __future__ import annotations

import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from tools.generators.build_object_family_discovery_index import (
    DiscoveryIndexError,
    build_discovery_index,
    main,
    render_index,
)


def _register() -> dict:
    return {
        "version": "v1",
        "registry": "object_family_register",
        "status": "PROPOSED",
        "authority": "navigational_index_only",
        "base_ref": "1" * 40,
        "entries": [
            {
                "family_id": "beta",
                "display_name": "Beta",
                "family_kind": "runtime",
                "maturity": "partial",
                "implementation_status": "PARTIAL",
                "lifecycle_stage": "beta_stage",
                "producer_classes": ["shared_producer"],
                "consumer_classes": ["beta_consumer", "shared_consumer"],
                "dependency_family_ids": ["alpha"],
                "evidence_family_ids": [],
                "release_family_ids": [],
                "correction_family_ids": [],
                "rollback_family_ids": [],
            },
            {
                "family_id": "alpha",
                "display_name": "Alpha",
                "family_kind": "evidence",
                "maturity": "covered",
                "implementation_status": "IMPLEMENTED",
                "lifecycle_stage": "alpha_stage",
                "producer_classes": ["alpha_producer", "shared_producer"],
                "consumer_classes": ["shared_consumer"],
                "dependency_family_ids": [],
                "evidence_family_ids": [],
                "release_family_ids": [],
                "correction_family_ids": [],
                "rollback_family_ids": [],
            },
        ],
    }


class ObjectFamilyDiscoveryIndexTests(unittest.TestCase):
    def test_builds_sorted_family_and_reverse_class_indexes(self) -> None:
        index = build_discovery_index(
            _register(), source_path="control_plane/object_family_register.yaml"
        )
        self.assertFalse(index["authority_created"])
        self.assertEqual("derived_discovery_only", index["authority"])
        self.assertEqual(
            ["alpha", "beta"],
            [item["family_id"] for item in index["families"]],
        )
        self.assertEqual(
            [
                {"producer_class": "alpha_producer", "family_ids": ["alpha"]},
                {
                    "producer_class": "shared_producer",
                    "family_ids": ["alpha", "beta"],
                },
            ],
            index["producer_index"],
        )
        self.assertEqual(
            {
                "consumer_class": "shared_consumer",
                "family_ids": ["alpha", "beta"],
            },
            index["consumer_index"][-1],
        )
        self.assertEqual(
            [{"from_family_id": "beta", "to_family_id": "alpha"}],
            index["dependency_edges"],
        )
        self.assertEqual(
            [
                {
                    "relation": "dependency",
                    "from_family_id": "beta",
                    "to_family_id": "alpha",
                }
            ],
            index["relation_edges"],
        )
        self.assertEqual(
            [
                {
                    "relation": "dependency",
                    "to_family_id": "alpha",
                    "from_family_ids": ["beta"],
                }
            ],
            index["relation_index"],
        )

    def test_projects_all_governed_relation_types_with_reverse_lookup(self) -> None:
        register = _register()
        for field in (
            "evidence_family_ids",
            "release_family_ids",
            "correction_family_ids",
            "rollback_family_ids",
        ):
            register["entries"][0][field] = ["alpha"]

        index = build_discovery_index(register, source_path="registry.json")

        self.assertEqual(
            ["correction", "dependency", "evidence", "release", "rollback"],
            sorted({edge["relation"] for edge in index["relation_edges"]}),
        )
        self.assertEqual(
            {
                "correction": 1,
                "dependency": 1,
                "evidence": 1,
                "release": 1,
                "rollback": 1,
            },
            index["relation_counts"],
        )
        self.assertEqual(5, len(index["relation_index"]))
        self.assertEqual(
            [{"from_family_id": "beta", "to_family_id": "alpha"}],
            index["dependency_edges"],
        )

    def test_render_is_deterministic(self) -> None:
        register = _register()
        first = render_index(
            build_discovery_index(register, source_path="registry.json")
        )
        second = render_index(
            build_discovery_index(register, source_path="registry.json")
        )
        self.assertEqual(first, second)
        self.assertEqual(
            first,
            json.dumps(
                json.loads(first), sort_keys=True, separators=(",", ":")
            )
            + "\n",
        )

    def test_unknown_dependency_fails_closed(self) -> None:
        register = _register()
        register["entries"][0]["dependency_family_ids"] = ["missing"]
        with self.assertRaisesRegex(
            DiscoveryIndexError, "unknown family in dependency_family_ids"
        ):
            build_discovery_index(register, source_path="registry.json")

    def test_all_relation_fields_fail_closed_on_unknown_family(self) -> None:
        for field in (
            "evidence_family_ids",
            "release_family_ids",
            "correction_family_ids",
            "rollback_family_ids",
        ):
            with self.subTest(field=field):
                register = _register()
                register["entries"][0][field] = ["missing"]
                with self.assertRaisesRegex(
                    DiscoveryIndexError, f"unknown family in {field}"
                ):
                    build_discovery_index(register, source_path="registry.json")

    def test_duplicate_family_id_fails_closed(self) -> None:
        register = _register()
        register["entries"][0]["family_id"] = "alpha"
        with self.assertRaisesRegex(
            DiscoveryIndexError, "family_id values must be unique"
        ):
            build_discovery_index(register, source_path="registry.json")

    def test_source_authority_cannot_escalate(self) -> None:
        register = _register()
        register["authority"] = "object_family_authority"
        with self.assertRaisesRegex(DiscoveryIndexError, "authority must remain"):
            build_discovery_index(register, source_path="registry.json")

    def test_duplicate_class_values_fail_closed(self) -> None:
        register = _register()
        register["entries"][0]["producer_classes"] = ["same", "same"]
        with self.assertRaisesRegex(
            DiscoveryIndexError, "contains duplicate values"
        ):
            build_discovery_index(register, source_path="registry.json")

    def test_cli_stdout_is_deterministic_and_public_metadata_only(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "register.json"
            path.write_text(json.dumps(_register()), encoding="utf-8")
            outputs: list[str] = []
            for _ in range(2):
                stream = io.StringIO()
                with redirect_stdout(stream):
                    rc = main(["--register", str(path)])
                self.assertEqual(0, rc)
                outputs.append(stream.getvalue())
            self.assertEqual(outputs[0], outputs[1])
            output = json.loads(outputs[0])
            self.assertEqual(
                "object-family-discovery-metadata-only", output["scope"]
            )
            self.assertNotIn("notes", output["families"][0])
            self.assertNotIn("schema_paths", output["families"][0])


if __name__ == "__main__":
    unittest.main()
