// PRISM county summaries in observations.sqlite. Each PRISM grid (one variable, resolution and
// period) is identified only by its source path, so the gateway reads the 361k grid paths once into
// an in-memory catalog and asks SQLite only for the chosen grids' county rows, through an index.
// Owner approval for public release: 2026-11-01; per-file acquisition dates are not yet verified.
import {only,text,oneOf,page,num,str,fail} from './query.mjs';

const VARIABLES=Object.freeze(['ppt','tmax','tmin','tmean','tdmean','vpdmin','vpdmax','soltotal','solslope','solclear','soltrans']);
const PRODUCTS=Object.freeze(['an','lt','normals','stable-201506']);
const SERIES=/^time_series\/us\/(an|lt)\/(4km|800m)\/([a-z]+)\/(daily|monthly)\/\d{4}\/prism_\3_us_(?:25m|30s)_(\d{8}|\d{6}|\d{4})\.zip$/;
const NORMALS=/^normals\/us\/(4km|800m)\/([a-z]+)\/(daily|monthly)\/prism_\2_us_(?:25m|30s)_2020(\d{4}|\d{2}|)_avg_30y\.zip$/;
const STABLE=/^prior_versions\/ppt\/daily_D1_201506\/\d{4}\/PRISM_ppt_stable_4kmD1_(\d{8})_bil\.zip$/;

/** {product,resolution,variable,step,period} for one grid's source path, or null. */
export function prismGrid(path){
 let m=SERIES.exec(path);
 if(m){const d=m[5],step=d.length===8?'daily':d.length===6?'monthly':'annual';
  return {product:m[1],resolution:m[2],variable:m[3],step,period:step==='daily'?`${d.slice(0,4)}-${d.slice(4,6)}-${d.slice(6)}`:step==='monthly'?`${d.slice(0,4)}-${d.slice(4)}`:d};}
 if((m=NORMALS.exec(path))){const d=m[4],step=d.length===4?'daily':d.length===2?'monthly':'annual';
  return {product:'normals',resolution:m[1],variable:m[2],step,period:step==='daily'?`${d.slice(0,2)}-${d.slice(2)}`:step==='monthly'?d:'annual'};}
 if((m=STABLE.exec(path))){const d=m[1];return {product:'stable-201506',resolution:'4km',variable:'ppt',step:'daily',period:`${d.slice(0,4)}-${d.slice(4,6)}-${d.slice(6)}`};}
 return null;
}

function bound(v,step,end){
 if(v===undefined||v===null||v==='')return null;
 const m=/^(\d{4})(?:-(\d{2})(?:-(\d{2}))?)?$/.exec(String(v).trim());if(!m)throw fail();
 if(+m[1]<1700||+m[1]>2100||m[2]&&(+m[2]<1||+m[2]>12)||m[3]&&(+m[3]<1||+m[3]>31))throw fail();
 if(step==='annual')return m[1];
 const month=m[2]??(end?'12':'01');
 if(step==='monthly')return `${m[1]}-${month}`;
 return `${m[1]}-${month}-${m[3]??(end?'31':'01')}`;
}

function catalog(db,cache){
 if(cache.has('prism'))return cache.get('prism');
 const series=new Map(),units=new Map();
 for(const r of db.prepare('SELECT grid_id,source_path,unit FROM kfm_prism_grids').iterate()){
  const g=prismGrid(r.source_path);if(!g)continue;
  const key=`${g.product}|${g.resolution}|${g.variable}|${g.step}`;
  if(!series.has(key)){series.set(key,[]);units.set(key,r.unit);}
  series.get(key).push([g.period,r.grid_id]);
 }
 for(const list of series.values())list.sort((a,b)=>a[0]<b[0]?-1:a[0]>b[0]?1:a[1]-b[1]);
 const first=db.prepare('SELECT MIN(grid_id) AS id FROM kfm_prism_grids').get().id;
 const counties=db.prepare('SELECT DISTINCT county_geoid,county_name FROM kfm_prism_county_stats WHERE grid_id=? ORDER BY county_geoid').all(first).map(r=>({geoid:r.county_geoid,name:r.county_name}));
 const value={series,units,counties};cache.set('prism',value);return value;
}

