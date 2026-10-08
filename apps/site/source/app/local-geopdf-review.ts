/** Device-only inspection of explicitly pinned WORK preparations. No admission or serving authority. */
export const ALLEN_REVIEW = Object.freeze({
  sourceSha256: "477eead68df3ed87d6c353a2bd1ba471e6064be76da61e98d739729d4e41f766",
  manifestSha256: "7796ae7a428286be480704a5e80c27e41bbcdc75edbed87fc794331dc4914cf4",
  candidateId: "8e26f9a0eec73580a30ffe84afef8e9387b195836b730646e32c4344adc4a0b6",
  title: "Allen County · June 2025 planning map",
  fileCount: 186, totalBytes: 3_751_691,
  tileCount: 181, maxFileBytes: 2_000_000,
  attribution: "KDOT Allen County · June 2025 planning map · device-only review, not released",
  sourceMeaning: "Future functional classifications, not current road conditions or closures. Edition: June 2025. County approval: May 13, 2003. FHWA approval: November 7, 2003.",
  renderDetail: "Nearest-neighbor tiles at zooms 10–13. Render detail is about 22.5 m per pixel; this is not positional accuracy or printed scale.",
  alignmentLimit: "Nine cartographic checkpoints differed by 0.225–5.058 m from Census 2025 roads without refitting. Reference lineage may overlap. This does not establish surveyed ground accuracy.",
});
export type PreparedMapProfile = Readonly<{
  sourceSha256: string; manifestSha256: string; candidateId: string; title: string;
  fileCount: number; totalBytes: number; tileCount: number; maxFileBytes: number;
  attribution: string; sourceMeaning: string; renderDetail: string; alignmentLimit: string;
}>;
// New map preparations enter only through source-reviewed pins in this registry.
// Download receipts and browser manifests never extend it at runtime.
export const PREPARED_MAP_PROFILES: readonly PreparedMapProfile[] = Object.freeze([ALLEN_REVIEW]);
export const preparedMapProfile = (sourceSha256: string) => PREPARED_MAP_PROFILES.find(profile=>profile.sourceSha256===sourceSha256);
export type ReviewFile = Pick<File, "name" | "size" | "arrayBuffer"> & { webkitRelativePath: string };
type Artifact = { bytes: number; sha256: string };
type Candidate = {
  version: 1; candidateId: string; state: "LOCAL_REVIEW_ONLY"; siteServing: false;
  source: { sha256: string }; holds: string[];
  artifacts: Record<string, Artifact>;
  display: { boundsWgs84: [number, number, number, number]; minZoom: number; maxZoom: number; tiles: Record<string, Artifact> };
};
export type LocalReviewPackage = Readonly<{
  bounds: [number, number, number, number]; minZoom: number; maxZoom: number;
  tiles: ReadonlyMap<string, ArrayBuffer>; original: Blob; legend: Blob;
  attribution: string;
}>;

const cancelled = (signal: AbortSignal) => { if (signal.aborted) throw new DOMException("File check cancelled.", "AbortError"); };
const hash = async (bytes: ArrayBuffer) => Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256", bytes)), n => n.toString(16).padStart(2, "0")).join("");

/** Pins describe a reviewed preparation identity, never an approved data release. */
export async function inspectLocalReview(files: readonly ReviewFile[], signal: AbortSignal, sourceSha256: string = ALLEN_REVIEW.sourceSha256): Promise<LocalReviewPackage> {
  cancelled(signal);
  const profile=preparedMapProfile(sourceSha256);
  if (!profile) throw new Error("No pinned preparation exists for this source. No files were loaded.");
  if (files.length !== profile.fileCount || files.some(f => !Number.isSafeInteger(f.size) || f.size < 1 || f.size > profile.maxFileBytes)
    || files.reduce((n, f) => n + f.size, 0) !== profile.totalBytes) throw new Error(`Choose the complete ${profile.title} prepared folder (${profile.fileCount} files). No files were loaded.`);
  const selected = new Map<string, ReviewFile>();
  let directory = "";
  for (const file of files) {
    const parts = file.webkitRelativePath.split("/");
    if (parts.length < 2 || parts.some(p => !p || p === "." || p === ".." || /[\\\x00-\x1f]/.test(p))
      || file.name !== parts.at(-1)) throw new Error("The selected folder contains an invalid file path.");
    directory ||= parts[0];
    const name = parts.slice(1).join("/");
    if (directory !== parts[0] || selected.has(name)) throw new Error("Select one prepared folder with no duplicate paths.");
    selected.set(name, file);
  }
  const manifestFile = selected.get("candidate.json");
  if (!manifestFile || manifestFile.size > 256 * 1024) throw new Error("The prepared manifest is missing or too large.");
  const manifestBytes = await manifestFile.arrayBuffer(); cancelled(signal);
  if (manifestBytes.byteLength !== manifestFile.size || await hash(manifestBytes) !== profile.manifestSha256) throw new Error("This folder is not the pinned preparation. Its manifest differs.");
  cancelled(signal);
  const m = JSON.parse(new TextDecoder("utf-8", { fatal: true }).decode(manifestBytes)) as Candidate;
  if (m.version !== 1 || m.candidateId !== profile.candidateId || m.source.sha256 !== profile.sourceSha256
    || m.state !== "LOCAL_REVIEW_ONLY" || m.siteServing !== false || !m.holds.includes("ACTIVATION")) throw new Error("The preparation's review boundary is invalid.");
  // The exact hash above pins geometry, zooms and all addresses. Never use a
  // browser-supplied approval, URL, new transform, filename, or bounds override.
  const expected = new Map<string, Artifact>(Object.entries(m.artifacts));
  for (const [address, record] of Object.entries(m.display.tiles)) expected.set(`tiles/${address}.png`, record);
  if (expected.size + 1 !== selected.size || [...selected.keys()].some(n => n !== "candidate.json" && !expected.has(n))) throw new Error("The prepared folder contains unexpected or missing files.");
  const tiles = new Map<string, ArrayBuffer>();
  let original: Blob | undefined, legend: Blob | undefined;
  // One bounded native read at a time. Cancelled results are never installed.
  for (const [name, record] of expected) {
    cancelled(signal);
    const file = selected.get(name);
    if (!file || file.size !== record.bytes) throw new Error("A prepared file is missing or its size has changed.");
    const bytes = await file.arrayBuffer(); cancelled(signal);
    if (bytes.byteLength !== record.bytes || await hash(bytes) !== record.sha256) throw new Error("A prepared file failed its integrity check. The overlay was withheld.");
    cancelled(signal);
    if (name.startsWith("tiles/")) tiles.set(name.slice(6, -4), bytes);
    else if (name === "input.pdf") original = new Blob([bytes], { type: "application/pdf" });
    else if (name === "page.png") legend = new Blob([bytes], { type: "image/png" });
  }
  if (!original || !legend || tiles.size !== profile.tileCount) throw new Error("The preparation is incomplete.");
  return { bounds: m.display.boundsWgs84, minZoom: m.display.minZoom, maxZoom: m.display.maxZoom, tiles, original, legend, attribution:profile.attribution };
}
