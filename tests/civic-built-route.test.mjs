import test from 'node:test';
import assert from 'node:assert/strict';

// Production Fetch handler acceptance, not a browser or hosting claim.
test('built civic route renders discovery tools without a configured database or AI', async () => {
  const { default: handler } = await import('../dist/server/index.js');
  const response = await handler(new Request('https://kansasfrontiermatrix.com/civic'));
  assert.equal(response.status, 200);
  assert.match(response.headers.get('content-type'), /text\/html/);
  const html = await response.text();
  for (const label of ['Your civic source desk', 'Load county choices', 'Your moral compass', 'Copy question', 'Source check &amp; limitations']) assert.ok(html.includes(label), label);
  assert.match(html, /not establish that records are loaded into KFM/);
  assert.match(html, /No candidate ranking or candidate records are loaded here/);
  assert.match(html, /About (?:<!-- -->)?civic atlas/);
  assert.doesNotMatch(html, /civic_county_reference_points|sqlite-intake-result|county-directory-candidates-research/);
});

test('built topic route exposes civic navigation', async () => {
  const { default: handler } = await import('../dist/server/index.js');
  const response = await handler(new Request('https://kansasfrontiermatrix.com/topics'));
  assert.equal(response.status, 200);
  const html = await response.text();
  assert.match(html, /href="\/civic"/);
  assert.match(html, /Government &amp; civic atlas/);
});
