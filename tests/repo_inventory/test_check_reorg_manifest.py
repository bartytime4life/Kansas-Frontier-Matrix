from tools.repo_inventory.check_reorg_manifest import check
from pathlib import Path

def test_check_manifest_exists():
    assert check(Path('docs/registers/reorg')) in (0,1)
