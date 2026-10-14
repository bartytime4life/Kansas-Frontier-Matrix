"use client";
import type { MapUtilityView } from "./map-interface";
export const EXPLORER_CONTROL_SECTIONS = [
  ["navigate", "Explore"], ["scene", "Appearance"], ["measure", "Measure"],
] as const;
export const ADVANCED_CONTROL_SECTIONS = [
  ["inspect", "Inspect records"], ["compare", "Compare"], ["report", "Reports"],
  ["export", "Export"], ["import", "Import a file"], ["connections", "Sources"],
  ["history", "Historic maps"], ["diagnostics", "Diagnostics"],
] as const;
export function ExplorerControlsNavigation({ value, onChange }: { value: MapUtilityView; onChange: (view: MapUtilityView) => void }) {
  const advanced = ADVANCED_CONTROL_SECTIONS.find(([id]) => id === value);
  return <div className="explorer-controls-navigation">
    <nav className="map-utility-tabs" aria-label="Map control sections">{EXPLORER_CONTROL_SECTIONS.map(([id, title]) => <button key={id} type="button" aria-pressed={value === id} onClick={() => onChange(id)}>{title}</button>)}</nav>
    <details className="explorer-advanced-navigation"><summary>Advanced tools{advanced && <span>{advanced[1]}</span>}</summary><nav aria-label="Advanced map tools">{ADVANCED_CONTROL_SECTIONS.map(([id, title]) => <button key={id} type="button" aria-pressed={value === id} onClick={event => { onChange(id); const disclosure = event.currentTarget.closest("details"); if (disclosure) { disclosure.open = false; disclosure.querySelector("summary")?.focus(); } }}>{title}</button>)}</nav></details>
  </div>;
}
