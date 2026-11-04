import { useId, useState } from 'react';
import './topic-illustration.css';

// Studies explain structure and methods. The map owns observations; generated
// specimen images and procedural geometry never become source data.
const STUDIES = {
 flora: { title:'Vegetation structure', description:'Plant architecture against classified land cover.', scope:'AI specimen illustration · no plant measurement', code:'BIO / 01', source:'NLCD 2021', detail:'LAND COVER · 30 m' },
 fauna: { title:'Wildlife & landscape', description:'Species form within regional landscape context.', scope:'AI specimen illustration · no animal tracking', code:'BIO / 02', source:'NLCD 2021', detail:'LANDSCAPE CONTEXT' },
 ecology: { title:'Watershed structure', description:'Surface, channel and subsurface in a single view.', scope:'AI terrain concept · not a measured flow model', code:'ECO / 03', source:'NLCD + WBD', detail:'COVER / DRAINAGE' },
 land: { title:'Survey geometry', description:'Survey references across a schematic surface.', scope:'Schematic geometry concept · BLM map shown separately', code:'GEO / 04', source:'BLM PLSS', detail:'TOWNSHIP REFERENCE' },
 history: { title:'Temporal registration', description:'Dated networks meet a contemporary reference base.', scope:'Registration concept · no reconstructed landscape', code:'TIME / 05', source:'KDOT 1918', detail:'HISTORICAL REFERENCE' },
 evidence: { title:'Evidence lineage', description:'Trace source, edition, method and limitations.', scope:'Provenance concept · not a released record', code:'TRACE / 06', source:'CENSUS 2020', detail:'COUNTY REFERENCE' },
 'public-safety': { title:'Reference & coverage', description:'Separate mapped geography from incident coverage.', scope:'Coverage concept · not an incident or safety model', code:'CIVIC / 07', source:'CENSUS 2020', detail:'REFERENCE GEOGRAPHY' },
};

function InstrumentFrame({study,children,prefix}) {
 return <>
  <defs>
   <linearGradient id={`${prefix}-glass`} x2=".5" y2="1"><stop stopColor="#69b9c0" stopOpacity=".18"/><stop offset="1" stopColor="#142e3c" stopOpacity=".05"/></linearGradient>
   <linearGradient id={`${prefix}-scan`} x2="0" y2="1"><stop stopColor="#8bdae4" stopOpacity="0"/><stop offset=".85" stopColor="#8bdae4" stopOpacity=".04"/><stop offset="1" stopColor="#8bdae4" stopOpacity=".35"/></linearGradient>
   <clipPath id={`${prefix}-viewport`}><rect x="25" y="45" width="550" height="340"/></clipPath>
  </defs>
  <g className="ti-frame">
   <path d="M25 67V45h22m506 0h22v22M25 363v22h22m506 0h22v-22"/>
   <path d="M65 45h470M65 385h470" opacity=".25"/>
   {Array.from({length:17},(_,i)=><path key={i} d={`M${60+i*30} 391v${i%4===0?7:3}M19 ${65+i*18}h${i%4===0?-7:-3}M581 ${65+i*18}h${i%4===0?7:3}`} opacity={i%4===0?.6:.25}/>) }
  </g>
  <g className="ti-instrument-label"><text x="26" y="25">KFM / SYSTEMS ATLAS</text><text x="574" y="25" textAnchor="end">{study.code}</text></g>
  <g clipPath={`url(#${prefix}-viewport)`}>{children}</g>
  <g className="ti-source-label"><text x="28" y="416">{study.source}</text><text x="572" y="416" textAnchor="end">{study.detail}</text></g>
 </>;
}

function Specimen({topic,prefix}) {
 const [failed,setFailed] = useState(false);
 return <>
  {failed?<text x="300" y="215" textAnchor="middle" className="ti-asset-failure">Specimen asset unavailable</text>:
   <g className={`ti-specimen ti-specimen-${topic}`}>
    <image href={`/welcome/scientific/${topic}-study.webp`} x="28" y="47" width="544" height="336" preserveAspectRatio="xMidYMid meet" onError={()=>setFailed(true)}/>
   </g>}
  <g className="ti-study-guide">
   {topic==='flora'?<><path d="M332 103h109l20-19M276 205H135l-22 22M327 306h121l18 20"/><circle cx="332" cy="103" r="3"/><circle cx="276" cy="205" r="3"/><circle cx="327" cy="306" r="3"/><text x="465" y="80">INFLORESCENCE</text><text x="60" y="241">LEAF VENATION</text><text x="468" y="339">ROOT SYSTEM</text></>:
    topic==='fauna'?<><path d="M300 133H161l-21-22M435 204h53l20 20M223 294H117l-17 17"/><circle cx="300" cy="133" r="3"/><circle cx="435" cy="204" r="3"/><circle cx="223" cy="294" r="3"/><text x="69" y="104">MORPHOLOGY</text><text x="465" y="239">SPECIMEN</text><text x="54" y="325">PRAIRIE CONTEXT</text></>:
    <><path d="M202 147H102l-18-18M369 221h109l18-20M354 325h114l20 20"/><circle cx="202" cy="147" r="3"/><circle cx="369" cy="221" r="3"/><circle cx="354" cy="325" r="3"/><text x="53" y="120">SURFACE</text><text x="472" y="192">CHANNEL</text><text x="449" y="359">SUBSURFACE</text></>}
  </g>
  <rect className="ti-scan" x="26" y="46" width="548" height="95" fill={`url(#${prefix}-scan)`}/>
 </>;
}

