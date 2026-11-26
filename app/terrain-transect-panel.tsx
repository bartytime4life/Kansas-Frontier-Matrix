'use client';
import {useEffect,useMemo,useRef,useState} from 'react';
import {terrainTransect,transectGeometry,transectJSON,TRANSECT_METHOD,type TransectCoordinate} from './terrain-transect';
import type {TerrainTileData} from './terrain-viewport-tiles';
import type {LidarGridMode} from './kansas-lidar-grid-layer';
import styles from './terrain-transect-panel.module.css';
export type TerrainTransectDrawing={line:readonly TransectCoordinate[];drawing:boolean;onStart:()=>void;onFinish:()=>void;onUndo:()=>void;onClear:()=>void;redacted:boolean};
const names={ground:'Ground',surface:'Surface',canopy:'Canopy height'};
const metres=(v:number)=>v>=1000?(v/1000).toFixed(2)+' km':v.toFixed(1)+' m';
export function TerrainTransectPanel({entries,mode,paused,drawing:d}:{entries:readonly TerrainTileData[];mode:LidarGridMode;paused:boolean;drawing:TerrainTransectDrawing}){
 const profile=useMemo(()=>!paused&&!d.drawing?terrainTransect(d.line,entries,mode):null,[d.line,d.drawing,entries,mode,paused]);
 const geometry=useMemo(()=>profile?.stations.length?transectGeometry(profile):null,[profile]);
 const [probe,setProbe]=useState<{profile:typeof profile;index:number}|null>(null),section=useRef<HTMLElement|null>(null),revealed=useRef<readonly TransectCoordinate[]|null>(null);
 const index=profile&&probe?.profile===profile?probe.index:Math.max(0,profile?.stations.findIndex(s=>s.value!==null)??0),sample=profile?.stations[index],point=geometry?.points[index],source=profile?.sources.find(s=>s.tile===sample?.tile);
 useEffect(()=>{if(profile?.stations.length&&revealed.current!==d.line){revealed.current=d.line;section.current?.scrollIntoView({block:'start',behavior:'auto'});}},[profile,d.line]);
 function download(){if(!profile||paused||d.drawing||d.redacted||!profile.stations.length)return;const url=URL.createObjectURL(new Blob([transectJSON(profile)],{type:'application/json'})),a=document.createElement('a');a.href=url;a.download='kfm-'+mode+'-transect.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);}
 return <section ref={section} className={styles.panel} data-terrain-transect aria-label="Drawn terrain cross-section">
  <header><span>LANDSCAPE LAB</span><strong>Draw a terrain profile</strong><small>Follow a ridge, valley or canopy across loaded tiles.</small></header>
  <div className={styles.actions}><button type="button" onClick={d.onStart} disabled={paused}>{d.drawing?'Cancel drawing':'Draw a cross-section'}</button>{d.drawing&&<button type="button" disabled={d.line.length<2} onClick={d.onFinish}>Finish profile</button>}</div>
  {d.drawing?<p role="status">Click the map to trace your line · {d.line.length} points. Finish to read source cells. Up to 64 vertices; no extra data downloads.</p>:paused&&d.line.length>1?<p role="status">Profile paused while the layer is inactive, hidden or moving. It updates from current source tiles after settling.</p>:null}
  {d.line.length>0&&<div className={styles.secondary}><button type="button" onClick={d.onUndo}>Undo point</button><button type="button" onClick={d.onClear}>Clear line</button></div>}
  {profile?.error&&<p role="alert">{profile.error}</p>}
  {profile&&geometry&&<>
   <dl className={styles.stats}><div><dt>Line length ≈</dt><dd>{metres(profile.length)}</dd></div><div><dt>Supported stations</dt><dd>{profile.supported}/{profile.stations.length}</dd></div><div><dt>Source tiles</dt><dd>{profile.sources.length}</dd></div></dl>
   <figure><figcaption>{names[mode]} · unscaled source metres</figcaption><svg viewBox="0 0 320 150" role="img" aria-label={`${names[mode]} cross-section: ${profile.supported} of ${profile.stations.length} stations supported, ${metres(profile.length)} approximate distance. Gaps and source boundaries split the guides; use the slider for numeric readings.`}>
    <path className={styles.axis} d="M12 12V124H308"/>
    {geometry.paths.map((path,i)=><path key={i} d={path} className={styles.guide}/>)}
    {geometry.points.map((p,i)=>p&&<circle key={i} cx={p.x} cy={p.y} r="1.35" className={styles.dot}/>)}
    {point&&<><path d={`M${point.x} 12V124`} className={styles.cursor}/><circle cx={point.x} cy={point.y} r="4" className={styles.selected}/></>}
    <text x="12" y="144">A · 0 m</text><text x="308" y="144" textAnchor="end">B · {metres(profile.length)}</text>
   </svg><div className={styles.range}><span>{profile.supported?geometry.low.toFixed(2)+'–'+geometry.high.toFixed(2)+' m':'No supported source stations'}</span><span>Reference may vary by tile</span></div></figure>
   <label className={styles.scrub}>Read along the line <output>{index+1}/{profile.stations.length}</output><input type="range" min="0" max={profile.stations.length-1} step="1" value={index} aria-label="Explore terrain transect stations" aria-valuetext={`Station ${index+1}, ${sample?.value===null?'no supported height':sample?.value+' source metres'}, ${sample?metres(sample.distance):''} from start`} onChange={e=>setProbe({profile,index:Number(e.target.value)})}/></label>
   {sample&&<div className={styles.reading} aria-live="polite"><strong>{sample.value===null?'No supported height at this station':sample.value.toFixed(3)+' m'}</strong><span>{metres(sample.distance)} from A · {names[mode]}{mode==='canopy'?' above same-survey ground':''}</span><small>Line position: {sample.coordinate.map(v=>v.toFixed(6)).join(', ')}°</small>{source&&<><span>Row {sample.row} · column {sample.column}</span><small>Source cell center: {sample.center?.map(v=>v.toFixed(6)).join(', ')}°</small><details><summary>This station’s source</summary><dl><dt>Source</dt><dd>{source.source}</dd><dt>Vertical reference</dt><dd>{source.verticalReference}</dd><dt>Acquisition</dt><dd>{source.acquisition}</dd><dt>Source-grid spacing</dt><dd>{source.spacing.map(n=>n.toFixed(2)).join(' × ')} · {source.spacingUnits}</dd><dt>Receipt cache time</dt><dd>{source.cacheTime??'Not supplied'}{source.stale?' · stale cache':''}</dd><dt>Request key</dt><dd>{source.requestKey}</dd></dl></details></>}</div>}
   <button className={styles.download} type="button" disabled={paused||d.redacted} onClick={download}>Download profile &amp; sources · JSON</button>
   {d.redacted&&<p>Download is unavailable while location privacy is active.</p>}
   <p className={styles.limit}>Station counts are samples along your line, not coverage percentages. Missing stations stay gaps. Loaded source cells can be finer than the drawn 3D detail. No heights are extrapolated.</p>
   <details className={styles.methods}><summary>Distance, sampling &amp; scientific limits</summary><p>{TRANSECT_METHOD}</p></details>
  </>}
 </section>;
}
