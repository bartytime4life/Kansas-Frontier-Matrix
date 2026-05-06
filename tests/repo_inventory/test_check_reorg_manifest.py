from pathlib import Path
from tools.repo_inventory.check_reorg_manifest import REQ

def test_required_constants():
    assert 'path_inventory.tsv' in REQ
    assert Path('tools/repo_inventory').exists()
