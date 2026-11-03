import type { TopicId } from './layer-workspaces';
import { RECOVERED_COLLECTIONS, recoveredMapId, recoveredTopics } from './recovered-collections';

export type ArchiveLayer = Readonly<{
  id: string; title: string; dataset: string; topics: readonly TopicId[];
  kind: 'tiger' | 'stations' | 'wind' | 'storms' | 'alerts' | 'earthquakes' | 'water' | 'reaches' | 'prism' | 'recovered';
  reference?: string; color: string; note: string; provider: string; sourceUrl: string;
}>;
const tiger: readonly [string, string, readonly TopicId[]][] = [
  ['state','State boundary',['places','government']], ['county','County boundaries',['places','government','people']],
  ['county-subdivision','County subdivisions',['places','government']], ['place','Cities and Census places',['places','people']],
  ['consolidated-city','Consolidated cities',['places','government']], ['tract','Census tracts',['people','places']],
  ['block-group','Census block groups',['people','places']], ['block','2020 Census blocks',['people','places']],
  ['block-suffix','Census block suffix areas',['places']], ['zcta','ZIP Code tabulation areas',['places','people']],
  ['school-district','Unified school districts',['government','people']], ['state-house','State House districts',['government']],
  ['state-senate','State Senate districts',['government']], ['congressional-district','119th Congress districts',['government']],
  ['puma','Public Use Microdata Areas',['people']], ['tribal-area','American Indian / Alaska Native / Hawaiian areas',['places','government']],
  ['tribal-subdivision','Tribal subdivisions',['places','government']], ['tribal-tract','Tribal Census tracts',['places','people']],
  ['tribal-block-group','Tribal Census block groups',['places','people']], ['cbsa','Core based statistical areas',['people','places']],
  ['csa','Combined statistical areas',['people','places']], ['urban-area','2020 urban areas',['people','places']],
  ['military','Military installation reference areas',['government','land']], ['area-landmark','Area landmarks',['places']],
  ['point-landmark','Point landmarks',['places']], ['primary-roads','Primary road references',['transport','engineering']],
  ['primary-secondary-roads','Primary and secondary roads',['transport','engineering']], ['rails','Rail references',['transport','engineering']],
  ['roads','Local road references',['transport','engineering']], ['area-water','Waterbody reference areas',['water','ecology']],
  ['linear-water','Waterway reference lines',['water','ecology']], ['address-ranges','Address-range reference lines',['places']],
  ['edges','Topological edges',['places','evidence']], ['faces','Topological faces',['places','evidence']],
];
const layer = (id: string, title: string, dataset: string, kind: ArchiveLayer['kind'], topics: readonly TopicId[], color: string, provider: string, sourceUrl: string, note: string): ArchiveLayer =>
  ({ id: `archive-${id}`, title, dataset, kind, topics, color, provider, sourceUrl, note });
