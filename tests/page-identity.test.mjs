import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile, readdir } from 'node:fs/promises';

const ORIGIN = 'https://kansasfrontiermatrix.com';
const read = path => readFile(path, 'utf8').catch(() => '');
const sources = async path => (await Promise.all(['page.tsx', 'page.jsx', 'layout.tsx', 'layout.jsx'].map(name => read(`app${path}/${name}`)))).join('\n');

test('every public reading page in the sitemap names its own canonical address', async () => {
  const discovery = await read('app/crawler-discovery.ts');
  const listed = [...discovery.match(/PUBLIC_PAGES = Object\.freeze\(\[([\s\S]*?)\]\)/)[1].matchAll(/"(\/[a-z0-9/-]+)"/g)].map(match => match[1]);
  assert.ok(listed.includes('/observatory') && listed.includes('/records') && listed.length >= 15);
  for (const path of listed) {
    const text = await sources(path);
    if (path === '/labs') {
      // The labs index is a client page whose layout would also wrap every lab. A canonical declared there
      // would be inherited by labs that do not declare their own, so it is deliberately left without one.
      assert.ok(!/canonical/.test(await read('app/labs/layout.tsx')), 'no canonical on a layout that wraps other pages');
      continue;
    }
    assert.ok(text.includes(`canonical: "${ORIGIN}${path}"`) || /canonical: url|canonical: `\$\{PUBLIC_SITE_ORIGIN\}/.test(text), `${path} declares its canonical address`);
    assert.ok(!new RegExp(`canonical: "${ORIGIN}(?!${path}")`).test(text), `${path} does not name another page's address`);
  }
});

test('a canonical address declared in a layout applies to one page only', async () => {
  for (const path of ['/data-lab', '/data-library', '/history/people-events', '/history/prentis-1909']) {
    assert.match(await read(`app${path}/layout.tsx`), new RegExp(`canonical: "${ORIGIN}${path}"`));
    const children = (await readdir(`app${path}`, { withFileTypes: true })).filter(entry => entry.isDirectory());
    assert.deepEqual(children.map(entry => entry.name), [], `${path} has no child routes that would inherit its address`);
  }
});

test('the two client pages that showed the site-wide title now have their own', async () => {
  for (const [path, title] of [['/data-lab', 'Data lab · Kansas Frontier Matrix'], ['/data-library', 'Public data library · Kansas Frontier Matrix']]) {
    const layout = await read(`app${path}/layout.tsx`);
    assert.ok(layout.includes(`title: "${title}"`)); assert.match(layout, /description: "[^"]{60,200}"/);
    assert.match(await read(`app${path}/page.tsx`), /^'use client';/, 'which is why the title lives in a layout');
  }
});
