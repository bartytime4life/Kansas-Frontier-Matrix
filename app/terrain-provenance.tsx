"use client";

import { useId, useMemo, useState } from "react";
import { filterTerrainWorkUnits, parseTerrainDiscovery, terrainDiagramBounds, TERRAIN_PROVENANCE_LINKS, TERRAIN_STUDY_BOUNDS, type TerrainExtent, type TerrainWorkUnit } from "./terrain-provenance-data";
import styles from "./terrain-provenance.module.css";

function ExtentDiagram({ projects, selected }: { projects: readonly TerrainWorkUnit[]; selected: TerrainWorkUnit | undefined }) {
  const id = useId();
  const extent = terrainDiagramBounds(projects);
  const x = (longitude: number) => 40 + (longitude - extent[0]) / (extent[2] - extent[0]) * 640;
  const y = (latitude: number) => 280 - (latitude - extent[1]) / (extent[3] - extent[1]) * 250;
  const rectangle = (value: TerrainExtent) => ({ x: x(value[0]), y: y(value[3]), width: x(value[2]) - x(value[0]), height: y(value[1]) - y(value[3]) });
  const plotted = projects.filter(item => item.geographicExtent);
  return <figure className={styles.figure}>
    <svg viewBox="0 0 720 330" role="img" aria-labelledby={`${id}-title ${id}-description`}>
      <title id={`${id}-title`}>Rectangular LiDAR dataset extents</title>
      <desc id={`${id}-description`}>{plotted.length} source-coordinate bounding boxes with reported EPSG 3857 or 4326 horizontal coordinates. Dashed gold rectangle is the approximate Kansas study area. These rectangles are not surveyed acquisition footprints and do not establish complete point coverage. {selected?.geographicExtent ? `Selected: ${selected.id}.` : "The selected record has no supported geographic extent."}</desc>
      {[0, .25, .5, .75, 1].map(fraction => {
        const longitude = extent[0] + fraction * (extent[2] - extent[0]);
        return <g key={fraction}><line x1={x(longitude)} x2={x(longitude)} y1="30" y2="280" className={styles.grid} /><text x={x(longitude)} y="306" textAnchor="middle">{Math.abs(longitude).toFixed(1)}°{longitude < 0 ? "W" : "E"}</text></g>;
      })}
      {[0, .5, 1].map(fraction => {
        const latitude = extent[1] + fraction * (extent[3] - extent[1]);
        return <g key={fraction}><line x1="40" x2="680" y1={y(latitude)} y2={y(latitude)} className={styles.grid} /><text x="5" y={y(latitude) - 5}>{Math.abs(latitude).toFixed(1)}°</text></g>;
      })}
      {plotted.map(item => <rect key={item.id} {...rectangle(item.geographicExtent!)} className={styles.extent}><title>{item.id}: rectangular dataset extent</title></rect>)}
      <rect {...rectangle(TERRAIN_STUDY_BOUNDS)} className={styles.study} />
      {selected?.geographicExtent && <rect {...rectangle(selected.geographicExtent)} className={styles.selected}><title>{selected.id}: selected dataset extent</title></rect>}
    </svg>
    <figcaption><span className={styles.legendStudy}>Approximate Kansas study bounds</span><span className={styles.legendExtent}>Dataset extent</span><span className={styles.legendSelected}>Selected work unit</span></figcaption>
    <p>{plotted.length} of {projects.length} matching work units can be positioned from their reported CRS. Rectangles show dataset bounds, not surveyed acquisition footprints, point density, or verified coverage.</p>
  </figure>;
}

