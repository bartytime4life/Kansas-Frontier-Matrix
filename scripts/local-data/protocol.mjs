// Shared by the website (server/local-data.mjs), the pipeline PC's local-data gateway and its
// relay worker, so all three agree on the routes, sizes and gateway identity. No dependencies.
export const LOCAL_DATA_GATEWAY='kfm-local-data/1';
export const LOCAL_DATA_WORKER='kfm-local-data-worker/1';
// The only calls that ever reach the PC. Each answers one fixed, read-only question.
export const LOCAL_DATA_ROUTES=new Map([['/v1/health','GET'],['/v1/data/storm-events','POST']]);
export const LOCAL_DATA_LIMITS=Object.freeze({
 requestBytes:4096,
 // A full page of storm events with narratives stays well under this.
 replyBytes:1_000_000,
 gatewayMs:10000,
 // Site-side wait for the whole relay trip (queue, lease, query, signed reply).
 clientMs:20000,
});
