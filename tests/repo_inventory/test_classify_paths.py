from tools.repo_inventory.classify_paths import classify

def test_classify_domains_doc():
    assert classify('docs/domains/hydrology/README.md') == 'doc_domain'

def test_classify_policy_split():
    assert classify('policy/README.md') == 'policy'
    assert classify('policies/README.md') == 'policy'
