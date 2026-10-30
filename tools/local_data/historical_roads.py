"""Prepare the qualified 1918 Kansas road-map document for private review offline."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

from tools.local_data.file_io import read_regular, write_new
from tools.local_data.manage import external_root, initialized, store_lock
from tools.local_data.review_images import image_metadata

PROFILE = 'kfm-historical-roads-review/v1'
SOURCE = Path('data/raw/Kansas Road Maps/1918 Kansas.pdf')
PACKAGE = Path('data/work/roads_rail_trade/map-document-library-review-20261012')
RECORD_ID = '841703d8b7d03c5807b30fc2b07229af8ffdae2e3296d19b69da57adab1c4858'
RECORD = Path('records') / (RECORD_ID + '.json')
AUTHORITY = {'admission': False, 'activation': False, 'release': False, 'publication': False}
LIMIT = 16 * 1024**2
RECIPE = {'tool': 'pdftoppm', 'page': 1, 'singleFile': True, 'scaleTo': 3600, 'format': 'png'}


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False) + '\n').encode()


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def pinned(path, expected, limit):
    if not isinstance(expected, str) or not re.fullmatch('[a-f0-9]{64}', expected):
        raise ValueError('ROADS_DIGEST_INVALID')
    raw = read_regular(path, limit)
    if digest(raw) != expected:
        raise ValueError('ROADS_PIN_CHANGED')
    return raw


def render_pdf(raw: bytes):
    """Render a private verified copy, one bounded page, with an installed Poppler."""
    executable = shutil.which('pdftoppm')
    if executable is None:
        raise ValueError('ROADS_RENDERER_UNAVAILABLE')
    version = subprocess.run([executable, '-v'], capture_output=True, timeout=5, check=True)
    match = re.search(rb'pdftoppm version ([0-9.]+)', version.stdout + version.stderr)
    if match is None:
        raise ValueError('ROADS_RENDERER_VERSION_UNKNOWN')
    with tempfile.TemporaryDirectory(prefix='kfm-road-review-') as temporary:
        directory = Path(temporary)
        write_new(directory / 'source.pdf', raw)
        subprocess.run([executable, '-f', '1', '-singlefile', '-scale-to', '3600', '-png',
                        str(directory / 'source.pdf'), str(directory / 'page-1')],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=45, check=True)
        image = read_regular(directory / 'page-1.png', LIMIT)
    return image, dict(RECIPE, version=match[1].decode())


def prepare(source_root: Path, qualification_path: Path, qualification_sha256: str):
    qualification_raw = pinned(qualification_path, qualification_sha256, 128 * 1024)
    q = json.loads(qualification_raw)
    if (q.get('schema') != 'kfm-historical-reference-qualification/v1'
            or q.get('state') != 'QUALIFIED_FOR_PRIVATE_DOCUMENT_PREPARATION'
            or q.get('titleOnSheet') != 'Official Map, Kansas State Roads'
            or q.get('issuingBodyOnSheet') != 'Kansas Highway Commission'
            or q.get('printedApprovalDate') != '1918-08-07'
            or q.get('printedDateText') != 'Approved August 7, 1918'
            or q.get('authority') != AUTHORITY or q.get('georeferencingVerified') is not False
            or q.get('geometry') is not None or q.get('sourceObservationInterval') is not None
            or q.get('featureConstructionDates') is not None
            or q.get('rights') != 'SOURCE_SPECIFIC_REVIEW_REQUIRED'
            or q.get('sensitivity') != 'INFRASTRUCTURE_CONTEXT_REVIEW_REQUIRED'
            or q.get('providerChecksumVerified') is not False or q.get('originalAcquisitionUrl') is not None):
        raise ValueError('ROADS_QUALIFICATION_INVALID')
    # Absolute paths retained in old evidence are never used to locate source files.
    manifest_raw = pinned(source_root / PACKAGE / 'review-manifest.json', q['sourceReviewManifest']['sha256'], 256 * 1024)
    manifest = json.loads(manifest_raw)
    if (manifest.get('profile') != 'kfm-map-document-review/v1' or manifest.get('review_state') != 'PENDING'
            or manifest.get('published') is not False or manifest.get('released') is not False
            or manifest.get('rights') != q['rights'] or manifest.get('sensitivity') != q['sensitivity']):
        raise ValueError('ROADS_ARCHIVE_REVIEW_STATE_INVALID')
    records = [r for r in manifest.get('outputs', []) if r.get('file') == str(RECORD)]
    if len(records) != 1 or records[0]['sha256'] != q['sourceRecord']['sha256']:
        raise ValueError('ROADS_RECORD_NOT_BOUND')
    record_raw = pinned(source_root / PACKAGE / RECORD, records[0]['sha256'], 128 * 1024)
    record = json.loads(record_raw)
    if (len(record_raw) != records[0]['bytes'] or record.get('id') != 'kfm:map-document:' + RECORD_ID
            or record.get('collection') != 'Kansas Road Maps' or record.get('edition_start_year') != 1918
            or record.get('edition_end_year') != 1918 or record.get('filename_conflict') is not False
            or record.get('published') is not False or record.get('released') is not False
            or record.get('review_state') != 'PENDING' or record.get('rights') != q['rights']
            or record.get('sensitivity') != q['sensitivity'] or record.get('sha256') != q['source']['sha256']):
        raise ValueError('ROADS_SOURCE_RECORD_INVALID')
    pdf = pinned(source_root / SOURCE, record['sha256'], LIMIT)
    if (not pdf.startswith(b'%PDF-') or len(pdf) != record.get('bytes') or len(pdf) != q['source']['bytes']):
        raise ValueError('ROADS_SOURCE_PDF_INVALID')
    image, recipe = render_pdf(pdf)
    metadata = image_metadata(image, '.png')
    expected_recipe = dict(recipe, dimensions=[metadata['width'], metadata['height']])
    if (expected_recipe != q.get('renderRecipe') or digest(image) != q['render']['sha256']
            or len(image) != q['render']['bytes']):
        raise ValueError('ROADS_RENDER_REPLAY_MISMATCH')
    inputs = {'qualification_sha256': qualification_sha256,
              'source_manifest_path': str(PACKAGE / 'review-manifest.json'), 'source_manifest_sha256': digest(manifest_raw),
              'source_record_path': str(PACKAGE / RECORD), 'source_record_sha256': digest(record_raw),
              'source_pdf_path': str(SOURCE), 'source_pdf_sha256': digest(pdf), 'source_pdf_bytes': len(pdf),
              'render_sha256': digest(image), 'render_recipe': expected_recipe,
              'generator_sha256': digest(Path(__file__).read_bytes()),
              'image_reader_sha256': digest(Path(image_metadata.__code__.co_filename).read_bytes())}
    coverage = {'profile': PROFILE, 'title': q['titleOnSheet'], 'issuing_body_on_sheet': q['issuingBodyOnSheet'],
                'topics': ['roads-rail-trade', 'history'], 'use': 'HISTORICAL_DOCUMENT_CONTEXT',
                'printed_map_approval_date': '1918-08-07', 'date_basis': 'Visually checked printed sheet date; retained qualification',
                'source_observation_interval': None, 'feature_construction_dates': None,
                'geometry': None, 'georeferencing_verified': False, 'image': metadata,
                'rights': q['rights'], 'sensitivity': q['sensitivity'], 'original_acquisition_url': None,
                'provider_checksum_verified': False, 'authority': AUTHORITY, 'inputs': inputs,
                'limitations': ['The map approval date does not date individual road construction, opening or surveys.',
                                'PDF producer timestamps do not establish the historical map date or acquisition date.',
                                'Page pixels and OCR search clues are not verified road geometry or transcription.',
                                'Source-specific redistribution rights and infrastructure context remain under review.']}
    return pdf, image, record_raw, manifest_raw, qualification_raw, coverage


def derive(source_root: Path, root: Path, qualification_path: Path, qualification_sha256: str):
    source_root, root = external_root(str(source_root)), external_root(str(root))
    if source_root == root or source_root in root.parents or root in source_root.parents:
        raise ValueError('ROADS_SEPARATE_DESTINATION_REQUIRED')
    if not initialized(root):
        raise ValueError('STORE_NOT_INITIALIZED_RUN_INIT')
    pdf, image, record, manifest, qualification, coverage = prepare(source_root, qualification_path, qualification_sha256)
    inputs = coverage['inputs']
    location = Path('data/work/roads_rail_trade/historical-1918') / digest(canonical(inputs))
    retained = {'file': 'retained/source-map.pdf', 'bytes': len(pdf), 'sha256': digest(pdf),
                'role': 'Original bytes retained for replay and backup; not a browser preview member.'}
    outputs = {'page-1.png': image, 'source-record.json': record, 'source-review-manifest.json': manifest,
               'qualification.json': qualification, 'coverage.json': canonical(coverage),
               'source-retention.json': canonical({'retained_sources': [retained], 'authority': AUTHORITY}),
               'validation.json': canonical({'state': 'PINNED_SOURCE_AND_RENDER_REPLAY_MATCH', 'image': coverage['image'],
                                              'inputs': inputs, 'authority': AUTHORITY}),
               'README.md': (
                   '# Historical Kansas road-map reference\n\nOfficial Map, Kansas State Roads, Kansas Highway Commission. '
                   'The printed sheet says Approved August 7, 1918. This is the map approval date, not a construction or survey date.\n\n'
                   'Open page-1.png for the complete rendered sheet. A fresh offline rendering of the pinned archived PDF '
                   'matches the previously inspected image byte for byte. The original PDF is retained privately in '
                   'retained/source-map.pdf for replay and backup; it is not served by this review desk.\n\n'
                   'Source-record.json retains the original noisy OCR search clues. Qualification.json records the visual check; '
                   'coverage.json separates the historical date from PDF producer metadata and states the limits. '
                   'No road vectors, construction dates or verified geographic coordinates have been derived.\n\n'
                   'Private reference only. Original acquisition URL, provider checksum and redistribution permission remain unverified. '
                   'Source-specific rights and infrastructure-context review holds remain. Admission, activation, release and publication are pending.\n'
               ).encode()}
    rows = [{'file': name, 'bytes': len(raw), 'sha256': digest(raw)} for name, raw in sorted(outputs.items())]
    outputs['review-manifest.json'] = canonical({'profile': PROFILE, 'review_state': 'PENDING', 'released': False,
        'published': False, 'source_admitted': False, 'output_bytes': sum(r['bytes'] for r in rows), 'outputs': rows,
        'retained_sources': [retained], 'inputs': inputs,
        'source_role': 'Kansas State Roads document; printed map approval August 7, 1918. No road geometry or feature dates inferred.',
        'rights': 'Source-specific rights and infrastructure-context review required; private reference only.'})
    with store_lock(root):
        target = root / location
        if target.exists() and {p.name for p in target.iterdir()} - {*outputs, 'retained'}:
            raise ValueError('ROADS_OUTPUT_CLOSURE_CHANGED')
        retained_dir = target / 'retained'
        if retained_dir.exists() and {p.name for p in retained_dir.iterdir()} - {'source-map.pdf'}:
            raise ValueError('ROADS_OUTPUT_CLOSURE_CHANGED')
        # Write the manifest last; a partially written directory is not bound for review.
        for name, raw in {'retained/source-map.pdf': pdf, **outputs}.items():
            try:
                write_new(target / name, raw)
            except FileExistsError:
                if read_regular(target / name, max(1, len(raw))) != raw:
                    raise ValueError('ROADS_OUTPUT_CHANGED') from None
    return {'profile': PROFILE, 'state': 'PREPARED_FOR_PRIVATE_REVIEW', 'printed_map_approval_date': '1918-08-07',
            'binding': str(location / 'review-manifest.json') + '@' + digest(outputs['review-manifest.json']),
            'image': coverage['image'], 'inputs': inputs, 'retained_sources': [retained], 'authority': AUTHORITY}


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    for name in ('source-root', 'root', 'qualification-path', 'qualification-sha256'):
        cli.add_argument('--' + name, required=True)
    args = vars(cli.parse_args())
    for name in ('source_root', 'root', 'qualification_path'):
        args[name] = Path(args[name])
    print(json.dumps(derive(**args)))


if __name__ == '__main__':
    main()
