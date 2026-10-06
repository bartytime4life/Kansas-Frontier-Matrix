import { ACQUISITION_MAX_BYTES, parseAcquisitionInventory, type AcquisitionInventory } from "./acquisition-inventory";

/** Local metadata only; File.text cannot be aborted, so retire its result explicitly. */
export async function readAcquisitionLocalJson(file: Pick<File, "size" | "text">, signal: AbortSignal): Promise<unknown> {
  signal.throwIfAborted();
  if (!Number.isSafeInteger(file.size) || file.size < 1 || file.size > ACQUISITION_MAX_BYTES) throw new Error("Metadata must be a nonempty JSON file no larger than 1 MiB.");
  const raw = await file.text();
  signal.throwIfAborted();
  return JSON.parse(raw);
}

/** A local file, saved read, and save response all belong to one current selection. */
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

export function acquisitionRead(body: unknown): AcquisitionInventory | null {
  if (!body || typeof body !== "object" || Array.isArray(body) || !("inventory" in body)) throw new Error("Saved receipt response is invalid.");
  if (body.inventory === null) return null;
  const inventory = parseAcquisitionInventory(body.inventory);
  if (!inventory) throw new Error("Saved receipt failed validation. It has not been loaded.");
  return inventory;
}

export async function verifyAcquisitionSave(body: unknown, submitted: AcquisitionInventory): Promise<void> {
  if (!body || typeof body !== "object" || !("saved" in body) || body.saved !== true || !("sha256" in body)
    || typeof body.sha256 !== "string" || !/^[a-f0-9]{64}$/.test(body.sha256)) throw new Error("Receipt save was not confirmed. Check saved status before retrying.");
  const saved = acquisitionRead(body);
  const expected = parseAcquisitionInventory(submitted);
  if (!expected) throw new Error("Submitted receipt failed validation.");
  const serialized = JSON.stringify(expected);
  if (!saved || JSON.stringify(saved) !== serialized) throw new Error("Saved receipt identity differs from the submitted preview.");
  const digest = Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256", new TextEncoder().encode(serialized))), byte => byte.toString(16).padStart(2, "0")).join("");
  if (digest !== body.sha256) throw new Error("Saved receipt digest differs from the submitted preview.");
}
