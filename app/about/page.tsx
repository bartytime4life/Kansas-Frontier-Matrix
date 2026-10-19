import Link from "next/link";
import identity from "../build-info.generated.json";
import { SITE_IDENTITY } from "../site-identity";

export const metadata = { title: "Explorer guide · KFM Public Staging" };
const repository = "https://github.com/bartytime4life/Kansas-Frontier-Matrix";
const references = [
  ["OpenFreeMap", "https://openfreemap.org/", "Vector basemap delivery; display context with attribution."],
  ["MapLibre GL JS", "https://maplibre.org/maplibre-gl-js/docs/", "Map renderer, terrain and globe documentation; no data admission authority."],
  ["USGS National Map", "https://www.usgs.gov/the-national-map-data-delivery/gis-data-download", "Official elevation and hydrography discovery; candidates require their own review."],
  ["Kansas Geological Survey", "https://www.kgs.ku.edu/", "Original Kansas geology and well-log discovery; no recorded-log package is approved here."],
] as const;

export default function Page() {
  return <div className="about-page">
    <a className="skip-link" href="#about-main">Skip to the guide</a>
    <nav className="about-nav" aria-label="Explorer guide navigation">
      <div className="brand-lockup"><span className="mark" aria-hidden="true">KFM</span><span><strong>Kansas Frontier Matrix</strong><small>Public Staging · restricted preview</small></span></div>
      <Link href="/">Open the map</Link><Link href="/topics">Explore by subject</Link>
    </nav>
    <main className="about-content" id="about-main" tabIndex={-1}>
      <header className="about-hero"><div><span>EXPLORER GUIDE</span><h1>Explore Kansas through place, time and evidence.</h1><p>Frame a Kansas place, check available layers, inspect their sources, then save an attributed draft. This restricted Site is a separate application from the GoDaddy Explorer.</p></div><aside><strong>Current data posture</strong><p>No observational or subsurface package is approved for this preview. Missing or held data stays unavailable. Map and terrain are display context.</p></aside></header>
      <nav className="about-section-links" aria-label="Guide sections"><a href="#workflow">Map workflow</a><a href="#capabilities">Features + limits</a><a href="#evidence">Evidence + exports</a><a href="#project">Code + build identity</a><a href="#sources">Official sources</a></nav>
      <section className="about-section" id="workflow">
        <div className="about-section-heading"><span>START HERE</span><h2>Follow one investigation from the map.</h2></div>
        <div className="about-workflow-grid">
          <article><span>01</span><h3>Choose a place</h3><p>Open Find &amp; ask to search, draft a question or check released evidence. Open the map navigation controls for Fit Kansas. Map controls → Appearance adjusts the display. The ? button reopens quick start.</p></article>
          <article><span>02</span><h3>Check availability</h3><p>Open Layers or Data. Review source role, observation dates, units, coverage and missingness. A catalogue listing is not an active release.</p></article>
          <article><span>03</span><h3>Inspect support</h3><p>Select an available feature or use Advanced tools → Inspect records for a keyboard alternative. The Evidence Drawer keeps support and limitations together.</p></article>
          <article><span>04</span><h3>Save a draft</h3><p>Use More → Reports or Stories. Include source attribution, dates and limits in permitted exports. Empty or withheld records remain unavailable.</p></article>
        </div>
      </section>
      <section className="about-section" id="capabilities">
        <div className="about-section-heading"><span>FEATURES + LIMITS</span><h2>Know what this preview can support.</h2></div>
        <div className="about-capability-grid">
          <article><h3>Map, terrain + globe</h3><p>2D is the starting view. Terrain and globe are optional display modes and depend on renderer and provider support. Display elevation is approximate.</p></article>
          <article><h3>Layers + source time</h3><p>Layers expose availability and holds. A selected atlas year does not change a source observation date or reconstruct unobserved history. Direct provider overlays stay disabled pending delivery approval.</p></article>
          <article><h3>Original records</h3><p>Underground tools require approved recorded intervals. Prepared private candidates and successful code tests do not authorize their delivery.</p></article>
          <article><h3>Qwen + account</h3><p><Link href="/?kfm-chat=1">Open Find / Ask / Evidence</Link> in this Site. The existing Qwen3 0.6B model stays on GoDaddy Node 22; inference requires a configured, authenticated service connection. Staging uses ChatGPT sign-in. Node accounts and passwords are not copied. Private locations and held records are not transferred. AI discussion cannot establish facts or release data.</p></article>
        </div>
      </section>
      <section className="about-section" id="evidence">
        <div className="about-section-heading"><span>EVIDENCE + EXPORTS</span><h2>Carry the source and its limits with the result.</h2></div>
        <div className="about-boundary"><article><h3>Inspect before using</h3><ul><li>Check title, provider, record time, units, coverage and source role.</li><li>Keep external context separate from admitted KFM evidence.</li><li>Unavailable, stale, corrected, withdrawn and denied states must remain visible.</li><li>Use source-linked references in <Link href="/almanacs">Almanacs</Link> and <Link href="/observatory/sources">Provider history</Link>; listings do not admit data.</li></ul></article><article><h3>Drafts and privacy</h3><ul><li>Reports and stories remain unpublished drafts; permitted exports are free.</li><li>Exports cannot approve, admit or publish data.</li><li>Protected details and browser-location-derived camera information remain withheld.</li><li>Missing evidence means abstention; no synthetic measurement fills the gap.</li></ul></article></div>
      </section>
      <section className="about-section" id="project">
        <div className="about-section-heading"><span>CODE + BUILD IDENTITY</span><h2>Identify this application separately from production.</h2></div>
        <div className="about-boundary"><article><h3>This Staging build</h3><ul><li>OpenAI Sites / Cloudflare Worker</li><li>Project: <code>{identity.application}</code></li><li><Link href="/api/build" prefetch={false}>Application build details</Link></li><li><a href={`${repository}/tree/codex/public-staging-qwen-workspace-20261019`}>Staging source branch (may advance)</a></li></ul><p className="about-build-note">Application input digest: <code>{identity.sourceDigest}</code>. Source commit: <code>{identity.sourceCommit ?? "unavailable for this build"}</code>. This identifies bounded source inputs. It does not attest to rendered behavior, live data, settings or release approval.</p></article><article><h3>Separate source histories</h3><ul><li><a href={`${repository}/blob/main/docs/runbooks/godaddy-node-hosting.md`}>GoDaddy hosting, verification + rollback guide</a></li><li><a href={`${repository}/blob/main/apps/site/README.md`}>Preserved private Explorer mirror</a></li><li><a href={`${repository}/blob/main/docs/doctrine/directory-rules.md`}>Directory governance</a></li><li><a href={`${repository}/blob/main/CONTRIBUTING.md`}>Contributing + validation</a></li></ul><p className="about-build-note">A GitHub merge, matching page title or successful build does not establish deployment. Staging updates do not publish the separate GoDaddy application.</p></article></div>
      </section>
      <section className="about-section" id="sources"><div className="about-section-heading"><span>OFFICIAL SOURCES</span><h2>Follow original providers and renderer documentation.</h2><p>These are discovery and implementation references. Listing them does not approve a dataset or establish provider availability.</p></div><div className="about-reference-list">{references.map(([title, href, note]) => <article key={href}><div><h3>{title}</h3><p>{note}</p></div><a href={href} target="_blank" rel="noreferrer" aria-label={`Open official source: ${title}`}>Open official source ↗</a></article>)}</div></section>
      <section className="about-final-action"><div><h2>Start with a Kansas place.</h2><p>Open the map and check available sources before drawing a conclusion.</p></div><Link href="/">Open Explorer</Link></section>
    </main>
  </div>;
}
