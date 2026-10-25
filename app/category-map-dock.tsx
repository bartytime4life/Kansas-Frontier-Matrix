"use client";

import type { CSSProperties } from "react";
import type { CategoryMap, CategoryScene } from "./category-maps";

const MODES: readonly (readonly [CategoryScene, string, string])[] = [
  ["2d", "2D", "Flat map, straight down"],
  ["terrain", "3D", "Tilted 3D terrain"],
  ["globe", "Globe", "Whole-Earth globe"],
];

/** Compass label for a light azimuth (the direction the light comes from). */
export function azimuthLabel(degrees: number): string {
  const names = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"];
  return names[Math.round((((degrees % 360) + 360) % 360) / 45) % 8];
}

/**
 * The category map's own instrument panel: which map look is on, and the few
 * controls most explorations need. Every action reuses an existing Explorer
 * handler; the dock holds no map state of its own.
 */
export function CategoryMapDock({ look, mode, depth, azimuth, terrainAvailable, onMode, onDepth, onAzimuth, onReset, onLayers, onClose }: Readonly<{
  look: CategoryMap;
  mode: CategoryScene;
  depth: number;
  azimuth: number;
  terrainAvailable: boolean;
  onMode: (mode: CategoryScene) => void;
  onDepth: (value: number) => void;
  onAzimuth: (value: number) => void;
  onReset: () => void;
  onLayers: () => void;
  onClose: () => void;
}>) {
  const swatch = { "--m0": look.swatch[0], "--m1": look.swatch[1], "--m2": look.swatch[2] } as CSSProperties;
  return <section className="category-map-dock" aria-label={`${look.name} controls`} data-mode={mode} style={swatch}>
    <header>
      <span className="category-map-dock-swatch" aria-hidden="true" />
      <div><strong>{look.name}</strong><small>{mode === "terrain" ? "3D terrain" : mode === "globe" ? "Globe" : "2D map"} · display context</small></div>
      <button type="button" className="category-map-dock-close" aria-label={`Hide ${look.name} controls`} onClick={onClose}>×</button>
    </header>
    <div className="category-map-dock-modes" role="group" aria-label="View">
      {MODES.map(([value, label, title]) => <button key={value} type="button" aria-pressed={mode === value} title={title}
        disabled={value === "terrain" && !terrainAvailable} onClick={() => onMode(value)}>{label}</button>)}
    </div>
    {mode === "terrain" && <label className="category-map-dock-range"><span>Relief</span>
      <input type="range" min={0.5} max={3} step={0.1} value={depth} aria-valuetext={`${depth.toFixed(1)} times vertical exaggeration`} onChange={event => onDepth(Number(event.target.value))} />
      <output>{depth.toFixed(1)}×</output></label>}
    {mode !== "globe" && <label className="category-map-dock-range"><span>Sun from</span>
      <input type="range" min={0} max={355} step={5} value={Math.round(azimuth) % 360} aria-valuetext={`Light from ${azimuthLabel(azimuth)}, ${Math.round(azimuth)} degrees`} onChange={event => onAzimuth(Number(event.target.value))} />
      <output>{azimuthLabel(azimuth)}</output></label>}
    <p className="category-map-dock-lede">{look.lede}</p>
    <div className="category-map-dock-actions">
      <button type="button" onClick={onReset}>Reset view</button>
      <button type="button" onClick={onLayers}>Layers for this map</button>
    </div>
  </section>;
}
