import Link from 'next/link';
import stops from './stops.json';
import styles from './fort-larned.module.css';

const brochure = 'https://www.nps.gov/fols/planyourvisit/audio-described-brochure.htm';

export const metadata = {
  title: 'Fort Larned’s parade ground | Kansas Frontier Matrix',
  description: 'Explore three buildings at Fort Larned through July 1965 survey photographs and National Park Service records.',
};

export default function FortLarnedPage() {
  return <main className={styles.page}>
    <div className={styles.frame}>
      <nav className={styles.breadcrumb} aria-label="Research navigation">
        <Link href="/labs">Research Labs</Link><span aria-hidden="true">/</span><span>Historic Places</span>
      </nav>
      <header className={styles.header}>
        <p className={styles.kicker}>Fort Larned · Pawnee County</p>
        <h1>Life around the parade ground</h1>
        <p>Follow three buildings at a Santa Fe Trail post. July 1965 survey photographs show what survived and how some of the buildings changed after the Army left.</p>
      </header>
      <div className={styles.layout}>
        <aside className={styles.sidebar}>
          <nav aria-labelledby="plan-title">
            <h2 id="plan-title" tabIndex={-1}>Choose a building</h2>
            <div className={styles.plan}>
              <span className={styles.compass} aria-hidden="true">N ↑</span>
              <span className={styles.field}>Parade ground</span>
              {stops.map(stop => <a key={stop.id} className={styles[stop.id]} href={`#${stop.id}`}>
                <span>{stop.side}</span><strong>{stop.mapLabel}</strong>
              </a>)}
            </div>
          </nav>
          <p className={styles.mapNote}>Three selected buildings shown in a simplified plan. <a href={brochure}>Read the full NPS site description</a>.</p>
          <Link className={styles.mapLink} href="/explore/frontier-trails">Explore the Santa Fe Trail map <span aria-hidden="true">→</span></Link>
        </aside>
        <div className={styles.stops}>
          {stops.map((stop, index) => <article className={styles.stop} id={stop.id} tabIndex={-1} key={stop.id} aria-labelledby={`${stop.id}-title`}>
            <p className={styles.kicker}>{stop.side} side</p>
            <h2 id={`${stop.id}-title`}>{stop.title}</h2>
            <figure>
              {/* Bundle the exact provider JPEG and keep the archive download alongside it. */}
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img src={`/labs/fort-larned/${stop.id}.jpg`} alt={stop.alt} width={stop.width} height={stop.height} loading={index === 0 ? 'eager' : 'lazy'}/>
              <figcaption>{stop.caption} David von Riesen, July 1965 · {stop.survey}, Library of Congress.</figcaption>
            </figure>
            <p>{stop.story}</p>
            <div className={styles.sourceLinks}>
              <a href={stop.photo}>Photo record</a><a href={stop.original}>Original JPEG</a><a href={stop.interpretation}>NPS building history</a><a href="#plan-title">Back to the plan <span aria-hidden="true">↑</span></a>
            </div>
          </article>)}
        </div>
      </div>
      <section className={styles.context} aria-labelledby="context-title">
        <h2 id="context-title">Fort Larned and the Santa Fe Trail</h2>
        <p>The Army used the fort to guard mail and trade on the Santa Fe Trail. Company A of the 10th U.S. Cavalry, one of the Buffalo Soldier units, arrived in 1867. Federal Indian agencies also used the fort to distribute treaty goods to Plains nations.</p>
        <div className={styles.sourceLinks}>
          <a href="https://www.nps.gov/fols/learn/historyculture/buffalo-soldiers.htm">Buffalo Soldiers at Fort Larned</a>
          <a href={brochure}>NPS history and accessibility guide</a>
          <a href="https://npgallery.nps.gov/AssetDetail/NRIS/66000107">National Register record</a>
          <a href="https://wwws.loc.gov/rr/print/res/114_habs.html">Survey image rights</a>
        </div>
      </section>
    </div>
  </main>;
}
