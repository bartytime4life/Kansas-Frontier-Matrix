/* Browser-local page shell only. Never handles provider or operational traffic. */
const CACHE = 'kfm-recovery-shell-v2';
self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', event => event.waitUntil(self.clients.claim()));
self.addEventListener('message', event => {
  if (event.origin !== self.location.origin) return;
  let sourceUrl;
  try {
    sourceUrl = typeof event.source?.url === 'string' ? new URL(event.source.url) : null;
  } catch {
    sourceUrl = null;
  }
  if (!sourceUrl || sourceUrl.origin !== self.location.origin) return;
  if (event.data?.type !== 'PREPARE' || !Array.isArray(event.data.urls)) return;
  event.waitUntil((async () => {
    let ready = true;
    const cache = await caches.open(CACHE);
    const urls = [...new Set(event.data.urls)].filter(value => {
      try { const url = new URL(value); return url.origin === self.location.origin && !url.pathname.startsWith('/api/') && !url.pathname.includes('/@vite') && !url.pathname.includes('__vite'); } catch { return false; }
    }).slice(0, 180);
    for (const url of urls) {
      try { const response = await fetch(url, { credentials: 'same-origin' }); if (!response.ok) { ready = false; continue; } await cache.put(url,response); } catch { ready = false; }
    }
    const shell = urls.find(value => new URL(value).pathname === '/');
    if (!shell || !(await cache.match(shell))) ready = false;
    event.ports[0]?.postMessage({ ready, cached: urls.length });
  })());
});
self.addEventListener('fetch', event => {
  const url = new URL(event.request.url);
  if (event.request.method !== 'GET' || url.origin !== self.location.origin || url.pathname.startsWith('/api/') || url.pathname.includes('/@vite') || url.pathname.includes('__vite')) return;
  if (event.request.mode === 'navigate') {
    event.respondWith(fetch(event.request).catch(async () => {
      const cache = await caches.open(CACHE);
      return await cache.match(event.request, { ignoreSearch: true }) || await cache.match('/', { ignoreSearch: true }) || new Response('Offline shell is not cached. Reconnect and prepare the workspace before relying on offline review.', { status: 503, headers: { 'Content-Type': 'text/plain' } });
    }));
  } else {
    // Vite varies static assets by Origin; module/style requests and cache
    // preparation send different Origin headers. These are fixed local assets,
    // so their cached bytes do not vary. Navigation/API matching stays separate.
    event.respondWith((async () => { const cache = await caches.open(CACHE); const cached = await cache.match(event.request, { ignoreVary: url.pathname.startsWith('/assets/') }); try { const response = await fetch(event.request); return response; } catch { return cached || Response.error(); } })());
  }
});
