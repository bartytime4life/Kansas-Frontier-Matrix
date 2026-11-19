// A share link names an exact public snapshot and a bounded, declarative UI state.
// It cannot name a resource to fetch or execute a command.
const object = value => value !== null && typeof value === 'object' && !Array.isArray(value);
const fields = new Set(['query', 'category', 'metric', 'from', 'to', 'minValue', 'maxValue', 'sort', 'direction',
  'compareMode', 'compareA', 'compareB', 'compareAFrom', 'compareATo', 'compareBFrom', 'compareBTo', 'view',
  'selectedId', 'element', 'baseline', 'area', 'xMetric', 'yMetric', 'showFit', 'rankDirection', 'summaryGroup',
  'scienceFrom', 'scienceTo']);
const validStory = value => typeof value === 'string' && /^[a-z]+(?:-[a-z]+)*$/.test(value) && value.length <= 64;
const validHash = value => typeof value === 'string' && /^[a-f0-9]{64}$/.test(value);
const numberFields = new Set(['from', 'to', 'minValue', 'maxValue', 'compareAFrom', 'compareATo', 'compareBFrom', 'compareBTo', 'scienceFrom', 'scienceTo']);
const choices = { view: ['map', 'trend', 'chart', 'relationships'], direction: ['asc', 'desc'], rankDirection: ['asc', 'desc'], compareMode: ['category', 'period'] };
function validControls(value) {
  return object(value) && Object.keys(value).length <= fields.size && Object.entries(value).every(([key, v]) =>
    fields.has(key) && (key === 'showFit' ? typeof v === 'boolean' : numberFields.has(key) ?
      v === null || v === '' || (typeof v === 'number' || typeof v === 'string') && Number.isFinite(Number(v)) && Math.abs(Number(v)) <= 1e12 :
      key === 'selectedId' && v === null || typeof v === 'string' && v.length <= (key === 'query' ? 300 : 200) && (!choices[key] || choices[key].includes(v)))) &&
    JSON.stringify(value).length <= 4000;
}
const validTime = value => value === null || typeof value === 'number' && Number.isFinite(value) && Math.abs(value) <= 1e6;

export function encodeLabView({ story, controls = {}, time = null, snapshotSha256 } = {}) {
  if (!validStory(story) || !validHash(snapshotSha256) || !validControls(controls) || !validTime(time)) throw new TypeError('Invalid Labs view');
  const raw = new TextEncoder().encode(JSON.stringify({ v: 1, s: story, h: snapshotSha256, c: controls, t: time }));
  return btoa(String.fromCharCode(...raw)).replaceAll('+', '-').replaceAll('/', '_').replace(/=+$/, '');
}

export function decodeLabView(token, { story, snapshotSha256 } = {}) {
  if (!validStory(story) || !validHash(snapshotSha256) || typeof token !== 'string' || token.length > 8192 || !/^[A-Za-z0-9_-]+$/.test(token)) return null;
  try {
    const base64 = token.replaceAll('-', '+').replaceAll('_', '/');
    const raw = Uint8Array.from(atob(base64), value => value.charCodeAt(0));
    const value = JSON.parse(new TextDecoder('utf-8', { fatal: true }).decode(raw));
    if (!object(value) || Object.keys(value).sort().join(',') !== 'c,h,s,t,v' || value.v !== 1 || value.s !== story ||
        value.h !== snapshotSha256 || !validControls(value.c) || !validTime(value.t)) return null;
    return { controls: value.c, time: value.t };
  } catch { return null; }
}
