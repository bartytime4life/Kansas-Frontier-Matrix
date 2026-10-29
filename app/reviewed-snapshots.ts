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
export type ReviewedSourceId = "usgs-streamflow" | "nws-alerts" | "usgs-earthquakes" | "newberry-county-history";
export const REVIEWED_SOURCE_BY_TOPIC: Readonly<Record<string, ReviewedSourceId>> = Object.freeze({ water: "usgs-streamflow", weather: "nws-alerts", disaster: "nws-alerts", geology: "usgs-earthquakes", government: "newberry-county-history" });
export const REVIEWED_SOURCE_LABEL: Readonly<Record<ReviewedSourceId, string>> = Object.freeze({ "usgs-streamflow": "USGS discharge", "nws-alerts": "NWS alerts", "usgs-earthquakes": "USGS earthquake", "newberry-county-history": "historical county" });

export type ReviewedRelease = Readonly<{ releaseId: string; publishedAt: string; effectiveDay?: string }>;
export type ReviewedProduct = Readonly<{
  state: "available" | "partial" | "empty"; sourceId: ReviewedSourceId; releaseId: string;
  retrievedAt: string; bucketAt: string; approvalExpiresAt: string; freshness: string; measurementFreshness: string;
  limitation: string; data: FeatureCollection; effectiveDay?: string;
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

export function isCountyDay(value: unknown): value is string {
  return typeof value === "string" && /^\d{4}-\d{2}-\d{2}$/.test(value) && value >= "1804-10-01" && value <= "2000-12-31"
    && Number.isFinite(Date.parse(value + "T00:00:00Z")) && new Date(value + "T00:00:00Z").toISOString().slice(0, 10) === value;
}
function validCountyProduct(p: Record<string, unknown>): boolean {
  const data = p.data as FeatureCollection | undefined, day = p.effectiveDay;
  if (p.format !== "kfm-curated-county-history-v1" || !isCountyDay(day) || !isTime(p.preparedAt)
    || p.archiveSha256 !== "a233b4b3bcf3f3d7a52a4c18de76017f0d4f1f421086f95312df4c59a0aa5f02"
    || p.sourceUrl !== "https://publications.newberry.org/ahcb/downloads/gis/KS_AtlasHCB.zip" || p.evidenceEligible !== false || p.partial !== false
    || day >= "1873-03-20" && day < "1874-03-18" || p.lifecycle !== undefined || !Array.isArray(data?.features) || !data.features.length || data.features.length > 107) return false;
  const seen = new Set<string>(); let vertices = 0;
  for (const feature of data.features) {
    const r = feature.properties, g = feature.geometry;
    if (!r || r.sourceDay !== day || typeof r.name !== "string" || r.name.length > 200 || r.classificationStatus !== "unreviewed_source_label"
      || typeof r.institutionSourceId !== "string" || !/^[a-z0-9_]{1,96}$/.test(r.institutionSourceId) || !Number.isSafeInteger(r.sourceVersion) || r.sourceVersion < 1 || r.sourceVersion > 1000
      || feature.id !== `ahcb-a233b4b3bcf3-${r.institutionSourceId}-v${r.sourceVersion}-${day}` || seen.has(String(feature.id))
      || !isCountyDay(r.validFrom) || !isCountyDay(r.sourceLastDay) || typeof r.validToExclusive !== "string"
      || r.validToExclusive !== new Date(Date.parse(r.sourceLastDay + "T00:00:00Z") + 86400000).toISOString().slice(0,10)
      || !(r.validFrom <= day && day < r.validToExclusive) || typeof r.citation !== "string" || !r.citation.trim() || r.citation.length > 3000
      || !g || !["Polygon","MultiPolygon"].includes(g.type)) return false;
    seen.add(String(feature.id));
    const polygons = g.type === "Polygon" ? [g.coordinates] : g.type === "MultiPolygon" ? g.coordinates : [];
    if (!Array.isArray(polygons) || !polygons.length || polygons.length > 1000) return false;
    for (const rings of polygons) {
      if (!Array.isArray(rings) || !rings.length || rings.length > 1000) return false;
      for (const ring of rings) {
        if (!Array.isArray(ring) || ring.length < 4 || ring.length > 100000) return false;
        for (const point of ring) if (!Array.isArray(point) || point.length !== 2 || !point.every(Number.isFinite) || Math.abs(point[0]) > 180 || Math.abs(point[1]) > 90 || ++vertices > 200000) return false;
        if (ring[0][0] !== ring.at(-1)![0] || ring[0][1] !== ring.at(-1)![1]) return false;
      }
    }
  }
  return true;
}
/** The county carrier can draw only on its own exact day, with a current build/approval. */
export function reviewedDataForDay(product: ReviewedProduct | null, selectedDay: string, buildCurrent = true, now = Date.now()): FeatureCollection | null {
  if (!product) return null;
  if (product.sourceId !== "newberry-county-history") return product.data;
  return buildCurrent && product.effectiveDay === selectedDay && Date.parse(product.approvalExpiresAt) > now ? product.data : null;
}

export function parseReviewedHistory(value: unknown, sourceId?: ReviewedSourceId): { items: ReviewedRelease[]; reason: string | null } {
  const record = value as { items?: unknown; state?: unknown; reason?: unknown } | null;
  if (!record || typeof record !== "object") return { items: [], reason: "RELEASE_STORE_UNAVAILABLE" };
  const items = Array.isArray(record.items) ? record.items.filter((item): item is ReviewedRelease =>
    typeof item?.releaseId === "string" && releaseIdPattern.test(item.releaseId) && isTime(item.publishedAt) && (sourceId !== "newberry-county-history" || isCountyDay(item.effectiveDay))) : [];
  // Oldest first, so the scrubber runs forward in time.
  items.sort((a, b) => sourceId === "newberry-county-history" ? String(a.effectiveDay).localeCompare(String(b.effectiveDay)) || Date.parse(a.publishedAt)-Date.parse(b.publishedAt) : Date.parse(a.publishedAt) - Date.parse(b.publishedAt));
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
    || (sourceId === "newberry-county-history" ? !validCountyProduct(p) : !isTime(p.retrievedAt) || !isTime(p.bucketAt)) || data?.type !== "FeatureCollection" || !Array.isArray(data.features) || data.features.length > 1000) return { withheld: "RELEASE_STORE_UNAVAILABLE" };
  // A release is shown only while its publication approval holds.
  if (!isTime(p.approvalExpiresAt)) return { withheld: "RELEASE_STORE_UNAVAILABLE" };
  if (Date.parse(p.approvalExpiresAt) <= now) return { withheld: "APPROVAL_EXPIRED" };
  // Expired alert areas leave the display; the release still records them.
  const features = sourceId === "nws-alerts" ? data.features.filter(feature => feature.properties?.expired !== true) : data.features;
  return { state: p.state as ReviewedProduct["state"], sourceId, releaseId: p.releaseId, retrievedAt: (sourceId === "newberry-county-history" ? p.preparedAt : p.retrievedAt) as string, bucketAt: (sourceId === "newberry-county-history" ? p.effectiveDay + "T00:00:00Z" : p.bucketAt) as string, ...(sourceId === "newberry-county-history" ? { effectiveDay: p.effectiveDay as string } : {}), approvalExpiresAt: p.approvalExpiresAt,
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
export function useReviewedSnapshots(sourceId: ReviewedSourceId | null, motionAllowed: boolean, requestedDay?: string): ReviewedSnapshots {
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
        const parsed = parseReviewedHistory(value, sourceId);
        // Releases no longer listed are no longer approved to show.
        for (const releaseId of cache.current.keys()) if (!parsed.items.some(release => release.releaseId === releaseId)) cache.current.delete(releaseId);
        setHistoryState(previous => previous && previous.reason === parsed.reason && sameReleases(previous.items, parsed.items) ? previous : parsed);
      })
      // A failed re-read keeps the history already shown; each release still expires on its own.
      .catch(() => { if (!controller.signal.aborted) setHistoryState(previous => previous?.items.length ? previous : { items: [], reason: "HISTORY_UNAVAILABLE" }); });
    return () => controller.abort();
  }, [on, sourceId, revalidation]);
  const history = historyState?.items ?? NO_RELEASES;
  const manualIndex = selectedId ? history.findIndex(release => release.releaseId === selectedId) : -1;
  const datedIndex = sourceId === "newberry-county-history" ? history.findLastIndex(release => release.effectiveDay === requestedDay) : -1;
  const picked = datedIndex >= 0 && (manualIndex < 0 || history[manualIndex].effectiveDay !== requestedDay) ? datedIndex : manualIndex;
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
    if (sourceId === "newberry-county-history" || !playing || !motionAllowed || status !== "ready" || index >= history.length - 1) return;
    const timer = window.setTimeout(() => {
      const next = index + 1;
      setSelectedId(next < history.length - 1 ? history[next].releaseId : null);
      if (next >= history.length - 1) setPlaying(false);
    }, REVIEWED_STEP_MS);
    return () => window.clearTimeout(timer);
  }, [sourceId, playing, motionAllowed, status, index, history]);
  // While a newly selected release loads, the last one drawn stays on the map.
  return { on, setOn, status, reason, history, index, setIndex, playing, setPlaying, product: status === "idle" || status === "withheld" ? null : product };
}

