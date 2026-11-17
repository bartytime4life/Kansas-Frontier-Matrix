import { readFile, readdir, lstat } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { resolve } from 'node:path';
import { PUBLIC_LAB_SNAPSHOTS } from '../app/labs/public-snapshots.mjs';
import { loadPublicLabSnapshot } from '../app/labs/snapshot-loader.mjs';

const expected = new Set();
const directories = ['labs-data', 'labs-data-extension', 'labs-data-bridges', 'labs-data-observatory'];
for (const [id, snapshot] of Object.entries(PUBLIC_LAB_SNAPSHOTS)) {
  if (!/^[a-z]+(?:-[a-z]+)*$/.test(id) || !new RegExp(`^/(?:${directories.join('|')})/${id}-[a-f0-9]{16}\\.json$`).test(snapshot.path)) {
    throw new Error('Invalid public Labs manifest path');
  }
  const path = new URL('../public' + snapshot.path, import.meta.url);
  const stat = await lstat(path);
  if (!stat.isFile() || stat.isSymbolicLink()) throw new Error('Labs data must be a regular file');
  const result = await loadPublicLabSnapshot(id, { fetcher: async () => new Response(await readFile(path)) });
  if (result.state !== 'ready') throw new Error(`Invalid public Labs snapshot: ${id}`);
  expected.add(fileURLToPath(path));
}
for (const directory of directories) for (const entry of await readdir(new URL(`../public/${directory}/`, import.meta.url))) {
  const path = fileURLToPath(new URL(`../public/${directory}/${entry}`, import.meta.url));
  if (!expected.has(resolve(path))) throw new Error(`Unlisted public Labs file: ${entry}`);
}
console.log(`Validated ${expected.size} public Labs snapshots: hashes, sizes, contracts and shipping file list.`);
