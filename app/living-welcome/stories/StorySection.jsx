'use client';
import { Suspense, lazy, useCallback, useEffect, useLayoutEffect, useRef, useState } from 'react';
import { createPortal } from 'react-dom';
import { isolateModalBackground, modalFocusableElements } from '../../modal-background';
import { STORIES, STORY_GROUPS, storyById } from './registry.mjs';
import { StoryBoundary, WaitingSketch, useStoryModule } from './story-parts.jsx';
import { scrollParent } from './story-kit.mjs';
import { useStoryBundle } from './useStoryBundle.js';
import './stories.css';

const StoryLab = lazy(() => import('./StoryLab.jsx').then(loaded => ({ default: loaded.StoryLab })));

const statusText = (story, state, observedTo) => {
  const detail = story.sources.join(' · ');
  if (story.status === 'planned') return { label: 'In the works', detail };
  if (state === 'ready') return { label: observedTo ? `Record to ${observedTo}` : 'Record ready', detail };
  if (state === 'offline') return { label: 'Record unavailable', detail };
  return { label: state === 'waiting' ? 'Data arriving' : 'Looking for the record', detail };
};

function StoryCard({ story, held, onOpen, root }) {
  const box = useRef(null), [near, setNear] = useState(false);
  useEffect(() => {
    const node = box.current;
    if (!node) return undefined;
    // A card's canvas and data exist only near the viewport. Its text and button always do.
    const observer = new IntersectionObserver(entries => setNear(entries.at(-1).isIntersecting), { root: root?.current || scrollParent(node), rootMargin: '500px 0px' });
    observer.observe(node);
    return () => observer.disconnect();
  }, [root]);
  const live = near && story.status === 'ready';
  const { state, bundle, known } = useStoryBundle(story.id, { enabled: live });
  const storyModule = useStoryModule(story, live);
  // A card scrolled far away lets its bundle go but keeps the line it last showed.
  const status = statusText(story, state === 'idle' && known ? known.state : state, bundle?.observed?.to ?? known?.observedTo);
  const Visual = state === 'ready' && bundle && storyModule?.default;
  const sketch = <WaitingSketch story={story} held={held}/>;
  return <article className="story-card" data-story={story.id} data-status={story.status} data-state={state} style={{ '--story-0': story.palette[0], '--story-1': story.palette[1], '--story-2': story.palette[2] }}>
    <button type="button" className="story-card-open" aria-label={`Open the ${story.title} lab: ${story.summary} ${status.label}.`} onClick={event => onOpen(story.id, event.currentTarget)}>
      <span className="story-thumb" ref={box}>
        {near && (Visual ? <StoryBoundary fallback={sketch}><Visual bundle={bundle} mode="card" paused={held} reduced={held}/></StoryBoundary> : sketch)}
      </span>
      <span className="story-card-copy">
        <span className="story-kicker">{story.kicker}</span>
        <strong>{story.title}</strong>
        <small>{story.summary}</small>
        <span className="story-status"><b>{status.label}</b><i>{status.detail}</i></span>
      </span>
    </button>
  </article>;
}

function StoryGroups({ held, onOpen, root }) {
  return <>{STORY_GROUPS.map(group => <section className="story-group" key={group} aria-label={group}>
    <h3 className="story-group-title">{group}</h3>
    <div className="story-group-cards">{STORIES.filter(story => story.group === group).map(story => <StoryCard key={story.id} story={story} held={held} onOpen={onOpen} root={root}/>)}</div>
  </section>)}</>;
}