const SEVERITY_RANK: Readonly<Record<string, number>> = Object.freeze({ Extreme: 4, Severe: 3, Moderate: 2, Minor: 1 });
/**
 * A shown release's features for a keyboard list, most significant first:
 * earthquakes by magnitude, gauges by discharge, alerts by NWS severity. Each
 * carries its release feature id and a one-line label from its summary.
 */
export function reviewedFeatureList(sourceId: ReviewedSourceId, data: FeatureCollection, limit = 40): readonly Readonly<{ id: string; label: string }>[] {
  const weight = (p: Record<string, unknown>) => sourceId === "usgs-earthquakes" ? num(p.magnitude) ?? -Infinity
    : sourceId === "usgs-streamflow" ? num(p.value) ?? -Infinity : SEVERITY_RANK[String(p.severity)] ?? 0;
  return data.features.filter(feature => feature.id !== undefined && feature.id !== null)
    .map(feature => ({ feature, w: weight(feature.properties ?? {}) }))
    .sort((a, b) => sourceId === "newberry-county-history" ? String(a.feature.properties?.name).localeCompare(String(b.feature.properties?.name), "en-US") : b.w - a.w)
    .slice(0, limit)
    .map(({ feature }) => {
      const summary = reviewedFeatureSummary(sourceId, feature.properties);
      return { id: String(feature.id), label: [summary.title, summary.lines[0]].filter(Boolean).join(" · ") };
    });
}

