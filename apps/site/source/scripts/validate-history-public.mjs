import { lstatSync, readdirSync, readFileSync } from "node:fs";
import path from "node:path";
import { brotliDecompressSync, gunzipSync } from "node:zlib";

const kinds = new Set(["person", "event", "topic", "organization", "fictional"]);
function containsResearch(value) {
  if (!value || typeof value !== "object") return false;
  if (Array.isArray(value)) return value.some(containsResearch);
  // This profile has no public release path. Changing its lifecycle labels is
  // not approval, and wrapping or extracting its records must not bypass a hold.
  if (Array.isArray(value.records) && Array.isArray(value.sources) && value.lifecycle) return true;
  if (kinds.has(value.kind) && typeof value.sourceId === "string" && typeof value.title === "string"
      && ("reviewNote" in value || "reviewStatus" in value) && ("date" in value || "place" in value)) return true;
  return Object.values(value).some(containsResearch);
}
function researchCsv(text) {
  const header = new Set(text.replace(/^\uFEFF/, "").split(/[\r\n]/, 1)[0].split(",")
    .map(cell => cell.trim().replace(/^"|"$/g, "").toLowerCase()));
  return ["sourceid", "kind", "title", "relation", "reviewnote"].every(field => header.has(field));
}

// A denial gate only: no metadata, manifest or approval-shaped label releases
// the held history research profile. A future derivative needs separate review.
export function validateHistoryPublic(root) {
  const errors = [];
  const visit = directory => {
    for (const name of readdirSync(directory)) {
      const file = path.join(directory, name);
      const relative = path.relative(root, file).split(path.sep).join("/");
      const stat = lstatSync(file);
      if (stat.isSymbolicLink()) { errors.push(relative + ": static symlink cannot be assessed"); continue; }
      if (/^history\/people-events(?:[./]|$)/i.test(relative)) { errors.push(relative + ": history research delivery is held"); continue; }
      if (stat.isDirectory()) { visit(file); continue; }
      if (!stat.isFile()) { errors.push(relative + ": static carrier cannot be assessed"); continue; }
      try {
        let bytes = readFileSync(file);
        const gzip = bytes[0] === 0x1f && bytes[1] === 0x8b;
        const brotli = /\.br$/i.test(name);
        if (gzip) bytes = gunzipSync(bytes, { maxOutputLength: 30_000_000 });
        else if (brotli) bytes = brotliDecompressSync(bytes, { maxOutputLength: 30_000_000 });
        const text = bytes.toString("utf8").replace(/^\uFEFF/, "").trimStart();
        if (researchCsv(text)) { errors.push(relative + ": history research CSV delivery is held"); continue; }
        if (!/^[{[]/.test(text) && !/\.(json|geojson)(?:\.(gz|br))?$/i.test(name)) continue;
        let value;
        try { value = JSON.parse(text); } catch (error) {
          if (gzip || brotli || /\.(json|geojson)(?:\.(gz|br))?$/i.test(name)) throw error;
          continue;
        }
        if (containsResearch(value)) errors.push(relative + ": history research carrier outside reserved path");
      } catch { errors.push(relative + ": static history carrier cannot be assessed"); }
    }
  };
  if (lstatSync(root).isSymbolicLink()) return ["Static root cannot be a symlink"];
  visit(root);
  return errors;
}
