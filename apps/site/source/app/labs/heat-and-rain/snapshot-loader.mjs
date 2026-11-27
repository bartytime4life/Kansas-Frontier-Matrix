import { loadVerifiedSnapshot } from '../../science/snapshot-loader.mjs';
import { validateSnapshot } from './climate-model.mjs';

export function loadClimateSnapshot(descriptor, options = {}) {
  return loadVerifiedSnapshot(descriptor, value => validateSnapshot(value, descriptor), {
    ...options, prefix: 'daily-climate', limit: 1024 * 1024,
  });
}
