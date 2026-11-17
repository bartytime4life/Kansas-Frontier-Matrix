import { BASE_LAB_SNAPSHOTS } from './base-snapshots.mjs';
import { EXTENSION_LAB_SNAPSHOTS } from './extension-snapshots.mjs';
import { BRIDGE_LAB_SNAPSHOTS } from './bridge-snapshots.mjs';
import { COUNTY_LAB_SNAPSHOTS } from './county-snapshots.mjs';

export const PUBLIC_LAB_SNAPSHOTS = Object.freeze({ ...BASE_LAB_SNAPSHOTS, ...EXTENSION_LAB_SNAPSHOTS, ...BRIDGE_LAB_SNAPSHOTS, ...COUNTY_LAB_SNAPSHOTS });
