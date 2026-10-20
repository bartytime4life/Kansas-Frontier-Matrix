import { useEffect, useLayoutEffect, useRef, useState } from 'react';
import { bindPlayback } from './motion-playback.mjs';

function VideoLayer({ clip, paused, small, onReady, onFailure }) {
  const ref = useRef(null), controller = useRef(null), latest = useRef({paused,onFailure});
  const src=small ? clip.preview : clip.src;
  useLayoutEffect(()=>{latest.current={paused,onFailure};},[paused,onFailure]);
  const [ready, setReady] = useState(false);
  useEffect(() => {
    const node = ref.current;
    const playback = bindPlayback(node, { src, paused:latest.current.paused, onBlocked:()=>latest.current.onFailure?.() });
    controller.current = playback;
    return () => { playback.dispose(); controller.current = null; };
  }, [src]);
  useEffect(() => { controller.current?.setPaused(paused); }, [paused]);
  return <video ref={ref} className={`motion-video ${ready ? 'is-decoded' : ''}`} src={small ? clip.preview : clip.src} poster={clip.poster} muted playsInline loop preload="auto" aria-hidden="true" onLoadedData={() => { setReady(true); onReady?.(); }} onError={onFailure} />;
}

export function MotionClip({ clip, paused = false, playing = true, small = false, className = '', showStatus = false }) {
  const [displayed, setDisplayed] = useState(clip), [previous, setPrevious] = useState(null);
  const [ready, setReady] = useState(false), [failed, setFailed] = useState(false), [retry, setRetry] = useState(0);
  const current = useRef(clip.id);
  useLayoutEffect(()=>{current.current=clip.id;},[clip.id]);
  // Reset selection state before committing a new source; retain its outgoing poster.
  if(clip.id !== displayed.id){
    setPrevious(displayed); setDisplayed(clip); setReady(false); setFailed(false); setRetry(0);
  }
  useEffect(() => {
    if (!previous) return;
    const timer = setTimeout(() => setPrevious(null), 650);
    return () => clearTimeout(timer);
  }, [previous]);
  return <div className={`motion-clip ${className}`} data-clip={clip.id} data-displayed={displayed.id} data-ready={String(ready)} data-failed={String(failed)} data-playing={String(playing && !paused)}>
    {previous && <img key={`out-${previous.id}`} className="motion-outgoing" src={previous.poster} alt="" aria-hidden="true" />}
    <div className="motion-incoming" key={displayed.id}>
      <img className="motion-poster" src={displayed.poster} alt="" aria-hidden="true" />
      {playing && !failed && <VideoLayer key={`${displayed.id}-${small}-${retry}`} clip={displayed} paused={paused} small={small} onReady={() => { if (current.current === displayed.id) setReady(true); }} onFailure={() => { if (current.current === displayed.id) setFailed(true); }} />}
    </div>
    {showStatus && playing && !paused && !ready && !failed && <span className="motion-loading">Loading scene…</span>}
    {showStatus && failed && <button className="motion-retry" onClick={() => { setFailed(false); setReady(false); setRetry(x => x + 1); }}>Play this scene again</button>}
  </div>;
}
