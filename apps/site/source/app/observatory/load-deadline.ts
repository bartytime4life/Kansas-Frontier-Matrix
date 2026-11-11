/** Bound one replay read, including its body, without cancelling other sources. */
export async function replayRead<T>(read: (signal: AbortSignal) => Promise<T>, parent: AbortSignal, message: string, timeoutMs = 30_000): Promise<T> {
  parent.throwIfAborted();
  const controller = new AbortController();
  let rejectDeadline!: (reason: unknown) => void;
  const deadline = new Promise<never>((_, reject) => { rejectDeadline = reject; });
  const cancel = () => { controller.abort(parent.reason); rejectDeadline(controller.signal.reason); };
  parent.addEventListener("abort", cancel, { once: true });
  const timer = setTimeout(() => {
    const failure = new Error(message);
    controller.abort(failure); rejectDeadline(failure);
  }, timeoutMs);
  try {
    return await Promise.race([Promise.resolve().then(() => {
      controller.signal.throwIfAborted();
      return read(controller.signal);
    }).then((value) => { controller.signal.throwIfAborted(); return value; }), deadline]);
  } finally {
    clearTimeout(timer);
    parent.removeEventListener("abort", cancel);
  }
}
