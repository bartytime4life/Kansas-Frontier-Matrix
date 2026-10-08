#!/usr/bin/env python3
"""Bounded, replaceable display cache. Never a KFM evidence or original-data lane."""
import argparse
import fcntl
import hashlib
import json
import math
import os
from pathlib import Path
import re
import secrets
import shutil
import sqlite3
import stat
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit, parse_qs, urlencode
from urllib.request import Request, build_opener, HTTPRedirectHandler

PORT = 8770
LIMIT = 10_000_000_000  # Owner-selected 10 GB; includes reserved index/in-flight space.
MAX_ITEM = 8 * 1024 * 1024
RESERVE = 64 * 1024 * 1024
MAX_JOB = 512 * 1024 * 1024
ORIGINS = {'https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site', 'http://127.0.0.1:4173', 'http://127.0.0.1:4194'}
DASC = 'https://dascservices.kansasgis.org/arcgis/rest/services/IMAGERY_STATEWIDE/NG911_2024_1ft_Natural_Color/ImageServer/exportImage'
TOPO = 'https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer/tile'
UA = 'KFM/1.0 (owner-local basemap cache; https://github.com/bartytime4life/Kansas-Frontier-Matrix)'


def policy(url):
    """Only exact existing basemap endpoints; no credentials, redirects, or arbitrary proxy."""
    if not isinstance(url, str) or len(url) > 2048 or any(ord(c) < 32 for c in url):
        raise ValueError('Invalid resource')
    u = urlsplit(url)
    if u.scheme != 'https' or u.username or u.password or u.port or u.fragment:
        raise ValueError('Unsupported resource')
    if u.netloc == 'tiles.openfreemap.org' and not u.query:
        m = re.fullmatch(r'/planet/(?:[0-9]{8}_[0-9]{6}_pt|latest)/(\d{1,2})/(\d+)/(\d+)\.pbf', u.path)
        if m:
            z, x, y = map(int, m.groups())
            if 0 <= z <= 14 and max(x, y) < 2 ** z: return 'vector', 86400
        m = re.fullmatch(r'/natural_earth/ne2sr/(\d)/(\d+)/(\d+)\.png', u.path)
        if m:
            z, x, y = map(int, m.groups())
            if z <= 6 and max(x, y) < 2 ** z: return 'natural-earth', 30 * 86400
    if url.startswith(TOPO + '/') and not u.query:
        m = re.fullmatch(re.escape(urlsplit(TOPO).path) + r'/(\d{1,2})/(\d+)/(\d+)', u.path)
        if m:
            z, y, x = map(int, m.groups())
            if z <= 16 and max(x, y) < 2 ** z: return 'topo', 7 * 86400
    if u.netloc == urlsplit(DASC).netloc and u.path == urlsplit(DASC).path:
        q = parse_qs(u.query, strict_parsing=True)
        expected = {'bboxSR':['3857'], 'imageSR':['3857'], 'size':['512,512'], 'format':['png32'], 'interpolation':['RSP_NearestNeighbor'], 'f':['image']}
        if set(q) == set(expected) | {'bbox'} and all(q[k] == v for k, v in expected.items()) and len(q['bbox']) == 1:
            b = [float(v) for v in q['bbox'][0].split(',')]
            if len(b) == 4 and all(math.isfinite(v) and abs(v) <= 20037509 for v in b) and b[0] < b[2] and b[1] < b[3]:
                return 'kansas-aerial-2024', 30 * 86400
    raise ValueError('Basemap is not eligible for this cache')


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *_args, **_kwargs):
        raise ValueError('Provider redirect rejected')


