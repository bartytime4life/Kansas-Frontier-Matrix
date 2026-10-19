import { timingSafeEqual } from "node:crypto";
import { ingestionConfig } from "./ingestion-config.mjs";

const HEADERS = { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff", "Referrer-Policy": "no-referrer" };
export function json(value, status = 200) { return Response.json(value, { status, headers: HEADERS }); }

// Machine capability only. Browser sessions and role headers grant no access.
export function workerAuthorized(request, environment = process.env) {
  const config = ingestionConfig(environment);
  const supplied = request.headers.get("authorization") ?? "";
  const expected = `Bearer ${environment.KFM_CAPTURE_WORKER_TOKEN ?? ""}`;
  return Boolean(config.ready && new URL(request.url).origin === config.origin
    && request.headers.get("origin") !== "null"
    && (!request.headers.has("origin") || request.headers.get("origin") === config.origin)
    && request.headers.get("sec-fetch-site") !== "cross-site"
    && /^Bearer [A-Za-z0-9_-]{43,256}$/.test(supplied)
    && supplied.length === expected.length
    && timingSafeEqual(Buffer.from(supplied), Buffer.from(expected)));
}
