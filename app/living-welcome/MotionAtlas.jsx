import { useEffect, useRef, useState } from 'react';
import { CATEGORY_IDS } from './catalog.mjs';
import { motionClip } from './motion-catalog.mjs';
import { sceneAt, dominantScene } from './sceneDirector.mjs';
import { fitScene } from './motion-playback.mjs';
import { MotionClip } from './MotionClip.jsx';

export function MotionAtlas({ paused, active, visible, manual, onReady, onScenes }) {
  const rootRef = useRef(null), latest = useRef(null), clock = useRef(0), lastFocus = useRef(null), historyStart = useRef(0);
  const [seconds, setSeconds] = useState(0), [bounds, setBounds] = useState(null), [hidden, setHidden] = useState(() => typeof document !== 'undefined' && document.hidden), [historyOrigin,setHistoryOrigin]=useState(0);
  latest.current = { paused, active, manual, onScenes };
  useEffect(() => {
    onReady?.(true);
    const visibility = () => setHidden(document.hidden);
    document.addEventListener('visibilitychange', visibility);
    return () => { document.removeEventListener('visibilitychange', visibility); onReady?.(false); };
  }, []);
  useEffect(() => {
    if (paused || hidden || (bounds && bounds.view.h <= 0)) return;
    let last=performance.now();
    // Native video presents frames. The story director only needs a low-rate
    // clock for scene changes; it does no per-frame rendering or pixel work.
    const timer=setInterval(()=>{
      const now=performance.now();clock.current+=Math.min(.5,(now-last)/1000);last=now;setSeconds(clock.current);
    },120);
    return()=>clearInterval(timer);
  }, [paused, hidden, bounds?.view.h > 0]);
  useEffect(() => {
    if (active === 'history' && lastFocus.current !== 'history') {historyStart.current=clock.current;setHistoryOrigin(clock.current);}
    lastFocus.current = active;
    setSeconds(clock.current);
  }, [active, manual]);
  useEffect(() => {
    const stage = rootRef.current.parentElement;
    let raf = 0;
    const measure = () => {
      raf = 0;
      const outer = stage.getBoundingClientRect();
      const port = stage.closest('.living-welcome')?.getBoundingClientRect();
      const clipTop = Math.max(0, port?.top ?? 0), clipBottom = Math.min(innerHeight, port?.bottom ?? innerHeight);
      const top = Math.max(0, clipTop - outer.top), height = Math.max(0, Math.min(outer.bottom, clipBottom) - Math.max(outer.top, clipTop));
      const local = {};
      for (const id of CATEGORY_IDS) {
        const r = stage.querySelector(`.${id}-scene`)?.getBoundingClientRect();
        if (r) local[id] = { x: r.left - outer.left, y: r.top - outer.top, w: r.width, h: r.height };
      }
      setBounds({ local, view: { x: 0, y: top, w: outer.width, h: height }, full: { x: outer.width * .015, y: top + height * .03, w: outer.width * .97, h: height * .94 } });
    };
    const update = () => { if (!raf) raf = requestAnimationFrame(measure); };
    const observer = new ResizeObserver(update); observer.observe(stage);
    stage.querySelectorAll('.scene-anchor').forEach(node => observer.observe(node));
    window.addEventListener('resize', update); window.addEventListener('scroll', update, { passive: true, capture: true });
    measure();
    return () => { observer.disconnect(); cancelAnimationFrame(raf); window.removeEventListener('resize', update); window.removeEventListener('scroll', update, true); };
  }, []);
  const indices = Object.fromEntries(CATEGORY_IDS.map(id => [id, dominantScene(sceneAt(id === 'history' ? seconds - historyOrigin : seconds, id, id === active ? manual : null))]));
  const key = Object.values(indices).join(',');
  useEffect(() => { latest.current.onScenes?.(indices); }, [key]);
  const eligible = CATEGORY_IDS.filter(id => {
    const r = bounds?.local[id], view = bounds?.view;
    return visible?.[id] !== false && r && r.y + r.h > view.y - 30 && r.y < view.y + view.h + 30;
  });
  const ambient = Math.floor(seconds / 7) % Math.max(1, eligible.length);
  return <div ref={rootRef} className="motion-atlas" aria-hidden="true" data-engine="native-video" data-revision="action-scenes-1" data-time={seconds.toFixed(3)} data-paused={String(paused || hidden)} data-focus={active || 'idle'}>
    {bounds && CATEGORY_IDS.map(id => {
      const local = bounds.local[id]; if (!local || visible?.[id] === false) return null;
      const selected = id === active, clip = motionClip(id, indices[id]);
      const position = fitScene(selected ? bounds.full : local, clip.width / clip.height);
      const onscreen = eligible.includes(id), playing = selected || (!active && onscreen && (id === eligible[ambient] || id === eligible[(ambient + 1) % eligible.length]));
      return <div key={id} className={`motion-portal ${selected ? 'is-immersive' : ''} ${active && !selected ? 'is-muted' : ''}`} data-category={id} style={{ left: position.x, top: position.y, width: position.w, height: position.h }}>
        <MotionClip clip={clip} paused={paused || hidden} playing={playing} small={!selected} />
      </div>;
    })}
  </div>;
}
