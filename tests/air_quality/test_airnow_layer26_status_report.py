from pathlib import Path
def test_status_report_limitations_language():
 s=Path('tests/fixtures/air_quality/airnow/layer26/expected/preservation_closure_finalization_status_board.md').read_text().lower();r=Path('tests/fixtures/air_quality/airnow/layer26/expected/preservation_closure_finalization_report.md').read_text().lower();assert 'no public release' in r and 'no preservation' in s