/** On phones the welcome is a map above a card rail, so the record opens as its own sheet instead of an inline list. */
function StorySheet({ held, onOpen, onClose, labOpen }) {
  const dialog = useRef(null);
  useLayoutEffect(() => {
    const restore = isolateModalBackground(dialog.current, document.body);
    dialog.current?.querySelector('h2')?.focus({ preventScroll: true });
    return restore;
  }, []);
  useEffect(() => {
    if (labOpen) return undefined;
    const keyboard = event => {
      if (event.key === 'Escape') { event.preventDefault(); event.stopImmediatePropagation(); onClose(); return; }
      if (event.key !== 'Tab') return;
      const nodes = dialog.current ? modalFocusableElements(dialog.current) : [];
      if (!nodes.length) return;
      if (event.shiftKey && (document.activeElement === nodes[0] || document.activeElement === dialog.current?.querySelector('h2'))) { event.preventDefault(); nodes.at(-1).focus(); }
      else if (!event.shiftKey && document.activeElement === nodes.at(-1)) { event.preventDefault(); nodes[0].focus(); }
    };
    document.addEventListener('keydown', keyboard, true);
    return () => document.removeEventListener('keydown', keyboard, true);
  }, [labOpen, onClose]);
  return createPortal(<div className="story-sheet" ref={dialog} role="dialog" aria-modal="true" aria-labelledby="story-sheet-title">
    <header className="story-sheet-head"><div><span className="story-kicker">KANSAS FRONTIER MATRIX</span><h2 id="story-sheet-title" tabIndex={-1}>The Kansas record</h2></div>
      <button type="button" className="story-icon-button" aria-label="Close The Kansas record" onClick={onClose}>×</button></header>
    <p className="story-section-lede">{STORIES.filter(entry => entry.status === 'ready').length} instruments and {STORIES.filter(entry => entry.status === 'planned').length} planned stories. Source availability is shown separately.</p>
    <StoryGroups held={held} onOpen={onOpen} root={dialog}/>
  </div>, document.querySelector('.site-root') || document.body);
}

export default function StorySection({ paused = false, reduced = false, modal = false, compact = false, onOpenChange }) {
  const [labId, setLabId] = useState(null), [sheet, setSheet] = useState(false);
  const trigger = useRef(null), launcher = useRef(null);
  const held = Boolean(paused || reduced || modal || labId), sheetOpen = sheet && compact;
  useEffect(() => { onOpenChange?.(Boolean(labId || sheetOpen)); }, [labId, sheetOpen, onOpenChange]);
  useEffect(() => () => onOpenChange?.(false), [onOpenChange]);
  const open = useCallback((id, node) => { trigger.current = node; setLabId(id); }, []);
  const close = useCallback(last => {
    setLabId(null);
    // Focus returns to the card of the story last shown, even after moving through others.
    requestAnimationFrame(() => {
      const card = document.querySelector(`.story-card[data-story="${last}"] .story-card-open`);
      (card?.isConnected ? card : trigger.current)?.focus();
    });
  }, []);
  const closeSheet = useCallback(() => { setSheet(false); requestAnimationFrame(() => launcher.current?.focus({ preventScroll: true })); }, []);
  const story = labId ? storyById(labId) : null;
  const liveCount = STORIES.filter(entry => entry.status === 'ready').length;
  return <>
    {compact
      ? <button type="button" ref={launcher} className="story-launcher" aria-label={`Open The Kansas record: ${STORIES.length} data stories`} onClick={() => setSheet(true)}><i aria-hidden="true"/>The Kansas record</button>
      : <section className="story-section" aria-labelledby="story-section-title">
        <header className="story-section-head"><h2 id="story-section-title">The Kansas record</h2>
          <p className="story-section-lede">{liveCount} research instruments; {STORIES.length - liveCount} more stories are planned. Each card shows whether a source snapshot is available.</p><a className="story-atlas-link" href="/labs">Open the research atlas ↗</a></header>
        <StoryGroups held={held} onOpen={open}/>
      </section>}
    {sheetOpen && <StorySheet held={held} onOpen={open} onClose={closeSheet} labOpen={Boolean(labId)}/>}
    {story && <Suspense fallback={null}><StoryLab story={story} paused={paused} reduced={reduced} onMove={setLabId} onClose={close}/></Suspense>}
  </>;
}