def download(url):
    provider, ttl = policy(url)
    with build_opener(NoRedirect()).open(Request(url, headers={'User-Agent': UA, 'Accept-Encoding':'identity'}), timeout=20) as r:
        kind = r.headers.get_content_type()
        if r.headers.get('Content-Encoding', 'identity') != 'identity': raise ValueError('Unexpected compression')
        data = r.read(MAX_ITEM + 1)
        if not data or len(data) > MAX_ITEM: raise ValueError('Resource exceeds 8 MiB limit or is empty')
        if provider == 'vector':
            if kind not in ('application/x-protobuf', 'application/vnd.mapbox-vector-tile', 'application/octet-stream'): raise ValueError('Invalid vector content')
        elif not (data.startswith(b'\x89PNG\r\n\x1a\n') or data.startswith(b'\xff\xd8\xff')):
            raise ValueError('Provider returned no usable image')
        cc = r.headers.get('Cache-Control', '')
        if re.search(r'(?:no-store|private|no-cache)', cc, re.I): ttl = 0
        match = re.search(r'max-age=(\d+)', cc)
        if match: ttl = min(ttl, int(match[1]))
        return data, kind, ttl, r.headers.get('ETag'), r.headers.get('Last-Modified')


def private_dir(path, create=False):
    path = Path(path)
    if not path.is_absolute(): raise ValueError('Absolute data root required')
    for p in reversed([path, *path.parents]):
        if p.is_symlink(): raise ValueError('Symlink directory rejected')
    if create: path.mkdir(mode=0o700, parents=True, exist_ok=True)
    s = path.stat()
    if not stat.S_ISDIR(s.st_mode) or s.st_uid != os.getuid() or s.st_mode & 0o022: raise ValueError('Private owner-controlled directory required')


