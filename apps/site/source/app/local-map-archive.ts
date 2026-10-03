/** Local discovery/inspection only: this module does not upload, fetch or persist. */
export type LocalMapSheet = {
  id: string; collection: string; fileName: string; sizeBytes: number; sha256: string;
  placeHint: string | null; editionLabel: string | null; editionBasis: string;
  startYear: number | null; endYear: number | null; alignment: string;
  flags: string[]; sameBytesAs: string[];
};
export type ArchiveFilter = { collection: string; text: string; year: string; issuesOnly: boolean };
export const MAX_LOCAL_PDF_BYTES = 100 * 1024 * 1024;
export const ARCHIVE_PAGE_SIZE = 20;
export function filterLocalMaps(records: readonly LocalMapSheet[], filter: ArchiveFilter): LocalMapSheet[] {
  const words = filter.text.trim().toLocaleLowerCase("en-US").split(/\s+/).filter(Boolean);
  return records.filter(row => (filter.collection === "all" || row.collection === filter.collection)
    && (!filter.issuesOnly || row.flags.length > 0)
    && (filter.year === "all" || (filter.year === "unknown" ? row.startYear === null : row.startYear !== null && row.endYear !== null && Number(filter.year) >= row.startYear && Number(filter.year) <= row.endYear))
    && words.every(word => `${row.fileName} ${row.collection} ${row.placeHint ?? ""} ${row.editionLabel ?? ""}`.toLocaleLowerCase("en-US").includes(word)));
}
export function editionBasisLabel(basis: string): string {
  return ({ "source_filename_label": "Filename clue", "title-block-ocr": "OCR title-block clue", "title-block-visual": "Visual title-block clue", "prior_verified_printed_edition": "Previously checked printed edition", "identity-conflict": "Identity conflict · date withheld" } as Record<string, string>)[basis] ?? "Edition not established";
}
export function archiveWarning(flag: string): string {
  return ({ "conflicting-filenames": "Identical bytes have conflicting filenames. Date and location claims are withheld.", "pdf-reader-warning": "The PDF reader recovered a structural warning. Check the original source before preparing an overlay.", "blank-source": "The recorded local source is blank. A replacement must be verified separately." } as Record<string, string>)[flag] ?? "Source review needed.";
}

type LocalFile = Pick<File, "name" | "size" | "arrayBuffer">;
type PdfCheck = { state: "matched"; url: string; sheetId: string } | { state: "blocked" | "cancelled"; message: string };
type PdfDependencies = { digest: (bytes: ArrayBuffer) => Promise<ArrayBuffer>; createUrl: (blob: Blob) => string; revokeUrl: (url: string) => void };
// Hashing is intentionally single-flight across mounted sessions: cancelling a
// WebCrypto digest cannot stop its work, so a rapid reopen must not multiply it.
let digestBusy = false;
export class LocalPdfSession {
  private generation = 0;
  private objectUrl: string | null = null;
  constructor(private readonly deps: PdfDependencies = {
    digest: bytes => crypto.subtle.digest("SHA-256", bytes),
    createUrl: blob => URL.createObjectURL(blob), revokeUrl: url => URL.revokeObjectURL(url),
  }) {}
  clear(): void {
    this.generation++;
    if (this.objectUrl) this.deps.revokeUrl(this.objectUrl);
    this.objectUrl = null;
  }
  async check(file: LocalFile, sheet: LocalMapSheet): Promise<PdfCheck> {
    this.clear(); const token = this.generation;
    if (digestBusy) return { state: "blocked", message: "A file check is finishing. Try again in a moment." };
    if (file.name !== sheet.fileName || file.size !== sheet.sizeBytes || file.size < 5 || file.size > MAX_LOCAL_PDF_BYTES) return { state: "blocked", message: "Filename or size differs from the selected sheet, or the file exceeds 100 MiB. Nothing opened." };
    digestBusy = true;
    try {
      const bytes = await file.arrayBuffer();
      if (token !== this.generation) return { state: "cancelled", message: "File check cancelled." };
      if (bytes.byteLength !== sheet.sizeBytes || new TextDecoder().decode(bytes.slice(0, 5)) !== "%PDF-") return { state: "blocked", message: "The file is not the expected bounded PDF. Nothing opened." };
      const digest = await this.deps.digest(bytes);
      if (token !== this.generation) return { state: "cancelled", message: "File check cancelled." };
      const sha256 = [...new Uint8Array(digest)].map(byte => byte.toString(16).padStart(2, "0")).join("");
      if (sha256 !== sheet.sha256) return { state: "blocked", message: "The SHA-256 differs from the selected inventory record. Nothing opened." };
      this.objectUrl = this.deps.createUrl(new Blob([bytes], { type: "application/pdf" }));
      return { state: "matched", url: this.objectUrl, sheetId: sheet.id };
    } catch {
      return { state: token === this.generation ? "blocked" : "cancelled", message: "The browser could not verify this file. Nothing opened." };
    } finally { digestBusy = false; }
  }
}
