from pathlib import Path

from tests.policy.boundary_constants import FORBIDDEN_INTERNAL_STORE_PATHS

ROOT = Path("apps/explorer-web/src")
RAW_RENDERER_PACKAGES = (
    '"maplibre-gl"',
    "'maplibre-gl'",
    '"mapbox-gl"',
    "'mapbox-gl'",
    '"cesium"',
    "'cesium'",
    '"leaflet"',
    "'leaflet'",
    '"openlayers"',
    "'openlayers'",
)


def _source_files() -> list[Path]:
    return [
        *ROOT.rglob("*.ts"),
        *ROOT.rglob("*.tsx"),
        *ROOT.rglob("*.js"),
        *ROOT.rglob("*.jsx"),
    ]


def test_explorer_web_uses_kfm_port_instead_of_raw_renderer_imports() -> None:
    for source_file in _source_files():
        text = source_file.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), start=1):
            stripped = line.strip()
            if not (
                stripped.startswith("import ")
                or stripped.startswith("export ")
                or "require(" in stripped
                or "import(" in stripped
            ):
                continue
            for package in RAW_RENDERER_PACKAGES:
                assert package not in stripped, (
                    "Explorer Web must consume the KFM-owned @kfm/maplibre port; "
                    f"raw renderer acquisition is package-owned: {source_file}:{line_number}:{line}"
                )


def test_explorer_web_has_no_internal_data_store_path_literals() -> None:
    for source_file in _source_files():
        text = source_file.read_text(encoding="utf-8")
        for marker in FORBIDDEN_INTERNAL_STORE_PATHS:
            assert marker not in text, f"Forbidden store path literal in {source_file}: {marker}"
