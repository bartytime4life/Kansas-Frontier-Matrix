import json
from pathlib import Path

RELEASE_MANIFEST = Path("fixtures/release/release_manifest.valid.json")
MAP_RELEASE = Path("fixtures/release/map_release_manifest.valid.json")
DRY_RUN = Path("release/dry_runs/synthetic_hydrology_release_manifest.json")


def load(path: Path) -> dict:
    return json.loads(path.read_text())


def main() -> int:
    errors = []

    release = load(RELEASE_MANIFEST)
    map_release = load(MAP_RELEASE)
    dry_run = load(DRY_RUN)

    if release.get("rollback_target") != map_release.get("rollback_target"):
        errors.append("rollback_target mismatch between release and map-release manifests")
    if release.get("correction_route") != map_release.get("correction_route"):
        errors.append("correction_route mismatch between release and map-release manifests")

    if not dry_run.get("rollback_target"):
        errors.append("dry-run release manifest missing rollback_target")
    if not dry_run.get("correction_route"):
        errors.append("dry-run release manifest missing correction_route")

    if errors:
        print("FAIL", errors)
        return 1

    print("PASS", "release manifest consistency checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
