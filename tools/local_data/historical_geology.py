"""Prepare the archived KGS M-118 (2008) document for private reference, offline."""
from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re

from tools.local_data.file_io import read_regular, write_new
from tools.local_data.manage import external_root, initialized, store_lock
from tools.local_data.review_images import image_metadata

PROFILE = 'kfm-historical-geology-review/v1'
RECORD = 'kgs-m118-2008'
ASSET = 'kgs-m118-jpeg'
NAME = 'M118_StatewideGeology_2008_72dpi.jpg'
URL = 'https://www.kgs.ku.edu/General/Geology/gifs/' + NAME
AUTHORITY = {'admission': False, 'activation': False, 'release': False, 'publication': False}


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False) + '\n').encode()


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def pinned(path, expected, limit):
    if not isinstance(expected, str) or not re.fullmatch('[a-f0-9]{64}', expected):
        raise ValueError('GEOLOGY_DIGEST_INVALID')
    raw = read_regular(path, limit)
    if digest(raw) != expected:
        raise ValueError('GEOLOGY_PIN_CHANGED')
    return raw


def prepare(source_root: Path, job_id: str, receipt_sha256: str, source_sha256: str):
    if not isinstance(job_id, str) or not re.fullmatch('[a-f0-9]{32}', job_id):
        raise ValueError('GEOLOGY_JOB_INVALID')
    receipt_path = Path('data/receipts/ingest/public-maps') / (job_id + '.json')
    receipt_raw = pinned(source_root / receipt_path, receipt_sha256, 128 * 1024)
    receipt = json.loads(receipt_raw)
    job = receipt.get('job', {})
    files = receipt.get('files', [])
    if (receipt.get('schema') != 'kfm-public-map-download-receipt/v1' or receipt.get('admission') != 'NOT_ADMITTED'
            or receipt.get('release') != 'NOT_RELEASED' or receipt.get('review') != 'UNREVIEWED'
            or job.get('id') != job_id or job.get('assetId') != ASSET or job.get('state') != 'downloaded'
            or job.get('mapReady') is not False or not isinstance(files, list) or len(files) != 1):
        raise ValueError('GEOLOGY_RECEIPT_INVALID')
    file = files[0]
    if (file.get('name') != NAME or file.get('complete') is not True or type(file.get('bytes')) is not int
            or not 0 < file['bytes'] <= 16 * 1024**2 or job.get('bytes') != file['bytes']
            or job.get('expectedBytes') != file['bytes'] or job.get('sha256') != file.get('sha256')):
        raise ValueError('GEOLOGY_CAPTURE_INCOMPLETE')
    captured = job.get('updatedAt')
    if not isinstance(captured, str) or datetime.fromisoformat(captured.replace('Z', '+00:00')).tzinfo is None:
        raise ValueError('GEOLOGY_CAPTURE_TIME_INVALID')
    # Old absolute destination paths in receipts are provenance only.
    directory = Path('data/raw/public-maps') / RECORD / job_id
    source_raw = pinned(source_root / directory / 'source.json', source_sha256, 128 * 1024)
    source = json.loads(source_raw)
    record, asset = source.get('record', {}), source.get('asset', {})
    if (record.get('id') != RECORD or record.get('publisher') != 'KGS' or record.get('mapYear') != 2008
            or record.get('scale') != '1:500,000' or record.get('rights', {}).get('status') != 'held'
            or asset.get('id') != ASSET or asset.get('format') != 'JPEG' or asset.get('url') != URL
            or asset.get('expectedBytes') != file['bytes']):
        raise ValueError('GEOLOGY_SOURCE_IDENTITY_INVALID')
    raw = pinned(source_root / directory / NAME, file['sha256'], 16 * 1024**2)
    if len(raw) != file['bytes']:
        raise ValueError('GEOLOGY_CAPTURE_SIZE_INVALID')
    image = image_metadata(raw, '.jpg')
    inputs = {'receipt_path': str(receipt_path), 'receipt_sha256': receipt_sha256,
              'source_path': str(directory / 'source.json'), 'source_sha256': source_sha256,
              'image_path': str(directory / NAME), 'image_sha256': file['sha256'], 'image_bytes': len(raw),
              'generator_sha256': digest(Path(__file__).read_bytes()),
              'image_reader_sha256': digest(Path(image_metadata.__code__.co_filename).read_bytes())}
    coverage = {'profile': PROFILE, 'use': 'HISTORICAL_DOCUMENT_CONTEXT', 'topics': ['geology', 'science'],
                'title': record['title'], 'publisher': 'Kansas Geological Survey', 'map_id': 'M-118',
                'map_edition_year': 2008, 'capture_completed_at': captured, 'scale_denominator': 500000,
                'coverage_label': 'Kansas statewide, as depicted by the publisher', 'image': image,
                'source_url': URL, 'metadata_url': record.get('metadataUrl'), 'rights': record['rights'],
                'provider_checksum_verified': receipt.get('providerChecksumVerified') is True,
                'source_observation_interval': None, 'geometry': None, 'georeferencing_verified': False,
                'authority': AUTHORITY, 'inputs': inputs,
                'limitations': ['Published interpretive map document; edition year is not an observation interval.',
                                'Pixel positions are not verified geographic coordinates. No polygons, units or numeric geology measurements extracted.',
                                'Stored-byte integrity and bounded image headers are checked; scientific accuracy and redistribution remain under review.']}
    return raw, source_raw, receipt_raw, coverage


