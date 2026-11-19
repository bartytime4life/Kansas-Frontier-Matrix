'use client';

import Link from 'next/link';
import { useEffect, useRef, useState } from 'react';
import styles from './then-now.module.css';

const viewDescriptions = {
  2021: 'A road and bridge form a continuous crossing of the Arkansas River beside the ballfields.',
  2024: 'The crossing is interrupted where the road meets the river. The ballfields remain visible north of the work area.',
};

function EditionImage({ edition, footprint, setUnavailable, alt = '' }) {
  const image = useRef(null);
  useEffect(() => {
    // A request can fail before the page hydrates and attaches its error handler.
    if (image.current?.complete && !image.current.naturalWidth) setUnavailable(true);
  }, [edition.preview, setUnavailable]);
  // These fixed-size, already encoded local assets need no runtime image service.
  // eslint-disable-next-line @next/next/no-img-element
  return <img ref={image} src={edition.preview} width={footprint.width} height={footprint.height} alt={alt} draggable={false} onError={() => setUnavailable(true)}/>;
}

export default function ThenNow({ pair }) {
  const [older, newer] = pair.editions;
  const [mode, setMode] = useState('swipe');
  const [split, setSplit] = useState(50);
  const [unavailable, setUnavailable] = useState(false);

  return <main className={styles.page}>
    <div className={styles.frame}>
      <nav className={styles.breadcrumb} aria-label="Research navigation"><Link href="/labs">Research Labs</Link><span aria-hidden="true">/</span><span>Kansas Then &amp; Now</span></nav>
      <header className={styles.header}>
        <p>Kansas Then &amp; Now · Finney County</p>
        <h1>The Arkansas River crossing at Garden City</h1>
        <p>Compare the same stretch of river in two aerial imagery editions. Use the ballfields as a landmark and look south to see what changed at the crossing.</p>
      </header>

      <div className={styles.layout}>
        <section className={styles.viewer} aria-labelledby="imagery-title">
          <div className={styles.viewerHeading}>
            <h2 id="imagery-title">Compare the aerial views</h2>
            <div className={styles.modes} role="group" aria-label="Comparison layout">
              <button type="button" aria-pressed={mode === 'swipe'} onClick={() => setMode('swipe')}>Swipe</button>
              <button type="button" aria-pressed={mode === 'side-by-side'} onClick={() => setMode('side-by-side')}>Side by side</button>
            </div>
          </div>
          {unavailable ? <p className={styles.unavailable} role="status">An image preview could not load. The descriptions and source links remain available.</p>
            : mode === 'swipe' ? <>
              <div className={styles.editionRow}><span>{older.year} edition</span><span>{newer.year} edition</span></div>
              <div className={styles.stage} style={{ '--split': `${split}%` }}>
                <div className={styles.newer} aria-hidden="true"><EditionImage edition={newer} footprint={pair.footprint} setUnavailable={setUnavailable}/></div>
                <div className={styles.older} aria-hidden="true"><EditionImage edition={older} footprint={pair.footprint} setUnavailable={setUnavailable}/></div>
                <div className={styles.divider} aria-hidden="true"><span>‹ ›</span></div>
                <input className={styles.range} type="range" min="0" max="100" step="1" value={split} aria-label="Compare imagery editions" aria-valuetext={`${older.year} covers ${split} percent. ${newer.year} covers ${100 - split} percent.`} aria-describedby="divider-help" onChange={event => setSplit(Number(event.target.value))}/>
              </div>
              <p className={styles.help} id="divider-help">Drag the divider or use the arrow keys. Home shows {newer.year} and End shows {older.year}.</p>
            </> : <div className={styles.duo}>{pair.editions.map(edition => <figure key={edition.year}>
              <EditionImage edition={edition} footprint={pair.footprint} setUnavailable={setUnavailable} alt={viewDescriptions[edition.year]}/>
              <figcaption>{edition.year} edition</figcaption>
            </figure>)}</div>}
        </section>

        <aside className={styles.context} aria-labelledby="crossing-title">
          <h2 id="crossing-title">What changed at the crossing?</h2>
          <dl>{pair.editions.map(edition => <div key={edition.year}><dt>{edition.year} edition</dt><dd>{viewDescriptions[edition.year]}</dd></div>)}</dl>
          <p>KDOT’s annual report says the U.S. 83 Business bridge replacement was completed at the end of 2024.</p>
          <a href={pair.project}>Read the KDOT project record <span aria-hidden="true">↗</span></a>
        </aside>
      </div>

      <section className={styles.sources} aria-labelledby="source-title">
        <h2 id="source-title">Imagery sources and dates</h2>
        <p>The date labels identify statewide editions. Exact flight dates at the crossing remain unconfirmed. Image color and shadows can vary with acquisition and processing.</p>
        <div className={styles.sourceList}>{pair.editions.map(edition => <article key={edition.year}>
          <h3>{edition.year} natural color</h3>
          <p>{edition.window}</p>
          <a href={edition.catalog}>Catalog and reuse terms</a><a href={edition.export}>Open source PNG</a>
        </article>)}</div>
        <p className={styles.credit}>{pair.source} · {pair.license}. Both previews use the same {pair.footprint.width} × {pair.footprint.height} pixel footprint. Each WebP is a compressed view of its source export.</p>
      </section>
    </div>
  </main>;
}
