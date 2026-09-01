import json
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
PACKAGE_ROOT = REPO_ROOT / "packages" / "maplibre"
EXPECTED_EXPORTS = {
    "@kfm/maplibre": "src/index.ts",
    "@kfm/maplibre/adapter": "src/maplibre-adapter.ts",
    "@kfm/maplibre/vite-adapter": "src/maplibre-vite-adapter.ts",
}
EXPECTED_ROOT_EXPORTS = {
    'export * from "./map-runtime-port";',
    'export * from "./null-map-runtime";',
    'export * from "./map-runtime-terrain-fallback";',
}


def test_export_map_points_each_public_specifier_at_its_owned_source() -> None:
    manifest = json.loads((PACKAGE_ROOT / "package.json").read_text())

    assert manifest["name"] == "@kfm/maplibre"
    assert set(manifest["exports"]) == {".", "./adapter", "./vite-adapter"}

    for specifier, expected_path in EXPECTED_EXPORTS.items():
        suffix = specifier.removeprefix("@kfm/maplibre")
        export_key = f".{suffix}" if suffix else "."
        export_target = manifest["exports"][export_key]
        expected_target = f"./{expected_path}"

        assert export_target == {
            "types": expected_target,
            "import": expected_target,
            "default": expected_target,
        }
        assert (PACKAGE_ROOT / expected_path).is_file()


def test_root_facade_reexports_only_renderer_neutral_modules() -> None:
    root_source = (PACKAGE_ROOT / "src" / "index.ts").read_text()
    root_statements = {line.strip() for line in root_source.splitlines() if line.strip()}

    assert root_statements == EXPECTED_ROOT_EXPORTS


def test_node_resolves_root_and_adapter_subpaths_through_package_exports() -> None:
    script = """
const specifiers = JSON.parse(process.argv[1]);
const resolved = Object.fromEntries(
  specifiers.map((specifier) => [specifier, import.meta.resolve(specifier)]),
);
console.log(JSON.stringify(resolved));
"""
    result = subprocess.run(
        [
            "node",
            "--input-type=module",
            "--eval",
            script,
            json.dumps(list(EXPECTED_EXPORTS)),
        ],
        cwd=PACKAGE_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    resolved = json.loads(result.stdout)

    assert resolved == {
        specifier: (PACKAGE_ROOT / expected_path).resolve().as_uri()
        for specifier, expected_path in EXPECTED_EXPORTS.items()
    }
