from pathlib import Path

FORBIDDEN_DOMAIN_ROOTS = {"hydrology", "soil", "fauna", "roads", "archaeology", "agriculture"}
FORBIDDEN_MISC_ROOTS = {"ui", "web", "jsonschema", "policies", "styles", "viewer_templates"}


def main() -> int:
    root_dirs = {p.name for p in Path(".").iterdir() if p.is_dir()}

    violations = []
    for d in sorted(FORBIDDEN_DOMAIN_ROOTS & root_dirs):
        violations.append(f"forbidden domain root directory: {d}/")
    for d in sorted(FORBIDDEN_MISC_ROOTS & root_dirs):
        violations.append(f"forbidden greenfield root directory: {d}/")

    if violations:
        print("FAIL", violations)
        return 1

    print("PASS", "directory rules satisfied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
