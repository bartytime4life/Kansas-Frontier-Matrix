"use client";

import s from "./geology-layer-controls.module.css";

export type GeologyPointKind = "well" | "core" | "oilgas" | "minerals";
export type GeologyPointVisibility = Readonly<Record<GeologyPointKind, boolean>>;
export type GeologyEarthquakeMode = "recent" | "record" | "off";

const rows: readonly { id: GeologyPointKind; name: string; source: string }[] = [
  { id: "well", name: "WWC5 wells", source: "KGS well-completion locator" },
  { id: "core", name: "Core samples", source: "KGS Core Library locator" },
  { id: "oilgas", name: "Oil & gas wells", source: "KGS source counts and locations" },
  { id: "minerals", name: "Mine locations", source: "KGS source counts and locations" },
];

export function GeologyLayerControls({ visibility, onVisibility, earthquakeMode, onEarthquakeMode, onUnderground, counts, recentTime, compact = false }: Readonly<{
  visibility: GeologyPointVisibility;
  onVisibility: (kind: GeologyPointKind, shown: boolean) => void;
  earthquakeMode: GeologyEarthquakeMode;
  onEarthquakeMode: (mode: GeologyEarthquakeMode) => void;
  onUnderground: () => void;
  counts?: Partial<Record<GeologyPointKind, string>>;
  recentTime?: string | null;
  compact?: boolean;
}>) {
  return <section className={s.controls} data-compact={compact} aria-label="Geology layers">
    <div className={s.heading}><strong>MAP LAYERS</strong><span>Source locations · Kansas 2D</span></div>
    <div className={s.rows}>{rows.map(row => <label className={s.row} key={row.id} data-visible={visibility[row.id]}>
      <input type="checkbox" checked={visibility[row.id]} onChange={event => onVisibility(row.id, event.target.checked)} aria-label={`Show ${row.name}`} />
      <i className={s[row.id]} aria-hidden="true" />
      <span><strong>{row.name}</strong><small>{counts?.[row.id] ?? row.source}</small></span>
    </label>)}</div>
    <fieldset className={s.earthquakes}><legend>Earthquakes · USGS</legend>
      <label><input type="radio" name={compact ? "geology-quakes-card" : "geology-quakes-panel"} checked={earthquakeMode === "recent"} onChange={() => onEarthquakeMode("recent")} /> {recentTime ? `Archive day ${recentTime}` : "Past 30 days"}</label>
      <label><input type="radio" name={compact ? "geology-quakes-card" : "geology-quakes-panel"} checked={earthquakeMode === "record"} onChange={() => onEarthquakeMode("record")} /> 1973+ · M2.5+</label>
      <label><input type="radio" name={compact ? "geology-quakes-card" : "geology-quakes-panel"} checked={earthquakeMode === "off"} onChange={() => onEarthquakeMode("off")} /> Off</label>
    </fieldset>
    <button type="button" className={s.underground} onClick={onUnderground}>Open Underground workspace <span aria-hidden="true">↗</span></button>
    {!compact && <p className={s.note}>Underground has well logs, core inventories, and a resource picker. Map marks are source positions, not surveyed borehole paths.</p>}
  </section>;
}
