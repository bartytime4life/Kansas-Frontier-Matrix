#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { publishTileLayer } from "../apps/web/src/map/pmtiles/tileReleasePublisher.js";

function arg(name) {
  const idx = process.argv.indexOf(name);
  return idx >= 0 ? process.argv[idx + 1] : undefined;
}

const candidatePath = arg("--candidate");
const outDir = arg("--out");
const metadataPath = arg("--pmtiles-metadata");
if (!candidatePath || !outDir) {
  console.error(JSON.stringify({ outcome: "ERROR", reasons: ["missing_args"] }));
  process.exit(2);
}

const candidate = JSON.parse(fs.readFileSync(candidatePath, "utf8"));
const metadata = metadataPath ? JSON.parse(fs.readFileSync(metadataPath, "utf8")) : {};
const result = publishTileLayer(candidate, metadata);

if (result.outcome === "PUBLISHABLE") {
  fs.mkdirSync(outDir, { recursive: true });
  fs.writeFileSync(path.join(outDir, "tilejson.json"), JSON.stringify(result.generated.tilejson, null, 2));
  fs.writeFileSync(path.join(outDir, "release_manifest.json"), JSON.stringify(result.generated.release_manifest, null, 2));
  fs.writeFileSync(path.join(outDir, "catalog_record.json"), JSON.stringify(result.generated.catalog_record, null, 2));
  fs.writeFileSync(path.join(outDir, "registry_entry.json"), JSON.stringify(result.generated.registry_entry, null, 2));
  console.log(JSON.stringify(result, null, 2));
  process.exit(0);
}

console.log(JSON.stringify(result, null, 2));
process.exit(1);
