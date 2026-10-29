import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { existsSync } from 'node:fs';

// Keeps docs/second-pc-pipeline.md navigable as the pipeline changes: heading levels
// do not skip, in-page links reach a heading, and cited repository paths exist.
const lines = (await readFile(new URL('../docs/second-pc-pipeline.md', import.meta.url), 'utf8')).split('\n');
const prose = []; let fence = false;
for (const [i, line] of lines.entries()) { if (/^\s*```/.test(line)) fence = !fence; else if (!fence) prose.push([i + 1, line]); }
// GitHub heading slug: lowercase, drop punctuation except - and _, spaces become hyphens.
const headings = prose.flatMap(([n, line]) => {
  const m = /^(#{1,6})\s+(.*)$/.exec(line);
  return m ? [{ n, level: m[1].length, slug: m[2].trim().toLowerCase().replace(/[^\p{L}\p{N} _-]/gu, '').replace(/ /g, '-') }] : [];
});
const cited = prefixes => new Set(prose.flatMap(([, line]) =>
  [...line.matchAll(new RegExp('`((?:' + prefixes + ')/[A-Za-z0-9_./-]+)`', 'g'))].map(m => m[1]).filter(path => !path.includes('*'))));

test('pipeline runbook heading levels do not skip', () => {
  for (let i = 1; i < headings.length; i++) {
    assert.ok(headings[i].level <= headings[i - 1].level + 1, `line ${headings[i].n} jumps from h${headings[i - 1].level} to h${headings[i].level}`);
  }
});
test('pipeline runbook in-page links reach a heading', () => {
  const slugs = new Set(headings.map(h => h.slug)); let anchors = 0;
  for (const [n, line] of prose) for (const [, anchor] of line.matchAll(/\]\(#([^)\s]+)\)/g)) { anchors++; assert.ok(slugs.has(anchor), `line ${n}: #${anchor} matches no heading`); }
  assert.ok(anchors > 0);
});
test('pipeline runbook cites repository paths that exist', () => {
  const paths = cited('scripts|server|tests|docs|\\.github'); assert.ok(paths.size > 5);
  for (const path of paths) assert.ok(existsSync(new URL('../' + path, import.meta.url)), `cited path is missing: ${path}`);
});
// tools/ lives in the pipeline-implementation checkout and pc-pipeline-data/ is private
// host state; both sit beside this checkout only on the pipeline PC.
const host = new URL('../../', import.meta.url);
test('pipeline runbook cites pipeline-host paths that exist', { skip: !existsSync(new URL('pipeline-implementation/', host)) && 'not on the pipeline PC' }, () => {
  for (const path of cited('tools')) assert.ok(existsSync(new URL('pipeline-implementation/' + path, host)), `cited path is missing: ${path}`);
  for (const path of cited('pc-pipeline-data')) assert.ok(existsSync(new URL(path, host)), `cited path is missing: ${path}`);
});
