"use client";
import { useEffect, useRef, useState } from "react";
import { loadMapLibre, type Map as MapLibreMap } from "./maplibre-seam";
import { ALLEN_REVIEW, inspectLocalReview, type LocalReviewPackage } from "./local-geopdf-review";
import { attachLocalReview, type ReviewMapState } from "./local-geopdf-map";

export type LocalReviewProps = { map: MapLibreMap | null; styleReady: boolean; flatMap: boolean; onFlatMap: () => void };
export default function LocalGeoPdfReviewControl({ map, styleReady, flatMap, onFlatMap }: LocalReviewProps) {
  const [pack, setPack] = useState<LocalReviewPackage | null>(null), [busy, setBusy] = useState(false), [error, setError] = useState("");
  const [visible, setVisible] = useState(true), [opacity, setOpacity] = useState(65), [mapState, setMapState] = useState<ReviewMapState>("hidden");
  const [zoom, setZoom] = useState(0), [urls, setUrls] = useState<{ original: string; legend: string } | null>(null);
  const pending = useRef<AbortController | null>(null), input = useRef<HTMLInputElement | null>(null);
  const installed = useRef<ReturnType<typeof attachLocalReview> | null>(null);
  const settings = useRef({ visible, opacity }), activeUrls = useRef<typeof urls>(null);
  useEffect(() => { settings.current = { visible, opacity }; }, [visible, opacity]);
  useEffect(() => () => {
    pending.current?.abort(); installed.current?.dispose();
    for (const url of Object.values(activeUrls.current ?? {})) URL.revokeObjectURL(url);
  }, []);
  useEffect(() => {
    if (!pack || !map || !styleReady) return;
    let cancelled = false;
    void loadMapLibre().then(runtime => {
      if (cancelled) return;
      const control = attachLocalReview(map, runtime, pack, flatMap, setMapState);
      installed.current = control; control.setVisible(settings.current.visible); control.setOpacity(settings.current.opacity / 100);
    }).catch(() => { if (!cancelled) setMapState("unavailable"); });
    return () => { cancelled = true; installed.current?.dispose(); installed.current = null; };
  }, [pack, map, styleReady, flatMap]);
  useEffect(() => { installed.current?.setVisible(visible); }, [visible]);
  useEffect(() => { installed.current?.setOpacity(opacity / 100); }, [opacity]);
  useEffect(() => {
    if (!map) return;
    const update = () => setZoom(map.getZoom()); update(); map.on("zoomend", update);
    return () => { map.off("zoomend", update); };
  }, [map]);
  const clear = () => {
    pending.current?.abort(); installed.current?.dispose(); installed.current = null;
    for (const url of Object.values(activeUrls.current ?? {})) URL.revokeObjectURL(url);
    activeUrls.current = null; setUrls(null);
    setPack(null); setBusy(false); setError(""); setMapState("hidden");
    if (input.current) input.current.value = "";
  };
  const choose = async (files: FileList | null) => {
    if (!files?.length) return;
    const selectedFiles = Array.from(files);
    clear(); setBusy(true); setVisible(true); setOpacity(65);
    const controller = new AbortController(); pending.current = controller;
    try {
      const result = await inspectLocalReview(selectedFiles, controller.signal);
      if (!controller.signal.aborted) {
        const original = URL.createObjectURL(result.original);
        try {
          const next = { original, legend: URL.createObjectURL(result.legend) };
          activeUrls.current = next; setUrls(next); setPack(result);
        } catch (cause) { URL.revokeObjectURL(original); throw cause; }
      }
    } catch (cause) { if (!controller.signal.aborted) setError(cause instanceof Error ? cause.message : "The prepared folder could not be checked."); }
    finally { if (!controller.signal.aborted) setBusy(false); }
  };
  const fit = () => {
    if (!map || !pack || !flatMap || map.getPitch() !== 0 || map.getTerrain()) return;
    const [w, s, e, n] = pack.bounds;
    const compact = window.innerWidth <= 760;
    map.fitBounds([[w, s], [e, n]], { padding: compact ? { top: 55, left: 25, right: 25, bottom: Math.round(window.innerHeight * .48) } : { top: 70, left: 70, right: 480, bottom: 70 }, maxZoom: pack.maxZoom,
      duration: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? 0 : 500 });
  };
  return <section className="local-geopdf-review" aria-label="Prepared map review">
    <header><strong>Prepared map review</strong><span>Device only · not released</span></header>
    <p>{ALLEN_REVIEW.title}. Choose the prepared folder to inspect its georeferenced tiles over your basemap.</p>
    <label>Choose prepared folder<input ref={node => { input.current = node; node?.setAttribute("webkitdirectory", ""); }} type="file" multiple onChange={e => void choose(e.target.files)} /></label>
    <p role="status">{busy ? "Checking all 186 files on this device…" : !pack ? "No prepared map loaded." : !map || !styleReady ? "Files verified; waiting for the map." : mapState === "unavailable" ? "Map rendering unavailable. Prepared overlay withheld; retry by selecting the folder again." : mapState === "flat-map-required" ? "Files verified. A flat map is required to inspect alignment." : visible ? "181 verified tiles · review overlay enabled" : "Prepared map hidden."}</p>
    {error && <p role="alert">{error}</p>}
    {pack && <>
      {(!flatMap || mapState === "flat-map-required") && <button type="button" onClick={onFlatMap}>Use flat map for review</button>}
      <label className="local-review-visible"><input type="checkbox" checked={visible} onChange={e => setVisible(e.target.checked)} />Show prepared map</label>
      <label>Review opacity <output>{opacity}%</output><input type="range" min="0" max="100" value={opacity} onChange={e => setOpacity(Number(e.target.value))} aria-valuetext={`${opacity} percent`} disabled={!visible} /></label>
      <div className="local-review-actions"><button type="button" onClick={fit} disabled={!flatMap || mapState === "flat-map-required" || !map || !styleReady}>Fit prepared sheet</button><button type="button" onClick={clear}>Remove review</button></div>
      {urls && <div className="local-review-actions"><a href={urls.original} target="_blank" rel="noreferrer">Open verified original</a><a href={urls.legend} target="_blank" rel="noreferrer">Open full page and legend</a></div>}
      <p>Future functional classifications, not current road conditions or closures. Edition: June 2025. County approval: May 13, 2003. FHWA approval: November 7, 2003.</p>
      <small>Nearest-neighbor tiles at zooms 10–13. Render detail is about 22.5 m per pixel; this is not positional accuracy or printed scale. Standard vector basemap is recommended; your current basemap is preserved.</small>
      {zoom > pack.maxZoom && <p className="local-archive-warning">Beyond the prepared image detail: pixels are enlarged, not additional source information.</p>}
      <details><summary>Alignment and review limits</summary><p>Nine cartographic checkpoints differed by 0.225–5.058 m from Census 2025 roads without refitting. Reference lineage may overlap. This does not establish surveyed ground accuracy. Source meaning, rights, sensitivity, independent review and release remain held.</p></details>
    </>}
    {busy && <button type="button" onClick={clear}>Cancel file check</button>}
    <small>One pinned preparation only. No upload, evidence, export, saved workspace or activation. Changing sheets or closing this panel clears the review.</small>
  </section>;
}
