import type { CSSProperties } from "react";
import { comparisonLabPath } from "./comparison-selection.mjs";
import styles from "./comparison.module.css";

type CoveredValue = { value: number | null; valid: number; expected: number };
type YearPair = { selected: CoveredValue; comparison: CoveredValue };
type ComparisonMetric = {
  id: string;
  label: string;
  unit: string;
  supportUnit: string;
  location: { name: string; scale: string };
  method: string;
  limitation: string;
  timeStandard: string;
  labPath: string;
  attribution: string;
  documentation: string;
  display: { url: string; sha256: string };
  sources: ReadonlyArray<{ url: string; year?: number | null; capturedAt?: string | null }>;
  annual: YearPair;
  monthly: ReadonlyArray<YearPair & { month: number }>;
};
type ComparisonReport = {
  selection: { year: number; compareYear: number };
  location: { id: string; name: string };
  series: ReadonlyArray<ComparisonMetric>;
};

const monthNames = ["January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"];
const formatNumber = new Intl.NumberFormat("en-US", { maximumFractionDigits: 2 });
const formatValue = (value: number | null) => value === null ? "Unavailable" : formatNumber.format(value);

function displayScale(metric: ComparisonMetric) {
  if (metric.unit === "%") return 100;
  const max = Math.max(1, ...metric.monthly.flatMap(({ selected, comparison }) => [selected.value ?? 0, comparison.value ?? 0]));
  const step = 10 ** Math.floor(Math.log10(max));
  const multiple = [1, 2, 5, 10].find((count) => max <= count * step) ?? 10;
  return multiple * step;
}

function ChartBar({ value, max, yearRole }: { value: number | null; max: number; yearRole: "selected" | "comparison" }) {
  const state = value === null ? "missing" : value === 0 ? "zero" : "value";
  return <i className={styles.bar} data-year-role={yearRole} data-value-state={state}
    style={value === null ? undefined : { "--bar-height": `${100 * value / max}%` } as CSSProperties} />;
}

function MonthlyChart({ metric }: { metric: ComparisonMetric }) {
  const max = displayScale(metric);
  return <figure className={styles.figure} aria-hidden="true">
    <figcaption className={styles.plotUnit}>{metric.unit}</figcaption>
    <div className={styles.plot}>
      {[metric.monthly.slice(0, 6), metric.monthly.slice(6)].map((group, index) => <div className={styles.plotGroup} key={index}>
        <div className={styles.axis}><span>{formatValue(max)}</span><span>{formatValue(max / 2)}</span><span>0</span></div>
        {group.map(({ month, selected, comparison }) => <div className={styles.month} key={month}>
          <div className={styles.columns}>
            <ChartBar value={selected.value} max={max} yearRole="selected" />
            <ChartBar value={comparison.value} max={max} yearRole="comparison" />
          </div>
          <span className={styles.monthLabel}>{monthNames[month - 1].slice(0, 3)}</span>
        </div>)}
      </div>)}
    </div>
  </figure>;
}

function YearSummary({ value, year, metric, role }: { value: CoveredValue; year: number; metric: ComparisonMetric; role: "selected" | "comparison" }) {
  return <div className={styles.yearSummary} data-year-role={role}>
    <dt>{year}</dt>
    <dd>
      <strong>{formatValue(value.value)}</strong>{value.value !== null && <span>{metric.unit}</span>}
      <small>{value.valid} of {value.expected} {metric.supportUnit}</small>
    </dd>
  </div>;
}

function TableValue({ value, supportUnit }: { value: CoveredValue; supportUnit: string }) {
  return <td><span>{formatValue(value.value)}</span><small>{value.valid} of {value.expected} {supportUnit}</small></td>;
}

function MetricPanel({ metric, year, compareYear, place }: { metric: ComparisonMetric; year: number; compareYear: number; place: string }) {
  const titleId = `comparison-${metric.id}`;
  return <article className={styles.metric} aria-labelledby={titleId}>
    <header className={styles.metricHeader}>
      <span className={styles.metricPlace}>{metric.location.name} · {metric.location.scale}</span>
      <h3 id={titleId}>{metric.label}</h3>
      <p>{metric.method}</p>
    </header>
    <dl className={styles.annual} aria-label="Calendar-year values and coverage">
      <YearSummary value={metric.annual.selected} year={year} metric={metric} role="selected" />
      <YearSummary value={metric.annual.comparison} year={compareYear} metric={metric} role="comparison" />
    </dl>
    <MonthlyChart metric={metric} />
    <details className={styles.monthlyDetails}>
      <summary>Monthly values and coverage</summary>
      <table>
        <caption>{metric.label} in {metric.unit}, with coverage by month. Values are rounded to at most two decimal places.</caption>
        <thead><tr><th scope="col">Month</th><th scope="col">{year}</th><th scope="col">{compareYear}</th></tr></thead>
        <tbody>{metric.monthly.map(({ month, selected, comparison }) => (
          <tr key={month}>
            <th scope="row">{monthNames[month - 1]}</th>
            <TableValue value={selected} supportUnit={metric.supportUnit} />
            <TableValue value={comparison} supportUnit={metric.supportUnit} />
          </tr>
        ))}</tbody>
      </table>
    </details>
    <details className={styles.provenance}>
      <summary>Source details</summary>
      <p>{metric.limitation} Dates use {metric.timeStandard}.</p>
      <p>{metric.attribution}</p>
      <ul className={styles.sourceList}>
        {metric.sources.map((source) => <li key={`${source.year}:${source.url}`}>
          <a href={source.url}>Original provider file{source.year ? ` · ${source.year}` : ""}</a>
          {source.capturedAt && <time dateTime={source.capturedAt}>Captured {source.capturedAt.slice(0, 10)}</time>}
        </li>)}
        <li><a href={metric.display.url}>Verified display snapshot</a><span>SHA‑256 <code>{metric.display.sha256}</code></span></li>
      </ul>
    </details>
    <footer className={styles.metricLinks}>
      <a href={comparisonLabPath(metric.id, year, place) ?? metric.labPath}>Explore {year} in the full lab</a>
      <a href={metric.documentation}>Provider documentation</a>
    </footer>
  </article>;
}

export default function ComparisonView({ report }: { report: ComparisonReport }) {
  const { year, compareYear } = report.selection;
  return <section className={styles.results} aria-labelledby="comparison-results">
    <header className={styles.resultsHeader}>
      <div>
        <h2 id="comparison-results">{report.location.name}</h2>
        <p>Each chart shares one scale across the two years. Coverage shows how many days or assessments support each value.</p>
      </div>
      <ul className={styles.legend} aria-label="Chart key">
        <li><i className={styles.key} data-year-role="selected" aria-hidden="true" />{year}</li>
        <li><i className={styles.key} data-year-role="comparison" aria-hidden="true" />{compareYear}</li>
        <li><i className={styles.zeroKey} aria-hidden="true" />Zero</li>
        <li><i className={styles.missingKey} aria-hidden="true" />Unavailable</li>
      </ul>
    </header>
    <div className={styles.metrics}>{report.series.map((metric) => <MetricPanel
      key={metric.id} metric={metric} year={year} compareYear={compareYear} place={report.location.id} />)}</div>
  </section>;
}
