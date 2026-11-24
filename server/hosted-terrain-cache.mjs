// Public prepared terrain only. Preserve the existing storage format and limits.
import {resolve} from 'node:path';
import {createSignedPublicCache} from './signed-public-cache.mjs';
export const HOSTED_TERRAIN_LIMITS=Object.freeze({bytes:1024**3,entries:2048,entryBytes:1_004_096,reserveBytes:512*1024**2,freshMs:24*3600000,staleMs:7*24*3600000});
const terminal=value=>value&&['ready','partial','no-coverage','detail-required'].includes(value.state)||value&&value.format==='kfm-lidar-grid-v1';
export function createHostedTerrainCache({root=resolve('public/assets/kfm-terrain-cache-v1'),secret,origin,clock=Date.now,limits={}}={}){
 return createSignedPublicCache({root,secret,origin,clock,limits:{...HOSTED_TERRAIN_LIMITS,...limits},format:'kfm-hosted-terrain-cache-v1',keyPattern:/^(?:ground|view|grid):[a-f0-9]{64}$/,accept:terminal});
}
