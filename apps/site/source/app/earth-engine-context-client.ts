"use client";

import { useCallback, useEffect, useState } from "react";
import { earthEngineSetYear, parseEarthEngineManifest, type EarthEngineContextManifest } from "./earth-engine-context";

export function useEarthEngineContext() {
  const [manifest, setManifest] = useState<EarthEngineContextManifest | null>(null);
  const [manifests, setManifests] = useState<EarthEngineContextManifest[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [generation, setGeneration] = useState(0);
  const reload = useCallback(() => { setLoading(true); setGeneration((value) => value + 1); }, []);
  useEffect(() => {
    const abort = new AbortController();
    void fetch("/api/earth-engine-context/catalog", { credentials: "same-origin", cache: "no-store", signal: abort.signal })
      .then(async (response) => {
        if (response.status === 401 || response.status === 403) throw new Error("Owner sign-in is required to load reviewed imagery. Local files alone do not establish an activated display set.");
        if (!response.ok) throw new Error("Reviewed snapshots are unavailable.");
        const payload: unknown = await response.json();
        if (!payload || typeof payload !== "object" || !("manifests" in payload) || !Array.isArray(payload.manifests) || payload.manifests.length > 70) throw new Error("Display-set details are invalid.");
        const checked = payload.manifests.map(parseEarthEngineManifest);
        if (checked.some((item) => !item)) throw new Error("Display-set details are invalid.");
        const years = checked.map((item) => earthEngineSetYear(item));
        if (years.some((year) => year === null) || new Set(years).size !== years.length) throw new Error("Display-set years are invalid.");
        return checked as EarthEngineContextManifest[];
      })
      .then((checked) => { if (!abort.signal.aborted) { setManifests(checked); setManifest(checked.find((item) => earthEngineSetYear(item) === 2024) ?? checked[0] ?? null); setError(null); } })
      .catch((cause: unknown) => { if (!abort.signal.aborted) { setManifests([]); setManifest(null); setError(cause instanceof Error ? cause.message : "Reviewed snapshots are unavailable."); } })
      .finally(() => { if (!abort.signal.aborted) setLoading(false); });
    return () => abort.abort();
  }, [generation]);
  return { manifest, manifests, loading, error, reload };
}
