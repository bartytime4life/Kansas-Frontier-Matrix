import { useCallback, useEffect, useRef, useState } from "react";
import type { FeatureCollection } from "geojson";
import { readBoundedJson } from "./bounded-json";

/**
 * Reviewed snapshots from the site's own database: hourly USGS streamflow, NWS
 * alert and USGS earthquake captures that the publishing pipeline normalized, signed and
 * committed to MySQL (server/pipeline-*.mjs), read through /api/curated. They
 * are approved context releases, not admitted evidence, and each keeps its own
 * capture time.
 */
export type ReviewedSourceId = "usgs-streamflow" | "nws-alerts" | "usgs-earthquakes";
export const REVIEWED_SOURCE_BY_TOPIC: Readonly<Record<string, ReviewedSourceId>> = Object.freeze({ water: "usgs-streamflow", weather: "nws-alerts", disaster: "nws-alerts", geology: "usgs-earthquakes" });
export const REVIEWED_SOURCE_LABEL: Readonly<Record<ReviewedSourceId, string>> = Object.freeze({ "usgs-streamflow": "USGS discharge", "nws-alerts": "NWS alerts", "usgs-earthquakes": "USGS earthquake" });

export type ReviewedRelease = Readonly<{ releaseId: string; publishedAt: string }>;
export type ReviewedProduct = Readonly<{
  state: "available" | "partial" | "empty"; sourceId: ReviewedSourceId; releaseId: string;
  retrievedAt: string; bucketAt: string; approvalExpiresAt: string; freshness: string; measurementFreshness: string;
  limitation: string; data: FeatureCollection;
}>;

/** Why nothing is shown, in words, for each reason the release API gives. */
export const REVIEWED_REASONS: Readonly<Record<string, string>> = Object.freeze({
  PIPELINE_NOT_CONFIGURED: "Reviewed snapshots are not switched on for this site yet.",
  NO_APPROVED_RELEASE: "No approved snapshot has been published yet.",
  RELEASE_STORE_UNAVAILABLE: "The site database is unavailable right now.",
  HISTORY_UNAVAILABLE: "The site database is unavailable right now.",
  APPROVAL_EXPIRED: "This snapshot's publication approval has expired.",
});
const releaseIdPattern = /^[a-f0-9]{64}$/;
const isTime = (value: unknown): value is string => typeof value === "string" && Number.isFinite(Date.parse(value));

export function parseReviewedHistory(value: unknown): { items: ReviewedRelease[]; reason: string | null } {
  const record = value as { items?: unknown; state?: unknown; reason?: unknown } | null;
  if (!record || typeof record !== "object") return { items: [], reason: "RELEASE_STORE_UNAVAILABLE" };
  const items = Array.isArray(record.items) ? record.items.filter((item): item is ReviewedRelease =>
    typeof item?.releaseId === "string" && releaseIdPattern.test(item.releaseId) && isTime(item.publishedAt)) : [];
  // Oldest first, so the scrubber runs forward in time.
  items.sort((a, b) => Date.parse(a.publishedAt) - Date.parse(b.publishedAt));
  const reason = items.length ? null : record.state === "setup-pending" ? "PIPELINE_NOT_CONFIGURED" : typeof record.reason === "string" ? record.reason : "NO_APPROVED_RELEASE";
  return { items, reason };
}

/** The release read, checked as /curated checks it; anything else is withheld. */
export function parseReviewedProduct(value: unknown, sourceId: ReviewedSourceId, now = Date.now()): ReviewedProduct | { withheld: string } {
  const p = value as Record<string, unknown> | null;
  if (!p || typeof p !== "object") return { withheld: "RELEASE_STORE_UNAVAILABLE" };
  if (!["available", "partial", "empty"].includes(String(p.state))) return { withheld: typeof p.reason === "string" ? p.reason : "NO_APPROVED_RELEASE" };
  const data = p.data as FeatureCollection | undefined;
  if (p.sourceId !== sourceId || p.evidenceRole !== "EXTERNAL_CONTEXT_ONLY" || typeof p.releaseId !== "string" || !releaseIdPattern.test(p.releaseId)
    || !isTime(p.retrievedAt) || !isTime(p.bucketAt) || data?.type !== "FeatureCollection" || !Array.isArray(data.features) || data.features.length > 1000) return { withheld: "RELEASE_STORE_UNAVAILABLE" };
  // A release is shown only while its publication approval holds.
  if (!isTime(p.approvalExpiresAt)) return { withheld: "RELEASE_STORE_UNAVAILABLE" };
  if (Date.parse(p.approvalExpiresAt) <= now) return { withheld: "APPROVAL_EXPIRED" };
  // Expired alert areas leave the display; the release still records them.
  const features = sourceId === "nws-alerts" ? data.features.filter(feature => feature.properties?.expired !== true) : data.features;
  return { state: p.state as ReviewedProduct["state"], sourceId, releaseId: p.releaseId, retrievedAt: p.retrievedAt as string, bucketAt: p.bucketAt as string, approvalExpiresAt: p.approvalExpiresAt,
    freshness: String(p.freshness ?? "unknown"), measurementFreshness: String(p.measurementFreshness ?? "unknown"),
    limitation: typeof p.limitation === "string" ? p.limitation : "", data: { type: "FeatureCollection", features } };
}

