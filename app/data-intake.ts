import { OFFICIAL_CONTEXT_SOURCES } from "./live-context";

export const MAX_UPLOAD_BYTES = 10 * 1024 * 1024;
export const UPLOAD_EXTENSIONS = ["csv", "json", "geojson", "kml", "kmz", "zip", "gpkg", "tif", "tiff", "nc", "pdf", "txt", "xml", "xlsx"];
export const REVIEW_STATES = ["submitted", "under_review", "changes_requested", "accepted", "rejected"] as const;
export type ReviewState = typeof REVIEW_STATES[number];
export const REVIEW_LABELS: Record<ReviewState, string> = { submitted: "Submitted", under_review: "In review", changes_requested: "Changes requested", accepted: "Accepted for preparation", rejected: "Declined" };
export const DATA_SOURCES = [{ id: "general", title: "General KFM proposal" }, ...OFFICIAL_CONTEXT_SOURCES.map((s) => ({ id: s.id, title: s.shortTitle })), { id: "noaa-daily-weather", title: "NOAA daily weather history" }, { id: "geology", title: "Kansas mapped geology" }, { id: "flora-fauna", title: "Flora / fauna records" }, { id: "history", title: "County and historical records" }];
export type SubmissionFields = { title: string; sourceId: string; sourceUrl: string; description: string; license: string; sensitivity: string; startDate: string; endDate: string };
export type Submission = SubmissionFields & { id: string; ownerName: string; fileName: string; fileBytes: number; fileSha256: string; status: ReviewState; version: number; createdAt: string; updatedAt: string };
export type Review = { id: string; reviewerName: string; previousStatus: ReviewState; status: ReviewState; note: string; version: number; createdAt: string };

const date = (value: string) => value === "" || /^\d{4}-\d{2}-\d{2}$/.test(value) && Number.isFinite(Date.parse(value)) && new Date(value).toISOString().slice(0,10) === value;
export function validateSubmission(input: Record<string, unknown>): SubmissionFields {
  const limits = { title: 160, sourceId: 100, sourceUrl: 1500, description: 6000, license: 1000, sensitivity: 30, startDate: 10, endDate: 10 };
  const result = {} as SubmissionFields;
  for (const key of Object.keys(limits) as (keyof SubmissionFields)[]) {
    if (typeof input[key] !== "string" || input[key].length > limits[key]) throw new Error(`Check the ${key} field.`);
    result[key] = input[key].trim();
  }
  if (result.title.length < 3 || result.description.length < 10) throw new Error("Add a title and a description of what the data contains.");
  if (!DATA_SOURCES.some((s) => s.id === result.sourceId)) throw new Error("Choose a listed source or General KFM proposal.");
  if (!["public", "restricted", "unknown"].includes(result.sensitivity)) throw new Error("Choose the data sensitivity.");
  if (!result.license) throw new Error("Describe the reuse terms, or enter Unknown for steward review.");
  if (!date(result.startDate) || !date(result.endDate) || result.startDate && result.endDate && result.startDate > result.endDate) throw new Error("Check the coverage dates.");
  if (result.sourceUrl) {
    let url: URL; try { url = new URL(result.sourceUrl); } catch { throw new Error("Enter a complete HTTPS source link."); }
    if (url.protocol !== "https:" || url.username || url.password) throw new Error("Use an HTTPS source link without credentials.");
  }
  return result;
}
export function validateUpload(name: string, size: number) {
  if (!name || name.length > 200 || /[\x00-\x1f\x7f/\\]/.test(name) || !UPLOAD_EXTENSIONS.includes(name.split(".").pop()?.toLowerCase() ?? "")) throw new Error("Choose a supported data or document file.");
  if (!Number.isInteger(size) || size < 1 || size > MAX_UPLOAD_BYTES) throw new Error("Choose a non-empty file no larger than 10 MB.");
}
export function validateReview(submission: SubmissionFields & { status: ReviewState }, status: unknown, note: unknown) {
  if (!REVIEW_STATES.includes(status as ReviewState) || status === "submitted" || status === submission.status) throw new Error("Choose a different review decision.");
  if (typeof note !== "string" || note.trim().length < 10 || note.length > 4000) throw new Error("Record a review note of 10–4,000 characters.");
  if (status === "accepted" && (submission.sensitivity !== "public" || /^(unknown|unsure|none|n\/a)$/i.test(submission.license) || !submission.sourceUrl)) throw new Error("Acceptance needs public sensitivity, stated reuse terms, and a source link. Request a corrected submission first.");
  return { status: status as ReviewState, note: note.trim() };
}
