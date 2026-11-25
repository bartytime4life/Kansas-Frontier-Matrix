'use client';
import {useId,useState} from 'react';
import {COVERAGE_LABELS,coverageRect,type TerrainCoverage} from './terrain-coverage';
import styles from './terrain-coverage-panel.module.css';
const label={ground:'Ground',surface:'Surface',canopy:'Canopy height'};
export function TerrainCoveragePanel({coverage:c,navigating,preparing,paused=false}:{coverage:TerrainCoverage;navigating:boolean;preparing:boolean;paused?:boolean}){
 const [selected,setSelected]=useState(''),id=useId().replaceAll(':','');
 // Never rebind an old numeric offset to a new tile after pan, mode or refresh.
 const tile=c.tiles.find(t=>t.key===selected)??c.tiles[0],extent=c.bounds;
 return <details className={styles.coverage} onToggle={e=>{if(e.currentTarget.open)e.currentTarget.querySelector('summary')?.scrollIntoView({block:'start',behavior:'auto'});}}><summary>Coverage in this view <span>{c.tiles.length?`${c.counts.supported+c.counts.gaps}/${c.tiles.length} supported tiles`:c.planState==='detail-required'?'Zoom closer':'No requested tiles'}</span></summary>
  <p className={styles.context}><strong>{label[c.mode]} · source support</strong><span>{paused?'Paused · last requested footprint':navigating?'Last settled footprint · updates after movement':preparing?'Source receipts shown · drawing is still preparing':'Current requested tile footprint · north up'}</span></p>
  {extent&&<>
   <svg className={styles.diagram} viewBox="0 0 280 190" role="img" aria-label={`${label[c.mode]} requested tiles, north up. Numbered tiles match the selector below; colors show source support, not drawn coverage.`}>
    <defs><pattern id={id+'pending'} width="6" height="6" patternUnits="userSpaceOnUse"><path d="M-1 1L1-1M0 6L6 0M5 7L7 5" stroke="#9bb9c2" strokeWidth="1"/></pattern><pattern id={id+'gaps'} width="6" height="6" patternUnits="userSpaceOnUse"><circle cx="3" cy="3" r="1" fill="#f4d48c"/></pattern></defs>
    <text x="264" y="15" className={styles.north}>N ↑</text>
    {c.tiles.map(t=>{const rect=coverageRect(t.bounds,extent);return <g key={t.key} data-state={t.state} data-selected={tile?.key===t.key}><rect {...rect} className={styles.tile}/>{(t.state==='pending'||t.state==='gaps')&&<rect {...rect} fill={`url(#${id+t.state})`} className={styles.pattern}/>}<text x={rect.x+rect.width/2} y={rect.y+rect.height/2} className={styles.number}>{t.number}</text></g>;})}
   </svg>
   <ul className={styles.legend} aria-label="Tile support legend">{Object.entries(c.counts).filter(([,n])=>n>0).map(([state,n])=><li key={state} data-state={state}><i aria-hidden="true"/>{COVERAGE_LABELS[state as keyof typeof COVERAGE_LABELS]} <b>{n}</b></li>)}</ul>
   <label className={styles.selector}>Inspect requested tile<select aria-label="Inspect requested tile" value={tile?.key??''} onChange={e=>setSelected(e.target.value)}>{c.tiles.map(t=><option key={t.key} value={t.key}>Tile {t.number} · {COVERAGE_LABELS[t.state]}{t.stale?' · stale cache':''}</option>)}</select></label>
   {tile&&<div className={styles.reading}>
    <strong>Tile {tile.number} · {COVERAGE_LABELS[tile.state]}</strong>
    {tile.supported!==null&&<p>{tile.supported.toLocaleString()} / {tile.total?.toLocaleString()} source cells supported. {tile.total!==null&&tile.supported<tile.total?'Unsupported cells remain gaps.':''}</p>}
    {tile.reason!==COVERAGE_LABELS[tile.state]&&<p>{tile.reason}</p>}
    <dl><dt>Requested extent · longitude / latitude</dt><dd>{tile.bounds.map(v=>v.toFixed(5)).join(', ')}°</dd><dt>Source</dt><dd>{tile.source}</dd><dt>Acquisition</dt><dd>{tile.acquisition}</dd><dt>Vertical reference</dt><dd>{tile.verticalReference}</dd><dt>Receipt cache time</dt><dd>{tile.checkedAt??'Not loaded'}{tile.stale?' · stale':''}</dd></dl>
   </div>}
  </>}
  {!extent&&<p>{navigating?'Waiting for the map to settle.':c.planState==='detail-required'?'Zoom closer to plan bounded native tiles.':c.planState==='outside'?'No current requested tiles in the Kansas data window.':'Waiting for the current layer’s tile plan.'}</p>}
  <p className={styles.limit}>Tile colors summarize returned source cells; gaps are not located within each tile. They do not show survey availability, area percentages or drawing completion. Ground is a resampled DEM; Surface and Canopy need native support. No extra downloads are started by this inspector.</p>
 </details>;
}
