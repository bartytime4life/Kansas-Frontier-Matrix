import assert from 'node:assert/strict';
import test from 'node:test';
import { createTraffic, crossingZones, roadKey } from '../app/living-welcome/scenes/transport-traffic.mjs';

const line = (id, vertical = false, y = 0, kind = 4) => ({ id, kind, w: .18, y: [1900, 1901], n: 5, ds: 1, len: 4,
 xs: Array.from({ length: 5 }, (_, i) => vertical ? 0 : i - 2),
 zs: Array.from({ length: 5 }, (_, i) => vertical ? i - 2 : 0), ys: Array(5).fill(y) });
const unit = (l, extra = {}) => ({ l, dir: 1, v: .6, front: .09, rear: .09, years: [1900, 2030], ...extra });

test('physical road identity unifies dirt and paved fleets; overpasses are separate', () => {
 assert.equal(roadKey('ns1'), roadKey('H2'));
 assert.equal(roadKey('ew1'), roadKey('H4'));
 assert.equal(crossingZones({ a: line('H1'), b: line('H2', true) }).length, 1);
 assert.equal(crossingZones({ a: line('H1'), b: line('I2', true, .38, 5) }).length, 0);
});

test('crossing traffic stops, waits outside the junction, and resumes after it clears', () => {
 const a = unit(line('H1')), b = unit(line('H2', true)), zones = crossingZones({ a: a.l, b: b.l });
 const traffic = createTraffic([a, b], zones, () => 1950);
 let stopped = false, resumed = false, wasWaiting = false;
 for (let i = 1; i < 1500; i++) {
  const state = traffic.sample(i / 120), sa = state.get(a), sb = state.get(b);
  const inside = (u, s) => s.admitted && s.s + u.front > 2 - zones[0].radius && s.s - u.rear < 2 + zones[0].radius;
  assert.ok(!(inside(a, sa) && inside(b, sb)), `exclusive junction at ${i / 120}`);
  if (sb.speed < .001 && sb.waiting) stopped = true;
  if (wasWaiting && sb.speed > .4) resumed = true;
  wasWaiting ||= sb.waiting;
 }
 assert.ok(stopped); assert.ok(resumed);
});

test('long vehicles and mixed speeds keep headway on a shared physical lane', () => {
 const a = unit(line('H2'), { front: .18, rear: .3, v: .24 });
 const b = unit(line('ns1'), { v: .8 });
 const traffic = createTraffic([a, b], [], () => 1950);
 for (let i = 1; i < 3600; i++) {
  const state = traffic.sample(i / 120), sa = state.get(a), sb = state.get(b);
  for (const [u, v, us, vs] of [[a, b, sa, sb], [b, a, sb, sa]]) {
   const gap = ((vs.s - us.s) % u.cycle + u.cycle) % u.cycle - u.front - v.rear;
   assert.ok(gap >= .099, `following gap ${gap}`);
  }
 }
});

test('railway reservations include the trailing consist and a new era cannot appear inside it', () => {
 const train = unit(line('R1', false, 0, 2), { front: .15, rear: 1.2 });
 const car = unit(line('H2', true), { years: [1948.5, 2030] });
 const zones = crossingZones({ train: train.l, car: car.l });
 const traffic = createTraffic([train, car], zones, t => 1948 + t);
 let held = false;
 for (let i = 1; i < 1800; i++) {
  const state = traffic.sample(i / 120), st = state.get(train), sc = state.get(car);
  const inside = (u, s) => s.admitted && s.s + u.front > 2 - zones[0].radius && s.s - u.rear < 2 + zones[0].radius;
  assert.ok(!(inside(train, st) && inside(car, sc)));
  held ||= sc.waiting;
 }
 assert.ok(held);
});

test('pause, forward seek and rewind reproduce the exact traffic state', () => {
 const a = unit(line('H1')), b = unit(line('H2', true));
 const traffic = createTraffic([a, b], crossingZones({ a: a.l, b: b.l }), () => 1950);
 const at = t => [...traffic.sample(t).values()].map(s => ({ ...s }));
 const first = at(8.25);
 assert.deepEqual(at(8.25), first);
 at(25); at(0);
 assert.deepEqual(at(8.25), first);
});
