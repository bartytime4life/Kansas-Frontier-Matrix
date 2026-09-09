import type { Metadata } from "next";
import Link from "next/link";
import { REPOSITORY_SNAPSHOT } from "../repository-updates";

export const metadata: Metadata = {
  title: "About · Kansas Frontier Matrix Explorer",
  description: "How to use the Kansas Frontier Matrix map, vector basemap context, Qwen companion, evidence states, and public-safe demonstration boundaries.",
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
        <div><span>ABOUT THE EXPLORER</span><h1>A map-first Living Atlas for seeing Kansas in context.</h1><p>The Explorer opens on a real MapLibre Kansas vector map with time, layers, and place context. Start with a view, then bring in evidence, reports, and Qwen interpretation only when they help answer the question.</p></div>
        <aside><strong>Current data posture</strong><p>The map currently uses site-local synthetic and generalized demonstration records. It demonstrates the interface and trust behavior; it is not a released operational KFM data service.</p></aside>
      </header>

      <section className="about-section">
        <div className="about-section-heading"><span>PRIMARY WORKFLOW</span><h2>Start with a question, finish with a report.</h2></div>
        <div className="about-workflow-grid">
          <article><span>01</span><h3>Frame the map</h3><p>Search a place or feature, move the camera, choose a time, and show only the layers relevant to the question.</p></article>
          <article><span>02</span><h3>Inspect records</h3><p>Select map features or use the searchable feature index. Evidence state, source role, freshness, release posture, and limitations remain attached.</p></article>
          <article><span>03</span><h3>Set report scope</h3><p>Report on the moving viewport, a locked area of interest, all visible layers, or one selected feature. Choose included layers, detail level, and report sections.</p></article>
          <article><span>04</span><h3>Use the result</h3><p>Copy a structured report, download a printable HTML report, or download JSON for another analysis workflow.</p></article>
        </div>
      </section>

      <section className="about-section">
        <div className="about-section-heading"><span>MAP CAPABILITIES</span><h2>The main interface is built for action, not presentation.</h2></div>
        <div className="about-capability-grid">
          <article><h3>Real map + context</h3><p>The default view is a real attributed Kansas vector basemap with counties, places, roads, rail, water, and labels. Satellite imagery and OpenStreetMap raster context remain optional display modes; local KFM overlays stay visibly separate from all basemaps.</p></article>
          <article><h3>Views + layers + time</h3><p>Start from a named Living Atlas investigation, then control visibility, opacity, order, temporal steps, evidence filters, and basemap treatments across the domain atlas.</p></article>
          <article><h3>Search + inspect</h3><p>Search layers, feature IDs, evidence states, and places. From a committed feature, discover nearby cross-domain records using generalized anchors and fit or reveal the represented layers.</p></article>
          <article><h3>Qwen map companion</h3><p>Ask Qwen about the active place, time, visible layers, or selected record. The bridge receives a bounded map-context packet; it never becomes the evidence authority and stays usable with local Qwen/Ollama when the Site endpoint is not configured.</p></article>
          <article><h3>Spatial analysis + motion</h3><p>Shift-drag a MapLibre report area, move through camera history, compare records, or use reduced-motion-aware water, smoke, fire, hazard, habitat, transport, and city effects that change paint only—not evidence.</p></article>
          <article><h3>Places, stories + reports</h3><p>Save complete map states as ordered device-local investigation stops, play the paused four-step story, and produce printable HTML or structured JSON with filters, evidence, attribution, and redactions.</p></article>
        </div>
      </section>

      <section className="about-section">
        <div className="about-section-heading"><span>DOMAIN ATLAS</span><h2>Broad relationships, bounded claims.</h2></div>
        <div className="about-capability-grid">
          <article><h3>Water + living systems</h3><p>Water, habitat connectivity, fauna guilds, flora communities, and prairie concepts support regional comparison. Rare-species and protected occurrence coordinates are absent or denied.</p></article>
          <article><h3>Fire, smoke + hazards</h3><p>Year-specific synthetic fire and smoke envelopes sit beside coarse drought, wind, and flood concepts. None are current conditions, forecasts, warnings, perimeters, or life-safety guidance.</p></article>
          <article><h3>People + DNA governance</h3><p>The layer visualizes aggregate-only, consent-required, and denied policy postures. It contains no people, households, tribal affiliation, genealogy, kinship, genomic sequence, ancestry inference, or living-person data.</p></article>
          <article><h3>Rail, roads + settlements</h3><p>Distinct generalized road and rail styles connect clustered, labeled settlement points for exploration—not routing, schedules, operations, asset condition, boundaries, or population claims.</p></article>
        </div>
      </section>

      <section className="about-section">
        <div className="about-section-heading"><span>EVIDENCE STATES</span><h2>The interface says what a record can support—and when it cannot.</h2></div>
        <div className="about-state-table">{evidenceStates.map(([state, description]) => <article key={state}><strong>{state}</strong><p>{description}</p></article>)}</div>
      </section>

      <section className="about-section">
        <div className="about-section-heading"><span>TRUST BOUNDARY</span><h2>Useful spatial work without turning the renderer into an authority.</h2></div>
        <div className="about-boundary">
          <article><h3>What the Explorer can do</h3><ul><li>Display admitted site fixtures on MapLibre.</li><li>Filter and summarize visible, selected, or viewport-scoped records.</li><li>Preview supported local KML or GeoJSON geometry without upload or external fetch.</li><li>Carry citations, attribution, uncertainty, corrections, and limitations into reports.</li><li>Withhold a browser-location-derived camera from shares, receipts, exports, and diagnostics.</li></ul></article>
          <article><h3>What it does not claim</h3><ul><li>A map pixel, overlap, or proximity is not evidence.</li><li>A generated report or local-file preview cannot release, publish, admit, approve, or authorize data.</li><li>Screen measurements are not survey, cadastral, engineering, legal, or navigational results.</li><li>Protected geometry and unsupported claims are not reconstructed or inferred.</li></ul></article>
        </div>
      </section>

      <section className="about-section">
        <div className="about-section-heading"><span>PROJECT CONTEXT</span><h2>Repository evidence and site behavior remain distinguishable.</h2></div>
        <div className="about-boundary">
          <article><h3>Repository checkpoint</h3><ul><li>{REPOSITORY_SNAPSHOT.repository}</li><li>Inspected main@{REPOSITORY_SNAPSHOT.shortCommit}</li><li>{REPOSITORY_SNAPSHOT.inspectedAt}</li><li>Architecture, functions, feature maturity, and transition records are read-only context in this Site.</li></ul></article>
          <article><h3>Site-local runtime</h3><ul><li>MapLibre GL JS 6.6.0 with same-origin worker assets</li><li>OpenFreeMap / OpenMapTiles / OpenStreetMap vector context plus optional attributed raster basemaps; not evidence</li><li>Local GeoJSON demonstration sources</li><li>Optional AWS Terrain Tiles DEM display context; source elevation remains external and non-authoritative</li><li>Optional Qwen/Ollama bridge; no inference endpoint is configured by default</li><li>No release, deployment, promotion, or publication authority</li></ul></article>
        </div>
      </section>

      <section className="about-final-action"><div><h2>Ready to work with the map?</h2><p>Open the Explorer, frame your question spatially, and build a custom report from the data in view.</p></div><Link href="/">Open map + report builder</Link></section>
    </main>
  </div>;
}
