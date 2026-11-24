'use client';
import {useCallback,useEffect,useRef,useState} from 'react';
import {visitorTerrainCacheStatus,setVisitorTerrainCacheEnabled,clearVisitorTerrainCache,TERRAIN_CACHE_EVENT} from './visitor-terrain-cache';
import {browserTerrainPolicy,readTerrainResourceMode,writeTerrainResourceMode,TERRAIN_LIGHT_FRAME_PIXELS,TERRAIN_NORMAL_FRAME_PIXELS,type TerrainResourceMode} from './visitor-terrain-policy';
export function useVisitorTerrainResources(){
 const [mode,setMode]=useState<TerrainResourceMode>('automatic'),[deviceLight,setDeviceLight]=useState(true),[slow,setSlow]=useState(false),[cache,setCache]=useState({enabled:false,usedBytes:0,limitBytes:8*1024*1024,available:false}),[busy,setBusy]=useState(false),[error,setError]=useState('');
 const alive=useRef(false),revision=useRef(0),markSlow=useCallback(()=>setSlow(true),[]);
 async function refresh(){const id=++revision.current;try{const value=await visitorTerrainCacheStatus();if(alive.current&&id===revision.current)setCache(value);}catch{if(alive.current&&id===revision.current)setError('Temporary terrain storage is unavailable. The map still works.');}}
 // Read optional browser preferences only after hydration.
 // eslint-disable-next-line react-hooks/set-state-in-effect
 useEffect(()=>{alive.current=true;setMode(readTerrainResourceMode());setDeviceLight(browserTerrainPolicy().lightweight);void refresh();const update=()=>{setMode(readTerrainResourceMode());void refresh();};window.addEventListener(TERRAIN_CACHE_EVENT,update);window.addEventListener('storage',update);return()=>{alive.current=false;window.removeEventListener(TERRAIN_CACHE_EVENT,update);window.removeEventListener('storage',update);};},[]);
 const lightweight=mode==='lightweight'||deviceLight||slow;
 async function changeStorage(enabled?:boolean){if(busy)return;setBusy(true);setError('');try{if(enabled===undefined)await clearVisitorTerrainCache();else await setVisitorTerrainCacheEnabled(enabled);await refresh();}catch{if(alive.current)setError('Temporary storage could not be changed. Source data and map controls are unchanged.');}finally{if(alive.current)setBusy(false);}}
 return {mode,lightweight,slow,framePixelLimit:lightweight?TERRAIN_LIGHT_FRAME_PIXELS:TERRAIN_NORMAL_FRAME_PIXELS,cache,busy,error,setMode:(value:TerrainResourceMode)=>{if(value!=='automatic'&&value!=='lightweight')return;setMode(value);writeTerrainResourceMode(value);},markSlow,setStorage:(enabled:boolean)=>changeStorage(enabled),clear:()=>changeStorage()};
}
