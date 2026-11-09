"use client";

import { useEffect, useMemo, useState } from "react";
import type { GeoJSONSource, Map as MapLibreMap, MapMouseEvent } from "./maplibre-seam";
import { readBoundedJson } from "./bounded-json";
import type { AreaBounds } from "./subsurface-model";
import { RESOURCE_SOURCES, type ResourceKind, type ResourceLocation } from "./underground-resources-model";
import s from "./geology-point-explorer.module.css";

type SourceResult = { rows: ResourceLocation[]; partial: boolean; rejected: number; retrievedAt: string };
type SourceState = { rows: ResourceLocation[]; partial: boolean; error: boolean };
const EMPTY: SourceState = { rows: [], partial: false, error: false };
const KANSAS: AreaBounds = [-102.1, 36.95, -94.55, 40.05];
const SOURCE_ID = "kfm-geology-resource-preview";
export const GEOLOGY_POINT_LAYER_ID = `${SOURCE_ID}-points`;

/** A moving local sample, never a statewide inventory or a claim of empty coverage. */
export function geologyPointFrame(center: [number, number], span: [number, number]): AreaBounds {
  const width = Math.min(0.8, Math.max(0.12, span[0]));
  const height = Math.min(0.8, Math.max(0.12, span[1]));
  const west = Math.max(KANSAS[0], Math.min(center[0] - width / 2, KANSAS[2] - width));
  const south = Math.max(KANSAS[1], Math.min(center[1] - height / 2, KANSAS[3] - height));
  return [Number(west.toFixed(3)), Number(south.toFixed(3)), Number((west + width).toFixed(3)), Number((south + height).toFixed(3))];
}

export default function GeologyPointExplorer({ map, enabled, redacted, monitoringVisible }: { map: MapLibreMap | null; enabled: boolean; redacted: boolean; monitoringVisible: boolean }) {
  const [frame, setFrame] = useState<AreaBounds | null>(null);

  useEffect(() => {
    if (!map || !enabled || redacted) return;
    const update = () => {
      const center = map.getCenter(), bounds = map.getBounds();
      const next = geologyPointFrame([center.lng, center.lat], [bounds.getEast() - bounds.getWest(), bounds.getNorth() - bounds.getSouth()]);
      setFrame(previous => previous?.join(",") === next.join(",") ? previous : next);
    };
    update();
    map.on("moveend", update);
    return () => { map.off("moveend", update); };
  }, [map, enabled, redacted]);

  if (!enabled || redacted || !map || !frame) return null;
  const frameKey = frame.join(",");
  // A different frame owns different requests, markers and selection. React
  // resets them together instead of resetting state from the loading effect.
  return <GeologyPointSample key={frameKey} map={map} frameKey={frameKey} monitoringVisible={monitoringVisible} />;
}

