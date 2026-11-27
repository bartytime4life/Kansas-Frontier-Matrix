import { loadVerifiedSnapshot } from '../../science/snapshot-loader.mjs';
import { validateSunlightSnapshot } from './sunlight-model.mjs';

export function loadSunlightSnapshot(descriptor, options = {}) {
  return loadVerifiedSnapshot(descriptor, snapshot => validateSunlightSnapshot(snapshot, descriptor),
    { ...options, prefix: 'sunlight', limit: 1024 * 1024 });
}
