import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import * as vinextServer from 'vinext/shims/server';

const require = createRequire(import.meta.url);
const nativeServer = require('next/server');

test('the installed Next runtime and lock agree outside the affected cache-race range', async () => {
  const manifest = JSON.parse(await readFile(new URL('../package.json', import.meta.url), 'utf8'));
  const lock = JSON.parse(await readFile(new URL('../package-lock.json', import.meta.url), 'utf8'));
  const installed = require('next/package.json').version;
  assert.equal(installed, manifest.dependencies.next);
  assert.equal(installed, lock.packages['node_modules/next'].version);
  const match = /^(\d+)\.(\d+)\.(\d+)$/.exec(installed);
  assert.ok(match, 'reviewed stable package version');
  const [, major, minor, patch] = match.map(Number);
  // GHSA-vc7v-qv4w-wrv8 starts at 16.2.0; GHSA-mfr8-8qww-v76h
  // starts at 16.3.0. Both end at 16.4.4 and are patched in 16.4.5.
  assert.ok(!(major === 16 && (minor === 2 || minor === 3 || minor === 4 && patch <= 4)),
    `Next ${installed} is in the reviewed affected range`);
});

for (const [name, { NextRequest, NextResponse }] of [['installed Next', nativeServer], ['vinext production shim', vinextServer]]) {
  test(`${name} preserves route URLs, zero-valued JSON and scoped response cookies`, async () => {
    const request = new NextRequest('https://example.invalid/api/fixture?source=synthetic&value=0', {
      headers: { cookie: 'kfm_fixture=bounded', 'x-fixture': 'local-only' },
    });
    assert.equal(request.nextUrl.pathname, '/api/fixture');
    assert.equal(request.nextUrl.searchParams.get('value'), '0');
    assert.equal(request.cookies.get('kfm_fixture').value, 'bounded');
    assert.equal(request.headers.get('x-fixture'), 'local-only');
    const payload = { source: 'synthetic', value: 0, matched: false };
    const response = NextResponse.json(payload, { status: 202, headers: { 'cache-control': 'no-store' } });
    response.cookies.set('kfm_fixture', 'bounded', { httpOnly: true, secure: true, sameSite: 'strict', path: '/api/fixture' });
    assert.equal(response.status, 202);
    assert.equal(response.headers.get('cache-control'), 'no-store');
    assert.deepEqual(await response.json(), payload);
    const cookie = response.headers.get('set-cookie');
    for (const part of ['kfm_fixture=bounded', 'Path=/api/fixture', 'HttpOnly', 'Secure', 'SameSite=Strict']) {
      assert.ok(cookie.toLowerCase().includes(part.toLowerCase()), `${name}: ${part}`);
    }
    const redirect = NextResponse.redirect(new URL('/explore', request.url), 307);
    assert.equal(redirect.status, 307);
    assert.equal(redirect.headers.get('location'), 'https://example.invalid/explore');
  });
}
