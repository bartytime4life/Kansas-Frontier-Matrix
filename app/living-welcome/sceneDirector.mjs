import { CATEGORY_IDS, SCENES } from './catalog.mjs';
export const SCENE_DWELL = 8.8;
export const SCENE_BLEND = 1.15;
export const EXIT_GRACE = 180;
export const clamp = (n,lo=0,hi=1)=>Math.max(lo,Math.min(hi,n));
export const ease = n=>{const x=clamp(n);return x*x*(3-2*x);};
// Use one continuous clock; interrupted interactions never create new timelines.
export function sceneAt(seconds,id,override=null) {
  const index=CATEGORY_IDS.indexOf(id),count=SCENES[id]?.length||1;
  if(Number.isInteger(override))return {from:override%count,to:override%count,mix:0};
  const t=Math.max(0,seconds+(id==='history'?0:index*2.17)),step=Math.floor(t/SCENE_DWELL),phase=t%SCENE_DWELL;
  return {from:step%count,to:(step+1)%count,mix:ease((phase-(SCENE_DWELL-SCENE_BLEND))/SCENE_BLEND)};
}
export function approach(current,target,seconds){return current+(target-current)*(1-Math.exp(-Math.max(0,seconds)*4.2));}
export function dominantScene(state){return state.mix>.5?state.to:state.from;}
