import type { Metadata } from "next";
import { PUBLIC_SITE_ORIGIN } from "../crawler-discovery";
import Link from "next/link";
import { REPOSITORY_SNAPSHOT } from "../repository-updates";
import { SITE_IDENTITY } from "../site-identity";
import buildIdentity from "../build-info.generated.json";

export const metadata: Metadata = {
  title: "About · Kansas Frontier Matrix Explorer",
  description: "Use the Kansas Frontier Matrix map, layers, time controls, free reports, assistant, and source documentation.",
  alternates: { canonical: `${PUBLIC_SITE_ORIGIN}/about` },
};

const evidenceStates = [
  ["ANSWER", "A released record needs a matching evidence reference for its bounded claim. No KFM domain records are currently released in this Site."],
  ["CORRECTED", "A correction remains attached to the current record and report output."],
  ["MISSING_EVIDENCE", "The Explorer shows the gap and declines to infer an answer."],
  ["SOURCE_STALE", "The source context is too old for a current claim without additional review."],
  ["GENERALIZED_GEOMETRY", "The location or shape is deliberately coarse and cannot support precise use."],
  ["SUPERSEDED", "The record remains available for history and lineage but is not current support."],
  ["RESTRICTED_ACCESS", "The interface cannot expose the protected material."],
  ["DENIED_BY_POLICY", "Policy blocks the requested detail and the Explorer fails closed."],
  ["ERROR", "A safe result could not be resolved; no fallback claim is generated."],
] as const;

const implementationTracks = [
  ["01", "Terrain foundation", "Keep the current key-free terrain carrier for display, then derive a version-pinned Kansas terrain package from USGS 3DEP with datum, resolution, lineage, checksum, and rollback metadata."],
  ["02", "Public data admission", "Admit one bounded source family at a time—transportation, hydrography, atmosphere, soils, land cover—through rights, sensitivity, temporal, quality, and EvidenceBundle gates."],
  ["03", "Temporal intelligence", "Bind each layer to actual observation, forecast, event, or edition timestamps. Playback advances only through available frames and makes gaps, model cycles, and mixed vintages visible."],
  ["04", "Analysis products", "Promote profiles, comparisons, measurements, and area summaries only when inputs, units, methods, uncertainty, and reproducible parameters can travel with the result."],
  ["05", "Performance + resilience", "Package large layers as range-friendly PMTiles, COG, or bounded vector/raster tiles; preserve a fast 2D fallback, lazy loading, cancellation, cache identity, and textual alternatives."],
  ["06", "Release proof", "Verify keyboard and screen-reader paths, reduced motion, WebGL2 degradation, mobile drawers, source outages, long sessions, visual regressions, export parity, correction handling, and rollback before promotion."],
] as const;

const referenceSources = [
  ["MapLibre GL JS — 3D terrain", "https://www.maplibre.org/maplibre-gl-js/docs/examples/3d-terrain/", "Renderer pattern for raster DEM terrain; implementation guidance, not data authority."],
  ["MapLibre GL JS — globe vector map", "https://www.maplibre.org/maplibre-gl-js/docs/examples/display-a-globe-with-a-vector-map/", "Projection and interaction reference for the optional globe context."],
  ["USGS — The National Map data delivery", "https://www.usgs.gov/the-national-map-data-delivery/gis-data-download", "Authoritative discovery path for elevation, hydrography, boundaries, transportation, structures, imagery, and web services."],
  ["USGS — 3DEP 1 m DEM catalog", "https://data.usgs.gov/datacatalog/data/USGS%3A77ae0551-c61e-4979-aedd-d797abdcde0e", "High-resolution elevation candidate; coverage and product identity must be resolved before admission."],
  ["KDOT — Kansas maps and GIS resources", "https://www.ksdot.gov/about/our-organization/divisions/planning-and-development/kansas-maps-and-gis-resources", "Official transportation maps, GIS applications, functional classes, traffic counts, and historical map discovery."],
  ["KDOT — LiDAR project data portal", "https://www.ksdot.gov/about/our-organization/divisions/planning-and-development/kdot-lidar-project-data-portal", "2021 and 2023 mobile-LiDAR project extracts, dictionaries, maps, and layer-specific discovery."],
  ["AirNow — AQI basics", "https://www.airnow.gov/aqi/aqi-basics", "Official AQI meaning and category semantics; monitor concentration, AQI, and reporting areas must remain distinct."],
] as const;

