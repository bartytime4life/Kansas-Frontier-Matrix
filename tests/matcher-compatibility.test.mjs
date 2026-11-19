import assert from 'node:assert/strict';
import {mkdtempSync, writeFileSync, rmSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {createRequire} from 'node:module';
import test from 'node:test';

const require = createRequire(import.meta.url);
const consumer = createRequire(require.resolve('@typescript-eslint/typescript-estree'));

test('the TypeScript matcher is patched while legacy callers keep the callable API', () => {
  assert.equal(consumer('minimatch/package.json').version, '11.0.1');
  assert.equal(require('minimatch/package.json').version, '3.1.5');
  assert.equal(typeof consumer('minimatch').minimatch, 'function');
  assert.equal(typeof require('minimatch'), 'function');
});

test('modern and legacy matchers preserve the project-file glob behavior', () => {
  const modern = consumer('minimatch').minimatch;
  const legacy = require('minimatch');
  for (const [file, pattern, expected] of [
    ['app/map.ts', 'app/**/*.ts', true],
    ['app/deep/map.tsx', 'app/**/*.{ts,tsx}', true],
    ['app/.fixture.ts', 'app/*.ts', true],
    ['server/map.mjs', 'app/**/*.{ts,tsx}', false],
    ['app/map.ts', '*.ts', false],
  ]) {
    assert.equal(modern(file, pattern, {dot: true}), expected, file);
    assert.equal(legacy(file, pattern, {dot: true}), expected, file);
  }
});

test('the actual TypeScript project service accepts only allowed default-project files', () => {
  const root = mkdtempSync(join(tmpdir(), 'kfm-matcher-'));
  const parser = require('@typescript-eslint/typescript-estree');
  try {
    writeFileSync(join(root, 'tsconfig.json'), JSON.stringify({
      compilerOptions: {strict: true}, include: ['included.ts'],
    }));
    writeFileSync(join(root, 'included.ts'), 'export const included = true;');
    const source = 'const fixture: number = 1;';
    const allowed = parser.parseAndGenerateServices(source, {
      filePath: join(root, '.fixture.ts'), tsconfigRootDir: root,
      projectService: {allowDefaultProject: ['*.ts']},
    });
    assert.equal(allowed.ast.type, 'Program');
    assert.ok(allowed.services.program);
    assert.throws(() => parser.parseAndGenerateServices(source, {
      filePath: join(root, 'blocked.js'), tsconfigRootDir: root,
      projectService: {allowDefaultProject: ['*.ts']},
    }), /not found by the project service|allowDefaultProject/);
  } finally {
    parser.clearCaches();
    rmSync(root, {recursive: true, force: true});
  }
});
