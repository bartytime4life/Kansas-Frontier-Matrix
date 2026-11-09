/** Prepare the newest worker, rather than an old worker being replaced. */
export async function activatedOfflineWorker(registration: ServiceWorkerRegistration): Promise<ServiceWorker> {
  const worker = registration.installing || registration.waiting || registration.active;
  if (!worker) throw Error('Worker unavailable');
  if (worker.state === 'activated') return worker;
  return new Promise((resolve, reject) => {
    const cleanup = () => { clearTimeout(timer); worker.removeEventListener('statechange', check); };
    const check = () => {
      if (worker.state === 'activated') { cleanup(); resolve(worker); }
      if (worker.state === 'redundant') { cleanup(); reject(Error('Worker unavailable')); }
    };
    const timer = setTimeout(() => { cleanup(); reject(Error('Cache preparation timed out')); }, 20000);
    worker.addEventListener('statechange', check);
    check();
  });
}
