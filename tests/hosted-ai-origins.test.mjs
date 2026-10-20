import test from 'node:test';
import assert from 'node:assert/strict';
import {hostedAiOriginAllowed} from '../server/hosted-ai-origins.mjs';
import {createSitesQwenHandler} from '../server/sites-qwen-handler.mjs';

const supportedOrigins = [
  'https://kansasfrontiermatrix.com',
  'https://urdng3v1vk.preview.c38.airoapp.ai',
];
const retiredOrigin = 'https://q9r9beo47t.preview.c38.airoapp.ai';
const token = 's'.repeat(43);
const site = 'appgprj_6acd1aafe0d88191a4306ea2ab44ed91';
const actor = 'a'.repeat(64);
const adapterRequest = path => new Request('https://node.test/api/sites-qwen/v1/' + path, {
  method: path === 'jobs' ? 'POST' : 'GET',
  headers: {authorization: 'Bearer ' + token, 'x-kfm-site': site, 'x-kfm-site-actor': actor, 'content-type': 'application/json'},
  ...(path === 'jobs' ? {body: JSON.stringify({question: 'Synthetic question', mode: 'explore'})} : {}),
});

test('production and the current replacement preview remain authorized', () => {
  for (const origin of supportedOrigins) assert.equal(hostedAiOriginAllowed(origin), true, origin);
});

test('the deleted preview application is no longer authorized', () => {
  assert.equal(hostedAiOriginAllowed(retiredOrigin), false);
});

test('origin authorization retains exact string matching', () => {
  for (const origin of supportedOrigins) {
    const host = new URL(origin).host;
    for (const invalid of [
      origin + '/', origin + '/api/ai', origin + '?query=1', origin + '#fragment',
      origin + ':443', origin + '.evil.test', origin.toUpperCase(), ' ' + origin, origin + ' ',
      'http://' + host, 'https://user@' + host, 'https://' + host + '.',
    ]) assert.equal(hostedAiOriginAllowed(invalid), false, invalid);
  }
  for (const invalid of ['https://other.preview.c38.airoapp.ai', 'https://www.kansasfrontiermatrix.com', '', undefined, null, {}, new URL(supportedOrigins[0])]) {
    assert.equal(hostedAiOriginAllowed(invalid), false, String(invalid));
  }
});

test('authenticated Sites status still reaches the runtime on supported origins', async () => {
  for (const origin of supportedOrigins) {
    const forwarded = [];
    const handler = createSitesQwenHandler({token, origin, handle: async request => {
      forwarded.push(request.url);
      return Response.json({provider: 'hosted-qwen3', model: 'Qwen3-0.6B INT8 · server WebAssembly'});
    }});
    const response = await handler(adapterRequest('status'));
    assert.equal(response.status, 200, origin);
    assert.equal((await response.json()).model, 'onnx-community/Qwen3-0.6B-ONNX');
    assert.deepEqual(forwarded, [origin + '/api/ai/status']);
  }
});

test('valid Sites credentials cannot authorize the retired origin or start runtime work', async () => {
  let calls = 0;
  const handler = createSitesQwenHandler({token, origin: retiredOrigin, handle: async () => {
    calls++;
    throw new Error('Retired origin must be denied before runtime access');
  }});
  for (const path of ['status', 'jobs']) {
    const response = await handler(adapterRequest(path));
    assert.equal(response.status, 401, path);
    assert.equal((await response.json()).reasonCode, 'SITES_QWEN_UNAUTHORIZED');
    assert.equal(response.headers.get('set-cookie'), null);
  }
  assert.equal(calls, 0);
});
