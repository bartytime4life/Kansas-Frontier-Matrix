'use strict';
(() => {
  const root = '/api/workspace/acceptance';
  const $ = id => document.getElementById(id);
  let sessionToken = '', state = null, selectedId = '', busy = false;
  const observation = $('observation'), review = $('review');
  const field = (form, key) => form.elements.namedItem(key);
  const announce = value => { $('message').textContent = value; };
  const newRun = () => 'LOCAL-' + crypto.randomUUID();
  function controls() {
    $('import').disabled = !sessionToken || busy;
    $('receipt').disabled = busy || !state?.receipts.length;
    $('export').disabled = !sessionToken || busy;
    $('original').disabled = !selectedId || busy;
    for (const button of document.querySelectorAll('form button')) button.disabled = !selectedId || busy;
  }
  async function request(path, options = {}) {
    const response = await fetch(root + path, {
      ...options, cache: 'no-store', credentials: 'same-origin',
      headers: { 'X-KFM-Session': sessionToken, ...(options.headers || {}) }
    });
    if (!response.ok) {
      const detail = await response.json().catch(() => ({}));
      if (response.status === 403) sessionToken = '';
      controls();
      throw new Error(detail.error || `Request failed (${response.status}). Nothing was marked accepted.`);
    }
    return response;
  }
  function selected() { return state?.receipts.find(item => item.id === selectedId); }
  function node(tag, text, parent) {
    const result = document.createElement(tag);
    if (text !== undefined) result.textContent = String(text);
    if (parent) parent.append(result);
    return result;
  }
  function table(target, headers, rows, action) {
    const holder = $(target); holder.replaceChildren();
    const t = node('table', undefined, holder), head = node('tr', undefined, node('thead', undefined, t));
    for (const name of headers) node('th', name, head).scope = 'col';
    const body = node('tbody', undefined, t);
    rows.forEach((row, index) => {
      const tr = node('tr', undefined, body);
      row.forEach(value => node('td', value ?? 'Unknown', tr));
      if (action) {
        const button = node('button', 'Open plan', node('td', undefined, tr));
        button.type = 'button'; button.addEventListener('click', () => action(index));
      }
    });
  }
  function showPlan(source) {
    const plan = $('plan'); plan.replaceChildren();
    node('h3', source.title, plan);
    node('p', `Internal category: ${source.category}. Drawer label: ${source.visibleDrawerCategoryLabel || 'Not supplied'}.`, plan);
    node('p', `Selection applicability: ${source.selectionApplicability || 'Not supplied'}`, plan);
    node('p', `Source URL (recorded, not fetched): ${source.sourceUrl || 'Not supplied'}`, plan);
    const list = node('ol', undefined, plan);
    for (const step of source.testCase.steps) node('li', step, list);
    node('h3', 'Expected results', plan);
    const expected = node('ul', undefined, plan);
    for (const item of source.testCase.expected) node('li', item, expected);
    field(observation, 'sourceId').value = source.id;
    field(observation, 'steps').value = source.testCase.steps.join('\n');
    field(observation, 'expected').value = source.testCase.expected.join('\n');
    $('case-plan').open = true;
    $('case-plan').scrollIntoView({ behavior: 'auto', block: 'start' });
  }
  function sourceTable() {
    const payload = selected()?.receipt.payload;
    if (!payload) return;
    const query = $('search-sources').value.toLowerCase();
    const sources = payload.sourceInventory.filter(s => [s.id,s.title,s.category,s.sourceUrl].join(' ').toLowerCase().includes(query));
    table('sources', ['Source', 'Internal category', 'Visible drawer label', 'Test plan'],
      sources.map(s => [s.title + '\n' + s.id, s.category, s.visibleDrawerCategoryLabel || 'Not supplied']),
      index => showPlan(sources[index]));
  }
  function render() {
    const item = selected(); $('loaded').hidden = !item;
    if (!item) { controls(); return; }
    const p = item.receipt.payload;
    const events = state.events.filter(e => e.receiptId === selectedId);
    const downloads = p.downloadEvidence.payload.results;
    $('receipt-identity').textContent = `Original bytes SHA-256: ${item.id}\nPayload digest: ${item.receipt.digest}\nImported locally: ${item.importedAt}\nOriginal cutoff: ${p.snapshotCutoff || 'Not supplied'}\nHistorical report only; local review starts UNREVIEWED.`;
    $('source-count').textContent = p.sourceInventory.length;
    $('download-count').textContent = downloads.length;
    $('event-count').textContent = events.length;
    const sourceSelect = $('source-select'), previousSource = sourceSelect.value;
    sourceSelect.replaceChildren(node('option', 'Whole-build check')); sourceSelect.firstChild.value = '';
    for (const source of p.sourceInventory) {
      const option = node('option', source.title, sourceSelect); option.value = source.id;
    }
    if (p.sourceInventory.some(s => s.id === previousSource)) sourceSelect.value = previousSource;
    $('builds').textContent = JSON.stringify({
      candidateRevision: p.candidateSha,
      candidateInputs: p.candidateApplicationInputs?.provenance?.identity || p.candidateApplicationInputs,
      publicObservation: p.publicIdentity,
      installed: 'Not established by importing this receipt',
      deployed: 'Separate deployment provenance required'
    }, null, 2);
    table('downloads', ['Source', 'HTTP reported', 'Provider state reported', 'Historical acceptance'],
      downloads.map(d => [d.sourceId, d.httpStatus, d.metadata?.state || 'Not supplied', d.acceptanceStatus || 'UNREVIEWED']));
    const history = $('history'); history.replaceChildren();
    if (!events.length) node('p', 'No local observations or reviewer decisions. Historical report entries have not been promoted.', history);
    const latestReview = new Map();
    for (const e of events) if (e.event.kind === 'review') latestReview.set(e.event.observation, e.event.decision);
    // The ledger export retains the full history; bound the rendered portion.
    for (const e of events.slice(-200).reverse()) {
      const value = e.event, section = node('article', undefined, history); section.className = 'acceptance-event';
      node('h3', `#${e.sequence} · ${value.kind === 'observation' ? value.result + ' · ' + value.lane : value.decision}`, section);
      node('p', `${value.actor} · observed ${value.observedAt} · recorded ${value.recordedAt}`, section);
      if (value.kind === 'observation') {
        node('p', `Run ${value.runId} · ${value.environment} · ${value.sourceId || 'Whole build'} · evidence review: ${latestReview.get(String(e.sequence)) || 'UNREVIEWED'}`, section);
        node('p', value.observed, section);
        if (value.risk) node('p', 'Unresolved risk: ' + value.risk, section);
        const button = node('button', 'Prepare linked retest', section); button.type = 'button';
        button.addEventListener('click', () => {
          for (const key of ['sourceId','lane','environment','buildIdentity','revision','browser','viewport','webgl2','steps','expected','intakeFileId']) field(observation,key).value = value[key] || '';
          field(observation,'retestOf').value = e.sequence;
          field(observation,'runId').value = newRun(); field(observation,'result').value = 'UNVERIFIED';
          for (const key of ['observed','evidence','risk','observedAt']) field(observation,key).value = '';
          $('record-section').scrollIntoView({ behavior:'auto',block:'start' });
          announce('Retest prepared, not performed or saved. Enter the actual observation time and new evidence.');
        });
      } else node('p', `Review of #${value.observation}: ${value.reason}`, section);
      const details = node('details', undefined, section); node('summary','Complete immutable record',details);
      node('pre',JSON.stringify(e,null,2),details);
    }
    if (events.length > 200) node('p','Showing the latest 200 events; export includes all events.',history);
    $('imported').textContent = JSON.stringify({claims:p.claims, browser:p.browserEvidence,review:p.assistantReview,risks:p.nextChecks,site:p.site}, null, 2);
    sourceTable(); controls();
  }
  async function refresh(prefer) {
    state = await (await request('/state')).json();
    const select = $('receipt'); select.replaceChildren();
    for (const item of state.receipts) {
      const option = node('option', `${item.receipt.payload.runId || 'Saved report'} · ${item.id.slice(0,12)}`, select);
      option.value = item.id;
    }
    const previousId = selectedId;
    selectedId = state.receipts.some(r => r.id === (prefer || selectedId)) ? (prefer || selectedId) : (state.receipts[0]?.id || '');
    if (previousId !== selectedId) {
      observation.reset(); review.reset(); field(observation,'runId').value = newRun();
      $('plan').replaceChildren();
    }
    select.value = selectedId; render();
  }
  async function connect() {
    try {
      const response = await fetch('/api/session', {cache:'no-store',credentials:'same-origin'});
      if (!response.ok) throw new Error('Local session is unavailable.');
      const session = await response.json();
      if (session.app !== 'kfm-local-intake-studio' || !session.token) throw new Error('Unexpected local application identity.');
      sessionToken = session.token;
      $('connection').textContent = 'Local evidence desk';
      $('storage').textContent = 'Private files and evidence stay on this PC';
      $('build-identity').textContent = 'Studio ' + (session.sourceFingerprint || 'unknown').slice(0,12);
      await refresh(); announce('Connected. Importing evidence never approves a release.');
    } catch (error) {
      sessionToken = ''; $('connection').textContent = 'Not connected'; announce(error.message);
    } finally { controls(); }
  }
  async function write(path, body, message) {
    if (busy) return;
    busy = true; controls();
    try {
      const result = await (await request(path, {method:'POST',headers:{'Content-Type':'application/json'},body})).json();
      await refresh(result.id); announce(message + (result.duplicate ? ' Existing identical record retained.' : ''));
      return result;
    } catch(error) { announce(error.message + ' Your form values were retained.'); }
    finally { busy = false; controls(); }
  }
  async function download(path, filename) {
    try {
      const response = await request(path), blob = await response.blob();
      const url = URL.createObjectURL(blob), a = document.createElement('a');
      a.href = url; a.download = filename; a.click(); setTimeout(() => URL.revokeObjectURL(url), 1000);
    } catch(error) { announce(error.message); }
  }
  $('import').addEventListener('click', async () => {
    const file = $('receipt-file').files[0];
    if (!file || file.size > 2*1024*1024 || !file.size) return announce('Choose one JSON receipt of at most 2 MiB.');
    try { await write('/import', await file.arrayBuffer(), 'Receipt imported as historical, unreviewed evidence.'); }
    catch(error) { announce(error.message); }
  });
  $('export').addEventListener('click', () => download('/export','kfm-acceptance-ledger.json'));
  $('original').addEventListener('click', () => download('/original/'+selectedId,'kfm-original-receipt.json'));
  $('reconnect').addEventListener('click', connect);
  $('receipt').addEventListener('change', () => {
    if (!confirm('Switch evidence snapshot? This clears unsaved observation and review fields.')) {
      $('receipt').value = selectedId; return;
    }
    selectedId = $('receipt').value; observation.reset(); review.reset();
    field(observation,'runId').value = newRun(); $('plan').replaceChildren(); render();
  });
  $('search-sources').addEventListener('input', sourceTable);
  observation.addEventListener('submit', async event => {
    event.preventDefault();
    const value = {...Object.fromEntries(new FormData(observation)),kind:'observation',receiptId:selectedId};
    const saved = await write('/events', JSON.stringify(value), 'Observation saved. Review and public acceptance remain separate.');
    if (saved) { field(observation,'runId').value = newRun(); field(observation,'observedAt').value=''; }
  });
  review.addEventListener('submit', async event => {
    event.preventDefault();
    const value = {...Object.fromEntries(new FormData(review)),kind:'review',receiptId:selectedId};
    if (await write('/events',JSON.stringify(value),'Scoped review saved; no Intake or release state changed.')) field(review,'observedAt').value='';
  });
  field(observation,'runId').value = newRun();
  connect();
})();
