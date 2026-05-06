from tools.repo_inventory.classify_paths import classify

def test_classify_known():
    assert classify('docs/adr/ADR-0001-schema-home.md')=='doc_adr'
    assert classify('data/raw/sample.json')=='data_lifecycle_raw'
    assert classify('apps/web/src/main.js')=='app_web'
