from pathlib import Path

def test_manifest_files_exist():
    d=Path('docs/registers/reorg')
    for n in ['REORG_SPRINT_MANIFEST.md','path_inventory.tsv','move_plan.tsv','reference_update_plan.tsv','authority_conflicts.md','validation_report.md','rollback_plan.sh']:
        assert (d/n).exists()
