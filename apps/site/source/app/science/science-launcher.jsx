"use client";

import { useState } from "react";
import Link from "next/link";
import { SCIENCE_YEARS } from "./science-handoff.mjs";
import { directoryEntryPath, filterScienceDirectory } from "./science-directory.mjs";
import styles from "./science.module.css";

export default function ScienceLauncher({ entries }) {
  const [query, setQuery] = useState("");
  const [topic, setTopic] = useState("");
  const [year, setYear] = useState("");
  const topics = [...new Set(entries.map(entry => entry.topic))];
  const results = filterScienceDirectory(entries, query, topic);

  return <section className={styles.directory} id="find-a-lab" aria-labelledby="science-launcher-heading">
    <h2 id="science-launcher-heading">Find a lab or report</h2>
    <div className={styles.filters}>
      <label>Search Science &amp; Labs<input type="search" value={query} maxLength={120} onChange={event => setQuery(event.target.value)} placeholder="Try drought, temperature, or NASA" /></label>
      <label>Topic<select value={topic} onChange={event => setTopic(event.target.value)}><option value="">All topics</option>{topics.map(item => <option key={item}>{item}</option>)}</select></label>
      <label>Starting year<select value={year} onChange={event => setYear(event.target.value)}><option value="">Default year</option>{SCIENCE_YEARS.map(option => <option key={option}>{option}</option>)}</select></label>
    </div>
    <div className={styles.resultsHeader}>
      <p role="status">{results.length} {results.length === 1 ? "result" : "results"}{year && " · Year applies to the dated science labs and year comparison."}</p>
      {(query || topic || year) && <button type="button" onClick={() => { setQuery(""); setTopic(""); setYear(""); }}>Clear filters</button>}
    </div>
    {results.length ? <ul className={styles.cards}>{results.map(entry => <li key={entry.id}>
      <article>
        <p className={styles.cardType}>{entry.kind} · {entry.topic}</p>
        <h3><Link href={directoryEntryPath(entry, year ? Number(year) : null)} prefetch={false}>{entry.label} <span aria-hidden="true">↗</span></Link></h3>
        <p>{entry.question}</p>
        <p className={styles.cardCoverage}>{entry.coverage}</p>
        <p className={styles.cardSource}>{entry.source}</p>
      </article>
    </li>)}</ul> : <p>Try another word or change the topic. Search checks titles, subjects, and source names.</p>}
  </section>;
}
