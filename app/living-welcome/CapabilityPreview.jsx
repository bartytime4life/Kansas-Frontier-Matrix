import { useEffect, useLayoutEffect, useRef, useState } from 'react';
import { bindPlayback } from './motion-playback.mjs';

/** One requested, source-bound tour. No animation bytes on opening a category. */
export function CapabilityPreview({ demo, paused = false, className = '' }) {
 const video = useRef(null), controller = useRef(null), latest = useRef(true);
 const [hidden, setHidden] = useState(() => typeof document !== 'undefined' && document.hidden);
 const [requested, setRequested] = useState(null), [held, setHeld] = useState(false), [failed, setFailed] = useState(null);
 const selected = Boolean(demo && requested === demo.id), stopped = paused || hidden || held;
 useLayoutEffect(() => { latest.current = stopped; }, [stopped]);
 useEffect(() => {
  const sync = () => setHidden(document.hidden);
  document.addEventListener('visibilitychange', sync);
  return () => document.removeEventListener('visibilitychange', sync);
 }, []);
 useEffect(() => {
  if (!selected || !video.current || failed === demo.id) return;
  const playback = bindPlayback(video.current, { src: demo.src, paused: latest.current, onBlocked: () => setFailed(demo.id) });
  controller.current = playback;
  return () => { playback.dispose(); controller.current = null; };
 }, [demo?.id, demo?.src, selected, failed]);
 useEffect(() => { controller.current?.setPaused(stopped); }, [stopped]);
 if (!demo) return null;
 const moving = selected && !stopped && failed !== demo.id;
 const play = () => { setFailed(null); setHeld(false); setRequested(demo.id); if (video.current?.ended) video.current.currentTime = 0; };
 return <figure className={`capability-preview ${className}`} data-demo={demo.id} data-moving={moving}>
  <div className="capability-preview-screen">
   {selected && failed !== demo.id ? <video ref={video} poster={demo.poster} muted playsInline preload="none" aria-label={`Recorded Explorer tour: ${demo.title}`} onEnded={() => setHeld(true)} onError={() => setFailed(demo.id)}/> :
    /* eslint-disable-next-line @next/next/no-img-element -- Exact captured still; animation loads only on request. */
    <img src={demo.poster} alt={demo.title} decoding="async" loading="lazy"/>}
   <button type="button" className="capability-preview-play" disabled={paused} onClick={moving ? () => setHeld(true) : play}>{moving ? 'Pause tour' : selected ? 'Play tour again' : `Watch ${demo.durationSeconds}-second tour`}<span aria-hidden="true"> {moving ? 'Ⅱ' : '▶'}</span></button>
  </div>
  <figcaption><span className="capability-preview-label">{demo.context ? 'CONTEXT CAPTURE' : 'EXPLORER CAPTURE'} · RECORDED TOUR</span><strong>{demo.title}</strong><span>{demo.sourceTime}</span>{demo.context && <span>{demo.context}</span>}<small>{demo.limitation}</small>{failed === demo.id && <span role="status">Tour unavailable; showing the captured still. Try again or open the map.</span>}</figcaption>
 </figure>;
}
