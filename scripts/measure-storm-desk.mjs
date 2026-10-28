// Real browser/provider capture. Deliberately outside *.test.mjs and fixture
// interception. Requires an installed Chrome/Chromium; default is headful.
import { spawn } from 'node:child_process';
import { mkdtemp, mkdir, writeFile, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { resolve, join } from 'node:path';
import { StormDeskNetwork, summarizeStormDeskNetwork } from './storm-desk-network.mjs';

const args = process.argv.slice(2);
const option = (name, fallback) => args.includes(name) ? args[args.indexOf(name) + 1] : fallback;
const origin = new URL(option('--origin', 'http://127.0.0.1:5182'));
if (origin.pathname !== '/' || origin.search || origin.hash || origin.username || origin.password ||
  !(origin.protocol === 'https:' || origin.protocol === 'http:' && ['127.0.0.1', 'localhost', '[::1]'].includes(origin.hostname))) throw new Error('Use an uncredentialed HTTPS or loopback origin');
const expected = option('--expected-digest');
if (!/^sha256:[a-f0-9]{64}$/.test(expected ?? '')) throw new Error('Required: --expected-digest sha256:<application-input digest>');
const seconds = Number(option('--seconds', '20'));
const hiddenSeconds = Number(option('--hidden-seconds', '330'));
const soakSeconds = Number(option('--soak-seconds', '0'));
if (![seconds, hiddenSeconds, soakSeconds].every(n => Number.isFinite(n) && n >= 0 && n <= 7200) || seconds < 1) throw new Error('Invalid bounded sampling duration');
const width = Number(option('--width', '1440')), height = Number(option('--height', '900'));
if (![width, height].every(n => Number.isSafeInteger(n) && n >= 320 && n <= 3840)) throw new Error('Invalid viewport');
const out = resolve(option('--output', 'storm-desk-performance.json'));
const network = new StormDeskNetwork();
const receipt = {kind: 'real-browser-provider-capture', startedAt: new Date().toISOString(), origin: origin.origin,
  configuration: {seconds, hiddenSeconds, soakSeconds, width, height, headless: args.includes('--headless'), cacheDisabled: false,
    slowNetwork: args.includes('--slow-network'),
    chrome: option('--chrome', process.env.KFM_TEST_CHROME ?? 'google-chrome')},
  status: 'incomplete', phases: [], checks: [],
  boundaries: ['No provider interception or synthetic data is installed.', 'Viewport emulation is not native mobile GPU acceptance.',
    'rAF cadence is page scheduling; MapLibre render callbacks are renderer work. Neither proves GPU-presented FPS.',
    'Transfer counts cover this browser and attached workers, not upstream adapter egress.',
    'No prior-revision bandwidth/FPS improvement is inferred from one capture.']};
let child, profile, closed = false, sequence = 0, buffer = '', stderr = '', call;
const pending = new Map(), listeners = new Set();
const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
try {
  const response = await fetch(new URL('/api/build', origin), {redirect: 'error', signal: AbortSignal.timeout(10000), cache: 'no-store'});
  const body = await response.text();
  if (body.length > 4096 || !response.ok) throw new Error('Application identity unavailable');
  receipt.identity = JSON.parse(body);
  if (receipt.identity.profile !== 'kfm.godaddy-application-inputs/v1' || receipt.identity.application !== 'urdng3v1vk' || receipt.identity.sourceDigest !== expected) throw new Error('Application identity mismatch: no browser test was started');
  profile = await mkdtemp(join(tmpdir(), 'kfm-storm-performance-'));
  child = spawn(receipt.configuration.chrome, [
    '--remote-debugging-pipe', `--user-data-dir=${profile}`, '--no-first-run', '--no-default-browser-check',
    ...(receipt.configuration.headless ? ['--headless=new'] : []), 'about:blank',
  ], {stdio: ['ignore', 'ignore', 'pipe', 'pipe', 'pipe']});
  const fail = error => {closed = true; for (const item of pending.values()) item.reject(error); pending.clear();};
  child.on('error', fail); child.on('exit', code => fail(new Error(`Browser exited ${code}: ${stderr.slice(-2000)}`)));
  child.stderr.on('data', chunk => {stderr = (stderr + chunk).slice(-8000);});
  child.stdio[4].on('data', chunk => {
    buffer += chunk;
    let split;
    while ((split = buffer.indexOf('\0')) >= 0) {
      const message = JSON.parse(buffer.slice(0, split)); buffer = buffer.slice(split + 1);
      if (message.id) {
        const item = pending.get(message.id); if (!item) continue;
        pending.delete(message.id);
        if (message.error) item.reject(new Error(JSON.stringify(message.error))); else item.resolve(message.result);
      } else for (const listener of listeners) listener(message);
    }
  });
  call = (method, params = {}, sessionId) => new Promise((resolve, reject) => {
    if (closed) return reject(new Error(`Browser unavailable: ${stderr}`));
    const id = ++sequence, timer = setTimeout(() => {pending.delete(id); reject(new Error(`CDP timeout: ${method}`));}, 30000);
    pending.set(id, {resolve: value => {clearTimeout(timer); resolve(value);}, reject: error => {clearTimeout(timer); reject(error);}});
    child.stdio[3].write(JSON.stringify({id, method, params, ...(sessionId ? {sessionId} : {})}) + '\0');
  });
  receipt.browser = await call('Browser.getVersion');
  receipt.gpu = (await call('SystemInfo.getInfo')).gpu;
  const {targetId} = await call('Target.createTarget', {url: 'about:blank'});
  const {sessionId} = await call('Target.attachToTarget', {targetId, flatten: true});
  const page = (method, params = {}) => call(method, params, sessionId);
  const evaluate = async expression => {
    const result = await page('Runtime.evaluate', {expression, returnByValue: true, awaitPromise: true});
    if (result.exceptionDetails) throw new Error(JSON.stringify(result.exceptionDetails));
    return result.result.value;
  };
  const sessions = new Set([sessionId]), attachmentErrors = [];
  const enableNetwork = async session => {
    await call('Network.enable', {}, session);
    if (receipt.configuration.slowNetwork) await call('Network.emulateNetworkConditions', {
      offline:false, latency:300, downloadThroughput:200000, uploadThroughput:100000, connectionType:'cellular3g',
    }, session);
  };
  listeners.add(message => {
    if (!sessions.has(message.sessionId)) return;
    if (message.method.startsWith('Network.')) network.event(message.method, message.params, message.sessionId);
    if (message.method === 'Target.attachedToTarget') {
      const worker = message.params.sessionId; sessions.add(worker);
      void (async () => {
        await enableNetwork(worker);
        await call('Target.setAutoAttach', {autoAttach: true, waitForDebuggerOnStart: true, flatten: true}, worker);
        await call('Runtime.runIfWaitingForDebugger', {}, worker);
      })().catch(error => {attachmentErrors.push(String(error));});
    }
  });
  await page('Page.enable'); await page('Runtime.enable'); await enableNetwork(sessionId);
  await page('Target.setAutoAttach', {autoAttach: true, waitForDebuggerOnStart: true, flatten: true});
  await page('Emulation.setDeviceMetricsOverride', {width, height, deviceScaleFactor: 1, mobile: width < 600});
  await page('Page.addScriptToEvaluateOnNewDocument', {source: `(() => {
    let last = null, intervals = [], count = 0, longTasks = 0, longTaskMs = 0;
    const tick = now => { if (!document.hidden) { if (last !== null && intervals.length < 60000) intervals.push(now-last); last = now; count++; } else last = null; requestAnimationFrame(tick); };
    document.addEventListener('visibilitychange', () => { last = null; });
    requestAnimationFrame(tick);
    if (PerformanceObserver.supportedEntryTypes.includes('longtask')) new PerformanceObserver(list => { for (const e of list.getEntries()) {longTasks++;longTaskMs+=e.duration;} }).observe({type:'longtask'});
    window.__kfmBrowserSample = {reset(){last=null;intervals=[];count=0;longTasks=0;longTaskMs=0;}, snapshot(){return {count, intervals:intervals.slice(), longTasks, longTaskMs, hidden:document.hidden, visibility:document.visibilityState};}};
  })();`});
  const url = new URL(origin); url.searchParams.set('stormPerf', '1');
  await page('Page.navigate', {url: url.href});
  const wait = async (expression, label, timeout = 30000) => {
    const end = Date.now() + timeout;
    while (Date.now() < end) {if (await evaluate(expression)) return; await sleep(200);}
    throw new Error('Timed out: ' + label);
  };
  const click = async selector => {
    await wait(`!!document.querySelector(${JSON.stringify(selector)})`, selector);
    const clicked = await evaluate(`(() => {const e=document.querySelector(${JSON.stringify(selector)});if(e.disabled)return false;e.click();return true;})()`);
    if (!clicked) throw new Error('Control disabled: ' + selector);
  };
  const snapshot = async () => ({at: new Date().toISOString(), browser: await evaluate('window.__kfmBrowserSample.snapshot()'),
    map: await evaluate('window.__kfmStormDeskPerf?.snapshot() ?? null'),
    heap: await page('Runtime.getHeapUsage'), dom: await page('Memory.getDOMCounters'),
    controls: await evaluate(`({radar:document.querySelector('.noaa-radar-loop')?.innerText, optional:[...document.querySelectorAll('.category-map-dock-context button')].map(e=>({title:e.textContent,pressed:e.getAttribute('aria-pressed')})),runtime:document.querySelector('.runtime-overlay')?.textContent})`)});
  const phase = async (name, duration, action = async () => {}, settleBeforeSampling = false) => {
    network.phase = settleBeforeSampling ? name + '-transition' : name;
    await evaluate('window.__kfmBrowserSample.reset()');
    const entry = {name, startedAt: new Date().toISOString()}; receipt.phases.push(entry);
    entry.before = await snapshot(); await action();
    if (settleBeforeSampling) {
      entry.transitionBefore = entry.before;
      network.phase = name;
      await evaluate('window.__kfmBrowserSample.reset()');
      entry.before = await snapshot();
    }
    entry.sampleStartedAt = new Date().toISOString();
    // Real elapsed time, never virtual time or a fabricated visibility event.
    const until = Date.now() + duration * 1000;
    while (Date.now() < until) await sleep(Math.min(1000, until - Date.now()));
    entry.after = await snapshot(); entry.endedAt = new Date().toISOString();
    console.log('Captured ' + name);
  };
  await wait(`!!document.querySelector('.living-welcome .topic-weather')`, 'welcome hydration');
  await phase('welcome-weather', seconds, () => click('.living-welcome .topic-weather'));
  await phase('storm-entry-paused', seconds, () => click('.welcome-open-map'));
  receipt.checks.push({name:'starter-selection', value:await evaluate(`Array.from(document.querySelectorAll('.category-map-dock button[aria-pressed]'),e=>({title:e.textContent,pressed:e.getAttribute('aria-pressed')}))`)});
  const playable = await evaluate(`!!document.querySelector('.noaa-radar-play') && !document.querySelector('.noaa-radar-play').disabled`);
  if (!playable) throw new Error('Radar cannot play: provider or WebGL unavailable; captured entry evidence only');
  await phase('playback', seconds, async () => {await click('.noaa-radar-play'); await wait(`document.querySelector('.noaa-radar-play')?.getAttribute('aria-pressed') === 'true'`, 'playback started');});
  await phase('paused', seconds, async () => {await click('.noaa-radar-play'); await wait(`document.querySelector('.noaa-radar-play')?.getAttribute('aria-pressed') === 'false'`, 'playback paused');});
  await phase('optional-context', seconds, async () => {
    await click('.category-map-dock-context summary');
    await evaluate(`document.querySelector('.category-map-dock-context button').click()`);
  });
  await phase('unrelated-switch-with-goes', seconds, () => evaluate(`document.querySelectorAll('.category-map-dock-context button')[1].click()`));
  await phase('playback-before-hidden', seconds, async () => {await click('.noaa-radar-play'); await wait(`document.querySelector('.noaa-radar-play')?.getAttribute('aria-pressed') === 'true'`, 'playback before inactivity');});
  const {targetId: background} = await call('Target.createTarget', {url: 'about:blank'});
  await phase('hidden', hiddenSeconds, async () => {
    await call('Target.activateTarget', {targetId: background});
    await wait('document.hidden', 'actual hidden document');
  }, true);
  await phase('returned', seconds, async () => {
    await call('Target.activateTarget', {targetId}); await wait('!document.hidden', 'visible return');
    await wait(`document.querySelector('.noaa-radar-play')?.getAttribute('aria-pressed') === 'false'`, 'playback remains paused after inactivity');
  });
  for (let i = 2; i < 5; i++) await phase('optional-layer-' + i, seconds, () => evaluate(`document.querySelectorAll('.category-map-dock-context button')[${i}].click()`));
  await phase('other-category', seconds, async () => {
    await click('button[aria-label="Open the quick start guide"]');
    await click('.living-welcome .topic-government'); await click('.welcome-open-map');
  });
  await phase('storm-return', seconds, async () => {
    await click('button[aria-label="Open the quick start guide"]');
    await click('.living-welcome .topic-weather'); await click('.welcome-open-map');
  });
  if (soakSeconds) await phase('extended-playback', soakSeconds, () => click('.noaa-radar-play'));
  receipt.attachmentErrors = attachmentErrors;
  receipt.status = attachmentErrors.length || network.dropped ? 'incomplete-capture' : 'captured';
} catch (error) {
  receipt.blocker = String(error);
  process.exitCode = 2;
} finally {
  receipt.finishedAt = new Date().toISOString(); receipt.network = network.snapshot();
  receipt.network.completeCapture = receipt.network.completeCapture && receipt.status === 'captured';
  receipt.networkSummary = summarizeStormDeskNetwork(receipt.network);
  for (const phase of receipt.phases) {
    if (!phase.after) continue;
    const intervals = phase.after.browser.intervals.slice().sort((a,b)=>a-b);
    const mean = intervals.length ? intervals.reduce((a,b)=>a+b,0)/intervals.length : null;
    phase.summary = {rafIntervals:intervals.length, meanRafIntervalMs:mean,
      pageRafCadenceHz:mean ? 1000/mean : null,
      p95RafIntervalMs:intervals.length ? intervals[Math.ceil(intervals.length*.95)-1] : null,
      mapRenderCallbacks:phase.before.map && phase.after.map ? phase.after.map.rendered-phase.before.map.rendered : null,
      gpuPresentedFps:null};
    if (phase.before.map && phase.after.map) {
      const staged = new Map(), ready = [];
      for (const event of phase.after.map.events) {
        if (event.kind === 'stage') staged.set(event.observedAt, event.at);
        else if (event.kind === 'confirmed' && event.at >= phase.before.map.sampledAt && staged.has(event.observedAt)) {
          ready.push({observedAt:event.observedAt, stageToReadyMs:event.at-staged.get(event.observedAt)});
          staged.delete(event.observedAt);
        }
      }
      phase.summary.exactFrameReadiness = ready;
    }
  }
  await mkdir(resolve(out, '..'), {recursive: true});
  await writeFile(out, JSON.stringify(receipt, null, 2) + '\n');
  if (call && !closed) {try {await call('Browser.close');} catch {child?.kill();}}
  if (child && child.exitCode === null) {await Promise.race([new Promise(resolve => child.once('exit', resolve)), sleep(2000)]); if (child.exitCode === null) child.kill('SIGKILL');}
  if (profile) await rm(profile, {recursive: true, force: true, maxRetries: 3});
  console.log(out);
}
