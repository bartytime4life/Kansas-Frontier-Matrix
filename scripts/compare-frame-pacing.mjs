import { readFile } from 'node:fs/promises';
import ts from 'typescript';
const [published, candidate] = process.argv.slice(2);
if (!published || !candidate) throw new Error('Usage: node scripts/compare-frame-pacing.mjs published.json candidate.json');
const code = ts.transpileModule(await readFile(new URL('../app/frame-check-model.ts', import.meta.url), 'utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const { comparePacingRecords } = await import(`data:text/javascript;base64,${Buffer.from(code).toString('base64')}`);
const result = comparePacingRecords(JSON.parse(await readFile(published, 'utf8')), JSON.parse(await readFile(candidate, 'utf8')));
console.log(JSON.stringify(result, null, 2));
if (result.status !== 'PASS') process.exitCode = 1;
