from __future__ import annotations

import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from tools.generators.build_path_alias_discovery_index import (
    DiscoveryIndexError,
    build_discovery_index,
    main,
    render_index,
)


def _alias(alias_id: str = "alias.beta", old_path: str = "legacy/beta.md") -> dict:
    return {
        "alias_id": alias_id,
        "class": "legacy",
        "status": "ACTIVE",
        "old_path": old_path,
        "canonical_target": f"canonical/{alias_id}.md",
        "object_family": "human_document",
        "identity_mapping": {
            "canonical_id": f"kfm://canonical/{alias_id}",
            "aliases": [f"kfm://legacy/{alias_id}"],
            "identity_rule": "aliases_resolve_to_canonical",
        },
        "consumers": [
            {
                "consumer_id": "consumer.shared",
                "kind": "repository_internal",
                "state": "VERIFIED_AT_DECISION",
            }
        ],
        "consumer_closure": "OPEN",
        "read_rule": "canonical_only_with_redirect",
        "write_rule": "canonical_only",
        "authority_mode": "non_authoritative",
        "body_mode": "tombstone",
        "verification_state": "PARTIAL",
    }


def _register() -> dict:
    alpha = _alias("alias.alpha", "legacy/alpha.md")
    alpha["class"] = "redirect"
    alpha["verification_state"] = "VERIFIED"
    return {
        "version": "v1",
        "registry": "path_alias_register",
        "status": "ACTIVE",
        "authority": "machine_projection_only",
        "base_ref": "1" * 40,
        "aliases": [_alias(), alpha],
    }


class PathAliasDiscoveryIndexTests(unittest.TestCase):
    def test_builds_stable_alias_identity_consumer_and_facet_indexes(self) -> None:
        index = build_discovery_index(
            _register(), source_path="control_plane/path_alias_register.yaml"
        )
        self.assertFalse(index["authority_created"])
        self.assertEqual("derived_discovery_only", index["authority"])
        self.assertEqual(
            ["alias.alpha", "alias.beta"],
            [item["alias_id"] for item in index["aliases"]],
        )
        self.assertEqual(
            [
                {
                    "old_path": "legacy/alpha.md",
                    "canonical_target": "canonical/alias.alpha.md",
                    "alias_id": "alias.alpha",
                    "canonical_id": "kfm://canonical/alias.alpha",
                },
                {
                    "old_path": "legacy/beta.md",
                    "canonical_target": "canonical/alias.beta.md",
                    "alias_id": "alias.beta",
                    "canonical_id": "kfm://canonical/alias.beta",
                },
            ],
            index["path_index"],
        )
        self.assertEqual(
            [{"consumer_id": "consumer.shared", "alias_ids": ["alias.alpha", "alias.beta"]}],
            index["consumer_index"],
        )
        self.assertEqual(
            [
                {"value": "legacy", "alias_ids": ["alias.beta"]},
                {"value": "redirect", "alias_ids": ["alias.alpha"]},
            ],
            index["facets"]["class"],
        )
        self.assertEqual(4, len(index["identity_index"]))

    def test_render_is_deterministic(self) -> None:
        index = build_discovery_index(_register(), source_path="register.json")
        first = render_index(index)
        second = render_index(index)
        self.assertEqual(first, second)
        self.assertEqual(
            first,
            json.dumps(json.loads(first), sort_keys=True, separators=(",", ":")) + "\n",
        )

    def test_duplicate_alias_id_and_old_path_fail_closed(self) -> None:
        duplicate_id = _register()
        duplicate_id["aliases"][0]["alias_id"] = "alias.alpha"
        with self.assertRaisesRegex(DiscoveryIndexError, "alias_id values must be unique"):
            build_discovery_index(duplicate_id, source_path="register.json")

        duplicate_path = _register()
        duplicate_path["aliases"][0]["old_path"] = "legacy/alpha.md"
        with self.assertRaisesRegex(DiscoveryIndexError, "old_path values must be unique"):
            build_discovery_index(duplicate_path, source_path="register.json")

    def test_identity_collisions_fail_closed(self) -> None:
        register = _register()
        register["aliases"][0]["identity_mapping"]["aliases"] = [
            "kfm://legacy/alias.alpha"
        ]
        with self.assertRaisesRegex(DiscoveryIndexError, "globally unique"):
            build_discovery_index(register, source_path="register.json")

    def test_duplicate_consumers_fail_closed(self) -> None:
        register = _register()
        register["aliases"][0]["consumers"].append(
            dict(register["aliases"][0]["consumers"][0])
        )
        with self.assertRaisesRegex(DiscoveryIndexError, "duplicate consumer_id"):
            build_discovery_index(register, source_path="register.json")

    def test_source_authority_cannot_escalate(self) -> None:
        register = _register()
        register["authority"] = "alias_authority"
        with self.assertRaisesRegex(DiscoveryIndexError, "authority must remain"):
            build_discovery_index(register, source_path="register.json")

    def test_self_alias_fails_closed(self) -> None:
        register = _register()
        register["aliases"][0]["canonical_target"] = register["aliases"][0]["old_path"]
        with self.assertRaisesRegex(DiscoveryIndexError, "own canonical target"):
            build_discovery_index(register, source_path="register.json")

    def test_alias_chains_fail_closed(self) -> None:
        register = _register()
        register["aliases"][0]["canonical_target"] = register["aliases"][1]["old_path"]
        with self.assertRaisesRegex(DiscoveryIndexError, "another registered alias"):
            build_discovery_index(register, source_path="register.json")

    def test_cli_is_deterministic_and_omits_sensitive_or_decisional_fields(self) -> None:
        register = _register()
        register["aliases"][0]["owner"] = "private-owner"
        register["aliases"][0]["source_digest"] = "sha256:sensitive-lineage"
        register["aliases"][0]["consumers"][0]["evidence_ref"] = "private-evidence"
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "register.json"
            path.write_text(json.dumps(register), encoding="utf-8")
            outputs: list[str] = []
            for _ in range(2):
                stream = io.StringIO()
                with redirect_stdout(stream):
                    self.assertEqual(0, main(["--register", str(path)]))
                outputs.append(stream.getvalue())
        self.assertEqual(outputs[0], outputs[1])
        output = json.loads(outputs[0])
        self.assertEqual("path-alias-discovery-metadata-only", output["scope"])
        rendered = outputs[0]
        self.assertNotIn("private-owner", rendered)
        self.assertNotIn("sensitive-lineage", rendered)
        self.assertNotIn("private-evidence", rendered)
        self.assertEqual(
            {
                "aliases_authorized": False,
                "consumer_closure_decided": False,
                "paths_migrated_or_deleted": False,
                "publication_inferred": False,
            },
            output["non_effects"],
        )


if __name__ == "__main__":
    unittest.main()
