import { EVIDENCE_DRAWER_PROJECTION_PROFILE } from "./GovernedClient";

const MAX_RESPONSE_BYTES = 16_384;
const MAX_RESPONSE_CHUNKS = 256;
const REQUEST_TIMEOUT_MS = 5_000;
const ENVELOPE_FIELDS = new Set([
  "id", "spec_hash", "version", "issued_at", "outcome", "reason_code",
  "evidence_refs", "policy_state", "freshness", "correction_state",
]);
const OUTCOME_REASONS: Readonly<Record<string, readonly string[]>> = {
  ABSTAIN: ["NOT_IMPLEMENTED", "UNSUPPORTED_SCOPE", "MISSING_EVIDENCE", "SOURCE_STALE", "REQUEST_CANCELLED"],
  DENY: ["POLICY_DENIED"],
  ERROR: ["INVALID_REQUEST", "DEPENDENCY_UNAVAILABLE", "REQUEST_TIMEOUT", "INVALID_RESPONSE", "SAFE_RUNTIME_ERROR"],
};

type NegativeKind = "unavailable" | "missing" | "stale" | "denied" | "cancelled" | "error";
export type GovernedApiNegativeProjection = Readonly<Record<string, unknown>>;

function projection(kind: NegativeKind): GovernedApiNegativeProjection {
  const outcome = kind === "error" ? "ERROR" : kind === "denied" ? "DENY" : "ABSTAIN";
  const reason = kind === "error" ? "UPSTREAM_ERROR" : kind === "denied" ? "POLICY_DENIED" : kind === "stale" ? "STALE_EVIDENCE" : "MISSING_EVIDENCE";
  const summaries: Record<NegativeKind, string> = {
    unavailable: "The governed API is reachable but does not yet resolve selected evidence. No evidence claim is available.",
    missing: "The governed API returned no supported evidence. No evidence claim is available.",
    stale: "The governed API reported stale support. No current evidence claim is available.",
    denied: "The governed API denied evidence access. No evidence or history is displayed.",
    cancelled: "The evidence availability request was cancelled. No evidence claim is available.",
    error: "The evidence availability request could not be safely completed. No evidence or upstream details are displayed.",
  };
  return Object.freeze({
    profile: EVIDENCE_DRAWER_PROJECTION_PROFILE,
    id: "kfm:drawer:governed-api:availability",
    outcome,
    reason_code: reason,
    title: "Governed API evidence availability",
    summary: summaries[kind],
    evidence_refs: Object.freeze([]),
    citations: Object.freeze([]),
    limitations: Object.freeze([
      "Availability response only: this request sends no feature, candidate, evidence, or policy identifiers.",
      "This negative-only adapter cannot establish evidence resolution, rights, review, release, correction, rollback, or publication authority.",
    ]),
    trust_state: Object.freeze({
      source_role: "context", policy: outcome, review: "PENDING", release: "UNRELEASED",
      freshness: kind === "stale" ? "STALE" : "UNKNOWN", correction: "NONE",
    }),
    history: Object.freeze({ negative_outcomes: Object.freeze([]), corrections: Object.freeze([]) }),
  });
}

/** The supported wire profile is flat: ten fields, strings and an empty list.
 * Scan that grammar before interpretation to reject duplicate keys, nested
 * payloads and trailing JSON without recursively parsing attacker input.
 */
function parseFlatEnvelope(text: string): Record<string, string | never[]> | null {
  let offset = 0;
  const whitespace = () => { while (/[\x20\t\r\n]/.test(text[offset] ?? "!") && offset < text.length) offset += 1; };
  const token = (value: string) => {
    whitespace();
    if (text[offset] !== value) return false;
    offset += 1;
    return true;
  };
  const string = (): string | null => {
    whitespace();
    const match = /^"(?:[^"\\\x00-\x1f]|\\(?:["\\/bfnrt]|u[0-9a-fA-F]{4}))*"/.exec(text.slice(offset));
    if (!match) return null;
    offset += match[0].length;
    return JSON.parse(match[0]) as string;
  };
  const result: Record<string, string | never[]> = Object.create(null);
  if (!token("{")) return null;
  for (let count = 0; count < ENVELOPE_FIELDS.size; count += 1) {
    if (count > 0 && !token(",")) return null;
    const key = string();
    if (key === null || !ENVELOPE_FIELDS.has(key) || Object.hasOwn(result, key) || !token(":")) return null;
    if (key === "evidence_refs") {
      if (!token("[") || !token("]")) return null;
      result[key] = [];
    } else {
      const value = string();
      if (value === null) return null;
      result[key] = value;
    }
  }
  if (!token("}")) return null;
  whitespace();
  return offset === text.length ? result : null;
}

function validTimestamp(value: string): boolean {
  const parts = /^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})(?:\.\d{1,6})?(?:Z|([+-])(\d{2}):(\d{2}))$/.exec(value);
  if (!parts) return false;
  const [year, month, day, hour, minute, second] = parts.slice(1, 7).map(Number);
  const leap = year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0);
  const days = [31, leap ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  return year >= 1 && month >= 1 && month <= 12 && day >= 1 && day <= days[month - 1]
    && hour <= 23 && minute <= 59 && second <= 59
    && (parts[7] === undefined || (Number(parts[8]) <= 23 && Number(parts[9]) <= 59));
}

