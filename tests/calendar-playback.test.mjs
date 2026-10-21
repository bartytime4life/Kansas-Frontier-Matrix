import assert from 'node:assert/strict';
import test from 'node:test';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';
import { componentHarness, findNode, settle } from './component-harness.mjs';
const js = ts.transpileModule(await readFile('app/calendar-sweep.ts','utf8'), { compilerOptions: { module: ts.ModuleKind.ESNext } }).outputText;
const calendar = await import('data:text/javascript;base64,' + Buffer.from(js).toString('base64'));
test('exhausted checked-empty playback clears intent and does not restart when skipping is disabled', async () => {
  const timers = new Map(); let nextTimer = 0;
  const h = await componentHarness(new URL('../app/compact-time-sweep.tsx', import.meta.url), {
    './calendar-sweep': calendar, './time-emblem': { TimeEmblem: 'emblem' }, './compact-time-sweep.css': {},
  }, { window: { setTimeout: fn => { timers.set(++nextTimer, fn); return nextTimer; }, clearTimeout: id => timers.delete(id) }, document: { hidden: false, addEventListener() {}, removeEventListener() {} } });
  const props = { value: {day:'2026-10-01',start:'2026-10-01',end:'2026-10-03',step:'days',before:null,showing:'B'},year:2026,years:[2026],today:'2026-10-21',sources:[{id:'quakes',state:'ready'}],open:true,onOpenChange(){},onPresent(){},onEra(){},onSeek: async next => { props.value = next; return {state:'empty', message:'No mapped records'}; } };
  const render = () => { const tree = h.render(h.exports.CompactTimeSweep, props); h.commit(); return tree; };
  const button = (tree, label) => findNode(tree, n => n.props?.['aria-label'] === label);
  const skip = tree => findNode(tree, n => n.type === 'input' && n.props.type === 'checkbox' && n.props.onChange.toString().includes('setSkipGaps'));
  let tree = render();
  for (let i = 0; i < 2; i++) { button(tree,'Next sweep frame').props.onClick(); await settle(); tree = render(); }
  for (let i = 0; i < 2; i++) { button(tree,'Previous sweep frame').props.onClick(); await settle(); tree = render(); }
  // Select the actual skip-empty checkbox, not the decorative animation switch.
  const skipControl = skip(tree);
  skipControl.props.onChange({target:{checked:true}}); tree = render();
  button(tree,'Play time sweep').props.onClick(); tree = render();
  for (const [id, fn] of [...timers]) { timers.delete(id); fn(); }
  await settle(); tree = render();
  assert.ok(button(tree,'Play time sweep'), 'exhaustion must show paused');
  skip(tree).props.onChange({target:{checked:false}}); tree = render();
  assert.ok(button(tree,'Play time sweep'), 'changing skip must not revive play intent');
  h.dispose();
});
