// Keep ordinary assets out of Fetch interception: Chrome can cancel a paused
// image/media request before emitting any matching Network-domain evidence.
// Block off-origin I/O in the browser itself; reproduce the same empty-style
// fixture in the page without creating an external network request.
export async function isolateBrowserNetwork(call, origin, { attribution = null, interceptScene = false, unavailableApis = false } = {}) {
  const base = new URL(origin);
  if (base.protocol !== 'http:' || !['127.0.0.1', 'localhost', '[::1]'].includes(base.hostname) || base.pathname !== '/' || base.search || base.hash || base.username || base.password) {
    throw new Error('Browser fixtures require an uncredentialed loopback origin');
  }
  await call('Network.setBlockedURLs', { urlPatterns: [
    ...(unavailableApis ? [
      { urlPattern: `${base.origin}/api/build`, block: false },
      { urlPattern: `${base.origin}/api/*`, block: true },
    ] : []),
    { urlPattern: `${base.origin}/*`, block: false },
    { urlPattern: '*://*:*/*', block: true },
  ] });
  // Optional local-only attribution exercises the real MapLibre control. The
  // empty inline source contains no observations and makes no provider request.
  const style={version:8,sources:{},layers:[{id:'test-background',type:'background',paint:{'background-color':'#172832'}}]};
  if(attribution){
    style.sources['test-attribution']={type:'geojson',data:{type:'FeatureCollection',features:[]},attribution};
    style.layers.push({id:'test-attribution-layer',type:'circle',source:'test-attribution',paint:{'circle-opacity':0}});
  }
  await call('Page.addScriptToEvaluateOnNewDocument', { source: `(() => {
    const originalFetch = window.fetch;
    window.fetch = function(input, init) {
      const url = new URL(input instanceof Request ? input.url : String(input), location.href);
      // Plain navigation needs an unavailable provider, not a paused request
      // that Chrome can discard during an immediate reload. Workers/non-fetch
      // APIs keep the explicit transport interceptor; the build receipt stays real.
      if (${unavailableApis} && url.origin === ${JSON.stringify(base.origin)} && url.pathname.startsWith('/api/') && url.pathname !== '/api/build') {
        const signal = init?.signal ?? (input instanceof Request ? input.signal : null);
        if (signal?.aborted) return Promise.reject(new DOMException('Aborted', 'AbortError'));
        return Promise.resolve(new Response('{"error":"Isolated navigation test: provider unavailable"}', {status:503,headers:{'Content-Type':'application/json'}}));
      }
      if (url.origin !== ${JSON.stringify(base.origin)} && /^https?:$/.test(url.protocol) && (url.pathname.includes('/styles/') || url.pathname.endsWith('/style.json'))) {
        if (init?.signal?.aborted || (input instanceof Request && input.signal.aborted)) return Promise.reject(new DOMException('Aborted', 'AbortError'));
        return Promise.resolve(new Response(JSON.stringify(${JSON.stringify(style)}), {status:200,headers:{'Content-Type':'application/json'}}));
      }
      return originalFetch.call(this,input,init);
    };
  })();` });
  const patterns = [
    // Page network block rules do not propagate to workers. Keep their API
    // transport fixture even when window.fetch returns its response locally.
    { urlPattern: `${base.origin}/api/*` },
    ...(interceptScene ? [{ urlPattern: `${base.origin}/assets/map-engine-*.js` }] : []),
  ];
  if (patterns.length) await call('Fetch.enable', { patterns });
}