export default function AboutPage() {
  const repositoryUrl = "https://github.com/bartytime4life/Kansas-Frontier-Matrix";
  const sourceUrl = buildIdentity.sourceCommit ? `${repositoryUrl}/tree/${buildIdentity.sourceCommit}` : repositoryUrl;
  return <div className="about-page">
    <a className="skip-link" href="#about-main">Skip to the guide</a>
    <nav className="about-nav" aria-label="About page navigation">
      <div className="brand-lockup">
        <span className="mark" aria-hidden="true">KFM</span>
        <span><strong>Kansas Frontier Matrix</strong><small>Explorer guide + boundaries</small></span>
      </div>
      <Link href="/">Open the map</Link>
      <Link href="/privacy">Privacy + contact</Link>
    </nav>

    <main className="about-content" id="about-main" tabIndex={-1}>
      <header className="about-hero">
        <div><span>ABOUT THE EXPLORER</span><h1>A map-first Living Atlas for seeing Kansas in context.</h1><p>The Explorer opens on a real MapLibre Kansas vector map with time, layers, and place context. Start with a view, inspect its sources, and carry their dates and limitations into free report exports.</p></div>
        <aside><strong>Current data posture</strong><p>The map presents attributed provider-backed layers such as Census counties, USGS water sources, and NOAA context. These sources have separate clocks and availability. No KFM domain layer has been admitted for this Site.</p></aside>
      </header>

      <nav className="about-section-links" aria-label="Guide sections"><a href="#workflow">Map workflow</a><a href="#capabilities">Features + limits</a><a href="#project">Code + documentation</a><a href="#sources">Official sources</a></nav>

      <section className="about-section" id="workflow">
        <div className="about-section-heading"><span>PRIMARY WORKFLOW</span><h2>Start with a question, finish with a report.</h2></div>
        <div className="about-workflow-grid">
          <article><span>01</span><h3>Frame the map</h3><p>Search a place or feature, move the camera, choose a time, and show only the layers relevant to the question.</p></article>
          <article><span>02</span><h3>Inspect records</h3><p>Select map features or use the searchable feature index. Evidence state, source role, freshness, release posture, and limitations remain attached.</p></article>
          <article><span>03</span><h3>Set report scope</h3><p>Report on the moving viewport, a locked area of interest, all visible layers, or one selected feature. Choose included layers, detail level, and report sections.</p></article>
          <article><span>04</span><h3>Use the result</h3><p>Copy a structured report, download a printable HTML report, or download JSON for another analysis workflow.</p></article>
        </div>
      </section>

      <section className="about-section" id="capabilities">
        <div className="about-section-heading"><span>MAP CAPABILITIES</span><h2>The main interface is built for action, not presentation.</h2></div>
        <div className="about-capability-grid">
          <article><h3>Real map + context</h3><p>The default view is an attributed Kansas vector basemap with counties, places, roads, rail, water, and labels. Satellite imagery, terrain, and provider-backed source layers are optional display context. No synthetic KFM domain overlays are offered.</p></article>
          <article><h3>Views + layers + time</h3><p>Start from a named source-backed view, then control source visibility, opacity, order, provider time, and basemap treatment.</p></article>
          <article><h3>Search + inspect</h3><p>Search source layers and places, then inspect mapped features with their provider and time information.</p></article>
          <article><h3>Chat with KFM</h3><p>Open Chat with KFM from the map. Availability depends on the hosted service status; responses can be incomplete or withheld. Chat is interpretive and cannot establish source facts or release data. Invited PC-assisted workflows retain their separate sign-in and connection requirements.</p></article>
          <article><h3>Spatial analysis + motion</h3><p>Shift-drag a report area, move through camera history, and inspect provider-backed water, smoke, and terrain context. Map presentation does not establish evidence.</p></article>
          <article><h3>Places, stories + reports</h3><p>Save map states as device-local investigation stops and produce reports that retain attribution and limitations.</p></article>
        </div>
      </section>

      <section className="about-section">
        <div className="about-section-heading"><span>REAL SOURCE CONTEXT</span><h2>Inspect mapped sources on their own terms.</h2></div>
        <div className="about-capability-grid">
          <article><h3>Water + living systems</h3><p>USGS stream gauges, mapped hydrography, and watershed boundaries offer separate views of water. A gauge reading does not establish flow throughout a mapped river.</p></article>
          <article><h3>Fire, smoke + hazards</h3><p>NOAA smoke analyses and radar images carry provider times and coverage limits. They do not establish surface exposure or a fire perimeter.</p></article>
          <article><h3>People + DNA governance</h3><p>Census county counts provide an edition-specific population and housing baseline. Individual and protected records are not mapped.</p></article>
          <article><h3>Rail, roads + settlements</h3><p>Roads, railways, and places in the vector basemap provide orientation. Their display does not verify routing, schedules, operations, or asset condition.</p></article>
        </div>
      </section>

      <section className="about-section">
        <div className="about-section-heading"><span>EVIDENCE STATES</span><h2>The interface says what a record can support—and when it cannot.</h2></div>
        <div className="about-state-table">{evidenceStates.map(([state, description]) => <article key={state}><strong>{state}</strong><p>{description}</p></article>)}</div>
      </section>

      <section className="about-section">
        <div className="about-section-heading"><span>TRUST BOUNDARY</span><h2>Useful spatial work without turning the renderer into an authority.</h2></div>
        <div className="about-boundary">
          <article><h3>What the Explorer can do</h3><ul><li>Display attributed provider-backed map context on MapLibre.</li><li>Inspect visible source features and their stated limits.</li><li>Preview supported local KML or GeoJSON geometry without upload or external fetch.</li><li>Carry citations, attribution, uncertainty, corrections, and limitations into reports.</li><li>Withhold a browser-location-derived camera from shares, receipts, exports, and diagnostics.</li></ul></article>
          <article><h3>What it does not claim</h3><ul><li>A map pixel, overlap, or proximity is not evidence.</li><li>A generated report or local-file preview cannot release, publish, admit, approve, or authorize data.</li><li>Screen measurements are not survey, cadastral, engineering, legal, or navigational results.</li><li>Protected geometry and unsupported claims are not reconstructed or inferred.</li></ul></article>
        </div>
      </section>

      <section className="about-section" id="project">
        <div className="about-section-heading"><span>PROJECT CONTEXT</span><h2>Repository evidence and site behavior remain distinguishable.</h2></div>
        <p>This public GoDaddy Node.js application is available at <a href={PUBLIC_SITE_ORIGIN}>{PUBLIC_SITE_ORIGIN}</a>. Its standalone source history and the repository&apos;s preserved Sites mirror are maintained separately. For project or correction questions, email <a href="mailto:Andy.barta.pro@gmail.com">Andy.barta.pro@gmail.com</a>.</p>
        <div className="about-boundary">
          <article><h3>Code + documentation</h3><ul><li><a href={sourceUrl}>{buildIdentity.sourceCommit ? "Source at this build commit" : "Project repository (deployment commit unavailable)"}</a></li><li><a href={`${repositoryUrl}/blob/main/docs/runbooks/godaddy-hosting.md`}>Hosting, verification + rollback guide</a></li><li><a href={`${repositoryUrl}/blob/main/docs/doctrine/directory-rules.md`}>Directory governance</a></li><li><a href={`${repositoryUrl}/blob/main/CONTRIBUTING.md`}>Contributing + validation</a></li><li><a href="/api/build">Application build details</a></li></ul><p className="about-build-note">Application input digest: <code>{buildIdentity.sourceDigest}</code>. This identifies source inputs; live data, settings, rendered acceptance, and release checks remain separate.</p></article>
          <article><h3>Hosted runtime + access</h3><ul><li>Node.js 22 with MapLibre GL JS 6.9.0 and same-origin worker assets</li><li>Public map, attributed provider context, and free report exports</li><li>Source downloads retain provider times, attribution, and coverage limits</li><li>Private acquisition, account, and review operations retain their authorization checks</li><li>Terrain and basemaps are display context; they do not establish source evidence</li></ul></article>
        </div>
        <details className="about-history"><summary>Historical repository and Sites snapshots</summary><p>{REPOSITORY_SNAPSHOT.repository} was inspected at main@{REPOSITORY_SNAPSHOT.shortCommit} on {REPOSITORY_SNAPSHOT.inspectedAt}. This dated snapshot is not the deployed application version.</p><p>Preserved Sites identity: {SITE_IDENTITY.provider} · {SITE_IDENTITY.slug}. Historical host: {SITE_IDENTITY.canonicalUrl}. Its recorded domain check ({SITE_IDENTITY.checkedAt}) and manifest state are historical context, not current public routing or availability.</p></details>
      </section>

      <section className="about-section" id="implementation">
        <div className="about-section-heading"><span>IMPLEMENTATION PROGRAM</span><h2>Advance the source-backed map to a governed operational atlas.</h2><p>This sequence preserves the working map while converting candidate sources into reproducible, public-safe products. A track may be prototyped early, but it cannot be promoted ahead of its evidence and release gates.</p></div>
        <div className="about-implementation-grid">
          {implementationTracks.map(([number, title, description]) => <article key={number}><span>{number}</span><div><h3>{title}</h3><p>{description}</p></div></article>)}
        </div>
      </section>

      <section className="about-section" id="sources">
        <div className="about-section-heading"><span>RESEARCH + REFERENCES</span><h2>Primary sources that shape the next implementation slices.</h2><p>These references identify authoritative datasets or renderer capabilities. Listing a source does not admit it into KFM; rights, version, coverage, transformation, sensitivity, quality, and EvidenceBundle closure remain mandatory.</p></div>
        <div className="about-reference-list">
          {referenceSources.map(([title, href, note]) => <article key={href}><div><h3>{title}</h3><p>{note}</p></div><a href={href} target="_blank" rel="noreferrer" aria-label={`Open official source: ${title}`}>Open official source <span aria-hidden="true">↗</span></a></article>)}
        </div>
      </section>

      <section className="about-final-action"><div><h2>Ready to work with the map?</h2><p>Open the Explorer, frame your question spatially, and build a custom report from the data in view.</p></div><Link href="/">Open map + report builder</Link></section>
    </main>
  </div>;
}
