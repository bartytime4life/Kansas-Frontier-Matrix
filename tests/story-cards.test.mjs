// "The Kansas record" story cards: the framework's contract. Registry and relay checks need no browser.
// Checks of the welcome page, the dataset list and the Vite config read files that live on the site branch
// (a0-hosted-ai-web-20261017), so they skip with a reason on a checkout without the site.
import test from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { STORIES, STORY_GROUPS, storyById } from '../app/living-welcome/stories/registry.mjs';

const path = relative => fileURLToPath(new URL(`../${relative}`, import.meta.url));
const read = relative => readFileSync(path(relative), 'utf8');
const onSite = existsSync(path('app/living-welcome/welcome.jsx'));
const siteOnly = onSite ? {} : { skip: 'the site is not in this checkout; run on a tree from a0-hosted-ai-web-20261017' };
const reactHere = existsSync(path('node_modules/react/package.json'));
const reactOnly = reactHere ? {} : { skip: 'react is not installed in this checkout' };
const hex = /^#[0-9a-f]{6}$/i;

test('the registry lists 22 stories with unique ids, known groups and complete copy', () => {
  assert.equal(STORIES.length, 22);
  assert.equal(new Set(STORIES.map(story => story.id)).size, 22);
  for (const story of STORIES) {
    assert.match(story.id, /^[a-z0-9]+(?:-[a-z0-9]+)*$/);
    assert.ok(STORY_GROUPS.includes(story.group), `${story.id} group`);
    for (const key of ['title', 'kicker', 'summary', 'try', 'limit']) assert.ok(story[key]?.length > 3, `${story.id} ${key}`);
    assert.equal(story.palette.length, 3, `${story.id} palette`);
    for (const colour of story.palette) assert.match(colour, hex, `${story.id} palette`);
    assert.ok(story.sources.length > 0, `${story.id} sources`);
    assert.ok(story.tables.length > 0 && story.tables.every(table => /^kfm_[a-z0-9_]+$/.test(table)), `${story.id} tables`);
    assert.ok(story.feeds.length > 0, `${story.id} feeds`);
    assert.ok(['observations', 'bulk'].includes(story.db), `${story.id} db`);
  }
  for (const group of STORY_GROUPS) assert.ok(STORIES.some(story => story.group === group), group);
  assert.equal(storyById('iron-horse').title, 'Iron Horse, 1861–1911');
  assert.equal(storyById('nope'), null);
});

test('only the two exemplars are ready, and every ready story has its module; the rest are planned', () => {
  const ready = STORIES.filter(story => story.status === 'ready');
  assert.deepEqual(ready.map(story => story.id).sort(), ['climate-stripes', 'iron-horse']);
  for (const story of ready) {
    assert.equal(typeof story.load, 'function');
    assert.ok(existsSync(path(`app/living-welcome/stories/${story.id}.jsx`)), story.id);
    assert.match(story.load.toString(), new RegExp(`import\\(['"]\\./${story.id}\\.jsx['"]\\)`), 'a lazy import');
  }
  for (const story of STORIES.filter(entry => entry.status !== 'ready')) {
    assert.equal(story.status, 'planned', story.id);
    assert.equal(story.load, null, story.id);
  }
});