export type ReviewedSnapshots = Readonly<{
  on: boolean; setOn: (on: boolean) => void;
  status: "idle" | "loading" | "ready" | "withheld";
  reason: string | null; history: readonly ReviewedRelease[];
  index: number; setIndex: (index: number) => void;
  playing: boolean; setPlaying: (playing: boolean) => void;
  product: ReviewedProduct | null;
}>;
export const REVIEWED_STEP_MS = 1400;
/** How often the release history is read again while snapshots are shown, as /curated revalidates. */
export const REVIEWED_REVALIDATE_MS = 60_000;
const MAX_TIMER_MS = 2 ** 31 - 1;
const NO_RELEASES: readonly ReviewedRelease[] = Object.freeze([]);
const approvalHolds = (product: ReviewedProduct, now: number) => Date.parse(product.approvalExpiresAt) > now;
const sameReleases = (a: readonly ReviewedRelease[], b: readonly ReviewedRelease[]) =>
  a.length === b.length && a.every((release, i) => release.releaseId === b[i].releaseId && release.publishedAt === b[i].publishedAt);

/**
 * Reviewed snapshots for one source: the release history when switched on, the
 * selected release (the newest unless one is picked), and a player that steps
 * forward through the releases. The history is read again every minute, so a
 * release whose approval lapses or is revoked leaves the scrubber; a shown
 * release also leaves the map the moment its own approval expires. Releases
 * are cached by id while their approval holds, so replay does not refetch.
 */
