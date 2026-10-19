/** Public-copy routing is deny by default; storage authorization remains per-reader. */
export type PublicRouteDecision = { allowed: boolean; reason: string };

const pages = new Set(["/", "/about", "/topics", "/almanacs", "/observatory", "/observatory/sources", "/favicon.ico", "/api/build"]);
const families = "(?:water|weather|soil|storm-events|earthquakes)";
const reads = new RegExp(`^/api/governed/(?:v1|${families}/v1)/(?:bootstrap|layers|evidence)$`);
const administrativeFamilies = "(?:water|weather|soil|storm-events|earthquakes|subsurface|groundwater|archive)";
const administration = new RegExp(`^/api/governed/${administrativeFamilies}-admin/(?:stage|status|activate|withdraw)$`);
const releasePages = new RegExp(`^/governed/${administrativeFamilies}-release$`);
const generatedAssets = /^\/(?:assets|_assets|_next\/static|maplibre|fonts|images|vendor)\/[a-zA-Z0-9_./@-]+$/;
const safeAsset = /^\/[a-zA-Z0-9_-]+\.(?:svg|png|jpg|jpeg|webp|ico|woff2?)$/;

export function publicRouteDecision(input: string, method = "GET"): PublicRouteDecision {
  const url = new URL(input, "https://kansasfrontiermatrix.com");
  const path = url.pathname;
  if (/%(?:2f|5c|2e|00)/i.test(path) || path.includes("\\") || path.includes("//")) return { allowed: false, reason: "INVALID_PUBLIC_PATH" };
  if (path.startsWith("/data/") || path.startsWith("/history/") || path.startsWith("/public/")) return { allowed: false, reason: "UNRELEASED_ASSET_PATH" };
  if (administration.test(path)) return { allowed: ["GET", "POST"].includes(method), reason: "OWNER_AUTHORIZATION_REQUIRED" };
  if (path === "/api/staging/account" || path === "/api/ai/status" || /^\/api\/ai\/jobs\/[A-Za-z0-9_-]{1,128}$/.test(path)) return {allowed:method === "GET",reason:"SITE_IDENTITY_REQUIRED"};
  if (path === "/api/ai/jobs" || /^\/api\/ai\/jobs\/[A-Za-z0-9_-]{1,128}\/cancel$/.test(path)) return {allowed:method === "POST",reason:"SITE_IDENTITY_AND_ORIGIN_REQUIRED"};
  if (!["GET", "HEAD"].includes(method)) return { allowed: false, reason: "PUBLIC_READ_ONLY" };
  if (pages.has(path) || releasePages.test(path) || reads.test(path)) return { allowed: true, reason: "RELEASE_GATE_REQUIRED" };
  if (path === "/api/governed/public/catalog" || /^\/api\/governed\/public\/assets\/(?:subsurface|groundwater|archive)\/[a-zA-Z0-9][a-zA-Z0-9._-]{0,127}$/.test(path)) return { allowed: true, reason: "PUBLIC_DELIVERY_GATE_REQUIRED" };
  if (["/almanacs/farmers-winter-2026-2027.jpg", "/almanacs/old-farmers-1861-title-page.jpg"].includes(path)) return { allowed: true, reason: "ATTRIBUTED_REFERENCE_ASSET" };
  if (generatedAssets.test(path) || safeAsset.test(path)) return { allowed: true, reason: "BUILD_ASSET_ALLOWLIST_REQUIRED" };
  return { allowed: false, reason: "PUBLIC_CAPABILITY_UNAVAILABLE" };
}

export function publicUnavailable(reason: string, status = 404): Response {
  return Response.json({ envelope: { outcome: "ABSTAIN", reason_code: reason, evidence_refs: [] }, status: "WITHHELD", message: "This capability is not in the approved public delivery." }, { status, headers: { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } });
}

/** Reject alternate raw Worker origins before trusting platform identity headers. */
export function publicApplicationOriginAllowed(input: string, hostedUrl: string, canonicalUrl: string): boolean {
  const url = new URL(input);
  // The direct preview wrapper separately rejects forged identity and exact-origin mismatch.
  if (url.protocol === "http:" && url.hostname === "127.0.0.1" && Number(url.port) >= 1024) return true;
  if (url.protocol !== "https:" || url.port || url.username || url.password) return false;
  const hosted = new URL(hostedUrl), canonical = new URL(canonicalUrl);
  return url.origin === hosted.origin || url.origin === canonical.origin || url.hostname === `www.${canonical.hostname}`;
}
