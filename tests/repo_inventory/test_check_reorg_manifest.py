from pathlib import Path

def test_manifest_files_exist():
    base=Path('docs/registers/reorg')
    assert (base/'REORG_SPRINT_MANIFEST.md').exists()