export function useReviewedSnapshots(sourceId: ReviewedSourceId | null, motionAllowed: boolean): ReviewedSnapshots {
  const [on, setOnState] = useState(false);
  // null until the history has been read.
  const [historyState, setHistoryState] = useState<Readonly<{ items: readonly ReviewedRelease[]; reason: string | null }> | null>(null);
  // The picked release; null follows the newest.
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [playing, setPlaying] = useState(false);
  const [product, setProduct] = useState<ReviewedProduct | null>(null);
  const [withheld, setWithheld] = useState<Readonly<{ releaseId: string; reason: string }> | null>(null);
  const [revalidation, setRevalidation] = useState(0);
  const cache = useRef(new Map<string, ReviewedProduct>());
  const reset = () => { setPlaying(false); setProduct(null); setWithheld(null); setHistoryState(null); setSelectedId(null); };
  const setOn = useCallback((next: boolean) => {
    setOnState(next); setPlaying(false);
    if (!next) { setProduct(null); setWithheld(null); setHistoryState(null); setSelectedId(null); }
  }, []);
  // A different source starts over (reset while rendering, not in an effect).
  const [shownSource, setShownSource] = useState(sourceId);
  if (shownSource !== sourceId) { setShownSource(sourceId); setOnState(false); reset(); }
  useEffect(() => { cache.current.clear(); }, [sourceId]);
  useEffect(() => {
    if (!on || !sourceId) return;
    const timer = window.setInterval(() => setRevalidation(count => count + 1), REVIEWED_REVALIDATE_MS);
    return () => window.clearInterval(timer);
  }, [on, sourceId]);
  useEffect(() => {
    if (!on || !sourceId) return;
    const controller = new AbortController();
    void fetch(`/api/curated/${sourceId}/history`, { cache: "no-store", signal: controller.signal })
      .then(response => readBoundedJson(response, 65_536, controller.signal))
      .then(value => {
        const parsed = parseReviewedHistory(value);
        // Releases no longer listed are no longer approved to show.
        for (const releaseId of cache.current.keys()) if (!parsed.items.some(release => release.releaseId === releaseId)) cache.current.delete(releaseId);
        setHistoryState(previous => previous && previous.reason === parsed.reason && sameReleases(previous.items, parsed.items) ? previous : parsed);
      })
      // A failed re-read keeps the history already shown; each release still expires on its own.
      .catch(() => { if (!controller.signal.aborted) setHistoryState(previous => previous?.items.length ? previous : { items: [], reason: "HISTORY_UNAVAILABLE" }); });
    return () => controller.abort();
  }, [on, sourceId, revalidation]);
  const history = historyState?.items ?? NO_RELEASES;
  const picked = selectedId ? history.findIndex(release => release.releaseId === selectedId) : -1;
  const index = picked >= 0 ? picked : history.length - 1;
  const releaseId = index >= 0 ? history[index].releaseId : undefined;
  useEffect(() => {
    if (!on || !sourceId || !releaseId) return;
    const controller = new AbortController();
    const show = (shown: ReviewedProduct) => { setProduct(shown); setWithheld(null); };
    const hold = (reason: string) => { setProduct(null); setWithheld({ releaseId, reason }); setPlaying(false); };
    const cached = cache.current.get(releaseId);
    // A cached release is shown on the next tick, the same path a fetched one takes.
    if (cached && approvalHolds(cached, Date.now())) { void Promise.resolve().then(() => { if (!controller.signal.aborted) show(cached); }); return () => controller.abort(); }
    cache.current.delete(releaseId);
    void fetch(`/api/curated/${sourceId}?release=${releaseId}`, { cache: "no-store", signal: controller.signal })
      .then(response => readBoundedJson(response, 8 * 1024 * 1024 + 65_536, controller.signal))
      .then(value => {
        const parsed = parseReviewedProduct(value, sourceId);
        if ("withheld" in parsed) return hold(parsed.withheld);
        if (parsed.releaseId !== releaseId) return hold("RELEASE_STORE_UNAVAILABLE");
        cache.current.set(releaseId, parsed);
        show(parsed);
      })
      .catch(() => { if (!controller.signal.aborted) hold("RELEASE_STORE_UNAVAILABLE"); });
    return () => controller.abort();
  }, [on, sourceId, releaseId]);
  // The shown release leaves the map when its approval expires, and the history is read again.
  useEffect(() => {
    if (!product) return;
    const expiresAt = Date.parse(product.approvalExpiresAt);
    let timer = 0;
    const check = () => {
      const remaining = expiresAt - Date.now();
      if (remaining > 0) { timer = window.setTimeout(check, Math.min(remaining, MAX_TIMER_MS)); return; }
      cache.current.delete(product.releaseId);
      setProduct(null); setWithheld({ releaseId: product.releaseId, reason: "APPROVAL_EXPIRED" }); setPlaying(false);
      setRevalidation(count => count + 1);
    };
    timer = window.setTimeout(check, Math.min(Math.max(0, expiresAt - Date.now()), MAX_TIMER_MS));
    return () => window.clearTimeout(timer);
  }, [product]);
  // Ready only once the selected release itself has been read; until then it is loading.
  const status: ReviewedSnapshots["status"] = !on || !sourceId ? "idle" : !historyState ? "loading" : !releaseId ? "withheld"
    : withheld?.releaseId === releaseId ? "withheld" : product?.releaseId === releaseId ? "ready" : "loading";
  const reason = status !== "withheld" ? null : releaseId ? withheld?.reason ?? null : historyState?.reason ?? "NO_APPROVED_RELEASE";
  const setIndex = useCallback((next: number) => {
    // Picking the newest follows the newest as new releases are published.
    setSelectedId(next >= 0 && next < history.length - 1 ? history[next].releaseId : null);
  }, [history]);
  // Play steps forward one release at a time, each once it has been drawn, and stops at the newest.
  useEffect(() => {
    if (!playing || !motionAllowed || status !== "ready" || index >= history.length - 1) return;
    const timer = window.setTimeout(() => {
      const next = index + 1;
      setSelectedId(next < history.length - 1 ? history[next].releaseId : null);
      if (next >= history.length - 1) setPlaying(false);
    }, REVIEWED_STEP_MS);
    return () => window.clearTimeout(timer);
  }, [playing, motionAllowed, status, index, history]);
  // While a newly selected release loads, the last one drawn stays on the map.
  return { on, setOn, status, reason, history, index, setIndex, playing, setPlaying, product: status === "idle" || status === "withheld" ? null : product };
}
