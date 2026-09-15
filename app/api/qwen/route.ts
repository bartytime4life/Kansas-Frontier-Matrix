import { buildQwenPrompt, normalizeQwenQuestion, QWEN_SYSTEM_PROMPT, type QwenMapContext } from "../../qwen-context";
import { JsonLimitError, readBoundedJson } from "../../bounded-json";

export const dynamic = "force-dynamic";

const MAX_REQUEST_BYTES = 32 * 1024;
const MAX_REPLY_BYTES = 64 * 1024;
const isRecord = (value: unknown): value is Record<string, unknown> =>
  value !== null && typeof value === "object" && !Array.isArray(value);
const reply = (body: Record<string, unknown>, status: number) =>
  Response.json(body, { status, headers: { "cache-control": "no-store", "x-content-type-options": "nosniff" } });

const envValue = (...keys: string[]) => {
  for (const key of keys) {
    const value = process.env[key]?.trim();
    if (value) return value;
  }
  return "";
};

const endpointFor = (base: string) => {
  const url = new URL(base);
  const localHttp = url.protocol === "http:" && ["localhost", "127.0.0.1", "[::1]"].includes(url.hostname);
  if ((url.protocol !== "https:" && !localHttp) || url.username || url.password || url.search || url.hash) {
    throw new Error("Invalid configured endpoint.");
  }
  if (!/\/api\/chat\/?$/i.test(url.pathname)) url.pathname = `${url.pathname.replace(/\/+$/, "")}/api/chat`;
  return url.toString();
};

export async function POST(request: Request) {
  const origin = request.headers.get("origin");
  if (origin && origin !== new URL(request.url).origin) {
    return reply({ status: "error", message: "The Qwen request must come from this Site." }, 403);
  }
  if (request.headers.get("content-type")?.split(";", 1)[0].trim().toLowerCase() !== "application/json") {
    return reply({ status: "error", message: "The Qwen request must use JSON." }, 415);
  }
  let body: unknown;
  try {
    body = await readBoundedJson(request, MAX_REQUEST_BYTES);
  } catch (error) {
    return reply({ status: "error", message: error instanceof JsonLimitError
      ? "The map context is too large. Reduce the visible layers and try again."
      : "The Qwen request body was not valid JSON." }, error instanceof JsonLimitError ? 413 : 400);
  }
  if (!isRecord(body) || Object.keys(body).some((key) => key !== "question" && key !== "context")
    || (body.context !== undefined && !isRecord(body.context))) {
    return reply({ status: "error", message: "The Qwen request has an invalid shape." }, 400);
  }

  const question = normalizeQwenQuestion(body.question);
  if (!question || (typeof body.question === "string" && body.question.trim().length > 1200)) {
    return reply({ status: "error", message: "Ask a map question of 1 to 1200 characters." }, 400);
  }

  const endpoint = envValue("QWEN_ENDPOINT", "QWEN_OLLAMA_URL", "OLLAMA_BASE_URL");
  if (!endpoint) {
    return reply({
      status: "not_configured",
      message: "No Qwen inference endpoint is configured for this Site.",
    }, 503);
  }

  let target: string;
  try { target = endpointFor(endpoint); } catch {
    return reply({ status: "error", message: "The configured Qwen endpoint is not supported." }, 503);
  }

  const model = envValue("QWEN_MODEL", "OLLAMA_MODEL") || "qwen3:8b";
  const apiKey = envValue("QWEN_API_KEY");
  const context = (body.context ?? {}) as QwenMapContext;
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 25_000);

  try {
    const upstream = await fetch(target, {
      method: "POST",
      redirect: "error",
      cache: "no-store",
      headers: {
        "content-type": "application/json",
        ...(apiKey ? { authorization: `Bearer ${apiKey}` } : {}),
      },
      body: JSON.stringify({
        model,
        stream: false,
        messages: [
          { role: "system", content: QWEN_SYSTEM_PROMPT },
          { role: "user", content: buildQwenPrompt(question, context) },
        ],
        options: { temperature: 0.2 },
      }),
      signal: controller.signal,
    });

    if (!upstream.ok) {
      void upstream.body?.cancel().catch(() => undefined);
      return reply({ status: "error", message: `Qwen endpoint returned HTTP ${upstream.status}.` }, 502);
    }
    const payload = await readBoundedJson(upstream, MAX_REPLY_BYTES) as {
      message?: { content?: unknown };
      response?: unknown;
      choices?: Array<{ message?: { content?: unknown } }>;
      error?: unknown;
    } | null;
    const answer = payload?.message?.content ?? payload?.choices?.[0]?.message?.content ?? payload?.response;
    if (typeof answer !== "string" || !answer.trim()) {
      return reply({ status: "error", message: "Qwen returned no readable answer." }, 502);
    }
    return reply({ status: "ok", model, answer: answer.trim() }, 200);
  } catch (error) {
    const message = error instanceof DOMException && error.name === "AbortError"
      ? "Qwen took too long to respond."
      : "The Qwen bridge could not reach its configured endpoint.";
    return reply({ status: "error", message }, 502);
  } finally {
    clearTimeout(timeout);
  }
}
