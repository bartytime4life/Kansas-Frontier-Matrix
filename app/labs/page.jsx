'use client';

import { Suspense, lazy, useCallback, useEffect, useLayoutEffect, useRef, useState } from 'react';
import Link from 'next/link';
import { STORIES, STORY_GROUPS, storyById } from '../living-welcome/stories/registry.mjs';
import { StoryBoundary, useStoryModule } from '../living-welcome/stories/story-parts.jsx';
import { useStoryBundle } from '../living-welcome/stories/useStoryBundle.js';
import { atlasCoverage, atlasFacts, atlasStatus, matchesAtlasStory, storyFromSearch, storyLocation } from './atlas-model.mjs';
import '../living-welcome/stories/stories.css';
import styles from './page.module.css';

const StoryLab = lazy(() => import('../living-welcome/stories/StoryLab.jsx').then(module => ({ default: module.StoryLab })));
const IMPLEMENTED = STORIES.filter(story => story.status === 'ready');
const FEATURED = ['climate-stripes', 'iron-horse', 'shaking-ground', 'river-memory'].map(storyById).filter(story => story?.status === 'ready');
const number = new Intl.NumberFormat('en-US');

function useNear(ref) {
  const [near, setNear] = useState(() => typeof window !== 'undefined' && typeof IntersectionObserver === 'undefined');
  useEffect(() => {
    if (!ref.current) return undefined;
    if (typeof IntersectionObserver === 'undefined') return undefined;
    const observer = new IntersectionObserver(entries => setNear(entries.at(-1).isIntersecting), { rootMargin: '260px 0px' });
    observer.observe(ref.current);
    return () => observer.disconnect();
  }, [ref]);
  return near;
}

function SourceStatus({ story, state }) {
  const status = atlasStatus(story, state);
  return <span className={styles.status} data-tone={status.tone}><i aria-hidden="true"/>{status.label}</span>;
}

function EmptyVisual({ state, story }) {
  return <div className={styles.emptyVisual}><span className={styles.emptyCross} aria-hidden="true">+</span><span>{state === 'offline' ? 'The source could not be reached.' : state === 'waiting' ? 'No released source snapshot is available here.' : 'Reading the source record…'}</span><small>{story.sources[0]}</small></div>;
}

function DataVisual({ story, bundle, state, held, enabled = true }) {
  const storyModule = useStoryModule(story, enabled && state === 'ready');
  const Visual = bundle && state === 'ready' && storyModule?.default;
  return Visual ? <StoryBoundary key={story.id} fallback={<div className={styles.emptyVisual}>This preview could not be drawn. Open the lab to inspect its source.</div>}><Visual bundle={bundle} mode="card" paused={held} reduced={held}/></StoryBoundary> : <EmptyVisual state={state} story={story}/>;
}

function FeaturedInstrument({ onOpen, onState }) {
  const [id, setId] = useState(FEATURED[0]?.id || 'climate-stripes');
  const story = storyById(id);
  const { state, bundle } = useStoryBundle(id);
  useEffect(() => { onState(id, state); }, [id, state, onState]);
  const facts = atlasFacts(bundle);
  return <section className={styles.instrument} aria-label="Featured research preview">
    <div className={styles.instrumentTop}><span>FIELD PLATE / {String(STORIES.findIndex(entry => entry.id === id) + 1).padStart(2, '0')}</span><SourceStatus story={story} state={state}/></div>
    <div className={styles.instrumentVisual} role="img" aria-label={`${story.title}. ${atlasCoverage(bundle) ? `Source coverage ${atlasCoverage(bundle)}.` : 'Source availability is being checked.'}`}><DataVisual story={story} state={state} bundle={bundle} held/></div>
    <div className={styles.instrumentCaption}><div><span className={styles.miniLabel}>{story.kicker}</span><h2>{story.title}</h2></div><button type="button" onClick={event => onOpen(id, event.currentTarget)} aria-label={`Explore ${story.title}`}><span aria-hidden="true">↗</span></button></div>
    <p className={styles.instrumentSource}>{bundle?.sources?.[0]?.name || story.sources[0]}{atlasCoverage(bundle) ? ` · ${atlasCoverage(bundle)}` : ''}</p>
    <div className={styles.instrumentFoot}>{facts.length ? facts.map(fact => <span key={fact.label}><strong>{number.format(fact.value)}</strong>{fact.label}</span>) : <span>Source coverage will appear when the record loads.</span>}<span className={styles.plateNote}>A source snapshot.<br/>A thousand questions.</span></div>
    <div className={styles.featureTabs} role="group" aria-label="Choose a featured preview">{FEATURED.map(entry => <button type="button" key={entry.id} aria-pressed={id === entry.id} onClick={() => setId(entry.id)}>{entry.id === 'climate-stripes' ? 'Climate' : entry.id === 'iron-horse' ? 'Railroads' : entry.id === 'shaking-ground' ? 'Earthquakes' : 'Rivers'}</button>)}</div>
  </section>;
}

