// Shared by the website (server/local-data.mjs), the pipeline PC's local-data gateway and its
// relay worker, so all three agree on the routes, sizes and gateway identity. No dependencies.
import {DATASETS} from './datasets.mjs';

export const LOCAL_DATA_GATEWAY='kfm-local-data/1';
export const LOCAL_DATA_WORKER='kfm-local-data-worker/1';
export const LOCAL_DATA_DATA_PREFIX='/v1/data/';
// The only calls that ever reach the PC: health, and one fixed, read-only question per dataset.
export const LOCAL_DATA_ROUTES=new Map([['/v1/health','GET'],...[...DATASETS.keys()].map(id=>[LOCAL_DATA_DATA_PREFIX+id,'POST'])]);
export const LOCAL_DATA_LIMITS=Object.freeze({
 requestBytes:4096,
 // A full page of any dataset stays under this; larger pages are refused with REPLY_TOO_LARGE.
 replyBytes:1_000_000,
 gatewayMs:10000,
 // Site-side wait for the whole relay trip (queue, lease, query, signed reply).
 clientMs:20000,
});
