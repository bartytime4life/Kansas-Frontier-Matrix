import importlib.util
import json
from pathlib import Path
import tempfile
import threading
import time
import unittest
import urllib.request
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('cache', 'scripts/basemap-cache.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

class Tests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.root = Path(self.tmp.name)
        (self.root / '.kfm-local-store.json').write_text(json.dumps({'schema_version':'1','scope':'local-quarantine-store'}))
        self.calls = []
        def fetch(url): self.calls.append(url); return b'raw-provider-bytes', 'image/png', 60, 'etag', 'source-date'
        self.cache = m.Cache(self.root, m.RESERVE + 8192, fetch)
    def tearDown(self):
        self.cache.db.close(); m.os.close(self.cache.file_lock); self.tmp.cleanup()
    def url(self, x): return f'{m.TOPO}/8/97/{x}'
    def test_eviction_and_integrity(self):
        c = self.cache
        c.get(self.url(1)); c.get(self.url(2)); self.assertEqual(c.get(self.url(1))[2], 'hit')
        c.get(self.url(3)); self.assertEqual(c.usage(), (8192,2))
        self.assertEqual({r[0] for r in c.db.execute('SELECT url FROM tiles')}, {self.url(1),self.url(3)})
        key = m.hashlib.sha256(self.url(1).encode()).hexdigest(); (c.objects/key).write_bytes(b'corrupt')
        self.assertEqual(c.get(self.url(1))[0], b'raw-provider-bytes')
        self.assertEqual(c.status()['limitBytes'], m.RESERVE+8192)
    def test_aerial_prefetch_matches_browser_query_encoding(self):
        url=m.overview()[1]
        browser=url.replace('%2C',',')
        self.assertEqual(self.cache.get(url)[2], 'stored')
        self.assertEqual(self.cache.get(browser)[2], 'hit')
        self.assertEqual(len(self.calls),1)
    def test_expired_does_not_silently_serve_old_tiles(self):
        c=self.cache; c.get(self.url(1)); c.db.execute('UPDATE tiles SET expires=0'); c.db.commit()
        c.fetch=lambda _: (_ for _ in ()).throw(ValueError('provider unavailable'))
        with self.assertRaises(ValueError): c.get(self.url(1))
    def test_bounds_and_original_lane(self):
        raw=self.root/'data/raw';raw.mkdir();(raw/'original').write_text('untouched')
        for x in range(8): self.cache.get(self.url(x))
        self.assertEqual((raw/'original').read_text(),'untouched')
        self.assertLessEqual(self.cache.usage()[0]+m.RESERVE,self.cache.limit)
        self.cache.fetch=lambda _: (b'x'*(m.MAX_ITEM+1),'image/png',60,None,None)
        with self.assertRaises(ValueError): self.cache.get(self.url(11))
    def test_unapproved_hosts_times_redirects_and_query_injection(self):
        for url in ['http://127.0.0.1/secret',self.url(1)+'?time=2026',self.url(1).replace('https:','file:'),self.url(1).replace('nationalmap.gov','nationalmap.gov.evil'),m.TOPO+'/99/0/0',m.TOPO+'/8/999/0',m.DASC+'?bbox=nan,1,2,3']:
            with self.subTest(url=url),self.assertRaises(ValueError): m.policy(url)
        with self.assertRaises(ValueError): m.NoRedirect().redirect_request(None,None,None,None,None,None)
        for url in m.overview(): m.policy(url)
        self.assertLess(len(m.overview()),512)
    def test_symlink_and_duplicate_service_denied(self):
        with self.assertRaises(BlockingIOError): m.Cache(self.root)
        other=self.root/'linked';other.symlink_to(self.root,target_is_directory=True)
        with self.assertRaises(ValueError): m.Cache(other)
    def test_http_origin_host_session_guards(self):
        saved_port=m.PORT;m.PORT=0;server=m.Server(self.cache);m.PORT=server.server_address[1];thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
        origin=next(iter(m.ORIGINS));base=f'http://127.0.0.1:{m.PORT}'
        try:
            def request(path,headers,method='GET'):
                return urllib.request.urlopen(urllib.request.Request(base+path,headers=headers,method=method))
            for headers in [{},{'Origin':'https://evil.example'},{'Origin':origin,'Host':'evil.example'}]:
                with self.assertRaises(urllib.error.HTTPError) as e: request('/status',headers)
                self.assertEqual(e.exception.code,403)
            with request('/status',{'Origin':origin}) as r: self.assertEqual(json.load(r)['schema'],'kfm-basemap-cache/v1')
            with self.assertRaises(urllib.error.HTTPError):request('/resource?url='+urllib.parse.quote(self.url(1)),{'Origin':origin})
            with request('/resource?url='+urllib.parse.quote(self.url(1)),{'Origin':origin,'X-KFM-Session':self.cache.token}) as r:self.assertEqual(r.read(),b'raw-provider-bytes')
            with request('/status',{'Origin':origin},'OPTIONS') as r:self.assertEqual(r.headers['Access-Control-Allow-Private-Network'],'true')
        finally:server.shutdown();server.server_close();thread.join();m.PORT=saved_port

if __name__ == '__main__': unittest.main()
