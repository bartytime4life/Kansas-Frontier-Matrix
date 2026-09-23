/** Cloudflare Worker entry point for the Vite client application. */

interface AssetFetcher {
  fetch(request: Request): Promise<Response>;
}

interface Env {
  ASSETS: AssetFetcher;
}

interface ExecutionContext {
  waitUntil(promise: Promise<unknown>): void;
  passThroughOnException(): void;
}

// This application has no API router. Never turn a missing adapter into a 200
// HTML shell; source/renderer availability must remain distinguishable from UI.
const unavailable = (request: Request, status: number, code: string): Response => new Response(
  request.method === "HEAD" ? null : JSON.stringify({
    state: "unavailable", code, runtime: "repository-shell",
    message: code === "KFM_API_NOT_CONFIGURED"
      ? "Live-feed API adapters are not configured in this repository application."
      : "The request path is invalid.",
  }),
  { status, headers: { "Content-Type": "application/json; charset=utf-8",
    "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff" } },
);

const worker = {
  async fetch(request: Request, env: Env, _ctx: ExecutionContext): Promise<Response> {
    const url = new URL(request.url);
    let pathname: string;
    try { pathname = decodeURIComponent(url.pathname).replace(/\/+/g, "/"); }
    catch { return unavailable(request, 400, "KFM_INVALID_PATH"); }
    if (/^\/api(?:\/|$)/i.test(pathname)) return unavailable(request, 503, "KFM_API_NOT_CONFIGURED");
    const response = await env.ASSETS.fetch(request);
    if (response.status !== 404 || request.method !== "GET") return response;
    if (url.pathname.includes(".")) return response;
    return env.ASSETS.fetch(new Request(new URL("/index.html", request.url), request));
  },
};

export default worker;
