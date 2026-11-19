"use client";
import { useCallback, useEffect, useRef } from "react";
import type { MapUtilityView } from "./map-interface";
export const EXPLORER_CONTROL_SECTIONS = [
  ["scene", "Appearance"], ["measure", "Measure"],
] as const;
export const ADVANCED_CONTROL_SECTIONS = [
  ["inspect", "Inspect records"], ["compare", "Compare"], ["report", "Reports"],
  ["export", "Export"], ["import", "Import a file"], ["connections", "Sources"],
  ["history", "Historic maps"], ["diagnostics", "Diagnostics"],
] as const;
export function ExplorerControlsNavigation({ value, onChange }: { value: MapUtilityView; onChange: (view: MapUtilityView) => void }) {
  const advanced = ADVANCED_CONTROL_SECTIONS.find(([id]) => id === value);
  const advancedRef = useRef<HTMLDetailsElement>(null);
  const positionAdvanced = useCallback(() => {
    const disclosure = advancedRef.current;
    if (!disclosure?.open) return;
    const panel = disclosure.closest(".map-utility-panel");
    const menu = disclosure.querySelector<HTMLElement>("nav");
    if (!panel || !menu) return;
    const anchor = disclosure.getBoundingClientRect(), bounds = panel.getBoundingClientRect();
    const below = Math.max(0, Math.min(window.innerHeight, bounds.bottom) - anchor.bottom - 8);
    const above = Math.max(0, anchor.top - Math.max(0, bounds.top) - 8);
    // Prefer the usual downward menu when it fits; short panels need the space
    // above the summary. Scroll options within that space, keeping the heading.
    const upward = below < menu.scrollHeight && above > below;
    disclosure.dataset.placement = upward ? "above" : "below";
    disclosure.style.setProperty("--advanced-menu-height", `${Math.floor(upward ? above : below)}px`);
  }, []);
  useEffect(() => {
    const disclosure = advancedRef.current, panel = disclosure?.closest(".map-utility-panel");
    const observer = typeof ResizeObserver === "undefined" ? null : new ResizeObserver(positionAdvanced);
    if (panel) observer?.observe(panel);
    const heading = panel?.querySelector(".map-utility-heading");
    if (heading) observer?.observe(heading);
    if (disclosure) observer?.observe(disclosure);
    window.addEventListener("resize", positionAdvanced);
    return () => { observer?.disconnect(); window.removeEventListener("resize", positionAdvanced); };
  }, [positionAdvanced]);
  return <div className="explorer-controls-navigation">
    <nav className="map-utility-tabs" aria-label="Map control sections">{EXPLORER_CONTROL_SECTIONS.map(([id, title]) => <button key={id} type="button" aria-pressed={value === id} onClick={() => onChange(id)}>{title}</button>)}</nav>
    <details ref={advancedRef} className="explorer-advanced-navigation" onToggle={positionAdvanced}
      onKeyDownCapture={event => {
        if (event.key !== "Escape" || !event.currentTarget.open) return;
        // Native panel listeners run before React's bubble handler. Own this
        // nested dismissal during capture so the outer panel stays available.
        event.preventDefault(); event.stopPropagation();
        event.currentTarget.open = false;
        event.currentTarget.querySelector<HTMLElement>("summary")?.focus({ preventScroll: true });
      }}>
      <summary>Advanced tools{advanced && <span>{advanced[1]}</span>}</summary>
      <nav aria-label="Advanced map tools">
        {ADVANCED_CONTROL_SECTIONS.map(([id, title]) => <button key={id} type="button" aria-pressed={value === id}
          onClick={event => {
            onChange(id);
            const disclosure = event.currentTarget.closest("details");
            if (disclosure) { disclosure.open = false; disclosure.querySelector("summary")?.focus(); }
          }}>{title}</button>)}
      </nav>
    </details>
  </div>;
}
