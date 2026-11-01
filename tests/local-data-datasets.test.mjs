import test from 'node:test';
import assert from 'node:assert/strict';
import {DatabaseSync} from 'node:sqlite';
import {mkdtemp,rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {newSecret,signRequest,RESPONSE_SIGNATURE_HEADER} from '../scripts/home-inference/signature.mjs';
import {createGateway} from '../scripts/local-data/gateway.mjs';
import {plannedIndexes} from '../scripts/local-data/indexes.mjs';
import {DATASETS,datasetCatalog} from '../scripts/local-data/datasets.mjs';
import {LOCAL_DATA_ROUTES} from '../scripts/local-data/protocol.mjs';
import {gpkgToGeoJSON} from '../scripts/local-data/gpkg.mjs';
import {prismGrid} from '../scripts/local-data/prism.mjs';
import {bbox,list,minute} from '../scripts/local-data/query.mjs';
import {localDataConfig,createLocalDataService} from '../server/local-data.mjs';

const SITE='https://kansasfrontiermatrix.com',secret=newSecret();

// GeoPackage geometry: GP header (little-endian, optional envelope) and little-endian WKB.
const u32=n=>{const b=Buffer.alloc(4);b.writeUInt32LE(n);return b;};
const f64=n=>{const b=Buffer.alloc(8);b.writeDoubleLE(n);return b;};
const xy=([x,y])=>Buffer.concat([f64(x),f64(y)]);
const wkb={
 point:p=>Buffer.concat([Buffer.from([1]),u32(1),xy(p)]),
 line:ps=>Buffer.concat([Buffer.from([1]),u32(2),u32(ps.length),...ps.map(xy)]),
 polygon:rings=>Buffer.concat([Buffer.from([1]),u32(3),u32(rings.length),...rings.flatMap(r=>[u32(r.length),...r.map(xy)])]),
 multiPolygon:polys=>Buffer.concat([Buffer.from([1]),u32(6),u32(polys.length),...polys.map(p=>wkb.polygon(p))]),
};
const gp=(body,{envelope=false}={})=>Buffer.concat([Buffer.from([0x47,0x50,0,envelope?0x03:0x01]),u32(4269),envelope?Buffer.alloc(32):Buffer.alloc(0),body]);
const square=(x,y,d=0.1)=>[[[x,y],[x+d,y],[x+d,y+d],[x,y+d],[x,y]]];

async function fixtures(t){
 const dir=await mkdtemp(join(tmpdir(),'kfm-local-datasets-'));t.after(()=>rm(dir,{recursive:true,force:true}));
 const obs=new DatabaseSync(join(dir,'observations.sqlite'));
 obs.exec(`
  CREATE TABLE kfm_storm_event_details(event_id TEXT);
  CREATE TABLE kfm_sql_sources(file_id INTEGER, source_id TEXT, source_path TEXT, source_url TEXT);
  INSERT INTO kfm_sql_sources VALUES(7,'noaa-ghcnd','x/USW00003928.csv.gz','https://www.ncei.noaa.gov/pub/data/ghcn/daily/by_station/USW00003928.csv.gz');
  CREATE TABLE kfm_ghcnd_stations(station_id TEXT,name TEXT,latitude REAL,longitude REAL,elevation_m REAL,metadata_json TEXT);
  INSERT INTO kfm_ghcnd_stations VALUES('USW00003928','WICHITA DWIGHT D EISENHOWER NAT AP',37.65,-97.43,407.2,'{"first_date":"19530101","inventory_elements":{"TMAX":{"first_year":1953,"last_year":2026},"PRCP":{"first_year":1953,"last_year":2026}}}'),
   ('US1KSSG0004','WICHITA 2.5 E',37.69,-97.29,410,'{"first_date":"20050101","inventory_elements":{"PRCP":{"first_year":2005,"last_year":2026}}}'),
   ('USC00140010','ABILENE',38.9,-97.2,350,'{}');
  CREATE TABLE kfm_ghcnd_daily(file_id INTEGER,row_number INTEGER,observation_day INTEGER,element TEXT,raw_value INTEGER,measurement_flag TEXT,quality_flag TEXT,source_flag TEXT,observation_time TEXT);
  INSERT INTO kfm_ghcnd_daily VALUES(7,1,20240101,'TMAX',56,'','','W','2400'),(7,2,20240101,'PRCP',127,'','','W','2400'),(7,3,20240102,'TMAX',-9999,'','','W',''),(7,4,20240102,'WT01',1,'','','W',''),(8,1,20240101,'TMAX',999,'','','W','');
  CREATE TABLE kfm_ghcndex_indices(index_code TEXT,definition TEXT,unit TEXT);
  INSERT INTO kfm_ghcndex_indices VALUES('TXx','Maximum daily maximum temperature','degC'),('CDD','Maximum consecutive dry days','days');
  CREATE TABLE kfm_ghcndex_values(station_id TEXT,index_code TEXT,year INTEGER,period INTEGER,value REAL,file_id INTEGER);
  INSERT INTO kfm_ghcndex_values VALUES('USW00003928','TXx',2023,13,41.1,1),('USW00003928','TXx',2023,7,40.5,1),('USW00003928','CDD',2023,13,30,1),('USW00003928','TXx',1999,13,39,1);
  CREATE TABLE kfm_asos_fivemin(file_id INTEGER,row_number INTEGER,wban TEXT,icao TEXT,local_time TEXT,utc_ddhhmm TEXT,wind_direction TEXT,wind_knots INTEGER,gust_knots INTEGER,visibility_sm TEXT,temperature_c INTEGER,dewpoint_c INTEGER,altimeter_inhg REAL,raw_line TEXT);
  INSERT INTO kfm_asos_fivemin VALUES(1,1,'03928','KICT','200001010000','010600Z','270',4,NULL,'10',3,-1,29.89,'KICT 010600Z 27004KT'),(1,2,'03928','KICT','200001010005','010605Z','VRB',2,NULL,'1 1/2',3,-1,29.89,'raw'),(1,3,'03928','KTOP','200001010000','010600Z','180',5,NULL,'10',1,-2,30.1,'raw');
  CREATE TABLE kfm_wind_stations(station_id TEXT,metadata_json TEXT);
  INSERT INTO kfm_wind_stations VALUES('ICT','{"name":"Wichita","county":"Sedgwick","latitude":"37.65","longitude":"-97.43","catalog_archive_begin":"1932-01-01","catalog_archive_end":""}'),('DDC','{"name":"Dodge City","county":"Ford","latitude":"37.76","longitude":"-99.97"}');
  CREATE TABLE kfm_wind_observations(file_id INTEGER,row_number INTEGER,station_id TEXT,observed_at_utc TEXT,direction_degrees TEXT,speed_knots TEXT,gust_knots TEXT,peak_gust_knots TEXT,peak_direction_degrees TEXT,peak_wind_time TEXT);
  INSERT INTO kfm_wind_observations VALUES(1,1,'ICT','2024-05-01 12:00','180.00','12.00','M','M','M','M'),(2,1,'ICT','2024-05-01 12:00','180.00','12.00','M','M','M','M'),(1,2,'ICT','2024-05-01 13:00','190.00','15.00','25.00','30.00','200.00','2024-05-01 12:41');
  CREATE TABLE kfm_wind_daily(file_id INTEGER,row_number INTEGER,station_id TEXT,observation_day TEXT,average_knots TEXT,maximum_knots TEXT,gust_knots TEXT);
  INSERT INTO kfm_wind_daily VALUES(1,1,'ICT','2024-05-01','8.5','15.0','None'),(1,2,'ICT','2024-05-02','6.0','11.0','20.0');
  CREATE TABLE kfm_prism_grids(grid_id INTEGER,source_path TEXT,unit TEXT,source_sha256 TEXT,source_bytes INTEGER,raster_path TEXT,processed_at TEXT,county_rows INTEGER,state TEXT);
  INSERT INTO kfm_prism_grids(grid_id,source_path,unit,state) VALUES
   (1,'time_series/us/an/4km/ppt/monthly/2023/prism_ppt_us_25m_202301.zip','Millimeters','complete'),
   (2,'time_series/us/an/4km/ppt/monthly/2023/prism_ppt_us_25m_202302.zip','Millimeters','complete'),
   (3,'time_series/us/an/4km/ppt/monthly/2023/prism_ppt_us_25m_2023.zip','Millimeters','complete'),
   (4,'normals/us/4km/ppt/monthly/prism_ppt_us_25m_202001_avg_30y.zip','Millimeters','complete'),
   (5,'prior_versions/ppt/daily_D1_201506/1981/PRISM_ppt_stable_4kmD1_19810101_bil.zip','Millimeters','complete'),
   (6,'something/else.zip','x','complete');
  CREATE TABLE kfm_prism_county_stats(grid_id INTEGER,county_geoid TEXT,county_name TEXT,mean REAL,minimum REAL,maximum REAL,valid_pixels INTEGER,quality_flag TEXT);
  INSERT INTO kfm_prism_county_stats VALUES(1,'20173','Sedgwick',20.5,10,30,75,''),(1,'20045','Douglas',40,30,50,60,''),(2,'20173','Sedgwick',25,12,33,75,''),(2,'20045','Douglas',35,20,44,60,''),(3,'20173','Sedgwick',800,700,900,75,''),(4,'20173','Sedgwick',22,20,24,75,'');
  CREATE TABLE kfm_nwm_channel_rt(feature_id INTEGER,product TEXT,filename_cycle_time TEXT,reference_time TEXT,valid_time TEXT,streamflow_m3s REAL,streamflow_packed INTEGER,streamflow_status TEXT,velocity_ms REAL,velocity_packed INTEGER,velocity_status TEXT,nudge_m3s REAL,nudge_packed INTEGER,nudge_status TEXT);
  INSERT INTO kfm_nwm_channel_rt VALUES(744183,'analysis_assim','c','2026-10-07T13:00:00Z','2026-10-07T16:00:00Z',1.5,0,'valid',0.3,0,'valid',0,0,'valid'),(744183,'short_range','c','2026-10-07T16:00:00Z','2026-10-07T17:00:00Z',-999,0,'missing',0.3,0,'valid',0,0,'valid');
  CREATE TABLE kfm_environmental_features(source_id TEXT,feature_sha256 TEXT,feature_id TEXT,feature_json TEXT);
 `);
 const add=obs.prepare('INSERT INTO kfm_environmental_features VALUES(?,?,?,?)');
 add.run('nws-alerts','a','A1',JSON.stringify({id:'A1',geometry:null,properties:{event:'Dense Fog Advisory',areaDesc:'Sedgwick; Butler',sent:'2026-10-27T19:24:00-05:00'}}));
 add.run('nws-alerts','b','A2',JSON.stringify({id:'A2',geometry:null,properties:{event:'Red Flag Warning',areaDesc:'Ford',sent:'2026-10-28T10:00:00-05:00'}}));
 add.run('usgs-earthquakes','c','Q1',JSON.stringify({id:'Q1',geometry:{type:'Point',coordinates:[-98.3,38.9]},properties:{mag:'2.7',time:'1792084734380',title:'M 2.7 - near Luray'}}));
 for(const [i,[site,time,value]] of [['USGS-07144100','2026-10-25T13:30:00+00:00','269'],['USGS-07144100','2026-10-25T13:45:00+00:00','270'],['USGS-06856600','2026-10-25T13:30:00+00:00','10']].entries())
  add.run('usgs-streamflow','s'+i,'F'+i,JSON.stringify({id:'F'+i,geometry:{type:'Point',coordinates:[-97.3,37.6]},properties:{monitoring_location_id:site,time,value,unit_of_measure:'ft^3/s',parameter_code:'00060',statistic_id:'00011',approval_status:'Provisional',qualifier:'None'}}));
 obs.close();

 const tiger=new DatabaseSync(join(dir,'tiger.gpkg'));
 const layer=(table,columns)=>tiger.exec(`CREATE TABLE "${table}"(fid INTEGER PRIMARY KEY,geom BLOB,${columns});CREATE VIRTUAL TABLE "rtree_${table}_geom" USING rtree(id,minx,maxx,miny,maxy);`);
 layer('us_county','STATEFP TEXT,COUNTYFP TEXT,GEOID TEXT,NAME TEXT,NAMELSAD TEXT,ALAND INTEGER');
 layer('us_state','GEOID TEXT,NAME TEXT');
 layer('ks_tabblock20','GEOID20 TEXT,COUNTYFP20 TEXT,NAME20 TEXT');
 layer('ks_tabblocksufx','GEOID TEXT,COUNTYFP TEXT,NAME TEXT');
 for(const t of ['ks_roads','ks_linearwater'])layer(t,'LINEARID TEXT,FULLNAME TEXT,kfm_source_file TEXT');
 layer('ks_areawater','HYDROID TEXT,FULLNAME TEXT,kfm_source_file TEXT');
 layer('ks_addrfeat','TLID INTEGER,FULLNAME TEXT,kfm_source_file TEXT');
 layer('ks_edges','TLID INTEGER,FULLNAME TEXT,COUNTYFP TEXT');
 layer('ks_faces','TFID INTEGER,COUNTYFP TEXT');
 const county=tiger.prepare('INSERT INTO us_county VALUES(?,?,?,?,?,?,?,?)'),box=tiger.prepare('INSERT INTO rtree_us_county_geom VALUES(?,?,?,?,?)');
 county.run(1,gp(wkb.polygon(square(-97.5,37.5))),'20','173','20173','Sedgwick','Sedgwick County',2600000000);box.run(1,-97.5,-97.4,37.5,37.6);
 county.run(2,gp(wkb.multiPolygon([square(-95.3,38.9),square(-95.1,38.9)]),{envelope:true}),'20','045','20045','Douglas','Douglas County',1100000000);box.run(2,-95.3,-95.0,38.9,39.0);
 const road=tiger.prepare('INSERT INTO ks_roads VALUES(?,?,?,?,?)');
 road.run(1,gp(wkb.line([[-97.45,37.55],[-97.44,37.56]])),'110','N Broadway','tl_2025_20173_roads.shp');
 road.run(2,gp(wkb.line([[-95.2,38.95],[-95.21,38.96]])),'111','Massachusetts St','tl_2025_20045_roads.shp');
 tiger.prepare('INSERT INTO rtree_ks_roads_geom VALUES(?,?,?,?,?)').run(1,-97.45,-97.44,37.55,37.56);
 tiger.prepare('INSERT INTO ks_edges VALUES(?,?,?,?,?)').run(1,gp(wkb.line([[-97.45,37.55],[-97.44,37.56]])),987654321,'N Broadway','173');
 tiger.close();

 const nwm=new DatabaseSync(join(dir,'nwm.gpkg'));
 nwm.exec('CREATE TABLE nwm_v30_flowlines(fid INTEGER PRIMARY KEY,geom BLOB,id TEXT,oid INTEGER,feature_id TEXT,name TEXT,strm_order INTEGER,huc6 TEXT,nwm_vers REAL);CREATE VIRTUAL TABLE rtree_nwm_v30_flowlines_geom USING rtree(id,minx,maxx,miny,maxy);');
 const reach=nwm.prepare('INSERT INTO nwm_v30_flowlines VALUES(?,?,?,?,?,?,?,?,?)');
 reach.run(1,gp(wkb.line([[-95.4,39.1],[-95.39,39.11]])),'744183',1,'744183','Delaware River',1,'102701',3.0);
 reach.run(2,gp(wkb.line([[-97.4,37.6],[-97.39,37.61]])),'744190',2,'744190','Arkansas River',5,'110300',3.0);
 nwm.prepare('INSERT INTO rtree_nwm_v30_flowlines_geom VALUES(?,?,?,?,?)').run(2,-97.4,-97.39,37.6,37.61);
 nwm.close();
 return {observations:join(dir,'observations.sqlite'),tiger:join(dir,'tiger.gpkg'),nwm:join(dir,'nwm.gpkg')};
}

function addIndexes(databases){
 for(const [name,indexes] of plannedIndexes()){const db=new DatabaseSync(databases[name]);for(const i of indexes.values())db.exec(i.sql);db.close();}
}

const gatewayFor=databases=>{
 const handle=createGateway({keyId:'gw',secret,databases});
 return (id,input={})=>{const path='/v1/data/'+id,body=JSON.stringify(input),a=handle({method:'POST',path,body,headers:signRequest({keyId:'gw',secret,method:'POST',path,body})});return {status:a.status,...JSON.parse(a.body)};};
};

test('every dataset has a relay route, a bounded parse and a public description',()=>{
 assert.equal(DATASETS.size,17);
 for(const id of DATASETS.keys())assert.equal(LOCAL_DATA_ROUTES.get('/v1/data/'+id),'POST');
 for(const d of datasetCatalog()){assert.match(d.path,/^\/api\/local-data\/[a-z0-9-]+$/);assert.ok(d.source.provider&&d.source.url&&d.title);}
 // Each dataset's recorded release limitation travels with its public source notes.
 const notes=id=>datasetCatalog().find(d=>d.id===id).source.notes;
 for(const id of ['nwm-reaches','nwm-streamflow'])assert.match(notes(id),/not admitted.*pending/);
 assert.match(notes('ghcndex'),/Beta product/);
 assert.match(notes('prism-county'),/acquisition dates are not yet verified/);
 // Unknown parameters are refused everywhere; so is a whole-state scan of a large layer.
 for(const d of DATASETS.values())assert.throws(()=>d.parse({nope:'1'}),{code:'QUERY_INVALID'},d.id);
 assert.throws(()=>DATASETS.get('tiger-features').parse({layer:'roads'}),{code:'QUERY_INVALID'});
 assert.throws(()=>DATASETS.get('tiger-features').parse({layer:'county',geometry:'1',limit:'21'}),{code:'QUERY_INVALID'});
 assert.throws(()=>DATASETS.get('nwm-reaches').parse({}),{code:'QUERY_INVALID'});
 assert.throws(()=>DATASETS.get('prism-county').parse({variable:'ppt'}),{code:'QUERY_INVALID'});
 assert.throws(()=>DATASETS.get('prism-county').parse({variable:'ppt',product:'normals'}),{code:'QUERY_INVALID'});
 assert.throws(()=>DATASETS.get('ghcn-daily').parse({station:"USW00003928' OR 1=1"}),{code:'QUERY_INVALID'});
 assert.deepEqual(DATASETS.get('prism-county').parse({variable:'PPT',county:'173',from:'2023',to:'2023-06'}),{variable:'ppt',county:'20173',step:'monthly',resolution:'4km',product:'an',from:'2023-01',to:'2023-06',limit:500,offset:0});
 assert.throws(()=>bbox('-100,37,-97,38'),{code:'QUERY_INVALID'});
 assert.deepEqual(bbox('-97.5,37.5,-97.2,37.8'),{west:-97.5,south:37.5,east:-97.2,north:37.8});
 assert.throws(()=>list('A,B,C',/^[A-Z]$/,2),{code:'QUERY_INVALID'});
 assert.equal(minute('2024-05-01',null,{end:true}),'2024-05-01T23:59');
 assert.throws(()=>minute('2024-05-01T24:00'),{code:'QUERY_INVALID'});
});

test('PRISM grid paths name their product, resolution, variable and period',()=>{
 assert.deepEqual(prismGrid('time_series/us/an/800m/tmax/daily/1981/prism_tmax_us_30s_19810102.zip'),{product:'an',resolution:'800m',variable:'tmax',step:'daily',period:'1981-01-02'});
 assert.deepEqual(prismGrid('time_series/us/lt/800m/ppt/monthly/1895/prism_ppt_us_30s_1895.zip'),{product:'lt',resolution:'800m',variable:'ppt',step:'annual',period:'1895'});
 assert.deepEqual(prismGrid('normals/us/4km/tmin/daily/prism_tmin_us_25m_20200229_avg_30y.zip'),{product:'normals',resolution:'4km',variable:'tmin',step:'daily',period:'02-29'});
 assert.deepEqual(prismGrid('normals/us/800m/soltotal/monthly/prism_soltotal_us_30s_2020_avg_30y.zip'),{product:'normals',resolution:'800m',variable:'soltotal',step:'annual',period:'annual'});
 assert.equal(prismGrid('time_series/us/an/4km/ppt/daily/1981/prism_tmax_us_25m_19810101.zip'),null);
});

test('GeoPackage geometry decodes to rounded GeoJSON and refuses anything else',()=>{
 assert.deepEqual(gpkgToGeoJSON(gp(wkb.point([-97.123456789,37.5]))),{type:'Point',coordinates:[-97.123457,37.5]});
 assert.deepEqual(gpkgToGeoJSON(gp(wkb.multiPolygon([square(0,0,1)]),{envelope:true})).coordinates[0][0][2],[1,1]);
 assert.equal(gpkgToGeoJSON(null),null);
 assert.throws(()=>gpkgToGeoJSON(Buffer.from('not a geometry')),{code:'GEOMETRY_INVALID'});
 assert.throws(()=>gpkgToGeoJSON(gp(wkb.point([0,0])).subarray(0,20)),{code:'GEOMETRY_INVALID'});
});

test('datasets that need an index are refused until it exists, then answer through it',async t=>{
 const databases=await fixtures(t),ask=gatewayFor(databases);
 assert.deepEqual(ask('ghcn-daily',{station:'USW00003928'}),{status:503,gateway:'kfm-local-data/1',error:'DATASET_NOT_READY'});
 assert.equal(ask('tiger-features',{layer:'county'}).status,503);
 // Index-free datasets answer at once.
 assert.equal(ask('ghcn-stations',{name:'wichita'}).total,2);
 addIndexes(databases);

 const daily=ask('ghcn-daily',{station:'USW00003928',from:'2024-01-01',to:'2024-01-02'});
 assert.equal(daily.status,200);assert.equal(daily.format,'kfm-local-data-v1');assert.equal(daily.total,4);
 assert.deepEqual(daily.rows.slice(0,2),[
  {date:'2024-01-01',element:'PRCP',value:12.7,unit:'mm',raw:127,flags:{measurement:null,quality:null,source:'W'},time:'2400',updated:false},
  {date:'2024-01-01',element:'TMAX',value:5.6,unit:'degC',raw:56,flags:{measurement:null,quality:null,source:'W'},time:'2400',updated:false}]);
 assert.deepEqual(daily.rows.slice(2).map(r=>[r.element,r.value,r.unit]),[['TMAX',null,'degC'],['WT01',1,null]]);
 assert.equal(ask('ghcn-daily',{station:'USW00003928',element:'tmax'}).total,2);
 assert.equal(ask('ghcn-daily',{station:'USC00140010'}).total,0);

 const stations=ask('ghcn-stations',{bbox:'-97.5,37.5,-97.2,37.8',element:'TMAX'});
 assert.deepEqual(stations.rows.map(r=>[r.id,r.firstDate,r.elements.TMAX]),[['USW00003928','1953-01-01',{firstYear:1953,lastYear:2026}]]);

 assert.deepEqual(ask('ghcndex',{station:'USW00003928',index:'txx',from:'2000',period:'annual'}).rows,[{index:'TXx',year:2023,period:'annual',value:41.1,unit:'degC'}]);
 assert.equal(ask('ghcndex',{station:'USW00003928',period:'7'}).rows[0].period,7);
 assert.equal(ask('ghcndex-indices').total,2);

 const asos=ask('asos-5min',{station:'kict',from:'2000-01-01T00:00',to:'2000-01-01T00:05'});
 assert.equal(asos.total,2);assert.equal(asos.rows[1].time,'2000-01-01T00:05');assert.equal(asos.rows[1].visibilityMiles,'1 1/2');

 assert.deepEqual(ask('wind-stations',{name:'sedgwick'}).rows.map(r=>[r.id,r.lat]),[['ICT',37.65]]);
 const wind=ask('wind-observations',{station:'ICT',from:'2024-05-01',to:'2024-05-01'});
 // The same reading captured in two exports appears once; IEM 'M' is missing, not zero.
 assert.equal(wind.total,2);
 assert.deepEqual(wind.rows[0],{time:'2024-05-01T12:00Z',directionDeg:180,speedKnots:12,gustKnots:null,peakGustKnots:null,peakDirectionDeg:null,peakTime:null});
 assert.equal(wind.rows[1].peakTime,'2024-05-01 12:41');
 assert.deepEqual(ask('wind-daily',{station:'ICT'}).rows.map(r=>r.gustKnots),[null,20]);

 const prism=ask('prism-county',{variable:'ppt',county:'sedgwick',from:'2023-01',to:'2023-12'});
 assert.deepEqual(prism.rows.map(r=>[r.period,r.mean,r.unit]),[['2023-01',20.5,'Millimeters'],['2023-02',25,'Millimeters']]);
 assert.equal(prism.total,2);assert.deepEqual(prism.county,{geoid:'20173',name:'Sedgwick'});
 assert.deepEqual(ask('prism-county',{variable:'ppt',from:'2023-01',to:'2023-01'}).rows.map(r=>r.county.geoid),['20045','20173']);
 assert.deepEqual(ask('prism-county',{variable:'ppt',county:'173',step:'annual'}).rows.map(r=>[r.period,r.mean]),[['2023',800]]);
 assert.deepEqual(ask('prism-county',{variable:'ppt',county:'20173',product:'normals'}).rows.map(r=>r.period),['01']);

 const counties=ask('tiger-features',{layer:'county',name:'sedg',geometry:'1'});
 assert.equal(counties.total,1);assert.equal(counties.rows[0].id,'20173');assert.equal(counties.rows[0].attributes.ALAND,2600000000);
 assert.equal('fid' in counties.rows[0].attributes||'geom' in counties.rows[0].attributes,false);
 assert.deepEqual(counties.rows[0].geometry.coordinates[0][1],[-97.4,37.5]);
 assert.equal(ask('tiger-features',{layer:'county',id:'20045',geometry:'1'}).rows[0].geometry.type,'MultiPolygon');
 assert.equal('geometry' in ask('tiger-features',{layer:'county'}).rows[0],false);
 assert.deepEqual(ask('tiger-features',{layer:'roads',county:'45'}).rows.map(r=>r.name),['Massachusetts St']);
 assert.deepEqual(ask('tiger-features',{layer:'roads',bbox:'-97.5,37.5,-97.4,37.6'}).rows.map(r=>r.id),['110']);
 assert.deepEqual(ask('tiger-features',{layer:'edges',id:'987654321'}).rows.map(r=>[r.id,r.name]),[['987654321','N Broadway']]);

 assert.deepEqual(ask('nwm-reaches',{name:'river',geometry:'1'}).rows.map(r=>[r.featureId,r.geometry.type]),[[744183,'LineString'],[744190,'LineString']]);
 assert.deepEqual(ask('nwm-reaches',{bbox:'-97.5,37.5,-97.3,37.7'}).rows.map(r=>r.featureId),[744190]);
 const flow=ask('nwm-streamflow',{feature:'744183'});
 assert.deepEqual(flow.rows.map(r=>[r.product,r.streamflowM3s,r.status.streamflow]),[['analysis_assim',1.5,'valid'],['short_range',null,'missing']]);

 assert.deepEqual(ask('nws-alerts',{area:'sedgwick'}).rows.map(r=>r.properties.event),['Dense Fog Advisory']);
 assert.deepEqual(ask('nws-alerts').rows.map(r=>r.id),['A2','A1']);
 assert.equal(ask('usgs-earthquakes').rows[0].geometry.type,'Point');
 assert.deepEqual(ask('usgs-streamflow-sites').rows.map(r=>[r.site,r.readings]),[['USGS-06856600',1],['USGS-07144100',2]]);
 const gauge=ask('usgs-streamflow',{site:'USGS-07144100',from:'2026-10-25T13:40'});
 assert.deepEqual(gauge.rows,[{time:'2026-10-25T13:45:00+00:00',value:270,unit:'ft^3/s',parameter:'00060',statistic:'00011',approval:'Provisional',qualifier:null,id:'F1'}]);
});

test('the website serves the catalog itself and maps PC answers for any dataset',async t=>{
 const databases=await fixtures(t);addIndexes(databases);
 const handle=createGateway({keyId:'gw',secret,databases:{observations:databases.observations}});
 const config=localDataConfig({KFM_LOCAL_DATA:'1',KFM_LOCAL_DATA_ORIGIN:SITE,KFM_LOCAL_DATA_GATEWAY_KEY_ID:'gw',KFM_LOCAL_DATA_GATEWAY_SECRET:secret,KFM_LOCAL_DATA_WORKER_KEY_ID:'wk',KFM_LOCAL_DATA_WORKER_SECRET:newSecret()});
 // The relay stood in by the gateway itself: signed like a lease, answered like a worker report.
 const trips=[];
 const relay={lastSeen:Date.now(),handler:async()=>new Response(null,{status:204}),async submit({method,path,body}){
  trips.push([path,JSON.parse(body)]);
  const requestHeaders={...signRequest({keyId:'gw',secret,method,path,body}),'content-type':'application/json'};
  const a=handle({method,path,headers:requestHeaders,body});
  return {status:a.status,bytes:a.body,requestHeaders,headers:new Headers({'content-type':'application/json',[RESPONSE_SIGNATURE_HEADER]:a.signature})};
 }};
 const service=createLocalDataService({config,relay});
 const get=(id,query='')=>service.query(new Request(`${SITE}/api/local-data/${id}?${query}`),id);

 const catalog=await (await service.catalog(new Request(SITE+'/api/local-data'))).json();
 assert.equal(catalog.online,true);assert.equal(catalog.datasets.length,17);assert.equal(trips.length,0);

 const daily=await get('ghcn-daily','station=usw00003928&element=PRCP');
 assert.equal(daily.status,200);const body=await daily.json();
 assert.equal(body.cache.state,'live');assert.equal(body.rows[0].value,12.7);assert.equal('gateway' in body,false);
 // The PC receives the visitor's own parameters and validates them again.
 assert.deepEqual(trips[0],['/v1/data/ghcn-daily',{station:'usw00003928',element:'PRCP'}]);
 assert.equal((await (await get('ghcn-daily','element=PRCP&station=USW00003928')).json()).cache.state,'fresh');

 assert.equal((await get('no-such-dataset')).status,404);
 assert.equal((await get('ghcn-daily','station=bad')).status,400);
 // This gateway has no TIGER database: the visitor sees an offline answer, never a scan or an error page.
 const missing=await get('tiger-features','layer=county');
 assert.equal(missing.status,503);assert.equal((await missing.json()).reasonCode,'LOCAL_DATA_UNAVAILABLE');
 assert.equal(trips.length,2);
});

test('daily feeds show through: GHCN revisions overlay the archive, a revised PRISM grid replaces its period, NWM takes a time range',async t=>{
 const databases=await fixtures(t);addIndexes(databases);
 const ask=gatewayFor(databases);
 // Without the feed's table the archive is served as before.
 assert.deepEqual(ask('ghcn-daily',{station:'USW00003928',from:'2024-01-01',to:'2024-01-02'}).rows.map(r=>[r.element,r.raw,r.updated]),
  [['PRCP',127,false],['TMAX',56,false],['TMAX',-9999,false],['WT01',1,false]]);
 const db=new DatabaseSync(databases.observations);
 db.exec(`CREATE TABLE kfm_ghcnd_daily_revisions(station_id TEXT NOT NULL,observation_day INTEGER NOT NULL,element TEXT NOT NULL,file_id INTEGER NOT NULL,
  row_number INTEGER NOT NULL,action TEXT NOT NULL,raw_value INTEGER NOT NULL,measurement_flag TEXT NOT NULL,quality_flag TEXT NOT NULL,source_flag TEXT NOT NULL,
  observation_time TEXT NOT NULL,PRIMARY KEY(station_id,observation_day,element,file_id,row_number)) WITHOUT ROWID;
  INSERT INTO kfm_ghcnd_daily_revisions VALUES
   ('USW00003928',20240101,'PRCP',90,1,'update',130,'','','W','2400'),
   ('USW00003928',20240101,'PRCP',91,1,'update',140,'','','W','2400'),
   ('USW00003928',20240102,'WT01',91,2,'delete',1,'','','W',''),
   ('USW00003928',20240103,'TMAX',91,3,'insert',61,'','','W','2400'),
   ('US1KSNE0001',20240103,'PRCP',91,4,'insert',5,'','','N','');
  INSERT INTO kfm_prism_grids(grid_id,source_path,unit,state) VALUES (7,'time_series/us/an/4km/ppt/monthly/2023/prism_ppt_us_25m_202301.zip#sha256=0123456789ab','Millimeters','complete');
  INSERT INTO kfm_prism_county_stats VALUES (7,'20173','Sedgwick',21.5,10,31,75,'');
  INSERT INTO kfm_nwm_channel_rt VALUES (744183,'analysis_assim','c','2026-10-31T09:00:00Z','2026-10-31T12:00:00Z',2.5,250,'valid',0.4,40,'valid',0,0,'valid');`);
 db.close();
 const fresh=gatewayFor(databases);
 const daily=fresh('ghcn-daily',{station:'USW00003928',from:'2024-01-01',to:'2024-01-03'});
 // The newest update wins, a delete removes, an insert adds; the archive fills the rest.
 assert.deepEqual(daily.rows.map(r=>[r.date,r.element,r.raw,r.updated]),
  [['2024-01-01','PRCP',140,true],['2024-01-01','TMAX',56,false],['2024-01-02','TMAX',-9999,false],['2024-01-03','TMAX',61,true]]);
 assert.equal(daily.total,4);
 assert.deepEqual(fresh('ghcn-daily',{station:'US1KSNE0001'}).rows.map(r=>[r.date,r.value]),[['2024-01-03',0.5]]);
 assert.deepEqual(fresh('prism-county',{variable:'ppt',county:'173',from:'2023-01',to:'2023-02'}).rows.map(r=>[r.period,r.mean]),[['2023-01',21.5],['2023-02',25]]);
 const flow=fresh('nwm-streamflow',{feature:'744183',from:'2026-10-31',to:'2026-10-31'});
 assert.deepEqual(flow.rows.map(r=>[r.validTime,r.streamflowM3s]),[['2026-10-31T12:00:00Z',2.5]]);
 assert.equal(fresh('nwm-streamflow',{feature:'744183'}).total,3);
 assert.throws(()=>DATASETS.get('nwm-streamflow').parse({feature:'1',limit:'1001'}),{code:'QUERY_INVALID'});
});
