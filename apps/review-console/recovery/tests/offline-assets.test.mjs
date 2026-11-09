import test from 'node:test';
import assert from 'node:assert/strict';
import { offlineAssetUrls } from '../src/offline-assets.ts';

test('cache preparation includes actual module/style assets even without performance entries', () => {
  const urls = offlineAssetUrls('http://127.0.0.1:4179/#review', [], ['/assets/app.js', '/assets/app.css']);
  assert.deepEqual(urls, [
    'http://127.0.0.1:4179/',
    'http://127.0.0.1:4179/assets/app.js',
    'http://127.0.0.1:4179/assets/app.css',
    'http://127.0.0.1:4179/baseline-evidence.json',
  ]);
});

test('cache candidates cannot broaden into providers, APIs or an unbounded list', () => {
  const urls = offlineAssetUrls('https://desk.example/', [
    'https://provider.example/observations', '/api/private', '/@vite/client', '/__vite/module',
    'javascript:alert(1)', ...Array.from({length:200}, (_,i)=>`/assets/${i}.js`),
  ], ['/assets/app.js', '/assets/app.js']);
  assert.equal(urls.length,180);
  assert.equal(new Set(urls).size,180);
  assert.ok(urls.every(url => url.startsWith('https://desk.example/')));
  assert.ok(!urls.some(url=>url.includes('/api/') || url.includes('vite') || url.includes('javascript:')));
  assert.equal(urls[1],'https://desk.example/assets/app.js');
});