export const prismCounty={
 id:'prism-county',db:'observations',title:'PRISM county climate summaries',
 source:Object.freeze({provider:'PRISM Group, Oregon State University',url:'https://prism.oregonstate.edu/',
  coverage:'Kansas counties (2025 TIGER), PRISM AN/LT time series 1895-2026, 1991-2020 normals and the 2015-06 stable precipitation version',
  notes:'Modeled values summarized over the PRISM cells whose centers fall in each county: not station observations or area-weighted statistics. Cite as: PRISM Group, Oregon State University, https://prism.oregonstate.edu. Per-file acquisition dates are not yet verified.'}),
 indexes:[{name:'kfm_prism_county_stats_grid',sql:'CREATE INDEX IF NOT EXISTS kfm_prism_county_stats_grid ON kfm_prism_county_stats(grid_id, county_geoid)'}],
 params:{variable:VARIABLES.join(', ')+' (required)',county:'county FIPS (e.g. 173 or 20173) or name; leave out for every county in one period',
  step:'daily, monthly (default) or annual',resolution:'4km (default) or 800m',product:'an (default), lt, normals or stable-201506',
  from:'YYYY, YYYY-MM or YYYY-MM-DD',to:'YYYY, YYYY-MM or YYYY-MM-DD',limit:'1-2000 (500)',offset:'0-100000'},
 parse(input){
  only(input,['variable','county','step','resolution','product','from','to','limit','offset']);
  const step=oneOf(input.step,['daily','monthly','annual'],{fallback:'monthly'}),product=oneOf(input.product,PRODUCTS,{fallback:'an'});
  const raw=text(input.county,/^(?:\d{1,3}|20\d{3})$|^[A-Z][A-Z .'-]{1,29}$/);
  const county=raw===null?null:/^20\d{3}$/.test(raw)?raw:/^\d{1,3}$/.test(raw)?'20'+raw.padStart(3,'0'):raw;
  const q={variable:oneOf(input.variable,VARIABLES,{required:true}),county,step,resolution:oneOf(input.resolution,['4km','800m'],{fallback:'4km'}),product,
   from:bound(input.from,step,false),to:bound(input.to,step,true),...page(input,{max:2000,fallback:500})};
  if(product==='normals'&&(q.from||q.to))throw fail();
  if(q.from&&q.to&&q.from>q.to)throw fail();
  // Every county at once only for a single time-series period; normals need a county.
  if(!q.county&&(product==='normals'||!q.from||q.from!==q.to))throw fail();
  return q;
 },
 run(db,q,{cache}){
  const cat=catalog(db,cache),key=`${q.product}|${q.resolution}|${q.variable}|${q.step}`,unit=str(cat.units.get(key));
  const grids=(cat.series.get(key)??[]).filter(([p])=>(!q.from||p>=q.from)&&(!q.to||p<=q.to));
  const row=(period,r)=>({period,county:{geoid:r.county_geoid,name:r.county_name},mean:num(r.mean),min:num(r.minimum),max:num(r.maximum),validCells:num(r.valid_pixels),qualityFlag:str(r.quality_flag),unit});
  const cols='SELECT grid_id,county_geoid,county_name,mean,minimum,maximum,valid_pixels,quality_flag FROM kfm_prism_county_stats WHERE ';
  if(q.county){
   const county=/^\d+$/.test(q.county)?cat.counties.find(c=>c.geoid===q.county):cat.counties.find(c=>c.name.toUpperCase()===q.county);
   if(!county)return {total:0,rows:[]};
   const chosen=grids.slice(q.offset,q.offset+q.limit),period=new Map(chosen.map(([p,id])=>[id,p]));
   if(!chosen.length)return {total:grids.length,county,rows:[]};
   const rows=db.prepare(cols+`grid_id IN (${chosen.map(()=>'?').join(',')}) AND county_geoid=?`).all(...chosen.map(g=>g[1]),county.geoid)
    .map(r=>row(period.get(r.grid_id),r)).sort((a,b)=>a.period<b.period?-1:a.period>b.period?1:0);
   return {total:grids.length,county,unit,rows};
  }
  // One period, every county.
  const one=grids[0];if(!one)return {total:0,rows:[]};
  const all=db.prepare(cols+'grid_id=? ORDER BY county_geoid').all(one[1]).map(r=>row(one[0],r));
  return {total:all.length,unit,rows:all.slice(q.offset,q.offset+q.limit)};
 },
};
