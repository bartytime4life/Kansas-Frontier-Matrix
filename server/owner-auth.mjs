import { createCipheriv, createDecipheriv, createHash, randomBytes, timingSafeEqual } from "node:crypto";
import { ingestionConfig, OWNER_GITHUB_ID } from "./ingestion-config.mjs";
import { getIngestionStore } from "./ingestion-store.mjs";
export const SESSION_COOKIE = "__Host-kfm-owner";
const FLOW_COOKIE = "__Host-kfm-github-flow";
const HEADERS = { "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff", "Referrer-Policy": "no-referrer" };
export function json(value, status = 200) { return Response.json(value, { status, headers: HEADERS }); }
export function sameOrigin(request, config = ingestionConfig()) {
  return Boolean(config.origin && new URL(request.url).origin === config.origin && request.headers.get("origin") === config.origin && request.headers.get("sec-fetch-site") !== "cross-site");
}
function cookie(request, name) {
  const matches = (request.headers.get("cookie") ?? "").split(";").map(value => value.trim()).filter(value => value.startsWith(name + "="));
  return matches.length === 1 ? matches[0].slice(name.length + 1) : "";
}
function cookieHeader(name, value, seconds) { return `${name}=${value}; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age=${seconds}`; }
function key(environment) { return createHash("sha256").update(environment.KFM_SESSION_KEY).digest(); }
export function sealFlow(value, environment = process.env) {
  const iv = randomBytes(12); const cipher = createCipheriv("aes-256-gcm", key(environment), iv);
  const encrypted = Buffer.concat([cipher.update(JSON.stringify(value)), cipher.final()]);
  return Buffer.concat([iv, cipher.getAuthTag(), encrypted]).toString("base64url");
}
export function openFlow(token, environment = process.env, at = Date.now()) {
  try {
    if (!/^[A-Za-z0-9_-]{40,1024}$/.test(token)) return null;
    const data = Buffer.from(token, "base64url"); const decipher = createDecipheriv("aes-256-gcm", key(environment), data.subarray(0, 12));
    decipher.setAuthTag(data.subarray(12, 28));
    const value = JSON.parse(Buffer.concat([decipher.update(data.subarray(28)), decipher.final()]).toString("utf8"));
    return value.expires > at && value.expires <= at + 300_000 && /^[A-Za-z0-9_-]{43}$/.test(value.state) && /^[A-Za-z0-9_-]{43}$/.test(value.verifier) ? value : null;
  } catch { return null; }
}
export async function authenticateOwner(request, { store, config = ingestionConfig() } = {}) {
  if (!config.authentication || new URL(request.url).origin !== config.origin) return false;
  const token = cookie(request, SESSION_COOKIE);
  if (!/^[A-Za-z0-9_-]{43}$/.test(token)) return false;
  try { return await (store ?? await getIngestionStore()).authenticate(token); } catch { return false; }
}
export async function ownerSignIn(request, environment = process.env) {
  const config = ingestionConfig(environment);
  if (!config.authentication || !config.database || !config.tls || new URL(request.url).origin !== config.origin) return json({ error: "Owner sign-in needs hosting configuration." }, 503);
  try { await (await getIngestionStore()).control(); } catch { return json({ error: "Owner sign-in needs the reviewed database migration." }, 503); }
  const state = randomBytes(32).toString("base64url"), verifier = randomBytes(32).toString("base64url");
  const flow = sealFlow({ state, verifier, expires: Date.now() + 300_000 }, environment);
  const location = new URL("https://github.com/login/oauth/authorize");
  for (const [name, value] of Object.entries({ client_id: environment.KFM_GITHUB_CLIENT_ID, redirect_uri: `${config.origin}/api/owner/callback`, scope: "", state, code_challenge: createHash("sha256").update(verifier).digest("base64url"), code_challenge_method: "S256", allow_signup: "false" })) location.searchParams.set(name, value);
  return new Response(null, { status: 303, headers: { ...HEADERS, Location: location.toString(), "Set-Cookie": cookieHeader(FLOW_COOKIE, flow, 300) } });
}
async function boundedOAuthJson(response) {
  if (!response.ok || !response.body) throw new Error("AUTH_FAILED");
  const reader = response.body.getReader(); let size = 0; const parts = [];
  try { while (true) { const { done, value } = await reader.read(); if (done) break; size += value.byteLength; if (size > 64_000) { await reader.cancel(); throw new Error("AUTH_FAILED"); } parts.push(Buffer.from(value)); } }
  finally { reader.releaseLock(); }
  return JSON.parse(Buffer.concat(parts).toString("utf8"));
}
export async function ownerCallback(request, { environment = process.env, fetcher = fetch, store } = {}) {
  const config = ingestionConfig(environment); const params = new URL(request.url).searchParams;
  const flow = openFlow(cookie(request, FLOW_COOKIE), environment);
  const state = params.get("state"), code = params.get("code");
  const cleared = cookieHeader(FLOW_COOKIE, "", 0);
  const denied = () => new Response("Owner sign-in was not completed.", { status: 403, headers: { ...HEADERS, "Set-Cookie": cleared } });
  if (!config.authentication || new URL(request.url).origin !== config.origin || !flow || !/^[A-Za-z0-9_-]{43}$/.test(state ?? "") || !timingSafeEqual(Buffer.from(state), Buffer.from(flow.state)) || !/^[A-Za-z0-9_-]{1,256}$/.test(code ?? "") || params.getAll("state").length !== 1 || params.getAll("code").length !== 1) return denied();
  const controller = new AbortController(); const timer = setTimeout(() => controller.abort(), 15_000);
  try {
    const token = await boundedOAuthJson(await fetcher("https://github.com/login/oauth/access_token", { method: "POST", redirect: "manual", signal: controller.signal,
      headers: { Accept: "application/json", "Content-Type": "application/x-www-form-urlencoded" },
      body: new URLSearchParams({ client_id: environment.KFM_GITHUB_CLIENT_ID, client_secret: environment.KFM_GITHUB_CLIENT_SECRET, code, code_verifier: flow.verifier, redirect_uri: `${config.origin}/api/owner/callback` }) }));
    // Empty-scope identity app only; never accept repo, email, admin or other scopes.
    if (!token.access_token || token.token_type !== "bearer" || String(token.scope ?? "").trim()) return denied();
    const profile = await boundedOAuthJson(await fetcher("https://api.github.com/user", { redirect: "manual", signal: controller.signal, headers: { Authorization: `Bearer ${token.access_token}`, Accept: "application/vnd.github+json", "User-Agent": "KansasFrontierMatrix", "X-GitHub-Api-Version": "2022-11-28" } }));
    if (String(profile.id) !== OWNER_GITHUB_ID) return denied();
    // GitHub token stays transient; only an opaque, revocable owner session persists.
    const session = randomBytes(32).toString("base64url");
    await (store ?? await getIngestionStore()).session(session, Date.now() + 4 * 3_600_000);
    const headers = new Headers({ ...HEADERS, Location: `${config.origin}/source-operations` });
    headers.append("Set-Cookie", cleared); headers.append("Set-Cookie", cookieHeader(SESSION_COOKIE, session, 4 * 3600));
    return new Response(null, { status: 303, headers });
  } catch { return denied(); } finally { clearTimeout(timer); }
}
export async function ownerLogout(request) {
  if (!sameOrigin(request) || !await authenticateOwner(request)) return json({ error: "Owner sign-in required." }, 401);
  await (await getIngestionStore()).logout(cookie(request, SESSION_COOKIE));
  return new Response(null, { status: 303, headers: { ...HEADERS, Location: "/source-operations", "Set-Cookie": cookieHeader(SESSION_COOKIE, "", 0) } });
}
export function workerAuthorized(request, environment = process.env) {
  const config = ingestionConfig(environment); const token = environment.KFM_CAPTURE_WORKER_TOKEN ?? "";
  const supplied = request.headers.get("authorization") ?? "";
  const expected = `Bearer ${token}`;
  return Boolean(config.ready && new URL(request.url).origin === config.origin && /^[A-Za-z0-9_-]{43,256}$/.test(token) && /^Bearer [A-Za-z0-9_-]{43,256}$/.test(supplied) && supplied.length === expected.length && timingSafeEqual(Buffer.from(supplied), Buffer.from(expected)));
}
