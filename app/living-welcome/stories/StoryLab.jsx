'use client';
import { useEffect, useLayoutEffect, useRef, useState } from 'react';
import { createPortal } from 'react-dom';
import { isolateModalBackground, modalFocusableElements } from '../../modal-background';
import { STORIES } from './registry.mjs';
import { KANSAS_OUTLINE_CREDIT, downloadCSV, fmt } from './story-kit.mjs';
import { StoryBoundary, WaitingSketch, useStoryModule } from './story-parts.jsx';
import { useStoryBundle } from './useStoryBundle.js';

const SPEEDS = [{ id: .5, label: '½×' }, { id: 1, label: '1×' }, { id: 2, label: '2×' }];

function WaitingPanel({ story, state }) {
  const text = story.status === 'planned' ? 'This story is in the works.' : state === 'offline' ? 'The record cannot be reached right now.' : state === 'loading' ? 'Looking for the record…' : 'No released source snapshot is available here.';
  return <div className="story-waiting">
    <div className="story-waiting-sketch"><WaitingSketch story={story} held/></div>
    <div className="story-panel"><p className="story-kicker">{story.kicker}</p><p role="status"><strong>{text}</strong></p><p>{story.summary}</p><p><strong>In the lab:</strong> {story.try}</p></div>
  </div>;
}

