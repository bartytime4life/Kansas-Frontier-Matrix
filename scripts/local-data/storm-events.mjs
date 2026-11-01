// The one Storm Events question the website may ask the pipeline PC: Kansas events filtered by
// county or forecast zone, date range and event type, newest first, one bounded page at a time.
// Validation is shared by the website and the gateway. Publication allow-list (phase 1): the
// event details NOAA publishes; the fatalities table (age, sex) is not exposed. No dependencies.
const fail=()=>Object.assign(new Error('QUERY_INVALID'),{code:'QUERY_INVALID'});
import {day as calendarDay} from './query.mjs';
export const STORM_EVENTS_SOURCE=Object.freeze({
 provider:'NOAA NCEI Storm Events Database',url:'https://www.ncei.noaa.gov/stormevents/',
 coverage:'Kansas, 1950 onward, from the NCEI Storm Events CSV files (v1.0); a newer NCEI file for a year replaces that year, checked weekly',
 notes:'Damage amounts are NOAA estimates as published (for example 10.00K). Times are local standard time for the listed time zone.',
});
export const STORM_EVENTS_MAX_LIMIT=200;

function day(value,fallback){
 if(value===undefined||value===null||value==='')return fallback;
 const normalized=calendarDay(value);
 if(normalized<'1950-01-01')throw fail();
 return normalized;
}

/** Normalize a query from URL parameters or a gateway request body. Throws QUERY_INVALID. */
export function parseStormQuery(input={}){
 const allowed=new Set(['county','from','to','type','limit','offset']);
 if(!input||typeof input!=='object'||Array.isArray(input)||Object.keys(input).some(k=>!allowed.has(k)))throw fail();
 const text=v=>v===undefined||v===null?'':String(v).trim();
 const county=text(input.county).toUpperCase(),type=text(input.type).toUpperCase();
 if(county&&!/^(?:\d{1,3}|[A-Z][A-Z .'/-]{1,39})$/.test(county))throw fail();
 if(type&&!/^[A-Z][A-Z ()/-]{1,39}$/.test(type))throw fail();
 const from=day(input.from,'1950-01-01'),to=day(input.to,'2100-12-31');
 if(from>to)throw fail();
 const int=(v,dflt,min,max)=>{if(v===undefined||v===null||v==='')return dflt;const s=String(v);if(!/^\d{1,5}$/.test(s))throw fail();const n=+s;if(n<min||n>max)throw fail();return n;};
 return {county:county?(/^\d+$/.test(county)?{fips:+county}:{name:county}):null,from,to,type:type||null,
  limit:int(input.limit,50,1,STORM_EVENTS_MAX_LIMIT),offset:int(input.offset,0,0,50000)};
}

const COLUMNS=['event_id','episode_id','event_type','cz_type','cz_fips','cz_name','wfo','begin_yearmonth','begin_day','begin_time',
 'end_yearmonth','end_day','end_time','cz_timezone','injuries_direct','injuries_indirect','deaths_direct','deaths_indirect',
 'damage_property','damage_crops','source','magnitude','magnitude_type','flood_cause','category','tor_f_scale','tor_length','tor_width',
 'begin_range','begin_azimuth','begin_location','end_range','end_azimuth','end_location','begin_lat','begin_lon','end_lat','end_lon',
 'episode_narrative','event_narrative','data_source'];
const BEGIN='(CAST(begin_yearmonth AS INTEGER)*100+CAST(begin_day AS INTEGER))';

/** SQL and parameters for one normalized query (rows) and its total (count). */
export function stormEventsSql(q){
 const where=[`${BEGIN} BETWEEN ? AND ?`],params=[+q.from.replaceAll('-',''),+q.to.replaceAll('-','')];
 if(q.county?.fips!==undefined){where.push("cz_type='C' AND CAST(cz_fips AS INTEGER)=?");params.push(q.county.fips);}
 else if(q.county?.name){where.push('upper(cz_name)=?');params.push(q.county.name);}
 if(q.type){where.push('upper(event_type)=?');params.push(q.type);}
 const clause=' FROM kfm_storm_event_details WHERE '+where.join(' AND ');
 return {
  rows:{sql:'SELECT '+COLUMNS.map(c=>`"${c}"`).join(',')+clause+` ORDER BY ${BEGIN} DESC, CAST(begin_time AS INTEGER) DESC, CAST(event_id AS INTEGER) DESC LIMIT ? OFFSET ?`,params:[...params,q.limit,q.offset]},
  count:{sql:'SELECT COUNT(*) AS n'+clause,params},
 };
}

const num=v=>v===null||v===undefined||v===''||!Number.isFinite(+v)?null:+v;
const str=v=>v===null||v===undefined||v===''?null:String(v);
function when(yearmonth,dayOfMonth,time,timezone){
 const ym=String(yearmonth??''),hhmm=String(time??'').padStart(4,'0');
 if(!/^\d{6}$/.test(ym)||!/^\d{4}$/.test(hhmm))return null;
 return {date:`${ym.slice(0,4)}-${ym.slice(4)}-${String(dayOfMonth).padStart(2,'0')}`,time:`${hhmm.slice(0,2)}:${hhmm.slice(2)}`,timezone:str(timezone)};
}
const place=(range,azimuth,name,lat,lon)=>({range:num(range),azimuth:str(azimuth),place:str(name),lat:num(lat),lon:num(lon)});

/** One public event from one database row (allow-listed fields only). */
export function stormEvent(r){
 const tornado=str(r.tor_f_scale)?{scale:str(r.tor_f_scale),lengthMiles:num(r.tor_length),widthYards:num(r.tor_width)}:null;
 return {
  eventId:num(r.event_id),episodeId:num(r.episode_id),type:str(r.event_type),
  area:{kind:{C:'county',Z:'zone',M:'marine'}[r.cz_type]??str(r.cz_type),fips:num(r.cz_fips),name:str(r.cz_name)},office:str(r.wfo),
  begin:when(r.begin_yearmonth,r.begin_day,r.begin_time,r.cz_timezone),end:when(r.end_yearmonth,r.end_day,r.end_time,r.cz_timezone),
  injuries:{direct:num(r.injuries_direct),indirect:num(r.injuries_indirect)},deaths:{direct:num(r.deaths_direct),indirect:num(r.deaths_indirect)},
  damage:{property:str(r.damage_property),crops:str(r.damage_crops)},magnitude:{value:num(r.magnitude),type:str(r.magnitude_type)},
  floodCause:str(r.flood_cause),category:num(r.category),tornado,
  location:{begin:place(r.begin_range,r.begin_azimuth,r.begin_location,r.begin_lat,r.begin_lon),end:place(r.end_range,r.end_azimuth,r.end_location,r.end_lat,r.end_lon)},
  source:str(r.source),narrative:{episode:str(r.episode_narrative),event:str(r.event_narrative)},dataSource:str(r.data_source),
 };
}
