import { copyFile, mkdir } from "node:fs/promises";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const projectRoot = dirname(dirname(fileURLToPath(import.meta.url)));
const maplibreDist = join(projectRoot, "node_modules", "maplibre-gl", "dist");
const publicDir = join(projectRoot, "public", "maplibre");
const runtimeAssets = ["maplibre-gl-worker.mjs", "maplibre-gl-shared.mjs"];

await mkdir(publicDir, { recursive: true });
await Promise.all(runtimeAssets.map((fileName) => copyFile(
  join(maplibreDist, fileName),
  join(publicDir, fileName),
)));

console.log(`[maplibre] prepared ${runtimeAssets.length} same-origin runtime assets`);
