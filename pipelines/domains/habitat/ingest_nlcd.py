"""Bounded native-grid NLCD candidate preparation from supplied GeoTIFF bytes.

Reads one uint8, north-up EPSG:5070 band in memory. Preserves source classes,
nodata and mask support without resampling, class recoding or habitat inference.
The explicit class scheme is a review candidate, never an admitted legend.
CLI input is limited to committed synthetic packets; stdout is aggregate-only.
"""
from __future__ import annotations

import argparse
import base64
import binascii
import json
import math
from pathlib import Path
import sys

import numpy as np
import rasterio
from rasterio.io import MemoryFile
from jsonschema import Draft202012Validator, FormatChecker

from connectors_core.captured_json import canonical_bytes, decode_object, digest_bytes, utc_time, timestamp
from tools.local_data.file_io import read_regular

ROOT = Path(__file__).resolve().parents[3]
SCHEMAS = ROOT / 'schemas/contracts/v1/domains/habitat/land_cover'
FIXTURES = ROOT / 'fixtures/domains/habitat/nlcd_ingest'
MAX_SOURCE_BYTES = 8 * 1024 * 1024
MAX_PACKET_BYTES = 12 * 1024 * 1024
MAX_PIXELS = 1024 * 1024
FLAGS = {**{key: False for key in ('source_admitted', 'review_completed', 'policy_evaluated',
         'lifecycle_write', 'promotion_authorized', 'release_authorized', 'publication_authorized',
         'public_use_allowed')}, 'review_required': True, 'rights_status': 'UNVERIFIED',
         'sensitivity': 'NOT_EVALUATED'}


def spec_hash(value: dict) -> str:
    return digest_bytes(canonical_bytes({key: item for key, item in value.items() if key != 'spec_hash'}))


def _schema(value: dict, name: str, reason: str) -> None:
    schema = json.loads((SCHEMAS / (name + '.schema.json')).read_text())
    if not Draft202012Validator(schema, format_checker=FormatChecker()).is_valid(value):
        raise ValueError(reason)


def validate_scheme(scheme: dict) -> None:
    _schema(scheme, 'class_scheme', 'NLCD_CLASS_SCHEME_INVALID')
    codes = [item['code'] for item in scheme['classes']]
    if any(type(code) is not int for code in codes) or codes != sorted(set(codes)):
        raise ValueError('NLCD_CLASS_CODES_NOT_CANONICAL')
    if scheme['spec_hash'] != spec_hash(scheme):
        raise ValueError('NLCD_CLASS_SCHEME_DIGEST_MISMATCH')


def _capture_times(capture: dict) -> dict:
    if (not isinstance(capture, dict) or set(capture) != {'retrieved_at', 'valid_time'}
            or not isinstance(capture['valid_time'], dict)
            or set(capture['valid_time']) != {'start', 'end'}):
        raise ValueError('NLCD_CAPTURE_METADATA_INVALID')
    start, end = [utc_time(capture['valid_time'][key]) for key in ('start', 'end')]
    retrieved = utc_time(capture['retrieved_at'])
    if not start <= end <= retrieved:
        raise ValueError('NLCD_CAPTURE_TIME_ORDER_INVALID')
    return {'retrieved_at': timestamp(retrieved), 'valid_time': {'start': timestamp(start), 'end': timestamp(end)}}


