import type { Metadata } from "next";
import { ALMANAC_RESOURCES } from "../almanac-resources";
import Link from "next/link";
import { IS_PUBLIC_COPY } from "../public-profile";
import { publicRouteDecision } from "../public-route-policy";
import { TOPIC_GROUPS, TOPIC_STRUCTURE, SPECIALTY_LAYER_CATALOG, officialSourceTopics, specialtyLayerTopics, imageryTopics, featureTopics } from "../layer-workspaces";
import { OFFICIAL_CONTEXT_SOURCES } from "../live-context";
import { EARTH_ENGINE_CONTEXT_LAYERS } from "../earth-engine-context";
import { FEATURE_CATALOG, featureMaturityLabel } from "../feature-catalog";
import styles from "./topics.module.css";

export const metadata: Metadata = {
  title: "Topics · Kansas Frontier Matrix",
  description: "Explore Kansas layers, research and feature families by subject, with source coverage and limitations.",
};

export default function TopicsPage() {
  return <main className={styles.page}>
    <header className={styles.header}><Link href="/">← Kansas map</Link><Link href="/about">Explorer guide</Link></header>
    <div className={styles.intro}><p>KANSAS FRONTIER MATRIX</p><h1>Explore by subject</h1>
      <p>Start with engineering, science, weather, history, land or people, then follow related layers and tools. A layer can belong to several subjects while keeping one source identity.</p>
      <p className={styles.boundary}>Coverage below describes configured source context and catalogue entries. Connections, reviewed imagery installation and released evidence are checked in their own views.</p>
    </div>
    <nav className={styles.groups} aria-label="Topic groups">{TOPIC_GROUPS.map((group, index) => <a key={group} href={`#topic-group-${index}`}>{group}</a>)}</nav>
    {TOPIC_GROUPS.map((group, index) => <section key={group} id={`topic-group-${index}`} className={styles.section} aria-labelledby={`topic-heading-${index}`}>
      <h2 id={`topic-heading-${index}`}>{group}</h2><div className={styles.grid}>
        {TOPIC_STRUCTURE.filter(topic => topic.group === group).map(topic => {
          const sources = OFFICIAL_CONTEXT_SOURCES.filter(source => officialSourceTopics(source.id).includes(topic.id));
          const imagery = EARTH_ENGINE_CONTEXT_LAYERS.filter(layer => imageryTopics(layer.id).includes(topic.id));
          const controls = SPECIALTY_LAYER_CATALOG.filter(layer => specialtyLayerTopics(layer.id).includes(topic.id));
          const features = FEATURE_CATALOG.filter(feature => featureTopics(feature.id).includes(topic.id));
          const almanacs = ALMANAC_RESOURCES.filter(resource => resource.topics.includes(topic.id));
          return <article key={topic.id} id={topic.id} className={styles.card}>
            <h3>{topic.title}</h3><p>{topic.description}</p>
            <ul className={styles.facets} aria-label={`${topic.title} subtopics`}>{topic.facets.map(facet => <li key={facet}>{facet}</li>)}</ul>
            <p className={styles.limits}>{topic.limitation}</p>
            <div className={styles.actions}><Link href={`/?topic=${topic.id}`} prefetch={false}>Browse map layers →</Link>{topic.resources.filter(resource => !IS_PUBLIC_COPY || publicRouteDecision(resource.href).allowed).map(resource => <Link key={resource.href} href={resource.href} prefetch={false}>{resource.title} ↗</Link>)}</div>
            <details><summary>Source context · {sources.length}</summary>{sources.length ? <ul>{sources.map(source => <li key={source.id}><a href={source.sourceUrl} target="_blank" rel="noreferrer">{source.title} ↗</a><small>{source.organization} · {source.evidenceRole.replaceAll("_", " ")}</small></li>)}</ul> : <p>No provider map layer is assigned here. Use the related tools or research links; no new dataset is implied.</p>}</details>
            {controls.length > 0 && <details><summary>Specialist layer controls · {controls.length}</summary><p>Selection, source connection, method and release eligibility are shown on each control in Map layers.</p><ul>{controls.map(layer => <li key={layer.id}>{layer.title}</li>)}</ul></details>}
            <details><summary>Imagery catalogue · {imagery.length}</summary>{imagery.length ? <><p>These are catalogue entries. Installed packages, years and display eligibility are checked in Map layers → Imagery.</p><ul>{imagery.map(layer => <li key={layer.id}>{layer.title}<small>{layer.source}</small></li>)}</ul><Link href={`/?topic=${topic.id}&layerView=imagery`} prefetch={false}>Browse related imagery →</Link></> : <p>No imagery entry is assigned here.</p>}</details>
            {almanacs.length > 0 && <details><summary>Almanac references · {almanacs.length}</summary><p>Publisher outlooks, gardening and astronomy references retain access and reuse limits. These are separate from map layers and released evidence.</p><ul>{almanacs.map(resource => <li key={resource.id}><Link href={`/almanacs?topic=${topic.id}#almanac-${resource.id}`} prefetch={false}>{resource.title} →</Link></li>)}</ul></details>}
            <details><summary>Repository feature families · {features.length}</summary><p>Repository maturity labels describe the pinned catalogue; they are not claims of live Site capability.</p>{features.length ? <ul>{features.map(feature => <li key={feature.id}>{feature.name}<small>{featureMaturityLabel(feature.maturity)} · {feature.area}</small></li>)}</ul> : <p>No subject-specific repository feature family is assigned here.</p>}</details>
          </article>;
        })}
      </div>
    </section>)}
  </main>;
}
