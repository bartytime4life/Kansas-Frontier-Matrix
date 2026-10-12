"""Private full-history review derivative from one verified, fixed-station capture.

Reuses the pinned canonical parser/flag policy. Does not grant admission or
release, replace the bounded pilot candidate, or infer historical locations.
"""
import argparse
import csv
from collections import Counter
from datetime import date, datetime, timezone
import hashlib
import json
import os
import shutil
from pathlib import Path
import sys
import zipfile

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO))
from tools.local_data.ghcnd_daily_pilot import load_capture
from tools.local_data.file_io import check_directory, hash_regular, open_regular, read_regular, write_new
from tools.local_data.manage import external_root, store_lock
from tools.local_data.acquisition import validate_root
from pipelines.domains.atmosphere import ghcnd_daily_normalize as normalizer
from connectors.noaa.src.noaa.ghcnd_daily_capture import STATIONS, ELEMENTS, STATION_LIST_KEY

LIMIT = 512 * 1024**2
VERSION = 'kfm-ghcnd-archive-review/v1'
OUTPUT_NAMES = ('observations.csv', 'station-year-coverage.csv', 'stations-current-provider-metadata.json')
MANIFEST_NAME = 'review-manifest.json'
PACKAGE_NAME = 'review-package.zip'

def canon(v):
    return json.dumps(v, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()


def verify_existing(target, receipt_path, inputs, limit, *, receipt=None):
    """Rehash exact members and check retained holds before reporting a replay."""
    check_directory(target)
    if receipt is None:
        receipt = json.loads(read_regular(receipt_path, 64 * 1024))
    saved_manifest = read_regular(target / MANIFEST_NAME, 64 * 1024)
    saved = json.loads(saved_manifest)
    expected_id = 'sha256:' + hashlib.sha256(canon(inputs)).hexdigest()
    if (not isinstance(receipt, dict) or not isinstance(saved, dict)
            or receipt.get('profile') != VERSION or saved.get('profile') != VERSION
            or receipt.get('state') != 'private-review-package-verified'
            or saved.get('review_id') != expected_id or saved.get('inputs') != inputs
            or saved.get('review_state') != 'PENDING' or receipt.get('review_state') != 'PENDING'
            or any(saved.get(key) is not False for key in ('source_admitted', 'released', 'published'))
            or any(receipt.get(key) is not False for key in ('admitted', 'released', 'published'))
            or hashlib.sha256(saved_manifest).hexdigest() != receipt.get('manifest_sha256')
            or saved.get('outputs') != receipt.get('outputs')
            or saved.get('counts') != receipt.get('counts')):
        raise ValueError('REVIEW_EXISTING_INTEGRITY_FAILED')
    outputs = receipt.get('outputs')
    if (not isinstance(outputs, list) or len(outputs) != len(OUTPUT_NAMES)
            or [item.get('file') for item in outputs if isinstance(item, dict)] != list(OUTPUT_NAMES)
            or {p.name for p in target.iterdir()} != set(OUTPUT_NAMES) | {MANIFEST_NAME, PACKAGE_NAME}):
        raise ValueError('REVIEW_EXISTING_INTEGRITY_FAILED')
    expected = {MANIFEST_NAME: (hashlib.sha256(saved_manifest).hexdigest(), len(saved_manifest))}
    for item in outputs:
        if (not isinstance(item.get('bytes'), int) or isinstance(item['bytes'], bool)
                or not 0 < item['bytes'] <= limit):
            raise ValueError('REVIEW_EXISTING_INTEGRITY_FAILED')
        digest, size = hash_regular(target / item['file'], limit, expected_size=item['bytes'])
        if digest != item.get('sha256'):
            raise ValueError('REVIEW_EXISTING_INTEGRITY_FAILED')
        expected[item['file']] = (digest, size)
    package = receipt.get('package')
    if (not isinstance(package, dict) or package.get('file') != str(target / PACKAGE_NAME)
            or not isinstance(package.get('bytes'), int) or isinstance(package['bytes'], bool)
            or not 0 < package['bytes'] <= limit):
        raise ValueError('REVIEW_EXISTING_INTEGRITY_FAILED')
    digest, _ = hash_regular(target / PACKAGE_NAME, limit, expected_size=package['bytes'])
    if digest != package.get('sha256'):
        raise ValueError('REVIEW_EXISTING_INTEGRITY_FAILED')
    # The ZIP is an output carrier; verify its exact members without extracting.
    with os.fdopen(open_regular(target / PACKAGE_NAME), 'rb') as handle, zipfile.ZipFile(handle) as archive:
        members = archive.infolist()
        if len(members) != len(expected) or {item.filename for item in members} != set(expected):
            raise ValueError('REVIEW_ZIP_CLOSURE_FAILED')
        for item in members:
            sha, size = expected[item.filename]
            if item.file_size != size or item.flag_bits & 1:
                raise ValueError('REVIEW_ZIP_CLOSURE_FAILED')
            hashed, count = hashlib.sha256(), 0
            with archive.open(item) as stream:
                while chunk := stream.read(min(1024**2, size - count + 1)):
                    count += len(chunk)
                    if count > size:
                        raise ValueError('REVIEW_ZIP_CLOSURE_FAILED')
                    hashed.update(chunk)
            if count != size or hashed.hexdigest() != sha:
                raise ValueError('REVIEW_ZIP_CLOSURE_FAILED')
    return {'outcome': 'ALREADY_VERIFIED', 'destination': str(target), **receipt}


def derive(root: Path, capture_id: str, *, max_output_bytes: int = LIMIT):
    """Create one immutable review package in WORK; existing completed output replays."""
    if (not isinstance(max_output_bytes, int) or isinstance(max_output_bytes, bool)
            or not 1 <= max_output_bytes <= LIMIT):
        raise ValueError('REVIEW_OUTPUT_LIMIT_INVALID')
    root = external_root(str(root))
    validate_root(root)
    with store_lock(root):
        return _derive(root, capture_id, max_output_bytes)


def _derive(root, capture_id, max_output_bytes):
    acquired = load_capture(root, capture_id)
    pilot = normalizer.normalize_capture(acquired.manifest, acquired.objects)
    pages = {p['key']: p for p in acquired.manifest['pages']}
    inputs = {'profile': VERSION, 'capture_id': capture_id, 'max_output_bytes': max_output_bytes,
              'generator_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'normalizer_sha256': hashlib.sha256(Path(normalizer.__file__).read_bytes()).hexdigest(),
              'station_ids': list(STATIONS), 'elements': list(ELEMENTS)}
    identity = hashlib.sha256(canon(inputs)).hexdigest()
    target = root / 'data/work/atmosphere/noaa-ghcnd-archive-review' / identity
    check_directory(target.parent, create=True)
    if target.exists() or target.is_symlink():
        receipt_path = root / 'data/receipts/curation/noaa-ghcnd-archive-review' / identity / 'verified.json'
        return verify_existing(target, receipt_path, inputs, max_output_bytes)
    if shutil.disk_usage(root).free < 2 * max_output_bytes + 1024**3:
        raise ValueError('INSUFFICIENT_REVIEW_SPACE')
    target.mkdir(mode=0o700)
    receipt_root = root / 'data/receipts/curation/noaa-ghcnd-archive-review' / identity
    write_new(receipt_root / 'started.json', canon({'profile': VERSION, 'state': 'started', 'inputs': inputs,
              'started_at': datetime.now(timezone.utc).isoformat(), 'admitted': False, 'released': False}))
    columns = ['id', 'station_id', 'observation_date', 'element', 'raw_value', 'value', 'unit',
               'measurement_flag', 'quality_flag', 'source_flag', 'observation_time', 'trace',
               'withheld', 'page_digest', 'retrieved_at', 'preliminary', 'source_role', 'evidence_ref', 'record_digest']
    coverage, counts, stations = {}, Counter(), []
    output = target / 'observations.csv'
    try:
        with output.open('x', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=columns, lineterminator='\n')
            writer.writeheader()
            for sid in STATIONS:
                page = pages[f'by_station/{sid}.csv.gz']
                seen = set()
                station_page = pages[STATION_LIST_KEY]
                stations.append(normalizer._station(acquired.objects[station_page['sha256']], sid, station_page))
                for day, element, value, mf, qf, sf, obs in normalizer._rows(acquired.objects[page['sha256']], sid):
                    if element not in ELEMENTS:
                        continue
                    parsed = date.fromisoformat(f'{day[:4]}-{day[4:6]}-{day[6:]}')
                    if parsed.isoformat() > acquired.manifest['captured_at'][:10]:
                        raise ValueError('FUTURE_OBSERVATION_DAY')
                    key = (day, element)
                    if key in seen:
                        raise ValueError('DUPLICATE_STATION_DAY_ELEMENT')
                    seen.add(key)
                    row = normalizer.observation(sid, element, parsed.isoformat(), value, mf, qf, sf, obs, page)
                    writer.writerow({k: row[k] for k in columns})
                    counts['observations'] += 1
                    counts[row['withheld'] or 'usable'] += 1
                    counts['trace'] += int(row['trace'])
                    if counts['observations'] > 2_000_000 or f.tell() > max_output_bytes:
                        raise ValueError('REVIEW_OUTPUT_LIMIT')
                    year_key = (sid, parsed.year, element)
                    stats = coverage.setdefault(year_key, {'observations': 0, 'usable': 0, 'MISSING': 0,
                        'QUALITY_FLAG': 0, 'trace': 0, 'first_day': parsed.isoformat(), 'last_day': parsed.isoformat()})
                    stats['observations'] += 1
                    stats[row['withheld'] or 'usable'] += 1
                    stats['trace'] += int(row['trace'])
                    stats['first_day'] = min(stats['first_day'], parsed.isoformat())
                    stats['last_day'] = max(stats['last_day'], parsed.isoformat())
            f.flush(); os.fsync(f.fileno())
        year_columns = ['station_id', 'year', 'element', 'unit', 'observations', 'usable', 'MISSING', 'QUALITY_FLAG', 'trace', 'first_day', 'last_day']
        with (target / 'station-year-coverage.csv').open('x', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=year_columns, lineterminator='\n'); writer.writeheader()
            for (sid, year, element), stats in sorted(coverage.items()):
                writer.writerow({'station_id': sid, 'year': year, 'element': element,
                                 'unit': normalizer.UNITS[element], **stats})
            f.flush(); os.fsync(f.fileno())
        write_new(target / 'stations-current-provider-metadata.json', canon({'stations': stations,
            'geometry_role': 'provider station catalog at capture; historical location stability unverified',
            'crs': 'WGS84 longitude/latitude', 'admission': False, 'released': False}))
        outputs = []
        for name in OUTPUT_NAMES:
            path = target / name; path.chmod(0o600)
            digest, size = hash_regular(path, max_output_bytes)
            outputs.append({'file': name, 'bytes': size, 'sha256': digest})
        if not coverage:
            raise ValueError('REVIEW_NO_SELECTED_OBSERVATIONS')
        manifest = {'profile': VERSION, 'review_id': 'sha256:' + identity, 'inputs': inputs,
            'source_pages': acquired.manifest['pages'], 'outputs': outputs, 'counts': dict(counts),
            'station_year_element_rows': len(coverage), 'first_day': min(r['first_day'] for r in coverage.values()),
            'last_day': max(r['last_day'] for r in coverage.values()), 'pilot_candidate_unchanged': pilot['candidate_id'],
            'ordering': 'fixed station order and retained provider record order; coverage rows sorted',
            'missing_values': 'blank normalized value with explicit MISSING/QUALITY_FLAG; never substituted with zero',
            'trace': 'trace=true retains canonical display convention value=0; not a claim of no precipitation',
            'scope': 'four captured Kansas stations; full available PRCP/TMAX/TMIN history; not statewide completeness',
            'count_semantics': 'usable means unwithheld by missing/QC flag policy; not scientific validity or station homogeneity',
            'lifecycle': 'WORK; private review package; not an admitted source or released dataset',
            'rights': 'current source/redistribution review required; no upload authorized',
            'historical_locations': 'not inferred from current station catalog coordinates',
            'review_state': 'PENDING', 'source_admitted': False, 'released': False, 'published': False}
        write_new(target / 'review-manifest.json', canon(manifest))
        archive = target / 'review-package.zip'
        with zipfile.ZipFile(archive, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
            for name in [r['file'] for r in outputs] + ['review-manifest.json']:
                info = zipfile.ZipInfo(name, date_time=(1980,1,1,0,0,0)); info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100600 << 16
                with z.open(info, 'w') as to, (target / name).open('rb') as src:
                    while chunk := src.read(1024**2): to.write(chunk)
        archive.chmod(0o600)
        digest, size = hash_regular(archive, max_output_bytes)
        receipt = {'profile': VERSION, 'state': 'private-review-package-verified', 'manifest_sha256': hashlib.sha256(canon(manifest)).hexdigest(),
            'outputs': outputs, 'package': {'file': str(archive), 'bytes': size, 'sha256': digest},
            'counts': dict(counts), 'review_state': 'PENDING', 'admitted': False, 'released': False, 'published': False}
        verify_existing(target, receipt_root / 'verified.json', inputs, max_output_bytes, receipt=receipt)
        write_new(receipt_root / 'verified.json', canon(receipt))
        return {'outcome': 'VERIFIED', 'destination': str(target), 'first_day': manifest['first_day'],
                'last_day': manifest['last_day'], 'coverage_rows': len(coverage), **receipt}
    except Exception as error:
        write_new(receipt_root / 'failed.json', canon({'profile': VERSION, 'state': 'failed; partial outputs retained',
                  'error_type': type(error).__name__, 'counts': dict(counts), 'published': False}))
        raise

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', required=True)
    parser.add_argument('--capture-id', required=True)
    parser.add_argument('--max-output-bytes', type=int, default=LIMIT,
                        help='explicit bound for each output, at most 512 MiB; separate from local/GitHub budgets')
    args = parser.parse_args(argv)
    try:
        result = derive(Path(args.root), args.capture_id, max_output_bytes=args.max_output_bytes)
    except (ValueError, OSError, KeyError, TypeError, EOFError, zipfile.BadZipFile):
        print('{"outcome":"HELD","reason":"ARCHIVE_REVIEW_FAILED; original/partial bytes preserved"}')
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
