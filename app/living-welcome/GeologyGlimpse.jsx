import { useEffect, useId, useState } from 'react';
import { geologyIntervals, readWelcomeGeology } from './geology-source';

/** One finite DOM/SVG reveal; never a second map or an interpolated section. */
export function GeologyGlimpse({ paused = false, reduced = false, expanded = false }) {
 const id = useId().replaceAll(':', ''), [record, setRecord] = useState(null), [failed, setFailed] = useState(false);
 const [lifted, setLifted] = useState(true), [automatic, setAutomatic] = useState(false);
 const [hidden, setHidden] = useState(() => typeof document !== 'undefined' && document.hidden);
 useEffect(() => {
  let current = true; const abort = new AbortController(), timeout = setTimeout(() => abort.abort(), 10000);
  readWelcomeGeology(abort.signal).then(value => {
   if (!current || abort.signal.aborted) return;
   setRecord(value); setAutomatic(!paused && !reduced && !document.hidden);
  }).catch(() => { if (current) setFailed(true); }).finally(() => clearTimeout(timeout));
  return () => { current = false; clearTimeout(timeout); abort.abort(); };
 // The request belongs to this settled Geology mount, not pause/replay controls.
 // eslint-disable-next-line react-hooks/exhaustive-deps
 }, []);
 useEffect(() => {
  const change = () => setHidden(document.hidden);
  document.addEventListener('visibilitychange', change);
  return () => document.removeEventListener('visibilitychange', change);
 }, []);
 const state = failed ? 'unavailable' : record ? 'ready' : 'loading';
 const intervals = record ? geologyIntervals(record) : [];
 return <figure className="welcome-geology-specimen" data-state={state} data-expanded={expanded} data-lifted={lifted} data-auto={automatic && !reduced} data-paused={paused || hidden} data-reduced={reduced} aria-label="One recorded well beneath a symbolic surface plate">
  <figcaption><span className="welcome-kicker">BENEATH THE MAP</span><strong>Lift the surface.<br/><em>Read one real log.</em></strong></figcaption>
  {state === 'ready' ? <>
   <svg className="welcome-geology-diagram" viewBox="0 0 380 324" role="img" aria-labelledby={`${id}-title ${id}-description`}>
    <title id={`${id}-title`}>WWC5 1054515520: eight original intervals, 0–60 ft below local land surface</title>
    <desc id={`${id}-description`}>A single recorded well column, not continuous geology. Symbolic surface plate and column width have no geographic footprint or elevation. Depths and descriptions are from the April 9, 2024 KGS log.</desc>
    <defs><pattern id={`${id}-bands`} width="12" height="6" patternUnits="userSpaceOnUse"><path d="M0 2h12M3 5h7" stroke="#061c28" strokeOpacity=".19" strokeWidth=".7"/></pattern><pattern id={`${id}-grain`} width="13" height="11" patternUnits="userSpaceOnUse"><circle cx="3" cy="3" r=".8" fill="#fff" fillOpacity=".23"/><circle cx="10" cy="8" r=".7" fill="#061c28" fillOpacity=".27"/></pattern></defs>
    <g className="welcome-geology-column">
     <path d="M113 94V298H252V94" fill="#081e29" stroke="#a8b4a3" strokeOpacity=".5"/>
     {intervals.map(row => <g key={row.index} data-top={row.top} data-bottom={row.bottom} data-description={row.description}><title>{row.top}–{row.bottom} ft: {row.description}</title><rect x="114" y={94 + row.y} width="110" height={row.height} fill={row.material.color}/><rect x="114" y={94 + row.y} width="110" height={row.height} fill={row.material.pattern === 'plain' || row.material.pattern === 'smooth' ? 'none' : `url(#${id}-${row.material.pattern === 'band' ? 'bands' : 'grain'})`}/><path d={`M224 ${94 + row.y}l26 -10v${row.height}l-26 10z`} fill={row.material.color}/><path d={`M224 ${94 + row.y}l26 -10v${row.height}l-26 10z`} fill="#061c28" fillOpacity=".3"/><path d={`M114 ${94 + row.y}h110l26 -10`} fill="none" stroke="#e5d4b1" strokeOpacity=".46" strokeWidth=".8"/></g>)}
     <path d="M224 94V298" stroke="#ecdbb9" strokeOpacity=".4"/>
     <g className="welcome-geology-ruler">{[0, 20, 40, 60].map(depth => <g key={depth}><path d={`M93 ${94 + depth / 60 * 204}h12`} stroke="currentColor"/><text x="83" y={98 + depth / 60 * 204} textAnchor="end">{depth}</text></g>)}<text x="83" y="77" textAnchor="end">ft</text></g>
     <g className="welcome-geology-materials"><path d="M251 97.4h12M251 134.8h12M251 158.6h12M251 230h12" stroke="#b7c7b2" strokeWidth=".7"/><text x="270" y="100.4">soil</text><text x="270" y="137.8">clay</text><text x="270" y="161.6">sandstone</text><text x="270" y="233">shale</text></g>
    </g>
    <g className="welcome-geology-plate" onAnimationEnd={() => setAutomatic(false)}><path d="M102 62L237 53L258 61L254 67L265 76L258 82L270 91L255 103L112 111L94 99Z" fill="#a8b9a1" stroke="#ead7a0" strokeWidth="1.5"/><path d="M112 111L255 103V109L112 117L94 105V99Z" fill="#4e756b" stroke="#c8b583" strokeWidth=".6"/><path d="M115 73l122 -8M110 84l138 -9M115 96l136 -10M140 65l8 40M177 62l8 42M214 60l8 42" stroke="#47665c" strokeOpacity=".35" strokeWidth=".7"/><circle cx="179" cy="84" r="4" fill="#123947" stroke="#f3d48b"/><path d="M179 78V69M173 84H164M185 84H194" stroke="#f3d48b" strokeWidth="1"/><text x="181" y="48" textAnchor="middle">SYMBOLIC SURFACE PLATE</text></g>
   </svg>
   <p className="welcome-geology-source">One recorded well · 2024 log <span>0–60 ft below local land surface</span></p>
   {expanded&&<div className="welcome-geology-controls"><button type="button" aria-pressed={lifted} onClick={() => { setAutomatic(false); setLifted(value => !value); }}>{lifted ? 'Return surface' : 'Lift surface'} <span aria-hidden="true">{lifted ? '↓' : '↑'}</span></button><a href={record.sourceUrl} target="_blank" rel="noreferrer">KGS original log ↗</a></div>}
   <small className="welcome-geology-limit">Width illustrative; unknown between observations.</small>
   {expanded&&<details className="welcome-geology-details"><summary>Original depths &amp; source limits</summary><p>WWC5 1054515520 · recorded 2024-04-09. GPS-labelled location, not surveyed. The symbolic plate is a presentation device, not this well’s footprint or a measured surface elevation.</p><ol>{intervals.map(row => <li key={row.index}><b>{row.top}–{row.bottom} ft</b> {row.description}</li>)}</ol><p>Colours and textures encode descriptions only. One log cannot establish nearby seams, aquifer occupancy or geological change. Source: Kansas Geological Survey website; all rights reserved. The record date is distinct from archive and retrieval dates.</p></details>}
  </> : <p className="welcome-geology-status" role="status">{failed ? 'Recorded log unavailable. No substitute geology is drawn; open Underground to inspect source status.' : 'Opening one verified KGS well log…'}</p>}
 </figure>;
}
