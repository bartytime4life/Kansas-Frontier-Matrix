'use client';

import { useState } from 'react';
import Link from 'next/link';
import { compareIssues, comparisonReceipt } from './cohort.mjs';
import cohort from './reflector-cohort.json';
import styles from './pulse.module.css';

const dateFormat = new Intl.DateTimeFormat('en-US', { dateStyle: 'long', timeZone: 'UTC' });
const percent = new Intl.NumberFormat('en-US', { style: 'percent', maximumFractionDigits: 1 });
const dateLabel = date => dateFormat.format(new Date(`${date}T00:00:00Z`));
const pageTotal = cohort.issues.reduce((total, issue) => total + issue.pageCount, 0);
const defaults = ['railroad', 'wheat'];

export default function NewspaperPulse() {
  const [terms, setTerms] = useState(defaults);
  const [result, setResult] = useState(() => compareIssues(cohort, ...defaults));
  const [issueDate, setIssueDate] = useState(cohort.issues[0].date);
  const [matchesOnly, setMatchesOnly] = useState(true);
  const [error, setError] = useState('');
  const [announcement, setAnnouncement] = useState('');
  const selected = result.issues.find(issue => issue.date === issueDate);
  const visiblePages = selected.pages.filter(page => !matchesOnly || page.matches.some(Boolean));

  function compare(event) {
    event.preventDefault();
    const next = compareIssues(cohort, ...terms);
    if (!next) {
      setError('Enter two different words using letters or numbers.');
      return;
    }
    setError('');
    setResult(next);
    setAnnouncement(`Compared ${next.terms.join(' and ')} across ${pageTotal} digitized pages.`);
  }

  function download() {
    const receipt = comparisonReceipt(cohort, result);
    const objectUrl = URL.createObjectURL(new Blob([JSON.stringify(receipt, null, 2)], { type: 'application/json' }));
    const link = document.createElement('a');
    link.href = objectUrl;
    link.download = 'kfm-newspaper-pulse.json';
    link.click();
    setTimeout(() => URL.revokeObjectURL(objectUrl), 1000);
  }

  const searchYear = selected.date.slice(0, 4);
  const searchTerm = result.terms.find(term => !['and', 'or', 'not'].includes(term));
  const searchUrl = searchTerm ? `/data-library?${new URLSearchParams({
    q: searchTerm, source: 'newspapers', title: cohort.lccn, from: searchYear, to: searchYear,
  })}#archive-search-title` : null;

  return <main className={styles.page}>
    <header className={styles.hero}>
      <nav aria-label="Research navigation">
        <Link href="/labs">Research Labs</Link>
        <Link href="/data-library#archive-search-title">Archive search</Link>
      </nav>
      <div className={styles.heroBody}>
        <div>
          <h1>Newspaper Pulse</h1>
          <p>Compare two words in the <i>{cohort.title}</i> across two digitized issues published a decade apart.</p>
        </div>
        <dl className={styles.coverage}>
          <div><dt>Digitized pages</dt><dd>{pageTotal}</dd></div>
          <div><dt>January editions</dt><dd>1890 · 1900</dd></div>
        </dl>
      </div>
    </header>

    <div className={styles.workspace}>
      <section aria-labelledby="pulse-comparison">
        <h2 id="pulse-comparison">Compare words</h2>
        <form className={styles.form} onSubmit={compare}>
          {terms.map((word, index) => <label key={index}>
            {index === 0 ? 'First word' : 'Second word'}
            <input type="search" required maxLength={40} value={word} onChange={event => {
              const next = [...terms];
              next[index] = event.target.value;
              setTerms(next);
            }} />
          </label>)}
          <button type="submit">Compare words</button>
        </form>
        {error && <p className={styles.error} role="alert">{error}</p>}
        <p className={styles.srOnly} role="status">{announcement}</p>

        <figure className={styles.chart}>
          <figcaption>Share of digitized pages containing each word</figcaption>
          <div className={styles.chartGrid}>
            {result.issues.map(issue => <section className={styles.issue} key={issue.date} aria-label={dateLabel(issue.date)}>
              <header>
                <h3>{dateLabel(issue.date)}</h3>
                <span>{issue.pageCount} pages</span>
              </header>
              {issue.shares.map((share, index) => <div key={index} className={styles.series}>
                <div><strong>{result.terms[index]}</strong><span>{issue.totals[index]} of {issue.pageCount} · {share === null ? 'Unavailable' : percent.format(share)}</span></div>
                <div className={styles.track} aria-hidden="true"><div data-series={index} style={{ width: `${(share ?? 0) * 100}%` }} /></div>
              </div>)}
              <div className={styles.axis} aria-hidden="true"><span>0%</span><span>50%</span><span>100%</span></div>
            </section>)}
          </div>
        </figure>
        <p className={styles.method}>A word counts once on each page where it appears in machine-read text (OCR). Spelling, OCR errors and the two-issue selection limit the comparison.</p>
      </section>

      <section className={styles.records} aria-labelledby="pulse-source-pages">
        <h2 id="pulse-source-pages">Read the source pages</h2>
        <div className={styles.recordControls}>
          <label>Issue
            <select value={issueDate} onChange={event => setIssueDate(event.target.value)}>
              {result.issues.map(issue => <option key={issue.date} value={issue.date}>{dateLabel(issue.date)}</option>)}
            </select>
          </label>
          <label className={styles.checkbox}>
            <input type="checkbox" checked={matchesOnly} onChange={event => setMatchesOnly(event.target.checked)} /> Show matching pages only
          </label>
          <a href={selected.issueUrl}>Open the full issue at the Library of Congress</a>
        </div>
        <ul className={styles.pageList}>
          {visiblePages.map(page => <li key={page.url}>
            <a href={page.url}>Page {page.number}</a>
            <span>{page.matches.some(Boolean) ? result.terms.filter((_, index) => page.matches[index]).join(' · ') : 'No OCR match'}</span>
          </li>)}
        </ul>
        {visiblePages.length === 0 && <p>Neither word appeared in the OCR for this issue. Show all pages to inspect the scans.</p>}
        <div className={styles.actions}>
          <button type="button" onClick={download}>Download comparison and sources · JSON</button>
          {searchUrl && <Link href={searchUrl}>Search the {searchYear} archive for “{searchTerm}”</Link>}
        </div>
      </section>

      <footer className={styles.sources}>
        <p><a href={cohort.source.url}>{cohort.source.provider}</a> · Digitized by {cohort.source.digitizedBy} · Retrieved {dateLabel(cohort.retrievedAt.slice(0, 10))}</p>
        <a href={cohort.source.rightsUrl}>Rights and access</a>
      </footer>
    </div>
  </main>;
}
