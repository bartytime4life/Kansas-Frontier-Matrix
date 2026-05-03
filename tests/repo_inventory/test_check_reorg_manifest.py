from tools.repo_inventory.check_reorg_manifest import check

def test_files_exist():
    assert check('docs/registers/reorg') == []