/** What the dock shows for a feature selected in a reviewed snapshot: its own details, in its source's terms. */
export type ReviewedFeatureSummary = Readonly<{ title: string; lines: readonly string[]; link: Readonly<{ href: string; label: string }> | null }>;
const str = (value: unknown, max = 200): string | null => typeof value === "string" && value.trim() ? value.trim().slice(0, max) : null;
const num = (value: unknown): number | null => typeof value === "number" && Number.isFinite(value) ? value : null;
const utc = (value: unknown): string | null => isTime(value) ? new Date(value).toISOString().slice(0, 16).replace("T", " ") + " UTC" : null;
const USGS_STATION = /^USGS-(\d{8,15})$/;
const USGS_EVENT_PAGE = "https://earthquake.usgs.gov/earthquakes/eventpage/";

export function reviewedFeatureSummary(sourceId: ReviewedSourceId, properties: Readonly<Record<string, unknown>> | null | undefined): ReviewedFeatureSummary {
  const p = properties ?? {};
  if (sourceId === "newberry-county-history") return {
    title: str(p.name, 200) ?? "Historical source area",
    lines: [`Boundary date ${str(p.sourceDay, 10) ?? "unknown"}`, `${str(p.validFrom, 10)} through ${str(p.sourceLastDay, 10)} (included)`,
      `Source type: ${str(p.sourceCountyType, 100)} · classification unreviewed`,
      p.fips === null ? "FIPS not reported" : `Source FIPS ${str(p.fips, 5)}`,
      str(p.change, 6000), str(p.citation, 3000), "Newberry Atlas reconstruction · approved context, not admitted KFM evidence"].filter((v): v is string => Boolean(v)),
    link: { href: "https://publications.newberry.org/ahcb/pages/Kansas.html", label: "Newberry source and chronology ↗" },
  };
  if (sourceId === "usgs-streamflow") {
    const station = str(p.stationId, 40), value = num(p.value), unit = str(p.unit, 32), observed = utc(p.observedAt);
    const site = station ? USGS_STATION.exec(station)?.[1] ?? null : null;
    return {
      title: station ? `Gauge ${station.replace(/^USGS-/, "")}` : "USGS gauge",
      lines: [
        value === null ? "No discharge value in this capture" : `${value.toLocaleString("en-US")}${unit ? ` ${unit}` : ""}`,
        [p.provisional === true ? "Provisional USGS value" : p.provisional === false ? "Approved USGS value" : null, observed ? `observed ${observed}` : null].filter(Boolean).join(" · "),
      ].filter(Boolean),
      link: site ? { href: `https://waterdata.usgs.gov/monitoring-location/${site}/`, label: "USGS station page ↗" } : null,
    };
  }
  if (sourceId === "nws-alerts") {
    const effective = utc(p.effective), expires = utc(p.expires);
    return {
      title: str(p.event, 120) ?? "NWS alert",
      lines: [
        [str(p.severity, 32), str(p.urgency, 32), str(p.certainty, 32)].filter(Boolean).join(" · "),
        [effective ? `effective ${effective}` : null, expires ? `expires ${expires}` : null].filter(Boolean).join(" · "),
        str(p.areaDesc, 240), str(p.headline, 240),
      ].filter((line): line is string => Boolean(line)),
      link: null,
    };
  }
  const magnitude = num(p.magnitude), type = str(p.magnitudeType, 16), depth = num(p.depthKm), when = utc(p.observedAt), id = str(p.sourceFeatureId, 40);
  return {
    title: magnitude === null ? "Earthquake, magnitude not given" : `M ${magnitude.toFixed(1)}${type ? ` ${type}` : ""}`,
    lines: [
      str(p.place, 240),
      [depth === null ? null : `depth ${depth.toFixed(1)} km`, when].filter(Boolean).join(" · "),
      p.status === "reviewed" ? "Reviewed by a USGS analyst" : p.status === "automatic" ? "Automatic USGS solution; may still be revised" : null,
    ].filter((line): line is string => Boolean(line)),
    // Built from the id the pipeline checked, the same way the release builds it.
    link: id && /^[a-z0-9]{2,40}$/.test(id) ? { href: USGS_EVENT_PAGE + id, label: "USGS event page ↗" } : null,
  };
}
