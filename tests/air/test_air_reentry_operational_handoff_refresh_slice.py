from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def test_files_exist():
  for p in [
    'policy/air/air_reentry_operational_handoff_refresh.rego',
    'tools/operations/air/build_air_reentry_operational_handoff_refresh.py',
    'tools/operations/air/evaluate_air_reentry_watch_window_refresh.py',
    'tools/validators/air/validate_air_reentry_operational_handoff_refresh.py',
    'tools/auditors/air/audit_air_reentry_operational_handoff_refresh.py',
    'docs/domains/atmosphere-air/AIR_REENTRY_OPERATIONAL_HANDOFF_REFRESH_SLICE.md',
  ]:
    assert (ROOT/p).exists()
