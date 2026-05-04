from pathlib import Path

REQUIRED_PATHS = [
    "README.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    ".github/workflows/baseline.yml",
    "docs/reports/bootstrap-repo-inspection.md",
    "docs/sources/SOURCE_LEDGER.md",
    "control_plane/source_authority_register.yaml",
    "contracts/source/source_descriptor.md",
    "schemas/contracts/v1/source/source_descriptor.schema.json",
    "fixtures/source/source_descriptor.valid.json",
    "tools/validate_fixtures.py",
    "tools/validate_schema_conformance.py",
    "tools/validate_api_contracts.py",
    "apps/api/kfm_mock_api.py",
    "apps/web/index.html",
    "scripts/validate_all.sh",
    "tests/test_fixture_validation.py",
    "tests/test_api_contracts.py",
    "release/dry_runs/synthetic_hydrology_release_manifest.json",
]

REQUIRED_DIRS = [
    "docs",
    "control_plane",
    "contracts",
    "schemas",
    "policy",
    "tests",
    "fixtures",
    "tools",
    "scripts",
    "apps",
    "packages",
    "connectors",
    "pipelines",
    "pipeline_specs",
    "data",
    "release",
    "runtime",
    "infra",
    "configs",
    "migrations",
    "examples",
]


def main() -> int:
    missing = [p for p in REQUIRED_PATHS if not Path(p).exists()]
    missing += [f"{d}/" for d in REQUIRED_DIRS if not Path(d).is_dir()]

    if missing:
        print("FAIL", missing)
        return 1

    print("PASS", "required repository skeleton present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
