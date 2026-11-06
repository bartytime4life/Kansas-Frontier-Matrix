import assert from 'node:assert/strict';
import test from 'node:test';
import vm from 'node:vm';
import { installRenderDiagnostics } from './render-performance-browser-fixtures.mjs';

test('render diagnostics retain bounded React console stacks and preserve native logging', () => {
  const logged = [], window = { addEventListener() {} }, receiver = { error(...args) { logged.push({ receiver: this, args }); } };
  class Map {}
  class WebGL2RenderingContext {}
  class PerformanceObserver { observe() {} }
  vm.runInNewContext(`(${installRenderDiagnostics})(Map);`, { window, console: receiver, Map, WebGL2RenderingContext, PerformanceObserver, WeakMap, performance: { now: () => 1 } });
  const error = new Error('render callback failed');
  receiver.error(error, 'The above error occurred in a React component');
  assert.equal(logged[0].receiver, receiver);
  assert.equal(logged[0].args[0], error, 'the original exception still reaches native logging');
  assert.equal(logged[0].args[1], 'The above error occurred in a React component');
  assert.match(window.__kfmRenderDiagnostics.consoleErrors[0][0], /render callback failed/);
  assert.match(window.__kfmRenderDiagnostics.consoleErrors[0][0], /render-diagnostics.test.mjs/);
  for (let i = 0; i < 40; i++) receiver.error('x'.repeat(13000));
  assert.equal(window.__kfmRenderDiagnostics.consoleErrors.length, 32);
  assert.equal(window.__kfmRenderDiagnostics.consoleErrors[0][0].length, 12000);
  const unprintable = { get stack() { throw Error('unprintable'); } };
  assert.doesNotThrow(() => receiver.error(unprintable));
  assert.equal(logged.at(-1).args[0], unprintable, 'diagnostic formatting never changes the native argument');
  assert.equal(window.__kfmRenderDiagnostics.consoleErrors.at(-1)[0], '[unprintable console value]');
});
