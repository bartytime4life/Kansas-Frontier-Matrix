'use client';

import { useState } from 'react';
import Link from 'next/link';
import { NOTEBOOK_STARTERS, createStarterNotebook, starterInvestigationLink } from './starter-investigations.mjs';
import styles from './StarterInvestigations.module.css';

export default function StarterInvestigations() {
  const [status, setStatus] = useState('');
  const download = () => {
    try {
      const url = URL.createObjectURL(new Blob([createStarterNotebook()], { type: 'application/json' }));
      const link = document.createElement('a'); link.href = url; link.download = 'kfm-starter-investigations.json'; link.click();
      setTimeout(() => URL.revokeObjectURL(url), 1000);
      setStatus('Starter notebook downloaded. It contains three public investigations and editable reasoning prompts. Import it below to add a copy to this browser.');
    } catch (error) { setStatus(error.message || 'The starter notebook could not be downloaded. You can still open the investigations below.'); }
  };
  return <section className={styles.shelf} aria-labelledby="starter-investigations-title">
    <div className={styles.heading}><div><span>THREE WAYS INTO THE RECORD</span><h2 id="starter-investigations-title">A useful question to start with.</h2></div><div><button type="button" onClick={download}>Download starter notebook JSON ↓</button><p>Opens public controls. Nothing is added to your saved notebook automatically.</p></div></div>
    <ol className={styles.starters}>{NOTEBOOK_STARTERS.map((starter, index) => <li key={starter.id}><span className={styles.index}>{String(index + 1).padStart(2, '0')}</span><div className={styles.question}><span>{starter.workspace === 'county' ? 'COUNTY OBSERVATORY' : 'SIGNAL STUDIO'} / {starter.title}</span><h3>{starter.question}</h3></div><dl><div><dt>Source coverage</dt><dd>{starter.coverage}</dd></div><div><dt>How to explore</dt><dd>{starter.method}</dd></div></dl><Link prefetch={false} href={starterInvestigationLink(starter.id)}>Open investigation <span aria-hidden="true">↗</span></Link></li>)}</ol>
    {status && <p className={styles.status} role="status">{status}</p>}
  </section>;
}