def _raster(source: bytes, scheme: dict) -> tuple[dict, dict, list, str]:
    if not isinstance(source, bytes) or not 0 < len(source) <= MAX_SOURCE_BYTES:
        raise ValueError('NLCD_SOURCE_BYTE_LIMIT')
    if source[:4] not in (b'II*\x00', b'MM\x00*'):
        raise ValueError('NLCD_CLASSIC_GEOTIFF_REQUIRED')
    try:
        with rasterio.Env(GDAL_PAM_ENABLED='NO', GDAL_DISABLE_READDIR_ON_OPEN='EMPTY_DIR', PROJ_NETWORK='OFF', GDAL_CACHEMAX=16 * 1024 * 1024):
            with MemoryFile(source) as memory, memory.open(driver='GTiff') as dataset:
                transform = dataset.transform
                if (dataset.driver != 'GTiff' or dataset.subdatasets or dataset.count != 1
                        or dataset.dtypes != ('uint8',) or dataset.nodata != 0
                        or dataset.crs != rasterio.crs.CRS.from_epsg(5070)
                        or not 1 <= dataset.width <= 2048 or not 1 <= dataset.height <= 2048
                        or dataset.width * dataset.height > MAX_PIXELS
                        or any(rows <= 0 or columns <= 0 or rows * columns > MAX_PIXELS
                               for rows, columns in dataset.block_shapes)
                        or not all(math.isfinite(value) for value in (*tuple(transform)[:6], *dataset.bounds))
                        or transform.a <= 0 or transform.e >= 0 or transform.b != 0 or transform.d != 0):
                    raise ValueError('NLCD_NATIVE_GRID_INVALID')
                cells, mask = dataset.read(1), dataset.read_masks(1)
                spatial = {'crs': 'EPSG:5070', 'width': dataset.width, 'height': dataset.height,
                           'transform': list(tuple(transform)[:6]), 'bounds': list(dataset.bounds),
                           'dtype': 'uint8', 'bands': 1}
    except rasterio.errors.RasterioError:
        raise ValueError('NLCD_GEOTIFF_INVALID') from None
    codes = {item['code'] for item in scheme['classes']}
    if not set(int(value) for value in np.unique(cells)) <= codes | {0}:
        raise ValueError('NLCD_CLASS_NOT_IN_SCHEME')
    valid = (mask != 0) & (cells != 0)
    count = int(np.count_nonzero(valid))
    if not count:
        raise ValueError('NLCD_NO_VALID_PIXELS')
    support = {'pixel_count': int(cells.size), 'valid_count': count,
               'nodata_count': int(cells.size) - count,
               'valid_mask_sha256': digest_bytes(valid.astype('uint8').tobytes(order='C'))}
    histogram = np.bincount(cells[valid], minlength=256)
    counts = [{**item, 'count': int(histogram[item['code']])} for item in scheme['classes']]
    normalized = digest_bytes(canonical_bytes(spatial) + b'\x00' + cells.tobytes(order='C')
                              + b'\x00' + valid.astype('uint8').tobytes(order='C'))
    return spatial, support, counts, normalized


def observation_id(candidate: dict) -> str:
    identity = [candidate['source_id'], candidate['scheme_hash'], candidate['spatial'],
                candidate['valid_time'], candidate['normalized_grid_sha256']]
    return 'kfm:land-cover-observation:' + digest_bytes(canonical_bytes(identity))[7:31]


def normalize_capture(source: bytes, scheme: dict, capture: dict) -> dict:
    validate_scheme(scheme)
    capture = _capture_times(capture)
    spatial, support, counts, normalized = _raster(source, scheme)
    result = {'object_type': 'LandCoverObservation', 'schema_version': '1.0.0',
              'profile_version': 'kfm.nlcd-observation-candidate/v1', 'source_id': 'nlcd',
              'source_descriptor_ref': scheme['source_descriptor_ref'], 'source_role': 'OBSERVATION_CANDIDATE',
              'source_product': scheme['source_product'], 'source_vintage': scheme['source_vintage'],
              'scheme_id': scheme['scheme_id'], 'scheme_version': scheme['scheme_version'],
              'scheme_hash': scheme['spec_hash'], 'retrieved_at': capture['retrieved_at'],
              'valid_time': dict(capture['valid_time']), 'spatial': spatial, 'support': support,
              'class_counts': counts, 'source_artifact_sha256': digest_bytes(source),
              'normalized_grid_sha256': normalized,
              'uncertainty': {'classification_accuracy': 'NOT_EVALUATED', 'source_coverage': 'NOT_ESTABLISHED',
                              'vintage_gap': 'NOT_EVALUATED'},
              'processing': {'resampling': 'NONE', 'class_recode': False, 'habitat_assertion': False,
                             'public_generalization': False},
              'evidence_bundle_ref': None, 'release_ref': None, 'governance': dict(FLAGS)}
    result['observation_id'] = observation_id(result)
    result['spec_hash'] = spec_hash(result)
    validate_candidate(result, scheme)
    return result


