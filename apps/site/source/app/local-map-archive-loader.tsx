"use client";
import { useEffect, useRef, useState, type ComponentType } from "react";
import type { LocalArchiveBrowserProps } from "./local-map-archive-browser";
import type { LocalReviewProps } from "./local-geopdf-review-control";

/** Keep the 596-record metadata and inspection code off the initial map load. */
export function LocalMapArchiveLoader(props: LocalReviewProps) {
  const [loaded, setLoaded] = useState<{ Browser: ComponentType<LocalArchiveBrowserProps>; Review: ComponentType<LocalReviewProps>; sourceSha256: string } | null>(null), [busy, setBusy] = useState(false), [failed, setFailed] = useState(false);
  const alive = useRef(true);
  useEffect(() => { const mounted = alive; mounted.current = true; return () => { mounted.current = false; }; }, []);
  const open = async () => {
    setBusy(true); setFailed(false);
    try {
      const [browser, review, profile] = await Promise.all([import("./local-map-archive-browser"), import("./local-geopdf-review-control"), import("./local-geopdf-review")]);
      if (alive.current) setLoaded({ Browser: browser.default, Review: review.default, sourceSha256: profile.ALLEN_REVIEW.sourceSha256 });
    } catch { if (alive.current) setFailed(true); }
    finally { if (alive.current) setBusy(false); }
  };
  if (loaded) { const { Browser, Review } = loaded; return <Browser renderPreparedReview={sheet => sheet.sha256 === loaded.sourceSha256 ? <Review key={sheet.id} {...props} /> : null} />; }
  return <section className="local-map-archive-entry"><h4>Local road &amp; bridge map archive</h4><p>Browse the local PDF inventory, including historic county and township sheets. Original files stay on your device.</p><button type="button" disabled={busy} onClick={() => void open()}>{busy ? "Loading archive index…" : failed ? "Retry local archive" : "Browse local map archive"}</button>{failed && <p role="alert">The archive index could not load. The map and existing layers remain available.</p>}</section>;
}
