'use client';

import { Suspense, lazy, useCallback, useEffect, useLayoutEffect, useRef, useState } from 'react';
import Link from 'next/link';
import { STORIES, STORY_GROUPS, storyById } from '../living-welcome/stories/registry.mjs';
import { StoryBoundary, useStoryModule } from '../living-welcome/stories/story-parts.jsx';
import { useStoryBundle } from '../living-welcome/stories/useStoryBundle.js';
import { atlasCoverage, atlasFacts, atlasStatus, matchesAtlasStory, storyFromSearch, storyLocation } from './atlas-model.mjs';
import { PUBLIC_LAB_SNAPSHOTS } from './public-snapshots.mjs';
import { cividis, kansasProjection } from '../living-welcome/stories/story-kit.mjs';
import { climateAnnualAnalysis } from '../living-welcome/stories/science-model.mjs';
import '../living-welcome/stories/stories.css';
import styles from './page.module.css';

const StoryLab = lazy(() => import('../living-welcome/stories/StoryLab.jsx').then(module => ({ default: module.StoryLab })));
const IMPLEMENTED = STORIES.filter(story => story.status === 'ready');
const GUIDED = STORIES.filter(story => story.status === 'guided');
const AVAILABLE = Object.keys(PUBLIC_LAB_SNAPSHOTS).length + GUIDED.length;
const QUESTIONS = [
  ['climate-stripes', 'How has Kansas warmed?', 'Since 1895 · 10 areas · temperature, rain & drought'],
  ['census-mosaic', 'Which counties are changing?', '105 counties · population, births & migration'],
  ['river-memory', 'When did the rivers surge?', '3 gauges · daily flow · compare the record'],
  ['river-flow', 'How often did the rivers run high?', 'River Flow Lab · gauge comparison and daily records'],
  ['tornado-tracks', 'Where have tornadoes traveled?', 'Since 1950 · tracks, ratings & reported impacts'],
  ['shaking-ground', 'Where has the ground shaken?', 'Since 2010 · magnitude, depth & source records'],
  ['built-kansas', 'What carries Kansas?', 'Bridge inventory · age, traffic, dimensions & condition'],
  ['energy-shift', 'How has our energy changed?', 'Annual energy series · sources, sectors & the long view'],
  ['air-and-health', 'What is in the air?', 'County air quality · monitored days & annual AQI'],
].filter(([id]) => Object.hasOwn(PUBLIC_LAB_SNAPSHOTS, id) || storyById(id)?.status === 'guided');
const number = new Intl.NumberFormat('en-US');
const PUBLIC_RECORDS = Object.values(PUBLIC_LAB_SNAPSHOTS).reduce((sum, snapshot) => sum + (snapshot.records || 0), 0);

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

