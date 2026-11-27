import { loadVerifiedSnapshot } from '../../science/snapshot-loader.mjs';
import { validateAirSnapshot } from './air-model.mjs';

export function loadAirSnapshot(manifest, options = {}) {
  return loadVerifiedSnapshot(manifest?.snapshot, snapshot => validateAirSnapshot(snapshot, manifest),
    { ...options, prefix: 'daily-air-quality', limit: 6 * 1024 * 1024 });
}
