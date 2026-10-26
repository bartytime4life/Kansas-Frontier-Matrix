"use client";

import type { CSSProperties } from "react";
import type { CategoryMap, CategoryScene } from "./category-maps";
import type { SceneLight } from "./scene-effects";

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
 * Quarter-hour steps through the day for the time-of-day study. The last step
 * is 11:45 PM: a full fraction would be tomorrow's midnight, outside the day
 * the slider measures against.
 */
export const SUN_TIME_STEPS = 96;
/** Play the day restarts here once it has reached the end: 5:00 AM, before sunrise in every Kansas season. */
export const SUN_PLAY_RESTART_STEP = 20;

/** The day fraction of the next quarter-hour step, or null once the last step (11:45 PM) is reached. */
export function nextSunStep(dayFraction: number): number | null {
  const step = Math.min(SUN_TIME_STEPS - 1, Math.max(0, Math.floor((Number.isFinite(dayFraction) ? dayFraction : 0) * SUN_TIME_STEPS + 1e-9)));
  return step >= SUN_TIME_STEPS - 1 ? null : (step + 1) / SUN_TIME_STEPS;
}
const SUN_CLOCK = new Intl.DateTimeFormat("en-US", { timeZone: "America/Chicago", hour: "numeric", minute: "2-digit", timeZoneName: "short" });

/** Plain reading of the computed sun over the map center, at the time it was computed. */
export function sunReading(light: SceneLight, at: number): string {
  const time = Number.isFinite(at) ? ` · ${SUN_CLOCK.format(at)}` : "";
  return light.source === "sun"
    ? `${Math.round(light.solarElevation ?? light.altitude)}° up, from ${azimuthLabel(light.azimuth)}${time}`
    : `Below the horizon · night fill${time}`;
}

/**
 * The category map's own instrument panel: which map look is on, and the few
 * controls most explorations need. Every action reuses an existing Explorer
 * handler; the dock holds no map state of its own.
 */
export function CategoryMapDock({ look, mode, depth, azimuth, sun, terrainAvailable, onMode, onDepth, onAzimuth, onRealSun, onSunTime, sunPlaying, motionAllowed, onSunPlay, onTransect, onReset, onLayers, onClose }: Readonly<{
  look: CategoryMap;
  mode: CategoryScene;
  depth: number;
  azimuth: number;
  /**
   * The computed sun when the scene follows it; the hand-set light is then
   * ignored. `dayFraction` places `at` in its Kansas day; `live` is false while
   * the visitor studies another time of day.
   */
  sun: Readonly<{ light: SceneLight; at: number; dayFraction: number; live: boolean }> | null;
  terrainAvailable: boolean;
  onMode: (mode: CategoryScene) => void;
  onDepth: (value: number) => void;
  onAzimuth: (value: number) => void;
  onRealSun: (on: boolean) => void;
  /** A time of day as a fraction of today in Kansas, or null to follow the clock again. */
  onSunTime: (dayFraction: number | null) => void;
  /** Whether Play the day is sweeping the sun, and whether motion is allowed at all. */
  sunPlaying: boolean;
  motionAllowed: boolean;
  onSunPlay: (on: boolean) => void;
  /** Starts the terrain investigation for looks that offer the transect tool. */
  onTransect?: () => void;
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
    {mode !== "globe" && (sun
      ? <>
        <p className="category-map-dock-sun-reading" aria-live="polite"><span>{sun.live ? "Real sun" : "Sun at"}</span><output>{sunReading(sun.light, sun.at)}</output></p>
        <div className="category-map-dock-range category-map-dock-sun-time"><span id="category-map-dock-sun-time">Time</span>
          <input type="range" min={0} max={SUN_TIME_STEPS - 1} step={1} value={Math.min(SUN_TIME_STEPS - 1, Math.round(sun.dayFraction * SUN_TIME_STEPS))} aria-labelledby="category-map-dock-sun-time"
            aria-valuetext={sunReading(sun.light, sun.at)} onChange={event => onSunTime(Number(event.target.value) / SUN_TIME_STEPS)} />
          <button type="button" disabled={sun.live} onClick={() => onSunTime(null)} title="Follow the clock again">Now</button></div>
      </>
      : <label className="category-map-dock-range"><span>Sun from</span>
        <input type="range" min={0} max={355} step={5} value={Math.round(azimuth) % 360} aria-valuetext={`Light from ${azimuthLabel(azimuth)}, ${Math.round(azimuth)} degrees`} onChange={event => onAzimuth(Number(event.target.value))} />
        <output>{azimuthLabel(azimuth)}</output></label>)}
    {mode !== "globe" && (sun
      ? <div className="category-map-dock-sun-actions">
        <button type="button" className="category-map-dock-sun" aria-pressed={sunPlaying && motionAllowed} disabled={!motionAllowed} onClick={() => onSunPlay(!sunPlaying)}
          title={motionAllowed ? "Sweep the sun through the rest of today in quarter-hour steps" : "Reduced motion is on; move Time by hand"}>{sunPlaying && motionAllowed ? "Pause" : "Play the day"}</button>
        <button type="button" className="category-map-dock-sun" aria-pressed={true} onClick={() => onRealSun(false)} title="Set the light direction by hand">Set light by hand</button>
      </div>
      : <button type="button" className="category-map-dock-sun" aria-pressed={false} onClick={() => onRealSun(true)} title="Light the map from where the sun is now over the map center">Use the real sun now</button>)}
    {look.tools?.includes("transect") && onTransect && <button type="button" className="category-map-dock-tool" disabled={!terrainAvailable} onClick={onTransect}
      title="Draw a line across the relief, then preview its elevation profile without the 3D exaggeration">Draw a cross-section</button>}
    <p className="category-map-dock-lede">{look.lede}</p>
    <div className="category-map-dock-actions">
      <button type="button" onClick={onReset}>Reset view</button>
      <button type="button" onClick={onLayers}>Layers for this map</button>
    </div>
  </section>;
}
