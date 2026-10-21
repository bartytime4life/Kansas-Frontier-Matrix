// Welcome scene timing and captions. Deliberately free of three.js so labels
// render before (or without) WebGL. Each scene loops over `duration` seconds;
// a beat's caption shows from its start time until the next beat.
export const SCENE_LABEL = 'Illustrative · synthetic terrain, not observations';

export const SCENE_CATALOG = Object.freeze({
 groundwater: { duration: 18, beats: [[0, 'Cut through the ground to reveal its layers'], [6, 'A second cut traces the saturated aquifer'], [12, 'Monitoring wells sample the water table']] },
 water: { duration: 16, beats: [[0, 'Stream gauges report flow at each station'], [5.5, 'Gauge readings set the direction water is drawn'], [11, 'A rising reading sends a surge downstream']] },
 agriculture: { duration: 16, beats: [[0, 'Soil moisture sweeps from dry to wet'], [5.5, 'Fields green up through the growing season'], [11, 'Rainfall passes and the moisture map responds']] },
 terrain: { duration: 18, beats: [[0, 'Elevation layers build the land surface'], [6, 'Sun angle and height reshape the hillshade'], [12, 'A colour ramp and contours map elevation']] },
 weather: { duration: 16, beats: [[0, 'Radar reflectivity drifts across the plains'], [5.5, 'Wind streamlines trace the flow aloft'], [11, 'Lightning flashes mark active cells']] },
 disaster: { duration: 20, beats: [[0, 'Flood water rises through a river valley'], [5, 'Fire detections send smoke downwind'], [10, 'A tornado tracks across the plains'], [15, 'Declared areas outline the affected counties']] },
 geology: { duration: 16, beats: [[0, 'Bedrock layers dip beneath the plains'], [5.5, 'A seismic event ripples through the strata'], [11, 'Stations record the arriving waves']] },
 ecology: { duration: 16, beats: [[0, 'Land-cover classes paint the landscape'], [5.5, 'Riparian corridors follow the water'], [11, 'Seasons shift the vegetation signal']] },
 engineering: { duration: 16, beats: [[0, 'Bridges span the mapped river crossings'], [5.5, 'Survey lines measure distance and grade'], [11, 'Drainage paths show where water collects']] },
 transport: { duration: 36, beats: [[0, '1860s · Trails, wagons and the first rails'], [5, '1880s–1900s · Rail reaches the county seats'], [10.5, '1910s–1920s · Model Ts and the first airmail'], [15.5, '1930s–1950s · Paved highways, trucks and propliners'], [21.5, '1956–1980s · The interstate and the jet age'], [27.5, '1990s–today · Freight, Amtrak, EVs and helicopters'], [33, 'Each era opened new places to reach']] },
 history: { duration: 36, beats: [[0, 'A cave mouth: a first step into daylight'], [6, 'A small encampment gathers around a fire'], [11.5, 'The encampment grows into a village'], [17, '1920s · A neighbourhood of homes and streetlights'], [23, 'Today · A city of towers'], [29, 'Imagined future · A vast city of light']] },
 land: { duration: 16, beats: [[0, 'Township and range lines grid the land'], [5.5, 'Sections subdivide each township'], [11, 'Survey references, not ownership, are shown']] },
 people: { duration: 16, beats: [[0, 'County outlines frame aggregate counts'], [5.5, 'Population rises as columns by county'], [11, 'Communities glow along the corridors']] },
 places: { duration: 16, beats: [[0, 'County boundaries trace the state'], [5.5, 'Watershed boundaries follow the drainage'], [11, 'Saved places pin an investigation']] },
 science: { duration: 16, beats: [[0, 'Monitoring stations sample the surface'], [5.5, 'A satellite swath scans the landscape'], [11, 'A model grid summarizes the field']] },
 sky: { duration: 18, beats: [[0, 'The sun arcs across the day'], [6, 'Shadows lengthen through twilight'], [12, 'Night-sky presentation fills the dark']] },
 evidence: { duration: 16, beats: [[0, 'Map layers separate into their sources'], [5.5, 'Each feature links to a citation'], [11, 'Dates and limits travel with the evidence']] },
});

export const SCENE_IDS = Object.freeze(Object.keys(SCENE_CATALOG));

/** Index of the beat showing at loop time `t` (seconds). */
export function beatIndex(id, t) {
 const beats = SCENE_CATALOG[id]?.beats || [];
 let index = 0;
 for (let i = 0; i < beats.length; i++) if (t >= beats[i][0]) index = i;
 return index;
}
export const beatTitle = (id, t) => SCENE_CATALOG[id]?.beats[beatIndex(id, t)]?.[1] || '';
