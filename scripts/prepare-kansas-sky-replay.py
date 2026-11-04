#!/usr/bin/env python3
"""Offline, deterministic readsb -> bounded Kansas replay candidate. Never fetches or publishes.
Usage: python3 scripts/prepare-kansas-sky-replay.py TRACE.json.gz SOURCE_URL MEMBER OUTPUT.json
The input SHA256 binds original compressed bytes; the output keeps one longest continuous regional segment.
"""
import gzip, hashlib, json, math, pathlib, re, sys
from datetime import datetime, timezone

def number(x, low, high):
    return x if isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x) and low <= x <= high else None

def text(x, pattern):
    return x.strip() if isinstance(x, str) and re.fullmatch(pattern, x.strip()) else None

def iso(ms):
    return datetime.fromtimestamp(ms / 1000, timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z')

def prepare(raw, source_url, member):
    if len(raw) > 4 * 1024 * 1024: raise ValueError('INPUT_TOO_LARGE')
    # Bound decompression before JSON parsing.
    import io
    with gzip.GzipFile(fileobj=io.BytesIO(raw)) as stream: decoded = stream.read(16 * 1024 * 1024 + 1)
    if len(decoded) > 16 * 1024 * 1024: raise ValueError('EXPANDED_INPUT_TOO_LARGE')
    data = json.loads(decoded)
    if not re.fullmatch(r'https://github\.com/adsblol/globe_history(?:_\d{4})?/releases/download/[^\s]+', source_url): raise ValueError('SOURCE_NOT_ARCHIVE')
    hex_id = text(data.get('icao'), r'~?[0-9a-f]{6}')
    epoch = number(data.get('timestamp'), 1_000_000_000, 4_000_000_000)
    if not hex_id or epoch is None or not isinstance(data.get('trace'), list) or len(data['trace']) > 100_000: raise ValueError('INVALID_TRACE')
    segments, segment, previous, callsign = [], [], None, None
    for row in data['trace']:
        if not isinstance(row, list) or len(row) < 8: raise ValueError('INVALID_POINT')
        seconds, lat, lon = number(row[0], 0, 86400), number(row[1], 36.2, 40.9), number(row[2], -103.2, -93.6)
        if seconds is None or lat is None or lon is None:
            if segment: segments.append(segment)
            segment, previous, callsign = [], None, None
            continue
        flags = row[6] if isinstance(row[6], int) else 0
        extra = row[8] if len(row) > 8 and isinstance(row[8], dict) else {}
        method = text(row[9], r'[a-z0-9_]{1,32}') if len(row) > 9 else None
        at = round((epoch + seconds) * 1000)
        if flags & 2: callsign = None
        if 'flight' in extra: callsign = text(extra['flight'], r'[A-Za-z0-9-]{1,8}')
        if previous and ((row[3] == 'ground') != previous['onGround'] or at <= previous['observedAt'] or at - previous['observedAt'] > 60000 or flags & 3 or previous['positionMethod'] != method):
            if segment: segments.append(segment)
            segment = []
        ground = row[3] == 'ground'
        baro = None if flags & 8 else (0 if ground else number(row[3], -1500, 70000))
        geometric = number(row[10], -1500, 70000) if len(row) > 10 else None
        if geometric is None and flags & 8: geometric = number(row[3], -1500, 70000)
        point = {'hex':hex_id, 'callsign':callsign, 'registration':text(data.get('r'), r'[A-Za-z0-9-]{1,10}'),
          'type':text(data.get('t'), r'[A-Za-z0-9]{2,4}'), 'category':text(extra.get('category'), r'[A-D][0-7]'),
          'lat':lat, 'lon':lon, 'onGround':ground, 'altBaroFt':baro, 'altGeomFt':geometric,
          'groundSpeedKt':number(row[4],0,1500), 'trackDeg':number(row[5],0,360), 'verticalRateFpm':number(row[7],-20000,20000),
          'squawk':text(extra.get('squawk'),r'[0-7]{4}'), 'emergency':None, 'military':bool((data.get('dbFlags') or 0) & 1),
          'positionAgeS':0, 'observedAt':at, 'timestampBasis':'provider', 'positionMethod':method,
          'rollDeg':number(row[13],-180,180) if len(row)>13 else None,
          'indicatedAirSpeedKt':number(row[12],0,1500) if len(row)>12 else None, 'mach':number(extra.get('mach'),0,5),
          'providerId':'adsb-lol', 'interpolated':False, 'traceFlags':flags, 'breakBefore':not segment,
          'verticalRateReference':'geometric' if flags & 4 else 'barometric',
          'positionQuality':{'nic':number(extra.get('nic'),0,11),'nacP':number(extra.get('nac_p'),0,11),'sil':number(extra.get('sil'),0,3),'rcM':number(extra.get('rc'),0,100000),'rssi':number(extra.get('rssi'),-100,0)}}
        segment.append(point); previous=point
    if segment: segments.append(segment)
    points = max(segments, key=lambda part: part[-1]['observedAt']-part[0]['observedAt'], default=[])
    if len(points)<2 or len(points)>10000 or points[-1]['observedAt']-points[0]['observedAt']<60000: raise ValueError('NO_BOUNDED_REGIONAL_SEGMENT')
    identifier = f"{iso(points[0]['observedAt'])[:10]}-{hex_id}"
    result = {'schemaVersion':1,'id':identifier,'provider':'adsb.lol','license':'ODbL-1.0','licenseUrl':'https://opendatacommons.org/licenses/odbl/1-0/',
      'sourceUrl':source_url, 'sourceMember':member, 'sourceSha256':hashlib.sha256(raw).hexdigest(),
      'transformation':'readsb trace; Kansas regional bounds; longest continuous segment; split at stale/new-leg flags, source changes, non-increasing timestamps or >60s gaps; no invented samples',
      'altitudeReferences':{'altBaroFt':'pressure altitude','altGeomFt':'WGS84 ellipsoid'}, 'points':points}
    return result

if __name__ == '__main__':
    source, url, member, output = sys.argv[1:]
    result = prepare(pathlib.Path(source).read_bytes(),url,member)
    encoded=(json.dumps(result,separators=(',',':'),allow_nan=False)+'\n').encode()
    if len(encoded)>4*1024*1024: raise ValueError('OUTPUT_TOO_LARGE')
    pathlib.Path(output).write_bytes(encoded)
    print(json.dumps({'id':result['id'],'points':len(result['points']),'start':iso(result['points'][0]['observedAt']),'end':iso(result['points'][-1]['observedAt']),'sha256':hashlib.sha256(encoded).hexdigest(),'bytes':len(encoded)}))
