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
export function DomainStage({ topic, paused = false, reduced = false, layersVisible = true, aviationMode = '3d', expanded = false, onGeologyModule, onPreviewState }) {
 const host = useRef(null), engine = useRef(null), latest = useRef({ topic, paused, reduced, layersVisible, aviationMode });
 const [state, setState] = useState('loading'), [sources, setSources] = useState(null);
 const [Geology, setGeology] = useState(null), [geologyReady, setGeologyReady] = useState(false), [geologyFailed, setGeologyFailed] = useState(false);
 const [Spotlight, setSpotlight] = useState(null), [map, setMap] = useState(null), [spotPlaced, setSpotPlaced] = useState(false);
 // A category hint owns no second map or Underground worker. Its source and
 // diagram chunk are requested only after a settled Geology selection.
 useEffect(() => {
  let current = true;
  if (topic !== 'geology') return;
  const timer = setTimeout(() => {
   import('./GeologyGlimpse.jsx').then(module => {
    if (current) { setGeology(() => module.GeologyGlimpse); setGeologyReady(true); setGeologyFailed(false); onGeologyModule?.({ Component: module.GeologyGlimpse }); }
   }).catch(() => { if (current) { setGeologyReady(false); setGeologyFailed(true); onGeologyModule?.({ failed: true }); } });
   // Real wells, cores and mines popping up on the map; optional, so a failure only leaves the map.
   import('./SubsurfaceSpotlight.jsx').then(module => { if (current) setSpotlight(() => module.SubsurfaceSpotlight); }).catch(() => {});
  }, 220);
  return () => { current = false; clearTimeout(timer); };
 }, [topic, onGeologyModule]);
 useEffect(() => {
  let cancelled = false, idle = null, started = false;
  const hidden = () => typeof document !== 'undefined' && document.hidden;
  const unavailable = () => { if (!cancelled) { setState('unavailable'); onPreviewState?.({ mapState: 'unavailable' }); } };
  const boot = () => {
   idle = null;
   if (cancelled || started || hidden()) return;
   started = true;
   return import('./map-engine.mjs').then(({ createWelcomeMap }) => {
   if (cancelled || !host.current) return null;
   if (hidden()) { started = false; return null; }
   return createWelcomeMap(host.current, {
    onReady: () => { if (!cancelled) setState('ready'); },
    onError: unavailable,
    onSources: value => { if (!cancelled) { if (value.mapState === 'unavailable' || value.mapState === 'loading') setState(value.mapState); setSources(value); onPreviewState?.(value); } },
   });
  }).then(instance => {
   if (!instance) return;
   if (cancelled) { instance.dispose(); return; }
   engine.current = instance; setMap({ engine: instance, host: host.current });
   const { topic: id, paused: stopped, reduced: still, layersVisible: visible, aviationMode: mode } = latest.current;
   instance.setAviationMode(mode); instance.setReduced(still); instance.setPaused(stopped); instance.setLayersVisible(visible); instance.show(id);
  }).catch(unavailable);
  };
  const cancelBoot = () => {
   if (idle === null) return;
   if (typeof window.cancelIdleCallback === 'function') window.cancelIdleCallback(idle); else clearTimeout(idle);
   idle = null;
  };
  const scheduleBoot = () => {
   if (hidden()) { cancelBoot(); return; }
   if (cancelled || started || idle !== null) return;
   if (typeof window.requestIdleCallback === 'function') idle = window.requestIdleCallback(boot, { timeout: 900 });
   else idle = setTimeout(boot, 120);
  };
  if (typeof document !== 'undefined') document.addEventListener('visibilitychange', scheduleBoot);
  scheduleBoot();
  return () => {
   cancelled = true;
   cancelBoot();
   if (typeof document !== 'undefined') document.removeEventListener('visibilitychange', scheduleBoot);
   engine.current?.dispose(); engine.current = null; setMap(null);
  };
 }, [onPreviewState]);
 // The latest props also seed the engine when it finishes loading.
 useEffect(() => { latest.current = { topic, paused, reduced, layersVisible, aviationMode }; }, [topic, paused, reduced, layersVisible, aviationMode]);
 useEffect(() => { engine.current?.show(topic); }, [topic]);
 useEffect(() => { engine.current?.setLayersVisible(layersVisible); }, [layersVisible]);
 useEffect(() => { engine.current?.setAviationMode(aviationMode); }, [aviationMode]);
 useEffect(() => { engine.current?.setPaused(paused); }, [paused]);
 useEffect(() => { engine.current?.setReduced(reduced); }, [reduced]);
 const view = welcomeView(topic);
 const shown = sources?.topic === view.topic ? sources.sources.filter(source => ['records', 'dated-frame', 'map-layer'].includes(source.state))
  .map(source => `${OFFICIAL_CONTEXT_BY_ID[source.id]?.shortTitle ?? source.id}${source.observedAt ? ` · ${source.product === 'visible' ? 'visible-band' : source.product === 'geocolor' ? 'GeoColor' : 'scan'} ${RADAR_TIME.format(new Date(source.observedAt))}` : ''}`) : [];
 return <div className="domain-stage" data-state={state} data-topic={view.topic ?? 'kansas'}>
  <div ref={host} className="domain-stage-map" />
  {topic==='geology'&&Spotlight&&map&&<Spotlight engine={map.engine} host={map.host} paused={paused} reduced={reduced} expanded={expanded} onPlaced={setSpotPlaced}/>}
  {/* The single-log specimen stays until a spotlight record actually fits on screen. */}
  {expanded&&topic==='geology'&&!(Spotlight&&map&&spotPlaced)&&geologyReady&&Geology&&<Geology paused={paused} reduced={reduced} expanded={expanded}/>}
  {expanded&&topic==='geology'&&geologyFailed&&<p className="welcome-geology-module-failure" role="status">Recorded log preview unavailable. Open Underground to check source status.</p>}
  <p className="domain-stage-caption"><span>Map preview · provider context</span><strong key={view.topic ?? 'kansas'}>{view.name}</strong><small>{view.topic==='aviation'?`${aviationMode==='3d'?'3D volumes · 1× heights':aviationMode==='slice'?'4,000 ft MSL slice':'2D chart'} · Pinned FAA reference; weather, traffic, drone grids and TFRs are separate.`:view.detail}</small>{shown.length>0&&<small className="domain-stage-data">Preview layers: {shown.join(' · ')}</small>}<small className="domain-stage-credit">{BASEMAPS[view.basemap].note}</small></p>
 </div>;
}
