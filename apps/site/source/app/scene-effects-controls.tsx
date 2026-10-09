"use client";
import { useEffect, useRef, useState } from "react";
import { SCENE_EFFECT_OPTIONS, SCENE_LOOK_PRESETS, matchingLookPreset, type SceneEffectSettings, type SceneLight, type SceneLookPreset, type SceneView } from "./scene-effects";

const compass = (degrees: number) => ["N", "NE", "E", "SE", "S", "SW", "W", "NW"][Math.round(((degrees % 360) + 360) % 360 / 45) % 8];
export const SCENE_VIEW_LABELS: Record<SceneView, string> = { "2d": "2D map", tilted: "Tilted map", terrain: "Terrain 3D", globe: "Globe" };

type ControlsProps = Readonly<{
  settings: SceneEffectSettings;
  light: SceneLight | null;
  efficient: boolean;
  reducedMotion: boolean;
  flyoverActive: boolean;
  view: SceneView;
  onChange: (next: SceneEffectSettings) => void;
  onFlyover: () => void;
}>;

/** Look presets, per-effect switches and the flyover launcher. Presentation settings only. */
export function SceneEffectsControls({ settings, light, efficient, reducedMotion, flyoverActive, view, onChange, onFlyover }: ControlsProps) {
  const preset = matchingLookPreset(settings);
  const sunReading = settings.sunSync && light && light.source !== "manual"
    ? light.source === "sun"
      ? `Sun ${Math.round(light.solarElevation ?? light.altitude)}° up in the ${compass(light.azimuth)}`
      : `Sun below the horizon (${Math.round(light.solarElevation ?? 0)}°) · cool night fill`
    : null;
  return <section className="scene-effects-controls" aria-labelledby="scene-effects-title">
    <header><span>CINEMATIC 3D</span><strong id="scene-effects-title">Scene effects</strong><em data-view={view}>{SCENE_VIEW_LABELS[view]}</em></header>
    <div className="scene-look-presets" role="radiogroup" aria-label="Scene look">
      {(Object.keys(SCENE_LOOK_PRESETS) as SceneLookPreset[]).map((id) => <button key={id} type="button" role="radio" aria-checked={preset === id} onClick={() => onChange(SCENE_LOOK_PRESETS[id].settings)}>
        <strong>{SCENE_LOOK_PRESETS[id].label}</strong><small>{SCENE_LOOK_PRESETS[id].detail}</small>
      </button>)}
    </div>
    <div className="scene-effects-switches">
      {SCENE_EFFECT_OPTIONS.map((option) => {
        const here = option.views.includes(view);
        const held = efficient && (option.key === "curtain" || option.key === "columns");
        const detail = held ? "Paused while Battery saver is on"
          : option.key === "sunSync" && sunReading ? sunReading
          : option.detail;
        return <label key={option.key} data-here={here || undefined} data-held={held || undefined}>
          <input type="checkbox" role="switch" checked={settings[option.key]} onChange={() => onChange({ ...settings, [option.key]: !settings[option.key] })} />
          <span>
            <strong>{option.label}{option.network && <i title="Requests display-DEM tiles while on"> · network</i>}</strong>
            <small aria-live={option.key === "sunSync" ? "polite" : undefined}>{detail}</small>
            <b>{here ? "Shows in this view" : `Shows in ${option.views.map((id) => SCENE_VIEW_LABELS[id]).join(", ")}`}</b>
          </span>
        </label>;
      })}
    </div>
    <button type="button" className="scene-effects-flyover" aria-pressed={flyoverActive} disabled={reducedMotion && !flyoverActive} onClick={onFlyover}>
      <span aria-hidden="true">{flyoverActive ? "■" : "✈"}</span>{flyoverActive ? "Stop flyover" : "Fly over Kansas"}
      <small>{reducedMotion ? "Unavailable with reduced motion" : flyoverActive ? "Or drag, scroll or press a key" : "Six landscapes in Terrain 3D · about a minute"}</small>
    </button>
    <p>Display effects only. Lighting, glow, relief and columns never change data, evidence, elevations or report values. Column heights encode the provider value shown on each point.</p>
  </section>;
}

type PanelProps = ControlsProps & Readonly<{
  onRepresentation: (mode: "2d" | "tilted" | "terrain" | "globe") => void;
}>;

/** Floating Scene button on the map, available in every view. */
export function ScenePanel(props: PanelProps) {
  const [open, setOpen] = useState(false);
  const root = useRef<HTMLDivElement>(null);
  const trigger = useRef<HTMLButtonElement>(null);
  useEffect(() => {
    if (!open) return;
    const outside = (event: PointerEvent) => { if (!root.current?.contains(event.target as Node)) setOpen(false); };
    const escape = (event: KeyboardEvent) => { if (event.key === "Escape") { event.stopPropagation(); setOpen(false); trigger.current?.focus(); } };
    document.addEventListener("pointerdown", outside);
    const node = root.current;
    node?.addEventListener("keydown", escape);
    return () => { document.removeEventListener("pointerdown", outside); node?.removeEventListener("keydown", escape); };
  }, [open]);
  const preset = matchingLookPreset(props.settings);
  return <div className="scene-panel" ref={root} data-open={open || undefined}>
    <button ref={trigger} type="button" className="scene-panel-trigger" aria-expanded={open} aria-controls="scene-panel-body"
      aria-label={`Scene look: ${preset ? SCENE_LOOK_PRESETS[preset].label : "Custom"}. Open scene effects`} title="Scene effects" onClick={() => setOpen(!open)}>
      <span aria-hidden="true">✦</span>
    </button>
    {open && <div id="scene-panel-body" className="scene-panel-body" role="dialog" aria-label="Scene effects">
      <div className="scene-panel-views" role="group" aria-label="Map view">
        {(["2d", "tilted", "terrain", "globe"] as const).map((mode) => <button key={mode} type="button" aria-pressed={props.view === mode} onClick={() => props.onRepresentation(mode)}>
          <span aria-hidden="true">{mode === "2d" ? "▭" : mode === "tilted" ? "⟋" : mode === "terrain" ? "⛰" : "◎"}</span>{SCENE_VIEW_LABELS[mode]}
        </button>)}
      </div>
      <SceneEffectsControls {...props} />
    </div>}
  </div>;
}
