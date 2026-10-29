#!/usr/bin/env python3
"""Build the welcome Geology spotlight: a few named, real KGS records.

Wells and core ranges come from the pinned subsurface tiles. Core box counts
and operator/lease names are joined from the KGS Core Library inventory only
where its start/end depths equal the tile range exactly. Mines are read by
OBJECTID from the KGS Quarries and Mines inventory. Nothing is interpolated;
this is a welcome display, not an evidence bundle.

Usage: python3 scripts/build-welcome-spotlight.py --cache /var/tmp/kfm-spotlight
"""
import argparse
import csv
import datetime as dt
import gzip
import hashlib
import io
import json
from pathlib import Path
import re
import urllib.parse
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]
TILES = ROOT / 'public/data/subsurface'
OUT = ROOT / 'app/living-welcome/subsurface-spotlight.json'
CORE_LIB = 'https://www.kgs.ku.edu/PRS/Ora_Archive/coreLib.zip'
MINES = 'https://services2.arcgis.com/ZOdjAzAQ2B0f85zi/arcgis/rest/services/Quarries_and_Mines/FeatureServer/0'
MINE_FIELDS = 'OBJECTID,KID,COUNTY_CODE,PRODUCT_CATEGORY,PRODUCT,QUARRY_TYPE,STATUS,ABANDONED_DURING_YEARS,OPERATOR_NAME,LEASE_NAME,ACRES_IN_MINE,COMMENTS,DATA_SOURCE,UPDATE_DATE'

# One per region of the state, so the spotlight wanders the map.
WELLS = ['wwc5-1056646013', 'wwc5-509325', 'wwc5-1056970867', 'wwc5-480993', 'wwc5-506704', 'wwc5-476439']
CORES = ['core-1006030866', 'core-1005425761', 'core-1031881223', 'core-1006154451', 'core-1044833286', 'core-1025810230']
# OBJECTID -> display label. Operators named here are companies or agencies.
MINE_LABELS = {
    5095: 'Hutchinson Salt Company', 5162: 'Lyons Rock Salt Mine', 127: 'Independent Salt Company',
    6078: 'Blue Rapids Mine', 8682: 'National Gypsum Mine', 5043: 'Calvert Corp. · Miller pit',
    635: 'Inland Quarries', 3721: 'Linn County lead workings',
}
COUNTIES = {7: 'Barber', 53: 'Ellsworth', 107: 'Linn', 117: 'Marshall', 137: 'Norton', 155: 'Reno', 159: 'Rice', 209: 'Wyandotte'}


def now():
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def fetch(url, path):
    if not path.exists():
        with urllib.request.urlopen(url, timeout=120) as response:
            path.write_bytes(response.read())
    return path.read_bytes()


def clean(value):
    return re.sub(r'\s+', ' ', value).strip() if isinstance(value, str) else None


def tile_records(ids):
    wanted, found = set(ids), {}
    for tile in sorted(TILES.glob('tile-*.json.gz')):
        for row in json.loads(gzip.decompress(tile.read_bytes())):
            if row['id'] in wanted:
                found[row['id']] = row
    missing = wanted - found.keys()
    if missing:
        raise SystemExit(f'missing tile records: {sorted(missing)}')
    return [found[i] for i in ids]


def well(row):
    iv = row['intervals']
    if iv[0]['top'] != 0 or iv[-1]['bottom'] != row['totalDepth'] or any(iv[i]['top'] != iv[i - 1]['bottom'] for i in range(1, len(iv))):
        raise SystemExit(f'{row["id"]}: log is not one contiguous column')
    return {'kind': 'well', 'id': row['id'], 'label': row['name'], 'coordinates': row['coordinates'], 'sourceUrl': row['sourceUrl'],
            'recordDate': row['sourceTime'], 'locationMethod': row['locationMethod'], 'depthUnit': row['depthUnit'],
            'totalDepth': row['totalDepth'], 'intervals': [{'top': i['top'], 'bottom': i['bottom'], 'description': i['description']} for i in iv]}


def core(row, library):
    kid = row['id'].removeprefix('core-')
    span = row['intervals'][0]
    match = [r for r in library.get(kid, []) if r['START_DEPTH'] and r['END_DEPTH'] and float(r['START_DEPTH']) == span['top'] and float(r['END_DEPTH']) == span['bottom']]
    if len(match) != 1:
        raise SystemExit(f'{row["id"]}: no single Core Library row with the tile range')
    lib = match[0]
    return {'kind': 'core', 'id': row['id'], 'label': clean(lib['LEASE_NAME']), 'operator': clean(lib['OPERATOR_NAME']), 'kid': kid,
            'coordinates': row['coordinates'], 'sourceUrl': row['sourceUrl'], 'photosUrl': row.get('photosUrl'), 'depthUnit': row['depthUnit'],
            'depthReference': row['depthReference'], 'top': span['top'], 'bottom': span['bottom'], 'boxes': int(lib['BOXES'])}


