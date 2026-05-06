import { mkdir, cp, rm, stat } from 'node:fs/promises';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = dirname(fileURLToPath(import.meta.url));
const dist = resolve(root, 'dist');
const src = resolve(root, 'src');
const publicDir = resolve(root, 'public');

async function exists(path) {
  try { await stat(path); return true; } catch { return false; }
}

await rm(dist, { recursive: true, force: true });
await mkdir(dist, { recursive: true });
await cp(resolve(root, 'index.html'), resolve(dist, 'index.html'));
await cp(src, resolve(dist, 'src'), { recursive: true });
if (await exists(publicDir)) await cp(publicDir, resolve(dist, 'public'), { recursive: true });
console.log('Built static web app into apps/web/dist');
