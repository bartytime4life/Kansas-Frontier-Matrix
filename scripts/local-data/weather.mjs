// Station weather datasets in observations.sqlite: GHCN-Daily, GHCNDEX extremes, ASOS 5-minute
// and IEM wind. Each answers one bounded question through an index named in `indexes`.
// Owner approval for public release: 2026-11-01. No dependencies.
import {only,text,int,oneOf,day,minute,ordered,bbox,list,page,num,str,reading,note} from './query.mjs';

const GHCN_STATION=/^[A-Z0-9]{11}$/;
const NAME=/^[A-Z0-9][A-Z0-9 .,'&/()#-]{0,39}$/;
const GHCN_URL='https://www.ncei.noaa.gov/pub/data/ghcn/daily/by_station/';
// Native GHCN-Daily units (readme.txt): scale to the public unit, or leave raw.
const GHCN_UNITS={PRCP:[0.1,'mm'],SNOW:[1,'mm'],SNWD:[1,'mm'],TMAX:[0.1,'degC'],TMIN:[0.1,'degC'],TAVG:[0.1,'degC'],TOBS:[0.1,'degC'],
 MDPR:[0.1,'mm'],DAPR:[1,'days'],WESF:[0.1,'mm'],WESD:[0.1,'mm'],AWND:[0.1,'m/s'],WSF2:[0.1,'m/s'],WSF5:[0.1,'m/s'],WSFG:[0.1,'m/s'],
 WDF2:[1,'deg'],WDF5:[1,'deg'],EVAP:[0.1,'mm'],MNPN:[0.1,'degC'],MXPN:[0.1,'degC'],TSUN:[1,'min'],PSUN:[1,'percent'],MDSF:[1,'mm'],DASF:[1,'days']};
const isoDay=n=>{const s=String(n);return /^\d{8}$/.test(s)?`${s.slice(0,4)}-${s.slice(4,6)}-${s.slice(6)}`:null;};
const ymd=s=>+s.replaceAll('-','');

const GHCN_SOURCE=Object.freeze({provider:'NOAA NCEI Global Historical Climatology Network - Daily (GHCN-Daily)',url:'https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily',
 coverage:'Kansas stations: station files archived on 2026-10-07, kept current since by NOAA\'s daily GHCN-Daily update files',notes:'Values are converted from GHCN native units where the unit is listed; raw holds the value as delivered. Flags are GHCN measurement, quality and source flags. updated marks a value that comes from a daily update file rather than the archived station file.'});

export const ghcnStations={
 id:'ghcn-stations',db:'observations',title:'GHCN-Daily stations',indexes:[],source:GHCN_SOURCE,
 params:{name:'part of the station name',bbox:'west,south,east,north',element:'only stations that report this element, e.g. TMAX',limit:'1-500 (100)',offset:'0-100000'},
 parse(input){
  only(input,['name','bbox','element','limit','offset']);
  return {name:text(input.name,NAME),bbox:bbox(input.bbox),element:text(input.element,/^[A-Z0-9]{4}$/),...page(input,{max:500,fallback:100})};
 },
 run(db,q){
  const where=[],params=[];
  if(q.name){where.push('upper(name) LIKE ?');params.push('%'+q.name+'%');}
  if(q.bbox){where.push('longitude BETWEEN ? AND ? AND latitude BETWEEN ? AND ?');params.push(q.bbox.west,q.bbox.east,q.bbox.south,q.bbox.north);}
  if(q.element){where.push("json_extract(metadata_json,'$.inventory_elements.'||?) IS NOT NULL");params.push(q.element);}
  const clause=' FROM kfm_ghcnd_stations'+(where.length?' WHERE '+where.join(' AND '):'');
  const total=db.prepare('SELECT COUNT(*) AS n'+clause).get(...params).n;
  const rows=db.prepare('SELECT station_id,name,latitude,longitude,elevation_m,metadata_json'+clause+' ORDER BY station_id LIMIT ? OFFSET ?').all(...params,q.limit,q.offset).map(r=>{
   let meta={};try{meta=JSON.parse(r.metadata_json??'{}');}catch{}
   const elements=Object.fromEntries(Object.entries(meta.inventory_elements??{}).map(([k,v])=>[k,{firstYear:num(v?.first_year),lastYear:num(v?.last_year)}]));
   return {id:r.station_id,name:str(r.name),lat:num(r.latitude),lon:num(r.longitude),elevationM:num(r.elevation_m),firstDate:isoDay(meta.first_date),elements};
  });
  return {total,rows};
 },
};

export const ghcnDaily={
 id:'ghcn-daily',db:'observations',title:'GHCN-Daily observations',source:GHCN_SOURCE,
 indexes:[{name:'kfm_ghcnd_daily_file_day',sql:'CREATE INDEX IF NOT EXISTS kfm_ghcnd_daily_file_day ON kfm_ghcnd_daily(file_id, observation_day)'}],
 params:{station:'GHCN station id (required), e.g. USW00003928',from:'YYYY-MM-DD',to:'YYYY-MM-DD',element:'comma list, e.g. TMAX,TMIN,PRCP',limit:'1-2000 (500)',offset:'0-100000'},
 parse(input){
  only(input,['station','from','to','element','limit','offset']);
  const q={station:text(input.station,GHCN_STATION,{required:true}),from:day(input.from,'1700-01-01'),to:day(input.to,'2100-12-31'),
   element:list(input.element,/^[A-Z0-9]{4}$/,10),...page(input,{max:2000,fallback:500})};
  ordered(q.from,q.to);return q;
 },
 run(db,q,{cache}){
  // The station's archived file, overlaid by NOAA's daily update files (kfm_ghcnd_daily_revisions,
  // written by the PC's ghcnd feed): the latest insert or update for a day and element replaces
  // the archived value, and a delete removes it.
  const file=db.prepare("SELECT file_id FROM kfm_sql_sources WHERE source_id='noaa-ghcnd' AND source_url=?").get(GHCN_URL+q.station+'.csv.gz');
  // Only a positive answer is remembered: the feed creates the table on its first run.
  if(!cache.get('ghcnd-revisions'))cache.set('ghcnd-revisions',!!db.prepare("SELECT 1 FROM sqlite_master WHERE name='kfm_ghcnd_daily_revisions'").get());
  const revisions=cache.get('ghcnd-revisions');
  if(!file&&!revisions)return {total:0,rows:[]};
  const elements=q.element?` AND element IN (${q.element.map(()=>'?').join(',')})`:'';
  const range=[ymd(q.from),ymd(q.to),...(q.element??[])];
  const cols='observation_day,element,raw_value,measurement_flag,quality_flag,source_flag,observation_time';
  const base=`SELECT ${cols},0 AS updated FROM kfm_ghcnd_daily d WHERE file_id=? AND observation_day BETWEEN ? AND ?${elements}`;
  const sql=revisions?`WITH rev AS (SELECT ${cols},action,ROW_NUMBER() OVER (PARTITION BY observation_day,element ORDER BY file_id DESC,row_number DESC) AS rn
    FROM kfm_ghcnd_daily_revisions WHERE station_id=? AND observation_day BETWEEN ? AND ?${elements}),
   merged AS (${base} AND NOT EXISTS (SELECT 1 FROM rev WHERE rev.observation_day=d.observation_day AND rev.element=d.element)
    UNION ALL SELECT ${cols},1 FROM rev WHERE rn=1 AND action<>'delete')`:`WITH merged AS (${base})`;
  const params=revisions?[q.station,...range,file?.file_id??-1,...range]:[file.file_id,...range];
  const total=db.prepare(sql+' SELECT COUNT(*) AS n FROM merged').get(...params).n;
  const rows=db.prepare(sql+` SELECT ${cols},updated FROM merged ORDER BY observation_day,element LIMIT ? OFFSET ?`).all(...params,q.limit,q.offset).map(r=>{
   const unit=GHCN_UNITS[r.element],raw=num(r.raw_value),missing=raw===-9999||raw===null;
   return {date:isoDay(r.observation_day),element:r.element,value:missing?null:unit?Math.round(raw*unit[0]*10)/10:raw,unit:unit?.[1]??null,raw,
    flags:{measurement:str(r.measurement_flag),quality:str(r.quality_flag),source:str(r.source_flag)},time:str(r.observation_time),updated:r.updated===1};
  });
  return {total,station:q.station,rows};
 },
};

const GHCNDEX_SOURCE=Object.freeze({provider:'NOAA NCEI GHCNDEX-STN (beta-20260919, from GHCN-Daily 3.34)',url:'https://www.ncei.noaa.gov/pub/data/ghcn/ghcndex/',
 coverage:'2,517 Kansas stations, 26 ETCCDI indices, 1857-2026',notes:'Beta product, values as delivered. period 1-12 is a month, 13 the year. Missing values (-99.9) are not stored.'});
export const GHCNDEX_INDICES=Object.freeze(['CDD','CSDI','CWD','DTR','FD','GSL','ID','PRCPTOT','R10mm','R20mm','R95p','R99p','Rx1day','Rx5day','SDII','SU','TN10p','TN90p','TNn','TNx','TR','TX10p','TX90p','TXn','TXx','WSDI']);

export const ghcndexIndices={
 id:'ghcndex-indices',db:'observations',title:'GHCNDEX index definitions',indexes:[],source:GHCNDEX_SOURCE,params:{},
 parse(input){only(input,[]);return {};},
 run(db){const rows=db.prepare('SELECT index_code AS code,definition,unit FROM kfm_ghcndex_indices ORDER BY index_code').all().map(r=>({...r}));return {total:rows.length,rows};},
};

export const ghcndex={
 id:'ghcndex',db:'observations',title:'GHCNDEX climate-extreme indices',source:GHCNDEX_SOURCE,
 indexes:[{name:'kfm_ghcndex_values_station',sql:'CREATE INDEX IF NOT EXISTS kfm_ghcndex_values_station ON kfm_ghcndex_values(station_id, index_code, year, period)'}],
 params:{station:'GHCN station id (required)',index:'one of the 26 index codes, e.g. TXx',from:'year',to:'year',period:'annual, or a month 1-12',limit:'1-2000 (500)',offset:'0-100000'},
 parse(input){
  only(input,['station','index','from','to','period','limit','offset']);
  const period=input.period===undefined||input.period===''?null:String(input.period).toLowerCase()==='annual'?13:int(input.period,{min:1,max:12});
  const q={station:text(input.station,GHCN_STATION,{required:true}),index:oneOf(input.index,GHCNDEX_INDICES),
   from:int(input.from,{min:1700,max:2100,fallback:1700}),to:int(input.to,{min:1700,max:2100,fallback:2100}),period,...page(input,{max:2000,fallback:500})};
  ordered(q.from,q.to);return q;
 },
 run(db,q){
  const where=['v.station_id=?','v.year BETWEEN ? AND ?'],params=[q.station,q.from,q.to];
  if(q.index){where.splice(1,0,'v.index_code=?');params.splice(1,0,q.index);}
  if(q.period){where.push('v.period=?');params.push(q.period);}
  const clause=' FROM kfm_ghcndex_values v JOIN kfm_ghcndex_indices i ON i.index_code=v.index_code WHERE '+where.join(' AND ');
  const total=db.prepare('SELECT COUNT(*) AS n'+clause).get(...params).n;
  const rows=db.prepare('SELECT v.index_code,v.year,v.period,v.value,i.unit'+clause+' ORDER BY v.index_code,v.year,v.period LIMIT ? OFFSET ?').all(...params,q.limit,q.offset)
   .map(r=>({index:r.index_code,year:r.year,period:r.period===13?'annual':r.period,value:num(r.value),unit:str(r.unit)}));
  return {total,station:q.station,rows};
 },
};

const ASOS_STATIONS=Object.freeze(['KCNK','KDDC','KGLD','KICT','KTOP']);
export const asosFiveMinute={
 id:'asos-5min',db:'observations',title:'ASOS 5-minute airport observations',
 source:Object.freeze({provider:'NOAA NCEI ASOS 5-minute data (TD-6401)',url:'https://www.ncei.noaa.gov/pub/data/asos-fivemin/',
  coverage:'Concordia KCNK, Dodge City KDDC, Goodland KGLD, Wichita KICT and Topeka KTOP, 2000 onward as backfilled; NCEI\'s TD-6401 archive ends in 2022',
  notes:'time is the TD-6401 local standard time stamp. Decoded values come only from unambiguous METAR tokens, otherwise null; raw is the line as delivered.'}),
 indexes:[{name:'kfm_asos_fivemin_station_time',sql:'CREATE INDEX IF NOT EXISTS kfm_asos_fivemin_station_time ON kfm_asos_fivemin(icao, local_time)'}],
 params:{station:'KCNK, KDDC, KGLD, KICT or KTOP (required)',from:'YYYY-MM-DDTHH:MM local standard time',to:'YYYY-MM-DDTHH:MM',limit:'1-2000 (288)',offset:'0-100000'},
 parse(input){
  only(input,['station','from','to','limit','offset']);
  const q={station:oneOf(input.station,ASOS_STATIONS,{required:true}),from:minute(input.from,'1700-01-01T00:00'),to:minute(input.to,'2100-12-31T23:59',{end:true}),...page(input,{max:2000,fallback:288})};
  ordered(q.from,q.to);return q;
 },
 run(db,q){
  const compact=s=>s.replace(/[-T:]/g,'');
  const params=[q.station,compact(q.from),compact(q.to)],clause=' FROM kfm_asos_fivemin WHERE icao=? AND local_time BETWEEN ? AND ?';
  const total=db.prepare('SELECT COUNT(*) AS n'+clause).get(...params).n;
  const rows=db.prepare('SELECT local_time,utc_ddhhmm,wind_direction,wind_knots,gust_knots,visibility_sm,temperature_c,dewpoint_c,altimeter_inhg,raw_line'+clause+' ORDER BY local_time LIMIT ? OFFSET ?').all(...params,q.limit,q.offset).map(r=>{
   const t=String(r.local_time);
   return {time:/^\d{12}$/.test(t)?`${t.slice(0,4)}-${t.slice(4,6)}-${t.slice(6,8)}T${t.slice(8,10)}:${t.slice(10)}`:null,utc:str(r.utc_ddhhmm),
    windDirection:str(r.wind_direction),windKnots:num(r.wind_knots),gustKnots:num(r.gust_knots),visibilityMiles:str(r.visibility_sm),
    temperatureC:num(r.temperature_c),dewpointC:num(r.dewpoint_c),altimeterInHg:num(r.altimeter_inhg),raw:str(r.raw_line)};
  });
  return {total,station:q.station,rows};
 },
};

const WIND_SOURCE=Object.freeze({provider:'Iowa Environmental Mesonet (IEM) ASOS/AWOS archive',url:'https://mesonet.agron.iastate.edu/request/download.phtml',
 coverage:'68 Kansas airport stations, 1932 onward, updated daily (readings for 2003-2026 are being backfilled a year at a time)',notes:'Speeds in knots, directions in degrees. IEM missing markers (M, None) are null, not zero. Identical readings captured in more than one export appear once.'});
const WIND_STATION=/^[A-Z0-9]{3,4}$/;

export const windStations={
 id:'wind-stations',db:'observations',title:'IEM wind stations',indexes:[],source:WIND_SOURCE,
 params:{name:'part of the station or county name',limit:'1-100 (100)',offset:'0-1000'},
 parse(input){only(input,['name','limit','offset']);return {name:text(input.name,NAME),...page(input,{max:100,fallback:100,maxOffset:1000})};},
 run(db,q){
  const all=db.prepare('SELECT station_id,metadata_json FROM kfm_wind_stations ORDER BY station_id').all().map(r=>{
   let m={};try{m=JSON.parse(r.metadata_json??'{}');}catch{}
   return {id:r.station_id,name:str(m.name),county:str(m.county),lat:num(m.latitude),lon:num(m.longitude),archiveBegin:str(m.catalog_archive_begin),archiveEnd:str(m.catalog_archive_end)};
  }).filter(s=>!q.name||`${s.name??''} ${s.county??''}`.toUpperCase().includes(q.name));
  return {total:all.length,rows:all.slice(q.offset,q.offset+q.limit)};
 },
};

export const windObservations={
 id:'wind-observations',db:'observations',title:'IEM wind observations',source:WIND_SOURCE,
 indexes:[{name:'kfm_wind_observations_station_time',sql:'CREATE INDEX IF NOT EXISTS kfm_wind_observations_station_time ON kfm_wind_observations(station_id, observed_at_utc)'}],
 params:{station:'station id (required), e.g. ICT',from:'YYYY-MM-DDTHH:MM UTC',to:'YYYY-MM-DDTHH:MM UTC',limit:'1-2000 (500)',offset:'0-100000'},
 parse(input){
  only(input,['station','from','to','limit','offset']);
  const q={station:text(input.station,WIND_STATION,{required:true}),from:minute(input.from,'1700-01-01T00:00'),to:minute(input.to,'2100-12-31T23:59',{end:true}),...page(input,{max:2000,fallback:500})};
  ordered(q.from,q.to);return q;
 },
 run(db,q){
  const params=[q.station,q.from.replace('T',' '),q.to.replace('T',' ')];
  const inner='SELECT DISTINCT observed_at_utc,direction_degrees,speed_knots,gust_knots,peak_gust_knots,peak_direction_degrees,peak_wind_time FROM kfm_wind_observations WHERE station_id=? AND observed_at_utc BETWEEN ? AND ?';
  const total=db.prepare(`SELECT COUNT(*) AS n FROM (${inner})`).get(...params).n;
  const rows=db.prepare(inner+' ORDER BY observed_at_utc LIMIT ? OFFSET ?').all(...params,q.limit,q.offset).map(r=>({
   time:/^\d{4}-\d{2}-\d{2} \d{2}:\d{2}/.test(r.observed_at_utc??'')?r.observed_at_utc.slice(0,16).replace(' ','T')+'Z':str(r.observed_at_utc),
   directionDeg:reading(r.direction_degrees),speedKnots:reading(r.speed_knots),gustKnots:reading(r.gust_knots),
   peakGustKnots:reading(r.peak_gust_knots),peakDirectionDeg:reading(r.peak_direction_degrees),peakTime:note(r.peak_wind_time)}));
  return {total,station:q.station,rows};
 },
};

export const windDaily={
 id:'wind-daily',db:'observations',title:'IEM daily wind summaries',source:WIND_SOURCE,
 indexes:[{name:'kfm_wind_daily_station_day',sql:'CREATE INDEX IF NOT EXISTS kfm_wind_daily_station_day ON kfm_wind_daily(station_id, observation_day)'}],
 params:{station:'station id (required)',from:'YYYY-MM-DD',to:'YYYY-MM-DD',limit:'1-2000 (366)',offset:'0-100000'},
 parse(input){
  only(input,['station','from','to','limit','offset']);
  const q={station:text(input.station,WIND_STATION,{required:true}),from:day(input.from,'1700-01-01'),to:day(input.to,'2100-12-31'),...page(input,{max:2000,fallback:366})};
  ordered(q.from,q.to);return q;
 },
 run(db,q){
  const inner='SELECT DISTINCT observation_day,average_knots,maximum_knots,gust_knots FROM kfm_wind_daily WHERE station_id=? AND observation_day BETWEEN ? AND ?',params=[q.station,q.from,q.to];
  const total=db.prepare(`SELECT COUNT(*) AS n FROM (${inner})`).get(...params).n;
  const rows=db.prepare(inner+' ORDER BY observation_day LIMIT ? OFFSET ?').all(...params,q.limit,q.offset)
   .map(r=>({date:str(r.observation_day),averageKnots:reading(r.average_knots),maximumKnots:reading(r.maximum_knots),gustKnots:reading(r.gust_knots)}));
  return {total,station:q.station,rows};
 },
};

