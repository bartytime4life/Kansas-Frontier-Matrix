from pathlib import Path

import yaml


WORKFLOW_PATH = Path('.github/workflows/usda-plants-deploy-cloudflare-pages.yml')


def _load_workflow() -> dict:
    assert WORKFLOW_PATH.exists()
    return yaml.safe_load(WORKFLOW_PATH.read_text(encoding='utf-8'))


def test_workflow_exists_and_dispatch_only():
    wf = _load_workflow()
    assert 'workflow_dispatch' in wf['on']
    assert 'schedule' not in wf['on']
    assert 'push' not in wf['on']
    assert 'pull_request' not in wf['on']


def test_deploy_toggle_defaults_false_and_condition_guarded():
    wf = _load_workflow()
    inputs = wf['on']['workflow_dispatch']['inputs']
    assert inputs['deploy_to_cloudflare']['default'] == 'false'
    assert inputs['deploy_to_cloudflare']['options'] == ['false', 'true']
    assert wf['jobs']['deploy']['if'] == "${{ inputs.deploy_to_cloudflare == 'true' }}"


def test_deploy_job_environment_and_permissions():
    wf = _load_workflow()
    assert wf['permissions'] == {'contents': 'read'}
    assert wf['jobs']['dry-run']['permissions'] == {'contents': 'read'}
    assert wf['jobs']['deploy']['permissions'] == {'contents': 'read'}
    assert wf['jobs']['deploy']['environment'] == 'usda-plants-external-deployment'


def test_secret_references_are_names_only_and_no_literals():
    text = WORKFLOW_PATH.read_text(encoding='utf-8')
    assert 'CLOUDFLARE_API_TOKEN' in text
    assert 'CLOUDFLARE_ACCOUNT_ID' in text
    assert 'ghp_' not in text
    assert 'AKIA' not in text
    assert 'secret_' not in text.lower()
