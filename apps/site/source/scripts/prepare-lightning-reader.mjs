import { mkdir, copyFile, rm } from "node:fs/promises";
const root = new URL("../", import.meta.url);
const out = new URL("public/vendor/h5wasm/", root);
await rm(out, { recursive: true, force: true });
await mkdir(out, { recursive: true });
await copyFile(new URL("node_modules/h5wasm/dist/iife/h5wasm.js", root), new URL("h5wasm.js", out));
await copyFile(new URL("node_modules/h5wasm/LICENSE.txt", root), new URL("LICENSE.txt", out));
console.log("[lightning] prepared pinned same-origin HDF5 reader");
