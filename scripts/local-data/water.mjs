// National Water Model reaches and streamflow, and the pipeline's captured NWS alerts, USGS
// earthquakes and USGS streamflow readings. Owner approval for public release: 2026-11-01.
import {only,text,oneOf,minute,ordered,bbox,flag,int,page,num,str,fail} from './query.mjs';
import {gpkgToGeoJSON} from './gpkg.mjs';

const NWM_SOURCE=Object.freeze({provider:'NOAA Office of Water Prediction, National Water Model v3.1',url:'https://water.noaa.gov/about/nwm',
 coverage:'101,599 NWM v3.0 reaches in the Kansas envelope; the 2026-10-07 16Z analysis and short-range run, then one 12Z analysis a day',
 notes:'Model output, not gauge observations. The pipeline has not admitted this source, and the review of v3.0 reach geometry against v3.1 model output is pending; the owner approved public release on 2026-11-01 with these limitations. Streamflow and nudge in m3/s, velocity in m/s; values whose status is not valid are null. Reach geometry is WGS84 (EPSG:4326).'});

export const nwmReaches={
 id:'nwm-reaches',db:'nwm',title:'National Water Model reaches',source:NWM_SOURCE,
 indexes:[{name:'kfm_nwm_flowlines_feature',sql:'CREATE INDEX IF NOT EXISTS kfm_nwm_flowlines_feature ON nwm_v30_flowlines(feature_id)'},
  {name:'kfm_nwm_flowlines_huc6',sql:'CREATE INDEX IF NOT EXISTS kfm_nwm_flowlines_huc6 ON nwm_v30_flowlines(huc6)'}],
 params:{feature:'NWM feature id',name:'part of the stream name',huc6:'6-digit hydrologic unit',bbox:'west,south,east,north (2 degrees at most)',
  geometry:'1 to include each reach\'s line (at most 50)',limit:'1-200 (50); 1-50 (10) with geometry',offset:'0-100000'},
 parse(input){
  only(input,['feature','name','huc6','bbox','geometry','limit','offset']);
  const geometry=flag(input.geometry);
  const q={feature:text(input.feature,/^\d{1,12}$/),name:text(input.name,/^[A-Z0-9][A-Z0-9 .,'&/()#-]{1,39}$/),huc6:text(input.huc6,/^\d{6}$/),bbox:bbox(input.bbox),geometry,
   limit:int(input.limit,{min:1,max:geometry?50:200,fallback:geometry?10:50}),offset:int(input.offset,{min:0,max:100000,fallback:0})};
  if(!q.feature&&!q.name&&!q.huc6&&!q.bbox)throw fail();
  return q;
 },
 run(db,q){
  const where=[],params=[];let from='nwm_v30_flowlines t';
  if(q.bbox){from+=' JOIN rtree_nwm_v30_flowlines_geom r ON r.id=t.fid';where.push('r.maxx>=? AND r.minx<=? AND r.maxy>=? AND r.miny<=?');params.push(q.bbox.west,q.bbox.east,q.bbox.south,q.bbox.north);}
  if(q.feature){where.push('t.feature_id=?');params.push(q.feature);}
  if(q.huc6){where.push('t.huc6=?');params.push(q.huc6);}
  if(q.name){where.push('upper(t.name) LIKE ?');params.push('%'+q.name+'%');}
  const clause=' FROM '+from+' WHERE '+where.join(' AND ');
  const total=db.prepare('SELECT COUNT(*) AS n'+clause).get(...params).n;
  const rows=db.prepare('SELECT t.feature_id,t.name,t.strm_order,t.huc6,t.nwm_vers'+(q.geometry?',t.geom':'')+clause+' ORDER BY CAST(t.feature_id AS INTEGER) LIMIT ? OFFSET ?').all(...params,q.limit,q.offset)
   .map(r=>({featureId:num(r.feature_id),name:str(r.name),streamOrder:num(r.strm_order),huc6:str(r.huc6),nwmVersion:str(r.nwm_vers),...(q.geometry?{geometry:gpkgToGeoJSON(r.geom)}:{})}));
  return {total,rows};
 },
};

export const nwmStreamflow={
 id:'nwm-streamflow',db:'observations',title:'National Water Model streamflow',source:NWM_SOURCE,
 indexes:[{name:'kfm_nwm_channel_rt_feature',sql:'CREATE INDEX IF NOT EXISTS kfm_nwm_channel_rt_feature ON kfm_nwm_channel_rt(feature_id, valid_time)'}],
 params:{feature:'NWM feature id (required)',product:'analysis_assim or short_range (both by default)',from:'YYYY-MM-DDTHH:MM UTC (valid time)',to:'YYYY-MM-DDTHH:MM UTC',limit:'1-1000 (100)',offset:'0-100000'},
 parse(input){
  only(input,['feature','product','from','to','limit','offset']);
  const q={feature:text(input.feature,/^\d{1,12}$/,{required:true}),product:oneOf(input.product,['analysis_assim','short_range']),
   from:minute(input.from,'1700-01-01T00:00'),to:minute(input.to,'2100-12-31T23:59',{end:true}),...page(input,{max:1000,fallback:100})};
  ordered(q.from,q.to);return q;
 },
 run(db,q){
  const where=['feature_id=?','substr(valid_time,1,16) BETWEEN ? AND ?'],params=[+q.feature,q.from,q.to];
  if(q.product){where.push('product=?');params.push(q.product);}
  const clause=' FROM kfm_nwm_channel_rt WHERE '+where.join(' AND ');
  const total=db.prepare('SELECT COUNT(*) AS n'+clause).get(...params).n;
  const value=(v,status)=>status==='valid'?num(v):null;
  const rows=db.prepare('SELECT product,reference_time,valid_time,streamflow_m3s,streamflow_status,velocity_ms,velocity_status,nudge_m3s,nudge_status'+clause+' ORDER BY valid_time,product LIMIT ? OFFSET ?').all(...params,q.limit,q.offset)
   .map(r=>({product:r.product,referenceTime:str(r.reference_time),validTime:str(r.valid_time),
    streamflowM3s:value(r.streamflow_m3s,r.streamflow_status),velocityMs:value(r.velocity_ms,r.velocity_status),nudgeM3s:value(r.nudge_m3s,r.nudge_status),
    status:{streamflow:str(r.streamflow_status),velocity:str(r.velocity_status),nudge:str(r.nudge_status)}}));
  return {total,feature:+q.feature,rows};
 },
};

// Captured GeoJSON features: properties as the provider published them.
const feature=json=>{let f;try{f=JSON.parse(json);}catch{return null;}return {id:str(f?.id),geometry:f?.geometry??null,properties:f?.properties??{}};};
const CAPTURE=" FROM kfm_environmental_features WHERE source_id=?";

export const nwsAlerts={
 id:'nws-alerts',db:'observations',title:'Captured NWS alerts for Kansas',indexes:[],
 source:Object.freeze({temporalMode:'historical-capture',provider:'NOAA National Weather Service API',url:'https://api.weather.gov/alerts',coverage:'Kansas alerts captured hourly by the pipeline since October 2026',notes:'Properties as published by the NWS when captured; this is not a live alert feed. Cache state describes relay delivery, not alert validity; use the provider timestamps and current official warnings.'}),
 params:{event:'part of the event name, e.g. Fog',area:'part of the area description, e.g. Sedgwick',limit:'1-50 (20)',offset:'0-1000'},
 parse(input){only(input,['event','area','limit','offset']);const pattern=/^[A-Z0-9][A-Z0-9 .,'&/()-]{1,39}$/;return {event:text(input.event,pattern),area:text(input.area,pattern),...page(input,{max:50,fallback:20,maxOffset:1000})};},
 run(db,q){
  const where=[],params=['nws-alerts'];
  if(q.event){where.push("upper(json_extract(feature_json,'$.properties.event')) LIKE ?");params.push('%'+q.event+'%');}
  if(q.area){where.push("upper(json_extract(feature_json,'$.properties.areaDesc')) LIKE ?");params.push('%'+q.area+'%');}
  const clause=CAPTURE+where.map(w=>' AND '+w).join('');
  const total=db.prepare('SELECT COUNT(*) AS n'+clause).get(...params).n;
  const rows=db.prepare("SELECT feature_json"+clause+" ORDER BY json_extract(feature_json,'$.properties.sent') DESC LIMIT ? OFFSET ?").all(...params,q.limit,q.offset).map(r=>feature(r.feature_json)).filter(Boolean);
  return {total,rows};
 },
};

export const usgsEarthquakes={
 id:'usgs-earthquakes',db:'observations',title:'Captured USGS earthquakes in Kansas',indexes:[],
 source:Object.freeze({temporalMode:'historical-capture',provider:'USGS Earthquake Hazards Program',url:'https://earthquake.usgs.gov/fdsnws/event/1/',coverage:'Kansas events captured hourly by the pipeline since October 2026',notes:'Properties as published by the USGS when captured; time and updated are milliseconds since 1970. This is not a live earthquake feed; generatedAt and cache state describe relay delivery, not event freshness.'}),
 params:{limit:'1-50 (50)',offset:'0-1000'},
 parse(input){only(input,['limit','offset']);return page(input,{max:50,fallback:50,maxOffset:1000});},
 run(db,q){
  const total=db.prepare('SELECT COUNT(*) AS n'+CAPTURE).get('usgs-earthquakes').n;
  const rows=db.prepare("SELECT feature_json"+CAPTURE+" ORDER BY CAST(json_extract(feature_json,'$.properties.time') AS INTEGER) DESC LIMIT ? OFFSET ?").all('usgs-earthquakes',q.limit,q.offset).map(r=>feature(r.feature_json)).filter(Boolean);
  return {total,rows};
 },
};

const USGS_SOURCE=Object.freeze({temporalMode:'historical-capture',provider:'USGS Water Data API (continuous values)',url:'https://api.waterdata.usgs.gov/',coverage:'Kansas monitoring locations captured hourly by the pipeline since October 2026',
 notes:'Historical captures, not a live gauge feed. Most values are provisional (approval_status) and may be revised by the USGS. Times are UTC; generatedAt and cache state describe relay delivery, not observation freshness.'});
const SITE=/^USGS-\d{8,15}$/;

export const usgsStreamflowSites={
 id:'usgs-streamflow-sites',db:'observations',title:'Captured USGS streamflow sites',indexes:[],source:USGS_SOURCE,
 params:{limit:'1-500 (500)',offset:'0-1000'},
 parse(input){only(input,['limit','offset']);return page(input,{max:500,fallback:500,maxOffset:1000});},
 run(db,q){
  const sql="SELECT json_extract(feature_json,'$.properties.monitoring_location_id') AS site,COUNT(*) AS n,MIN(json_extract(feature_json,'$.properties.time')) AS first,MAX(json_extract(feature_json,'$.properties.time')) AS last,"
   +"group_concat(DISTINCT json_extract(feature_json,'$.properties.parameter_code')) AS parameters,MAX(json_extract(feature_json,'$.geometry')) AS geometry"+CAPTURE+" GROUP BY site ORDER BY site";
  const all=db.prepare(sql).all('usgs-streamflow').filter(r=>SITE.test(r.site??'')).map(r=>{
   let geometry=null;try{geometry=JSON.parse(r.geometry);}catch{}
   return {site:r.site,readings:r.n,first:str(r.first),last:str(r.last),parameters:String(r.parameters??'').split(',').filter(Boolean).sort(),geometry};
  });
  return {total:all.length,rows:all.slice(q.offset,q.offset+q.limit)};
 },
};

export const usgsStreamflow={
 id:'usgs-streamflow',db:'observations',title:'Captured USGS streamflow readings',indexes:[],source:USGS_SOURCE,
 params:{site:'monitoring location (required), e.g. USGS-07144100',parameter:'5-digit USGS parameter code, e.g. 00060 discharge',from:'YYYY-MM-DDTHH:MM UTC',to:'YYYY-MM-DDTHH:MM UTC',limit:'1-1000 (500)',offset:'0-100000'},
 parse(input){
  only(input,['site','parameter','from','to','limit','offset']);
  const q={site:text(input.site,SITE,{required:true}),parameter:text(input.parameter,/^\d{5}$/),from:minute(input.from,'1700-01-01T00:00'),to:minute(input.to,'2100-12-31T23:59',{end:true}),...page(input,{max:1000,fallback:500})};
  ordered(q.from,q.to);return q;
 },
 run(db,q){
  const where=["json_extract(feature_json,'$.properties.monitoring_location_id')=?","substr(json_extract(feature_json,'$.properties.time'),1,16) BETWEEN ? AND ?"],params=['usgs-streamflow',q.site,q.from,q.to];
  if(q.parameter){where.push("json_extract(feature_json,'$.properties.parameter_code')=?");params.push(q.parameter);}
  const clause=CAPTURE+where.map(w=>' AND '+w).join('');
  const total=db.prepare('SELECT COUNT(*) AS n'+clause).get(...params).n;
  const rows=db.prepare("SELECT feature_json"+clause+" ORDER BY json_extract(feature_json,'$.properties.time') LIMIT ? OFFSET ?").all(...params,q.limit,q.offset).map(r=>{
   const f=feature(r.feature_json),p=f?.properties??{};
   return {time:str(p.time),value:num(p.value),unit:str(p.unit_of_measure),parameter:str(p.parameter_code),statistic:str(p.statistic_id),approval:str(p.approval_status),qualifier:p.qualifier==='None'?null:str(p.qualifier),id:f?.id??null};
  });
  return {total,site:q.site,rows};
 },
};
