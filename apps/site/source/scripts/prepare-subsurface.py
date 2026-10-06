#!/usr/bin/env python3
"""Build pinned, public-context display assets; never write to an evidence DB.

Requires Python 3.10+ and pyproj==3.7.1 for the documented NAD27 grid shift.
Input archives and the PROJ grid are cached OUTSIDE the application tree.
"""
import argparse
import collections
import csv
import datetime as dt
import gzip
import hashlib
import io
import json
import math
from pathlib import Path
import re
import sqlite3
import tempfile
import urllib.request
import zipfile

CAPTURED = '2026-10-06T02:23:24.686123+00:00'
ARCHIVES = {
    'wwc5_wells': ('f08e1b808691ec19cd08afd644a565e13e7279f062aac6ab27d47c1adf9ee23f', '2026-09-11', '2026-10-06T02:23:24.686123+00:00'),
    'wwc5_lith_log': ('58b122d0af710474e7263fc9e44013081e026ba1eab922ca9e6a9644eb36d317', '2026-09-11', '2026-10-06T02:23:17.961907+00:00'),
    'interpreted_logs': ('09172a57bac1937afe664332686469d3e05da8c97ef377fe079a8cb093d180df', '2025-03-27', '2026-10-06T02:23:24.215681+00:00'),
    'coreLib': ('f087d0bbd88597fb88189bdbb16f91b29471343db5fda42d0d8d1558ce6ea2b0', '2026-09-11', '2026-10-06T02:23:15.997130+00:00'),
}
GRID_HASH = '44611d823c48e5347500ee6afe40ff33d2b88cf817bf59f705ed4a4c3bd687d7'
PREFIX = '/data/subsurface/'
MAX_TILE_BYTES = 3_000_000


def encode(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':'), allow_nan=False).encode('utf-8')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def pinned_download(path, url, sha):
    if not path.exists():
        with urllib.request.urlopen(url, timeout=180) as response:
            data = response.read()
        if digest(data) != sha:
            raise ValueError(f'Source changed: {url}; qualify the new version before replacing pinned inputs')
        path.write_bytes(data)
    if digest(path.read_bytes()) != sha:
        raise ValueError(f'Input integrity failure: {path.name}')


def rows(input_dir, name, stats):
    with zipfile.ZipFile(input_dir / (name + '.zip')) as archive:
        if archive.testzip() is not None:
            raise ValueError(f'Corrupt archive: {name}')
        members = archive.infolist()
        if len(members) != 1:
            raise ValueError(f'Unexpected archive layout: {name}')
        with io.TextIOWrapper(archive.open(members[0]), encoding='cp1252', newline='') as text:
            for row in csv.DictReader(text):
                stats[name + 'Rows'] += 1
                if None in row or any(v is None for v in row.values()):
                    stats[name + 'MalformedRows'] += 1
                    continue
                yield row


def number(value):
    try:
        parsed = float(value)
        return parsed if math.isfinite(parsed) else None
    except (TypeError, ValueError):
        return None


def interval(top, bottom, description):
    a, b = number(top), number(bottom)
    if a is None or b is None or a < 0 or b <= a:
        return None
    # Original descriptions are retained, never inferred from interpretation codes.
    return {'top': a, 'bottom': b, 'description': description.strip()}


def normalize_description(value):
    return ' '.join(value.lower().split())


def kansas_coordinates(lng, lat):
    x, y = number(lng), number(lat)
    if x is None or y is None or not (-102.1 <= x <= -94.5 and 36.9 <= y <= 40.1):
        return None
    return [round(x, 6), round(y, 6)]


def record_date(value):
    try:
        return dt.datetime.strptime(value, '%d-%b-%Y').date().isoformat()
    except ValueError:
        return 'Unknown record date'


def transform_core(lng, lat, transformer):
    if not kansas_coordinates(lng, lat):
        return None
    return kansas_coordinates(*transformer.transform(float(lng), float(lat), errcheck=True))


def core_record_url(kid):
    return 'https://chasm.kgs.ku.edu/ords/qualified.well_page.DisplayWell?f_kid=' + kid


def write_gzip(path, data):
    raw = encode(data)
    compressed = gzip.compress(raw, compresslevel=9, mtime=0)
    path.write_bytes(compressed)
    return {'sha256': digest(compressed), 'bytes': len(compressed), 'uncompressedBytes': len(raw)}


