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
// not evidence for a request that was current when its command failed.
export function createInterceptionErrorTracker({ graceMs = 1000, setTimer = setTimeout, clearTimer = clearTimeout } = {}) {
  const errors = [], canceled = new Set(), pending = new Set();
  const describe = (error, request) => `${String(error)} [${request.url}; network=${request.networkId}; navigation=${request.requestNavigation}/${request.navigation}]`;
  const settle = (entry, confirmed) => {
    if (!pending.delete(entry)) return;
    clearTimer(entry.timer);
    if (!confirmed) errors.push(describe(entry.error, entry.request));
    entry.resolve();
  };
  return {
    errors,
    loadingFailed({ requestId, canceled: wasCanceled }) {
      if (wasCanceled !== true || typeof requestId !== 'string' || !requestId) return;
      canceled.add(requestId);
      for (const entry of pending) if (entry.request.networkId === requestId) settle(entry, true);
    },
    failed(error, request) {
      const { networkId, requestNavigation, navigation } = request;
      if (isStaleInterceptionCancellation(error, requestNavigation, navigation, canceled.has(networkId))) return;
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
