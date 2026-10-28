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
export function DomainStage({ topic, paused = false, reduced = false, layersVisible = true, onPreviewState }) {
 const host = useRef(null), engine = useRef(null), latest = useRef({ topic, paused, reduced, layersVisible });
 const [state, setState] = useState('loading'), [sources, setSources] = useState(null);
 useEffect(() => {
  let cancelled = false, idle = 0;
  const boot = () => import('./map-engine.mjs').then(({ createWelcomeMap }) => {
   if (cancelled || !host.current) return null;
   return createWelcomeMap(host.current, {
    onReady: () => { if (!cancelled) setState('ready'); },
    onError: () => { if (!cancelled) { setState('unavailable'); onPreviewState?.({ mapState: 'unavailable' }); } },
    onSources: value => { if (!cancelled) { if (value.mapState === 'unavailable' || value.mapState === 'loading') setState(value.mapState); setSources(value); onPreviewState?.(value); } },
   });
  }).then(instance => {
   if (!instance) return;
   if (cancelled) { instance.dispose(); return; }
   engine.current = instance;
   const { topic: id, paused: stopped, reduced: still, layersVisible: visible } = latest.current;
   instance.setReduced(still); instance.setPaused(stopped); instance.setLayersVisible(visible); instance.show(id);
  }).catch(() => { if (!cancelled) setState('unavailable'); });
  if (typeof window.requestIdleCallback === 'function') idle = window.requestIdleCallback(boot, { timeout: 900 });
  else idle = setTimeout(boot, 120);
  return () => {
   cancelled = true;
   if (typeof window.cancelIdleCallback === 'function') window.cancelIdleCallback(idle); else clearTimeout(idle);
   engine.current?.dispose(); engine.current = null;
  };
 }, [onPreviewState]);
 // The latest props also seed the engine when it finishes loading.
 useEffect(() => { latest.current = { topic, paused, reduced, layersVisible }; }, [topic, paused, reduced, layersVisible]);
 useEffect(() => { engine.current?.show(topic); }, [topic]);
 useEffect(() => { engine.current?.setLayersVisible(layersVisible); }, [layersVisible]);
 useEffect(() => { engine.current?.setPaused(paused); }, [paused]);
 useEffect(() => { engine.current?.setReduced(reduced); }, [reduced]);
 const view = welcomeView(topic);
 const shown = sources?.topic === view.topic ? sources.sources.filter(source => ['records', 'dated-frame', 'map-layer'].includes(source.state))
  .map(source => `${OFFICIAL_CONTEXT_BY_ID[source.id]?.shortTitle ?? source.id}${source.observedAt ? ` · ${source.product === 'visible' ? 'visible-band' : source.product === 'geocolor' ? 'GeoColor' : 'scan'} ${RADAR_TIME.format(new Date(source.observedAt))}` : ''}`) : [];
 return <div className="domain-stage" data-state={state} data-topic={view.topic ?? 'kansas'}>
  <div ref={host} className="domain-stage-map" />
  <p className="domain-stage-caption"><span>Map preview · provider context</span><strong key={view.topic ?? 'kansas'}>{view.name}</strong><small>{view.detail}</small>{shown.length>0&&<small className="domain-stage-data">Preview layers: {shown.join(' · ')}</small>}<small className="domain-stage-credit">{BASEMAPS[view.basemap].note}</small></p>
 </div>;
}