function GeologyPointSample({ map, frameKey, monitoringVisible }: { map: MapLibreMap; frameKey: string; monitoringVisible: boolean }) {
  const [sources, setSources] = useState<Record<ResourceKind, SourceState>>({ oilgas: EMPTY, minerals: EMPTY });
  const [loading, setLoading] = useState(true);
  const [selected, setSelected] = useState("");
  const rows = useMemo(() => [...sources.oilgas.rows, ...sources.minerals.rows], [sources]);
  const selectedRow = rows.find(row => row.id === selected);

  useEffect(() => {
    const controller = new AbortController();
    const load = async (kind: ResourceKind): Promise<SourceState> => {
      try {
        const response = await fetch(`/api/subsurface/resources?${new URLSearchParams({ kind, bounds: frameKey })}`, { signal: controller.signal, cache: "no-store" });
        if (!response.ok) throw new Error("Source unavailable");
        const value = await readBoundedJson(response, 1_000_000, controller.signal) as SourceResult;
        if (!Array.isArray(value.rows) || value.rows.length > 200 || typeof value.partial !== "boolean") throw new Error("Invalid source response");
        return { rows: value.rows, partial: value.partial, error: false };
      } catch { return { ...EMPTY, error: true }; }
    };
    void Promise.all([load("oilgas"), load("minerals")]).then(([oilgas, minerals]) => {
      if (!controller.signal.aborted) { setSources({ oilgas, minerals }); setLoading(false); }
    });
    return () => controller.abort();
  }, [frameKey]);

  useEffect(() => {
    const data: GeoJSON.FeatureCollection = { type: "FeatureCollection", features: rows.map(row => ({
      type: "Feature", geometry: { type: "Point", coordinates: row.coordinates },
      properties: { id: row.id, kind: row.id.startsWith("oilgas:") ? "oilgas" : "minerals", selected: row.id === selected },
    })) };
    const draw = () => {
      if (!map.isStyleLoaded()) return;
      if (!map.getSource(SOURCE_ID)) map.addSource(SOURCE_ID, { type: "geojson", data });
      else (map.getSource(SOURCE_ID) as GeoJSONSource).setData(data);
      if (!map.getLayer(GEOLOGY_POINT_LAYER_ID)) map.addLayer({ id: GEOLOGY_POINT_LAYER_ID, type: "circle", source: SOURCE_ID, paint: {
        "circle-radius": ["case", ["get", "selected"], 8, 5],
        "circle-color": ["match", ["get", "kind"], "oilgas", "#ef9d51", "minerals", "#bd92e4", "#ffffff"],
        "circle-stroke-color": "#10212d", "circle-stroke-width": 1.8,
      } });
    };
    const click = (event: MapMouseEvent) => {
      if (!map.getLayer(GEOLOGY_POINT_LAYER_ID)) return;
      const hit = map.queryRenderedFeatures(event.point, { layers: [GEOLOGY_POINT_LAYER_ID] })[0];
      if (typeof hit?.properties?.id === "string") setSelected(hit.properties.id);
    };
    draw();
    map.on("styledata", draw);
    map.on("click", click);
    return () => {
      map.off("styledata", draw); map.off("click", click);
      try { if (map.getLayer(GEOLOGY_POINT_LAYER_ID)) map.removeLayer(GEOLOGY_POINT_LAYER_ID); if (map.getSource(SOURCE_ID)) map.removeSource(SOURCE_ID); } catch { /* Style may already be gone. */ }
    };
  }, [map, rows, selected]);

  return <aside className={s.card} aria-label="Geology source points">
    <strong>2D SOURCE POINTS · LOCAL SAMPLE</strong>
    <div className={s.key}>{monitoringVisible && <span><i className={s.monitoring} /> Monitoring wells</span>}<span><i className={s.well} /> Oil &amp; gas · {sources.oilgas.rows.length}</span><span><i className={s.mine} /> Mines · {sources.minerals.rows.length}</span></div>
    <p role="status">{loading ? "Loading local source points…" : "Select a point for its 2D record details."}</p>
    {!loading && (sources.oilgas.error || sources.minerals.error) && <p>One or more KGS resource sources are unavailable in this view.</p>}
    <details className={s.coverage}><summary>Coverage &amp; core records</summary>
      <p>Oil and gas wells and mines are a bounded local sample: at most the first 200 records per source. Zoom in to inspect a smaller area. An empty sample is not proof of no records.</p>
      <p>Core inventory points remain held pending the Site’s separate release review. <a href="https://www.kgs.ku.edu/Magellan/CoreLibrary/" target="_blank" rel="noreferrer">KGS core library ↗</a></p>
      <p>The source of this material is the Kansas Geological Survey website at http://www.kgs.ku.edu/. All Rights Reserved.</p>
    </details>
    {selectedRow && <div className={s.detail}>
      <button type="button" onClick={() => setSelected("")} aria-label="Close point details">×</button>
      <h3>{selectedRow.name}</h3><p>{selectedRow.material} · recorded {selectedRow.status}</p>
      <p>{selectedRow.coordinates[1].toFixed(5)}° N, {Math.abs(selectedRow.coordinates[0]).toFixed(5)}° W · source position</p>
      <dl>{selectedRow.details.map(([name, value]) => <div key={name}><dt>{name}</dt><dd>{value}</dd></div>)}</dl>
      <p>{selectedRow.id.startsWith("oilgas:") ? RESOURCE_SOURCES.oilgas.limitation : RESOURCE_SOURCES.minerals.limitation}</p>
      <a href={selectedRow.id.startsWith("oilgas:") ? RESOURCE_SOURCES.oilgas.link : RESOURCE_SOURCES.minerals.link} target="_blank" rel="noreferrer">KGS source and methods ↗</a>
    </div>}
  </aside>;
}
