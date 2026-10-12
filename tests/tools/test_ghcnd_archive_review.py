"""Offline history, immutable replay, and private-store failure boundaries."""
import csv
import hashlib
import json
from pathlib import Path
import zipfile

import pytest

from tests.domains.atmosphere.ghcnd_daily_fixtures import acquired
from tools.local_data import ghcnd_archive_review as review
from tools.local_data.ghcnd_daily_pilot import object_path, stage
from tools.local_data.manage import init_store, store_lock


@pytest.fixture
def prepared(tmp_path):
    root = tmp_path / 'store'
    init_store(root)
    # Out-of-window records are important: the pilot does not review these rows.
    def older(key, text):
        if key.startswith('by_station/'):
            sid = key.split('/')[1].removesuffix('.csv.gz')
            text += (f'{sid},19000101,PRCP,0,T,,W,\n'
                     f'{sid},19000102,TMAX,-9999,,,W,\n'
                     f'{sid},19000103,TMIN,15,,X,W,\n')
        return text
    capture = acquired(older)
    stage(root, capture)
    return root, capture


def run(prepared, **kw):
    root, capture = prepared
    return review.derive(root, capture.manifest['capture_id'], **kw)


def receipt_path(prepared, result):
    return prepared[0] / 'data/receipts/curation/noaa-ghcnd-archive-review' / Path(result['destination']).name / 'verified.json'


def test_full_history_flags_units_ids_and_replay(prepared):
    result = run(prepared)
    target = Path(result['destination'])
    with (target / 'observations.csv').open() as handle:
        rows = list(csv.DictReader(handle))
    assert result['first_day'] == '1900-01-01'
    assert len({r['id'] for r in rows}) == len(rows)
    older = [r for r in rows if r['observation_date'] < '1901']
    assert len(older) == 12
    for row in older:
        if row['element'] == 'PRCP':
            assert row['value'] == '0.0' and row['trace'] == 'True' and row['unit'] == 'mm'
        else:
            assert row['value'] == '' and row['withheld'] in {'MISSING', 'QUALITY_FLAG'} and row['unit'] == 'degC'
        assert row['record_digest'].startswith('sha256:')
        assert row['preliminary'] == 'True' and row['source_role'] == 'observed_station'
    manifest = json.loads((target / 'review-manifest.json').read_bytes())
    assert 'not scientific validity' in manifest['count_semantics']
    assert not result['admitted'] and not result['released'] and not result['published']
    before = {p.name: p.read_bytes() for p in target.iterdir()}
    assert run(prepared)['outcome'] == 'ALREADY_VERIFIED'
    assert before == {p.name: p.read_bytes() for p in target.iterdir()}


@pytest.mark.parametrize('kind', ['output', 'extra', 'receipt', 'missing-output', 'zip-member'])
def test_replay_tampering_is_held_without_overwrite(prepared, kind):
    result = run(prepared)
    target = Path(result['destination'])
    rpath = receipt_path(prepared, result)
    receipt = json.loads(rpath.read_bytes())
    if kind == 'output':
        with (target / 'observations.csv').open('ab') as out:
            out.write(b'bad')
    elif kind == 'extra':
        (target / 'unexpected.csv').write_bytes(b'bad')
    elif kind == 'receipt':
        receipt['released'] = True
        rpath.write_bytes(review.canon(receipt))
    elif kind == 'missing-output':
        receipt['outputs'].pop()
        rpath.write_bytes(review.canon(receipt))
    else:
        package = target / 'review-package.zip'
        with zipfile.ZipFile(package, 'w') as archive:
            archive.writestr('../escape', b'bad')
        receipt['package'].update(bytes=package.stat().st_size, sha256=hashlib.sha256(package.read_bytes()).hexdigest())
        rpath.write_bytes(review.canon(receipt))
    before = {p.name: p.read_bytes() for p in target.iterdir()}
    with pytest.raises(ValueError):
        run(prepared)
    assert before == {p.name: p.read_bytes() for p in target.iterdir()}


def test_source_digest_mismatch_before_derivative(prepared):
    root, capture = prepared
    page = capture.manifest['pages'][-1]
    object_path(root, page['sha256']).write_bytes(b'changed')
    with pytest.raises(ValueError):
        run(prepared)
    assert not (root / 'data/work/atmosphere/noaa-ghcnd-archive-review').exists()


def test_partial_limit_failure_retained_and_retry_denied(prepared):
    with pytest.raises(ValueError, match='REVIEW_OUTPUT_LIMIT'):
        run(prepared, max_output_bytes=1000)
    root = prepared[0]
    targets = list((root / 'data/work/atmosphere/noaa-ghcnd-archive-review').iterdir())
    assert len(targets) == 1
    partial = (targets[0] / 'observations.csv').read_bytes()
    receipts = root / 'data/receipts/curation/noaa-ghcnd-archive-review' / targets[0].name
    assert (receipts / 'failed.json').exists() and not (receipts / 'verified.json').exists()
    with pytest.raises(FileNotFoundError):
        run(prepared, max_output_bytes=1000)
    assert partial == (targets[0] / 'observations.csv').read_bytes()


def test_duplicate_outside_pilot_window_is_held(tmp_path):
    root = tmp_path / 'store'
    init_store(root)
    def duplicate(key, text):
        if key.startswith('by_station/'):
            sid = key.split('/')[1].removesuffix('.csv.gz')
            text += f'{sid},19000101,PRCP,1,,,W,\n' * 2
        return text
    capture = acquired(duplicate)
    assert stage(root, capture)['outcome'] == 'CANDIDATE_READY'
    with pytest.raises(ValueError, match='DUPLICATE_STATION_DAY_ELEMENT'):
        review.derive(root, capture.manifest['capture_id'])
    assert list(root.glob('data/receipts/curation/noaa-ghcnd-archive-review/*/failed.json'))


def test_writer_and_static_link_denied(prepared):
    root = prepared[0]
    with store_lock(root):
        with pytest.raises(ValueError, match='STORE_LOCKED'):
            run(prepared)
    (root / 'data/work/atmosphere/noaa-ghcnd-archive-review').symlink_to(root / 'data/published')
    with pytest.raises(ValueError, match='DIRECTORY_SYMLINK_OR_SPECIAL'):
        run(prepared)
    assert not list((root / 'data/published').iterdir())


def test_output_link_denied_on_replay(prepared):
    result = run(prepared)
    target = Path(result['destination'])
    output = target / 'observations.csv'
    retained = target.parent / 'retained.csv'
    output.rename(retained)
    output.symlink_to(retained)
    with pytest.raises(ValueError, match='INPUT_SYMLINK_OR_SPECIAL'):
        run(prepared)


@pytest.mark.parametrize('limit', [0, True, review.LIMIT + 1])
def test_invalid_limits_before_writes(prepared, limit):
    with pytest.raises(ValueError, match='REVIEW_OUTPUT_LIMIT_INVALID'):
        run(prepared, max_output_bytes=limit)


def test_disk_reserve_before_started_receipt(prepared, monkeypatch):
    monkeypatch.setattr(review.shutil, 'disk_usage', lambda _: type('Disk', (), {'free': 0})())
    with pytest.raises(ValueError, match='INSUFFICIENT_REVIEW_SPACE'):
        run(prepared)
    assert not list(prepared[0].glob('data/receipts/curation/noaa-ghcnd-archive-review/*/started.json'))
