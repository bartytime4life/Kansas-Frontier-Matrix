import Link from "next/link";
import styles from "./science.module.css";

const sources = [
  { key: "climate", label: "Heat and Rain", href: "/labs/heat-and-rain", type: "Weather station observations" },
  { key: "drought", label: "County Drought", href: "/labs/county-drought", type: "Weekly county assessments" },
  { key: "soil", label: "Soil Profile", href: "/labs/soil-profile", type: "In-ground station observations" },
  { key: "air", label: "Daily Air Quality", href: "/labs/daily-air-quality", type: "Reported county AQI" },
  { key: "sunlight", label: "Sunlight and Sky", href: "/labs/sunlight-and-sky", type: "Modeled solar estimates" },
];

function coverageDate(value) {
  return new Intl.DateTimeFormat("en-US", { dateStyle: "medium", timeZone: "UTC" }).format(new Date(value));
}

export default function ScienceDataCoverage({ manifests }) {
  return <section className={styles.coverage} id="data-coverage" aria-labelledby="data-coverage-heading">
    <h2 id="data-coverage-heading">Data coverage and dates</h2>
    <p>These historical snapshots have a fixed analysis window. The source capture date records when KFM collected the source material. Each lab shows its own missing observations within the window.</p>
    <ul className={styles.coverageCards}>{sources.map(({ key, label, href, type }) => {
      const manifest = manifests[key];
      return <li key={key}>
        <h3><Link href={href} prefetch={false}>{label}</Link></h3>
        <p>{type} · {manifest.provider}</p>
        <dl>
          <dt>Analysis window</dt>
          <dd><time dateTime={manifest.period.from}>{coverageDate(manifest.period.from)}</time> to{" "}<time dateTime={manifest.period.to}>{coverageDate(manifest.period.to)}</time></dd>
          <dt>Latest recorded capture</dt>
          <dd><time dateTime={manifest.generatedAt}>{coverageDate(manifest.generatedAt)} UTC</time></dd>
        </dl>
        <a href={manifest.documentation}>Provider documentation <span aria-hidden="true">↗</span></a>
      </li>;
    })}</ul>
  </section>;
}