def validate_candidate(candidate: dict, scheme: dict) -> dict:
    """Check candidate shape, identity and internal support; does not authenticate a provider."""
    validate_scheme(scheme)
    _schema(candidate, 'observation', 'NLCD_OBSERVATION_SCHEMA_INVALID')
    if candidate['spec_hash'] != spec_hash(candidate) or candidate['observation_id'] != observation_id(candidate):
        raise ValueError('NLCD_OBSERVATION_DIGEST_OR_IDENTITY_MISMATCH')
    for name in ('source_product', 'source_vintage', 'scheme_id', 'scheme_version'):
        if candidate[name] != scheme[name]:
            raise ValueError('NLCD_SCHEME_BINDING_MISMATCH')
    if candidate['scheme_hash'] != scheme['spec_hash']:
        raise ValueError('NLCD_SCHEME_BINDING_MISMATCH')
    capture = {key: candidate[key] for key in ('retrieved_at', 'valid_time')}
    if capture != _capture_times(capture):
        raise ValueError('NLCD_CAPTURE_TIME_NOT_CANONICAL')
    support, spatial = candidate['support'], candidate['spatial']
    expected_classes = [{key: item[key] for key in ('code', 'label')} for item in candidate['class_counts']]
    if (expected_classes != scheme['classes'] or sum(item['count'] for item in candidate['class_counts']) != support['valid_count']
            or support['pixel_count'] != spatial['width'] * spatial['height']
            or support['valid_count'] + support['nodata_count'] != support['pixel_count']):
        raise ValueError('NLCD_PIXEL_SUPPORT_MISMATCH')
    a, b, c, d, e, f = spatial['transform']
    if (not all(math.isfinite(value) for value in (*spatial['transform'], *spatial['bounds']))
            or a <= 0 or e >= 0 or b != 0 or d != 0
            or spatial['bounds'] != [c, f + e * spatial['height'], c + a * spatial['width'], f]):
        raise ValueError('NLCD_GRID_BINDING_MISMATCH')
    return {'outcome': 'PASS', 'observation_id': candidate['observation_id'],
            'review_required': True, 'source_admitted': False, 'release_authorized': False,
            'publication_authorized': False}


def replay_packet(raw: bytes) -> dict:
    packet = decode_object(raw, limit=MAX_PACKET_BYTES)
    if (set(packet) != {'fixture_only', 'class_scheme', 'capture', 'source_base64', 'source_sha256', 'expected_candidate'}
            or packet['fixture_only'] is not True or not isinstance(packet['source_base64'], str)):
        raise ValueError('NLCD_FIXTURE_PACKET_INVALID')
    try:
        source = base64.b64decode(packet['source_base64'], validate=True)
    except (ValueError, binascii.Error):
        raise ValueError('NLCD_FIXTURE_BASE64_INVALID') from None
    if digest_bytes(source) != packet['source_sha256']:
        raise ValueError('NLCD_SOURCE_DIGEST_MISMATCH')
    candidate = normalize_capture(source, packet['class_scheme'], packet['capture'])
    if candidate != packet['expected_candidate']:
        raise ValueError('NLCD_FIXTURE_REPLAY_MISMATCH')
    return {'fixture_only': True, 'candidate': candidate, 'validation': validate_candidate(candidate, packet['class_scheme'])}


def replay_fixture(name: str) -> dict:
    if name not in ('base', 'changed'):
        raise ValueError('NLCD_FIXTURE_UNKNOWN')
    return replay_packet(read_regular(FIXTURES / (name + '.json'), MAX_PACKET_BYTES))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('fixture', choices=('base', 'changed'))
    args = parser.parse_args(argv)
    try:
        candidate = replay_fixture(args.fixture)['candidate']
    except (ValueError, OSError):
        print('{"outcome":"ERROR","reason":"NLCD_FIXTURE_REPLAY_FAILED"}', file=sys.stderr)
        return 1
    print(canonical_bytes({'outcome': 'REVIEW_REQUIRED', 'observation_id': candidate['observation_id'],
                           'valid_pixels': candidate['support']['valid_count'],
                           'nodata_pixels': candidate['support']['nodata_count'],
                           'release_authorized': False, 'publication_authorized': False}).decode())
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
