#!/usr/bin/env python3
"""Build a complete source-bound KDOT bridge lab from public inventory services.
Raw responses are cached outside shipping assets; no local database is read.
"""
import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json
from pathlib import Path
import runpy
from urllib.parse import urlencode

ROOT = Path(__file__).resolve().parents[1]
base = runpy.run_path(str(ROOT / 'scripts/prepare-labs-data.py'))
Fetcher, encoded, sha, column = (base[k] for k in ('Fetcher', 'encoded', 'sha', 'column'))
SERVICE = 'https://kanplan.ksdot.gov/arcgis_web_adaptor/rest/services/Structures/'
NETWORKS = {'state': ('State_Bridges', 'OBJECTID,STR_NAME,FACILITY,FEATINT,COUNTYNAME,BUILT_DATE,STR_LENGTH,LANES_CARRIED,STR_AADT,OPPOSTCL,SUF_RATE,UNDER_CONSTRUCTION'),
            'local': ('Non_State_Bridges', 'OBJECTID,STRUCT_NUM,FACILITY,FEATINT,COUNTY,YEARBUILT,YEARRECON,LENGTH_ENG,LANES,ADTTOTAL,ADTYEAR,OPPOSTCL,SUFF_RATE,HISTSIGN,INSPDATE')}


def clean(value, limit=120):
    if value is None:
        return None
    text = ' '.join(str(value).replace('<', '').replace('>', '').split())
    return text[:limit] or None


def number(value, minimum=0, maximum=2_000_000):
    return value if isinstance(value, (int, float)) and not isinstance(value, bool) and minimum <= value <= maximum else None


