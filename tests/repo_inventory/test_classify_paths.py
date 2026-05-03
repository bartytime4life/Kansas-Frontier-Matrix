from tools.repo_inventory.classify_paths import classify

def test_classify_core():
    assert classify('apps/web/src/main.js')=='app_web'
    assert classify('docs/adr/ADR-0001-schema-home.md')=='doc_adr'
    assert classify('data/raw/x.json')=='data_lifecycle_raw'
