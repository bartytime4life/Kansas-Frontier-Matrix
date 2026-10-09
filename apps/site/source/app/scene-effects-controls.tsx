"use client";
import { useEffect, useId, useRef, useState } from "react";
import { KANSAS_FLYOVER, SCENE_EFFECT_OPTIONS, SCENE_LOOK_PRESETS, matchingLookPreset, type SceneEffectSettings, type SceneLight, type SceneLookPreset, type SceneView } from "./scene-effects";
import { SCENE_RECIPES, compositionDefaults, matchingSceneRecipe, normalizedBearing, type SceneComposition, type ScenePresentation, type SceneRecipe } from "./scene-studio";

import { TERRAIN_SLOPE_LEGEND, TERRAIN_ASPECT_LEGEND, TERRAIN_SURFACE_FLAT_DEGREES, terrainAspectDirection } from "./terrain-surface";
import type { TerrainSurfaceMode, TerrainSurfaceProbe, TerrainDrawingMode, TerrainDrawingStatus } from "./terrain-drawing";
import type { TerrainSourceRecord } from "./terrain-sources";

const compass = (degrees: number) => ["N", "NE", "E", "SE", "S", "SW", "W", "NW"][Math.round(((degrees % 360) + 360) % 360 / 45) % 8];
export const SCENE_VIEW_LABELS: Record<SceneView, string> = { "2d": "2D map", tilted: "Tilted map", terrain: "Terrain 3D", globe: "Globe" };

type ControlsProps = Readonly<{
  settings: SceneEffectSettings;
  light: SceneLight | null;
  efficient: boolean;
  reducedMotion: boolean;
  flyoverActive: boolean;
  view: SceneView;
  presentation: Omit<ScenePresentation, "settings">;
  camera: SceneComposition;
  cameraReady: boolean;
  onRecipe: (recipe: SceneRecipe) => void;
  onLight: (light: Omit<ScenePresentation, "settings">) => void;
  onCamera: (patch: Partial<SceneComposition>, reset?: boolean) => void;
  onChange: (next: SceneEffectSettings) => void;
  onFlyover: () => void;
  drawing?: Readonly<{
    mode: TerrainDrawingMode;
    detail: boolean;
    status: TerrainDrawingStatus;
    source: TerrainSourceRecord;
    onMode: (mode: TerrainDrawingMode) => void;
    onDetail: (detail: boolean) => void;
  }>;
  surface?: Readonly<{
    mode: TerrainSurfaceMode;
    opacity: number;
    probe: TerrainSurfaceProbe | null;
    probeEnabled: boolean;
    onMode: (mode: TerrainSurfaceMode) => void;
    onOpacity: (opacity: number) => void;
    onProbeCenter: () => void;
  }>;
  exploration?: Readonly<{
    orbiting: boolean;
    onOrbit: () => void;
    onLandscape: (id: string) => void;
  }>;
}>;