def derive(source_root: Path, root: Path, job_id: str, receipt_sha256: str, source_sha256: str):
    source_root, root = external_root(str(source_root)), external_root(str(root))
    if source_root == root or source_root in root.parents or root in source_root.parents:
        raise ValueError('GEOLOGY_SEPARATE_DESTINATION_REQUIRED')
    if not initialized(root):
        raise ValueError('STORE_NOT_INITIALIZED_RUN_INIT')
    raw, source, receipt, coverage = prepare(source_root, job_id, receipt_sha256, source_sha256)
    inputs = coverage['inputs']
    location = Path('data/work/geology/historical-m118') / digest(canonical(inputs))
    outputs = {'source-map.jpg': raw, 'source-record.json': source, 'capture-receipt.json': receipt,
               'coverage.json': canonical(coverage),
               'validation.json': canonical({'state': 'PINNED_CAPTURE_BYTES_MATCH', 'image_header': coverage['image'],
                                              'inputs': inputs, 'authority': AUTHORITY}),
               'README.md': (f"# Historical Kansas geology reference\n\nSurficial Geology of Kansas, KGS Map M-118, 2008 edition, scale 1:500,000. "
                             f"Capture completed {coverage['capture_completed_at']}.\n\nOpen source-map.jpg to inspect the original publisher JPEG. "
                             "Its bytes match the pinned completed capture receipt. No image transformation was applied. "
                             "Source-record.json and capture-receipt.json preserve the acquisition evidence; coverage.json explains dates, scale and limits.\n\n"
                             "This is a statewide interpretive document. The edition year is not an observation interval, and map pixels are not verified geographic coordinates. "
                             "No vector layer or numeric geology measurements have been extracted.\n\nPrivate reference only. Source rights remain held; "
                             "admission, activation, release and publication remain pending. Stored-byte integrity does not establish scientific accuracy or provider-checksum verification.\n").encode()}
    records = [{'file': name, 'bytes': len(body), 'sha256': digest(body)} for name, body in sorted(outputs.items())]
    outputs['review-manifest.json'] = canonical({'profile': PROFILE, 'review_state': 'PENDING', 'released': False,
        'published': False, 'source_admitted': False, 'output_bytes': sum(r['bytes'] for r in records), 'outputs': records,
        'source_role': 'KGS M-118, 2008 edition, scale 1:500,000. Statewide interpretive geology document.',
        'rights': 'Retained KGS rights hold; private reference only.', 'inputs': inputs})
    with store_lock(root):
        target = root / location
        if target.exists() and {p.name for p in target.iterdir()} - set(outputs):
            raise ValueError('GEOLOGY_OUTPUT_CLOSURE_CHANGED')
        for name, body in outputs.items():
            try:
                write_new(target / name, body)
            except FileExistsError:
                if read_regular(target / name, max(1, len(body))) != body:
                    raise ValueError('GEOLOGY_OUTPUT_CHANGED') from None
    return {'profile': PROFILE, 'state': 'PREPARED_FOR_PRIVATE_REVIEW', 'map_edition_year': 2008,
            'binding': str(location / 'review-manifest.json') + '@' + digest(outputs['review-manifest.json']),
            'image': coverage['image'], 'inputs': inputs, 'authority': AUTHORITY}


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    for name in ('source-root', 'root', 'job-id', 'receipt-sha256', 'source-sha256'):
        cli.add_argument('--' + name, required=True)
    args = vars(cli.parse_args()); args['source_root'], args['root'] = Path(args['source_root']), Path(args['root'])
    print(json.dumps(derive(**args)))


if __name__ == '__main__':
    main()
