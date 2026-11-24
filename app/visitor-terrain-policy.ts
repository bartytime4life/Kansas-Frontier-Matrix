export type TerrainResourceMode='automatic'|'lightweight';
export const TERRAIN_LIGHT_FRAME_PIXELS=1_048_576;
export const TERRAIN_NORMAL_FRAME_PIXELS=4_194_304;
export const TERRAIN_RESOURCE_MODE_KEY='kfm.terrain.resources.v1';
type Hints={deviceMemory?:number;hardwareConcurrency?:number;saveData?:boolean};
export function visitorTerrainPolicy(hints:Hints={}){
 const low=!Number.isFinite(hints.deviceMemory)||hints.deviceMemory!<=4||!Number.isFinite(hints.hardwareConcurrency)||hints.hardwareConcurrency!<=4||hints.saveData===true;
 return {lightweight:low,framePixelLimit:low?TERRAIN_LIGHT_FRAME_PIXELS:TERRAIN_NORMAL_FRAME_PIXELS};
}
export function browserTerrainPolicy(){
 if(typeof navigator==='undefined')return visitorTerrainPolicy();
 const hints=navigator as Navigator&{deviceMemory?:number;connection?:{saveData?:boolean}};
 return visitorTerrainPolicy({deviceMemory:hints.deviceMemory,hardwareConcurrency:hints.hardwareConcurrency,saveData:hints.connection?.saveData});
}
export function readTerrainResourceMode():TerrainResourceMode{try{return globalThis.localStorage?.getItem(TERRAIN_RESOURCE_MODE_KEY)==='lightweight'?'lightweight':'automatic';}catch{return 'automatic';}}
export function writeTerrainResourceMode(mode:TerrainResourceMode){try{globalThis.localStorage?.setItem(TERRAIN_RESOURCE_MODE_KEY,mode);}catch{/* Optional preference; no permission prompt or persistence requirement. */}}
