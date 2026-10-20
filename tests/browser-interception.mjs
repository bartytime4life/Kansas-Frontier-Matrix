// Navigation or a matching Network.loadingFailed(canceled=true) event can
// invalidate a paused request. Never hide an unconfirmed current-request error
// or another protocol failure behind that cancellation.
export function isStaleInterceptionCancellation(error, requestNavigation, navigation, canceled = false) {
  if (!(requestNavigation < navigation) && canceled !== true) return false;
  try {
    const protocolError = JSON.parse(error.message);
    return protocolError?.code === -32602 && protocolError.message === "Invalid InterceptionId.";
  } catch {
    return false;
  }
}

// Fetch command replies and Network events are delivered independently. Keep
// an exact invalid-ID reply provisional for a bounded interval, so a matching
// cancellation may arrive on either side of the reply. A later navigation is
// not evidence on its own: only a matching Network request tied to a loader
// that Page.frameNavigated has actually replaced proves an old document.
export function createInterceptionErrorTracker({ graceMs = 1000, setTimer = setTimeout, clearTimer = clearTimeout } = {}) {
  const errors = [], canceled = new Set(), pending = new Set();
  const requests = new Map(), frameLoaders = new Map(), retiredLoaders = new Set(), networkFailures = new Map();
  const confirmed = networkId => {
    const request = requests.get(networkId);
    return canceled.has(networkId) || (request && retiredLoaders.has(JSON.stringify([request.frameId, request.loaderId])));
  };
  const describe = (error, request) => `${String(error)} [${request.url}; network=${request.networkId}; navigation=${request.requestNavigation}/${request.navigation}; identity=${JSON.stringify(requests.get(request.networkId))}; failure=${JSON.stringify(networkFailures.get(request.networkId))}]`;
  const settle = (entry, confirmed) => {
    if (!pending.delete(entry)) return;
    clearTimer(entry.timer);
    if (!confirmed) errors.push(describe(entry.error, entry.request));
    entry.resolve();
  };
  const confirmPending = () => {
    for (const entry of pending) if (confirmed(entry.request.networkId)) settle(entry, true);
  };
  return {
    errors,
    requestWillBeSent({ requestId, frameId, loaderId }) {
      if (typeof requestId !== 'string' || !requestId || !frameId || !loaderId) return;
      requests.set(requestId, { frameId, loaderId });
      confirmPending();
    },
    frameNavigated({ frame }) {
      if (!frame?.id || !frame.loaderId) return;
      const previous = frameLoaders.get(frame.id);
      if (previous && previous !== frame.loaderId) retiredLoaders.add(JSON.stringify([frame.id, previous]));
      frameLoaders.set(frame.id, frame.loaderId);
      confirmPending();
    },
    loadingFailed({ requestId, canceled: wasCanceled, errorText }) {
      networkFailures.set(requestId, { canceled: wasCanceled, errorText });
      if (wasCanceled !== true || typeof requestId !== 'string' || !requestId) return;
      canceled.add(requestId);
      confirmPending();
    },
    failed(error, request) {
      const { networkId, requestNavigation, navigation } = request;
      if (isStaleInterceptionCancellation(error, requestNavigation, navigation, confirmed(networkId))) return;
      if (!isStaleInterceptionCancellation(error, 0, 0, true) || typeof networkId !== 'string' || !networkId) {
        errors.push(describe(error, request));
        return;
      }
      const entry = { error, request };
      entry.done = new Promise(resolve => { entry.resolve = resolve; });
      pending.add(entry);
      entry.timer = setTimer(() => settle(entry, false), graceMs);
    },
    async assertHealthy() {
      // Include failures arriving while a previous cancellation is settling.
      while (pending.size) await Promise.all([...pending].map(entry => entry.done));
      if (errors.length) throw new Error(errors.join('\n'));
    },
  };
}
