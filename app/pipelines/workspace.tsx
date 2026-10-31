'use client';
import { useEffect, useState } from 'react';
import Link from 'next/link';
import { readBoundedJson } from '../bounded-json';
import type { CardPipelineBinding, PipelineDefinition, PipelineHealthSummary } from '../card-pipelines';
import './workspace.css';
type Card = CardPipelineBinding & { state: string; coverage: string; expansion: string };
type Snapshot = { format: string; checkedAt: string; state: string; cards: Card[]; sources: (PipelineDefinition & { health: PipelineHealthSummary })[] };
const modes: Record<string, string> = {
  display: 'Explorer display · checked when selected', candidate: 'Proposed pipeline · acquisition disabled',
  'pc-capture': 'PC capture adapter · hosted release checked separately', calculated: 'Calculated context · not measured observations',
  index: 'Search index · check permitted record coverage',
};
const labels: Record<string, string> = {
  'not-checked': 'Not checked here', 'coverage-gap': 'Coverage gap', candidate: 'Awaiting source review', demo: 'Demonstration',
  available: 'Available snapshot', empty: 'Successful empty snapshot', partial: 'Partial coverage', stale: 'Stale snapshot',
  held: 'Awaiting approved release', unavailable: 'Temporarily unavailable',
};
export default function PipelineDashboard({ initial }: { initial: Snapshot }) {
  const [snapshot, setSnapshot] = useState(initial), [attempt, setAttempt] = useState(0);
  const [error, setError] = useState(false), [checking, setChecking] = useState(true);
  const [filter, setFilter] = useState('topic');
  useEffect(() => {
    const controller = new AbortController(), timeout = setTimeout(() => controller.abort(), 12000);
    let active = true;
    queueMicrotask(() => { if (active) setChecking(true); });
    void fetch('/api/pipeline/v1/cards', { cache: 'no-store', signal: controller.signal })
      .then(async response => {
        if (!response.ok) throw new Error();
        const value = await readBoundedJson(response, 256 * 1024, controller.signal) as Snapshot;
        if (value?.format !== 'kfm-card-pipelines-v1' || !Array.isArray(value.cards) || !Array.isArray(value.sources)) throw new Error();
        if (active) { setSnapshot(value); setError(false); }
      }).catch(() => { if (active) setError(true); })
      .finally(() => { clearTimeout(timeout); if (active) setChecking(false); });
    return () => { active = false; clearTimeout(timeout); controller.abort(); };
  }, [attempt]);
  useEffect(() => {
    const interval = setInterval(() => { if (document.visibilityState === 'visible') setAttempt(value => value + 1); }, 60000);
    return () => clearInterval(interval);
  }, []);
  const sources = new Map(snapshot.sources.map(source => [source.id, source]));
  return <main className="pipeline-workspace">
    <Link href="/">← Kansas Frontier Matrix</Link>
    <h1>Card pipelines &amp; source coverage</h1>
    <p>Follow each current topic card and map recipe to its source context, planned data and review requirements.</p>
    <p>Existing map displays are checked when selected in the Explorer. This page checks approved hosted snapshots; it does not measure the private PC’s capture jobs.</p>
    <div className="pipeline-toolbar"><label>Show <select value={filter} onChange={event => setFilter(event.target.value)}>
      {(['topic', 'recipe'] as const).map(kind => <option key={kind} value={kind}>{snapshot.cards.filter(card => card.kind === kind).length} {kind === 'topic' ? 'welcome topics' : 'map recipes'}</option>)}
    </select></label><button type="button" disabled={checking} onClick={() => setAttempt(value => value + 1)}>{checking ? 'Checking…' : 'Check snapshots'}</button></div>
    <p role="status">{error ? 'Snapshot check failed. Last checked details may be out of date.' : checking ? 'Checking hosted snapshots…' : snapshot.state === 'setup-pending' ? 'Hosted snapshot publication is not configured here. Local PC activity is separate.' : snapshot.state === 'degraded' ? 'Some hosted snapshots could not be checked.' : `Hosted snapshots checked ${snapshot.checkedAt}`}</p>
    <div className="pipeline-cards">{snapshot.cards.filter(card => card.kind === filter).map(card => <article key={card.id}>
      <h2>{card.title}</h2><p className="pipeline-status">{error ? 'Current snapshot status unknown' : labels[card.state] ?? card.state}</p>
      {card.demo && <p>Illustrative demonstrations are separate from factual evidence.</p>}
      {!card.required.length && !card.optional.length && !card.demo && <p>No bundled source set. Search coverage must be checked for this question.</p>}
      {[['Source dependencies', card.required], ['Optional source context', card.optional], ['Planned expansion · review required', card.gaps]].map(([heading, ids]) => {
        const values = ids as readonly string[];
        return values.length ? <section key={heading as string}><h3>{heading as string}</h3><ul>{values.map(id => {
          const source = sources.get(id); if (!source) return <li key={id}>Coverage details unavailable</li>;
          const expired = source.health.approvalExpiresAt && Date.parse(source.health.approvalExpiresAt) <= Date.now();
          return <li key={id}><strong>{source.title}</strong><span>{modes[source.mode]}</span>
            <span>{error ? 'Current status unknown' : expired ? 'Approval expired · refresh required' : labels[source.health.state] ?? source.health.state}</span>
            {source.health.retrievedAt && <span>Snapshot retrieved <time dateTime={source.health.retrievedAt}>{source.health.retrievedAt}</time></span>}
            {source.health.observedThrough && <span>Latest returned source time <time dateTime={source.health.observedThrough}>{source.health.observedThrough}</time></span>}
            {source.mode === 'candidate' ? <span>{source.nextGate}</span> : <span>{source.cadence}</span>}
          </li>;
        })}</ul></section> : null;
      })}
      <small>{card.expansion === 'review-required' ? 'Some requested domain data still needs qualification.' : 'Source context does not establish admitted evidence.'}</small>
    </article>)}</div>
    <p><Link href="/data-status">Database &amp; intake status</Link> · <Link href="/curated">Inspect approved snapshots</Link> · <Link href="/observatory/sources">Source observatory</Link></p>
  </main>;
}
