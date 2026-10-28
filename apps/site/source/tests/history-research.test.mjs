import { test } from 'node:test';
import assert from 'node:assert/strict';
import { componentHarness } from './component-harness.mjs';

const css = new Proxy({}, { get: (_, key) => String(key) });
function nodes(tree) {
  const result = [];
  function visit(node) {
    if (!node || typeof node !== 'object') return;
    result.push(node);
    for (const child of [node.props?.children].flat(Infinity)) visit(child);
  }
  visit(tree);
  return result;
}
function content(node) {
  if (typeof node === 'string' || typeof node === 'number') return String(node);
  return [node?.props?.children].flat(Infinity).map(child => child == null ? '' : content(child)).join(' ');
}

test('public history page shows a hold without fetching, rendering records or offering exports', () => {
  const calls = [];
  const h = componentHarness;
  return h('app/history/people-events/page.tsx', {
    '../../downloads/workspace.module.css': { default: css },
    '../../history-research.module.css': { default: css },
  }, { fetch: (...args) => { calls.push(args); throw new Error('No catalogue request is permitted'); } }).then(view => {
    try {
      const tree = view.render(view.exports.default, {}); view.commit();
      assert.match(content(tree), /unavailable pending review and approval for public release/);
      assert.equal(nodes(tree).filter(node => node.props?.role === 'status').length, 1);
      assert.equal(nodes(tree).filter(node => ['input', 'select', 'article', 'table'].includes(node.type)).length, 0);
      assert.equal(nodes(tree).filter(node => node.props?.download || /people-events\.(json|csv)/.test(node.props?.href ?? '')).length, 0);
      assert.deepEqual(calls, []);
    } finally { view.dispose(); }
  });
});

test('hold page preserves archive, book reader and reviewed knowledge navigation', async () => {
  const view = await componentHarness('app/history/people-events/page.tsx', {
    '../../downloads/workspace.module.css': { default: css },
    '../../history-research.module.css': { default: css },
  });
  try {
    const tree = view.render(view.exports.default, {});
    const links = nodes(tree).filter(node => node.type === 'a').map(node => node.props.href);
    assert.deepEqual(links, ['/downloads#history', '/knowledge', '/history/prentis-1909']);
  } finally { view.dispose(); }
});
