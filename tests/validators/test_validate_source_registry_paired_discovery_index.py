from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

VALIDATOR_PATH = (
    Path(__file__).resolve().parents[2]
    / "tools"
    / "validators"
    / "catalog"
    / "validate_source_registry_paired_discovery_index.py"
)

_SPEC = importlib.util.spec_from_file_location(
    "validate_source_registry_paired_discovery_index", VALIDATOR_PATH
)
assert _SPEC and _SPEC.loader
_MODULE = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_MODULE)

validate_source_registry_paired_discovery_index = (
    _MODULE.validate_source_registry_paired_discovery_index
)


def _readme(*pairs: tuple[str, str]) -> str:
    rows = "\n".join(
        f"| {canonical.title()} | [`sources/{canonical}/`]({canonical}/README.md) "
        f"| [`{parallel}/sources/`](../{canonical}/sources/README.md) |"
        for canonical, parallel in pairs
    )
    return f"""# Source Registry

The 13 paired domain README lanes confirmed at the pinned base are:

| Domain | Canonical-family lane | Parallel domain-first lane |
|---|---|---|
{rows}

## Write rule while topology is unresolved
"""


class SourceRegistryPairedDiscoveryIndexTests(unittest.TestCase):
    def _fixture(
        self,
        pairs: tuple[tuple[str, str], ...],
        canonical: tuple[str, ...],
        parallel: tuple[str, ...],
    ):
        tempdir = tempfile.TemporaryDirectory()
        repo = Path(tempdir.name)
        source_root = repo / "data" / "registry" / "sources"
        source_root.mkdir(parents=True)
        (source_root / "README.md").write_text(_readme(*pairs), encoding="utf-8")

        for domain in canonical:
            lane = source_root / domain
            lane.mkdir()
            (lane / "README.md").write_text(f"# {domain}\n", encoding="utf-8")

        for domain in parallel:
            lane = repo / "data" / "registry" / domain / "sources"
            lane.mkdir(parents=True)
            (lane / "README.md").write_text(f"# {domain} sources\n", encoding="utf-8")
        return tempdir, repo

    def test_current_paired_topology_passes(self) -> None:
        pairs = (("agriculture", "agriculture"), ("atmosphere", "atmosphere"))
        tempdir, repo = self._fixture(
            pairs,
            ("agriculture", "atmosphere"),
            ("agriculture", "atmosphere"),
        )
        self.addCleanup(tempdir.cleanup)
        report = validate_source_registry_paired_discovery_index(repo)
        self.assertEqual("PASS", report["outcome"])
        self.assertFalse(report["authority_created"])

    def test_standalone_canonical_lane_is_not_forced_into_paired_index(self) -> None:
        tempdir, repo = self._fixture(
            (("agriculture", "agriculture"),),
            ("agriculture", "atmosphere"),
            ("agriculture",),
        )
        self.addCleanup(tempdir.cleanup)
        report = validate_source_registry_paired_discovery_index(repo)
        self.assertEqual("PASS", report["outcome"])
        self.assertEqual([], report["missing_canonical_index"])
        self.assertEqual(["atmosphere"], report["unpaired_canonical_domains"])

    def test_standalone_parallel_lane_is_not_forced_into_paired_index(self) -> None:
        tempdir, repo = self._fixture(
            (("agriculture", "agriculture"),),
            ("agriculture",),
            ("agriculture", "atmosphere"),
        )
        self.addCleanup(tempdir.cleanup)
        report = validate_source_registry_paired_discovery_index(repo)
        self.assertEqual("PASS", report["outcome"])
        self.assertEqual([], report["missing_parallel_index"])
        self.assertEqual(["atmosphere"], report["unpaired_parallel_domains"])

    def test_unindexed_paired_lane_fails_closed(self) -> None:
        tempdir, repo = self._fixture(
            (("agriculture", "agriculture"),),
            ("agriculture", "atmosphere"),
            ("agriculture", "atmosphere"),
        )
        self.addCleanup(tempdir.cleanup)
        report = validate_source_registry_paired_discovery_index(repo)
        self.assertEqual("FAIL", report["outcome"])
        self.assertEqual(["atmosphere"], report["missing_canonical_index"])
        self.assertEqual(["atmosphere"], report["missing_parallel_index"])
        self.assertEqual([], report["unpaired_canonical_domains"])
        self.assertEqual([], report["unpaired_parallel_domains"])

    def test_stale_index_row_fails_closed(self) -> None:
        tempdir, repo = self._fixture(
            (("agriculture", "agriculture"), ("atmosphere", "atmosphere")),
            ("agriculture",),
            ("agriculture",),
        )
        self.addCleanup(tempdir.cleanup)
        report = validate_source_registry_paired_discovery_index(repo)
        self.assertEqual("FAIL", report["outcome"])
        self.assertEqual(["atmosphere"], report["stale_canonical_index"])
        self.assertEqual(["atmosphere"], report["stale_parallel_index"])

    def test_missing_canonical_readme_fails_closed(self) -> None:
        tempdir, repo = self._fixture(
            (("agriculture", "agriculture"),),
            ("agriculture",),
            ("agriculture",),
        )
        self.addCleanup(tempdir.cleanup)
        canonical_readme = (
            repo / "data" / "registry" / "sources" / "agriculture" / "README.md"
        )
        canonical_readme.unlink()

        report = validate_source_registry_paired_discovery_index(repo)

        self.assertEqual("FAIL", report["outcome"])
        self.assertEqual(["agriculture"], report["missing_canonical_readmes"])
        self.assertEqual([], report["stale_canonical_index"])

    def test_missing_parallel_readme_fails_closed(self) -> None:
        tempdir, repo = self._fixture(
            (("agriculture", "agriculture"),),
            ("agriculture",),
            ("agriculture",),
        )
        self.addCleanup(tempdir.cleanup)
        parallel_readme = (
            repo / "data" / "registry" / "agriculture" / "sources" / "README.md"
        )
        parallel_readme.unlink()

        report = validate_source_registry_paired_discovery_index(repo)

        self.assertEqual("FAIL", report["outcome"])
        self.assertEqual(["agriculture"], report["missing_parallel_readmes"])
        self.assertEqual([], report["stale_parallel_index"])

    def test_duplicate_index_row_fails_closed(self) -> None:
        tempdir, repo = self._fixture(
            (("agriculture", "agriculture"), ("agriculture", "agriculture")),
            ("agriculture",),
            ("agriculture",),
        )
        self.addCleanup(tempdir.cleanup)
        report = validate_source_registry_paired_discovery_index(repo)
        self.assertEqual("FAIL", report["outcome"])
        self.assertEqual(["agriculture"], report["duplicate_index_domains"])

    def test_row_domain_mismatch_fails_closed(self) -> None:
        tempdir, repo = self._fixture(
            (("agriculture", "atmosphere"),),
            ("agriculture",),
            ("atmosphere",),
        )
        self.addCleanup(tempdir.cleanup)
        report = validate_source_registry_paired_discovery_index(repo)
        self.assertEqual("FAIL", report["outcome"])
        self.assertEqual(
            ["agriculture!=atmosphere"], report["row_domain_mismatches"]
        )

    def test_malformed_pairing_row_fails_closed(self) -> None:
        tempdir, repo = self._fixture(
            (("agriculture", "agriculture"),),
            ("agriculture",),
            ("agriculture",),
        )
        self.addCleanup(tempdir.cleanup)
        readme = repo / "data" / "registry" / "sources" / "README.md"
        readme.write_text(
            readme.read_text(encoding="utf-8").replace(
                "[`agriculture/sources/`](../agriculture/sources/README.md)",
                "[`agriculture/sources/`](../agriculture/sources/README.md",
            ),
            encoding="utf-8",
        )

        report = validate_source_registry_paired_discovery_index(repo)

        self.assertEqual("FAIL", report["outcome"])
        self.assertEqual(1, len(report["invalid_index_rows"]))
        self.assertEqual(["agriculture"], report["missing_canonical_index"])
        self.assertEqual(["agriculture"], report["missing_parallel_index"])

    def test_missing_section_errors(self) -> None:
        tempdir, repo = self._fixture(
            (("agriculture", "agriculture"),),
            ("agriculture",),
            ("agriculture",),
        )
        self.addCleanup(tempdir.cleanup)
        readme = repo / "data" / "registry" / "sources" / "README.md"
        readme.write_text("# Source Registry\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "missing section marker"):
            validate_source_registry_paired_discovery_index(repo)

    def test_cli_output_is_deterministic_json(self) -> None:
        tempdir, repo = self._fixture(
            (("agriculture", "agriculture"), ("atmosphere", "atmosphere")),
            ("agriculture", "atmosphere"),
            ("agriculture", "atmosphere"),
        )
        self.addCleanup(tempdir.cleanup)
        first = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--repo-root", str(repo)],
            check=False,
            capture_output=True,
            text=True,
        )
        second = subprocess.run(
            [sys.executable, str(VALIDATOR_PATH), "--repo-root", str(repo)],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, first.returncode)
        self.assertEqual(first.stdout, second.stdout)
        parsed = json.loads(first.stdout)
        self.assertEqual(
            "kfm.source-registry-paired-discovery-index.v4", parsed["profile"]
        )
        self.assertEqual("PASS", parsed["outcome"])


if __name__ == "__main__":
    unittest.main()
