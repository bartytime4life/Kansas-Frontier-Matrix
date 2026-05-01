from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def test_files_exist():
 for p in [
  'policy/air/air_reentry_deployment_authorization_refresh.rego',
  'tools/deployments/air/record_air_reentry_release_manager_refresh_decision.py',
  'tools/validators/air/validate_air_reentry_deployment_authorization_refresh.py',
  'docs/domains/atmosphere/AIR_REENTRY_DEPLOYMENT_AUTHORIZATION_REFRESH_SLICE.md',
 ]:
  assert (ROOT/p).exists()
