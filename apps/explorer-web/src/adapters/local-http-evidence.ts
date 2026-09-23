import {
  MAP_FEATURE_SELECTION_PROFILE,
  type MapFeatureSelection,
} from "@kfm/maplibre";
import { parseEvidenceDrawerProjection } from "./GovernedClient";
import { mapRuntimeSelectionToEvidenceRequest } from "./map_runtime_evidence_adapter";
import {
  resolveMapFeatureEvidence,
  type MapEvidenceResolution,
} from "../features/map_runtime";

export const LOCAL_EVIDENCE_SCENARIOS = Object.freeze([
  "current", "stale", "withdrawn", "missing", "denied", "error",
] as const);
export type LocalEvidenceScenario = typeof LOCAL_EVIDENCE_SCENARIOS[number];
export type LocalEvidenceResolver = (
  selection: MapFeatureSelection,
  signal: AbortSignal,
) => Promise<unknown>;

const ENDPOINT = "/__local__/evidence";
const MAX_RESPONSE_BYTES = 16_384;
const MAX_RESPONSE_CHUNKS = 256;
const REQUEST_TIMEOUT_MS = 5_000;
const SUPPORTED_LAYERS = new Set(["layer:kansas-frame", "layer:county-locators"]);

/** Fixed synthetic request identities, never arbitrary feature properties or URLs. */
export function localEvidenceSelection(
  layerId: string,
  scenario: LocalEvidenceScenario,
): MapFeatureSelection | null {
  if (!SUPPORTED_LAYERS.has(layerId) || !LOCAL_EVIDENCE_SCENARIOS.includes(scenario)) return null;
  const slug = layerId.slice("layer:".length);
  const evidenceRef = `kfm:evidence:site-local:${slug}`;
  const historical = scenario === "stale" || scenario === "withdrawn";
  return Object.freeze({
    profile: MAP_FEATURE_SELECTION_PROFILE,
    selectionId: `selection:local-http:${slug}:${scenario}`,
    layerId,
    featureId: `feature:local-http:${slug}`,
    evidenceRefs: Object.freeze(historical ? [] : [evidenceRef]),
    ...(historical ? { historyEvidenceRefs: Object.freeze([evidenceRef]) } : {}),
  });
}

function allowedSelection(selection: MapFeatureSelection): boolean {
  const scenario = selection.selectionId.split(":").at(-1) as LocalEvidenceScenario;
  const expected = localEvidenceSelection(selection.layerId, scenario);
  return expected !== null &&
    JSON.stringify(mapRuntimeSelectionToEvidenceRequest(selection)) ===
      JSON.stringify(mapRuntimeSelectionToEvidenceRequest(expected));
}

