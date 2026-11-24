'use client';
import Link from 'next/link';
import { useMemo, useState } from 'react';
import { NeonLidarWorkspace, useNeonLidarPreview } from '../../neon-lidar-panel';
import { createNeonScienceDataset, neonScienceDatasetJSON } from '../../neon-lidar-science';
import RecordLab, { toCSV } from '../../living-welcome/stories/record-lab.jsx';
import { downloadCSV } from '../../living-welcome/stories/story-kit.mjs';
import styles from './terrain.module.css';

const DEFAULT_CONTROLS = { view: 'chart', metric: 'chm_m', xMetric: 'chm_m', yMetric: 'surface_above_ground_m' };

export function TerrainAnalysis({ dataset, controller }) {
  const [controls, setControls] = useState(DEFAULT_CONTROLS);
  const { bundle } = dataset;
  const { row: draftRow, column: draftColumn } = controller.coordinateDraft;
  const grid = dataset.receipt.preview.grid;
  const selected = useMemo(() => {
    if (!/^\d+$/.test(draftRow) || !/^\d+$/.test(draftColumn)) return undefined;
    const numericRow = Number(draftRow), numericColumn = Number(draftColumn);
    if (!Number.isInteger(numericRow) || numericRow < 1 || numericRow > grid.height
      || !Number.isInteger(numericColumn) || numericColumn < 1 || numericColumn > grid.width) return undefined;
    return bundle.data.records.find(record => record.row === numericRow && record.column === numericColumn);
  }, [bundle, grid, draftRow, draftColumn]);
  const linkedControls = useMemo(() => ({ ...controls, selectedId: selected?.id ?? null }), [controls, selected?.id]);
  const change = next => {
    setControls(next);
    if (Object.hasOwn(next, 'selectedId') && next.selectedId !== selected?.id) {
      const record = bundle.data.records.find(row => row.id === next.selectedId);
      controller.setCoordinateDraft(record ? { row: String(record.row), column: String(record.column) } : { row: '', column: '' });
    }
  };
  const saveReceipt = () => {
    const url = URL.createObjectURL(new Blob([neonScienceDatasetJSON(dataset)], { type: 'application/json' }));
    const link = document.createElement('a'); link.href = url; link.download = 'kfm-neon-terrain-science.json';
    document.body.append(link); link.click(); link.remove(); setTimeout(() => URL.revokeObjectURL(url), 1000);
  };
  return <section className={styles.analysis} aria-labelledby="terrain-analysis-title">
    <div className={styles.sectionTitle}><div><p>02 / DESCRIBE THE SAMPLES</p><h2 id="terrain-analysis-title">From a place to a pattern.</h2></div><div className={styles.exports}>
      <button type="button" onClick={() => { const csv = toCSV(bundle, { controls: linkedControls, time: null }); downloadCSV(csv.filename, csv.rows); }}>Download selection CSV ↓</button>
      <button type="button" onClick={saveReceipt}>Download science JSON ↓</button>
    </div></div>
    <p className={styles.scope}>These statistics describe regularly spaced nearest 1 m samples. They do not represent every native pixel or measured vegetation area. Raster inspection keeps the whole tile visible; analysis filters apply to the charts, table and CSV.</p>
    <p className={styles.caution}>Spatial neighbors are dependent. Relationships are descriptive; DSM − DTM is arithmetically coupled to ground and surface elevation. Provider CHM is a separate product. No significance, field accuracy, species, biomass, carbon or change is inferred.</p>
    <RecordLab bundle={bundle} time={null} controls={linkedControls} onControls={change}/>
    <details className={styles.limits}><summary>Methods and interpretation limits</summary><ul>{bundle.data.limits.map(limit => <li key={limit}>{limit}</li>)}</ul></details>
  </section>;
}

export default function TerrainScience() {
  const controller = useNeonLidarPreview();
  const dataset = useMemo(() => controller.pilotReceipt ? createNeonScienceDataset(controller.pilotReceipt) : null, [controller.pilotReceipt]);
  return <div className={styles.page}>
    <header className={styles.header}><Link href="/labs" className={styles.brand}>KFM <span>/ THE RESEARCH ATLAS</span></Link><nav aria-label="Terrain science navigation"><Link href="/">Map explorer ↗</Link><Link href="/labs">All Science labs</Link><Link href="/acquisition">Data & receipts</Link></nav></header>
    <main className={styles.main}>
      <section className={styles.intro}><p className={styles.eyebrow}>ONE TILE / THREE SURFACES / OPEN SCIENCE</p><h1>Terrain &amp; vegetation.</h1><p>Read the ground. Compare the canopy. Follow the same samples from the raster into distributions, relationships and a source-linked export.</p><div className={styles.datasetStrip} aria-label="Available provider pilot"><span><b>Available pilot · Konza Prairie</b> Kansas · 1 km tile</span><span><b>Historical acquisition</b> Catalog September 2024</span><span><b>Scientific review pending</b> Preview only · not admitted</span></div></section>
      <NeonLidarWorkspace controller={controller} embedded/>
      {dataset ? <TerrainAnalysis key={dataset.id} dataset={dataset} controller={controller}/> : <section className={styles.analysisEmpty} aria-labelledby="terrain-analysis-empty"><p className={styles.eyebrow}>02 / SCIENCE WORKSPACE</p><h2 id="terrain-analysis-empty">A real dataset opens the instrument.</h2><p>{controller.preview ? 'Your imported grid remains available in the raster inspector. Scientific analysis here requires the validated Konza Prairie provider receipt; a local or synthetic file is not treated as that pilot.' : 'Load the Konza Prairie pilot above to compare distributions, inspect quartiles and missingness, choose relationship axes, and download the selected source samples.'}</p><p>Free tools. No subscription. The provider preview retains its source files, sampling method and pending review.</p></section>}
    </main><footer className={styles.footer}><span>KANSAS FRONTIER MATRIX / TERRAIN SCIENCE</span><Link href="/labs">Return to the research atlas ↑</Link></footer>
  </div>;
}