test('a story never fetches, and cards hold still and stop offscreen through the shared hook', () => {
  for (const name of ['iron-horse.jsx', 'climate-stripes.jsx', 'story-parts.jsx', 'story-kit.mjs']) {
    const source = read(`app/living-welcome/stories/${name}`);
    for (const banned of [/\bfetch\(/, /<video/, /<img/, /XMLHttpRequest/, /WebSocket/, /new Worker/, /qwen|\/api\/(?!local-data)/i]) assert.doesNotMatch(source, banned, `${name} ${banned}`);
  }
  const kit = read('app/living-welcome/stories/story-kit.mjs');
  assert.match(kit, /const shouldRun = \(\) => run\.current && onscreen && sized && !document\.hidden/, 'a frame loop needs motion, sight and a visible tab');
  assert.match(kit, /run\.current = animate && !held/);
  for (const name of ['iron-horse.jsx', 'climate-stripes.jsx']) assert.match(read(`app/living-welcome/stories/${name}`), /held=\{Boolean\(paused \|\| reduced\)\}/, name);
});

test('the lab is a real dialog: focus trap, Escape, focus return and an isolated background', () => {
  const lab = read('app/living-welcome/stories/StoryLab.jsx'), section = read('app/living-welcome/stories/StorySection.jsx');
  assert.match(lab, /role="dialog" aria-modal="true"/);
  assert.match(lab, /isolateModalBackground\(/);
  assert.match(lab, /modalFocusableElements\(/);
  assert.match(lab, /event\.key === 'Escape'/);
  assert.match(section, /\.story-card\[data-story="\$\{last\}"\] \.story-card-open/, 'focus returns to the card of the story last shown');
  assert.match(section, /Boolean\(paused \|\| reduced \|\| modal \|\| labId\)/, 'an open dialog holds the cards still');
  assert.match(section, /lazy\(\(\) => import\('\.\/StoryLab\.jsx'\)/, 'the lab is its own chunk');
});

test('story controls are at least 44 px', () => {
  const css = read('app/living-welcome/stories/stories.css');
  for (const selector of ['.story-tool', '.story-speed) button', '.story-scrubber input', '.story-select select', '.story-launcher', '.story-table-wrap summary']) {
    const rules = [...css.matchAll(new RegExp(`${selector.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}[^{}]*\\{[^}]*\\}`, 'g'))].map(match => match[0]);
    assert.ok(rules.some(rule => /min-height:44px/.test(rule)), selector);
  }
  assert.match(css, /\.story-icon-button\{[^}]*width:44px;height:44px/);
});

test('the relay dataset reads one bundle by primary key and rejects anything else', siteOnly, async () => {
  const { storyBundles } = await import('../scripts/local-data/stories.mjs');
  assert.equal(storyBundles.id, 'stories');
  assert.equal(storyBundles.db, 'observations');
  assert.deepEqual(storyBundles.parse({ story: 'iron-horse' }), { story: 'iron-horse' });
  for (const bad of [{}, { story: '' }, { story: '../etc' }, { story: 'A' }, { story: 'x'.repeat(65) }, { story: 'iron-horse', extra: 1 }, { story: ['iron-horse'] }]) {
    assert.throws(() => storyBundles.parse(bad), /QUERY_INVALID/, JSON.stringify(bad));
  }
  const { DatabaseSync } = await import('node:sqlite');
  const db = new DatabaseSync(':memory:');
  assert.deepEqual(storyBundles.run(db, { story: 'iron-horse' }), { total: 0, rows: [] }, 'no table yet means no bundle');
  db.exec('CREATE TABLE kfm_story_bundles (story_id TEXT PRIMARY KEY, version INTEGER, built_at TEXT, sha256 TEXT, bytes INTEGER, bundle_json TEXT)');
  db.prepare('INSERT INTO kfm_story_bundles VALUES (?,?,?,?,?,?)').run('iron-horse', 1, '2026-11-04T00:00:00Z', 'abc', 9, '{"format":"kfm-story-bundle-v1","story":"iron-horse"}');
  const reply = storyBundles.run(db, { story: 'iron-horse' });
  assert.equal(reply.total, 1);
  assert.equal(reply.rows[0].bundle.story, 'iron-horse');
  assert.equal(reply.rows[0].bundle_json, undefined);
  assert.deepEqual(storyBundles.run(db, { story: 'climate-stripes' }), { total: 0, rows: [] });
  db.close();
});

test('the bundle hook maps replies to ready, waiting and offline', reactOnly, async () => {
  const { storyBundleFrom, storyBundleState } = await import('../app/living-welcome/stories/useStoryBundle.js');
  const bundle = { format: 'kfm-story-bundle-v1', story: 'iron-horse', data: {} };
  assert.equal(storyBundleFrom(bundle, 'iron-horse'), bundle, 'the dev preview serves the bundle itself');
  assert.equal(storyBundleFrom({ rows: [{ bundle }] }, 'iron-horse'), bundle, 'the relay wraps it in a row');
  assert.equal(storyBundleFrom(bundle, 'climate-stripes'), null, 'a bundle for another story is refused');
  assert.equal(storyBundleState(200, bundle, 'iron-horse').state, 'ready');
  assert.equal(storyBundleState(200, { rows: [] }, 'iron-horse').state, 'waiting', 'no row yet');
  assert.equal(storyBundleState(404, { state: 'not-configured' }, 'iron-horse').state, 'waiting');
  assert.equal(storyBundleState(404, { reasonCode: 'DATASET_NOT_FOUND' }, 'iron-horse').state, 'waiting');
  assert.equal(storyBundleState(503, {}, 'iron-horse').state, 'offline');
});

test('the kit: colour scales, projection, grid paths, numbers and CSV', reactOnly, async () => {
  const kit = await import('../app/living-welcome/stories/story-kit.mjs');
  for (const scale of [kit.viridis, kit.magma, kit.cividis, kit.divergingBlueRed, kit.divergingBrownTeal]) {
    for (const t of [-1, 0, .25, .5, 1, 2, NaN]) assert.match(scale(t), /^rgb\(\d+,\d+,\d+\)$/);
  }
  const p = kit.kansasProjection(320, 200, { padding: 10 }), { west, east, south, north } = kit.KANSAS_BOUNDS;
  for (const [lon, lat] of kit.KANSAS_OUTLINE) {
    assert.ok(lon >= west - .01 && lon <= east + .01 && lat >= south - .01 && lat <= north + .01);
    assert.ok(p.x(lon) >= 9 && p.x(lon) <= 311 && p.y(lat) >= 9 && p.y(lat) <= 191);
  }
  const [lon, lat] = p.invert(p.x(-98), p.y(38.5));
  assert.ok(Math.abs(lon + 98) < 1e-9 && Math.abs(lat - 38.5) < 1e-9);
  assert.deepEqual([...kit.decodeGridPath([1000, 500, 10, -5], [-103, 36], .001)].map(v => +v.toFixed(3)), [-102, 36.5, -101.99, 36.495]);
  assert.equal(kit.fmt(1234.5, { digits: 1 }), '1,234.5');
  assert.equal(kit.fmt(-2, { unit: '°F', sign: true }), '−2°F');
  assert.equal(kit.fmt(null), '—');
  assert.equal(kit.csvText([['a', 'b,c'], [1, 'say "hi"'], [null, 2]]), 'a,"b,c"\r\n1,"say ""hi"""\r\n,2\r\n');
  const grid = kit.hitGrid(100, 100, 20);
  grid.add(7, 0, 0, 50, 0);
  assert.ok(grid.near(45, 5, 10).has(7));
  assert.ok(!grid.near(90, 90, 5).has(7));
  assert.equal(kit.distanceToSegment(5, 5, 0, 0, 10, 0), 5);
});

const miniBundle = {
  iron: { data: { years: [1861, 1872], milesByYear: [{ year: 1861, kansas: 0, kansasTotal: 0, neighbours: 2.5, neighboursTotal: 2.5, kansasSegments: 0, neighbourSegments: 1 }, { year: 1872, kansas: 10, kansasTotal: 10, neighbours: 0, neighboursTotal: 2.5, kansasSegments: 1, neighbourSegments: 0 }] } },
  climate: {
    data: {
      years: [2000, 2001], areas: [{ id: '20', name: 'Kansas' }], baselines: ['1901-2000'], latest: { year: 2001, month: 1 },
      elements: { tmpc: { label: 'Temperature', unit: '°F', scale: 10, annual: 'mean' } },
      values: { tmpc: { 20: [...Array(12).fill(500), 600, ...Array(11).fill(null)] } },
      normals: { '1901-2000': { tmpc: { 20: Array(12).fill(450) } } },
    },
  },
};
test('CSV rows and ranges come from the bundle', reactOnly, async t => {
  // JSX needs a transform that a plain node test lacks; the site's own TypeScript compiler provides it.
  const ts = await import('typescript').then(module => module.default);
  const { mkdtemp, writeFile, rm } = await import('node:fs/promises'), { join } = await import('node:path');
  const directory = await mkdtemp(join(path('node_modules'), '.story-cards-')), kitUrl = new URL('../app/living-welcome/stories/story-kit.mjs', import.meta.url).href;
  t.after(() => rm(directory, { recursive: true, force: true }));
  const load = async name => {
    const source = read(`app/living-welcome/stories/${name}.jsx`).replace("'./story-kit.mjs'", `'${kitUrl}'`);
    const output = ts.transpileModule(source, { compilerOptions: { jsx: ts.JsxEmit.ReactJSX, module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
    const file = join(directory, `${name}.mjs`);
    await writeFile(file, output);
    return import(`file://${file}`);
  };
  const iron = await load('iron-horse');
  assert.deepEqual({ min: iron.range(miniBundle.iron).min, max: iron.range(miniBundle.iron).max }, { min: 1861, max: 1872 });
  const ironCsv = iron.toCSV(miniBundle.iron);
  assert.equal(ironCsv.rows.length, 3);
  assert.deepEqual(ironCsv.rows[2], [1872, 10, 10, 0, 2.5, 1, 0]);
  const climate = await load('climate-stripes');
  const csv = climate.toCSV(miniBundle.climate, {});
  assert.deepEqual(csv.rows[1], [2000, 'Kansas', 'Temperature', 50, '°F', 5, '1901-2000', 12]);
  assert.deepEqual(csv.rows[2], [2001, 'Kansas', 'Temperature', 60, '°F', 15, '1901-2000', 1], 'an unfinished year compares only the months it has');
});

test('the section is mounted once, below the topic cards, and the 22 topics are untouched', siteOnly, () => {
  const welcome = read('app/living-welcome/welcome.jsx');
  assert.match(welcome, /const StorySection=lazy\(\(\)=>import\('\.\/stories\/StorySection\.jsx'\)\)/, 'the section is a lazy chunk');
  assert.doesNotMatch(welcome, /from '\.\/stories\//, 'nothing from the stories is in the welcome chunk');
  const mounted = welcome.indexOf('<StorySection '), field = welcome.indexOf('</section>', welcome.indexOf('className="discovery-field discovery-field--grouped"'));
  assert.ok(mounted > field && field > 0, 'after section.discovery-field');
  assert.ok(mounted < welcome.indexOf('{fullscreen&&touched&&<aside className="welcome-layer-demo"'), 'inside .welcome-discovery-content');
  assert.match(welcome, /<StorySection paused=\{paused\} reduced=\{reduced\} modal=\{modal\} compact=\{carousel\} onOpenChange=\{setStoryOpen\}\/>/);
  assert.match(welcome, /paused=\{paused\|\|modal\|\|storyOpen\|\|/, 'an open lab also holds the map stage');
  for (const name of ['StorySection.jsx', 'StoryLab.jsx', 'story-parts.jsx']) assert.doesNotMatch(read(`app/living-welcome/stories/${name}`), /topic-callout/, 'story cards are never counted as topic cards');
  assert.doesNotMatch(read('app/layer-workspaces.ts'), /iron-horse|climate-stripes/, 'stories are not topics');
});

test('stories stay out of the published datasets until the owner approves', siteOnly, async () => {
  const { DATASETS, PENDING_DATASETS, datasetCatalog } = await import('../scripts/local-data/datasets.mjs');
  assert.ok(PENDING_DATASETS.has('stories'));
  assert.ok(!DATASETS.has('stories'));
  assert.ok(!datasetCatalog().some(entry => entry.id === 'stories'));
  assert.match(read('scripts/local-data/datasets.mjs'), /pending owner publication approval; move into DATASETS only after the owner approves/i);
});

test('story preview data is a dev-server feature and validates its id', siteOnly, () => {
  const config = read('vite.config.ts');
  assert.match(config, /command === "serve" \? process\.env\.KFM_STORY_PREVIEW_DIR : undefined/);
  assert.match(config, /apply: "serve"/);
  assert.match(config, /\^\[a-z0-9\]\+\(\?:-\[a-z0-9\]\+\)\*\$/);
});
