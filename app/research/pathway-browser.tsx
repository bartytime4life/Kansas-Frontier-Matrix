import Link from "next/link";
import { sourceMapHref } from "./discovery";
import { RESEARCH_PATHWAYS, pathwayComparisonHref } from "./pathways";
import styles from "./pathway-browser.module.css";

export function ResearchPathways() {
  return <section className={styles.section} id="research-pathways" aria-labelledby="research-pathways-title">
    <div className={styles.heading}>
      <div><p className={styles.eyebrow}>FOLLOW A QUESTION ACROSS KANSAS</p><h2 id="research-pathways-title">Explore Kansas, across disciplines.</h2></div>
      <p>Start with a subject, open its tools, and follow a useful connection. Each record keeps its own place, time and limits.</p>
    </div>

    <nav className={styles.subjects} aria-label="Research subjects">
      {RESEARCH_PATHWAYS.map(pathway => <a key={pathway.id} href={`#research-${pathway.id}`}>{pathway.title}</a>)}
    </nav>

    <div className={styles.grid}>
      {RESEARCH_PATHWAYS.map(pathway => <article className={styles.card} id={`research-${pathway.id}`} data-research-pathway={pathway.id} tabIndex={-1} aria-labelledby={`research-${pathway.id}-title`} key={pathway.id}>
        <h3 id={`research-${pathway.id}-title`}>{pathway.title}</h3>
        <p className={styles.question}>{pathway.question}</p>
        <p className={styles.summary}>{pathway.summary}</p>
        <p className={styles.scope}><strong>Scope</strong> {pathway.scope}</p>

        <ul className={styles.tools} aria-label={`${pathway.title} tools`}>
          {pathway.tools.map(tool => <li key={tool.href}>
            <Link href={tool.href} prefetch={false}><span className={styles.toolTitle}>{tool.label}<span aria-hidden="true">↗</span></span><span className={styles.toolScope}>{tool.scope}</span></Link>
          </li>)}
        </ul>

        <p className={styles.boundary}><strong>Keep in view</strong> {pathway.boundary}</p>
        <details className={styles.context}>
          <summary>Sources &amp; map context</summary>
          <p>Check the selected map sources’ providers, dates, representation and limitations before combining them.</p>
          <div className={styles.contextLinks}>
            <a href={pathwayComparisonHref(pathway)} aria-label={`Compare map sources for ${pathway.title}`}>Compare source details <span aria-hidden="true">↗</span></a>
            <a href={sourceMapHref(pathway.sourceIds)} aria-label={`Open map context for ${pathway.title}`}>Open map context <span aria-hidden="true">↗</span></a>
          </div>
          <p>These links select existing provider context. They do not start a data download or establish a reviewed analysis.</p>
        </details>

        <div className={styles.connections}>
          <p>Connect the question</p>
          <div>{pathway.connections.map(id => {
            const related = RESEARCH_PATHWAYS.find(candidate => candidate.id === id);
            return related ? <a key={id} href={`#research-${related.id}`}>{related.title} <span aria-hidden="true">→</span></a> : null;
          })}<Link className={styles.topicLink} href={pathway.topicHref} prefetch={false}>More in this subject <span aria-hidden="true">↗</span></Link></div>
        </div>
      </article>)}
    </div>

    <div className={styles.directoryLinks}><p>Ready to choose a specific tool or layer?</p><Link href="/science" prefetch={false}>Browse Science &amp; Labs <span aria-hidden="true">↗</span></Link><Link href="/topics" prefetch={false}>Browse all topics <span aria-hidden="true">↗</span></Link></div>
  </section>;
}

export default ResearchPathways;