// Procedural heights are schematic: no metres or measured terrain are claimed.
function surfacePoint(u,v,flat=false) {
 const h=flat?0:26*Math.sin(u*.21)*Math.cos(v*.23)+22*Math.exp(-((u-7)**2+(v-9)**2)/30);
 return [300+(u-v)*16,106+(u+v)*7-h];
}
function lineOf(points) { return points.map(([x,y],i)=>`${i?'L':'M'}${x.toFixed(2)} ${y.toFixed(2)}`).join(' '); }
function SurfaceMesh({flat=false}) {
 return <g className="ti-surface-mesh" fill="none">
  {Array.from({length:17},(_,n)=><g key={n}>
   <path d={lineOf(Array.from({length:33},(_,i)=>surfacePoint(n,i/2,flat)))}/>
   <path d={lineOf(Array.from({length:33},(_,i)=>surfacePoint(i/2,n,flat)))}/>
  </g>)}
 </g>;
}

function Survey({prefix}) {
 const [a,b,c,d]=[[0,0],[16,0],[16,16],[0,16]].map(([u,v])=>surfacePoint(u,v));
 const edge=lineOf([a,b,c,d,a]);
 return <>
  <g className="ti-model-orbit">
   <path d={edge} fill={`url(#${prefix}-glass)`} stroke="#719fa8" strokeWidth=".7"/>
   <g transform="translate(0 27)" opacity=".27"><SurfaceMesh flat/></g>
   <SurfaceMesh/>
   <g stroke="#9dbdbf" opacity=".3">{[a,b,c,d].map(([x,y],i)=><path key={i} d={`M${x} ${y}v27`}/>)}</g>
   <g className="ti-survey-reference" fill="none" stroke="#e1c791" strokeWidth="1.4">
    <path d={lineOf(Array.from({length:33},(_,i)=>surfacePoint(8,i/2)))}/>
    <path d={lineOf(Array.from({length:33},(_,i)=>surfacePoint(i/2,8)))}/>
   </g>
   {[[4,4],[12,4],[4,12],[12,12]].map(([u,v],i)=>{const [x,y]=surfacePoint(u,v);return <g key={i} className="ti-control-point" style={{'--i':i}}><circle cx={x} cy={y} r="3" fill="#e2ce9b"/><path d={`M${x-8} ${y}h16m-8-8v16`} stroke="#e2ce9b" strokeWidth=".7"/></g>;})}
  </g>
  <g className="ti-study-guide"><path d="M300 119V78h127M110 237H66v48"/><text x="432" y="81">SURVEY AXIS</text><text x="56" y="303">CONTROL / ALIGNMENT</text></g>
 </>;
}

function Registration({prefix}) {
 const frame='M85 149 332 82 518 191 271 271Z';
 const network='M117 155 194 167 235 137 314 159 353 126 454 169M153 195 216 188 276 222 346 184 397 215 467 191M242 113 251 176 310 201 322 248';
 return <>
  <g className="ti-registration-lower" transform="translate(0 74)"><path d={frame} fill={`url(#${prefix}-glass)`} stroke="#75a5b3"/><path d={network} fill="none" stroke="#87c6d5" strokeWidth="1.5"/></g>
  <g className="ti-registration-upper"><path d={frame} fill={`url(#${prefix}-glass)`} stroke="#c7b78f"/><path className="ti-route-trace" d={network} fill="none" stroke="#dfc28b" strokeWidth="1.5"/></g>
  <g stroke="#c0d0cc" strokeDasharray="2 6" opacity=".4">{[[117,155],[235,137],[353,126],[397,215]].map(([x,y])=><path key={x} d={`M${x} ${y}v74`}/>)}</g>
  <g className="ti-study-guide"><path d="M445 140h56V92M402 302h107"/><text x="480" y="82">1918</text><text x="439" y="325">MODERN BASE</text><text x="73" y="355">ALIGN / COMPARE / INTERPRET</text></g>
 </>;
}

