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


def _alias(
    alias_id: str,
    old_path: str,
    target: str,
    canonical_id: str,
    identity_aliases: list[str],
) -> dict:
    return {
        "alias_id": alias_id,
        "class": "legacy",
        "status": "ACTIVE",
        "old_path": old_path,
        "canonical_target": target,
        "object_family": "human_document",
        "identity_mapping": {
            "canonical_id": canonical_id,
            "aliases": identity_aliases,
            "identity_rule": "superseded_aliases_resolve_to_canonical",
        },
        "read_rule": "canonical_only_with_redirect",
        "write_rule": "canonical_only",
        "authority_mode": "non_authoritative",
        "verification_state": "PARTIAL",
        "consumers": [{"consumer_id": "should-not-project"}],
        "writers": {"alias": [], "canonical": ["should-not-project"]},
        "parity_validation": {"validation_refs": ["should-not-project"]},
    }


def _register() -> dict:
    return {
        "version": "v1",
        "registry": "path_alias_register",
        "status": "ACTIVE",
        "authority": "machine_projection_only",
        "coverage_scope": "accepted_directory_rules_aliases",
        "base_ref": "1" * 40,
        "aliases": [
            _alias(
                "alias.zeta",
                "docs/old-zeta.md",
                "docs/new-zeta.md",
                "kfm://doc/zeta",
                ["kfm://legacy/zeta", "kfm://legacy/zeta-2"],
            ),
            _alias(
                "alias.alpha",
                "docs/old-alpha.md",
                "docs/new-alpha.md",
                "kfm://doc/alpha",
                ["kfm://legacy/alpha"],
            ),
        ],
    }


class PathAliasDiscoveryIndexTests(unittest.TestCase):
    def test_builds_sorted_path_and_identity_alias_indexes(self) -> None:
        index = build_discovery_index(
            _register(), source_path="control_plane/path_alias_register.yaml"
        )
        self.assertFalse(index["authority_created"])
        self.assertEqual("derived_discovery_only", index["authority"])
        self.assertEqual(
            ["alias.alpha", "alias.zeta"],
            [item["alias_id"] for item in index["aliases"]],
        )
        self.assertEqual(
            ["docs/old-alpha.md", "docs/old-zeta.md"],
            [item["old_path"] for item in index["path_index"]],
        )
        self.assertEqual(
            [
                "kfm://legacy/alpha",
                "kfm://legacy/zeta",
                "kfm://legacy/zeta-2",
            ],
            [item["alias"] for item in index["identity_alias_index"]],
        )

    def test_render_is_deterministic(self) -> None:
        first = render_index(
            build_discovery_index(_register(), source_path="registry.json")
        )
        second = render_index(
            build_discovery_index(_register(), source_path="registry.json")
        )
        self.assertEqual(first, second)
        self.assertEqual(
            first,
            json.dumps(json.loads(first), sort_keys=True, separators=(",", ":"))
            + "\n",
        )

    def test_duplicate_alias_id_fails_closed(self) -> None:
        register = _register()
        register["aliases"][1]["alias_id"] = "alias.zeta"
        with self.assertRaisesRegex(
            DiscoveryIndexError, "alias_id values must be unique"
        ):
            build_discovery_index(register, source_path="registry.json")

    def test_duplicate_old_path_fails_closed(self) -> None:
        register = _register()
        register["aliases"][1]["old_path"] = "docs/old-zeta.md"
        with self.assertRaisesRegex(
            DiscoveryIndexError, "old_path values must be unique"
        ):
            build_discovery_index(register, source_path="registry.json")

    def test_alias_chain_fails_closed(self) -> None:
        register = _register()
        register["aliases"][0]["canonical_target"] = "docs/old-alpha.md"
        with self.assertRaisesRegex(
            DiscoveryIndexError, "canonical_target points to another alias path"
        ):
            build_discovery_index(register, source_path="registry.json")

    def test_duplicate_identity_alias_fails_closed(self) -> None:
        register = _register()
        register["aliases"][1]["identity_mapping"]["aliases"] = [
            "kfm://legacy/zeta"
        ]
        with self.assertRaisesRegex(
            DiscoveryIndexError, "identity alias .* is declared by both"
        ):
            build_discovery_index(register, source_path="registry.json")

    def test_source_authority_cannot_escalate(self) -> None:
        register = _register()
        register["authority"] = "path_authority"
        with self.assertRaisesRegex(DiscoveryIndexError, "authority must remain"):
            build_discovery_index(register, source_path="registry.json")

    def test_cli_stdout_is_deterministic_and_metadata_only(self) -> None:
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
                "path-alias-discovery-metadata-only", output["scope"]
            )
            alias = output["aliases"][0]
            self.assertNotIn("consumers", alias)
            self.assertNotIn("writers", alias)
            self.assertNotIn("parity_validation", alias)


if __name__ == "__main__":
    unittest.main()
