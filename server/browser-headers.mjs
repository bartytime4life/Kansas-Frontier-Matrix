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
  'Content-Security-Policy': "default-src 'self'; script-src 'self' 'unsafe-inline' 'wasm-unsafe-eval'; style-src 'self' 'unsafe-inline'; img-src 'self' https: data: blob:; font-src 'self' https: data:; connect-src 'self' https:; worker-src 'self' blob:; child-src 'self' blob:; frame-src 'self'; media-src 'self' https: blob:; object-src 'none'; base-uri 'self'; form-action 'self'; frame-ancestors 'self' https://host.godaddy.com",
});

export function applyBrowserHeaders(_request, response) {
  for (const [name, value] of Object.entries(browserHeaders)) response.setHeader(name, value);
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
    for(const handler of handlers)handler.call(server,request,response);
  });
}
