import test, { before, after } from 'node:test';
import assert from 'node:assert/strict';
import { spawn } from 'node:child_process';
import { createServer, request, Agent } from 'node:http';
import { setTimeout as delay } from 'node:timers/promises';

// Exercise server/start.mjs itself: the GoDaddy proxy pools idle sockets, so an
// idle keep-alive connection must outlive Node's 5 s default and stay reusable.
let origin = process.env.KFM_NODE_TEST_ORIGIN;
let child;
const freePort = () => new Promise((resolve, reject) => {
  const probe = createServer().once('error', reject).listen(0, '127.0.0.1', () => {
    const { port } = probe.address(); probe.close(() => resolve(port));
  });
});
before(async () => {
  if (origin) return;
  const port = await freePort();
  child = spawn(process.execPath, ['server/start.mjs'], { env: { ...process.env, PORT: String(port), NODE_ENV: 'production' }, stdio: 'ignore' });
  origin = `http://127.0.0.1:${port}`;
  for (let attempt = 0; attempt < 100; attempt++) {
    if (child.exitCode !== null) throw new Error('server/start.mjs exited ' + child.exitCode);
    try { if ((await fetch(origin + '/robots.txt')).ok) return; } catch {}
    await delay(200);
  }
  throw new Error('server/start.mjs did not answer');
});
after(() => { child?.kill(); });

const get = (agent, path) => new Promise((resolve, reject) => {
  const req = request(new URL(path, origin), { agent }, response => {
    response.resume();
    response.on('end', () => resolve({ status: response.statusCode, keepAlive: response.headers['keep-alive'], reused: req.reusedSocket }));
  });
  req.setTimeout(10000, () => req.destroy(new Error('TEST_RESPONSE_TIMEOUT')));
  req.on('error', reject); req.end();
});

test('idle keep-alive sockets outlive the hosting proxy pool', async () => {
  const agent = new Agent({ keepAlive: true, maxSockets: 1 });
  try {
    const first = await get(agent, '/robots.txt');
    assert.equal(first.status, 200);
    assert.equal(first.keepAlive, 'timeout=65');
    await delay(6000);
    const second = await get(agent, '/robots.txt');
    assert.equal(second.status, 200);
    assert.equal(second.reused, true);
  } finally { agent.destroy(); }
});
