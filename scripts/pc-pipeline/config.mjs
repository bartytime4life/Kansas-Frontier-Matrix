import { resolve } from 'node:path';
import { readRegular } from '../../server/pipeline-files.mjs';
import { parse, fail } from '../../server/pipeline-contract.mjs';
import { storagePolicy } from './storage-policy.mjs';
import { PC_CAPTURE_IDS } from '../../app/pipeline-catalog.mjs';

/** v2 can reference only implemented capture adapters, not proposed registry lanes. */
export function validateConfig(input) {
  let config = input;
  if (input?.format === 'kfm-pc-pipeline-config-v2') {
    if ('sources' in input || !Array.isArray(input.pipelines) || input.pipelines.length > PC_CAPTURE_IDS.length
      || input.pipelines.some(p => !p || Object.keys(p).sort().join(',') !== 'enabled,sourceId'
        || !PC_CAPTURE_IDS.includes(p.sourceId) || typeof p.enabled !== 'boolean')
      || new Set(input.pipelines.map(p => p.sourceId)).size !== input.pipelines.length) fail('CONFIG_INVALID');
    // Normalize once to the existing worker/backup contract; persisted v2 input is unchanged.
    config = { ...input, format: 'kfm-pc-pipeline-config-v1', sources: input.pipelines.filter(p => p.enabled).map(p => p.sourceId) };
    delete config.pipelines;
  }
  if (!config || !['kfm-pc-pipeline-config-v1', 'kfm-pc-pipeline-config-v2'].includes(config.format)
    || !['root','mount','approvalDirectory'].every(key => typeof config[key] === 'string' && config[key].startsWith('/') && resolve(config[key]) === config[key])
    || !/^[a-f0-9]{32}$/.test(config.storeId ?? '') || !/^\d+$/.test(String(config.device))
    || !Array.isArray(config.sources) || config.sources.length > PC_CAPTURE_IDS.length || new Set(config.sources).size !== config.sources.length
    || config.sources.some(source => !PC_CAPTURE_IDS.includes(source)) || typeof config.publish !== 'boolean'
    || (config.remoteMode !== undefined && config.remoteMode !== 'connection-only')) fail('CONFIG_INVALID');
  if (config.remoteMode === 'connection-only' && config.publish) fail('CONNECTION_ONLY_UPLOADS_DISABLED');
  // Only working files under data/work/ may leave the per-file backup; captures, raw files and receipts never do.
  if (config.separateBackup !== undefined && (!Array.isArray(config.separateBackup) || !config.separateBackup.length
    || config.separateBackup.length > 8 || new Set(config.separateBackup).size !== config.separateBackup.length
    || config.separateBackup.some(p => typeof p !== 'string' || p.length > 256
      || !/^work(?:\/[A-Za-z0-9_-][A-Za-z0-9._-]*)+$/.test(p)))) fail('CONFIG_INVALID');
  storagePolicy(config);
  return config;
}
export async function readConfig(path) { return validateConfig(parse(await readRegular(path, 16384))); }
