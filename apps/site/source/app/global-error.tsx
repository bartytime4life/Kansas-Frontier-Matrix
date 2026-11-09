"use client";

export default function GlobalError({ reset }: { error: Error & { digest?: string }; reset?: () => void }) {
  const retry = () => { if (reset) reset(); else window.location.reload(); };
  return <html lang="en"><body style={{ margin: 0, background: "#061416", color: "#eff5ef", fontFamily: "system-ui, sans-serif" }}>
    <main style={{ minHeight: "100dvh", display: "grid", placeItems: "center", padding: 24 }}>
      <section role="alert" aria-labelledby="global-recovery-title" style={{ width: "100%", maxWidth: 620, boxSizing: "border-box", border: "1px solid #8b7650", borderRadius: 18, padding: 28, background: "#0a2022" }}>
        <p style={{ color: "#e0ba6d", fontWeight: 800 }}>KANSAS FRONTIER MATRIX</p>
        <h1 id="global-recovery-title">The Explorer could not finish loading</h1>
        <p style={{ color: "#b8cbc4", lineHeight: 1.6 }}>Try this page again. If the error returns, open another workspace or return later.</p>
        <button type="button" onClick={retry} style={{ border: 0, borderRadius: 10, padding: "11px 16px", background: "#e0ba6d", color: "#102022", font: "inherit", fontWeight: 800, cursor: "pointer" }}>Retry Explorer</button>
        <nav aria-label="Recovery options" style={{ display: "flex", flexWrap: "wrap", gap: "12px 20px", marginTop: 16 }}>
          {/* Plain links also work when the application shell cannot recover. */}
          <a href="/downloads" style={{ color: "#e0ba6d", padding: "10px 0", textUnderlineOffset: 4 }}>Data &amp; downloads</a>
          <a href="/about" style={{ color: "#e0ba6d", padding: "10px 0", textUnderlineOffset: 4 }}>Sources &amp; evidence guide</a>
        </nav>
        <p style={{ color: "#b8cbc4", fontSize: ".9rem", lineHeight: 1.6 }}>Before repeating a submission or download, check its status in the relevant workspace.</p>
      </section>
    </main>
  </body></html>;
}
