from pathlib import Path

ALLOWED_CLASSES = {
    "canonical",
    "compatibility",
    "transitional",
    "generated",
    "data-lifecycle",
    "release/proof",
    "runtime",
    "policy",
    "UNKNOWN",
}

REQUIRED_CROSSLINKS = {
    ".github",
    "docs",
    "control_plane",
    "contracts",
    "schemas",
    "policy",
    "policies",
    "ui",
    "web",
    "jsonschema",
    "styles",
    "viewer_templates",
}


def parse_register(path: Path) -> tuple[dict[str, str], set[str]]:
    roots: dict[str, str] = {}
    cross_links: set[str] = set()

    lines = path.read_text(encoding="utf-8").splitlines()
    mode = None
    current_root = None
    current_cross = None

    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        if stripped == "roots:":
            mode = "roots"
            current_root = None
            continue
        if stripped == "cross_links:":
            mode = "cross"
            current_cross = None
            continue

        if mode == "roots":
            if line.startswith("  ") and not line.startswith("    ") and stripped.endswith(":"):
                current_root = stripped[:-1]
                continue
            if current_root and stripped.startswith("class:"):
                roots[current_root] = stripped.split(":", 1)[1].strip()
                continue

        if mode == "cross":
            if line.startswith("  ") and not line.startswith("    ") and stripped.endswith(":"):
                current_cross = stripped[:-1]
                cross_links.add(current_cross)
                continue

    return roots, cross_links


def main() -> int:
    register_path = Path("control_plane/root_surface_register.yaml")
    doc_path = Path("docs/registers/root-surface-register.md")
    if not register_path.exists() or not doc_path.exists():
        print("FAIL", "missing register source files")
        return 1

    roots, cross_links = parse_register(register_path)
    errors = []

    root_dirs = {p.name for p in Path(".").iterdir() if p.is_dir()}
    for d in sorted(root_dirs):
        if d not in roots:
            errors.append(f"root missing from register: {d}")
        elif roots[d] not in ALLOWED_CLASSES:
            errors.append(f"invalid class for root {d}: {roots[d]}")

    for d, c in sorted(roots.items()):
        if c not in ALLOWED_CLASSES:
            errors.append(f"invalid class in register for {d}: {c}")

    for k in sorted(REQUIRED_CROSSLINKS):
        if k not in cross_links:
            errors.append(f"missing required cross-link: {k}")

    if errors:
        print("FAIL", errors)
        return 1

    print("PASS", "root surface register is complete and valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
