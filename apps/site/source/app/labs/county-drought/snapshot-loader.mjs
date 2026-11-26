import { loadVerifiedSnapshot } from '../../science/snapshot-loader.mjs';
import { validateDroughtSnapshot } from './drought-model.mjs';

export function loadDroughtSnapshot(manifest, options = {}) {
  return loadVerifiedSnapshot(manifest?.snapshot, value => validateDroughtSnapshot(value, manifest), {
    ...options, prefix: 'county-drought', limit: 2 * 1024 * 1024,
  });
}
