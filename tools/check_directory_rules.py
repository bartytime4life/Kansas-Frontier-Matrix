from pathlib import Path

FORBIDDEN_DOMAIN_ROOTS = {"hydrology", "soil", "fauna", "roads", "archaeology", "agriculture"}
TRANSITIONAL_ROOTS = {"ui", "web", "jsonschema", "policies", "styles", "viewer_templates"}
TRANSITIONAL_STATUS_TERMS = {
    "canonical",
    "legacy",
    "generated",
    "mirrored",
    "awaiting-migration",
    "awaiting migration",
}


def _readme_declares_transitional_status(root: Path, dirname: str) -> bool:
    readme = root / dirname / "README.md"
    if not readme.exists():
        return False
    text = readme.read_text(encoding="utf-8").lower()
    return any(term in text for term in TRANSITIONAL_STATUS_TERMS)


def collect_violations(root: Path) -> list[str]:
    root_dirs = {p.name for p in root.iterdir() if p.is_dir()}
    violations: list[str] = []

    for d in sorted(FORBIDDEN_DOMAIN_ROOTS & root_dirs):
        violations.append(f"forbidden domain root directory: {d}/")

    for d in sorted(TRANSITIONAL_ROOTS & root_dirs):
        if not _readme_declares_transitional_status(root, d):
            violations.append(
                f"transitional root missing documented status README.md: {d}/ "
                f"(must declare canonical/legacy/generated/mirrored/awaiting-migration)"
            )

    return violations


def main() -> int:
    violations = collect_violations(Path("."))
    if violations:
        print("FAIL", violations)
        return 1

    print("PASS", "directory rules satisfied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
