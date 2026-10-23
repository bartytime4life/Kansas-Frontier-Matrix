// Explicit synthetic CPU benchmark. Outside *.test.mjs; no timing gate or provider I/O.
import { readFile } from 'node:fs/promises';
import { performance } from 'node:perf_hooks';
import { createHash } from 'node:crypto';
import { cpus } from 'node:os';
import ts from 'typescript';
const source = await readFile(process.argv[2] ?? 'app/water-flow-motion.ts', 'utf8');
const js = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const flow = await import('data:text/javascript;base64,' + Buffer.from(js).toString('base64'));
const cases = [];
for (const segments of [3000, 20000, 60000]) for (const gauges of [0, 193]) {
  const reaches = Array.from({ length: segments / 100 }, (_, r) => ({ id: 'synthetic-' + r, sequence: r, downstream: null, levelpath: r, name: null, featureType: 1,
    coordinates: Array.from({ length: 101 }, (_, i) => [-101 + (r % 60) * .07 + i * .0005, 37 + Math.floor(r / 60) * .05 + Math.sin(i * .08) * .0002]) }));
  const cues = Array.from({ length: gauges }, (_, i) => ({ coordinate: reaches[i % reaches.length].coordinates[50], intensity: .7, moving: true, tint: 'rising' }));
  for (let i = 0; i < 3; i++) flow.buildFlowGeometry(reaches, cues);
  const times = []; let result;
  for (let i = 0; i < 12; i++) { const start = performance.now(); result = flow.buildFlowGeometry(reaches, cues); times.push(performance.now() - start); }
  times.sort((a, b) => a - b);
  cases.push({ segments, gauges, samples: times.length, p50Ms: times[6], p95Ms: times[11], segmentCount: result.count, gpuBufferBytes: result.segments.byteLength });
}
console.log(JSON.stringify({ profile: 'kfm.synthetic-water-flow-cpu/v1', sourceSha256: createHash('sha256').update(source).digest('hex'), node: process.version, cpu: cpus()[0]?.model ?? 'unknown', limitation: 'Synthetic spread-out Kansas reaches; CPU geometry only. No provider latency, GPU FPS, dense worst-case or physical phone qualification.', cases }, null, 2));
