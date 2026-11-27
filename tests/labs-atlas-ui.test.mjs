import assert from 'node:assert/strict';
import test from 'node:test';
import * as registry from '../app/living-welcome/stories/registry.mjs';
import * as atlas from '../app/labs/atlas-model.mjs';
import { PUBLIC_LAB_SNAPSHOTS } from '../app/labs/public-snapshots.mjs';
import { componentHarness, findNode } from './component-harness.mjs';

function atlasHarness(globals = {}, bundle = { useStoryBundle() { throw new Error('Unexpected source read'); } }) {
  return componentHarness('app/labs/page.jsx', {
    'next/link': { default: 'a' },
    '../living-welcome/stories/registry.mjs': registry,
    '../living-welcome/stories/story-parts.jsx': {},
    '../living-welcome/stories/useStoryBundle.js': bundle,
    './atlas-model.mjs': atlas,
    './public-snapshots.mjs': { PUBLIC_LAB_SNAPSHOTS },
    '../living-welcome/stories/story-kit.mjs': {},
    '../living-welcome/stories/science-model.mjs': {},
    '../living-welcome/stories/stories.css': {},
    './page.module.css': { default: {} },
  }, globals, '\nexport { ResearchCard, ConnectedWorkspaces };');
}

test('the Atlas opens on a catalogue that can filter before source previews run', async t => {
  const harness = await atlasHarness();
  t.after(() => harness.dispose());
  const draw = () => harness.render(harness.exports.default);
  const tree = draw();
  const finder = findNode(tree, node => node.props?.id === 'research-labs');
  assert.ok(finder);
  assert.ok(findNode(finder, node => node.props?.type === 'search'));
  assert.equal(findNode(tree, node => node.type === 'a' && node.props.href === '/science').props.children, '← Science & Labs');
  assert.ok(findNode(tree, node => node.type === 'a' && node.props.href === '/labs/observatory'));
  assert.ok(findNode(tree, node => node.type === 'a' && node.props.href === '/labs/signals'));
  assert.equal(findNode(tree, node => node.type === harness.exports.ConnectedWorkspaces), undefined);

  const filter = findNode(finder, node => node.props?.['aria-label'] === 'Data availability');
  filter.props.onChange({ target: { value: 'bundled' } });
  const bundled = draw();
  const first = findNode(bundled, node => node.type === harness.exports.ResearchCard && !node.props.hidden);
  assert.ok(first && Object.hasOwn(PUBLIC_LAB_SNAPSHOTS, first.props.story.id));
  assert.equal(first.props.previews, false);
  assert.equal(findNode(bundled, node => node.type === 'option' && node.props.value === 'ready'), undefined);
  assert.ok(findNode(bundled, node => node.type === 'button' && node.props.children === 'Show source previews'));
});

test('a source preview stays idle until enabled and near the viewport', async t => {
  const enabled = [];
  let enter;
  class IntersectionObserver {
    constructor(callback) { enter = () => callback([{ isIntersecting: true }]); }
    observe() {}
    disconnect() {}
  }
  const harness = await atlasHarness({ IntersectionObserver }, {
    useStoryBundle(_id, options) { enabled.push(options.enabled); return { state: 'idle' }; },
  });
  t.after(() => harness.dispose());
  const card = (previews, hidden = false) => harness.render(harness.exports.ResearchCard, {
    story: registry.storyById('river-memory'), previews, hidden, onState() {}, onOpen() {},
  });
  const resting = card(false);
  resting.props.ref.current = {};
  harness.commit();
  assert.equal(enabled.at(-1), false);
  assert.equal(enter, undefined);
  assert.equal(findNode(resting, node => node.props?.role === 'img'), undefined);
  card(true); harness.commit();
  assert.equal(enabled.at(-1), false);
  enter(); card(true);
  assert.equal(enabled.at(-1), true);
  card(true, true);
  assert.equal(enabled.at(-1), false);
});
