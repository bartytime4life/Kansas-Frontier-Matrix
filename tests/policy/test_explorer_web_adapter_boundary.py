from pathlib import Path

ROOT = Path("apps/explorer-web/src")


def test_maplibre_and_cesium_imports_stay_in_adapters_only() -> None:
    adapter_dir = ROOT / "adapters"
    for ts_file in list(ROOT.rglob("*.ts")) + list(ROOT.rglob("*.tsx")) + list(ROOT.rglob("*.js")) + list(ROOT.rglob("*.jsx")):
        text = ts_file.read_text(encoding="utf-8")
        is_adapter = adapter_dir in ts_file.parents
        for line in text.splitlines():
            stripped = line.strip()
            if "maplibre" in stripped.lower() or "cesium" in stripped.lower():
                if stripped.startswith("import ") or stripped.startswith("from "):
                    assert is_adapter, f"Runtime map import must stay in adapters: {ts_file}:{line}"


def test_explorer_web_has_no_internal_data_store_path_literals() -> None:
    forbidden = (
        "data/raw",
        "data/work",
        "data/quarantine",
        "data/processed",
        "data/catalog",
        "data/published",
        "release/",
    )
    for ts_file in list(ROOT.rglob("*.ts")) + list(ROOT.rglob("*.tsx")) + list(ROOT.rglob("*.js")) + list(ROOT.rglob("*.jsx")):
        text = ts_file.read_text(encoding="utf-8")
        for marker in forbidden:
            assert marker not in text, f"Forbidden store path literal in {ts_file}: {marker}"
