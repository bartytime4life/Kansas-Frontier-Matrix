// Browser policy for this separate GoDaddy Node composition. Resource origins
// remain HTTPS-capable for attributed map providers; hydration/MapLibre require
// inline script/style and WebAssembly. This is not a nonce-based script policy.
export const browserHeaders = Object.freeze({
  'X-Content-Type-Options': 'nosniff',
  'Referrer-Policy': 'strict-origin-when-cross-origin',
  'Permissions-Policy': 'camera=(), microphone=(), payment=(), usb=(), geolocation=(self)',
  'Strict-Transport-Security': 'max-age=86400',
  // Preserve the owner's public contact text and React hydration through CDN
  // HTML rewriting. API routes keep their stricter private/no-store overrides.
  'Cache-Control': 'no-transform',
  // connect-src includes blob: because the map library fetches images it is handed as blob URLs. Without it
  // the Event Observatory's radar frames were refused and every frame was withheld. A blob URL can only
  // name data this page already holds, so this opens no outside destination.
  'Content-Security-Policy': "default-src 'self'; script-src 'self' 'unsafe-inline' 'wasm-unsafe-eval'; style-src 'self' 'unsafe-inline'; img-src 'self' https: data: blob:; font-src 'self' https: data:; connect-src 'self' https: blob:; worker-src 'self' blob:; child-src 'self' blob:; frame-src 'self'; media-src 'self' https: blob:; object-src 'none'; base-uri 'self'; form-action 'self'; frame-ancestors 'self' https://host.godaddy.com",
});

export function applyBrowserHeaders(_request, response) {
  for (const [name, value] of Object.entries(browserHeaders)) response.setHeader(name, value);
}

// The pinned framework does not list WebM in its static MIME table. Correct
// only successful public welcome videos at header commit; the framework still
// owns file lookup, status, ranges, caching, lengths and the response stream.
function welcomeVideoHeaders(request, response) {
  if (!['GET', 'HEAD'].includes(request.method) || !/^\/welcome\/(?:motion|demos)\/[a-z0-9][a-z0-9_-]*\.webm$/.test((request.url ?? '').split('?')[0])) return;
  const writeHead = response.writeHead;
  response.writeHead = function (statusCode, ...args) {
    if (Number.isInteger(statusCode) && statusCode >= 200 && statusCode < 300) {
      const index = typeof args[0] === 'string' ? 1 : 0, supplied = args[index];
      // Explicit writeHead headers override setHeader. Preserve every other
      // header, including duplicate raw-array fields and the reason phrase.
      if (Array.isArray(supplied)) {
        const headers = [];
        for (let i = 0; i < supplied.length; i += 2) if (String(supplied[i]).toLowerCase() !== 'content-type') headers.push(supplied[i], supplied[i + 1]);
        args[index] = [...headers, 'Content-Type', 'video/webm'];
      } else if (supplied && typeof supplied === 'object') {
        const headers = { ...supplied };
        for (const name of Object.keys(headers)) if (name.toLowerCase() === 'content-type') delete headers[name];
        args[index] = { ...headers, 'Content-Type': 'video/webm' };
      }
      response.setHeader('Content-Type', 'video/webm');
    }
    return writeHead.call(this, statusCode, ...args);
  };
}

// The hosting proxy replaces the body of a 502 or 504 with its own "error code: 502" page, so a route's
// own explanation ("The exact historical radar frame is unavailable...") never reached the visitor and the
// page's JSON reader failed instead. A public read that ends in 502 or 504 therefore leaves as 503, which
// the proxy passes through with its body. The route's status stays readable in X-KFM-Upstream-Status.
// Only GET and HEAD under /api/ are touched; writes and the worker relays keep their exact statuses.
function keepUpstreamFailureBody(request, response) {
  if (!['GET', 'HEAD'].includes(request.method) || !(request.url ?? '').startsWith('/api/')) return;
  const writeHead = response.writeHead;
  response.writeHead = function (statusCode, ...args) {
    if (statusCode !== 502 && statusCode !== 504) return writeHead.call(this, statusCode, ...args);
    response.setHeader('X-KFM-Upstream-Status', String(statusCode));
    // A reason phrase written for the old status would contradict the new one.
    if (typeof args[0] === 'string') args[0] = 'Service Unavailable';
    response.statusMessage = 'Service Unavailable';
    return writeHead.call(this, 503, ...args);
  };
}

export function installPublicDelivery(server) {
  const handlers=server.listeners('request');
  server.removeAllListeners('request');
  server.on('request',(request,response)=>{
    applyBrowserHeaders(request,response);
    const host=String(request.headers.host??'').toLowerCase();
    const forwarded=String(request.headers['x-forwarded-host']??'').split(',')[0].trim().toLowerCase();
    // These headers can select only a fixed public redirect. They confer no
    // trusted request origin, account identity or authorization capability.
    if([host,forwarded].some(value=>value==='www.kansasfrontiermatrix.com'||value==='www.kansasfrontiermatrix.com:443')){
      const target=request.url??'/';
      if(!target.startsWith('/')||target.startsWith('//')||/[\\\r\n]/.test(target)){
        response.writeHead(400);response.end('Bad Request');request.resume();return;
      }
      response.writeHead(308,{Location:'https://kansasfrontiermatrix.com'+target});
      response.end();request.resume();return;
    }
    welcomeVideoHeaders(request,response);
    keepUpstreamFailureBody(request,response);
    for(const handler of handlers)handler.call(server,request,response);
  });
}
