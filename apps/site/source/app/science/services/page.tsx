import Link from "next/link";
import ScienceNav from "../science-nav";
import InquiryBuilder, { ServiceScopeLink } from "./inquiry-builder";
import styles from "./services.module.css";

export const metadata = {
  title: "Custom science projects | Kansas Frontier Matrix",
  description: "Discuss a scoped evidence brief, reusable data preparation or a guided team walkthrough. Explore the free worked example and prepare an inquiry on your device.",
  alternates: { canonical: "https://kansasfrontiermatrix.com/science/services" },
};

const offers = [
  { id: "brief", number: "01", title: "Custom evidence brief", audience: "For local organizations, researchers and communicators with a focused Kansas question.", items: ["A clearly scoped question and source-linked figures", "Coverage, uncertainty and interpretation notes", "A reproducible data appendix for the agreed scope"] },
  { id: "data", number: "02", title: "Reusable data pack", audience: "For teams that need a documented starting table they can inspect and work with again.", items: ["A bounded table with consistent fields and units", "Source lineage, quality flags and missing values", "Documented preparation steps and reuse limits"] },
  { id: "walkthrough", number: "03", title: "Guided team walkthrough", audience: "For a team that wants to ask better questions and make confident use of the public tools.", items: ["A session shaped around your question", "A guided reading of charts, coverage and sources", "A short reading guide and practical next steps"] },
];

export default function ScienceServicesPage() {
  return <main className={styles.page}><div className={styles.frame}>
    <ScienceNav active="services" />
    <header className={styles.hero}><div><span className={styles.eyebrow}>Kansas Frontier Matrix / Optional custom work</span><h1>A good question.<br /><em>A useful deliverable.</em></h1><p>Need help turning public science data into something your team can use? Start a conversation about a focused brief, a reusable data pack or a guided walkthrough.</p><div className={styles.heroActions}><a className={styles.primaryLink} href="#project-brief">Build a project brief <span aria-hidden="true">↓</span></a><Link href="/science">Explore the free tools ↗</Link></div></div><aside className={styles.example}><span className={styles.eyebrow}>See the approach / free worked example</span><h2>Two Topeka years.<br />Four source perspectives.</h2><p>Explore a real comparison report before discussing a custom project.</p><ul><li>Precipitation <span>NOAA station</span></li><li>Drought <span>County assessments</span></li><li>Air quality <span>Reported county AQI</span></li><li>Sunlight <span>NASA model</span></li></ul><Link href="/science/compare">Open the free comparison report ↗</Link></aside></header>
    <aside className={styles.freeNote}><strong>The public tools stay free.</strong><p>Science labs, the worked report and self-service downloads remain free. Custom work starts with an inquiry; there is no purchase or payment on this page.</p></aside>
    <section className={styles.services} aria-labelledby="custom-work-heading"><div className={styles.sectionHeading}><div><span className={styles.eyebrow}>Three ways to work together</span><h2 id="custom-work-heading">Choose the help you need.</h2></div><p>These are starting scopes. Feasibility, data coverage, deliverables, pricing and availability are discussed and agreed by email.</p></div>{offers.map(offer => <article className={styles.service} key={offer.id}><span className={styles.serviceIndex} aria-hidden="true">{offer.number}</span><div><h3>{offer.title}</h3><p>{offer.audience}</p><ServiceScopeLink service={offer.id}>Discuss this scope ↗</ServiceScopeLink></div><div><ul>{offer.items.map(item => <li key={item}>{item}</li>)}</ul></div></article>)}<p className={styles.scopeNote}>A custom project does not confer scientific certification, provider endorsement or KFM dataset admission. Source rights, coverage and uncertainty determine what a project can support.</p></section>
    <section className={styles.process} aria-label="How a custom project begins"><div><strong><span>01</span>Frame the question</strong><p>Describe the audience, intended use and general area. A link from a lab can carry your public analysis selection.</p></div><div><strong><span>02</span>Agree the scope</strong><p>Discuss what the sources support, the deliverables, a quote and availability before work begins.</p></div><div><strong><span>03</span>Keep the evidence</strong><p>The agreed work carries source links, methods and limitations, so the result remains understandable.</p></div></section>
    <section id="project-brief" className={styles.builder} aria-labelledby="project-brief-heading" tabIndex={-1}><div className={styles.builderIntro}><span className={styles.eyebrow}>Start a conversation / no account needed</span><h2 id="project-brief-heading">Make the question concrete.</h2><p>Prepare a short inquiry here, then choose how to keep or send it. You can edit the final message in your own email app.</p></div><InquiryBuilder /></section>
    <footer className={styles.footer}><span>Kansas Frontier Matrix · Source-linked work, clearly scoped</span><Link href="/science">Back to the science tools ↗</Link><Link href="/privacy">Privacy &amp; contact ↗</Link></footer>
  </div></main>;
}
