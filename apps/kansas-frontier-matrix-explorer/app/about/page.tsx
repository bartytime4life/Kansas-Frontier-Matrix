import type { Metadata } from "next";
import Link from "next/link";
import { REPOSITORY_SNAPSHOT } from "../repository-updates";

export const metadata: Metadata = {
  title: "About · Kansas Frontier Matrix Explorer",
  description: "How to use the Kansas Frontier Matrix map, evidence states, custom reports, and public-safe demonstration boundaries.",
};

const evidenceStates = [
  ["ANSWER", "A visible record has a matching demonstration evidence reference for its bounded claim."],
  ["CORRECTED", "A correction remains attached to the current record and report output."],
  ["MISSING_EVIDENCE", "The Explorer shows the gap and declines to infer an answer."],
  ["SOURCE_STALE", "The source context is too old for a current claim without additional review."],
  ["GENERALIZED_GEOMETRY", "The location or shape is deliberately coarse and cannot support precise use."],
  ["SUPERSEDED", "The record remains available for history and lineage but is not current support."],
  ["RESTRICTED_ACCESS", "The interface cannot expose the protected material."],
  ["DENIED_BY_POLICY", "Policy blocks the requested detail and the Explorer fails closed."],
  ["ERROR", "A safe result could not be resolved; no fallback claim is generated."],
] as const;

export default function AboutPage() {
  return <div className="about-page">
    <nav className="about-nav" aria-label="About page navigation">
      <div className="brand-lockup" aria-label="Kansas Frontier Matrix">
        <span className="mark" aria-hidden="true">KFM</span>
        <span><strong>Kansas Frontier Matrix</strong><small>Explorer guide + boundaries</small></span>
      </div>
      <Link href="/">Open the map</Link>
    </nav>

    <main className="about-content">
      <header className="about-hero">
        <div><span>ABOUT THE EXPLORER</span><h1>A map workbench for inspecting data and producing bounded reports.</h1><p>The Explorer is an actionable spatial interface: choose layers, move through time, inspect features, compare records, measure on screen, and create custom reports from the current map context.</p></div>
        <aside><strong>Current data posture</strong><p>The map currently uses site-local synthetic and generalized demonstration records. It demonstrates the interface and trust behavior; it is not a released operational KFM data service.</p></aside>
      </header>

      <section className="about-section">
        <div className="about-section-heading"><span>PRIMARY WORKFLOW</span><h2>Start with a question, finish with a report.</h2></div>
        <div className="about-workflow-grid">
          <article><span>01</span><h3>Frame the map</h3><p>Search a place or feature, move the camera, choose a time, and show only the layers relevant to the question.</p></article>
          <article><span>02</span><h3>Inspect records</h3><p>Select map features or use the searchable feature index. Evidence state, source role, freshness, release posture, and limitations remain attached.</p></article>
          <article><span>03</span><h3>Set report scope</h3><p>Report on the current viewport, all visible layers, or one selected feature. Choose included layers, detail level, and report sections.</p></article>
          <article><span>04</span><h3>Use the result</h3><p>Copy a structured report, download a printable HTML report, or download JSON for another analysis workflow.</p></article>
        </div>
      </section>

      <section className="about-section">
        <div className="about-section-heading"><span>MAP CAPABILITIES</span><h2>The main interface is built for action, not presentation.</h2></div>
        <div className="about-capability-grid">
          <article><h3>Layers + time</h3><p>Control visibility, opacity, order, domain filters, temporal steps, and two basemap treatments while preserving the selected context.</p></article>
          <article><h3>Search + inspect</h3><p>Search layers, feature IDs, evidence states, and places. Limit results to the viewport or visible layers and fit the map to the results.</p></article>
          <article><h3>Compare + measure</h3><p>Compare two layer records without flattening their source or release differences. Measure approximate distance or area locally on screen.</p></article>
          <article><h3>Reports + exports</h3><p>Reports summarize filtered data for people. Public-safe JSON exports preserve structured map context, attribution, time, evidence, and redactions.</p></article>
        </div>
      </section>

      <section className="about-section">
        <div className="about-section-heading"><span>EVIDENCE STATES</span><h2>The interface says what a record can support—and when it cannot.</h2></div>
        <div className="about-state-table">{evidenceStates.map(([state, description]) => <article key={state}><strong>{state}</strong><p>{description}</p></article>)}</div>
      </section>

      <section className="about-section">
        <div className="about-section-heading"><span>TRUST BOUNDARY</span><h2>Useful spatial work without turning the renderer into an authority.</h2></div>
        <div className="about-boundary">
          <article><h3>What the Explorer can do</h3><ul><li>Display admitted site fixtures on MapLibre.</li><li>Filter and summarize visible, selected, or viewport-scoped records.</li><li>Carry citations, attribution, uncertainty, corrections, and limitations into reports.</li><li>Withhold a browser-location-derived camera from shares, receipts, exports, and diagnostics.</li></ul></article>
          <article><h3>What it does not claim</h3><ul><li>A map pixel, overlap, or proximity is not evidence.</li><li>A generated report cannot release, publish, admit, approve, or authorize data.</li><li>Screen measurements are not survey, cadastral, engineering, legal, or navigational results.</li><li>Protected geometry and unsupported claims are not reconstructed or inferred.</li></ul></article>
        </div>
      </section>

      <section className="about-section">
        <div className="about-section-heading"><span>PROJECT CONTEXT</span><h2>Repository evidence and site behavior remain distinguishable.</h2></div>
        <div className="about-boundary">
          <article><h3>Repository checkpoint</h3><ul><li>{REPOSITORY_SNAPSHOT.repository}</li><li>Inspected main@{REPOSITORY_SNAPSHOT.shortCommit}</li><li>{REPOSITORY_SNAPSHOT.inspectedAt}</li><li>Architecture, functions, feature maturity, and transition records are read-only context in this Site.</li></ul></article>
          <article><h3>Site-local runtime</h3><ul><li>MapLibre GL JS 6.6.0</li><li>Local GeoJSON demonstration sources</li><li>No direct model endpoint or live operational source</li><li>No release, deployment, promotion, or publication authority</li></ul></article>
        </div>
      </section>

      <section className="about-final-action"><div><h2>Ready to work with the map?</h2><p>Open the Explorer, frame your question spatially, and build a custom report from the data in view.</p></div><Link href="/">Open map + report builder</Link></section>
    </main>
  </div>;
}
