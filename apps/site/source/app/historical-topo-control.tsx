"use client";

import { useEffect, useMemo, useState, type FormEvent } from "react";
import type { FeatureCollection, Polygon } from "geojson";
import { readBoundedJson } from "./bounded-json";
import { TOPO_PAGE_SIZE, type TopoSearch, type TopoSheet } from "./historical-topo";
import type { GeoJSONSource, Map as MapLibreMap } from "./maplibre-seam";

const SOURCE = "kfm-historical-topo-footprint";
const FILL = "kfm-historical-topo-footprint-fill";
const LINE = "kfm-historical-topo-footprint-line";
const empty: FeatureCollection<Polygon> = { type: "FeatureCollection", features: [] };
type CatalogResponse = { state: string; sheets: TopoSheet[]; more: boolean; retrievedAt: string; message?: string };

export function HistoricalTopoControl({ map, styleReady, locationPrivate }: { map: MapLibreMap | null; styleReady: boolean; locationPrivate: boolean }) {
  const [from, setFrom] = useState("1930");
  const [through, setThrough] = useState("1960");
  const [scale, setScale] = useState<TopoSearch["scale"]>("all");
  const [name, setName] = useState("");
  const [search, setSearch] = useState<TopoSearch>(() => {
    const center = map?.getCenter();
    return { lng: center?.lng ?? -98.4, lat: center?.lat ?? 38.5, from: 1930, through: 1960, scale: "all", name: "", offset: 0 };
  });
  const [rows, setRows] = useState<TopoSheet[]>([]);
  const [selectedId, setSelectedId] = useState<number | null>(null);
  const [more, setMore] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [retrievedAt, setRetrievedAt] = useState("");
  const [retry, setRetry] = useState(0);
  const selected = useMemo(() => rows.find((row) => row.id === selectedId) ?? null, [rows, selectedId]);

  useEffect(() => {
    if (locationPrivate) return;
    const controller = new AbortController();
    const params = new URLSearchParams(Object.entries(search).map(([key, value]) => [key, String(value)]));
    void (async () => {
      await Promise.resolve();
      if (controller.signal.aborted) return;
      setLoading(true);
      setError("");
      try {
        const response = await fetch(`/api/historical-topo?${params}`, { signal: controller.signal });
        const body = await readBoundedJson(response, 512 * 1024) as CatalogResponse;
        if (!response.ok || body.state !== "available" || !Array.isArray(body.sheets)) throw new Error(body.message || "USGS catalog unavailable.");
        if (controller.signal.aborted) return;
        setRows((current) => search.offset === 0 ? body.sheets : [...current, ...body.sheets.filter((sheet) => !current.some((known) => known.id === sheet.id))]);
        setMore(body.more);
        setRetrievedAt(body.retrievedAt);
        setError("");
      } catch (cause) {
        if (!controller.signal.aborted) setError(cause instanceof Error ? cause.message : "USGS catalog unavailable.");
      } finally { if (!controller.signal.aborted) setLoading(false); }
    })();
    return () => controller.abort();
  }, [search, retry, locationPrivate]);

  useEffect(() => {
    if (!map || !styleReady) return;
    try {
      if (!map.getSource(SOURCE)) map.addSource(SOURCE, { type: "geojson", data: empty });
      if (!map.getLayer(FILL)) map.addLayer({ id: FILL, type: "fill", source: SOURCE, paint: { "fill-color": "#f4cf7b", "fill-opacity": 0, "fill-opacity-transition": { duration: 220 } } });
      if (!map.getLayer(LINE)) map.addLayer({ id: LINE, type: "line", source: SOURCE, paint: { "line-color": "#f8df9e", "line-width": 2.3, "line-opacity": 0, "line-opacity-transition": { duration: 220 } } });
    } catch { return; }
    return () => {
      try {
        if (map.getLayer(LINE)) map.removeLayer(LINE);
        if (map.getLayer(FILL)) map.removeLayer(FILL);
        if (map.getSource(SOURCE)) map.removeSource(SOURCE);
      } catch { /* A basemap change may already have removed this temporary overlay. */ }
    };
  }, [map, styleReady]);

  useEffect(() => {
    if (!map || !styleReady) return;
    const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    try {
      if (reducedMotion) {
        map.setPaintProperty(FILL, "fill-opacity-transition", { duration: 0 });
        map.setPaintProperty(LINE, "line-opacity-transition", { duration: 0 });
      }
      map.setPaintProperty(FILL, "fill-opacity", 0);
      map.setPaintProperty(LINE, "line-opacity", 0);
    } catch { return; }
    const timer = window.setTimeout(() => {
      try {
        (map.getSource(SOURCE) as GeoJSONSource | undefined)?.setData(selected ? { type: "FeatureCollection", features: [selected.footprint] } : empty);
        if (selected) {
          map.setPaintProperty(FILL, "fill-opacity", 0.1);
          map.setPaintProperty(LINE, "line-opacity", 0.95);
        }
      } catch { /* Style replacement may have removed the temporary source. */ }
    }, reducedMotion ? 0 : 130);
    return () => window.clearTimeout(timer);
  }, [map, styleReady, selected]);

  function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const center = map?.getCenter();
    if (!center || locationPrivate) return;
    const start = Number(from), end = Number(through);
    if (!Number.isInteger(start) || !Number.isInteger(end) || start < 1800 || end > 2100 || start > end) {
      setError("Choose a valid year range from 1800 to 2100.");
      return;
    }
    setSelectedId(null);
    setMore(false);
    setSearch({ lng: center.lng, lat: center.lat, from: start, through: end, scale, name: name.trim(), offset: 0 });
    setRetry((value) => value + 1);
  }

  function fitSheet(sheet: TopoSheet) {
    if (!map) return;
    const points = sheet.footprint.geometry.coordinates.flat();
    const west = Math.min(...points.map((point) => point[0]));
    const east = Math.max(...points.map((point) => point[0]));
    const south = Math.min(...points.map((point) => point[1]));
    const north = Math.max(...points.map((point) => point[1]));
    const compact = window.innerWidth <= 760;
    map.fitBounds([[west, south], [east, north]], {
      padding: compact ? { top: 55, left: 30, right: 30, bottom: Math.round(window.innerHeight * 0.48) } : { top: 80, left: 80, right: 480, bottom: 80 },
      maxZoom: 12, duration: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? 0 : 650,
    });
  }

  return <section className="map-utility-section historical-topo-control" aria-label="Historical topographic sheets">
    <div className="map-utility-section-heading"><span>USGS TOPOVIEW CATALOG</span><h3>Find a real map edition</h3><p>Search near the map center by sheet name, printed year, and scale. Select a result to see its actual catalog footprint at map scale.</p></div>
    <form className="historical-topo-search" onSubmit={submit}>
      <label className="historical-topo-name">Sheet name <input type="search" maxLength={40} value={name} onChange={(event) => setName(event.target.value)} placeholder="Any name near map center" /></label>
      <div className="historical-topo-range"><label>From year <input type="number" min="1800" max="2100" step="1" value={from} onChange={(event) => setFrom(event.target.value)} /></label><label>Through year <input type="number" min="1800" max="2100" step="1" value={through} onChange={(event) => setThrough(event.target.value)} /></label></div>
      <label>Map scale <select value={scale} onChange={(event) => setScale(event.target.value as TopoSearch["scale"])}><option value="all">Any scale</option><option value="24000">1:24,000</option><option value="62500">1:62,500</option><option value="125000">1:125,000</option><option value="250000">1:250,000</option></select></label>
      <button type="submit" disabled={loading || locationPrivate || !map}>Search near map center</button>
    </form>
    {locationPrivate && <div className="map-utility-boundary" data-tone="privacy"><strong>Private location</strong><p>Use Fit Kansas before searching. This prevents a browser-location-derived camera from being sent to the USGS catalog.</p></div>}
    <div className="historical-topo-status" role="status" aria-live="polite">{locationPrivate ? "Search held while map location is private." : loading ? `Checking USGS catalog…${rows.length ? " Previous results remain below." : ""}` : error ? `${error}${rows.length ? " Previous search results remain below." : ""}` : `${rows.length} sheet${rows.length === 1 ? "" : "s"} shown${more ? " · more available" : ""} near ${search.lat.toFixed(2)}°, ${search.lng.toFixed(2)}°`}</div>
    {rows.length > 0 && <div className="historical-topo-results" aria-label="Historical map editions" aria-busy={loading}>{rows.map((sheet) => <button key={sheet.id} type="button" className="historical-topo-result" disabled={loading} aria-pressed={selectedId === sheet.id} onClick={() => setSelectedId(sheet.id)}><span className="historical-topo-year">{sheet.year}</span><span><strong>{sheet.name}, {sheet.state}</strong><small>1:{sheet.scale.toLocaleString()} · {sheet.series} · scan {sheet.scanId}</small></span><span aria-hidden="true">⌖</span></button>)}</div>}
    {more && search.offset < 240 && <button className="historical-topo-more" type="button" disabled={loading} onClick={() => setSearch((current) => ({ ...current, offset: current.offset + TOPO_PAGE_SIZE }))}>Show more editions</button>}
    {more && search.offset >= 240 && <p className="historical-topo-limit">More catalog sheets may exist. Narrow the years, scale, name, or map area to continue.</p>}
    {!loading && !error && rows.length === 0 && <div className="map-utility-empty"><strong>No catalog sheets match</strong><p>Widen the years, remove the name filter, or move the map. An empty search does not establish that no historical map exists.</p></div>}
    {selected && <article className="historical-topo-detail"><header><span>SELECTED USGS SHEET</span><strong>{selected.name} · {selected.year}</strong></header><dl><div><dt>Printed map year</dt><dd>{selected.year}</dd></div><div><dt>Imprint year</dt><dd>{selected.imprintYear ?? "Not listed"}</dd></div><div><dt>Scale</dt><dd>1:{selected.scale.toLocaleString()}</dd></div><div><dt>Scan ID</dt><dd>{selected.scanId}</dd></div><div><dt>Datum</dt><dd>{selected.datum}</dd></div></dl><div className="historical-topo-actions"><button type="button" onClick={() => fitSheet(selected)}>Fit actual footprint</button><a href={selected.viewerHref} target="_blank" rel="noreferrer">Open USGS TopoView ↗</a></div><p>The outline shows catalog coverage, not scanned map pixels. TopoView provides the original preview, metadata, and downloads.</p></article>}
    <aside className="map-utility-boundary"><strong>Historical map context</strong><p>USGS edition and imprint years do not date every road, river, or feature printed on a sheet. This browser is external context only; it does not add a KFM evidence record or change the active map time.</p><a href="https://ngmdb.usgs.gov/topoview/help/" target="_blank" rel="noreferrer">How USGS TopoView works ↗</a>{retrievedAt && <small>Catalog checked {new Date(retrievedAt).toLocaleString()}</small>}</aside>
  </section>;
}
