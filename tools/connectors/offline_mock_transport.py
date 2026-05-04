import json
from pathlib import Path

def execute(plan_path: str) -> dict:
    p = json.loads(Path(plan_path).read_text())
    if p.get('no_network') is not True or p.get('transport') != 'offline_mock':
        return {'finite_state': 'ERROR', 'reason': 'INVALID_TRANSPORT'}
    if p.get('credentials_present'):
        return {'finite_state': 'DENY', 'reason': 'CREDENTIALS_NOT_ALLOWED'}
    if p.get('finite_state') != 'PLAN_READY_FOR_SIMULATION':
        return {'finite_state': 'BLOCKED', 'reason': 'PLAN_NOT_ALLOWED'}
    return {'finite_state': 'SIMULATED', 'synthetic': True, 'not_public_claim_evidence': True}
