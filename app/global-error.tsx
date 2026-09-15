"use client";

export default function GlobalError({ reset }: { error: Error & { digest?: string }; reset: () => void }) {
  return <html lang="en"><body style={{ margin: 0, background: "#061416", color: "#eff5ef", fontFamily: "system-ui, sans-serif" }}>
    <main style={{ minHeight: "100dvh", display: "grid", placeItems: "center", padding: 24 }}>
      <section role="alert" style={{ maxWidth: 620, border: "1px solid #8b7650", borderRadius: 18, padding: 28, background: "#0a2022" }}>
        <p style={{ color: "#e0ba6d", fontWeight: 800 }}>KANSAS FRONTIER MATRIX</p>
        <h1>The Explorer could not finish loading</h1>
        <p style={{ color: "#b8cbc4", lineHeight: 1.6 }}>The failure is visible and no map data has been inferred. Retry the current private Site.</p>
        <button type="button" onClick={reset} style={{ border: 0, borderRadius: 10, padding: "11px 16px", background: "#e0ba6d", color: "#102022", fontWeight: 800 }}>Retry Explorer</button>
      </section>
    </main>
  </body></html>;
}
