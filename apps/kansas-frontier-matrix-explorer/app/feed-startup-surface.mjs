import { CONNECTIONS, probeContextConnections } from './context-connection-probe.mjs';
import { createFeedStartupSession } from './feed-startup-session.mjs';
import { readBundledStartupDemo } from './feed-startup-demo.mjs';

/** Mount an isolated repository inspector, never rewrite the map's investigation.
 * DOM writes use textContent; no provider body, credential or URL query is shown.
 * @param {HTMLElement} host
 * @param {{fixtureText: string}} options
 */
export function mountFeedStartupSurface(host, { fixtureText }) {
  const doc = host.ownerDocument;
  let disposed = false, opened = false, report = null, demo = null, epoch = 0;
  const node = (tag, text = '', className = '') => {
    const element = doc.createElement(tag);
    element.textContent = text;
    if (className) element.className = className;
    return element;
  };
  const trigger = node('button', 'Data startup · preview', 'kfm-feed-trigger');
  trigger.type = 'button'; trigger.setAttribute('aria-haspopup', 'dialog');
  const dialog = node('dialog', '', 'kfm-feed-dialog');
  dialog.setAttribute('aria-label', 'Data startup and connection inspector');
  const header = node('header');
  const title = node('h2', 'Data startup & connections');
  const close = node('button', 'Close'); close.type = 'button';
  header.append(title, close);
  const boundary = node('p', 'Repository preview — not the deployed Site. These controls inspect startup policy; they do not change the main map, its selected date, layers, or Evidence Drawer.', 'kfm-feed-boundary');
  const controls = node('div', '', 'kfm-feed-controls');
  const sourceLabel = node('label', 'Connection to inspect');
  const source = node('select'); source.setAttribute('aria-label', 'Connection to inspect');
  for (const connection of CONNECTIONS) {
    const option = node('option', connection.id); option.value = connection.id; source.append(option);
  }
  source.value = 'usgs-earthquakes'; sourceLabel.append(source);
  const directionLabel = node('label', 'Preview startup policy');
  const direction = node('select'); direction.setAttribute('aria-label', 'Preview startup policy');
  for (const [value, text] of [['auto', 'Auto'], ['live', 'Live'],
    ['history', 'History'], ['demo', 'Demo']]) {
    const option = node('option', text); option.value = value; direction.append(option);
  }
  directionLabel.append(direction); controls.append(sourceLabel, directionLabel);
  const status = node('p', '', 'kfm-feed-status'); status.setAttribute('role', 'status');
  status.setAttribute('aria-live', 'polite'); status.setAttribute('aria-atomic', 'true');
  const detail = node('p');
  const policyNote = node('p', 'Auto prefers current data, then a matching dated snapshot, then a labeled demo. Live and History never switch modes silently.');
  const counts = node('p', '', 'kfm-feed-counts');
  const preview = node('section', '', 'kfm-feed-preview'); preview.setAttribute('aria-label', 'Separate synthetic demonstration');
  const previewTitle = node('h3', 'SYNTHETIC DEMO — not observations');
  const previewNote = node('p', 'Two invented shapes test presentation only. They are not earthquake, smoke, radar, flow, terrain, or boundary data. This is not the main map.');
  const shapes = node('ul');
  preview.append(previewTitle, previewNote, shapes); preview.hidden = true;
  const probeNote = node('p', 'Check connections sends up to ten bounded same-origin GET requests, which may reach configured provider adapters. The inventory comes from the saved v40 source, not verified current Site configuration. No response bodies or credentials are exported.');
  const probe = node('button', 'Check connections'); probe.type = 'button';
  const cancel = node('button', 'Cancel check'); cancel.type = 'button'; cancel.hidden = true;
  const actions = node('div', '', 'kfm-feed-actions'); actions.append(probe, cancel);
  const tableWrap = node('div', '', 'kfm-feed-table-wrap');
  const table = node('table');
  const caption = node('caption', 'Transport diagnostics — not payload, freshness, or map-render acceptance');
  const thead = node('thead'), tr = node('tr');
  for (const text of ['Connection', 'Result', 'HTTP']) { const th = node('th', text); th.scope = 'col'; tr.append(th); }
  thead.append(tr); const tbody = node('tbody'); table.append(caption, thead, tbody); tableWrap.append(table);
  const limitation = node('p', 'No approved real snapshot or historical artifact is bundled. Successful JSON or PNG transport alone cannot make a live-data claim. Empty responses are not an all-clear. No geolocation, persistent cache, data export, or background polling is used.');
  dialog.append(header, boundary, controls, policyNote, status, detail, counts, preview, probeNote, actions, tableWrap, limitation);
  host.append(trigger, dialog);

  const renderRows = () => {
    tbody.replaceChildren();
    for (const connection of CONNECTIONS) {
      const row = report?.results.find((r) => r.id === connection.id);
      const line = node('tr');
      for (const text of [connection.id, row?.status ?? 'NOT_CHECKED', row?.httpStatus == null ? '—' : String(row.httpStatus)]) line.append(node('td', text));
      tbody.append(line);
    }
  };
  const render = (snapshot) => {
    if (disposed) return;
    const d = snapshot.decision;
    status.textContent = `${snapshot.workState.toUpperCase()} · ${d.display} · ${d.connectionFailure ?? d.reason}`;
    detail.textContent = d.disclosure;
    counts.textContent = `This inspector: validated live ${Number(d.liveAvailable)}; rendered live ${Number(d.renderedLive)}. Main-map telemetry is not measured here.`;
    preview.hidden = d.display !== 'SYNTHETIC_DEMO';
    const busy = snapshot.workState === 'loading';
    probe.disabled = busy || direction.value === 'history' || direction.value === 'demo';
    cancel.hidden = !busy;
    probe.title = direction.value === 'history' ? 'No historical adapter is bound to this policy preview.'
      : direction.value === 'demo' ? 'Demo mode makes no provider requests.' : '';
    dialog.setAttribute('aria-busy', String(busy));
  };
  const session = createFeedStartupSession({ now: new Date().toISOString(), sourceId: source.value,
    scopeKey: `preview:${source.value}`, direction: 'auto', enabled: true, access: 'allowed',
    timeSupported: true, zoomSupported: true, phase: 'idle' }, { onChange: render });
  render(session.snapshot()); renderRows();
  // Digest computation is local. It starts no network activity and never overrides a later choice.
  const preparation = readBundledStartupDemo(fixtureText).then((verified) => {
    if (disposed) return;
    demo = verified;
    shapes.replaceChildren(...demo.data.features.map((f) => node('li', `${f.properties.label} (${f.geometry.type})`)));
    // Prepare before the dialog becomes interactive; no active request is displaced.
    session.select({ demo: demo.artifact, direction: direction.value, sourceId: source.value,
      scopeKey: `preview:${source.value}` });
  }).catch(() => { if (!disposed) detail.textContent = 'Synthetic fixture unavailable: integrity verification failed.'; });

  const choose = () => {
    epoch++; report = null;
    session.select({ direction: direction.value, sourceId: source.value, scopeKey: `preview:${source.value}`,
      demo: demo?.artifact });
    renderRows();
  };
  const stop = () => { epoch++; session.cancel(); report = null; renderRows(); };
  const onClose = () => { opened = false; stop(); if (!disposed && trigger.isConnected) trigger.focus({ preventScroll: true }); };
  const onCancel = (event) => { event.preventDefault(); dialog.close(); };
  const onOpen = async () => {
    await preparation;
    if (disposed || opened) return;
    opened = true; dialog.showModal(); close.focus();
  };
  const onProbe = async () => {
    if (disposed || !opened || probe.disabled) return;
    const ownEpoch = ++epoch; report = null; renderRows();
    await session.load(async ({ signal, sourceId }) => {
      const next = await probeContextConnections({ origin: doc.location.origin, signal });
      if (!disposed && opened && ownEpoch === epoch && !signal.aborted) { report = next; renderRows(); }
      const state = next.results.find((row) => row.id === sourceId)?.status;
      // This is a transport inspector, not a source parser. It never fabricates an accepted Artifact.
      const failureCode = ({ API_NOT_CONFIGURED: 'API_NOT_CONFIGURED', ROUTE_MISSING: 'ROUTE_MISSING',
        AUTH_REQUIRED: 'AUTH_REQUIRED', REDIRECT_OR_AUTH_UNVERIFIED: 'AUTH_REQUIRED',
        RATE_LIMITED: 'RATE_LIMITED', TIMEOUT: 'TIMEOUT', UNEXPECTED_MEDIA_TYPE: 'UNEXPECTED_MEDIA_TYPE',
        NETWORK_OR_STREAM_ERROR: 'NETWORK_ERROR', NOT_PROBED_RENDERER: 'RENDER_UNVERIFIED',
        UPSTREAM_OR_ADAPTER_ERROR: 'UPSTREAM_ERROR', INVALID_JSON_OR_UTF8: 'INVALID_RESPONSE',
        BODY_LIMIT: 'INVALID_RESPONSE', INVALID_PNG_HEADER: 'INVALID_RESPONSE', HTTP_ERROR: 'UPSTREAM_ERROR' })[state] ?? 'PAYLOAD_UNVERIFIED';
      return { phase: 'error', failureCode };
    });
  };
  trigger.addEventListener('click', onOpen);
  const closeDialog = () => dialog.close();
  close.addEventListener('click', closeDialog);
  dialog.addEventListener('close', onClose); dialog.addEventListener('cancel', onCancel);
  source.addEventListener('change', choose); direction.addEventListener('change', choose);
  probe.addEventListener('click', onProbe); cancel.addEventListener('click', stop);
  return Object.freeze({ dispose() {
    if (disposed) return;
    disposed = true; epoch++; session.dispose();
    trigger.removeEventListener('click', onOpen); close.removeEventListener('click', closeDialog);
    dialog.removeEventListener('close', onClose); dialog.removeEventListener('cancel', onCancel);
    source.removeEventListener('change', choose); direction.removeEventListener('change', choose);
    probe.removeEventListener('click', onProbe); cancel.removeEventListener('click', stop);
    if (dialog.open) dialog.close(); dialog.remove(); trigger.remove();
  } });
}
