/** Opt-in access for the operator's loopback-only preview. Never used by writes.
 * The dev service must bind 127.0.0.1; hosted deployments omit this setting.
 */
export function localImageryReadAllowed(request: Request, configuredOrigin: unknown): boolean {
  if (configuredOrigin !== "http://127.0.0.1:4173") return false;
  const url = new URL(request.url);
  if (url.origin !== configuredOrigin || request.method !== "GET") return false;
  const origin = request.headers.get("origin");
  const site = request.headers.get("sec-fetch-site");
  // Cross-site pages cannot use the local imagery endpoint or its catalogs.
  if (origin && origin !== configuredOrigin || site && site !== "same-origin" && site !== "none") return false;
  return url.pathname === "/api/earth-engine-context/catalog"
    || url.pathname === "/api/earth-engine-context/active"
    || /^\/api\/earth-engine-context\/ks-\d{4}-[a-z0-9]+\/ee-[a-z0-9]+\/\d+\/\d+\/\d+\.png$/.test(url.pathname);
}
