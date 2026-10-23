// Deterministic staging for the illustrative welcome, not a traffic model or
// observations. Fixed steps make playback, pause, seek and rewind agree.
const STEP = 1 / 120, GAP = .10;
const mod = (a, b) => ((a % b) + b) % b;
export const roadKey = id => ({ ns1: 'H2', ew0: 'H1', ew1: 'H4', ew3: 'H3' }[id] || id);

/** At-grade intersections, including railway crossings; overpasses stay free. */
export function crossingZones(lines) {
 const unique = [...new Map(Object.values(lines).filter(l => l.kind !== 1 && l.kind !== 6).map(l => [roadKey(l.id), l])).values()];
 const zones = [];
 for (let a = 0; a < unique.length; a++) for (let b = a + 1; b < unique.length; b++) {
  const l = unique[a], r = unique[b];
  // Branch joins are rail dispatch boundaries, not road junctions.
  if (l.kind === 2 && r.kind === 2) continue;
  const stride = 4;
  for (let i = 0; i < l.n - 1; i += stride) for (let j = 0; j < r.n - 1; j += stride) {
   const ii = Math.min(l.n - 1, i + stride), jj = Math.min(r.n - 1, j + stride);
   const ax = l.xs[ii] - l.xs[i], az = l.zs[ii] - l.zs[i], bx = r.xs[jj] - r.xs[j], bz = r.zs[jj] - r.zs[j];
   const det = ax * bz - az * bx;
   if (Math.abs(det) < 1e-8) continue;
   const dx = r.xs[j] - l.xs[i], dz = r.zs[j] - l.zs[i];
   const u = (dx * bz - dz * bx) / det, v = (dx * az - dz * ax) / det;
   if (u < 0 || u > 1 || v < 0 || v > 1) continue;
   const ly = l.ys[i] + (l.ys[ii] - l.ys[i]) * u, ry = r.ys[j] + (r.ys[jj] - r.ys[j]) * v;
   if (Math.abs(ly - ry) > .16) continue;
   const x = l.xs[i] + ax * u, z = l.zs[i] + az * u;
   // Merge nearby crossings so a long vehicle reserves the whole junction.
   let zone = zones.find(c => Math.hypot(c.x - x, c.z - z) < .32);
   if (!zone) { zone = { x, z, routes: {}, radius: .16 }; zones.push(zone); }
   zone.routes[roadKey(l.id)] = (i + (ii - i) * u) * l.ds;
   zone.routes[roadKey(r.id)] = (j + (jj - j) * v) * r.ds;
   zone.radius = Math.max(zone.radius, l.w / 2 + .05, r.w / 2 + .05);
  }
 }
 return zones;
}

/** Units carry measured model extents, era limits and a physical route. */
export function createTraffic(units, zones, yearAt) {
 const groups = new Map(), state = new Map(), owners = new Map();
 const laneKey = u => `${roadKey(u.l.id)}:${u.dir}`;
 for (const u of units) {
  const key = laneKey(u);
  if (!groups.has(key)) groups.set(key, []);
  groups.get(key).push(u);
  u.crossings = zones.filter(c => c.routes[roadKey(u.l.id)] !== undefined).map(c => ({ zone: c, at: u.dir > 0 ? c.routes[roadKey(u.l.id)] : u.l.len - c.routes[roadKey(u.l.id)] })).sort((a, b) => a.at - b.at);
 }
 for (const group of groups.values()) {
  const cycle = group[0].l.len + Math.max(...group.map(u => u.front + u.rear)) + 1;
  // All eras share slots on a physical lane, including a paved-over dirt road.
  group.forEach((u, i) => { u.cycle = cycle; u.start = mod((i / group.length + (u.dir < 0 ? .37 : .08)) * cycle, cycle); });
 }
 const active = (u, year) => year >= Math.max(u.years[0] - 1.6, u.l.y[1] + 1) && year <= Math.min(u.years[1] + 1.6, u.l.gone ?? 9999);
 let frame = 0;
 function reset() {
  frame = 0; owners.clear();
  for (const u of units) state.set(u, { s: u.start - .4, speed: u.v, waiting: false, admitted: false });
 }
 function step() {
  const year = yearAt((frame + 1) * STEP), moving = units.filter(u => active(u, year));
  for (const u of units) if (!active(u, year)) state.get(u).admitted = false;
  for (const [zone, u] of owners) {
   const at = u.crossings.find(c => c.zone === zone).at, s = state.get(u).s;
   if (!active(u, year) || s - u.rear > at + zone.radius + GAP || s + u.front < at - zone.radius - .5) owners.delete(zone);
  }
  // Railway priority only applies before a road user has entered the junction.
  const ordered = [...moving].sort((a, b) => (b.l.kind === 2) - (a.l.kind === 2));
  const next = new Map();
  for (const u of ordered) {
   const st = state.get(u), s = st.s;
   // A newly appearing era cannot materialize inside occupied traffic.
   if (!st.admitted) {
    const blocked = moving.some(other => other !== u && state.get(other).admitted && laneKey(u) === laneKey(other) && (
     mod(state.get(other).s - s, u.cycle) < u.front + other.rear + GAP ||
     mod(s - state.get(other).s, u.cycle) < other.front + u.rear + GAP
    )) || u.crossings.some(({ zone, at }) => s + u.front >= at - zone.radius - GAP && s - u.rear <= at + zone.radius + GAP && owners.has(zone) && owners.get(zone) !== u);
    if (blocked) continue;
    st.admitted = true;
   }
   let clearance = Infinity;
   for (const other of groups.get(laneKey(u))) {
    if (other === u || !active(other, year) || !state.get(other).admitted) continue;
    const ahead = mod(state.get(other).s - s, u.cycle);
    clearance = Math.min(clearance, ahead - other.rear - u.front - GAP);
   }
   for (const { zone, at } of u.crossings) {
    if (s - u.rear > at + zone.radius + GAP || s + u.front < at - zone.radius - .7) continue;
    const owner = owners.get(zone), stop = at - zone.radius - u.front - GAP;
    if (owner && owner !== u) clearance = Math.min(clearance, Math.max(0, stop - s));
    else if (s + u.front >= at - zone.radius - .25) owners.set(zone, u);
   }
   // Brake before the stop line, accelerate gently after it clears. Clamp the
   // actual displacement as well, so low frame rates cannot tunnel a crossing.
   const target = Math.min(u.v, Math.sqrt(Math.max(0, 2 * .8 * clearance)));
   const speed = Math.max(0, Math.min(target, st.speed + .55 * STEP));
   const advance = Math.max(0, Math.min(speed * STEP, clearance));
   next.set(u, { s: mod(s + advance + .4, u.cycle) - .4, speed: advance / STEP, waiting: advance < u.v * STEP * .8, admitted: true });
  }
  for (const [u, st] of next) state.set(u, st);
  frame++;
 }
 reset();
 return {
  sample(t) {
   const target = Math.max(0, Math.floor(t / STEP + 1e-7));
   if (target < frame) reset();
   while (frame < target) step();
   return state;
  },
 };
}
