from tools.repo_inventory.classify_paths import cls

def test_basic():
    assert cls('apps/web/src/main.js')=='app_web'
    assert cls('docs/adr/ADR-0001-schema-home.md')=='doc_adr'
    assert cls('data/raw/x.txt')=='data_lifecycle_raw'
