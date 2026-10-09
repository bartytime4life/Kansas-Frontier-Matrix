"use client";
import type { SceneEffectSettings, SceneLight } from "./scene-effects";

const compass = (degrees: number) => ["N", "NE", "E", "SE", "S", "SW", "W", "NW"][Math.round(((degrees % 360) + 360) % 360 / 45) % 8];

/** Cinematic 3D toggles and the flyover launcher. Presentation settings only. */
export function SceneEffectsControls({ settings, light, efficient, reducedMotion, flyoverActive, onChange, onFlyover }: {
  settings: SceneEffectSettings;
  light: SceneLight | null;
  efficient: boolean;
  reducedMotion: boolean;
  flyoverActive: boolean;
  onChange: (next: SceneEffectSettings) => void;
  onFlyover: () => void;
}) {
  const toggle = (key: keyof SceneEffectSettings) => onChange({ ...settings, [key]: !settings[key] });
  const sunReading = settings.sunSync && light && light.source !== "manual"
    ? light.source === "sun"
      ? `Sun ${Math.round(light.solarElevation ?? light.altitude)}° up in the ${compass(light.azimuth)}`
      : `Sun below the horizon (${Math.round(light.solarElevation ?? 0)}°) · cool night fill`
    : "Uses the manual light and direction";
  return <section className="scene-effects-controls" aria-labelledby="scene-effects-title">
    <header><span>CINEMATIC 3D</span><strong id="scene-effects-title">Scene effects</strong></header>
    <div className="scene-effects-switches">
      <label><input type="checkbox" role="switch" checked={settings.cinematic} onChange={() => toggle("cinematic")} /><span><strong>Cinematic relief &amp; sky</strong><small>Deeper relief shading, richer sky and distance haze</small></span></label>
      <label data-held={efficient || undefined}><input type="checkbox" role="switch" checked={settings.curtain} onChange={() => toggle("curtain")} /><span><strong>Kansas light curtain</strong><small>{efficient ? "Paused while Battery saver is on" : "Glowing border walls when the map is tilted"}</small></span></label>
      <label><input type="checkbox" role="switch" checked={settings.sunSync} onChange={() => toggle("sunSync")} /><span><strong>Follow the real sun</strong><small aria-live="polite">{sunReading}</small></span></label>
    </div>
    <button type="button" className="scene-effects-flyover" aria-pressed={flyoverActive} disabled={reducedMotion && !flyoverActive} onClick={onFlyover}>
      <span aria-hidden="true">{flyoverActive ? "■" : "✈"}</span>{flyoverActive ? "Stop flyover" : "Fly over Kansas"}
      <small>{reducedMotion ? "Unavailable with reduced motion" : flyoverActive ? "Or drag, scroll or press a key" : "Six landscapes in Terrain 3D · about a minute"}</small>
    </button>
    <p>Display effects only. Lighting, haze and walls never change data, evidence, elevations or report values.</p>
  </section>;
}
