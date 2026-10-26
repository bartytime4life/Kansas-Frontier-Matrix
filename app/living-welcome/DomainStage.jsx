import { useEffect, useRef, useState } from 'react';
import { BASEMAPS } from '../map-runtime';
import { welcomeView } from '../welcome-map-view';

/**
 * Full-window live map for the selected domain: the real map that topic opens
 * with (basemap, view and camera), drifting slowly while the welcome plays.
 * The map engine loads after the welcome has painted; until then (or without
 * WebGL) the stage stays a quiet backdrop and the caption still names the map.
 */
export function DomainStage({ topic, paused = false, reduced = false }) {
 const host = useRef(null), engine = useRef(null), latest = useRef({ topic, paused, reduced });
 const [state, setState] = useState('loading');
 useEffect(() => {
  let cancelled = false, idle = 0;
  const boot = () => import('./map-engine.mjs').then(({ createWelcomeMap }) => {
   if (cancelled || !host.current) return null;
   return createWelcomeMap(host.current, { onReady: () => { if (!cancelled) setState('ready'); }, onError: () => { if (!cancelled) setState('unavailable'); } });
  }).then(instance => {
   if (!instance) return;
   if (cancelled) { instance.dispose(); return; }
   engine.current = instance;
   const { topic: id, paused: stopped, reduced: still } = latest.current;
   instance.setReduced(still); instance.setPaused(stopped); instance.show(id);
  }).catch(() => { if (!cancelled) setState('unavailable'); });
  if (typeof window.requestIdleCallback === 'function') idle = window.requestIdleCallback(boot, { timeout: 900 });
  else idle = setTimeout(boot, 120);
  return () => {
   cancelled = true;
   if (typeof window.cancelIdleCallback === 'function') window.cancelIdleCallback(idle); else clearTimeout(idle);
   engine.current?.dispose(); engine.current = null;
  };
 }, []);
 // The latest props also seed the engine when it finishes loading.
 useEffect(() => { latest.current = { topic, paused, reduced }; engine.current?.show(topic); }, [topic, paused, reduced]);
 useEffect(() => { engine.current?.setPaused(paused); }, [paused]);
 useEffect(() => { engine.current?.setReduced(reduced); }, [reduced]);
 const view = welcomeView(topic);
 return <div className="domain-stage" data-state={state} data-topic={view.topic ?? 'kansas'}>
  <div ref={host} className="domain-stage-map" />
  <p className="domain-stage-caption"><span>Live map preview</span><strong key={view.topic ?? 'kansas'}>{view.name}</strong><small>{view.detail}</small><small className="domain-stage-credit">{BASEMAPS[view.basemap].note}</small></p>
 </div>;
}