def mine(feature):
    p = feature['properties']
    oid = p['OBJECTID']
    note = clean(p['COMMENTS'])
    # Inventory notes about reserves or production are not shown on the welcome.
    if note and re.search(r'reserve|production', note, re.I):
        note = None
    return {'kind': 'mine', 'id': f'mine-{oid}', 'label': MINE_LABELS[oid], 'kid': str(p['KID']),
            'coordinates': [round(c, 6) for c in feature['geometry']['coordinates']], 'county': COUNTIES[p['COUNTY_CODE']],
            'sourceUrl': MINES + '/query?' + urllib.parse.urlencode({'where': f'OBJECTID={oid}', 'outFields': '*', 'f': 'json'}),
            'category': clean(p['PRODUCT_CATEGORY']), 'product': clean(p['PRODUCT']), 'operation': clean(p['QUARRY_TYPE']),
            'status': clean(p['STATUS']), 'abandonedDuring': clean(p['ABANDONED_DURING_YEARS']), 'operator': clean(p['OPERATOR_NAME']),
            'lease': clean(p['LEASE_NAME']), 'acres': clean(p['ACRES_IN_MINE']), 'note': note, 'inventorySource': clean(p['DATA_SOURCE']),
            'updated': dt.datetime.fromtimestamp(p['UPDATE_DATE'] / 1000, dt.timezone.utc).date().isoformat() if p['UPDATE_DATE'] else None}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cache', type=Path, required=True, help='download cache outside the application tree')
    args = parser.parse_args()
    args.cache.mkdir(parents=True, exist_ok=True)
    manifest = json.loads((TILES / 'manifest.json').read_text())
    sources = {s['id']: s for s in manifest['sources']}

    core_zip = fetch(CORE_LIB, args.cache / 'coreLib.zip')
    core_at = dt.datetime.fromtimestamp((args.cache / 'coreLib.zip').stat().st_mtime, dt.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
    with zipfile.ZipFile(io.BytesIO(core_zip)) as archive:
        text = archive.read('coreLib.txt').decode('latin-1')
    library = {}
    for row in csv.DictReader(io.StringIO(text)):
        library.setdefault(row['WELL_KID'], []).append(row)

    query = urllib.parse.urlencode({'where': f'OBJECTID IN ({",".join(map(str, MINE_LABELS))})', 'outFields': MINE_FIELDS, 'returnGeometry': 'true', 'outSR': '4326', 'f': 'geojson'})
    mines_raw = fetch(f'{MINES}/query?{query}', args.cache / 'mines.geojson')
    mines_at = dt.datetime.fromtimestamp((args.cache / 'mines.geojson').stat().st_mtime, dt.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
    features = {f['properties']['OBJECTID']: f for f in json.loads(mines_raw)['features']}
    if set(features) != set(MINE_LABELS):
        raise SystemExit(f'missing mine records: {sorted(set(MINE_LABELS) - set(features))}')

    wells, cores = tile_records(WELLS), tile_records(CORES)
    records = []
    # Interleave well -> core -> mine so each kind takes turns.
    mines = [mine(features[i]) for i in MINE_LABELS]
    for i in range(max(len(wells), len(cores), len(mines))):
        if i < len(wells): records.append(well(wells[i]))
        if i < len(cores): records.append(core(cores[i], library))
        if i < len(mines): records.append(mines[i])

    out = {
        'version': 1, 'generatedAt': now(),
        'sources': [
            {**{k: sources['kgs-wwc5'][k] for k in ('id', 'title', 'url', 'retrievedAt', 'sourceTime', 'sha256')}, 'limitation': 'Recorded water-well logs as written by the driller. Depths are below local land surface; one log does not describe the ground between wells.'},
            {**{k: sources['kgs-core'][k] for k in ('id', 'title', 'url', 'retrievedAt', 'sourceTime', 'sha256')}, 'limitation': 'Inventory start/end spans in drilled depth; recovery gaps are possible and the hole may deviate from vertical.'},
            {'id': 'kgs-core-boxes', 'title': 'KGS Core Library inventory (box counts and lease names)', 'url': CORE_LIB, 'retrievedAt': core_at, 'sha256': hashlib.sha256(core_zip).hexdigest(), 'limitation': 'Joined only where the inventory start/end depths equal the pinned core range. Box counts describe stored boxes, not recovered length.'},
            {'id': 'kgs-mines', 'title': 'KGS Quarries and Mines inventory', 'url': MINES, 'retrievedAt': mines_at, 'sha256': hashlib.sha256(mines_raw).hexdigest(), 'limitation': 'KGS/KDHE historical inventory, largely circa 2000. Status is historical, not a present-day operating assessment. Points are PLSS-based and do not describe underground workings, depths or reserves.'},
        ],
        'records': records,
    }
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n')
    print(f'wrote {OUT.relative_to(ROOT)}: {len(records)} records')


if __name__ == '__main__':
    main()
