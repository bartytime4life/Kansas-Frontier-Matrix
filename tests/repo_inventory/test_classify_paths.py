from tools.repo_inventory.classify_paths import classify

def test_classify_doc_domain():
    assert classify('docs/domains/hydrology/README.md')=='doc_domain'
