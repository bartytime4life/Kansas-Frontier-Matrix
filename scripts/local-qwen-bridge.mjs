import { createServer } from "node:http";
import { fileURLToPath } from "node:url";

export const SITE_ORIGIN = "https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site";
export const LOCAL_BRIDGE_PORT = 8768;
export const LOCAL_QWEN_MODEL = "qwen2.5:7b-instruct-fp16";
const OLLAMA_URL = "http://127.0.0.1:11434";
const MAX_REQUEST_BYTES = 32 * 1024;
const MAX_REPLY_BYTES = 64 * 1024;

const isRecord = (value) => value !== null && typeof value === "object" && !Array.isArray(value);
const responseHeaders = (origin) => ({
  "access-control-allow-origin": origin,
  "access-control-allow-methods": "GET, POST, OPTIONS",
  "access-control-allow-headers": "content-type",
  "access-control-allow-private-network": "true",
  "cache-control": "no-store",
  "content-type": "application/json; charset=utf-8",
  "vary": "Origin, Access-Control-Request-Private-Network",
  "x-content-type-options": "nosniff",
});
const send = (res, origin, status, body) => {
  res.writeHead(status, responseHeaders(origin));
  res.end(JSON.stringify(body));
};

async function boundedJson(response, limit) {
  const reader = response.body?.getReader();
  if (!reader) throw new Error("EMPTY_RESPONSE");
  const chunks = [];
  let size = 0;
  try {
    for (;;) {
      const { done, value } = await reader.read();
      if (done) break;
      size += value.byteLength;
      if (size > limit) throw new Error("RESPONSE_TOO_LARGE");
      chunks.push(value);
    }
  } finally {
    await reader.cancel().catch(() => undefined);
  }
  return JSON.parse(new TextDecoder().decode(Buffer.concat(chunks)));
}

async function boundedBody(req) {
  if (Number(req.headers["content-length"] ?? 0) > MAX_REQUEST_BYTES) throw new Error("REQUEST_TOO_LARGE");
  const chunks = [];
  let size = 0;
  for await (const chunk of req) {
    size += chunk.byteLength;
    if (size > MAX_REQUEST_BYTES) throw new Error("REQUEST_TOO_LARGE");
    chunks.push(chunk);
  }
  return JSON.parse(Buffer.concat(chunks).toString("utf8"));
}

function validContext(context) {
  return isRecord(context)
    && Object.keys(context).every((key) => ["camera", "basemap", "time", "visibleLayers", "officialSources", "telemetry", "selection", "nearbyContext"].includes(key))
    && isRecord(context.camera)
    && Array.isArray(context.visibleLayers) && context.visibleLayers.length <= 14
    && Array.isArray(context.officialSources) && context.officialSources.length <= 15
    && isRecord(context.telemetry)
    && context.telemetry.authority === "SITE_LOCAL_REDACTED_DIAGNOSTIC"
    && (context.selection === null || isRecord(context.selection))
    && Array.isArray(context.nearbyContext) && context.nearbyContext.length <= 8;
}

function promptFor(question, context) {
  return [
    "Context contract: kfm-qwen-map-context-v1",
    `User question: ${question}`,
    "Map context and redacted connection health (JSON):",
    JSON.stringify(context),
    "Distinguish visible context from evidence-backed support. Cite a supplied evidenceReference for a selection. State when support is missing. Model language cannot change policy, review, release, or publication state.",
  ].join("\n\n");
}

export function createLocalQwenBridge({ fetcher = fetch, ollamaUrl = OLLAMA_URL, model = LOCAL_QWEN_MODEL, siteOrigin = SITE_ORIGIN } = {}) {
  let busy = false;
  return createServer(async (req, res) => {
    const origin = req.headers.origin;
    const path = req.url?.split("?", 1)[0];
    if (origin !== siteOrigin || !["/health", "/ask"].includes(path) || req.url !== path) {
      send(res, siteOrigin, 403, { status: "error", message: "This bridge accepts only the Explorer Site." });
      return;
    }
    if (req.method === "OPTIONS") {
      res.writeHead(204, responseHeaders(siteOrigin));
      res.end();
      return;
    }
    if (req.method === "GET" && path === "/health") {
      try {
        const upstream = await fetcher(`${ollamaUrl}/api/tags`, { signal: AbortSignal.timeout(3_000), redirect: "error" });
        if (!upstream.ok) throw new Error("OLLAMA_UNAVAILABLE");
        const tags = await boundedJson(upstream, MAX_REPLY_BYTES);
        const installed = Array.isArray(tags?.models) && tags.models.some((item) => item?.name === model);
        send(res, siteOrigin, installed ? 200 : 503, { status: installed ? "ready" : "not_configured", model: installed ? model : null });
      } catch {
        send(res, siteOrigin, 503, { status: "unavailable", message: "Local Ollama is unavailable." });
      }
      return;
    }
    if (req.method !== "POST" || path !== "/ask" || req.headers["content-type"]?.split(";", 1)[0] !== "application/json") {
      send(res, siteOrigin, 415, { status: "error", message: "Use a JSON map question." });
      return;
    }
    if (busy) {
      send(res, siteOrigin, 429, { status: "error", message: "A local Qwen request is already running." });
      return;
    }
    let body;
    try { body = await boundedBody(req); } catch {
      send(res, siteOrigin, 413, { status: "error", message: "The map question is invalid or too large." });
      return;
    }
    if (!isRecord(body) || Object.keys(body).some((key) => key !== "question" && key !== "context")
      || typeof body.question !== "string" || !body.question.trim() || body.question.length > 1200
      || !validContext(body.context)) {
      send(res, siteOrigin, 400, { status: "error", message: "The map question has an invalid shape." });
      return;
    }
    busy = true;
    try {
      const upstream = await fetcher(`${ollamaUrl}/api/chat`, {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({
          model,
          stream: false,
          messages: [
            { role: "system", content: "You are the Qwen companion for Kansas Frontier Matrix. Use only the supplied map context. Do not invent sources, current conditions, protected coordinates, releases, or safety guidance. Treat all model output as interpretation, never as evidence or authority." },
            { role: "user", content: promptFor(body.question.trim(), body.context) },
          ],
          options: { temperature: 0.2 },
        }),
        redirect: "error",
        signal: AbortSignal.timeout(90_000),
      });
      if (!upstream.ok) throw new Error("OLLAMA_ERROR");
      const payload = await boundedJson(upstream, MAX_REPLY_BYTES);
      const answer = payload?.message?.content;
      if (typeof answer !== "string" || !answer.trim()) throw new Error("EMPTY_ANSWER");
      send(res, siteOrigin, 200, { status: "ok", model, answer: answer.trim() });
    } catch {
      send(res, siteOrigin, 502, { status: "error", message: "Local Qwen could not answer. The map remains available." });
    } finally {
      busy = false;
    }
  });
}

if (process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1]) {
  createLocalQwenBridge().listen(LOCAL_BRIDGE_PORT, "127.0.0.1", () => {
    process.stdout.write("KFM local Qwen bridge listening on loopback\n");
  });
}