function ResearchCard({ story, held, onOpen, onState, hidden }) {
  const ref = useRef(null), near = useNear(ref);
  const { state, bundle, known } = useStoryBundle(story.id, { enabled: near && !hidden });
  const effectiveState = state === 'idle' ? known?.state || state : state;
  useEffect(() => { if (effectiveState !== 'idle') onState(story.id, effectiveState); }, [story.id, effectiveState, onState]);
  const facts = atlasFacts(bundle);
  return <article ref={ref} hidden={hidden} className={styles.researchCard} data-story={story.id} style={{ '--atlas-accent': story.palette[1] }}>
    <button type="button" className={styles.cardOpen} onClick={event => onOpen(story.id, event.currentTarget)} aria-label={`Explore ${story.title}. ${atlasStatus(story, effectiveState).label}.`}>
      <div className={styles.cardPlate}><div className={styles.cardVisual} role="img" aria-label={`${story.title} source-data preview`}>{near && <DataVisual story={story} bundle={bundle} state={state} enabled={near} held={held}/>}</div><span className={styles.plateNumber}>{String(STORIES.findIndex(entry => entry.id === story.id) + 1).padStart(2, '0')} / {story.group}</span><span className={styles.cardArrow} aria-hidden="true">↗</span></div>
      <div className={styles.cardCopy}><SourceStatus story={story} state={effectiveState}/><h3>{story.title}</h3><p>{story.summary}</p><div className={styles.cardFacts}>{facts.length ? facts.map(fact => <span key={fact.label}><strong>{number.format(fact.value)}</strong> {fact.label}</span>) : <span>{story.kicker}</span>}</div></div>
    </button>
    <div className={styles.cardSource}><span>{bundle?.sources?.[0]?.name || story.sources[0]}</span><span>{atlasCoverage(bundle) || 'Snapshot coverage pending'}</span></div>
  </article>;
}