/** Reject ambiguous duplicate keys before JSON.parse applies last-key-wins. */
function parseUniqueJson(source: string): unknown {
  let offset = 0;
  let values = 0;
  const invalid = (): never => { throw new Error("Invalid local evidence JSON"); };
  const whitespace = (): void => {
    while (offset < source.length && /[\x20\t\r\n]/.test(source[offset])) offset += 1;
  };
  const string = (): string => {
    whitespace();
    const token = /^"(?:[^"\\\x00-\x1f]|\\(?:["\\/bfnrt]|u[0-9a-fA-F]{4}))*"/.exec(source.slice(offset));
    if (!token) return invalid();
    offset += token[0].length;
    return JSON.parse(token[0]) as string;
  };
  const value = (depth: number): void => {
    if (depth > 8 || ++values > 512) invalid();
    whitespace();
    const start = source[offset];
    if (start === "{") {
      offset += 1;
      whitespace();
      const keys = new Set<string>();
      if (source[offset] === "}") { offset += 1; return; }
      while (true) {
        const key = string();
        if (keys.has(key)) invalid();
        keys.add(key);
        whitespace();
        if (source[offset++] !== ":") invalid();
        value(depth + 1);
        whitespace();
        const separator = source[offset++];
        if (separator === "}") return;
        if (separator !== ",") invalid();
      }
    }
    if (start === "[") {
      offset += 1;
      whitespace();
      if (source[offset] === "]") { offset += 1; return; }
      while (true) {
        value(depth + 1);
        whitespace();
        const separator = source[offset++];
        if (separator === "]") return;
        if (separator !== ",") invalid();
      }
    }
    if (start === '"') { string(); return; }
    const token = /^(?:true|false|null|-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?)/.exec(source.slice(offset));
    if (!token) invalid();
    offset += token![0].length;
  };
  value(0);
  whitespace();
  if (offset !== source.length) invalid();
  return JSON.parse(source) as unknown;
}

/**
 * Explicit local development transport. No endpoint override, credentials,
 * public API activation, inline success fallback, or lifecycle-store access.
 * The total deadline covers fetch and streamed reads, even when a transport
 * ignores cancellation. The existing strict projection parser owns semantics.
 */
export const fetchLocalEvidenceProjection: LocalEvidenceResolver = async (selection, signal) => {
  if (!allowedSelection(selection) || signal.aborted) throw new Error("Local evidence request unavailable");
  const controller = new AbortController();
  let reader: ReadableStreamDefaultReader<Uint8Array> | undefined;
  let rejectStopped: (error: Error) => void = () => undefined;
  const stopped = new Promise<never>((_, reject) => { rejectStopped = reject; });
  const stop = (): void => {
    if (controller.signal.aborted) return;
    controller.abort();
    rejectStopped(new Error("Local evidence request stopped"));
  };
  signal.addEventListener("abort", stop, { once: true });
  const timeout = setTimeout(stop, REQUEST_TIMEOUT_MS);

  const operation = async (): Promise<unknown> => {
    const response = await fetch(ENDPOINT, {
      method: "POST",
      mode: "same-origin",
      credentials: "omit",
      redirect: "error",
      cache: "no-store",
      referrerPolicy: "no-referrer",
      headers: { Accept: "application/json", "Content-Type": "application/json" },
      body: JSON.stringify(mapRuntimeSelectionToEvidenceRequest(selection)),
      signal: controller.signal,
    });
    if (controller.signal.aborted) throw new Error("Local evidence request stopped");
    if (response.redirected || !["basic", "default"].includes(response.type) ||
        ![200, 400, 403, 404, 405, 411, 413, 415, 500, 503].includes(response.status) ||
        response.headers.get("x-kfm-local-fixture") !== "synthetic-only" ||
        !/^application\/json(?:\s*;\s*charset=(?:utf-8|"utf-8"))?\s*$/i.test(response.headers.get("content-type") ?? "")) {
      throw new Error("Unsupported local evidence response");
    }
    if (response.url) {
      const actual = new URL(response.url);
      if (actual.origin !== window.location.origin || actual.pathname !== ENDPOINT || actual.search || actual.hash) {
        throw new Error("Unexpected local evidence response location");
      }
    }
    const length = response.headers.get("content-length");
    if (length !== null && (!/^\d+$/.test(length) || Number(length) > MAX_RESPONSE_BYTES)) {
      throw new Error("Local evidence response exceeds bounds");
    }
    if (response.body === null) throw new Error("Missing local evidence body");
    reader = response.body.getReader();
    const buffer = new Uint8Array(MAX_RESPONSE_BYTES);
    let size = 0;
    let chunks = 0;
    while (true) {
      const chunk = await reader.read();
      if (controller.signal.aborted) throw new Error("Local evidence request stopped");
      if (chunk.done) break;
      chunks += 1;
      if (!(chunk.value instanceof Uint8Array) || chunks > MAX_RESPONSE_CHUNKS || size + chunk.value.byteLength > MAX_RESPONSE_BYTES) {
        throw new Error("Local evidence response exceeds bounds");
      }
      buffer.set(chunk.value, size);
      size += chunk.value.byteLength;
    }
    if (length !== null && Number(length) !== size) throw new Error("Local evidence response length mismatch");
    const value = parseUniqueJson(new TextDecoder("utf-8", { fatal: true }).decode(buffer.subarray(0, size)));
    const parsed = parseEvidenceDrawerProjection(value);
    if (!parsed.ok || (response.status !== 200 && parsed.payload.outcome !== "ERROR" &&
        !(response.status === 404 && parsed.payload.outcome === "ABSTAIN"))) {
      throw new Error("Invalid local evidence response");
    }
    const expectedId = `kfm:ui:evidence-drawer:${selection.selectionId.slice("selection:".length)}`;
    if (parsed.payload.outcome !== "ERROR" && response.status === 200 && parsed.payload.id !== expectedId) {
      throw new Error("Local evidence response identity mismatch");
    }
    return value;
  };
  try {
    return await Promise.race([operation(), stopped]);
  } finally {
    clearTimeout(timeout);
    signal.removeEventListener("abort", stop);
    controller.abort();
    if (reader) {
      void reader.cancel().catch(() => undefined);
      try { reader.releaseLock(); } catch { /* A cancelled pending read retains its lock. */ }
    }
  }
};

/** Selection supersession and context invalidation also defeat late ignored aborts. */
export function createLocalEvidenceSession(
  resolver: LocalEvidenceResolver,
  consume: (resolution: MapEvidenceResolution) => void,
): Readonly<{
  select: (selection: MapFeatureSelection) => Promise<void>;
  invalidate: () => void;
  destroy: () => void;
}> {
  let generation = 0;
  let active = true;
  let request: AbortController | null = null;
  const invalidate = (): void => {
    generation += 1;
    request?.abort();
    request = null;
  };
  return Object.freeze({
    async select(selection: MapFeatureSelection): Promise<void> {
      if (!active) return;
      invalidate();
      const version = generation;
      const controller = new AbortController();
      request = controller;
      const result = await resolveMapFeatureEvidence(
        mapRuntimeSelectionToEvidenceRequest(selection),
        (scope) => resolver(scope, controller.signal),
      );
      if (!active || version !== generation || controller.signal.aborted) return;
      request = null;
      consume(result);
    },
    invalidate,
    destroy(): void {
      active = false;
      invalidate();
    },
  });
}
