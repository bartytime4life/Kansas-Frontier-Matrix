"use client";

import { useState } from "react";
import { compareSpreads, evidenceByDate, replays, sourceGuides } from "./model.mjs";
import styles from "./wheat-trade.module.css";

const dateLabel = new Intl.DateTimeFormat("en-US", { dateStyle: "medium", timeZone: "UTC" });
const displayDate = (value: string) => dateLabel.format(new Date(`${value}T00:00:00Z`));
const dollars = new Intl.NumberFormat("en-US", { style: "currency", currency: "USD", signDisplay: "exceptZero" });

function SpreadComparison({ dates }: { dates: string[] }) {
  const [earlier, setEarlier] = useState("");
  const [later, setLater] = useState("");
  const change = compareSpreads(earlier, later);

  return (
    <div className={styles.comparison}>
      <p>From Table 2a, enter the two signed HRW “KS–Gulf” values in dollars per bushel. A positive change means the Kansas-minus-Gulf value moved up. The figures stay in this page.</p>
      <div className={styles.controls}>
        <label>Earlier observation · {displayDate(dates[0])}<input type="text" inputMode="text" maxLength={7} value={earlier} onChange={(event) => setEarlier(event.target.value)} placeholder="e.g., -2.10" /></label>
        <label>Later observation · {displayDate(dates[1])}<input type="text" inputMode="text" maxLength={7} value={later} onChange={(event) => setLater(event.target.value)} placeholder="e.g., -2.00" /></label>
      </div>
      <p className={styles.result} role="status">
        {change !== null
          ? <>Change in entered spread <strong>{dollars.format(change / 100)} per bushel</strong></>
          : "Enter both signed dollar values with up to two decimal places. Leave an unavailable quote blank."}
      </p>
      <p>Table 2a compares the stated inland and Gulf bid specifications. The spread combines market differences. Use the separate freight tables for published charge references.</p>
    </div>
  );
}

export default function TradeReplay() {
  const [replayIndex, setReplayIndex] = useState(0);
  const [dateIndex, setDateIndex] = useState(replays[0].dates.length - 1);
  const replay = replays[replayIndex];
  const cutoff = replay.dates[dateIndex];
  const evidence = evidenceByDate(replay, cutoff);
  const reports = evidence.filter((entry) => entry.observations);
  const [reportSelection, setReportSelection] = useState("");
  const report = reports.find((entry) => entry.published === reportSelection) ?? reports.at(-1);

  return (
    <>
      <section className={styles.section} aria-labelledby="wheat-replay">
        <h2 id="wheat-replay">Replay the reporting timeline</h2>
        <div className={styles.controls}>
          <label>Case study<select value={replayIndex} onChange={(event) => {
            const next = Number(event.target.value);
            setReplayIndex(next);
            setDateIndex(replays[next].dates.length - 1);
            setReportSelection("");
          }}>
            {replays.map((item, index) => <option key={item.id} value={index}>{item.label}</option>)}
          </select></label>
          <label>Reports available by<select value={dateIndex} onChange={(event) => {
            setDateIndex(Number(event.target.value));
            setReportSelection("");
          }}>
            {replay.dates.map((date, index) => <option key={date} value={index}>{displayDate(date)}</option>)}
          </select></label>
        </div>
        <p className={styles.status} role="status">
          {evidence.length === 0 ? "None of the selected case-study sources had been published by this date." : `${evidence.length} selected ${evidence.length === 1 ? "source" : "sources"} published by ${displayDate(cutoff)}.`}
        </p>
        <ol className={styles.timeline}>
          {evidence.map((entry) => <li key={entry.published}>
            <div>
              <span className={styles.kind}>{entry.kind}</span>
              <p className={styles.date}>Published <time dateTime={entry.published}>{displayDate(entry.published)}</time></p>
              {entry.effective && <p className={styles.date}>Stated start <time dateTime={entry.effective}>{displayDate(entry.effective)}</time>
                {entry.effective > cutoff ? " · scheduled at cutoff" : ""}
              </p>}
            </div>
            <div>
              <h3>{entry.title}</h3>
              <p>{entry.detail}</p>
              <a href={entry.source}>Open the original source</a>
            </div>
          </li>)}
        </ol>
      </section>

      {report?.observations && (
        <section className={styles.section} aria-labelledby="wheat-comparison">
          <h2 id="wheat-comparison">Compare two published weeks</h2>
          <label className={styles.report}>USDA report date<select value={report.published} onChange={(event) => setReportSelection(event.target.value)}>
            {reports.map((entry) => <option key={entry.published}>{entry.published}</option>)}
          </select></label>
          <a href={report.source}>Open the {displayDate(report.published)} Grain Transportation Report and find Table 2a</a>
          <SpreadComparison key={`${replay.id}:${cutoff}:${report.published}`} dates={report.observations} />
        </section>
      )}

      <section className={styles.section} aria-labelledby="wheat-sources">
        <h2 id="wheat-sources">Trace the next signal</h2>
        <p>These catalogs can contain newer releases than the replay date. When evaluating a Kansas price change, check whether shipping, local demand and harvest timing all fit the evidence.</p>
        <ul className={styles.guides}>
          {sourceGuides.map(({ title, href, description }) => <li key={href}><a href={href}>{title}</a><p>{description}</p></li>)}
        </ul>
      </section>
    </>
  );
}
