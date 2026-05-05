from pathlib import Path

CANONICAL_PREFIX = Path("schemas/contracts/v1")
EXEMPT_PHRASES = {
    "human contract docs",
    "compatibility examples",
    "generated mirrors",
}


def is_machine_schema(path: Path) -> bool:
    return path.name.endswith(".schema.json")


def _readme_has_exemption(path: Path) -> bool:
    for parent in [path.parent, *path.parents]:
        readme = parent / "README.md"
        if readme.exists():
            text = readme.read_text(encoding="utf-8").lower()
            if any(p in text for p in EXEMPT_PHRASES):
                return True
    return False


IGNORED_PREFIXES = {"fixtures/policy/schema_home/"}


def collect_violations(root: Path) -> list[str]:
    violations: list[str] = []
    for p in root.rglob("*.schema.json"):
        rel = p.relative_to(root)
        if str(rel).startswith(str(CANONICAL_PREFIX)):
            continue

        rel_str = rel.as_posix()
        if any(rel_str.startswith(prefix) for prefix in IGNORED_PREFIXES):
            continue
        in_forbidden_surface = rel_str.startswith("contracts/") or rel_str.startswith("jsonschema/")
        if in_forbidden_surface and _readme_has_exemption(p):
            continue

        violations.append(
            f"schema outside canonical home: {rel_str} (expected under schemas/contracts/v1/ or documented exemption)"
        )
    return violations


def main() -> int:
    root = Path(".")
    violations = collect_violations(root)
    if violations:
        print("FAIL", violations)
        return 1
    print("PASS", "schema-home enforcement satisfied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
