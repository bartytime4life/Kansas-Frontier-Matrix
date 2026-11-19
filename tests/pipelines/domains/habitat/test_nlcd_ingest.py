"""Actual GeoTIFF preparation, source-mask fidelity, semantic identity and fail-closed bounds."""
from copy import deepcopy
import base64
import json
from pathlib import Path
import subprocess
import sys

import pytest

rasterio = pytest.importorskip('rasterio', reason='NLCD native cases run in the locked imagery lane')
import numpy as np
from rasterio.io import MemoryFile
from rasterio.transform import from_origin, Affine

from connectors_core.captured_json import canonical_bytes
from pipelines.domains.habitat.ingest_nlcd import (
    FIXTURES, normalize_capture, replay_fixture, replay_packet, spec_hash, validate_candidate,
)

ROOT = Path(__file__).resolve().parents[4]


def packet():
    return json.loads((FIXTURES / 'base.json').read_text())


def source(cells=None, *, crs='EPSG:5070', dtype='uint8', nodata=0, transform=None, compression='NONE', mask=None):
    cells = np.array([[11, 41, 0, 90], [41, 90, 11, 0], [90, 11, 41, 0]], dtype=dtype) if cells is None else cells
    with rasterio.Env(GDAL_TIFF_INTERNAL_MASK=True):
        with MemoryFile() as memory:
            with memory.open(driver='GTiff', width=cells.shape[1], height=cells.shape[0], count=1,
                             dtype=dtype, crs=crs, transform=transform or from_origin(-100000, 2100000, 30, 30),
                             nodata=nodata, compress=compression) as dataset:
                dataset.write(cells, 1)
                if mask is not None:
                    dataset.write_mask(mask)
            return memory.read()


def normalize(raw, value=None):
    value = value or packet()
    return normalize_capture(raw, value['class_scheme'], value['capture'])


@pytest.mark.parametrize('name,counts', [('base', [3, 3, 3]), ('changed', [2, 4, 3])])
def test_native_replay_preserves_classes_support_and_no_authority(name, counts):
    result = replay_fixture(name)
    assert result == replay_fixture(name)
    value = result['candidate']
    assert [row['count'] for row in value['class_counts']] == counts
    assert value['support']['valid_count'] == 9
    assert value['support']['nodata_count'] == 3
    assert value['processing']['resampling'] == 'NONE'
    assert value['processing']['class_recode'] is False
    assert value['processing']['habitat_assertion'] is False
    assert value['uncertainty']['classification_accuracy'] == 'NOT_EVALUATED'
    assert value['governance']['review_required'] is True
    assert all(value['governance'][field] is False for field in
               ('source_admitted', 'review_completed', 'lifecycle_write', 'release_authorized', 'publication_authorized'))
    assert result['validation']['outcome'] == 'PASS'


def test_recompression_changes_byte_identity_while_preserving_observation_identity():
    first, second = normalize(source()), normalize(source(compression='LZW'))
    assert first['source_artifact_sha256'] != second['source_artifact_sha256']
    assert first['normalized_grid_sha256'] == second['normalized_grid_sha256']
    assert first['observation_id'] == second['observation_id']
    assert first['spec_hash'] != second['spec_hash']


def test_internal_valid_mask_is_preserved_without_class_recoding():
    mask = np.ones((3, 4), dtype='uint8') * 255
    mask[0, 0] = 0
    result = normalize(source(mask=mask))
    assert [row['count'] for row in result['class_counts']] == [2, 3, 3]
    assert result['support']['valid_count'] == 8
    assert result['support']['nodata_count'] == 4
    assert result['observation_id'] != normalize(source())['observation_id']


@pytest.mark.parametrize('kwargs', [
    {'crs': 'EPSG:4326'}, {'dtype': 'uint16'}, {'nodata': 255},
    {'transform': Affine(30, 1, -100000, 0, -30, 2100000)},
    {'cells': np.zeros((1024, 1025), dtype='uint8')},
])
def test_native_grid_contract_rejects_unsupported_inputs(kwargs):
    with pytest.raises(ValueError, match='NLCD_NATIVE_GRID_INVALID'):
        normalize(source(**kwargs))


def test_unknown_class_and_empty_coverage_are_refused():
    with pytest.raises(ValueError, match='NLCD_CLASS_NOT_IN_SCHEME'):
        normalize(source(np.array([[255]], dtype='uint8')))
    with pytest.raises(ValueError, match='NLCD_NO_VALID_PIXELS'):
        normalize(source(np.zeros((1, 1), dtype='uint8')))