/** An atlas cinematographer's studio. All controls share the real renderer state. */
export function SceneEffectsControls({ settings, light, efficient, reducedMotion, flyoverActive, view, presentation, camera, cameraReady, onRecipe, onLight, onCamera, onChange, onFlyover, drawing, surface, exploration }: ControlsProps) {
  const id = useId();
  const mode = matchingLookPreset(settings);
  const recipe = matchingSceneRecipe({ ...presentation, settings });
  const defaults = compositionDefaults(view);
  const surfaceActive = Boolean(surface && surface.mode !== "off");
  const drawingActive = Boolean(drawing && (drawing.mode !== "off" || surfaceActive));
  const surfaceLegend = surface?.mode === "aspect" ? TERRAIN_ASPECT_LEGEND : TERRAIN_SLOPE_LEGEND;
  const validCells = drawing?.status.validCellCount;
  const totalCells = drawing?.status.totalCellCount;
  const cellCoverage = typeof validCells === "number" && typeof totalCells === "number" && totalCells > 0
    ? `${Math.round(validCells / totalCells * 100)}% · ${validCells.toLocaleString()} / ${totalCells.toLocaleString()}` : "—";
  const sunReading = settings.sunSync && light && light.source !== "manual"
    ? light.source === "sun"
      ? `Sun ${Math.round(light.solarElevation ?? light.altitude)}° up in the ${compass(light.azimuth)}`
      : `Sun below the horizon (${Math.round(light.solarElevation ?? 0)}°) · cool night fill`
    : null;
  return <section className="scene-effects-controls" aria-labelledby={`${id}-title`}
    onPointerDown={(event) => event.stopPropagation()} onClick={(event) => event.stopPropagation()}
    onDoubleClick={(event) => event.stopPropagation()} onWheel={(event) => event.stopPropagation()} onKeyDown={(event) => event.stopPropagation()}>
    <header><div><span>LIGHT / LAND / LENS</span><strong id={`${id}-title`}>Scene studio</strong></div><em data-view={view}>{SCENE_VIEW_LABELS[view]}</em></header>
    <div className="scene-studio-status"><span>Presentation light</span><strong aria-live="polite">{settings.sunSync ? "Following the sun" : recipe ? SCENE_RECIPES[recipe].label : "Custom"}</strong></div>
    <div className="scene-recipe-grid" role="group" aria-label="Presentation looks">
      {(Object.keys(SCENE_RECIPES) as SceneRecipe[]).map((key) => <button key={key} type="button" data-look={key} aria-pressed={recipe === key} onClick={() => onRecipe(key)}>
        <span className="scene-recipe-art" aria-hidden="true"><i /><b /><em /></span>
        <span className="scene-recipe-copy"><strong>{SCENE_RECIPES[key].label}</strong><small>{SCENE_RECIPES[key].detail}</small></span>
        <span className="scene-recipe-mark" aria-hidden="true">{recipe === key ? "✓" : "+"}</span>
      </button>)}
    </div>
    {drawing && <section className="scene-terrain-drawing" aria-labelledby={`${id}-drawing`}>
      <header><strong id={`${id}-drawing`}>Terrain drawing</strong><span>{drawing.source.organization === "U.S. Geological Survey" ? "USGS 3DEP" : "Mapzen DEM"}</span></header>
      <div className="scene-drawing-modes" role="group" aria-label="Terrain drawing mode">
        {([ ["off", "Off"], ["contours", "Contours"], ["grid", "Surface grid"], ["both", "Both"] ] as const).map(([value, label]) => <button key={value} type="button" aria-pressed={drawing.mode === value} onClick={() => drawing.onMode(value)}>{label}</button>)}
      </div>
      {surface && <div className="scene-surface-choice"><strong>Surface color</strong>
        <div className="scene-surface-modes" role="group" aria-label="Surface color">
          {([["off", "Off"], ["slope", "Slope"], ["aspect", "Facing direction"]] as const).map(([value, label]) => <button key={value} type="button" aria-pressed={surface.mode === value} onClick={() => surface.onMode(value)}>{label}</button>)}
        </div>
      </div>}
      <p className="scene-drawing-status" role="status" data-state={drawing.status.state}>{drawingActive ? drawing.status.message : "Loaded display DEM · gaps stay empty"}</p>
      {drawingActive && <>
        <dl className="scene-drawing-readings" data-mode={drawing.mode}>
          {drawing.mode !== "grid" && drawing.mode !== "off" && <div><dt>Contour interval</dt><dd>{drawing.status.intervalMeters === null ? "—" : `${drawing.status.intervalMeters.toLocaleString()} m`}</dd></div>}
          <div><dt>Sample spacing</dt><dd>{drawing.status.spacingMeters === null ? "—" : `${Math.round(drawing.status.spacingMeters).toLocaleString()} m`}</dd></div>
          <div><dt>Valid samples</dt><dd>{drawing.status.state === "ready" ? `${Math.round(drawing.status.coverage * 100)}%` : "—"}</dd></div>
        </dl>
        <small className="scene-drawing-boundary">Local patch around the camera. Loaded display DEM · gaps stay empty.</small>
      </>}
      {surface && surfaceActive && <section className="scene-surface-lens" aria-label="Surface color legend and sample">
        <div className="scene-surface-legend" data-mode={surface.mode}>
          <strong>{surface.mode === "slope" ? "Approximate slope · degrees" : "Downhill facing direction"}</strong>
          <ul aria-label={surface.mode === "slope" ? "Slope color legend" : "Facing direction color legend"}>{surfaceLegend.map((entry) => <li key={entry.key}><i aria-hidden="true" style={{ backgroundColor: entry.color }} /><span>{entry.label}</span></li>)}</ul>
          <small>{surface.mode === "slope" ? "Fixed degree bands; colors do not change with scene light." : `Compass direction, not sun exposure. Flat includes slopes below ${TERRAIN_SURFACE_FLAT_DEGREES}° with no stable direction.`}</small>
        </div>
        <div className="scene-studio-range scene-surface-strength"><label htmlFor={`${id}-surface-opacity`}>Color strength</label><output htmlFor={`${id}-surface-opacity`}>{Math.round(surface.opacity * 100)}%</output>
          <input id={`${id}-surface-opacity`} type="range" min="20" max="75" step="1" value={Math.round(surface.opacity * 100)} aria-valuetext={`${Math.round(surface.opacity * 100)} percent`} onChange={(event) => surface.onOpacity(Number(event.target.value) / 100)} />
        </div>
        <p className="scene-surface-coverage"><span>Valid surface cells</span><strong>{cellCoverage}</strong></p>
        <section className="scene-surface-probe" aria-labelledby={`${id}-surface-sample`}>
          <header><strong id={`${id}-surface-sample`}>Surface sample</strong><span>Approximate cell</span></header>
          <div aria-live="polite" aria-atomic="true">{surface.probe && surface.probeEnabled ? <dl>
            <div><dt>Slope</dt><dd>{surface.probe.slopeDegrees.toFixed(1)}°</dd></div>
            <div><dt>Faces</dt><dd>{surface.probe.aspectDegrees === null ? "Flat / no direction" : terrainAspectDirection(surface.probe.aspectDegrees)}</dd></div>
            <div><dt>Elevation</dt><dd>{Math.round(surface.probe.elevationMeters).toLocaleString()} m</dd></div>
          </dl> : <p>{surface.probeEnabled ? "Point or tap a colored cell, or sample the view center." : "Sampling is paused while a measurement tool is active."}</p>}</div>
          <button type="button" disabled={!surface.probeEnabled || !cameraReady || drawing.status.state !== "ready"} onClick={surface.onProbeCenter}>Sample view center</button>
          <small>Loaded display DEM cell estimates. Elevation is the unexaggerated center sample; slope and facing use its neighbors. Not a survey or site-suitability reading.</small>
        </section>
        <p className="scene-surface-density">Sample spacing is density, not source accuracy. Missing neighborhoods stay uncolored.</p>
      </section>}
      <details className="scene-drawing-provenance"><summary>Sampling &amp; source limits</summary>
        <label className="scene-drawing-detail"><input type="checkbox" checked={drawing.detail} disabled={efficient} onChange={(event) => drawing.onDetail(event.target.checked)} /><span>Finer drawing<small>{efficient ? "Battery saver uses fewer samples" : "More samples in the same local patch"}</small></span></label>
        <p>Spacing is sampling density, not source accuracy. Contours show unexaggerated display elevations; every fifth contour is emphasized.</p>
        <p><strong>{drawing.source.title}</strong><br />{drawing.source.resolution}</p>
        <p>{drawing.source.boundary}</p>
        <a href={drawing.source.sourceUrl} target="_blank" rel="noreferrer">Display DEM source ↗</a>
      </details>
    </section>}
    <fieldset className="scene-studio-light"><legend>Light direction</legend>
      <label className="scene-studio-sun"><input type="checkbox" checked={settings.sunSync} onChange={() => onChange({ ...settings, sunSync: !settings.sunSync })} />Follow real sun</label>
      <div className="scene-studio-range"><label htmlFor={`${id}-light`}>{settings.sunSync ? "Computed light" : "Manual light"}</label><output htmlFor={`${id}-light`}>{Math.round(settings.sunSync && light ? light.azimuth : presentation.azimuth)}° · {compass(settings.sunSync && light ? light.azimuth : presentation.azimuth)}</output>
        <input id={`${id}-light`} aria-label="Scene light direction" type="range" min="0" max="359" step="1" value={settings.sunSync && light ? light.azimuth : presentation.azimuth} disabled={settings.sunSync} onChange={(event) => onLight({ ...presentation, azimuth: Number(event.target.value) })} />
      </div>
      {sunReading && <small className="scene-studio-sun-reading">{sunReading}</small>}
    </fieldset>
    <fieldset className="scene-studio-camera" disabled={!cameraReady}><legend>Compose the view</legend>
      <div className="scene-studio-camera-grid">
        <div className="scene-studio-range"><label htmlFor={`${id}-tilt`}>Tilt</label><output htmlFor={`${id}-tilt`}>{Math.round(camera.pitch)}°</output><input id={`${id}-tilt`} type="range" min="0" max={view === "terrain" ? 72 : 60} step="1" value={camera.pitch} disabled={view === "globe"} aria-valuetext={`${Math.round(camera.pitch)} degrees${view === "globe" ? ", fixed on globe" : ""}`} onChange={(event) => onCamera({ pitch: Number(event.target.value) })} /></div>
        <div className="scene-studio-range"><label htmlFor={`${id}-lens`}>Lens · field of view</label><output htmlFor={`${id}-lens`}>{Math.round(camera.fieldOfView)}°</output><input id={`${id}-lens`} type="range" min="20" max="60" step="1" value={camera.fieldOfView} aria-valuetext={`${Math.round(camera.fieldOfView)} degrees vertical field of view`} onChange={(event) => onCamera({ fieldOfView: Number(event.target.value) })} /></div>
        <div className="scene-studio-range scene-studio-bearing"><label htmlFor={`${id}-bearing`}>Orientation</label><output htmlFor={`${id}-bearing`}>{Math.round(normalizedBearing(camera.bearing))}° · {compass(camera.bearing)}</output><input id={`${id}-bearing`} type="range" min="-180" max="180" step="1" value={normalizedBearing(camera.bearing)} onChange={(event) => onCamera({ bearing: Number(event.target.value) })} /></div>
      </div>
      <div className="scene-studio-reset"><small>{cameraReady ? view === "globe" ? "Globe keeps a level camera." : "Drag the map to compose, too." : "Waiting for the map camera…"}</small><button type="button" title={`North up · ${defaults.pitch}° tilt · ${defaults.fieldOfView}° lens. Keeps location and zoom.`} onClick={() => onCamera(defaults, true)}>Reset composition ↺</button></div>
    </fieldset>
    {exploration && <details className="scene-studio-details scene-landscape-exploration"><summary>Kansas landscapes <span>6 viewpoints</span></summary>
      <p>Go straight to a landscape in Terrain 3D. Keep your light, lens, basemap and display scale.</p>
      <div className="scene-landscape-list" role="group" aria-label="Kansas landscape viewpoints">
        {KANSAS_FLYOVER.filter((stop) => stop.id !== "return").map((stop, index) => <button key={stop.id} type="button" disabled={!cameraReady} onClick={() => exploration.onLandscape(stop.id)}>
          <span aria-hidden="true">{String(index + 1).padStart(2, "0")}</span><span><strong>{stop.id === "statewide" ? "Kansas overview" : stop.label}</strong><small>{stop.region}</small></span><b aria-hidden="true">↗</b>
        </button>)}
      </div>
    </details>}
    {exploration && <button type="button" className="scene-orbit-action" aria-pressed={exploration.orbiting} disabled={!exploration.orbiting && (reducedMotion || view === "globe" || !cameraReady)} onClick={exploration.onOrbit}>
      <span aria-hidden="true">{exploration.orbiting ? "■" : "◌"}</span><span><strong>{exploration.orbiting ? "Stop orbit" : "Orbit this view"}</strong><small>{reducedMotion ? "Paused with reduced motion" : view === "globe" ? "Use Tilted map or Terrain 3D" : exploration.orbiting ? "Drag, scroll or press a key to take over" : "A slow 90° turn · 12 seconds"}</small></span>
    </button>}
    <button type="button" className="scene-effects-flyover" aria-pressed={flyoverActive} disabled={reducedMotion && !flyoverActive} onClick={onFlyover}>
      <span aria-hidden="true">{flyoverActive ? "■" : "✈"}</span>{flyoverActive ? "Stop flyover" : "Fly over Kansas"}
      <small>{reducedMotion ? "Unavailable with reduced motion" : flyoverActive ? "Or drag, scroll or press a key" : "Six landscapes in Terrain 3D · about a minute"}</small>
    </button>
    <details className="scene-studio-details"><summary>Effects &amp; rendering <span>{mode ? SCENE_LOOK_PRESETS[mode].label : "Custom"}</span></summary>
      <div className="scene-look-presets" role="group" aria-label="Scene effect mode">
        {(Object.keys(SCENE_LOOK_PRESETS) as SceneLookPreset[]).map((key) => <button key={key} type="button" aria-pressed={mode === key} onClick={() => onChange(SCENE_LOOK_PRESETS[key].settings)}>
          <strong>{SCENE_LOOK_PRESETS[key].label}</strong><small>{SCENE_LOOK_PRESETS[key].detail}</small>
        </button>)}
      </div>
      <div className="scene-effects-switches">
        {SCENE_EFFECT_OPTIONS.filter((option) => option.key !== "sunSync").map((option) => {
          const here = option.views.includes(view);
          const held = efficient && (option.key === "curtain" || option.key === "columns");
          return <label key={option.key} data-here={here || undefined} data-held={held || undefined}>
            <input type="checkbox" role="switch" checked={settings[option.key]} onChange={() => onChange({ ...settings, [option.key]: !settings[option.key] })} />
            <span><strong>{option.label}{option.network && <i title="Requests display-DEM tiles while on"> · network</i>}</strong><small>{held ? "Paused while Battery saver is on" : option.detail}</small><b>{here ? "Shows in this view" : `Shows in ${option.views.map((key) => SCENE_VIEW_LABELS[key]).join(", ")}`}</b></span>
          </label>;
        })}
      </div>
    </details>
    <p>Presentation only. Looks change light, never source dates, weather or elevations. Enabled effects stay your choice. Columns use provider values.</p>
  </section>;
}

