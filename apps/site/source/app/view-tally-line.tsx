"use client";
import { useEffect, useRef, useState, type RefObject } from "react";
import type { FeatureCollection } from "geojson";
import type { Map } from "./maplibre-seam";
import { viewTally, viewTallyBrief, type ViewTally } from "./view-tally";

/** One line under a counted layer: how many of its records the map shows now, and what they are. */
export function ViewTallyLine({ contextId, data, mapRef, reducedMotion, onShowRecord }: {
  contextId: string; data: FeatureCollection | null | undefined; mapRef: RefObject<Map | null>; reducedMotion: boolean;
  /** Selects the record now drawn at this spot, as a click on it would. Returns whether one was found. */
  onShowRecord?: (center: readonly [number, number], opener: HTMLElement | null) => boolean;
}) {
  const [tally, setTally] = useState<ViewTally | null>(null);
  // The selection waiting for the map to arrive, so a second press or leaving the panel cancels the first.
  const pendingShow = useRef<(() => void) | null>(null);
  useEffect(() => () => { pendingShow.current?.(); }, []);
  // A pressed button can disappear when the line recounts for the new view (one record left, nothing to pick out).
  // Keyboard focus then goes to the line itself instead of being dropped to the top of the page.
  const lineRef = useRef<HTMLParagraphElement>(null), keepFocus = useRef(false);
  useEffect(() => {
    if (!keepFocus.current) return;
    keepFocus.current = false;
    if (document.activeElement === document.body) lineRef.current?.focus({ preventScroll: true });
  }, [tally]);
  useEffect(() => {
    const map = mapRef.current;
    if (!map) return;
    const read = () => {
      const bounds = map.getBounds();
      setTally(viewTally(contextId, data, { west: bounds.getWest(), south: bounds.getSouth(), east: bounds.getEast(), north: bounds.getNorth() }));
    };
    const first = requestAnimationFrame(read);
    map.on("moveend", read);
    return () => { cancelAnimationFrame(first); map.off("moveend", read); };
  }, [mapRef, contextId, data]);
  if (!tally) return null;
  const nearest = tally.nearest;
  // Not a live region: it changes with every pan, and the map's own move is the feedback.
  return <p className="view-tally" data-empty={tally.count === 0} ref={lineRef} tabIndex={-1}>
    <strong>{tally.title}</strong>
    {tally.detail && <span>{tally.detail}</span>}
    {nearest && <button type="button" onClick={() => mapRef.current?.easeTo({ center: [nearest[0], nearest[1]], duration: reducedMotion ? 0 : 600 })}>Go to the nearest</button>}
    {tally.highlights.length > 0 && <span className="view-tally-actions">{tally.highlights.map((highlight, index) => <button type="button" key={index} onClick={event => {
      const map = mapRef.current;
      if (!map) return;
      pendingShow.current?.();
      keepFocus.current = true;
      if (onShowRecord) {
        const opener = event.currentTarget, center = highlight.center;
        // Still where the button sent it? A visitor who has moved on since is not handed a record they did not ask for.
        const arrived = () => { const at = map.project([center[0], center[1]]), middle = map.project(map.getCenter()); return Math.hypot(at.x - middle.x, at.y - middle.y) < 12; };
        // The record is drawn a moment after the map stops; if it is not there yet, look once more when the map has settled.
        const settled = () => { pendingShow.current = null; if (arrived()) onShowRecord(center, opener); };
        const stopped = () => {
          if (!arrived()) { pendingShow.current = null; return; }
          if (onShowRecord(center, opener)) { pendingShow.current = null; return; }
          map.once("idle", settled);
          pendingShow.current = () => { map.off("idle", settled); pendingShow.current = null; };
        };
        map.once("moveend", stopped);
        pendingShow.current = () => { map.off("moveend", stopped); pendingShow.current = null; };
      }
      // Never zooms out: a visitor already closer than the record needs stays where they are.
      map.easeTo({ center: [highlight.center[0], highlight.center[1]], zoom: Math.max(map.getZoom(), highlight.zoom), duration: reducedMotion ? 0 : 900 });
    }}>{highlight.label}</button>)}</span>}
  </p>;
}

/** The same counts for every counted layer on the map, as one short status-bar line that stays in sight while panning. */
export function ViewTallyStatus({ layers, mapRef }: {
  layers: readonly Readonly<{ contextId: string; data: FeatureCollection | null | undefined }>[]; mapRef: RefObject<Map | null>;
}) {
  const [brief, setBrief] = useState("");
  useEffect(() => {
    const map = mapRef.current;
    if (!map || !layers.length) return;
    const read = () => {
      const bounds = map.getBounds(), view = { west: bounds.getWest(), south: bounds.getSouth(), east: bounds.getEast(), north: bounds.getNorth() };
      setBrief(viewTallyBrief(layers.flatMap(({ contextId, data }) => { const tally = viewTally(contextId, data, view); return tally ? [{ contextId, count: tally.count }] : []; })));
    };
    const first = requestAnimationFrame(read);
    map.on("moveend", read);
    return () => { cancelAnimationFrame(first); map.off("moveend", read); };
  }, [mapRef, layers]);
  if (!brief || !layers.length) return null;
  return <output className="status-view-tally" aria-live="off">{brief}</output>;
}
