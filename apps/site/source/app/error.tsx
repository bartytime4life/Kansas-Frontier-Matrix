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
    <section role="alert" aria-labelledby="explorer-recovery-title" style={{ width: "100%", maxWidth: 620, boxSizing: "border-box", border: "1px solid rgba(224,186,109,.45)", borderRadius: 18, padding: 28, background: "#0a2022" }}>
      <p style={{ color: "#e0ba6d", fontWeight: 800, letterSpacing: ".08em" }}>EXPLORER RECOVERY</p>
      <h1 id="explorer-recovery-title" style={{ margin: "8px 0 12px" }}>This workspace could not finish loading</h1>
      <p style={{ color: "#b8cbc4", lineHeight: 1.6 }}>Try this page again. Battery saver lowers the map&apos;s rendering budget when this browser allows saved settings.</p>
      <button type="button" onClick={retryEfficiently} style={{ marginTop: 10, border: 0, borderRadius: 10, padding: "11px 16px", background: "#e0ba6d", color: "#102022", font: "inherit", fontWeight: 800, cursor: "pointer" }}>Retry in battery saver</button>
      <p style={{ color: "#b8cbc4", lineHeight: 1.6 }}>If the error returns, open another workspace:</p>
      <nav aria-label="Recovery options" style={{ display: "flex", flexWrap: "wrap", gap: "12px 20px" }}>
        {/* Full navigation leaves the failed client workspace behind. */}
        <a href="/downloads" style={{ color: "#e0ba6d", padding: "10px 0", textUnderlineOffset: 4 }}>Data &amp; downloads</a>
        <a href="/about" style={{ color: "#e0ba6d", padding: "10px 0", textUnderlineOffset: 4 }}>Sources &amp; evidence guide</a>
      </nav>
      <p style={{ color: "#b8cbc4", fontSize: ".9rem", lineHeight: 1.6 }}>Before repeating a submission or download, check its status in the relevant workspace.</p>
    </section>
  </main>;
}