export default function LabsPage() {
  const [labId, setLabId] = useState(null), [paused, setPaused] = useState(false), [reduced, setReduced] = useState(true);
  const [query, setQuery] = useState(''), [group, setGroup] = useState('All'), [availability, setAvailability] = useState('all'), [states, setStates] = useState({});
  const trigger = useRef(null), catalogue = useRef(null), title = useRef(null), previousLabId = useRef(null);
  const onState = useCallback((id, state) => setStates(current => current[id] === state ? current : { ...current, [id]: state }), []);
  useEffect(() => {
    const media = window.matchMedia('(prefers-reduced-motion: reduce)');
    const update = () => setReduced(media.matches);
    const readURL = () => setLabId(storyFromSearch(window.location.search, STORIES));
    update(); readURL();
    media.addEventListener('change', update); window.addEventListener('popstate', readURL);
    return () => { media.removeEventListener('change', update); window.removeEventListener('popstate', readURL); };
  }, []);
  const open = useCallback((id, node) => {
    if (!storyById(id)) return;
    if (node) trigger.current = node;
    window.history.pushState({ ...window.history.state, kfmAtlasStory: id }, '', storyLocation(window.location.href, id));
    setLabId(id);
  }, []);
  const close = useCallback(() => {
    window.history.replaceState({ ...window.history.state, kfmAtlasStory: null }, '', storyLocation(window.location.href, null));
    setLabId(null);
  }, []);
  // Close, browser Back and forward history share one focus handoff after the
  // dialog has released its background isolation. Filtered-out cards cannot
  // receive focus, so the catalogue is the stable return point in that case.
  useLayoutEffect(() => {
    const wasOpen = previousLabId.current !== null;
    previousLabId.current = labId;
    if (!wasOpen || labId !== null) return;
    const original = trigger.current;
    const visible = original?.isConnected && original.getClientRects().length > 0 && !original.closest('[hidden], [inert]');
    (visible ? original : catalogue.current)?.focus({ preventScroll: true });
  }, [labId]);
  const story = labId ? storyById(labId) : null;
  const readyCount = Object.values(states).filter(state => state === 'ready').length;
  const filters = { query, group, availability, states };
  const shownReady = IMPLEMENTED.filter(entry => matchesAtlasStory(entry, filters));
  const planned = STORIES.filter(entry => entry.status !== 'ready' && matchesAtlasStory(entry, filters));
  const resetFilters = () => { setQuery(''); setGroup('All'); setAvailability('all'); };
  return <div className={styles.page}>
    <header className={styles.masthead}><Link prefetch={false} className={styles.brand} href="/" aria-label="Kansas Frontier Matrix map"><span className={styles.brandMark} aria-hidden="true">K<span>F</span>M</span><span>KANSAS FRONTIER MATRIX<small>The research atlas</small></span></Link><nav aria-label="Atlas navigation"><Link prefetch={false} href="/">Map explorer <span aria-hidden="true">↗</span></Link><Link prefetch={false} href="/observatory/sources">Source observatory</Link><button type="button" disabled={reduced} aria-pressed={paused || reduced} onClick={() => setPaused(value => !value)}>{reduced ? 'Motion reduced' : paused ? 'Play previews' : 'Pause previews'}</button></nav></header>
    <main>
      <section className={styles.hero} aria-labelledby="atlas-title"><div className={styles.heroCopy}><p className={styles.eyebrow}><span aria-hidden="true"/>THE KANSAS RECORD / AN OPEN FIELD OF QUESTIONS</p><h1 id="atlas-title" ref={title} tabIndex={-1}>One place.<br/>Countless ways<br/>to <em>see it.</em></h1><p className={styles.lede}>Read the land in layers. Follow a warming century, trace a railroad, find the pattern hiding in a record. Then go all the way back to the source.</p><div className={styles.heroActions}><button type="button" className={styles.primaryAction} onClick={() => catalogue.current?.scrollIntoView({ behavior: reduced ? 'instant' : 'smooth', block: 'start' })}>Find your next discovery <span aria-hidden="true">↓</span></button><Link prefetch={false} href="/">Explore the map <span aria-hidden="true">↗</span></Link></div><div className={styles.heroIndex}><span><strong>{String(IMPLEMENTED.length).padStart(2, '0')}</strong>research instruments</span><span><strong>{String(STORIES.length).padStart(2, '0')}</strong>stories in the atlas</span><span><strong>01</strong>place to connect them</span></div></div><FeaturedInstrument onOpen={open} onState={onState}/></section>
      <div className={styles.methodStrip} aria-label="Research workflow"><span><b>01</b> Follow a question</span><span><b>02</b> Explore the evidence</span><span><b>03</b> Inspect the source</span><span><b>04</b> Take the record with you</span></div>
      <section className={styles.catalogue} ref={catalogue} tabIndex={-1} aria-labelledby="research-title"><header className={styles.catalogueHeading}><div><p className={styles.eyebrow}>YOUR FIELDWORK STARTS HERE</p><h2 id="research-title">Open a new perspective.</h2></div><p>Every working plate is drawn from its source snapshot. Search, change the view, inspect individual records, and export what you find.</p></header>
        <div className={styles.finder}><label className={styles.search}><span aria-hidden="true">⌕</span><span className={styles.srOnly}>Search research labs</span><input type="search" value={query} onChange={event => setQuery(event.target.value)} placeholder="What draws you in? Try water, census, railroads…"/></label><label className={styles.availability}><span>SHOW</span><select value={availability} onChange={event => setAvailability(event.target.value)} aria-label="Data availability"><option value="all">All research</option><option value="ready">Snapshots found ({readyCount})</option><option value="planned">In development</option></select></label></div>
        <div className={styles.catalogueFilters}><div className={styles.groupFilters} role="group" aria-label="Filter research by field">{['All', ...STORY_GROUPS.filter(entry => entry !== 'Data to come')].map(entry => <button key={entry} type="button" aria-pressed={group === entry} onClick={() => setGroup(entry)}>{entry === 'All' ? 'All fields' : entry}</button>)}</div><span className={styles.resultCount} role="status">{shownReady.length + planned.length} {shownReady.length + planned.length === 1 ? 'perspective' : 'perspectives'}</span></div>
        {shownReady.length > 0 && <div className={styles.sectionRule}><h3>Research instruments</h3><span>{readyCount} source {readyCount === 1 ? 'snapshot' : 'snapshots'} found this visit</span></div>}
        <div className={styles.researchGrid}>{IMPLEMENTED.map(entry => <ResearchCard key={entry.id} story={entry} hidden={!shownReady.includes(entry)} held={paused || reduced || Boolean(story)} onOpen={open} onState={onState}/>)}</div>
        {!shownReady.length && !planned.length && <div className={styles.noResults} role="status"><span aria-hidden="true">∅</span><h3>No records in this view.</h3><p>{availability === 'ready' ? 'Source status is checked as previews enter view. Select All research to inspect an unchecked instrument.' : 'Try a source name, a broader topic, or a different field.'}</p><button type="button" onClick={resetFilters}>Show all research</button></div>}
        {planned.length > 0 && <section className={styles.planned} aria-labelledby="planned-title"><div className={styles.sectionRule}><h3 id="planned-title">On the horizon</h3><span>{planned.length} stories in development</span></div><p className={styles.plannedIntro}>The next questions are already taking shape. These entries describe the intended research; they do not yet have a working source-backed instrument.</p><div className={styles.plannedGrid}>{planned.map(entry => <button type="button" key={entry.id} onClick={event => open(entry.id, event.currentTarget)} className={styles.plannedRow}><span className={styles.plannedNumber}>{String(STORIES.indexOf(entry) + 1).padStart(2, '0')}</span><span><small>{entry.kicker}</small><strong>{entry.title}</strong><span>{entry.sources[0]}</span></span><span aria-hidden="true">↗</span></button>)}</div></section>}
      </section>
      <aside className={styles.researchNote}><span className={styles.noteSymbol} aria-hidden="true">∴</span><div><p className={styles.eyebrow}>BEAUTY IN THE PATTERN. TRUST IN THE RECORD.</p><h2>Curiosity is open. Evidence is specific.</h2><p>Instruments open when a source snapshot is released for this environment. Private local previews remain on the owner’s computer. Their dates, methods, gaps and source rights travel with every view. An observed pattern invites a question; it does not establish a cause.</p></div><Link prefetch={false} href="/observatory/sources">Meet the sources <span aria-hidden="true">↗</span></Link></aside>
    </main>
    <footer className={styles.footer}><span>KANSAS FRONTIER MATRIX <span aria-hidden="true">/</span> THE RESEARCH ATLAS</span><Link prefetch={false} href="/">Return to the Kansas map ↑</Link></footer>
    {story && <Suspense fallback={<div className={styles.loading} role="status">Opening the research instrument… <button type="button" onClick={close}>Cancel</button></div>}><StoryLab story={story} paused={paused} reduced={reduced} onMove={id => open(id)} onClose={close}/></Suspense>}
  </div>;
}