class Cache:
    def __init__(self, root, limit=LIMIT, fetch=download):
        self.root = Path(root)
        private_dir(self.root)
        marker = self.root / '.kfm-local-store.json'
        if marker.is_symlink() or json.loads(marker.read_text()) != {'schema_version':'1', 'scope':'local-quarantine-store'}:
            raise ValueError('Existing initialized KFM data root required')
        self.path = self.root / 'data/work/basemap-cache'
        private_dir(self.path, True)
        self.objects = self.path / 'objects'
        private_dir(self.objects, True)
        for name in ['index.sqlite', 'index.sqlite-journal', '.lock']:
            if (self.path / name).is_symlink(): raise ValueError('Symlink index rejected')
        self.file_lock = os.open(self.path / '.lock', os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
        fcntl.flock(self.file_lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        self.db = sqlite3.connect(self.path / 'index.sqlite', check_same_thread=False)
        self.db.execute('PRAGMA max_page_count=4096')
        self.db.execute('CREATE TABLE IF NOT EXISTS tiles (key TEXT PRIMARY KEY, url TEXT, bytes INTEGER, mime TEXT, hash TEXT, fetched REAL, expires REAL, touched REAL, etag TEXT, modified TEXT)')
        self.lock = threading.RLock()
        self.gate = threading.BoundedSemaphore(2)
        self.limit, self.fetch = limit, fetch
        self.token = secrets.token_urlsafe(32)
        self.hits = self.misses = 0
        self.cancel = threading.Event()
        self.job = {'state':'idle', 'completed':0, 'total':0, 'bytes':0}
        # Only this namespace's fixed hash filenames are disposable; crash leftovers are never originals.
        with self.lock:
            known = {row[0] for row in self.db.execute('SELECT key FROM tiles')}
            for p in self.objects.iterdir():
                if p.is_symlink() or not p.is_file() or not re.fullmatch(r'[a-f0-9]{64}(?:\.part)?', p.name): raise ValueError('Unrecognized cache object')
                if p.name not in known: p.unlink()
            self.evict(0)

    def usage(self):
        return self.db.execute('SELECT COALESCE(SUM(bytes),0),COUNT(*) FROM tiles').fetchone()

    def evict(self, incoming):
        while self.usage()[0] + incoming > self.limit - RESERVE or self.usage()[1] >= 100_000:
            row = self.db.execute('SELECT key FROM tiles ORDER BY touched LIMIT 1').fetchone()
            if not row: raise ValueError('Cache limit too small')
            (self.objects / row[0]).unlink(missing_ok=True)
            self.db.execute('DELETE FROM tiles WHERE key=?', row)
            self.db.commit()

    def status(self):
        with self.lock:
            used, count = self.usage()
            return {'schema':'kfm-basemap-cache/v1', 'destination':str(self.path), 'limitBytes':self.limit,
                    'usedBytes':used, 'reservedBytes':RESERVE, 'tiles':count, 'hits':self.hits, 'misses':self.misses,
                    'sessionToken':self.token, 'job':dict(self.job), 'evidenceRole':'DISPLAY_CONTEXT_ONLY'}

    def get(self, url):
        policy(url)
        # Equivalent query encodings share a tile; retain the exact provider URL in the index.
        identity = url
        if url.startswith(DASC + '?'):
            q = parse_qs(urlsplit(url).query)
            q['bbox'] = [','.join(float(v).hex() for v in q['bbox'][0].split(','))]
            identity = DASC + '?' + urlencode(sorted((k, v[0]) for k, v in q.items()))
        key = hashlib.sha256(identity.encode()).hexdigest()
        if not self.gate.acquire(timeout=2): raise ValueError('Cache busy; use provider directly')
        try:
            with self.lock:
                row = self.db.execute('SELECT mime,hash,expires FROM tiles WHERE key=?', (key,)).fetchone()
                if row and row[2] > time.time():
                    try:
                        fd = os.open(self.objects / key, os.O_RDONLY | os.O_NOFOLLOW)
                        with os.fdopen(fd, 'rb') as f: data = f.read(MAX_ITEM + 1)
                        if len(data) > MAX_ITEM or hashlib.sha256(data).hexdigest() != row[1]: raise ValueError('Corrupt cache entry')
                        self.db.execute('UPDATE tiles SET touched=? WHERE key=?', (time.time(), key)); self.db.commit()
                        self.hits += 1
                        return data, row[0], 'hit'
                    except (OSError, ValueError): pass
                self.misses += 1
            data, mime, ttl, etag, modified = self.fetch(url)
            if len(data) > MAX_ITEM: raise ValueError('Resource too large')
            if ttl > 0:
                with self.lock:
                    allocated = math.ceil(len(data) / 4096) * 4096
                    self.evict(allocated)
                    if shutil.disk_usage(self.path).free < RESERVE + allocated: raise ValueError('Keep at least 64 MiB free')
                    tmp = self.objects / (key + '.part')
                    fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
                    try:
                        with os.fdopen(fd, 'wb') as f: f.write(data); f.flush(); os.fsync(f.fileno())
                        now = time.time()
                        self.db.execute('INSERT OR REPLACE INTO tiles VALUES (?,?,?,?,?,?,?,?,?,?)', (key,url,allocated,mime,hashlib.sha256(data).hexdigest(),now,now+ttl,now,etag,modified)); self.db.commit()
                        os.replace(tmp, self.objects / key)
                    finally: tmp.unlink(missing_ok=True)
            return data, mime, 'stored' if ttl > 0 else 'uncached'
        finally: self.gate.release()

    def start(self):
        with self.lock:
            if self.job['state'] == 'running': return
            self.cancel.clear()
            urls = overview()
            self.job = {'state':'running', 'completed':0, 'total':len(urls), 'bytes':0, 'failed':0}
        def work():
            for url in urls:
                if self.cancel.is_set() or self.job['bytes'] + MAX_ITEM > MAX_JOB: break
                try:
                    data, _, _ = self.get(url)
                    with self.lock: self.job['bytes'] += len(data)
                except Exception:
                    with self.lock: self.job['failed'] += 1
                with self.lock: self.job['completed'] += 1
                if self.cancel.wait(.15): break
            with self.lock:
                self.job['state'] = 'cancelled' if self.cancel.is_set() else 'partial' if self.job['failed'] or self.job['completed'] < self.job['total'] else 'complete'
        threading.Thread(target=work, daemon=True).start()


def overview():
    # Small Kansas overview only. Detailed aerial tiles are stored on demand, never statewide.
    urls = []
    for z in range(4, 10):
        n = 2 ** z
        x0, x1 = [int((lon + 180) / 360 * n) for lon in [-102.071, -94.556]]
        y0, y1 = [int((1 - math.asinh(math.tan(math.radians(lat))) / math.pi) / 2 * n) for lat in [40.077, 36.93]]
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                urls.append(f'{TOPO}/{z}/{y}/{x}')
                # Same arithmetic as MapLibre's EPSG:3857 tile template.
                half = 20037508.342789244
                resolution = (2 * half / 256) / n
                flipped = n - y - 1
                bbox = ','.join(str(v) for v in [x*256*resolution-half, flipped*256*resolution-half, (x+1)*256*resolution-half, (flipped+1)*256*resolution-half])
                urls.append(DASC + '?' + urlencode({'bbox':bbox,'bboxSR':'3857','imageSR':'3857','size':'512,512','format':'png32','interpolation':'RSP_NearestNeighbor','f':'image'}))
    return urls


class Server(ThreadingHTTPServer):
    daemon_threads = True
    def __init__(self, cache):
        self.cache = cache
        super().__init__(('127.0.0.1', PORT), Handler)


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *_args): pass  # Never log URL coordinates or session tokens.
    def _safe_origin(self):
        origin = self.headers.get('Origin')
        if origin in ORIGINS and '\r' not in origin and '\n' not in origin:
            return origin
        return None
    def _header_value(self, value):
        if value is None:
            return None
        value = value.replace('\r', '').replace('\n', '')
        return value if value else None
    def allowed(self):
        return self.headers.get('Host') == f'127.0.0.1:{PORT}' and self._safe_origin() is not None
    def reply(self, code, data, mime='application/json', cache=None):
        # Validate all provider-derived header values before emitting any response bytes.
        if mime not in {'application/json', 'image/png', 'image/jpeg', 'application/x-protobuf', 'application/vnd.mapbox-vector-tile', 'application/octet-stream'}:
            code, data, mime = 502, b'{"error":"Unsupported provider content type"}', 'application/json'
        if cache not in {'hit', 'stored', 'uncached'}: cache = None
        self.send_response(code)
        if self.allowed():
            origin = self._header_value(self._safe_origin())
            if origin is not None:
                self.send_header('Access-Control-Allow-Origin', origin)
            self.send_header('Vary', 'Origin')
        self.send_header('Content-Type', mime)
        self.send_header('Content-Length', str(len(data)))
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        if cache: self.send_header('X-KFM-Cache', cache)
        self.end_headers(); self.wfile.write(data)
    def do_OPTIONS(self):
        if not self.allowed(): return self.reply(403, b'{}')
        self.send_response(204)
        origin = self._header_value(self._safe_origin())
        if origin is not None:
            self.send_header('Access-Control-Allow-Origin', origin)
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'X-KFM-Session, Content-Type')
        self.send_header('Access-Control-Allow-Private-Network', 'true')
        self.send_header('Access-Control-Max-Age', '600')
        self.end_headers()
    def do_GET(self):
        if not self.allowed(): return self.reply(403, b'{}')
        if self.path == '/status': return self.reply(200, json.dumps(self.server.cache.status()).encode())
        if not secrets.compare_digest(self.headers.get('X-KFM-Session', ''), self.server.cache.token): return self.reply(403, b'{}')
        try:
            u = urlsplit(self.path); q = parse_qs(u.query, strict_parsing=True)
            if u.path != '/resource' or set(q) != {'url'} or len(q['url']) != 1: raise ValueError('Unknown request')
            data, mime, state = self.server.cache.get(q['url'][0])
            self.reply(200, data, mime, state)
        except Exception: self.reply(502, b'{"error":"Cache unavailable; use provider directly"}')
    def do_POST(self):
        if not self.allowed() or not secrets.compare_digest(self.headers.get('X-KFM-Session', ''), self.server.cache.token): return self.reply(403, b'{}')
        if self.headers.get('Transfer-Encoding') or self.headers.get('Content-Length', '0') != '0': return self.reply(400, b'{}')
        if self.path == '/overview': self.server.cache.start()
        elif self.path == '/cancel': self.server.cache.cancel.set()
        else: return self.reply(404, b'{}')
        self.reply(200, json.dumps(self.server.cache.status()).encode())


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', required=True)
    args = p.parse_args()
    os.umask(0o077)
    Server(Cache(args.root)).serve_forever()
