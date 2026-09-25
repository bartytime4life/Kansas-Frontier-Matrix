"use client";

import { useEffect } from "react";
import { QUALITY_STORAGE_KEY } from "./map-performance";

export default function ExplorerError({ error, reset }: { error: Error & { digest?: string }; reset?: () => void }) {
  useEffect(() => { console.error("KFM Explorer route failure", error); }, [error]);
  const retryEfficiently = () => {
    try { window.localStorage.setItem(QUALITY_STORAGE_KEY, "efficient"); } catch { /* Retry still works without storage. */ }
    if (reset) reset();
    else window.location.reload();
  };
  return <main style={{ minHeight: "100dvh", display: "grid", placeItems: "center", padding: 24, background: "#061416", color: "#eff5ef", fontFamily: "system-ui, sans-serif" }}>
    <section role="alert" style={{ maxWidth: 620, border: "1px solid rgba(224,186,109,.45)", borderRadius: 18, padding: 28, background: "#0a2022" }}>
      <p style={{ color: "#e0ba6d", fontWeight: 800, letterSpacing: ".08em" }}>EXPLORER RECOVERY</p>
      <h1 style={{ margin: "8px 0 12px" }}>The map workspace hit a client error</h1>
      <p style={{ color: "#b8cbc4", lineHeight: 1.6 }}>This recovery screen keeps the failure visible. Retry with the lighter rendering budget; data remains read-only and no missing value is inferred.</p>
      <button type="button" onClick={retryEfficiently} style={{ marginTop: 10, border: 0, borderRadius: 10, padding: "11px 16px", background: "#e0ba6d", color: "#102022", fontWeight: 800 }}>Retry in battery saver</button>
    </section>
  </main>;
}
