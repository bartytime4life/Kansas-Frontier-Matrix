#!/usr/bin/env node
import { modelUrl } from './lib/typescript-model.mjs';
import { fileURLToPath } from 'node:url';
const model = await import(await modelUrl(fileURLToPath(new URL('../app/card-pipelines.ts', import.meta.url))));
const sources = new Map(model.PIPELINE_DEFINITIONS.map(source => [source.id, source]));
const cell = value => String(value).replaceAll('|', '\\|').replaceAll('\n', ' ');
console.log('# Explorer card pipeline map\n\nGenerated from the application registry. This inventory does not activate sources or prove live coverage.\n');
console.log('Provider → bounded capture → private originals and receipts → normalization and validation → review → versioned release → authenticated transfer → serving checks → Explorer.\n');
for (const kind of ['topic', 'recipe']) {
  console.log(`## ${kind === 'recipe' ? 'Map starter recipes' : 'Visual welcome topics'}\n`);
  console.log('| Card | Required context | Optional context | Planned expansion |\n|---|---|---|---|');
  for (const card of model.CARD_PIPELINE_BINDINGS.filter(card => card.kind === kind)) {
    const names = ids => ids.map(id => sources.get(id).title).join('; ') || '—';
    console.log(`| ${cell(card.title)} | ${cell(card.demo ? 'Demo only' : names(card.required))} | ${cell(names(card.optional))} | ${cell(names(card.gaps))} |`);
  }
  console.log('');
}
console.log('## Domain qualification queue\n\n| Pipeline | Wave | Source reference | Next gate |\n|---|---|---|---|');
for (const source of model.PIPELINE_DEFINITIONS.filter(source => source.mode === 'candidate')) console.log(`| ${cell(source.title)} | ${source.wave} | ${cell(source.sourceRef)} | ${cell(source.nextGate)} |`);
console.log('\nUSGS streamflow, NWS alerts and USGS earthquakes have implemented PC capture adapters; this PC still schedules only the first two. Explorer display sources are not automatically scheduled. The active PC configuration determines capture; source profiles and serving gates determine publication.');
