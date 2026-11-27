"use client";

import { useState } from "react";
import Link from "next/link";
import { SCIENCE_TOOLS, SCIENCE_YEARS, scienceToolPath } from "./science-handoff.mjs";
import styles from "./science.module.css";

export default function ScienceLauncher() {
  const [toolId, setToolId] = useState("weather");
  const [year, setYear] = useState(2025);
  const tool = SCIENCE_TOOLS.find(option => option.id === toolId);
  return <section className={styles.launcher} aria-labelledby="science-launcher-heading">
    <div className={styles.launcherIntro}><span className={styles.eyebrow}>Start in seconds / keep the source</span><h2 id="science-launcher-heading">What would you<br /><em>like to understand?</em></h2><p>A question and a year are enough to begin. Choose the place and fine-tune the view inside the tool.</p></div>
    <div className={styles.launcherControls}><label>Choose your question<select value={toolId} onChange={event => setToolId(event.target.value)}>{SCIENCE_TOOLS.map(option => <option key={option.id} value={option.id}>{option.question}</option>)}</select></label><div className={styles.launcherAction}><label>Explore year<select value={year} onChange={event => setYear(Number(event.target.value))}>{SCIENCE_YEARS.map(option => <option key={option}>{option}</option>)}</select></label><Link className={styles.launchButton} href={scienceToolPath(toolId, year)}>Open {tool.label} <span aria-hidden="true">↗</span></Link></div><p className={styles.launcherSupport} aria-live="polite"><strong>{tool.label}</strong> · {tool.support}</p><p className={styles.launcherNote}>Each source has its own geography and clock. Locations are not matched across tools.</p></div>
  </section>;
}
