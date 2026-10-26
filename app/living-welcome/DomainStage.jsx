import { useEffect, useRef, useState } from 'react';
import { BASEMAPS } from '../map-runtime';
import { OFFICIAL_CONTEXT_BY_ID } from '../live-context';
import { welcomeView } from '../welcome-map-view';

const RADAR_TIME = new Intl.DateTimeFormat('en-US', { timeZone: 'America/Chicago', hour: 'numeric', minute: '2-digit', timeZoneName: 'short' });

/**
 * Full-window live map for the selected domain: the real map that topic opens
 * with (basemap, view, camera and its starter data), drifting slowly while the
 * welcome plays.
 * The map engine loads after the welcome has painted; until then (or without
 * WebGL) the stage stays a quiet backdrop and the caption still names the map.
 */
export function DomainStage({ topic, paused = false, reduced = false }) {
 const host = useRef(null), engine = useRef(null), latest = useRef({ topic, paused, reduced });
 const [state, setState] = useState('loading'), [radarAt, setRadarAt] = useState(null);
 useEffect(() => {
  let cancelled = false, idle = 0;
  const boot = () => import('./map-engine.mjs').then(({ createWelcomeMap }) => {
   if (cancelled || !host.current) return null;
   return createWelcomeMap(host.current, { onReady: () => { if (!cancelled) setState('ready'); }, onError: () => { if (!cancelled) setState('unavailable'); }, onRadar: at => { if (!cancelled) setRadarAt(at); } });
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
 // Name only the data drawn at the preview's zoom; closer-zoom layers wait for the opened map.
 // Radar is named, with its scan time, only while a current scan is drawn.
 const shown = view.starters.map(id => OFFICIAL_CONTEXT_BY_ID[id]).filter(source => source && (source.minDisplayZoom ?? 0) <= view.camera.zoom && (source.id !== 'nws-radar' || radarAt))
  .map(source => source.id === 'nws-radar' ? `${source.shortTitle} · scan ${RADAR_TIME.format(new Date(radarAt))}` : source.shortTitle);
 return <div className="domain-stage" data-state={state} data-topic={view.topic ?? 'kansas'}>
  <div ref={host} className="domain-stage-map" />
  <p className="domain-stage-caption"><span>Live map preview</span><strong key={view.topic ?? 'kansas'}>{view.name}</strong><small>{view.detail}</small>{shown.length>0&&<small className="domain-stage-data">Showing {shown.join(' · ')}</small>}<small className="domain-stage-credit">{BASEMAPS[view.basemap].note}</small></p>
 </div>;
}