def network(fetch, name, through):
    service, fields = NETWORKS[name]
    url = SERVICE + service + '/MapServer/0'
    def read(params):
        raw, meta = fetch.get(url + '/query?' + urlencode({'f': 'json', 'where': '1=1', **params}))
        body = json.loads(raw)
        if 'error' in body:
            raise ValueError(body['error'])
        return body, meta
    ids_body, ids_meta = read({'returnIdsOnly': 'true'})
    source_ids = ids_body.get('objectIds')
    if not isinstance(source_ids, list) or not source_ids or not all(isinstance(i, int) for i in source_ids) or len(source_ids) > 40000:
        raise ValueError('Invalid or unbounded KDOT source identifiers')
    multiplicity = Counter(source_ids)
    ordered = sorted(multiplicity)
    pages = [ordered[i:i+900] for i in range(0, len(ordered), 900)]
    def page(ids):
        result, meta = read({'objectIds': ','.join(map(str, ids)), 'outFields': fields, 'returnGeometry': 'true', 'outSR': '4326', 'geometryPrecision': '5', 'orderByFields': 'OBJECTID', 'resultRecordCount': '1000'})
        received = result.get('features', [])
        if result.get('exceededTransferLimit') or Counter(r['attributes']['OBJECTID'] for r in received) != Counter({i: multiplicity[i] for i in ids}):
            raise ValueError('KDOT source changed or a page was capped; no partial inventory is published')
        return received, meta
    with ThreadPoolExecutor(max_workers=3) as pool:
        replies = list(pool.map(page, pages))
    rows, snapshots = [], [ids_meta]
    occurrences = Counter()
    for features, meta in replies:
        snapshots.append(meta)
        for feature in sorted(features, key=encoded):
            a, point = feature['attributes'], feature.get('geometry') or {}
            state = name == 'state'
            built = number(a.get('BUILT_DATE' if state else 'YEARBUILT'), 1800, int(through[:4]))
            lon, lat = point.get('x'), point.get('y')
            row_hash = sha(encoded(feature))[:16]
            row_key = f'kdot-{name}-{a["OBJECTID"]}-{row_hash}'
            occurrences[row_key] += 1
            row = {'id': f'{row_key}-{occurrences[row_key]}', 'name': clean(a.get('FACILITY')) or clean(a.get('FEATINT')) or f'Bridge {a["OBJECTID"]}',
                   'structure': clean(a.get('STR_NAME' if state else 'STRUCT_NUM')), 'crossing': clean(a.get('FEATINT')),
                   'network': 'State highway' if state else 'Local road', 'county': clean(a.get('COUNTYNAME' if state else 'COUNTY')) or 'Not recorded',
                   'year': built, 'length': number(a.get('STR_LENGTH' if state else 'LENGTH_ENG'), 1, 60000),
                   'lanes': number(a.get('LANES_CARRIED' if state else 'LANES'), 1, 40),
                   'traffic': number(a.get('STR_AADT' if state else 'ADTTOTAL'), 0, 2_000_000),
                   'sufficiency': number(a.get('SUF_RATE' if state else 'SUFF_RATE'), 0, 100),
                   'status': clean(a.get('OPPOSTCL')) or 'Not recorded',
                   'construction': clean(a.get('UNDER_CONSTRUCTION')) if state else None,
                   'trafficYear': number(a.get('ADTYEAR'), 1950, int(through[:4])),
                   'historic': clean(a.get('HISTSIGN')) if not state else None}
            if isinstance(lon, (float,int)) and isinstance(lat, (float,int)) and -180<=lon<=180 and -90<=lat<=90:
                row.update(longitude=lon,latitude=lat)
            rows.append(row)
    again, end_meta = read({'returnIdsOnly': 'true', 'returnGeometry': 'false'})
    snapshots.append(end_meta)
    if Counter(again['objectIds']) != multiplicity:
        raise ValueError('KDOT source inventory changed during acquisition; retry for a coherent snapshot')
    return rows, snapshots, {'network': name, 'sourceRecords': len(source_ids), 'uniqueObjectIds': len(multiplicity), 'returnedRecords': len(rows), 'url': url}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cache',type=Path,default=ROOT/'work/labs-bridge-raw')
    parser.add_argument('--offline',action='store_true')
    parser.add_argument('--through',default=datetime.now(timezone.utc).date().isoformat())
    args=parser.parse_args()
    fetch=Fetcher(args.cache,args.offline)
    rows,snapshots,counts=[],[],[]
    for name in NETWORKS:
        r,s,c=network(fetch,name,args.through);rows.extend(r);snapshots.extend(s);counts.append(c)
    if len(rows)>40000 or len({r['id'] for r in rows})!=len(rows):
        raise ValueError('Unexpected bridge inventory size or duplicate identifiers')
    years=[r['year'] for r in rows if r['year'] is not None]
    data={'kind':'records','records':rows,'columns':[column('name','Carries','string'),column('structure','Structure identifier','string'),column('crossing','Crossing','string'),column('network','Network','string'),column('county','County','string'),column('year','Recorded built year','year'),column('length','Structure length',unit='ft'),column('traffic','Average daily traffic',unit='vehicles/day'),column('trafficYear','Traffic count year','year'),column('lanes','Lanes'),column('sufficiency','Source sufficiency score',unit='0–100'),column('status','Recorded status','string'),column('construction','Under construction flag','string'),column('historic','Historic designation','string')],
          'yearField':'year','categoryField':'network','valueField':'length','temporalMode':'events','inventoryAsOf':args.through,
          'coverage':'Complete returned KDOT state and local bridge inventories; construction years describe structures present in this snapshot, not every bridge ever built.',
          'sourceCounts':counts,'sourceSnapshot':snapshots[0],'sourceSnapshots':snapshots,
          'limits':['This is a present-day inventory with recorded construction years. Scrubbing the timeline shows surviving inventory by built year, not historical network completeness, construction rates or abandoned bridges.',
                    'Counts are inventory records, not unique physical bridges. The state service returns some repeated OBJECTIDs and structure identifiers with different route attributes; every returned row is retained with a source-content identifier.',
                    'Recorded status and sufficiency scores are source attributes, not a current safety determination, engineering assessment or permission to enter a structure.',
                    'State and local inventories have different attribute definitions and observation dates. Sufficiency score is not a physical condition percentage. Traffic counts may come from different years.',
                    'Unknown and future construction years remain undated; no year or coordinate is fabricated. Under-construction flags and source status are retained.',
                    'The collection covers bridges and structures in these two KDOT services. Dams, mines, towers and airports are not included in this instrument.']}
    sources=[{'name':'Kansas Department of Transportation bridge inventories','url':SERVICE,'license':'Public KDOT inventory data, provided as source context without warranty; credit KDOT.','citation':'Kansas Department of Transportation, State_Bridges and Non_State_Bridges public ArcGIS inventory services. Complete enumerated OBJECTID sets checked before and after paged acquisition.'}]
    result={'format':'kfm-story-bundle-v1','story':'built-kansas','version':1,'built_at':max(s['retrievedAt'] for s in snapshots),'sources':sources,'observed':{'from':str(min(years)),'to':str(max(years))},'data':data}
    raw=encoded(result)
    if len(raw)>16_000_000:
        raise ValueError('Bridge bundle exceeds its explicit 16MB instrument budget')
    digest=sha(raw);filename=f'built-kansas-{digest[:16]}.json'
    target=ROOT/'public/labs-data-bridges';target.mkdir(parents=True,exist_ok=True)
    (target/filename).write_bytes(raw)
    manifest={'built-kansas':{'path':'/labs-data-bridges/'+filename,'sha256':digest,'bytes':len(raw),'observed':result['observed'],'retrievedAt':result['built_at'],'records':len(rows)}}
    (ROOT/'app/labs/bridge-snapshots.mjs').write_text('// Generated by scripts/prepare-labs-bridges.py from public KDOT inventories.\nexport const BRIDGE_LAB_SNAPSHOTS = Object.freeze('+json.dumps(manifest,indent=2)+');\n')
    for old in target.glob('*.json'):
        if old.name!=filename:old.unlink()
    print(json.dumps({'manifest':manifest,'sourceCounts':counts,'undated':sum(r['year'] is None for r in rows)},indent=2))

if __name__=='__main__':main()