def build(input_dir, output_dir):
    import pyproj
    if pyproj.__version__ != '3.7.1':
        raise RuntimeError('Use pyproj==3.7.1 to reproduce the pinned horizontal transformation')
    input_dir.mkdir(parents=True, exist_ok=True)
    for name, (sha, _, _) in ARCHIVES.items():
        pinned_download(input_dir / (name + '.zip'), 'https://www.kgs.ku.edu/PRS/Ora_Archive/' + name + '.zip', sha)
    grid = input_dir / 'us_noaa_conus.tif'
    pinned_download(grid, 'https://cdn.proj.org/us_noaa_conus.tif', GRID_HASH)
    transformer = pyproj.Transformer.from_pipeline(
        '+proj=pipeline +step +proj=unitconvert +xy_in=deg +xy_out=rad '
        '+step +proj=hgridshift +grids=' + str(grid.resolve()) +
        ' +step +proj=unitconvert +xy_in=rad +xy_out=deg')
    output_dir.mkdir(parents=True, exist_ok=True)
    stats = collections.Counter()
    with tempfile.TemporaryDirectory(prefix='kfm-subsurface-') as temporary:
        db = sqlite3.connect(str(Path(temporary) / 'display.sqlite'))
        db.executescript('''PRAGMA journal_mode=OFF; PRAGMA synchronous=OFF;
            CREATE TABLE wells (id TEXT PRIMARY KEY, payload TEXT, county TEXT, lng REAL, lat REAL);
            CREATE TABLE logs (well TEXT, top REAL, bottom REAL, description TEXT, normalized TEXT,
                UNIQUE(well, top, bottom, description));
            CREATE TABLE interpretations (well TEXT, top REAL, bottom REAL, normalized TEXT, codes TEXT,
                UNIQUE(well, top, bottom, normalized, codes));''')
        for r in rows(input_dir, 'wwc5_wells', stats):
            if not r['WELL_ID'].isdigit():
                stats['wellsInvalidIdentity'] += 1
                continue
            coordinates = kansas_coordinates(r['NAD83_LONGITUDE'], r['NAD83_LATITUDE'])
            if not coordinates:
                stats['wellsUnlocatedOrOutsideBounds'] += 1
                continue
            depth = number(r['WELL_DEPTH'])
            record = {'id': 'wwc5-' + r['WELL_ID'], 'sourceId': 'kgs-wwc5', 'kind': 'well',
                'name': 'WWC5 ' + r['WELL_ID'], 'coordinates': coordinates,
                'coordinateReference': 'WGS84 display from KGS NAD83; EPSG:1188 approximation (4 m)',
                'locationMethod': r['LONG_LAT_TYPE'] if r['LONG_LAT_TYPE'] in ('From PLSS', 'GPS') else 'Unspecified',
                'sourceUrl': 'https://chasm.kgs.ku.edu/ords/wwc5.wwc5d2.well_details?well_id=' + r['WELL_ID'],
                'sourceTime': record_date(r['COMPLE_DATE']), 'depthUnit': 'ft', 'depthReference': 'land-surface',
                'totalDepth': depth if depth is not None and depth > 0 else None}
            try:
                db.execute('INSERT INTO wells VALUES (?,?,?,?,?)', (r['WELL_ID'], encode(record).decode(), r['COUNTY'].strip(), *coordinates))
            except sqlite3.IntegrityError:
                stats['duplicateWells'] += 1
        db.commit()
        print('Read well locations', flush=True)
        for r in rows(input_dir, 'wwc5_lith_log', stats):
            value = interval(r['TOP'], r['BOTTOM'], r['LOG'])
            if value is None:
                stats['invalidLoggedIntervals'] += 1
                continue
            cursor = db.execute('INSERT OR IGNORE INTO logs VALUES (?,?,?,?,?)',
                (r['WELL_ID'], value['top'], value['bottom'], value['description'], normalize_description(value['description'])))
            if not cursor.rowcount:
                stats['duplicateLoggedIntervals'] += 1
        db.commit()
        print('Read original logged intervals', flush=True)
        for r in rows(input_dir, 'interpreted_logs', stats):
            value = interval(r['TOP_DEPTH'], r['BOTTOM_DEPTH'], r['SAMPLE_DESCRIPTION'])
            if value is None:
                stats['invalidInterpretedIntervals'] += 1
                continue
            codes = r['LITHOLOGY_CODES'].strip()
            if not codes or not re.fullmatch(r'[A-Za-z0-9/,. -]+', codes):
                stats['invalidInterpretationCodes'] += 1
                continue
            db.execute('INSERT OR IGNORE INTO interpretations VALUES (?,?,?,?,?)',
                (r['WELL_ID'], value['top'], value['bottom'], normalize_description(value['description']), codes))
        db.commit()
        db.executescript('CREATE INDEX log_well ON logs(well); CREATE INDEX int_well ON interpretations(well,top,bottom,normalized);')
        print('Read published interpretations', flush=True)
        tiles = collections.defaultdict(list)
        counties = collections.defaultdict(lambda: [0, 0.0, 0.0])
        locator = []
        for well_id, payload, county, lng, lat in db.execute('SELECT * FROM wells ORDER BY id'):
            record = json.loads(payload)
            logs = []
            for top, bottom, description, normalized in db.execute('SELECT top,bottom,description,normalized FROM logs WHERE well=? ORDER BY top,bottom,description', (well_id,)):
                value = {'top': top, 'bottom': bottom, 'description': description}
                interpretation = db.execute('SELECT DISTINCT codes FROM interpretations WHERE well=? AND top=? AND bottom=? AND normalized=?', (well_id, top, bottom, normalized)).fetchall()
                if len(interpretation) == 1:
                    value['interpreted'] = interpretation[0][0]
                    stats['matchedInterpretedIntervals'] += 1
                elif len(interpretation) > 1:
                    stats['ambiguousInterpretationMatches'] += 1
                logs.append(value)
            record['intervals'] = logs
            stats['wellCount'] += 1
            stats['loggedIntervalCount'] += len(logs)
            stats['wellsWithIntervals'] += bool(logs)
            bounds = (math.floor(lng * 2) / 2, math.floor(lat * 2) / 2)
            tiles[bounds].append(record)
            counties[county][0] += 1; counties[county][1] += lng; counties[county][2] += lat
            locator.append([record['id'], county, [lng, lat]])
        stats['loggedIntervalsWithoutMappedWell'] = db.execute('SELECT COUNT(*) FROM logs LEFT JOIN wells ON logs.well=wells.id WHERE wells.id IS NULL').fetchone()[0]
        db.close()
        print('Joined display columns', flush=True)
        core_records = {}
        for r in rows(input_dir, 'coreLib', stats):
            if r['STATE_CODE'] != 'Kansas':
                stats['coresOutsideKansas'] += 1
                continue
            kid = r['WELL_KID']
            if not kid.isdigit():
                stats['coresInvalidIdentity'] += 1
                continue
            coordinates = transform_core(r['LONGITUDE'], r['LATITUDE'], transformer)
            if coordinates is None:
                stats['coresUnlocatedOrOutsideBounds'] += 1
                continue
            record = core_records.setdefault(kid, {
                'id': 'core-' + kid, 'sourceId': 'kgs-core', 'kind': 'core', 'name': 'Core KID ' + kid,
                'coordinates': coordinates, 'coordinateReference': 'WGS84 display from NAD27 via NOAA CONUS NADCON to NAD83; EPSG:1188 approximation (4 m)',
                'locationMethod': 'Provider location; original method unspecified', 'sourceUrl': core_record_url(kid),
                'sourceTime': '2026-09-11 inventory; sampling date not supplied',
                'depthUnit': 'ft', 'depthReference': 'drilled-depth', 'totalDepth': None, 'intervals': []})
            if record['coordinates'] != coordinates:
                raise ValueError('Conflicting coordinates for core identity ' + kid)
            if r['PHOTOS'] == 'YES':
                record['photosUrl'] = 'https://chasm.kgs.ku.edu/ords/qualified.cimg2.CoreImages?f_well=' + kid
            sample = interval(r['START_DEPTH'], r['END_DEPTH'], 'Core inventory range; recovery and lithology not provided')
            if sample is not None and sample not in record['intervals']:
                record['intervals'].append(sample)
            elif sample is None:
                stats['invalidCoreRanges'] += 1
            else:
                stats['duplicateCoreRanges'] += 1
        for record in core_records.values():
            record['intervals'].sort(key=lambda v: (v['top'], v['bottom']))
            lng, lat = record['coordinates']
            tiles[(math.floor(lng * 2) / 2, math.floor(lat * 2) / 2)].append(record)
            stats['coreCount'] += 1; stats['coreRangeCount'] += len(record['intervals'])
            stats['coresWithPhotoLinks'] += 'photosUrl' in record
            locator.append([record['id'], '', [lng, lat]])
        tile_entries = []
        tile_by_record = {}
        def partition(records, west, south, size, tile_id):
            records.sort(key=lambda r: r['id'])
            if len(encode(records)) > MAX_TILE_BYTES and size > 0.0078125:
                half = size / 2
                groups = collections.defaultdict(list)
                for r in records:
                    x = int(r['coordinates'][0] >= west + half)
                    y = int(r['coordinates'][1] >= south + half)
                    groups[(x, y)].append(r)
                for (x,y), group in sorted(groups.items()):
                    partition(group, west + x * half, south + y * half, half, tile_id + str(x + 2*y))
                return
            filename = tile_id + '.json.gz'
            metrics = write_gzip(output_dir / filename, records)
            tile_entries.append({'id': tile_id, 'bounds': [west,south,west+size,south+size],
                'url': PREFIX + filename, 'count': len(records),
                'wellCount': sum(r['kind']=='well' for r in records), 'coreCount': sum(r['kind']=='core' for r in records), **metrics})
            for r in records:
                tile_by_record[r['id']] = tile_id
        for (west,south), records in sorted(tiles.items()):
            partition(records,west,south,0.5,'tile-' + str(int((west+180)*2)) + '-' + str(int((south+90)*2)))
        # Compact arrays: [id, county-or-empty, [longitude,latitude], tileId].
        locator.sort(key=lambda row: row[0])
        for row in locator:
            row.append(tile_by_record[row[0]])
        locator_metrics = write_gzip(output_dir / 'locator.json.gz', locator)
        source_entries = []
        for name,(sha,date,retrieved) in ARCHIVES.items():
            source_entries.append({'id': {'wwc5_wells':'kgs-wwc5','wwc5_lith_log':'kgs-wwc5-logs','interpreted_logs':'kgs-wwc5-interpreted','coreLib':'kgs-core'}[name],
                'title': {'wwc5_wells':'KGS WWC5 well records','wwc5_lith_log':'KGS original lithologic logs','interpreted_logs':'KGS standardized lithology codes','coreLib':'KGS Core Library inventory'}[name],
                'url':'https://www.kgs.ku.edu/PRS/Ora_Archive/'+name+'.zip','retrievedAt':retrieved,'sourceTime':date,'sha256':sha,
                'limitation': {'wwc5_wells':'Provider records may be inaccurate or incomplete; PLSS locations are approximate. Record date can mean construction, reconstruction or plugging. No water-quality data, current well status or surveyed trajectory is inferred.',
                    'wwc5_lith_log':'Original logged descriptions, with recorded gaps and overlaps. Not continuous geology between wells. Invalid depth ranges are counted and excluded.',
                    'interpreted_logs':'Older independent interpretation edition; only exact well/depth/normalized-description matches are attached. Codes are interpretations, not observations or measured hydraulic properties.',
                    'coreLib':'Inventory start/end spans may contain recovery gaps. Original drilling reference and deviation are unknown; ranges cannot be treated as true vertical depths or placed beneath terrain. Photos are external links only.'}[name]})
        manifest = {'version':1, 'capturedAt':CAPTURED, 'status':'EXTERNAL_CONTEXT_ONLY',
            'sources':source_entries, 'tiles':tile_entries, 'totals':dict(sorted(stats.items())),
            'locator':{'url':PREFIX+'locator.json.gz','count':len(locator),'columns':['id','county','coordinates','tileId'],**locator_metrics},
            'counties':[{'name':name,'coordinates':[round(values[1]/values[0],6),round(values[2]/values[0],6)],'count':values[0]} for name,values in sorted(counties.items()) if name],
            'horizontalTransform':{'from':['EPSG:4269','EPSG:4267'],'to':'EPSG:4326', 'nad83Operation':'EPSG:1188, NAD83 to WGS84 (1), 4 m stated operation accuracy; not source-location accuracy',
                'nad27GridUrl':'https://cdn.proj.org/us_noaa_conus.tif','nad27GridSha256':GRID_HASH,
                'software':'pyproj '+pyproj.__version__+' / PROJ '+pyproj.proj_version_str,'coordinateDecimals':6},
            'coverageLimits':['Kansas records with valid provider coordinates inside the Kansas regional bounding box; not an exact state-boundary clip.',
                'County navigation points are arithmetic means of included WWC5 locations, not county boundaries or official county centroids.',
                'No DEM registration, ground-elevation datum, deviation trajectory, published 3D framework or geophysical raw data is supplied by these archives.',
                'Public-source coordinate precision does not establish accuracy; do not use for excavation, engineering, water quality, property boundaries or resource estimates.'],
            'privacy':{'excludedFields':['OWNER','DIRECTIONS','DWR_NUMBER','DRILLER','OTHER_ID','OPERATOR_NAME','CURRENT_OPERATOR_NAME','LEASE_NAME','API','WELL_USE','ELEV','STATIC_DEPTH','EST_YIELD'],
                'labels':'Generic provider record identities only. No owner/operator labels or directions are projected.'},
            'useConstraints':'Official KGS public-download factual records. KGS/KDHE accuracy and completeness disclaimers apply; no Creative Commons license or independent evidence admission is asserted.'}
        (output_dir / 'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
        print(json.dumps({'totals':manifest['totals'],'tiles':len(tile_entries),'compressedBytes':sum(t['bytes'] for t in tile_entries)+locator_metrics['bytes'],'largestTileBytes':max(t['uncompressedBytes'] for t in tile_entries)},indent=2),flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-dir',type=Path,required=True,help='External cache for pinned original archives; never public/ or another deployed directory')
    parser.add_argument('--output-dir',type=Path,default=Path(__file__).resolve().parents[1]/'public/data/subsurface')
    args = parser.parse_args()
    if args.input_dir.resolve().is_relative_to(Path(__file__).resolve().parents[1]):
        parser.error('Raw input cache must stay outside the application tree')
    build(args.input_dir,args.output_dir)


if __name__ == '__main__':
    main()
