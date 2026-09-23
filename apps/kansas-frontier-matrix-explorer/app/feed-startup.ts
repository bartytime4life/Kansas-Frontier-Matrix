/** Presentation only. Callers must verify payload, digest, rights and scope before
 * supplying artifacts. This selector performs no I/O or source admission. */
export type FeedPhase = "idle" | "loading" | "ready" | "empty" | "partial" | "error";
export type RendererState = "unverified" | "loading" | "rendered" | "error" | "unavailable";
export type DataKind = "live" | "snapshot" | "historical" | "synthetic";
export type Artifact = Readonly<{
  id: string; sourceId: string; scopeKey: string; kind: DataKind;
  dataRole: "observation" | "forecast" | "model" | "reference" | "synthetic";
  sha256: string; validation: "passed" | "failed"; displayAllowed: boolean;
  dataTime: string; retrievedAt: string | null;
  freshnessAnchor: string | null; validUntil: string | null;
  featureCount: number;
}>;
export type StartupInput = Readonly<{
  now: string; sourceId: string; scopeKey: string;
  direction: "auto" | "live" | "history" | "demo";
  enabled: boolean; access: "allowed" | "held" | "restricted" | "denied";
  timeSupported: boolean; zoomSupported: boolean;
  phase: FeedPhase; failureCode?: string;
  live?: Artifact; history?: Artifact; snapshots?: readonly Artifact[]; demo?: Artifact;
  rendererState?: RendererState;
  renderedArtifactId?: string; renderedScopeKey?: string;
}>;
export type Display = "NONE" | "LIVE" | "LIVE_EMPTY" | "LIVE_PARTIAL" | "LIVE_STALE"
  | "SNAPSHOT" | "STALE_SNAPSHOT" | "HISTORICAL" | "SYNTHETIC_DEMO";
export type StartupDecision = Readonly<{
  display: Display; artifact: Artifact | null; phase: FeedPhase;
  reason: string; connectionFailure: string | null;
  liveAvailable: boolean; renderedLive: boolean; rendererState: RendererState;
  disclosure: string;
}>;
const codes = new Set(["ROUTE_MISSING", "AUTH_REQUIRED", "TIMEOUT", "NETWORK_ERROR",
  "INVALID_RESPONSE", "UPSTREAM_ERROR", "INVALID_LIVE_RESULT",
  "API_NOT_CONFIGURED", "RATE_LIMITED", "UNEXPECTED_MEDIA_TYPE"]);
const time = (value: string | null): number => {
  if (typeof value !== "string" || !/^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d\.\d{3}Z$/.test(value)) return NaN;
  const n = Date.parse(value);
  return Number.isFinite(n) && new Date(n).toISOString() === value ? n : NaN;
};
const safeId = (value: string) => typeof value === "string" && /^[A-Za-z0-9:._-]{1,160}$/.test(value);
const structurallyEligible = (a: Artifact | undefined, now: number): a is Artifact => {
  if (!a || !safeId(a.id) || !safeId(a.sourceId) || !safeId(a.scopeKey)
    || a.validation !== "passed" || a.displayAllowed !== true
    || !/^[a-f0-9]{64}$/.test(a.sha256)
    || !Number.isSafeInteger(a.featureCount) || a.featureCount < 0 || a.featureCount > 100_000
    || !Number.isFinite(time(a.dataTime))) return false;
  if (a.kind === "synthetic") return a.dataRole === "synthetic" && a.sourceId === "synthetic:starter"
    && a.id.startsWith("demo:") && a.retrievedAt === null
    && a.freshnessAnchor === null && a.validUntil === null;
  if (!["observation", "forecast", "model", "reference"].includes(a.dataRole)) return false;
  if (!Number.isFinite(time(a.retrievedAt)) || time(a.retrievedAt) > now) return false;
  if (a.kind === "historical") return time(a.dataTime) <= now;
  const anchor = time(a.freshnessAnchor), expiry = time(a.validUntil);
  return (a.kind === "live" || a.kind === "snapshot")
    && Number.isFinite(anchor) && anchor <= time(a.retrievedAt)
    && Number.isFinite(expiry) && expiry >= anchor;
};

/** Scope keys bind source/product/AOI/time semantics; they are opaque identifiers,
 * never URLs or raw coordinates. An expired artifact is usable only as stale. */