def test_non_tiff_cannot_open_a_virtual_or_remote_dataset():
    with pytest.raises(ValueError, match='NLCD_CLASSIC_GEOTIFF_REQUIRED'):
        normalize(b'<VRTDataset><SourceFilename>https://example.test/private</SourceFilename></VRTDataset>')


def test_profile_hash_class_order_and_capture_times_are_bound():
    value = packet()
    value['class_scheme']['classes'][0]['label'] = 'changed legend'
    with pytest.raises(ValueError, match='NLCD_CLASS_SCHEME_DIGEST_MISMATCH'):
        normalize(source(), value)
    value['class_scheme']['classes'].reverse()
    value['class_scheme']['spec_hash'] = spec_hash(value['class_scheme'])
    with pytest.raises(ValueError, match='NLCD_CLASS_CODES_NOT_CANONICAL'):
        normalize(source(), value)
    value = packet()
    value['class_scheme']['classes'][0]['code'] = 11.0
    value['class_scheme']['spec_hash'] = spec_hash(value['class_scheme'])
    with pytest.raises(ValueError, match='NLCD_CLASS_CODES_NOT_CANONICAL'):
        normalize(source(), value)
    value = packet()
    value['capture']['valid_time']['end'] = '2099-01-01T00:00:00Z'
    with pytest.raises(ValueError, match='NLCD_CAPTURE_TIME_ORDER_INVALID'):
        normalize(source(), value)


def test_packet_and_candidate_tamper_never_gain_authority():
    value = packet()
    value['source_base64'] = base64.b64encode(b'substituted bytes').decode()
    with pytest.raises(ValueError, match='NLCD_SOURCE_DIGEST_MISMATCH'):
        replay_packet(canonical_bytes(value))
    value = packet()
    candidate = deepcopy(value['expected_candidate'])
    candidate['governance']['publication_authorized'] = True
    candidate['spec_hash'] = spec_hash(candidate)
    with pytest.raises(ValueError, match='NLCD_OBSERVATION_SCHEMA_INVALID'):
        validate_candidate(candidate, value['class_scheme'])
    candidate = deepcopy(value['expected_candidate'])
    candidate['support']['valid_count'] -= 1
    candidate['spec_hash'] = spec_hash(candidate)
    with pytest.raises(ValueError, match='NLCD_PIXEL_SUPPORT_MISMATCH'):
        validate_candidate(candidate, value['class_scheme'])
    value['expected_candidate']['class_counts'][0]['count'] = 2
    with pytest.raises(ValueError, match='NLCD_FIXTURE_REPLAY_MISMATCH'):
        replay_packet(canonical_bytes(value))


def test_cli_uses_fixed_fixtures_and_emits_aggregates_without_writes(tmp_path, monkeypatch):
    monkeypatch.setenv('PYTHONPATH', str(ROOT / 'tools/ci/kfm_no_network') + ':' + str(ROOT))
    result = subprocess.run([sys.executable, '-B', '-m', 'pipelines.domains.habitat.ingest_nlcd', 'base'],
                            cwd=tmp_path, capture_output=True, text=True, check=True)
    summary = json.loads(result.stdout)
    assert summary['outcome'] == 'REVIEW_REQUIRED'
    assert summary['valid_pixels'] == 9
    assert summary['publication_authorized'] is False
    assert '2100000' not in result.stdout and 'source_base64' not in result.stdout
    assert not result.stderr
    assert list(tmp_path.iterdir()) == []


def test_equivalent_time_offsets_produce_the_same_normalized_candidate():
    value = packet()
    value['capture'] = {'retrieved_at': '2026-11-18T18:00:00-06:00', 'valid_time': {
        'start': '2020-12-31T18:00:00-06:00', 'end': '2021-12-31T17:59:59-06:00'}}
    assert normalize(source(), value) == normalize(source())


def test_source_and_packet_byte_limits_refuse_oversized_inputs():
    with pytest.raises(ValueError, match='NLCD_SOURCE_BYTE_LIMIT'):
        normalize(b'II*\x00' + bytes(8 * 1024 * 1024))
    with pytest.raises(ValueError, match='JSON_BYTE_LIMIT'):
        replay_packet(bytes(12 * 1024 * 1024 + 1))
