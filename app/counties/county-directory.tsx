"use client";

import { useRef, useState } from "react";
import Link from "next/link";
import styles from "./counties.module.css";

type CountyEntry = { name: string; href: string };

export function CountyDirectory({ counties }: { counties: readonly CountyEntry[] }) {
  const [search, setSearch] = useState("");
  const input = useRef<HTMLInputElement>(null);
  const query = search.trim().toLowerCase().replace(/\s+/g, " ");
  const matches = query ? counties.filter(county => county.name.toLowerCase().includes(query)) : counties;
  const resultLabel = matches.length === 0 ? "No counties found." :
    `${matches.length} ${matches.length === 1 ? "county" : "counties"}`;

  return <>
    <div className={styles.finder} role="search" aria-label="County directory">
      <label htmlFor="county-search">Search by county name</label>
      <div className={styles.searchRow}>
        <input
          ref={input}
          id="county-search"
          type="search"
          value={search}
          placeholder="e.g. Sedgwick"
          onChange={event => setSearch(event.target.value)}
        />
        {search && <button type="button" onClick={() => {
          setSearch("");
          input.current?.focus();
        }}>Clear</button>}
      </div>
    </div>
    <p className={styles.resultCount} role="status">{resultLabel}</p>
    <ul className={styles.index} aria-label="County results">
      {matches.map(county => <li key={county.href}><Link href={county.href} prefetch={false}>{county.name}</Link></li>)}
    </ul>
  </>;
}
