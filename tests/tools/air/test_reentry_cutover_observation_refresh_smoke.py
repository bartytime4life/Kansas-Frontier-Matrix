from pathlib import Path

def test_schema_files_exist():
    base = Path('schemas/contracts/v1/air')
    assert (base/'reentry_cutover_observation_refresh_record.schema.json').exists()
    assert (base/'reentry_post_deploy_gate_refresh_evaluation.schema.json').exists()
