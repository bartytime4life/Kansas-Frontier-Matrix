"use client";

import { useEffect, useState } from "react";
import type { OfficialContextId, OfficialContextSource } from "./live-context";
import { MAP_STARTERS, contextSelectionChanges, readContextPreference, starterPlan, writeContextPreference,
  type ContextSelection, type StarterAccessMap } from "./map-starters";

export function MapStartersControl({ sources, access, visibility, selectionReady, sourceStatus, onApply, onRetry, onChooseTime, onUse2D, onBrowse }: Readonly<{
  sources: readonly OfficialContextSource[]; access: StarterAccessMap; visibility: ContextSelection; selectionReady: boolean;
  sourceStatus: (id: OfficialContextId) => string;
  onApply: (ids: readonly OfficialContextId[], title: string) => void;
  onRetry?: (id: OfficialContextId) => void;
  onChooseTime?: () => void;
  onUse2D?: () => void;
  onBrowse?: () => void;
}>) {
  const [choice, setChoice] = useState<string>("learning-kansas");
  const [remember, setRemember] = useState(false);
  const [storageReady, setStorageReady] = useState(false);
  const [message, setMessage] = useState("");
  useEffect(() => {
    let cancelled = false;
    // Hydrate optional browser state after the first render; keep the server shell deterministic.
    void Promise.resolve().then(() => {
      if (cancelled) return;
      setRemember(readContextPreference(sources) !== null);
      setStorageReady(true);
    });
    return () => { cancelled = true; };
  }, [sources]);
  useEffect(() => {
    if (!remember || !storageReady || !selectionReady) return;
    let cancelled = false;
    // Coalesce transient selection changes; cancelled effects never save an older stack.
    void Promise.resolve().then(() => {
      if (cancelled) return;
      if (!writeContextPreference(sources.filter(source => visibility[source.id]).map(source => source.id), sources)) {
        setRemember(false);
        setMessage("Browser storage is unavailable. Your layers still work for this visit.");
      }
    });
    return () => { cancelled = true; };
  }, [remember, selectionReady, sources, storageReady, visibility]);
  const starter = MAP_STARTERS.find(item => item.id === choice) ?? MAP_STARTERS[2];
  const plan = starterPlan(starter.ids, sources, access);
  const matches = plan.selected.length > 0 && contextSelectionChanges(plan.selected, sources, visibility).length === 0;
  const apply = (ids: readonly OfficialContextId[], title: string) => {
    onApply(ids, title);
    setMessage(`${title}: ${ids.length} public context layers selected.${plan.skipped.length ? ` ${plan.skipped.length} starter sources skipped; see source status.` : ""} Use View selected layers to customize.`);
  };
  return <section className="map-starters" aria-labelledby="map-starters-title">
    <h2 id="map-starters-title">Start with a purpose</h2>
    <p id="map-starters-help">Choose a small public context stack, then customize individual layers. Reviewed layers and imagery keep their own selections.</p>
    <div className="map-starters-options" role="group" aria-label="Map purpose" aria-describedby="map-starters-help map-starters-description">
      {MAP_STARTERS.map(item => <button key={item.id} type="button" aria-pressed={starter.id === item.id} onClick={() => setChoice(item.id)}>{item.title}</button>)}
    </div>
    <p id="map-starters-description">{starter.description}</p>
    <div className="map-starters-actions">
      <button type="button" disabled={!selectionReady || plan.selected.length === 0} onClick={() => apply(plan.selected, starter.title)}>Use starter</button>
      <button type="button" disabled={!selectionReady} onClick={() => {
        onApply([], "Clear starter layers");
        setMessage("Public context layers cleared. Choose a starter or use Browse for individual layers.");
      }}>Clear context layers</button>
    </div>
    {onBrowse && <button type="button" className="map-starters-browse" onClick={onBrowse}>View selected layers</button>}
    {plan.skipped.some(item => access[item.id as OfficialContextId]?.held) && onChooseTime && <p className="map-starters-recovery">Some sources are held by this map time or representation. <button type="button" onClick={onChooseTime}>Choose map time</button>{onUse2D && <button type="button" onClick={onUse2D}>Use 2D map</button>}</p>}
    <p className="map-starters-selection">{matches ? "Public context matches this starter" : "Custom public context selection"} · {plan.selected.length} of {starter.ids.length} sources selectable</p>
    <details><summary>Sources &amp; limits</summary>
      <p>External context only · selection does not create a KFM evidence release.</p>
      <ul>{starter.ids.map(id => {
        const source = sources.find(item => item.id === id), skipped = plan.skipped.find(item => item.id === id);
        return <li key={id}><strong>{source?.shortTitle ?? id}</strong><span>{skipped?.reason ?? sourceStatus(id)}</span>
          {source && access[source.id]?.unavailable && onRetry && <button type="button" onClick={() => onRetry(source.id)}>Retry {source.shortTitle}</button>}
          {source && <small>{source.freshness}{access[id]?.guidance ? ` · ${access[id]?.guidance}` : ""}</small>}</li>;
      })}</ul>
      <p>{starter.limitation}</p>
    </details>
    <label className="map-starters-remember"><input type="checkbox" checked={remember} disabled={!storageReady || !selectionReady} onChange={event => {
      const enabled = event.target.checked;
      setRemember(enabled);
      if (!enabled) setMessage(writeContextPreference(null, sources) ? "Saved layer preference removed. Current layers stay selected." : "Browser storage could not remove the saved preference. Clear this site's browser data to remove it.");
      else setMessage("Remembering public layer IDs in this browser only. No account, location or personal details are saved by this option.");
    }} />Remember my context layers on this device</label>
    <p className="map-starters-privacy">Saves only public layer IDs. Shared map links take precedence. Uncheck to forget; clearing context layers also saves an empty stack when enabled.</p>
    <p role="status" aria-live="polite" aria-atomic="true">{message}</p>
  </section>;
}