function classifyEnvelope(text: string, status: number): NegativeKind {
  const value = parseFlatEnvelope(text);
  if (!value) throw new Error("Invalid negative envelope");
  const field = (key: string) => value[key] as string;
  const outcome = field("outcome");
  const reason = field("reason_code");
  if (!/^[a-z][a-z0-9_:.-]{0,255}$/.test(field("id"))
      || !/^sha256:[a-f0-9]{64}$/.test(field("spec_hash"))
      || !/^[a-z0-9][a-z0-9_.-]{0,63}$/.test(field("version"))
      || !validTimestamp(field("issued_at"))
      || !OUTCOME_REASONS[outcome]?.includes(reason)
      || ["policy_state", "freshness", "correction_state"].some((key) => !/^[a-z][a-z0-9_-]{0,63}$/.test(field(key)))) {
    throw new Error("Invalid negative envelope");
  }
  // Mirror the existing WSGI transport. Caught cancellation is the one
  // ABSTAIN failure that the synchronous operation guard transports as 500.
  const compatible = outcome === "ERROR"
    ? status === 500 || ((status === 404 || status === 405) && reason === "SAFE_RUNTIME_ERROR")
    : status === 200 || (status === 500 && outcome === "ABSTAIN" && reason === "REQUEST_CANCELLED");
  if (!compatible) throw new Error("Incompatible negative response status");
  if (outcome === "ERROR") return "error";
  if (outcome === "DENY") return "denied";
  if (reason === "NOT_IMPLEMENTED") return "unavailable";
  if (reason === "SOURCE_STALE") return "stale";
  if (reason === "REQUEST_CANCELLED") return "cancelled";
  return "missing";
}

/**
 * Read only the existing same-origin /evidence scaffold's negative envelope.
 * There is no endpoint override, selection query, credential, positive-data
 * fallback, retry or operational activation. A total deadline races fetch AND
 * body reads, even when a transport ignores AbortSignal. Cleanup never waits
 * for a stalled reader cancellation.
 */
export async function fetchGovernedApiNegativeProjection(
  options: Readonly<{ signal?: AbortSignal }> = {},
): Promise<GovernedApiNegativeProjection> {
  if (options.signal?.aborted) return projection("cancelled");
  const controller = new AbortController();
  let reader: ReadableStreamDefaultReader<Uint8Array> | undefined;
  let stopKind: "cancelled" | "error" | undefined;
  let rejectStopped: (error: Error) => void = () => undefined;
  const stopped = new Promise<never>((_, reject) => { rejectStopped = reject; });
  const stop = (kind: "cancelled" | "error") => {
    if (stopKind !== undefined) return;
    stopKind = kind;
    controller.abort();
    rejectStopped(new Error("Evidence availability request stopped"));
  };
  const abort = () => stop("cancelled");
  const timeout = setTimeout(() => stop("error"), REQUEST_TIMEOUT_MS);
  options.signal?.addEventListener("abort", abort, { once: true });
  const operation = async (): Promise<GovernedApiNegativeProjection> => {
    const response = await fetch("/evidence", {
      method: "GET", mode: "same-origin", credentials: "omit", redirect: "error",
      cache: "no-store", referrerPolicy: "no-referrer", headers: { Accept: "application/json" },
      signal: controller.signal,
    });
    // A transport that ignores cancellation must not begin consuming a late body.
    if (controller.signal.aborted) throw new Error("Request stopped");
    if (response.redirected || !["basic", "default"].includes(response.type)
        || ![200, 404, 405, 500].includes(response.status)
        || !/^application\/json(?:\s*;\s*charset=(?:utf-8|"utf-8"))?\s*$/i.test(response.headers.get("content-type") ?? "")) {
      throw new Error("Unsupported evidence response");
    }
    if (response.url) {
      if (typeof location === "undefined" || response.url !== new URL("/evidence", location.href).href) {
        throw new Error("Unexpected evidence response URL");
      }
    }
    const lengthHeader = response.headers.get("content-length");
    const declaredLength = lengthHeader === null ? null : Number(lengthHeader);
    if (lengthHeader !== null && (!/^[0-9]{1,5}$/.test(lengthHeader) || declaredLength! < 1 || declaredLength! > MAX_RESPONSE_BYTES)) {
      throw new Error("Unsupported evidence response size");
    }
    if (!response.body) throw new Error("Missing evidence response body");
    reader = response.body.getReader();
    const buffer = new Uint8Array(MAX_RESPONSE_BYTES);
    let size = 0;
    let chunks = 0;
    while (true) {
      const item = await reader.read();
      if (controller.signal.aborted) throw new Error("Request stopped");
      if (item.done) break;
      chunks += 1;
      if (chunks > MAX_RESPONSE_CHUNKS || !(item.value instanceof Uint8Array) || size + item.value.byteLength > MAX_RESPONSE_BYTES) {
        throw new Error("Evidence response exceeds bounds");
      }
      buffer.set(item.value, size);
      size += item.value.byteLength;
    }
    if (declaredLength !== null && declaredLength !== size) throw new Error("Evidence response length mismatch");
    const text = new TextDecoder("utf-8", { fatal: true }).decode(buffer.subarray(0, size));
    return projection(classifyEnvelope(text, response.status));
  };
  try {
    return await Promise.race([operation(), stopped]);
  } catch {
    return projection(stopKind ?? "error");
  } finally {
    clearTimeout(timeout);
    options.signal?.removeEventListener("abort", abort);
    controller.abort();
    if (reader) {
      void reader.cancel().catch(() => undefined);
      try { reader.releaseLock(); } catch { /* A pending cancelled read still owns its lock. */ }
    }
  }
}