export function resolveFeedStartup(input: StartupInput): StartupDecision {
  const now = time(input.now);
  let phase = input.phase;
  let failure = phase === "error"
    ? (codes.has(input.failureCode ?? "") ? input.failureCode! : "UPSTREAM_ERROR") : null;
  const result = (display: Display, artifact: Artifact | null, reason: string): StartupDecision => {
    const liveAvailable = display === "LIVE" || display === "LIVE_EMPTY";
    return Object.freeze({ display, artifact, phase, reason, connectionFailure: failure,
      liveAvailable, rendererState: input.rendererState ?? "unverified",
      renderedLive: input.rendererState === "rendered" && liveAvailable && artifact !== null && artifact.featureCount > 0
        && input.renderedArtifactId === artifact.id && input.renderedScopeKey === artifact.scopeKey,
      disclosure: display === "SYNTHETIC_DEMO"
        ? "SYNTHETIC DEMO — not observations, not live, not a hazard assessment."
        : display === "NONE" ? "No eligible display data; this is not an all-clear."
        : `${display} / ${artifact!.dataRole} — data time ${artifact!.dataTime}; retrieved ${artifact!.retrievedAt}. Not an all-clear.`,
    });
  };
  if (!Number.isFinite(now)) return result("NONE", null, "INVALID_CLOCK");
  if (!safeId(input.sourceId) || !safeId(input.scopeKey)) return result("NONE", null, "INVALID_SCOPE");
  if (input.access !== "allowed") return result("NONE", null, "ACCESS_BLOCKED");
  if (!input.enabled) return result("NONE", null, "DISABLED");
  if (!input.timeSupported) return result("NONE", null, "OUTSIDE_SELECTED_TIME");
  if (!input.zoomSupported) return result("NONE", null, "OUTSIDE_SUPPORTED_ZOOM");
  const matching = (a: Artifact | undefined, kind: DataKind): a is Artifact =>
    structurallyEligible(a, now) && a.kind === kind
      && a.sourceId === input.sourceId && a.scopeKey === input.scopeKey;
  const demo = () => structurallyEligible(input.demo, now) && input.demo.kind === "synthetic"
    ? result("SYNTHETIC_DEMO", input.demo, "SEPARATE_DEMO_BASELINE")
    : result("NONE", null, "NO_ELIGIBLE_BASELINE");
  if (input.direction === "demo") return demo();
  if (input.direction === "history") return matching(input.history, "historical")
    ? result("HISTORICAL", input.history, "EXPLICIT_HISTORY")
    : result("NONE", null, "SELECTED_HISTORY_UNAVAILABLE");
  if (!["auto", "live"].includes(input.direction)) return result("NONE", null, "INVALID_DIRECTION");
  if (["ready", "empty", "partial"].includes(phase)) {
    const a = input.live;
    if (matching(a, "live") && (phase !== "empty" || a.featureCount === 0)
      && (phase !== "ready" || a.featureCount > 0)) {
      if (time(a.validUntil) < now) return result("LIVE_STALE", a, "EXPIRED_SOURCE_FRESHNESS");
      return result(phase === "empty" ? "LIVE_EMPTY" : phase === "partial" ? "LIVE_PARTIAL" : "LIVE",
        a, phase === "empty" ? "VALID_EMPTY_NOT_ALL_CLEAR" : phase === "partial" ? "INCOMPLETE_RESULT" : "CURRENT_RESULT");
    }
    phase = "error"; failure = "INVALID_LIVE_RESULT";
  }
  // Explicit live/history directions never silently become a different data mode.
  if (input.direction === "live") return result("NONE", null, "SELECTED_LIVE_UNAVAILABLE");
  if ((input.snapshots?.length ?? 0) > 32) return result("NONE", null, "SNAPSHOT_LIMIT");
  const snapshots = (input.snapshots ?? []).filter((a) => matching(a, "snapshot"));
  snapshots.sort((a, b) => Number(time(b.validUntil) >= now) - Number(time(a.validUntil) >= now)
    || time(b.freshnessAnchor) - time(a.freshnessAnchor) || (a.id < b.id ? -1 : a.id > b.id ? 1 : 0));
  if (snapshots.length) {
    const a = snapshots[0];
    return result(time(a.validUntil) >= now ? "SNAPSHOT" : "STALE_SNAPSHOT", a, "LAST_KNOWN_GOOD_NOT_LIVE");
  }
  return demo();
}
