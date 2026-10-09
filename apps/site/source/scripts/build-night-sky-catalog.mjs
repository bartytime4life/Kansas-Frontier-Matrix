#!/usr/bin/env node
// Builds app/night-sky-catalog.json from d3-celestial's stars.6.json.
//
//   npm pack d3-celestial@0.7.35 && tar -xzf d3-celestial-0.7.35.tgz
//   node scripts/build-night-sky-catalog.mjs package/data/stars.6.json
//
// The input is read as data only. Output is deterministic for the same input.
import { createHash } from "node:crypto";
import { readFileSync, writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

const SOURCE_PACKAGE = "d3-celestial@0.7.35";
const SOURCE_FILE = "data/stars.6.json";
const SOURCE_SHA256 = "0297b8fa3adfbce1dc26566f61c4abcc1df4f29c6a28729ca06b56d1c6d25602";
const MAGNITUDE_LIMIT = 5.5;
const OUTPUT = fileURLToPath(new URL("../app/night-sky-catalog.json", import.meta.url));

const input = process.argv[2];
if (!input) {
  console.error("usage: build-night-sky-catalog.mjs <path to d3-celestial data/stars.6.json>");
  process.exit(64);
}
const raw = readFileSync(input);
const sha256 = createHash("sha256").update(raw).digest("hex");
if (sha256 !== SOURCE_SHA256) {
  console.error(`unexpected ${SOURCE_FILE} digest ${sha256}; expected ${SOURCE_SHA256} from ${SOURCE_PACKAGE}`);
  process.exit(65);
}

const round = (value, places) => Number(value.toFixed(places));
const stars = [];
for (const feature of JSON.parse(raw).features) {
  const mag = Number(feature.properties?.mag);
  const [lon, lat] = feature.geometry?.coordinates ?? [];
  if (!(mag <= MAGNITUDE_LIMIT) || !Number.isFinite(lon) || !Number.isFinite(lat)) continue;
  const bv = Number.parseFloat(feature.properties.bv);
  // d3-celestial stores right ascension as a longitude in [-180, 180].
  stars.push([round(lon < 0 ? lon + 360 : lon, 3), round(lat, 3), round(mag, 2), Number.isFinite(bv) ? round(bv, 2) : null]);
}
// Faintest first, so the brightest stars draw last and sit on top.
stars.sort((a, b) => b[2] - a[2] || a[0] - b[0] || a[1] - b[1]);

const catalog = {
  schema: "kfm-night-sky-catalog/v1",
  role: "display",
  description: "Bright stars for the Site's night-sky scene effect. Right ascension and declination are J2000 degrees; magnitude is apparent visual; bv is the B-V colour index (null when unknown).",
  source: {
    catalog: "XHIP: An Extended Hipparcos Compilation (Anderson & Francis 2012, VizieR V/137D)",
    package: SOURCE_PACKAGE,
    file: SOURCE_FILE,
    sha256,
    license: "BSD-3-Clause",
    notice: "Copyright (c) 2015, Olaf Frohn. All rights reserved. Redistributed under the BSD 3-Clause License; see apps/site/source/docs/night-sky.md.",
  },
  magnitudeLimit: MAGNITUDE_LIMIT,
  fields: ["ra", "dec", "mag", "bv"],
  count: stars.length,
  stars: stars.flat(),
};
writeFileSync(OUTPUT, `${JSON.stringify(catalog)}\n`);
console.log(`wrote ${stars.length} stars to ${OUTPUT}`);
