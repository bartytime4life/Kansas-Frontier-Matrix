"use client";
import { useEffect, useState, type RefObject } from "react";
import type { FeatureCollection } from "geojson";
import type { Map } from "./maplibre-seam";
import { viewTally, viewTallyBrief, type ViewTally } from "./view-tally";

/** One line under a counted layer: how many of its records the map shows now, and what they are. */
export function ViewTallyLine({ contextId, data, mapRef, reducedMotion }: {
  contextId: string; data: FeatureCollection | null | undefined; mapRef: RefObject<Map | null>; reducedMotion: boolean;
}) {
  const [tally, setTally] = useState<ViewTally | null>(null);
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
  return <p className="view-tally" data-empty={tally.count === 0}>
    <strong>{tally.title}</strong>
    {tally.detail && <span>{tally.detail}</span>}
    {nearest && <button type="button" onClick={() => mapRef.current?.easeTo({ center: [nearest[0], nearest[1]], duration: reducedMotion ? 0 : 600 })}>Go to the nearest</button>}
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
