/** One visible request round at a time. Hidden/obsolete replies cannot commit. */
export function startDownloadPolling(run: (signal: AbortSignal) => Promise<boolean>, environment = {
  document,
  // Browser timers require the Window receiver; storing their native functions
  // directly on this environment would call them with the wrong `this` value.
  setTimeout: (callback: () => void, delay: number) => window.setTimeout(callback, delay),
  clearTimeout: (id: number) => window.clearTimeout(id),
}) {
  let disposed = false, running = false, immediate = false;
  let timer: ReturnType<typeof environment.setTimeout> | undefined, round: AbortController | null = null;
  const visible = () => environment.document.visibilityState !== "hidden";
  const clear = () => { if (timer !== undefined) environment.clearTimeout(timer); timer = undefined; };
  const poll = async () => {
    if (disposed || running || !visible()) return;
    clear(); running = true; const controller = new AbortController(); round = controller;
    let fast = false;
    try { fast = await run(controller.signal); } catch { /* The controller reports connection failure. */ }
    finally {
      running = false;
      if (!disposed && visible()) {
        const delay = immediate ? 0 : fast ? 2500 : 15000; immediate = false;
        timer = environment.setTimeout(() => void poll(), delay);
      }
    }
  };
  const refresh = () => { clear(); if (running) immediate = true; else void poll(); };
  const visibility = () => { clear(); if (!visible()) round?.abort(); else refresh(); };
  environment.document.addEventListener("visibilitychange", visibility);
  void poll();
  return { refresh, dispose() { disposed = true; clear(); round?.abort(); environment.document.removeEventListener("visibilitychange", visibility); } };
}
