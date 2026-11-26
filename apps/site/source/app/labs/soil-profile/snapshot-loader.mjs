import { loadVerifiedSnapshot } from '../../science/snapshot-loader.mjs';
import { validateSoilSnapshot } from './soil-model.mjs';

export function loadSoilSnapshot(descriptor, options = {}) {
  return loadVerifiedSnapshot(descriptor, value => validateSoilSnapshot(value, descriptor), {
    ...options, prefix: 'soil-profile', limit: 1024 * 1024,
  });
}