export const ARCHIVE_LAYERS: readonly ArchiveLayer[] = [
  ...RECOVERED_COLLECTIONS.filter(c=>c.geometry).map((c): ArchiveLayer=>({id:recoveredMapId(c.id),title:`${c.title} · archive records`,dataset:`recovered-${c.database}`,kind:'recovered',reference:c.id,topics:recoveredTopics(c.id),color:'#c7b5e8',provider:c.id.includes('-osm-')?'© OpenStreetMap contributors · ODbL':'Archived source geometry',sourceUrl:c.id.includes('-osm-')?'https://www.openstreetmap.org/copyright':`/data-library?collection=${c.id}`,note:'Draws original geometry from loaded record pages, not every feature in the current map area. Load more or browse the full collection. Source dates, accuracy and attributes remain attached; historical records are not current conditions.'})),
  ...tiger.map(([reference,title,topics]): ArchiveLayer => ({...layer(`tiger-${reference}`,`${title} · Census 2025`,'tiger-features','tiger',topics,'#e8c784','U.S. Census Bureau · TIGER/Line 2025','https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html','Reference geography, not legal boundaries, ownership, navigation or population counts. NAD83 coordinates; nearby features may extend beyond Kansas. 2020 statistical areas retain their stated vintage.'),reference})),
  layer('ghcn','Weather station archive','ghcn-stations','stations',['weather','agriculture','science','history'],'#7ad5c0','NOAA NCEI · GHCN-Daily','https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily','Station locations, not a continuous weather surface. Daily observations and climate indices are available by station; missing and quality-flagged readings remain distinct.'),
  layer('wind','Airport weather archive','wind-stations','wind',['weather','aviation','science','history'],'#ddb1f3','Iowa Environmental Mesonet','https://mesonet.agron.iastate.edu/request/download.phtml','Archived station locations and readings; not live aviation weather. Wind uses knots and UTC. NCEI five-minute records use local standard time and a separate coverage period.'),
  layer('storms','Historical storm event locations','storm-events','storms',['weather','disaster','history','science'],'#f4ad78','NOAA NCEI · Storm Events','https://www.ncei.noaa.gov/stormevents/','Only reported begin locations are plotted. A point is not a storm footprint or tornado path. Events without valid coordinates remain in the record list; times retain the provider time zone.'),
  layer('alerts','Captured warning areas','nws-alerts','alerts',['weather','disaster','history'],'#ec9eac','NOAA National Weather Service','https://api.weather.gov/alerts','Historical captures, not current warnings. Only provider-supplied polygons are drawn; alerts without polygons are not assigned invented areas.'),
  layer('earthquakes','Captured earthquake locations','usgs-earthquakes','earthquakes',['geology','disaster','science','history'],'#eda87b','U.S. Geological Survey','https://earthquake.usgs.gov/fdsnws/event/1/','Captured earthquake locations with their event times; not a live earthquake feed. Epicentres do not represent shaking footprints.'),
  layer('water','Stream gauge archive','usgs-streamflow-sites','water',['water','weather','science','history'],'#7ccef5','U.S. Geological Survey','https://api.waterdata.usgs.gov/','Monitoring locations and retained readings, not current river flow. Values retain parameter, unit, qualifier and approval status.'),
  layer('reaches','NWM v3.0 river references','nwm-reaches','reaches',['water','science'],'#8fcbd7','NOAA Office of Water Prediction','https://water.noaa.gov/about/nwm','Reference lines only. The stored v3.1 model values are not painted on v3.0 geometry: their correspondence has not been verified.'),
  layer('prism','County climate · PRISM monthly','prism-county','prism',['weather','agriculture','water','science'],'#88b8ed','PRISM Group · Oregon State University','https://prism.oregonstate.edu/','Modelled county summaries of grid-cell centres, not station readings or area-weighted means. One explicit month and variable; missing values have no fill. County geography is TIGER 2025.'),
];
export const archiveLayer = (id: string) => ARCHIVE_LAYERS.find(layer => layer.id === id);
export const normalizeArchiveSelection = (values: readonly string[]) => [...new Set(values.filter(id => archiveLayer(id)))];
/** Every public SQL endpoint has a named use or a specific spatial hold. */
export const ARCHIVE_DATASET_USES = {
  'recovered-observations':'all allowlisted observation collections: records, original geometry pages and source provenance',
  'recovered-bulk':'all allowlisted bulk collections: records, original geometry pages and source provenance',
  'tiger-features':'34 reference layers and county joins', 'ghcn-stations':'station points', 'ghcn-daily':'station readings',
  'ghcndex-indices':'climate-index definitions', ghcndex:'station climate indices', 'wind-stations':'airport station points',
  'wind-observations':'station wind readings', 'wind-daily':'daily station summaries', 'asos-5min':'five named airports, joined by exact station identifier',
  'storm-events':'reported begin locations and unlocated record list', 'nws-alerts':'historical provider polygons', 'usgs-earthquakes':'captured epicentres',
  'usgs-streamflow-sites':'gauge locations', 'usgs-streamflow':'gauge readings', 'prism-county':'dated county climate summaries',
  'nwm-reaches':'v3.0 reference geometry', 'nwm-streamflow':'spatial hold: v3.1 values / v3.0 geometry correspondence unverified',
} as const;
