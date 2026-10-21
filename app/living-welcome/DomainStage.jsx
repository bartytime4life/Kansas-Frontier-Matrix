import { useEffect, useRef, useState } from 'react';
import { SCENE_CATALOG, SCENE_LABEL } from './scenes/catalog.mjs';

/**
 * Full-window illustrative scene for the selected domain. The WebGL engine
 * loads after the welcome has painted; until then (or without WebGL) the stage
 * stays a quiet backdrop and the caption still names the scene.
 */
export function DomainStage({ topic, paused = false, reduced = false, onBeat }) {
 const canvas = useRef(null), engine = useRef(null), latest = useRef({ topic, paused, reduced }), beatListener = useRef(onBeat);
 const [beat, setBeat] = useState({ id: topic, index: 0 }), [state, setState] = useState('loading');
 useEffect(() => {
  let cancelled = false, idle = 0;
  const boot = () => import('./scenes/engine.mjs').then(({ createSceneEngine }) => {
   if (cancelled || !canvas.current) return;
   const instance = createSceneEngine(canvas.current, {
    onBeat: (id, index) => { setBeat({ id, index }); beatListener.current?.(id, index); },
    onReady: () => setState('ready'),
    onError: () => setState('unavailable'),
   });
   if (!instance) return;
   engine.current = instance;
   const { topic: id, paused: stopped, reduced: still } = latest.current;
   instance.setReduced(still); instance.setPaused(stopped); instance.show(id);
   if (import.meta.env?.DEV) window.__kfmScene = instance; // development review hook only
  }).catch(() => { if (!cancelled) setState('unavailable'); });
  if (typeof window.requestIdleCallback === 'function') idle = window.requestIdleCallback(boot, { timeout: 900 });
  else idle = setTimeout(boot, 120);
  return () => {
   cancelled = true;
   if (typeof window.cancelIdleCallback === 'function') window.cancelIdleCallback(idle); else clearTimeout(idle);
   engine.current?.dispose(); engine.current = null;
  };
 }, []);
 useEffect(() => { beatListener.current = onBeat; }, [onBeat]);
 // The latest props also seed the engine when it finishes loading.
 useEffect(() => { latest.current = { topic, paused, reduced }; engine.current?.show(topic); }, [topic, paused, reduced]);
 useEffect(() => { engine.current?.setPaused(paused); }, [paused]);
 useEffect(() => { engine.current?.setReduced(reduced); }, [reduced]);
 const entry = SCENE_CATALOG[topic], index = beat.id === topic ? beat.index : 0;
 return <div className="domain-stage" data-state={state} data-topic={topic}>
  <canvas ref={canvas} aria-hidden="true" />
  {entry && <p className="domain-stage-caption"><span>{SCENE_LABEL}</span><strong key={`${topic}-${index}`}>{entry.beats[index][1]}</strong></p>}
 </div>;
}
