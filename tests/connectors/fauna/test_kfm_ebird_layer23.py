from __future__ import annotations
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RERUN = ROOT / 'tools/connectors/fauna/kfm-ebird-ingest/kfm-ebird-rerun-remediation'
BACKFILL = ROOT / 'tools/connectors/fauna/kfm-ebird-ingest/kfm-ebird-backfill'
FIXTURE = ROOT / 'tests/fixtures/fauna/ebird/sample_ebd.tsv'


def test_rerun_help_and_version():
    assert subprocess.run([str(RERUN), '--help'], capture_output=True).returncode == 0
    assert subprocess.run([str(RERUN), '--version'], capture_output=True).returncode == 0


def test_backfill_help_and_version():
    assert subprocess.run([str(BACKFILL), '--help'], capture_output=True).returncode == 0
    assert subprocess.run([str(BACKFILL), '--version'], capture_output=True).returncode == 0


def test_rerun_id_deterministic(tmp_path: Path):
    out1 = tmp_path / 'a'; out2 = tmp_path / 'b'
    cmd = [str(RERUN), '--mode', 'plan', '--aggregate', 'huc12', '--ebd-file', str(FIXTURE), '--source-uri', f'file://{FIXTURE}', '--out-dir']
    id1 = subprocess.check_output([*cmd, str(out1)], text=True).strip()
    id2 = subprocess.check_output([*cmd, str(out2)], text=True).strip()
    assert id1 == id2


def test_backfill_period_validation(tmp_path: Path):
    p = subprocess.run([str(BACKFILL), '--mode', 'plan', '--period', '2026-13', '--out-dir', str(tmp_path)], capture_output=True, text=True)
    assert p.returncode == 2


def test_candidate_blocks_failed_public_safety(tmp_path: Path):
    public = tmp_path / 'public'; public.mkdir()
    (public / 'bad.json').write_text(json.dumps({'decimalLatitude': 1}), encoding='utf-8')
    out = tmp_path / 'catalog'
    subprocess.check_call([str(RERUN), '--mode', 'candidate', '--aggregate', 'huc12', '--public-out-dir', str(public), '--out-dir', str(out)])
    candidate = json.loads((out / 'data_affecting_corrective_release_candidate.json').read_text())
    assert 'public_safety_validation_failed' in candidate['blockers']