function Evidence({prefix}) {
 const labels=['PROVIDER','EDITION','METHOD','LIMITS'];
 return <>
  <g fill="none" stroke="#75a9b7" opacity=".28"><ellipse cx="300" cy="242" rx="231" ry="99"/><ellipse cx="300" cy="242" rx="175" ry="72"/><path d="M63 242h474M300 134v213"/></g>
  <path className="ti-lineage-path" d="M93 233 225 179 377 251 504 195" pathLength="1" fill="none" stroke="#b8e3e6" strokeWidth="1.5"/>
  {[[93,233],[225,179],[377,251],[504,195]].map(([x,y],i)=><g key={i} className="ti-lineage-node" style={{'--i':i}}>
   <path d={`M${x-37} ${y-15}l38-18 38 18-38 18Z`} fill={`url(#${prefix}-glass)`} stroke="#a2c8cd"/>
   <path d={`M${x-37} ${y-15}v13l38 18 38-18v-13M${x+1} ${y+3}v13`} fill="none" stroke="#6f9ba9" opacity=".7"/>
   <path d={`M${x+1} ${y-16}v-40`} stroke="#e0c58e" strokeWidth=".8"/>
   <circle cx={x+1} cy={y-16} r="3" fill="#e3d09d"/>
   <text x={x+1} y={y-65} textAnchor="middle" className="ti-node-label">{labels[i]}</text>
  </g>)}
  <g className="ti-study-guide"><text x="72" y="363">REFERENCE → QUALIFICATION → INTERPRETATION</text></g>
 </>;
}

function Coverage({prefix}) {
 return <>
  <g className="ti-coverage-stack">
   <g transform="translate(0 30)"><SurfaceMesh flat/></g>
   <path d="M94 176 301 116 506 210 299 278Z" fill={`url(#${prefix}-glass)`} stroke="#79b2bd"/>
   <g fill="none" stroke="#9bd0d6" opacity=".6">{[0,1,2,3,4,5,6].map(i=><g key={i}><path d={`M${121+i*27} ${168-i*8}l205 94M${119+i*28} ${188+i*12}l207-60`}/></g>)}</g>
   <path className="ti-coverage-reference" d="M94 176 301 116 506 210 299 278Z" pathLength="1" fill="none" stroke="#cee6dc" strokeDasharray=".08 .92" strokeWidth="2"/>
  </g>
  <g className="ti-coverage-missing" fill="none" stroke="#91a4ac" strokeDasharray="3 5"><path d="M94 116 301 56 506 150 299 218Z"/><path d="M94 86 301 26 506 120 299 188Z" opacity=".35"/></g>
  <g className="ti-study-guide"><path d="M476 197h47v38M431 94h93"/><text x="410" y="252">REFERENCE GEOGRAPHY</text><text x="439" y="85">INCIDENTS / UNCONNECTED</text><text x="74" y="361">GEOGRAPHY DOES NOT ESTABLISH INCIDENT COVERAGE</text></g>
 </>;
}

const ART={land:Survey,history:Registration,evidence:Evidence,'public-safety':Coverage};
function sourceStatus(sources,mapState) {
 if(mapState==='unavailable')return ['unavailable','MAP UNAVAILABLE'];
 if(!sources.length)return ['loading','SOURCE CONTEXT PENDING'];
 if(sources.some(s=>s.state==='unavailable'))return ['unavailable','SOURCE UNAVAILABLE'];
 if(sources.every(s=>s.state==='hidden'))return ['hidden','MAP OVERLAYS HIDDEN'];
 if(sources.some(s=>s.state==='loading'))return ['loading','SOURCE CONTEXT LOADING'];
 if(sources.some(s=>s.state==='zoom-in'))return ['context','CLOSER MAP SCALE NEEDED'];
 if(sources.some(s=>s.state==='empty'))return ['context','NO RECORDS RETURNED'];
 return ['context','PROVIDER CONTEXT SELECTED'];
}

export function TopicIllustration({topic,paused=false,reduced=false,sources=[],mapState='loading'}) {
 const id=useId().replace(/:/g,'');
 if(!Object.hasOwn(STUDIES,topic))return null;
 const study=STUDIES[topic],Art=ART[topic],prefix=`study-${id}`;
 const [status,statusLabel]=sourceStatus(sources,mapState);
 return <figure className="topic-illustration" data-topic={topic} data-paused={paused||reduced} data-reduced={reduced} data-source-state={status}>
  <div className="ti-art"><svg viewBox="0 0 600 430" aria-hidden="true" focusable="false">
   <InstrumentFrame study={study} prefix={prefix}>{Art?<Art prefix={prefix}/>:<Specimen topic={topic} prefix={prefix}/>}</InstrumentFrame>
  </svg></div>
  <figcaption><span className="ti-eyebrow">SCIENTIFIC STUDY <span aria-hidden="true">/</span> {study.code}</span><strong>{study.title}</strong><span className="ti-description">{study.description}</span><small>{study.scope}</small><span className="ti-status"><i aria-hidden="true"/>{statusLabel}</span></figcaption>
 </figure>;
}