type PanelProps = ControlsProps & Readonly<{ onRepresentation: (mode: SceneView) => void; onOpenChange?: (open: boolean) => void }>;

/** Floating Scene button on the map, available in every view. */
export function ScenePanel(props: PanelProps) {
  const id = useId();
  const [open, setOpen] = useState(false);
  const root = useRef<HTMLDivElement>(null);
  const trigger = useRef<HTMLButtonElement>(null);
  const onOpenChange = props.onOpenChange;
  useEffect(() => { onOpenChange?.(open); }, [onOpenChange, open]);
  useEffect(() => {
    if (!open) return;
    const outside = (event: PointerEvent) => {
      if (root.current?.contains(event.target as Node)) return;
      // Keep the reading visible while a map tap samples the displayed surface.
      // This does not consume the event: evidence picking and map gestures still run.
      if (props.surface?.mode !== undefined && props.surface.mode !== "off" && props.surface.probeEnabled
        && event.target instanceof Element && event.target.matches("canvas.maplibregl-canvas")) return;
      setOpen(false);
    };
    const escape = (event: KeyboardEvent) => { if (event.key === "Escape") { event.stopPropagation(); setOpen(false); trigger.current?.focus(); } };
    document.addEventListener("pointerdown", outside);
    const node = root.current;
    node?.addEventListener("keydown", escape);
    return () => { document.removeEventListener("pointerdown", outside); node?.removeEventListener("keydown", escape); };
  }, [open, props.surface?.mode, props.surface?.probeEnabled]);
  const recipe = matchingSceneRecipe({ ...props.presentation, settings: props.settings });
  const label = props.settings.sunSync ? "Following the sun" : recipe ? SCENE_RECIPES[recipe].label : "Custom";
  return <div className="scene-panel" ref={root} data-open={open || undefined}
    onPointerDown={(event) => event.stopPropagation()} onClick={(event) => event.stopPropagation()} onDoubleClick={(event) => event.stopPropagation()} onWheel={(event) => event.stopPropagation()}>
    <button ref={trigger} type="button" className="scene-panel-trigger" aria-expanded={open} aria-controls={`${id}-body`}
      aria-label={`Scene look: ${label}. Open scene effects`} title="Scene studio" onClick={() => setOpen(!open)}>
      <span aria-hidden="true">✦</span><small>Scene</small>
    </button>
    {open && <div id={`${id}-body`} className="scene-panel-body" role="dialog" aria-label="Scene effects">
      <div className="scene-panel-views" role="group" aria-label="Map view">
        {(["2d", "tilted", "terrain", "globe"] as const).map((mode) => <button key={mode} type="button" aria-pressed={props.view === mode} onClick={() => props.onRepresentation(mode)}>
          <span aria-hidden="true">{mode === "2d" ? "▭" : mode === "tilted" ? "⟋" : mode === "terrain" ? "⛰" : "◎"}</span>{SCENE_VIEW_LABELS[mode]}
        </button>)}
      </div>
      <SceneEffectsControls {...props} />
    </div>}
  </div>;
}
