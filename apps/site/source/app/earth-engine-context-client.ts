"use client";

import { useCallback, useEffect, useState } from "react";
import { EARTH_ENGINE_CATALOG_MAX_BYTES, earthEngineSetYear, parseEarthEngineCatalog, type EarthEngineContextManifest } from "./earth-engine-context";
import { browserJsonRequest } from "./browser-json-request";

export function useEarthEngineContext() {
  const [manifest, setManifest] = useState<EarthEngineContextManifest | null>(null);
  const [manifests, setManifests] = useState<EarthEngineContextManifest[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [generation, setGeneration] = useState(0);
  const reload = useCallback(() => { setLoading(true); setGeneration((value) => value + 1); }, []);
  useEffect(() => {
    const abort = new AbortController();
    void browserJsonRequest("/api/earth-engine-context/catalog", { signal: abort.signal, maxBytes: EARTH_ENGINE_CATALOG_MAX_BYTES, timeoutMs: 30_000 })
      .then(({ response, body: payload }) => {
        if (response.status === 401 || response.status === 403) throw new Error("Owner sign-in is required to load reviewed imagery. Local files alone do not establish an activated display set.");
        if (!response.ok) throw new Error("Reviewed snapshots are unavailable.");
        const checked = parseEarthEngineCatalog(payload);
        if (!checked) throw new Error("Display-set details or years are invalid.");
        return checked;
      })
      .then((checked) => { if (!abort.signal.aborted) { setManifests(checked); setManifest(checked.find((item) => earthEngineSetYear(item) === 2024) ?? checked[0] ?? null); setError(null); } })
      .catch((cause: unknown) => { if (!abort.signal.aborted) { setManifests([]); setManifest(null); setError(cause instanceof Error ? cause.message : "Reviewed snapshots are unavailable."); } })
      .finally(() => { if (!abort.signal.aborted) setLoading(false); });
    return () => abort.abort();
  }, [generation]);
  return { manifest, manifests, loading, error, reload };
}