function ConnectedWorkspaces() {
  const population = useStoryBundle('census-mosaic'), climate = useStoryBundle('climate-stripes');
  const [measure, setMeasure] = useState('population'), [county, setCounty] = useState('20173'), [element, setElement] = useState('tmpc');
  const rows = (population.bundle?.data.records || []).filter(row=>row.year===2025), selected = rows.find(row=>row.fips===county), values=rows.map(row=>row[measure]).filter(value=>typeof value==='number');
  const min=Math.min(...values),max=Math.max(...values), projection=kansasProjection(760,340,{padding:20});
  const path = geometry => (geometry?.type==='Polygon'?[geometry.coordinates]:geometry?.type==='MultiPolygon'?geometry.coordinates:[]).map(polygon=>polygon.map(ring=>ring.map(([lon,lat],index)=>`${index?'L':'M'}${projection.x(lon)},${projection.y(lat)}`).join(' ')+'Z').join(' ')).join(' ');
  const annual=climate.bundle?climateAnnualAnalysis(climate.bundle,{element,from:1970,to:2025}):null;
  const annualMin=annual?.rows.length?Math.min(...annual.rows.map(row=>row.value)):0, annualMax=annual?.rows.length?Math.max(...annual.rows.map(row=>row.value)):1;
  const unit=climate.bundle?.data.elements[element]?.unit||'', points=annual?.rows.map((row,index)=>`${index?'L':'M'}${35+(row.year-1970)/55*530},${230-(row.value-annualMin)/(annualMax-annualMin||1)*195}`).join(' ');
  return <div className={styles.connectedWorkspaces}>
    <section className={styles.countyLaunch} aria-labelledby="county-workspace-title"><div className={styles.workspaceTop}><span>WORKSPACE 01 / CONNECT BY PLACE</span><span>105 COUNTIES</span></div><div className={styles.workspaceTitle}><h2 id="county-workspace-title">County Observatory</h2><label><span className={styles.srOnly}>County preview measure</span><select aria-label="County preview measure" value={measure} onChange={event=>setMeasure(event.target.value)}><option value="population">Population · 2025</option><option value="netMigration">Net migration · 2025</option><option value="naturalChange">Natural change · 2025</option></select></label></div>
      {population.state==='ready'?<><svg viewBox="0 0 760 340" role="group" aria-label="Kansas county population preview. Select a county for its reported value.">{rows.map(row=><path key={row.fips} d={path(row.geometry)} fill={typeof row[measure]==='number'?cividis(.1+.9*(row[measure]-min)/(max-min||1)):'#39515e'} fillRule="evenodd" stroke={row.fips===county?'#ffefbc':'#102b37'} strokeWidth={row.fips===county?3:.8} role="button" tabIndex={0} aria-label={`${row.name}: ${typeof row[measure]==='number'?number.format(row[measure]):'unavailable'}`} onClick={()=>setCounty(row.fips)} onKeyDown={event=>{if(event.key==='Enter'||event.key===' '){event.preventDefault();setCounty(row.fips);}}}><title>{row.name} · {typeof row[measure]==='number'?number.format(row[measure]):'Unavailable'}</title></path>)}</svg><div className={styles.workspaceReadout}><label><span className={styles.srOnly}>County preview selection</span><select aria-label="County preview selection" value={county} onChange={event=>setCounty(event.target.value)}>{rows.map(row=><option key={row.fips} value={row.fips}>{row.name}</option>)}</select></label><strong>{typeof selected?.[measure]==='number'?number.format(selected[measure]):'Unavailable'}<small>{measure==='population'?'estimated residents':'people · annual component'}</small></strong></div></>:<div className={styles.connectedLoading} role="status">{population.state==='offline'?'County source unavailable. Open the workspace to retry.':'Reading the Census county snapshot…'}</div>}
      <div className={styles.workspaceLaunchFoot}><p>Link population, income, poverty, education, bridge inventory and monitored air. Compare two counties or join your own private CSV.</p><Link prefetch={false} href={`/labs/observatory?county=${county}`}>Open County Observatory <span aria-hidden="true">↗</span></Link><div><Link prefetch={false} href={`/labs/observatory?preset=income-growth&county=${county}`}>Income × growth</Link><Link prefetch={false} href={`/labs/observatory?preset=education-poverty&county=${county}`}>Education × poverty</Link></div></div>
    </section>
    <section className={styles.signalLaunch} aria-labelledby="signal-workspace-title"><div className={styles.workspaceTop}><span>WORKSPACE 02 / CONNECT THROUGH TIME</span><span>ANNUAL SIGNALS</span></div><div className={styles.workspaceTitle}><h2 id="signal-workspace-title">Signal Studio</h2><label><span className={styles.srOnly}>Annual climate preview measure</span><select aria-label="Annual climate preview measure" value={element} onChange={event=>setElement(event.target.value)}><option value="tmpc">Temperature</option><option value="pcpn">Precipitation</option></select></label></div>
      {climate.state==='ready'?<><div className={styles.signalPreviewLabel}><span>KANSAS / NOAA COMPLETE-YEAR RECORD</span><strong>1970–2025</strong></div><svg viewBox="0 0 600 265" role="img" aria-label={`Annual Kansas ${element==='tmpc'?'temperature':'precipitation'}, 1970–2025. ${annual.count} complete years.`}>{[0,.5,1].map(tick=><line key={tick} x1="35" x2="565" y1={230-tick*195} y2={230-tick*195} stroke="#b6cdd333"/>)}<path d={points} fill="none" stroke={element==='tmpc'?'#e6b579':'#83d7da'} strokeWidth="3"/><text x="35" y="253" fill="#bed1d8" fontSize="14">1970</text><text x="565" y="253" textAnchor="end" fill="#bed1d8" fontSize="14">2025</text></svg><div className={styles.signalPreviewStats}><span><strong>{annual.slopePerDecade===null?'—':annual.slopePerDecade.toFixed(2)}</strong>{unit} / decade · descriptive trend</span><span><strong>{annual.count}</strong>complete years · no filled months</span></div></>:<div className={styles.connectedLoading} role="status">{climate.state==='offline'?'Climate source unavailable. Open the workspace to retry.':'Reading complete annual climate observations…'}</div>}
      <div className={styles.workspaceLaunchFoot}><p>Pair climate, energy, river flow and event records by year. Test lags, remove trends, compare changes and keep the missing years visible.</p><Link prefetch={false} href="/labs/signals">Open Signal Studio <span aria-hidden="true">↗</span></Link><div><Link prefetch={false} href="/labs/signals?preset=rain-and-tornadoes">Rain × tornado counts</Link><span>Save · reopen · export</span></div></div>
    </section>
  </div>;
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
  const [query, setQuery] = useState(''), [group, setGroup] = useState('All'), [availability, setAvailability] = useState('available'), [states, setStates] = useState({});
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
  const guided = GUIDED.filter(entry => matchesAtlasStory(entry, filters));
  const planned = STORIES.filter(entry => entry.status === 'planned' && matchesAtlasStory(entry, filters));
  const resultCount = shownReady.length + guided.length + planned.length;
  const resetFilters = () => { setQuery(''); setGroup('All'); setAvailability('all'); };
  return <div className={styles.page}>
    <header className={styles.masthead}><Link prefetch={false} className={styles.brand} href="/" aria-label="Kansas Frontier Matrix map"><span className={styles.brandMark} aria-hidden="true">K<span>F</span>M</span><span>KANSAS FRONTIER MATRIX<small>The research atlas</small></span></Link><nav aria-label="Atlas navigation"><Link prefetch={false} href="/">Map explorer <span aria-hidden="true">↗</span></Link><Link prefetch={false} href="/labs/notebook">Research notebook</Link><Link prefetch={false} href="/observatory/sources">Source observatory</Link><button type="button" disabled={reduced} aria-pressed={paused || reduced} onClick={() => setPaused(value => !value)}>{reduced ? 'Motion reduced' : paused ? 'Play previews' : 'Pause previews'}</button></nav></header>
    <main>
      <section className={styles.connectedHero} aria-labelledby="atlas-title"><div className={styles.connectedIntro}><div><p className={styles.eyebrow}>THE KANSAS RECORD / CONNECTED SCIENCE</p><h1 id="atlas-title" ref={title} tabIndex={-1}>Ask more of the record.</h1><p>Start with a place. Follow change through time. Connect real measurements, bring your own county data, and save an investigation you can reproduce.</p></div><button type="button" onClick={() => catalogue.current?.scrollIntoView({ behavior: reduced ? 'instant' : 'smooth', block: 'start' })}>{Object.keys(PUBLIC_LAB_SNAPSHOTS).length} data labs · {number.format(PUBLIC_RECORDS)} source rows <span aria-hidden="true">↓</span></button></div><ConnectedWorkspaces/></section>
      <div className={styles.methodStrip} aria-label="Research workflow"><span><b>01</b> Follow a question</span><span><b>02</b> Explore the evidence</span><span><b>03</b> Inspect the source</span><span><b>04</b> Take the record with you</span></div>
      <section className={styles.scienceStrip} aria-label="Tools for scientific exploration"><div><span>01 / RELATIONSHIPS</span><h2>What changes together?</h2><p>Compare two measurements. Inspect Pearson and Spearman association, paired counts and a descriptive fitted line.</p></div><div><span>02 / DISTRIBUTIONS</span><h2>Go beyond the average.</h2><p>Read quartiles, spread and missingness. Follow the highest and lowest source observations into the record.</p></div><div><span>03 / REPRODUCIBILITY</span><h2>Keep the evidence.</h2><p>Download a selection or group summary. Share the exact view, bound to the source snapshot that produced it.</p></div></section>
      <section className={styles.questions} aria-labelledby="questions-title"><div><p className={styles.eyebrow}>START WITH A QUESTION</p><h2 id="questions-title">Real records. Room to explore.</h2><p>Ask a question. Change the measure. Investigate the relationship. Every result starts with real source records.</p></div><div className={styles.questionGrid}>{QUESTIONS.map(([id, question, detail]) => {
        const href = storyById(id)?.href;
        const label = <><span>{question}</span><small>{detail}</small><b aria-hidden="true">↗</b></>;
        return href
          ? <Link key={id} href={href} prefetch={false}>{label}</Link>
          : <button key={id} type="button" onClick={event => open(id, event.currentTarget)}>{label}</button>;
      })}</div></section>
      <section className={styles.catalogue} ref={catalogue} tabIndex={-1} aria-labelledby="research-title"><header className={styles.catalogueHeading}><div><p className={styles.eyebrow}>YOUR FIELDWORK STARTS HERE</p><h2 id="research-title">Open a new perspective.</h2></div><p>Every working plate is drawn from its source snapshot. Search, change the view, compare distributions and relationships, inspect individual records, and export what you find.</p></header>
        <div className={styles.finder}><label className={styles.search}><span aria-hidden="true">⌕</span><span className={styles.srOnly}>Search research labs</span><input type="search" value={query} onChange={event => setQuery(event.target.value)} placeholder="What draws you in? Try water, census, railroads…"/></label><label className={styles.availability}><span>SHOW</span><select value={availability} onChange={event => setAvailability(event.target.value)} aria-label="Data availability"><option value="available">Open labs with data ({AVAILABLE})</option><option value="all">All research</option><option value="ready">Snapshots found ({readyCount})</option><option value="planned">In development</option></select></label></div>
        <div className={styles.catalogueFilters}><div className={styles.groupFilters} role="group" aria-label="Filter research by field">{['All', ...STORY_GROUPS.filter(entry => entry !== 'Data to come' || IMPLEMENTED.some(story => story.group === entry))].map(entry => <button key={entry} type="button" aria-pressed={group === entry} onClick={() => setGroup(entry)}>{entry === 'All' ? 'All fields' : entry}</button>)}</div><span className={styles.resultCount} role="status">{resultCount} {resultCount === 1 ? 'perspective' : 'perspectives'}</span></div>
        {guided.length > 0 && <section className={styles.guided} aria-labelledby="guided-labs-title">
          <div className={styles.sectionRule}><h3 id="guided-labs-title">Guided investigations</h3></div>
          <div className={styles.guidedGrid}>{guided.map(entry => <Link key={entry.id} href={entry.href} prefetch={false} className={styles.guidedCard} style={{ '--atlas-accent': entry.palette[1] }}>
            <span className={styles.guidedTitle}>{entry.title}<span aria-hidden="true">↗</span></span>
            <span>{entry.summary}</span>
            <small>{entry.sources[0]}</small>
          </Link>)}</div>
        </section>}
        {shownReady.length > 0 && <div className={styles.sectionRule}><h3>Research instruments</h3><span>{readyCount} source {readyCount === 1 ? 'snapshot' : 'snapshots'} found this visit</span></div>}
        <div className={styles.researchGrid}>{IMPLEMENTED.map(entry => <ResearchCard key={entry.id} story={entry} hidden={!shownReady.includes(entry)} held={paused || reduced || Boolean(story)} onOpen={open} onState={onState}/>)}</div>
        {!resultCount && <div className={styles.noResults} role="status"><span aria-hidden="true">∅</span><h3>No records in this view.</h3><p>{availability === 'ready' ? 'Source status is checked as previews enter view. Select All research to inspect an unchecked instrument.' : 'Try a source name, a broader topic, or a different field.'}</p><button type="button" onClick={resetFilters}>Show all research</button></div>}
        {planned.length > 0 && <section className={styles.planned} aria-labelledby="planned-title"><div className={styles.sectionRule}><h3 id="planned-title">On the horizon</h3><span>{planned.length} stories in development</span></div><p className={styles.plannedIntro}>The next questions are already taking shape. These entries describe the intended research; they do not yet have a working source-backed instrument.</p><div className={styles.plannedGrid}>{planned.map(entry => <button type="button" key={entry.id} onClick={event => open(entry.id, event.currentTarget)} className={styles.plannedRow}><span className={styles.plannedNumber}>{String(STORIES.indexOf(entry) + 1).padStart(2, '0')}</span><span><small>{entry.kicker}</small><strong>{entry.title}</strong><span>{entry.sources[0]}</span></span><span aria-hidden="true">↗</span></button>)}</div></section>}
      </section>
      <aside className={styles.researchNote}><span className={styles.noteSymbol} aria-hidden="true">∴</span><div><p className={styles.eyebrow}>BEAUTY IN THE PATTERN. TRUST IN THE RECORD.</p><h2>Curiosity is open. Evidence is specific.</h2><p>These open labs include public records from NOAA, the U.S. Census Bureau and USGS, with infrastructure, energy and air-quality records from their named public sources. Coverage dates and retrieval times travel with the data. Filter a view, inspect a record, and take the selection and its sources with you. Snapshots can lag their providers; an observed pattern does not establish a cause.</p></div><Link prefetch={false} href="/observatory/sources">Meet the sources <span aria-hidden="true">↗</span></Link></aside>
    </main>
    <footer className={styles.footer}><span>KANSAS FRONTIER MATRIX <span aria-hidden="true">/</span> THE RESEARCH ATLAS</span><Link prefetch={false} href="/labs/notebook">Your research notebook ↗</Link><Link prefetch={false} href="/">Return to the Kansas map ↑</Link></footer>
    {story && <Suspense fallback={<div className={styles.loading} role="status">Opening the research instrument… <button type="button" onClick={close}>Cancel</button></div>}><StoryLab story={story} paused={paused} reduced={reduced} onMove={id => open(id)} onClose={close}/></Suspense>}
  </div>;
}