function downloadJSON(filename, value) {
  const url = URL.createObjectURL(new Blob([JSON.stringify(value, null, 2)], { type: 'application/json' }));
  const link = document.createElement('a');
  link.href = url; link.download = filename; document.body.append(link); link.click(); link.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

function Sources({ story, bundle, controls, time }) {
  const sources = bundle?.sources || story.sources.map(name => ({ name }));
  const observed = bundle?.observed;
  const observedText = value => bundle?.data?.timeUnit === 'Ma' && Number.isFinite(Number(value))
    ? `${Math.abs(Number(value))} Ma` : String(value).replace(/T.*$/, '');
  return <footer className="story-lab-foot" aria-label="Sources and limits">
    <div><h3>Sources</h3><ul>{sources.map(source => <li key={source.name}>{source.url ? <a href={source.url} target="_blank" rel="noopener noreferrer">{source.name}</a> : source.name}{source.license ? <span> · {source.license}</span> : null}</li>)}</ul>
      {observed?.from != null && <p className="story-num">{bundle.data.timeUnit === 'Ma' ? 'Age midpoint coverage' : 'Observed'} {observedText(observed.from)} to {observedText(observed.to)}{bundle.built_at ? ` · built ${bundle.built_at.slice(0, 10)}` : ''}</p>}
      {bundle && <details className="story-provenance"><summary>Snapshot & reproducibility</summary>
        <p>{bundle.data.sourceSnapshot?.retrievedAt ? `Retrieved ${bundle.data.sourceSnapshot.retrievedAt}. ` : ''}This source snapshot carries its own dates, rights and limits. Display and export do not establish admission or release approval.</p>
        {sources.map(source => <p key={source.name}>{source.citation}</p>)}
        <div className="story-export-actions">
          <button type="button" className="story-tool" onClick={() => downloadJSON(`${story.id}-snapshot.json`, bundle)}>Download source snapshot</button>
          <button type="button" className="story-tool" onClick={() => downloadJSON(`${story.id}-view-receipt.json`, {
            format: 'kfm-local-lab-view-v1', story: story.id, exportedAt: new Date().toISOString(),
            snapshotBuiltAt: bundle.built_at, sourceSnapshot: bundle.data.sourceSnapshot || null,
            sourceSnapshots: bundle.data.sourceSnapshots || (bundle.data.sourceSnapshot ? [bundle.data.sourceSnapshot] : []),
            observed: bundle.observed, sources: bundle.sources, controls, time,
            interpretation: 'View settings and source metadata; not a release or admission receipt.',
          })}>Save view receipt</button>
        </div>
      </details>}</div>
    <div><h3>Limits</h3><ul>{(bundle?.data?.limits || [story.limit]).map(limit => <li key={limit}>{limit}</li>)}</ul><p className="story-note">{KANSAS_OUTLINE_CREDIT}</p></div>
  </footer>;
}

function LabContent({ story, paused, reduced }) {
  const { state, bundle } = useStoryBundle(story.status === 'ready' ? story.id : null);
  const storyModule = useStoryModule(story, story.status === 'ready');
  const Visual = state === 'ready' && bundle && storyModule?.default;
  const range = Visual && storyModule.range ? storyModule.range(bundle) : null;
  const canCSV = Boolean(Visual && storyModule.toCSV);
  const [time, setTime] = useState(null), [controls, setControls] = useState({}), [playRequested, setPlaying] = useState(false), [speed, setSpeed] = useState(1);
  const motionHeld = Boolean(paused || reduced), playing = playRequested && !motionHeld && Boolean(range);
  const shownTime = time ?? range?.max ?? null;
  const rangeMin = range?.min, rangeMax = range?.max, rangeRate = range?.rate, rangeStep = range?.step || 1;

  // Playback advances the shared time only while the tab is visible and motion is allowed.
  const startFrom = useRef(null);
  useEffect(() => { startFrom.current = time; }, [time]);
  useEffect(() => {
    if (!playing) return undefined;
    let frame = 0, last = null, value = startFrom.current === null || startFrom.current >= rangeMax ? rangeMin : startFrom.current;
    const tick = now => {
      frame = 0;
      if (document.hidden) return;
      value += (now - (last ?? now)) / 1000 * (rangeRate || 4) * speed;
      last = now;
      if (value >= rangeMax) { setTime(rangeMax); setPlaying(false); return; }
      setTime(Math.max(rangeMin, Math.min(rangeMax, Math.round(value / rangeStep) * rangeStep)));
      frame = requestAnimationFrame(tick);
    };
    const visibility = () => {
      if (document.hidden) { if (frame) cancelAnimationFrame(frame); frame = 0; }
      else if (!frame) { last = null; frame = requestAnimationFrame(tick); }
    };
    frame = requestAnimationFrame(tick);
    document.addEventListener('visibilitychange', visibility);
    return () => { if (frame) cancelAnimationFrame(frame); document.removeEventListener('visibilitychange', visibility); };
  }, [playing, speed, rangeMin, rangeMax, rangeRate, rangeStep]);

  const reset = () => { setPlaying(false); setTime(null); setControls({}); };
  const download = () => { const result = storyModule.toCSV(bundle, { time: shownTime, controls }); if (result) downloadCSV(result.filename, result.rows); };
  const scrubberLabel = range ? `${range.label}: ${range.format ? range.format(shownTime) : fmt(shownTime)}` : '';
  return <>
    <div className="story-lab-body">
      <StoryBoundary fallback={<WaitingPanel story={story} state="offline"/>}>
        {Visual
          ? <Visual bundle={bundle} mode="lab" paused={paused} reduced={reduced} time={shownTime} onTime={value => { setPlaying(false); setTime(value); }} controls={controls} onControls={setControls}/>
          : <WaitingPanel story={story} state={story.status === 'planned' ? 'planned' : state}/>}
      </StoryBoundary>
      <Sources story={story} bundle={state === 'ready' ? bundle : null} controls={controls} time={shownTime}/>
    </div>
    {Visual && <div className="story-lab-bar" role="group" aria-label="Lab controls">
      {range && <>
        <button type="button" className="story-tool" aria-pressed={playing} disabled={motionHeld} title={motionHeld ? 'Motion is held. Use the timeline.' : undefined} onClick={() => setPlaying(value => !value)}>{playing ? 'Pause' : 'Play'}</button>
        <label className="story-scrubber"><span className="story-num">{scrubberLabel}</span>
          <input type="range" min={range.min} max={range.max} step={range.step || 1} value={shownTime} aria-label={range.label} aria-valuetext={scrubberLabel} onChange={event => { setPlaying(false); setTime(Number(event.target.value)); }}/></label>
        <div className="story-speed" role="group" aria-label="Playback speed">{SPEEDS.map(option => <button type="button" key={option.id} aria-pressed={speed === option.id} aria-label={`Speed ${option.id} times`} disabled={motionHeld} onClick={() => setSpeed(option.id)}>{option.label}</button>)}</div>
      </>}
      <button type="button" className="story-tool" onClick={reset}>Reset</button>
      {canCSV && <button type="button" className="story-tool" onClick={download}><span className="story-tool-long">Download </span>CSV</button>}
    </div>}
  </>;
}

export function StoryLab({ story, paused, reduced, onMove, onClose }) {
  const dialog = useRef(null), heading = useRef(null);
  const index = STORIES.findIndex(entry => entry.id === story.id);
  const previous = STORIES[(index + STORIES.length - 1) % STORIES.length], next = STORIES[(index + 1) % STORIES.length];
  useLayoutEffect(() => {
    const restore = isolateModalBackground(dialog.current, document.body);
    return restore;
  }, []);
  useLayoutEffect(() => { heading.current?.focus({ preventScroll: true }); }, [story.id]);
  useEffect(() => {
    const keyboard = event => {
      if (event.key === 'Escape') { event.preventDefault(); event.stopImmediatePropagation(); onClose(story.id); return; }
      if (event.key !== 'Tab') return;
      const nodes = dialog.current ? modalFocusableElements(dialog.current).filter(node => node !== heading.current) : [];
      if (!nodes.length) { event.preventDefault(); return; }
      const active = document.activeElement;
      if (event.shiftKey && (active === nodes[0] || active === heading.current)) { event.preventDefault(); nodes.at(-1).focus(); }
      else if (!event.shiftKey && active === nodes.at(-1)) { event.preventDefault(); nodes[0].focus(); }
    };
    document.addEventListener('keydown', keyboard, true);
    return () => document.removeEventListener('keydown', keyboard, true);
  }, [onClose, story.id]);
  return createPortal(<div className="story-lab" ref={dialog} role="dialog" aria-modal="true" aria-labelledby="story-lab-title" data-story={story.id}>
    <header className="story-lab-head">
      <div className="story-lab-title"><span className="story-kicker">{story.kicker}</span><h2 id="story-lab-title" ref={heading} tabIndex={-1}>{story.title}</h2>
        <p className="story-lab-try">{story.try}</p></div>
      <nav className="story-lab-nav" aria-label="Other stories">
        <button type="button" className="story-icon-button" aria-label={`Previous story: ${previous.title}`} onClick={() => onMove(previous.id)}>←</button>
        <span className="story-num" aria-live="polite">{index + 1} / {STORIES.length}</span>
        <button type="button" className="story-icon-button" aria-label={`Next story: ${next.title}`} onClick={() => onMove(next.id)}>→</button>
        <button type="button" className="story-icon-button" aria-label="Close this lab" onClick={() => onClose(story.id)}>×</button>
      </nav>
    </header>
    <LabContent key={story.id} story={story} paused={paused} reduced={reduced}/>
  </div>, document.querySelector('.site-root') || document.body);
}
