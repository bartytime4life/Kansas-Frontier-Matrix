import assert from 'node:assert/strict';

// Synthetic transport for hydrated UI acceptance only. These values are not
// provider observations, and every response is confined to the loopback app.
export function droughtBrowserFixtures(origin, { history = 'ready', unsupported = true } = {}) {
  const base = new URL(origin);
  assert.equal(base.protocol, 'http:');
  assert.ok(['127.0.0.1', 'localhost', '[::1]'].includes(base.hostname));
  assert.equal(base.pathname, '/');
  assert.equal(base.search + base.hash + base.username + base.password, '');
  assert.ok(['ready', 'held', 'failed'].includes(history));
  const weeks = Array.from({ length: 60 }, (_, index) => {
    const day = new Date(Date.UTC(2000, 0, 4) + index * 7 * 86400000);
    return {
      date: day.toISOString().slice(0, 10).replaceAll('-', ''),
      label: day.toLocaleDateString('en-US', { timeZone: 'UTC', month: 'short', day: 'numeric', year: 'numeric' }),
      shares: [70 + index % 20, 40 + index % 20, 20 + index % 10, 5 + index % 5, index % 3],
    };
  });
  const newest = weeks.at(-1);
  const hits = { history: 0, maps: [] };
  const heldHistory = [], heldMaps = new Map(), holdDates = new Set(), mapWaiters = new Map();
  let markHistoryRequested;
  const historyRequested = new Promise(resolve => { markHistoryRequested = resolve; });
  const waitForRequest = async (promise, label) => {
    let timeout;
    try {
      await Promise.race([promise, new Promise((_, reject) => {
        timeout = setTimeout(() => reject(new Error('Timed out waiting for '+label)), 10000);
      })]);
    } finally { clearTimeout(timeout); }
  };
  const knownWeek = date => {
    const week = weeks.find(week => week.date === date);
    assert.ok(week, 'the UI requested a date inside the synthetic history: '+date);
    return week;
  };
  const json = (call, requestId, value, status = 200) => call('Fetch.fulfillRequest', {
    requestId, responseCode: status,
    responseHeaders: [{ name: 'Content-Type', value: 'application/json' }],
    body: Buffer.from(JSON.stringify(value)).toString('base64'),
  });
  const series = () => ({ weeks: weeks.map(({ date, shares }) => ({ date, shares })), retrievedAt: new Date().toISOString(), source: 'synthetic browser fixture' });
  const map = date => ({
    date, data: { type: 'FeatureCollection', features: [] },
    kansas: knownWeek(date).shares,
    retrievedAt: new Date().toISOString(), source: 'synthetic browser fixture',
  });
  return {
    weeks, newest, hits, historyRequested,
    async setup(call) {
      if (!unsupported) return;
      // Exercise the application's own capability check and unsupported overlay;
      // do not insert an overlay or change the dock's DOM/CSS in the test.
      await call('Page.addScriptToEvaluateOnNewDocument', { source: `(() => {
        const getContext = HTMLCanvasElement.prototype.getContext;
        HTMLCanvasElement.prototype.getContext = function(kind, ...args) {
          return kind === 'webgl2' ? null : getContext.call(this, kind, ...args);
        };
      })();` });
    },
    async intercept({ requestId, request }, call) {
      const url = new URL(request.url);
      if (url.origin !== base.origin) return false;
      if (url.pathname === '/api/drought-series') {
        hits.history++;
        if (history === 'held') heldHistory.push({ call, requestId });
        else await json(call, requestId, history === 'failed' ? { error: 'Synthetic statistics outage' } : series(), history === 'failed' ? 503 : 200);
        markHistoryRequested();
        return true;
      }
      if (url.pathname !== '/api/drought-monitor') return false;
      const date = url.searchParams.get('date') ?? newest.date;
      hits.maps.push(date);
      if (holdDates.has(date)) {
        const pending = heldMaps.get(date) ?? [];
        pending.push({ call, requestId }); heldMaps.set(date, pending);
      } else await json(call, requestId, map(date));
      mapWaiters.get(date)?.(); mapWaiters.delete(date);
      return true;
    },
    async releaseHistory() {
      await waitForRequest(historyRequested, 'the history request');
      assert.ok(heldHistory.length, 'the real history request was held');
      history = 'ready';
      for (const { call, requestId } of heldHistory.splice(0)) await json(call, requestId, series());
    },
    holdMap(date) {
      knownWeek(date);
      assert.ok(!hits.maps.includes(date) && !holdDates.has(date), 'hold an uncached date before its first request');
      holdDates.add(date);
    },
    async releaseMap(date) {
      assert.ok(holdDates.has(date), 'only release a deliberately held map');
      if (!heldMaps.has(date)) {
        try { await waitForRequest(new Promise(resolve => mapWaiters.set(date, resolve)), 'map '+date); }
        finally { mapWaiters.delete(date); }
      }
      const pending = heldMaps.get(date) ?? [];
      assert.ok(pending.length, 'the selected historical map request was held');
      holdDates.delete(date); heldMaps.delete(date);
      for (const { call, requestId } of pending) await json(call, requestId, map(date));
    },
    assertDrained() {
      assert.equal(heldHistory.length + heldMaps.size + holdDates.size + mapWaiters.size, 0, 'all deliberately held drought requests were released');
    },
  };
}
