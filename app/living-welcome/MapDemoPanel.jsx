import { useEffect, useLayoutEffect, useRef, useState } from 'react';
import { mapDemos, demoDuration } from './map-demos.mjs';
import { bindPlayback } from './motion-playback.mjs';

// A rendered map tour is different from a decorative motion preview:
// nothing downloads or plays until the visitor explicitly chooses a demo.
export function MapDemoPanel({ category, paused = false, reducedMotion = false, onTry, onPlaybackChange }) {
  const demos = mapDemos(category);
  const [selectedId, setSelectedId] = useState(demos[0]?.id);
  const [requested, setRequested] = useState(false), [held, setHeld] = useState(false);
  const [status, setStatus] = useState('idle'), [failed, setFailed] = useState(false), [retry, setRetry] = useState(0);
  const [hidden, setHidden] = useState(() => typeof document !== 'undefined' && document.hidden);
  const video = useRef(null), controller = useRef(null);
  const selected = demos.find(demo => demo.id === selectedId) || demos[0];
  const shouldPause = paused || hidden || held;
  const latest = useRef({ shouldPause, onPlaybackChange });
  useLayoutEffect(() => { latest.current = { shouldPause, onPlaybackChange }; }, [shouldPause, onPlaybackChange]);
  useEffect(() => {
    const visibility = () => setHidden(document.hidden);
    document.addEventListener('visibilitychange', visibility);
    return () => document.removeEventListener('visibilitychange', visibility);
  }, []);
  useEffect(() => {
    if (!requested || failed || !selected?.src || !video.current) return;
    const playback = bindPlayback(video.current, {
      src: selected.src, paused: latest.current.shouldPause,
      onBlocked: () => { setFailed(true); setStatus('failed'); latest.current.onPlaybackChange?.(false); },
    });
    controller.current = playback;
    return () => { playback.dispose(); controller.current = null; latest.current.onPlaybackChange?.(false); };
  }, [selected?.id, selected?.src, requested, failed, retry]);
  useEffect(() => { controller.current?.setPaused(shouldPause); }, [shouldPause]);
  function play(demo = selected) {
    if (paused || !demo?.src) return;
    if (demo.id === selectedId && requested && !failed && video.current) {
      video.current.currentTime = 0; setHeld(false); controller.current?.setPaused(false);
      setStatus(status === 'playing' ? 'playing' : 'loading'); return;
    }
    setSelectedId(demo.id); setFailed(false); setHeld(false); setRequested(true);
    setStatus('loading');
  }
  function failure() { setFailed(true); setStatus('failed'); onPlaybackChange?.(false); }
  if (!demos.length) return null;
  return <section className="map-demo-panel" aria-labelledby={`map-demo-title-${category}`} data-state={status}>
    <div className="map-demo-heading"><span className="welcome-kicker">INSIDE THE ATLAS</span><h3 id={`map-demo-title-${category}`}>See the map in action.</h3><p>Short tours made with the real Explorer layers.</p></div>
    <div className="map-demo-choices" role="group" aria-label="Rendered map tours">{demos.map((demo, index) => <button type="button" key={demo.id} className="map-demo-choice" aria-label={`Play map tour: ${demo.title}`} aria-pressed={requested && selected?.id === demo.id} disabled={paused || !demo.src} onClick={() => play(demo)}>
      <span className="map-demo-thumbnail"><img src={demo.poster} alt="" loading="lazy" decoding="async"/><span className="map-demo-play" aria-hidden="true">▶</span><span className="map-demo-runtime">{demoDuration(demo.durationSeconds)}</span></span>
      <span className="map-demo-choice-copy"><small>TOUR {String(index + 1).padStart(2, '0')}</small><strong>{demo.title}</strong><span>{demo.src ? 'Watch the map tour →' : 'Tour unavailable'}</span></span>
    </button>)}</div>
    {requested && <div className="map-demo-screen" data-demo={selected.id}>
      <div className="map-demo-video-frame">{!failed ? <video ref={video} src={selected.src} poster={selected.poster} muted playsInline preload="auto" aria-label={`Rendered KFM map tour: ${selected.title}`} onLoadedData={() => { if (latest.current.shouldPause) setStatus('paused'); }} onPlay={() => {
        if (latest.current.shouldPause) { video.current?.pause(); return; }
        setStatus('playing'); onPlaybackChange?.(true);
      }} onPause={() => { setStatus(current => current === 'ended' || current === 'failed' ? current : 'paused'); onPlaybackChange?.(false); }} onEnded={() => { setHeld(true); setStatus('ended'); onPlaybackChange?.(false); }} onError={failure}/>
        : <div className="map-demo-failure" role="status"><strong>This tour couldn’t load.</strong><span>You can still open the tool below.</span><button type="button" disabled={paused} onClick={() => { setRetry(value => value + 1); play(); }}>Retry tour</button><button type="button" aria-label="Close map tour player" onClick={() => { setRequested(false); setStatus('idle'); onPlaybackChange?.(false); }}>Close tour</button></div>}
        {status === 'loading' && !failed && <span className="map-demo-loading" role="status">Loading map tour…</span>}
      </div>
      {!failed && <div className="map-demo-transport"><span>{status === 'ended' ? 'Tour complete' : 'Rendered map tour'}</span><button type="button" disabled={paused} aria-label={status === 'ended' ? 'Replay map tour' : held || status === 'paused' ? 'Play map tour' : 'Pause map tour'} onClick={() => { if (status === 'ended') play(); else if (held || status === 'paused') { setHeld(false); controller.current?.setPaused(false); } else setHeld(true); }}><span aria-hidden="true">{status === 'ended' ? '↻' : held || status === 'paused' ? '▶' : 'Ⅱ'}</span>{status === 'ended' ? 'Replay' : held || status === 'paused' ? 'Play' : 'Pause'}</button><a className="map-demo-full-size" href={selected.src} target="_blank" rel="noreferrer">Open full-size tour <span aria-hidden="true">↗</span></a><button type="button" aria-label="Close map tour player" onClick={() => { setRequested(false); setStatus('idle'); onPlaybackChange?.(false); }}>Close ×</button></div>}
    </div>}
    <div className="map-demo-context">{selected?.sourceTime&&<span className="map-demo-source-time">{selected.sourceTime}</span>}<p>{selected?.caption} {selected?.limitation} Rendered tours show dated source context, not live feeds.</p>{paused ? <small>Animations are paused. Resume them in the welcome controls to play a map tour.</small> : reducedMotion && !requested ? <small>Motion is off by preference. A tour plays only when you choose it.</small> : null}<button type="button" className="welcome-text-action" onClick={() => onTry?.(selected)}>Try this tool <span aria-hidden="true">↗</span></button></div>
  </section>;
}
