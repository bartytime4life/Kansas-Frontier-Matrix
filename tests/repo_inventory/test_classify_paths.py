from tools.repo_inventory.classify_paths import classify

def test_classify_core():
    assert classify('apps/web/src/main.js')=='app_web'
    assert classify('docs/domains/habitat/README.md')=='doc_domain'
    assert classify('data/raw/a.txt')=='data_lifecycle_raw'
