"use client";

import { useCallback, useEffect, useState } from "react";
import { parseEarthEngineManifest, type EarthEngineContextManifest } from "./earth-engine-context";

export function useEarthEngineContext() {
  const [manifest, setManifest] = useState<EarthEngineContextManifest | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [generation, setGeneration] = useState(0);
  const reload = useCallback(() => { setLoading(true); setGeneration((value) => value + 1); }, []);
  useEffect(() => {
    const abort = new AbortController();
    void fetch("/api/earth-engine-context/active", { credentials: "same-origin", cache: "no-store", signal: abort.signal })
      .then(async (response) => {
        if (!response.ok) throw new Error("Reviewed snapshots are unavailable.");
        const payload: unknown = await response.json();
        if (!payload || typeof payload !== "object" || !("available" in payload)) throw new Error("Display-set details are invalid.");
        if (payload.available === false) return null;
        if (payload.available !== true || !("manifest" in payload)) throw new Error("Display-set details are invalid.");
        const checked = parseEarthEngineManifest(payload.manifest);
        if (!checked) throw new Error("Display-set details are invalid.");
        return checked;
      })
      .then((checked) => { if (!abort.signal.aborted) { setManifest(checked); setError(null); } })
      .catch((cause: unknown) => { if (!abort.signal.aborted) { setManifest(null); setError(cause instanceof Error ? cause.message : "Reviewed snapshots are unavailable."); } })
      .finally(() => { if (!abort.signal.aborted) setLoading(false); });
    return () => abort.abort();
  }, [generation]);
  return { manifest, loading, error, reload };
}
