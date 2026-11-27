"use client";

import { useState } from "react";
import Link from "next/link";
import { SCIENCE_TOOLS, scienceSelectionPath, scienceToolPath, serviceInquiryPath } from "./science-handoff.mjs";
import styles from "./science-nav.module.css";

/** @param {{ active: string, selection?: Record<string, unknown>, sourceHref?: string, sourceLabel?: string, extraLinks?: Array<{href: string, label: string}> }} props */
export default function ScienceNav({ active, selection = undefined, sourceHref = "", sourceLabel = "Source & methods ↓", extraLinks = [] }) {
  const [destination, setDestination] = useState(SCIENCE_TOOLS.some(tool => tool.id === active) ? active : "weather");
  const current = SCIENCE_TOOLS.find(tool => tool.id === active);
  const year = Number(selection?.year ?? selection?.toYear ?? 2025);
  let context = "";
  try { if (current && selection) context = scienceSelectionPath(active, selection); } catch { /* Do not carry an unsupported selector. */ }
  const openPath = destination === active && context ? context : scienceToolPath(destination, year);
  const comparisonPath = active === "comparison" && context ? context : scienceToolPath("comparison", year);
  return <nav className={styles.nav} aria-label="Science and Labs navigation">
    <div className={styles.row}>
      <Link className={styles.brand} href="/science" aria-current={active === "hub" ? "page" : undefined}><span>KFM</span><span>Science &amp; Labs<br /><small>Find a lab or report</small></span></Link>
      <div className={styles.switcher}><label>Open another science tool<select aria-label="Science destination" value={destination} onChange={event => setDestination(event.target.value)}>{SCIENCE_TOOLS.map(tool => <option key={tool.id} value={tool.id}>{tool.label}</option>)}</select></label><Link className={styles.open} href={openPath}>Open <span aria-hidden="true">↗</span></Link></div>
      <div className={styles.links}><Link href={comparisonPath} aria-current={active === "comparison" ? "page" : undefined}>Year comparison</Link><Link className={styles.custom} href={active === "services" ? "#project-brief" : serviceInquiryPath(context)} aria-current={active === "services" ? "page" : undefined}>Request custom work <span aria-hidden="true">↗</span></Link></div>
    </div>
    <div className={styles.subrow}><div>{current && <Link href={context || current.path} aria-current="page">{current.label} <span className={styles.current}>/ current</span></Link>}<Link href="/">Explorer ↗</Link>{sourceHref && <a href={sourceHref}>{sourceLabel}</a>}{extraLinks.map(link => <Link key={link.href} href={link.href}>{link.label}</Link>)}</div><p>Other tools open in {year}. Choose their location inside; coverage differs.</p></div>
  </nav>;
}
