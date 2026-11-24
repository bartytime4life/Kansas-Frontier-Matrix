'use client';
import { useState } from 'react';
import { KANSAS_LIDAR_SOURCE_CATALOG, LIDAR_CATALOG_CHECKED_AT, LIDAR_COMPARISON_REQUIREMENTS } from './lidar-source-catalog';
import styles from './lidar-source-panel.module.css';
const READY = { 'continuous-terrain': 'Continuous ground display', 'sampled-science': 'Prepared sample science', discovery: 'Discovery only', 'access-unverified': 'Access unverified' } as const;
const ACCESS = { 'public-no-key': 'Public · no key', 'free-account': 'Free provider account', unverified: 'Access not qualified' } as const;
export function LidarSourcePanel({ anchorId, onOpenContinuous }: { anchorId?: string; onOpenContinuous?: () => void }) {
  const [filter, setFilter] = useState('all');
  const connectedGround = KANSAS_LIDAR_SOURCE_CATALOG.filter(row => row.readiness === 'continuous-terrain').length, connectedSamples = KANSAS_LIDAR_SOURCE_CATALOG.filter(row => row.readiness === 'sampled-science').length;
  const shown = KANSAS_LIDAR_SOURCE_CATALOG.filter(row => filter === 'all' || (filter === 'ready' ? ['continuous-terrain', 'sampled-science'].includes(row.readiness) : row.readiness === filter));
  return <details className={styles.panel} id={anchorId}>
    <summary>Kansas LiDAR sources <span>Coverage, access &amp; readiness</span></summary>
    <p>{connectedGround} continuous ground display and {connectedSamples} prepared historical sample family connected. Other provider families below are discovery paths; a catalog entry does not install files or create statewide 1 m LiDAR coverage.</p>
    <label>Show source families<select value={filter} onChange={event => setFilter(event.target.value)}><option value="all">All families</option><option value="ready">Connected KFM views</option><option value="discovery">Discovery only</option><option value="access-unverified">Access unverified</option></select></label>
    <p role="status">{shown.length} of {KANSAS_LIDAR_SOURCE_CATALOG.length} source families · catalog checked {LIDAR_CATALOG_CHECKED_AT.replace('T', ' ').replace('Z', ' UTC')}</p>
    <ul className={styles.sources}>{shown.map(row => <li key={row.id} data-readiness={row.readiness}><div className={styles.heading}><strong>{row.title}</strong><span>{READY[row.readiness]}</span></div><p>{row.coverage}</p><small>{row.organization} · Provider access: {ACCESS[row.access]} · {row.geometry === 'orbital-profiles' ? 'Sparse orbital profiles / footprints' : row.geometry === 'survey-index' ? 'Survey index' : row.geometry === 'derived-assets' ? 'Derived assets' : 'Grids / point-cloud source family'}</small><div className={styles.actions}>{row.id === 'usgs-3dep' && onOpenContinuous && <button type="button" onClick={onOpenContinuous}>Open Kansas terrain →</button>}{row.actionUrl && <a href={row.actionUrl}>Open prepared Science view →</a>}<a href={row.sourceUrl} target="_blank" rel="noreferrer">Provider &amp; downloads ↗</a></div><details><summary>Products &amp; source limits</summary><p>{row.products.join(' · ')}</p><p>{row.notes}</p></details></li>)}</ul>
    <details className={styles.comparison}><summary>Before comparing providers</summary><p>A ground DEM, surface model, canopy model and orbital profile measure different things. Mirror copies of one survey are not independent observations. Quantitative comparison needs:</p><ul>{LIDAR_COMPARISON_REQUIREMENTS.map(item => <li key={item}>{item}</li>)}</ul></details>
  </details>;
}
