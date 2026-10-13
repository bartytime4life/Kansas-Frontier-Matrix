import { PREPARED_COLLECTIONS } from "./prepared-collection-pins";
export type PreparedProfile = typeof PREPARED_COLLECTIONS[number];
export type ReviewFile = { name: string; webkitRelativePath?: string; size: number; arrayBuffer(): Promise<ArrayBuffer> };
export type PreparedSelection = { profile: PreparedProfile; files: ReadonlyMap<string, ArrayBuffer> };
const digest = async (b: ArrayBuffer) => Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256", b)), x => x.toString(16).padStart(2, "0")).join("");
const cancelled = (s: AbortSignal) => s.throwIfAborted();
const decode = (b: ArrayBuffer) => new TextDecoder("utf-8", { fatal: true }).decode(b);

/** Pin the whole device-selected package before exposing any bytes to preview. No network or store paths. */
export async function inspectPreparedCollection(id: string, files: readonly ReviewFile[], signal: AbortSignal): Promise<PreparedSelection> {
  const profile = PREPARED_COLLECTIONS.find(p => p.id === id);
  if (!profile) throw new Error("No pinned preparation exists for this collection.");
  cancelled(signal);
  const inputs = new Map<string, ReviewFile>();
  for (const f of files) {
    const path = f.webkitRelativePath || f.name;
    if (!path || path.length > 400 || path.includes("\\") || path.startsWith("/") || path.split("/").some(s => !s || s === "." || s === "..") || /[\x00-\x1f\x7f]/.test(path)) throw new Error("Unsafe or ambiguous file selection.");
    // The operator's marker is not payload and cannot extend the package.
    if (f.name === ".kfm-copy-plan.json" && files.length === profile.fileCount + 1 && f.size <= 4096) continue;
    if (inputs.has(f.name) || !Number.isSafeInteger(f.size) || f.size < 1 || f.size > 16 * 1024 * 1024) throw new Error("Duplicate, empty or oversized file selection.");
    const expected = f.name === "review-manifest.json" || profile.members.some(m => m.file.split("/").at(-1) === f.name);
    if (!expected) throw new Error("Unexpected file. Choose the exact prepared collection.");
    inputs.set(f.name, f);
  }
  if (inputs.size !== profile.fileCount || [...inputs.values()].reduce((sum, f) => sum + f.size, 0) !== profile.totalBytes) throw new Error("The preparation is incomplete or changed. Choose the whole prepared folder.");
  const mf = inputs.get("review-manifest.json");
  if (!mf || mf.size > 256 * 1024) throw new Error("Prepared manifest missing or too large.");
  const raw = await mf.arrayBuffer(); cancelled(signal);
  if (raw.byteLength !== mf.size || await digest(raw) !== profile.manifestSha256) throw new Error("Manifest differs from the pinned preparation. Data held.");
  cancelled(signal);
  const manifest = JSON.parse(decode(raw));
  if (manifest.profile !== "kfm-private-collection-readiness/v1" || manifest.readiness !== "SUPPORTED_FOR_BOUNDED_PRIVATE_PREPARATION" || manifest.review_state !== "PENDING" || manifest.source_admitted !== false || manifest.released !== false || manifest.published !== false || JSON.stringify(manifest.outputs) !== JSON.stringify(profile.members)) throw new Error("Unsupported preparation or review state. Data held.");
  const result = new Map<string, ArrayBuffer>();
  for (const member of profile.members) {
    const f = inputs.get(member.file.split("/").at(-1)!);
    if (!f || f.size !== member.bytes) throw new Error("Member missing or size changed. Data held.");
    const b = await f.arrayBuffer(); cancelled(signal);
    if (b.byteLength !== member.bytes || await digest(b) !== member.sha256) throw new Error("Member digest changed. Data held.");
    cancelled(signal); result.set(member.file, b);
  }
  return { profile, files: result };
}

export const preparedText = (selection: PreparedSelection, name: string) => {
  const b = selection.files.get(name);
  if (!b) throw new Error("No verified member selected.");
  return decode(b);
};
/** RFC4180 subset: quoted commas/newlines and doubled quotes; bounded rows, columns and cell sizes. */
export function preparedTable(text: string): { headers: string[]; rows: string[][] } {
  if (text.length > 8 * 1024 * 1024) throw new Error("Table is too large for this review.");
  const records: string[][] = []; let row: string[] = [], cell = "", quoted = false, ended = false;
  const field = () => { if (cell.length > 8000 || row.length >= 64) throw new Error("Table field limit exceeded."); row.push(cell); cell = ""; ended = false; };
  const record = () => { field(); records.push(row); row = []; if (records.length > 50001) throw new Error("Table row limit exceeded."); };
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (quoted) { if (c === '"') { if (text[i + 1] === '"') { cell += '"'; i++; } else { quoted = false; ended = true; } } else cell += c; }
    else if (c === '"' && !cell && !ended) quoted = true;
    else if (c === ',') field();
    else if (c === '\n' || c === '\r') { if (c === '\r' && text[i + 1] === '\n') i++; record(); }
    else { if (ended || c === '"') throw new Error("Malformed CSV quoting."); cell += c; }
    if (cell.length > 8000) throw new Error("Table cell limit exceeded.");
  }
  if (quoted) throw new Error("Unclosed CSV quote.");
  if (row.length || cell || ended) record();
  const headers = records.shift();
  if (!headers?.length || headers.some(h => !h || h.length > 160) || new Set(headers).size !== headers.length || records.some(r => r.length !== headers.length)) throw new Error("Unsupported table structure.");
  return { headers, rows: records };
}
