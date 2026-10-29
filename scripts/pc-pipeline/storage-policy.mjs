import { fail, MAX_PACKAGE } from '../../server/pipeline-contract.mjs';

// This is a publication budget, never permission to release a source.
export function storagePolicy(config) {
  const supplied = config.storagePolicy === undefined ? {} : config.storagePolicy;
  if (!supplied || typeof supplied !== 'object' || Array.isArray(supplied)
    || Object.keys(supplied).some(k => !['priority', 'maxPublicationsPerTick', 'maxBytesPerTick'].includes(k))) fail('STORAGE_POLICY_INVALID');
  const priority = supplied.priority ?? ['nws-alerts', 'usgs-streamflow', 'usgs-earthquakes'];
  const maxPublicationsPerTick = supplied.maxPublicationsPerTick ?? 1;
  const maxBytesPerTick = supplied.maxBytesPerTick ?? MAX_PACKAGE;
  // Earlier configs list the two original sources; a config may name earthquakes as a third.
  if (!Array.isArray(priority) || priority.length < 2 || priority.length > 3 || new Set(priority).size !== priority.length
    || priority.some(s => !['nws-alerts', 'usgs-streamflow', 'usgs-earthquakes'].includes(s))
    || !Number.isInteger(maxPublicationsPerTick) || maxPublicationsPerTick < 1 || maxPublicationsPerTick > 3
    || !Number.isInteger(maxBytesPerTick) || maxBytesPerTick < 262144 || maxBytesPerTick > 2 * MAX_PACKAGE) fail('STORAGE_POLICY_INVALID');
  return { priority, maxPublicationsPerTick, maxBytesPerTick };
}
export function storagePlan(config) {
  return { format: 'kfm-storage-plan-v1', publicationEnabled: config.publish === true,
    policy: storagePolicy(config), sources: config.sources,
    pc: ['Original captures', 'Processing history', 'SQLite job journal', 'Private backups'],
    hosting: ['Approved current projections', 'Release identities and provenance', 'Bounded released history'],
    capacity: 'unverified', automaticDeletion: false,
    note: 'Budget covers normalized payload bytes, not HTTP/base64 overhead or total MySQL usage. Manual stage-package is separate. Approval and storage qualification remain required.' };
}
