import { buildQwenPrompt, normalizeQwenQuestion, QWEN_SYSTEM_PROMPT, type QwenMapContext } from "../../qwen-context";

export const dynamic = "force-dynamic";

type QwenRequest = {
  question?: unknown;
  context?: unknown;
};

const envValue = (...keys: string[]) => {
  for (const key of keys) {
    const value = process.env[key]?.trim();
    if (value) return value;
  }
  return "";
};

const endpointFor = (base: string) => {
  if (/\/api\/chat\/?$/i.test(base)) return base;
  return `${base.replace(/\/+$/, "")}/api/chat`;
};

export async function POST(request: Request) {
  let body: QwenRequest;
  try {
    body = await request.json() as QwenRequest;
  } catch {
    return Response.json({ status: "error", message: "The Qwen request body was not valid JSON." }, { status: 400 });
  }

  const question = normalizeQwenQuestion(body.question);
  if (!question) {
    return Response.json({ status: "error", message: "Ask a question about the current map view." }, { status: 400 });
  }

  const endpoint = envValue("QWEN_ENDPOINT", "QWEN_OLLAMA_URL", "OLLAMA_BASE_URL");
  if (!endpoint) {
    return Response.json({
      status: "not_configured",
      message: "No Qwen inference endpoint is configured for this Site.",
    }, { status: 503 });
  }

  const model = envValue("QWEN_MODEL", "OLLAMA_MODEL") || "qwen3:8b";
  const apiKey = envValue("QWEN_API_KEY");
  const context = (body.context && typeof body.context === "object" ? body.context : {}) as QwenMapContext;
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 25_000);

  try {
    const upstream = await fetch(endpointFor(endpoint), {
      method: "POST",
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

    const payload = await upstream.json().catch(() => null) as {
      message?: { content?: unknown };
      response?: unknown;
      choices?: Array<{ message?: { content?: unknown } }>;
      error?: unknown;
    } | null;
    if (!upstream.ok) {
      return Response.json({ status: "error", message: typeof payload?.error === "string" ? payload.error : `Qwen endpoint returned HTTP ${upstream.status}.` }, { status: 502 });
    }

    const answer = payload?.message?.content ?? payload?.choices?.[0]?.message?.content ?? payload?.response;
    if (typeof answer !== "string" || !answer.trim()) {
      return Response.json({ status: "error", message: "Qwen returned no readable answer." }, { status: 502 });
    }
    return Response.json({ status: "ok", model, answer: answer.trim() });
  } catch (error) {
    const message = error instanceof DOMException && error.name === "AbortError"
      ? "Qwen took too long to respond."
      : "The Qwen bridge could not reach its configured endpoint.";
    return Response.json({ status: "error", message }, { status: 502 });
  } finally {
    clearTimeout(timeout);
  }
}