export function TerrainProvenancePanel({ discovery }: { discovery?: unknown }) {
  const parsed = useMemo(() => parseTerrainDiscovery(discovery), [discovery]);
  const [query, setQuery] = useState("");
  const [selectedId, setSelectedId] = useState("");
  const id = useId();
  const filtered = useMemo(() => filterTerrainWorkUnits(parsed?.projects ?? [], query), [parsed, query]);
  const selected = filtered.find(item => item.id === selectedId) ?? filtered[0];
  return <section className={styles.panel} aria-labelledby={`${id}-heading`}>
    <header className={styles.heading}><div><span className={styles.eyebrow}>Terrain provenance</span><h2 id={`${id}-heading`}>Inspect the LiDAR work units</h2></div><span className={styles.badge}>Candidate metadata · not admitted</span></header>
    <p>Inspect public USGS work-unit records before choosing terrain data. This viewer does not fetch point clouds or establish which work unit supplied the current terrain mosaic.</p>
    <div className={styles.sourceLinks}><a href={TERRAIN_PROVENANCE_LINKS.catalog} target="_blank" rel="noreferrer">Public LiDAR catalog</a><a href={TERRAIN_PROVENANCE_LINKS.program} target="_blank" rel="noreferrer">USGS 3DEP program</a></div>
    {!parsed ? <p className={styles.notice} role="status">{discovery === undefined ? "Load a 3DEP discovery.json to inspect its work units and source-coordinate extents." : "This file is not a supported 3DEP discovery snapshot. No work units or extents are displayed."}</p> : <>
      <div className={styles.summary}><strong>{parsed.projects.length} work units</strong><span>Captured {new Date(parsed.capturedAt).toISOString().replace("T", " ").replace(/\.\d+Z$/, " UTC")}</span><span>{parsed.completeForPrefix ? "KS_ prefix listing captured" : "Partial or incomplete KS_ prefix listing"}</span></div>
      <p className={styles.notice}>Selection uses provider IDs beginning <code>KS_</code>. Cross-state projects may be absent; this is not a spatially complete Kansas inventory. A year in a work-unit name is not an asserted acquisition date.{parsed.rejectedProjects > 0 ? ` ${parsed.rejectedProjects} invalid or duplicate metadata records were excluded.` : ""}</p>
      <div className={styles.controls}><label htmlFor={`${id}-search`}>Find a work unit<input id={`${id}-search`} type="search" value={query} onChange={event => setQuery(event.target.value)} placeholder="Search provider ID" /></label><label htmlFor={`${id}-selection`}>Matching work units<select id={`${id}-selection`} value={selected?.id ?? ""} onChange={event => setSelectedId(event.target.value)} disabled={!filtered.length}>{filtered.length ? filtered.map(item => <option key={item.id} value={item.id}>{item.id}</option>) : <option value="">No matching work units</option>}</select></label></div>
      {!selected ? <p role="status">No matching work units. Clear the search to return to the captured records.</p> : <>
        <ExtentDiagram projects={filtered} selected={selected} />
        <article className={styles.record} aria-label="Selected work-unit provenance">
          <h3>{selected.id}</h3>
          <dl className={styles.facts}>
            <div><dt>Acquisition period</dt><dd>{selected.acquisitionStart && selected.acquisitionEnd ? `${selected.acquisitionStart} to ${selected.acquisitionEnd}` : "Not reported"}</dd></div>
            <div><dt>Vertical datum</dt><dd>Not independently verified</dd></div>
            <div><dt>Reported horizontal CRS</dt><dd>{selected.horizontalCrs ?? "Not reported"}</dd></div>
            <div><dt>Reported vertical CRS</dt><dd>{selected.verticalCrs ?? "Not reported"}</dd></div>
            <div><dt>Provider point count</dt><dd>{selected.pointCount === null ? "Not reported" : selected.pointCount.toLocaleString("en-US")}</dd></div>
            <div><dt>Point-cloud download size</dt><dd>Not measured by this metadata snapshot</dd></div>
          </dl>
          {(!selected.acquisitionStart || !selected.acquisitionEnd) && <p>{selected.acquisitionReason}</p>}
          <details><summary>Source metadata and integrity</summary><p><a href={selected.sourceUrl} target="_blank" rel="noreferrer">Open this work unit’s EPT metadata</a> · {selected.metadataBytes.toLocaleString("en-US")} captured metadata bytes.</p><p>Recorded metadata SHA-256: <code>{selected.metadataSha256}</code>. The browser has not re-fetched or verified the provider bytes.</p><p>Native X/Y/Z bounds: {selected.nativeBounds ? selected.nativeBounds.map(n => n.toLocaleString("en-US", { maximumFractionDigits: 3 })).join(", ") : "Not available"}.</p><p>{selected.geographicExtent ? `Displayed rectangle: ${selected.geographicExtent.map(n => n.toFixed(5)).join(", ")} (west, south, east, north). ${selected.horizontalCrs === "EPSG:3857" ? "Converted from reported Web Mercator X/Y bounds." : "Reported longitude/latitude X/Y bounds."}` : "No extent is plotted: the captured bounds or horizontal CRS are unsupported or missing."} Reported CRS codes do not establish vertical accuracy, survey quality, or compatible datums.</p></details>
        </article>
      </>}
    </>}
  </section>;
}
