import { useCallback, useEffect, useRef, useState } from "react";
import type { FeatureCollection } from "geojson";
import { readBoundedJson } from "./bounded-json";

/**
 * Reviewed snapshots from the site's own database: hourly USGS streamflow and
 * NWS alert captures that the publishing pipeline normalized, signed and
 * committed to MySQL (server/pipeline-*.mjs), read through /api/curated. They
 * are approved context releases, not admitted evidence, and each keeps its own
 * capture time.
 */
export type ReviewedSourceId = "usgs-streamflow" | "nws-alerts";
export const REVIEWED_SOURCE_BY_TOPIC: Readonly<Record<string, ReviewedSourceId>> = Object.freeze({ water: "usgs-streamflow", weather: "nws-alerts", disaster: "nws-alerts" });
export const REVIEWED_SOURCE_LABEL: Readonly<Record<ReviewedSourceId, string>> = Object.freeze({ "usgs-streamflow": "USGS discharge", "nws-alerts": "NWS alerts" });

export type ReviewedRelease = Readonly<{ releaseId: string; publishedAt: string }>;
export type ReviewedProduct = Readonly<{
  state: "available" | "partial" | "empty"; sourceId: ReviewedSourceId; releaseId: string;
  retrievedAt: string; bucketAt: string; freshness: string; measurementFreshness: string;
  limitation: string; data: FeatureCollection;
}>;

/** Why nothing is shown, in words, for each reason the release API gives. */
export const REVIEWED_REASONS: Readonly<Record<string, string>> = Object.freeze({
  PIPELINE_NOT_CONFIGURED: "Reviewed snapshots are not switched on for this site yet.",
  NO_APPROVED_RELEASE: "No approved snapshot has been published yet.",
  RELEASE_STORE_UNAVAILABLE: "The site database is unavailable right now.",
  HISTORY_UNAVAILABLE: "The site database is unavailable right now.",
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
export function parseReviewedProduct(value: unknown, sourceId: ReviewedSourceId): ReviewedProduct | { withheld: string } {
  const p = value as Record<string, unknown> | null;
  if (!p || typeof p !== "object") return { withheld: "RELEASE_STORE_UNAVAILABLE" };
  if (!["available", "partial", "empty"].includes(String(p.state))) return { withheld: typeof p.reason === "string" ? p.reason : "NO_APPROVED_RELEASE" };
  const data = p.data as FeatureCollection | undefined;
  if (p.sourceId !== sourceId || p.evidenceRole !== "EXTERNAL_CONTEXT_ONLY" || typeof p.releaseId !== "string" || !releaseIdPattern.test(p.releaseId)
    || !isTime(p.retrievedAt) || !isTime(p.bucketAt) || data?.type !== "FeatureCollection" || !Array.isArray(data.features) || data.features.length > 1000) return { withheld: "RELEASE_STORE_UNAVAILABLE" };
  // Expired alert areas leave the display; the release still records them.
  const features = sourceId === "nws-alerts" ? data.features.filter(feature => feature.properties?.expired !== true) : data.features;
  return { state: p.state as ReviewedProduct["state"], sourceId, releaseId: p.releaseId, retrievedAt: p.retrievedAt as string, bucketAt: p.bucketAt as string,
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

/**
 * Reviewed snapshots for one source: the release history when switched on, the
 * selected release (newest first shown), and a player that steps forward
 * through the releases. Releases are cached by id, so replay does not refetch.
 */
export function useReviewedSnapshots(sourceId: ReviewedSourceId | null, motionAllowed: boolean): ReviewedSnapshots {
  const [on, setOnState] = useState(false);
  const [status, setStatus] = useState<ReviewedSnapshots["status"]>("idle");
  const [reason, setReason] = useState<string | null>(null);
  const [history, setHistory] = useState<readonly ReviewedRelease[]>([]);
  const [index, setIndex] = useState(-1);
  const [playing, setPlaying] = useState(false);
  const [product, setProduct] = useState<ReviewedProduct | null>(null);
  const cache = useRef(new Map<string, ReviewedProduct>());
  const setOn = useCallback((next: boolean) => {
    setOnState(next); setPlaying(false);
    if (next) setStatus("loading"); else { setProduct(null); setStatus("idle"); }
  }, []);
  // A different source starts over (reset while rendering, not in an effect).
  const [shownSource, setShownSource] = useState(sourceId);
  if (shownSource !== sourceId) {
    setShownSource(sourceId); setOnState(false); setPlaying(false); setProduct(null);
    setHistory([]); setIndex(-1); setStatus("idle"); setReason(null);
  }
  useEffect(() => { cache.current.clear(); }, [sourceId]);
  useEffect(() => {
    if (!on || !sourceId) return;
    const controller = new AbortController();
    void fetch(`/api/curated/${sourceId}/history`, { cache: "no-store", signal: controller.signal })
      .then(response => readBoundedJson(response, 65_536, controller.signal))
      .then(value => {
        const parsed = parseReviewedHistory(value);
        setHistory(parsed.items); setReason(parsed.reason);
        setIndex(parsed.items.length - 1);
        if (!parsed.items.length) setStatus("withheld");
      })
      .catch(() => { if (!controller.signal.aborted) { setHistory([]); setReason("HISTORY_UNAVAILABLE"); setStatus("withheld"); } });
    return () => controller.abort();
  }, [on, sourceId]);
  const release = index >= 0 ? history[index] : undefined;
  useEffect(() => {
    if (!on || !sourceId || !release) return;
    const controller = new AbortController();
    const cached = cache.current.get(release.releaseId);
    // A cached release is shown on the next tick, the same path a fetched one takes.
    if (cached) { void Promise.resolve().then(() => { if (!controller.signal.aborted) { setProduct(cached); setReason(null); setStatus("ready"); } }); return () => controller.abort(); }
    void fetch(`/api/curated/${sourceId}?release=${release.releaseId}`, { cache: "no-store", signal: controller.signal })
      .then(response => readBoundedJson(response, 8 * 1024 * 1024 + 65_536, controller.signal))
      .then(value => {
        const parsed = parseReviewedProduct(value, sourceId);
        if ("withheld" in parsed) { setProduct(null); setReason(parsed.withheld); setStatus("withheld"); setPlaying(false); return; }
        cache.current.set(parsed.releaseId, parsed);
        setProduct(parsed); setReason(null); setStatus("ready");
      })
      .catch(() => { if (!controller.signal.aborted) { setProduct(null); setReason("RELEASE_STORE_UNAVAILABLE"); setStatus("withheld"); setPlaying(false); } });
    return () => controller.abort();
  }, [on, sourceId, release]);
  // Play steps forward one release at a time and stops at the newest.
  useEffect(() => {
    if (!playing || !motionAllowed || status !== "ready" || index >= history.length - 1) return;
    const timer = window.setTimeout(() => {
      const next = Math.min(history.length - 1, index + 1);
      setIndex(next);
      if (next >= history.length - 1) setPlaying(false);
    }, REVIEWED_STEP_MS);
    return () => window.clearTimeout(timer);
  }, [playing, motionAllowed, status, index, history.length]);
  return { on, setOn, status, reason, history, index, setIndex, playing, setPlaying, product };
}
