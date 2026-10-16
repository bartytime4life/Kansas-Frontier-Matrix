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
