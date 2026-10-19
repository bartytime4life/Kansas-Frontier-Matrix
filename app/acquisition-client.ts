import { ACQUISITION_MAX_BYTES } from "./acquisition-inventory";

/** Local metadata only; File.text cannot be aborted, so retire its result explicitly. */
export async function readAcquisitionLocalJson(file: Pick<File, "size" | "text">, signal: AbortSignal): Promise<unknown> {
  signal.throwIfAborted();
  if (!Number.isSafeInteger(file.size) || file.size < 1 || file.size > ACQUISITION_MAX_BYTES) throw new Error("Metadata must be a nonempty JSON file no larger than 1 MiB.");
  const raw = await file.text();
  signal.throwIfAborted();
  return JSON.parse(raw);
}

/** Only the latest local file selection may replace the preview. */
export function createAcquisitionSession() {
  let active: AbortController | undefined;
  return {
    begin() {
      active?.abort();
      const controller = new AbortController(); active = controller;
      return { signal: controller.signal, current: () => active === controller && !controller.signal.aborted };
    },
    cancel() { active?.abort(); active = undefined; },
  };
}
