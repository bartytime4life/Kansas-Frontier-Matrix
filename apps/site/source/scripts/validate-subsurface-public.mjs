import { createHash } from "node:crypto";
import { lstatSync, readdirSync, readFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { gunzipSync } from "node:zlib";

export const HOLD_MANIFEST = {"version": 1, "status": "PUBLICATION_HELD", "sources": [], "tiles": [], "counties": [], "totals": {"wellCount": 0, "coreCount": 0}, "reason": "Subsurface records withheld pending rights, sensitivity, evidence, policy, review and release closure."};
function containsRestricted(value) {
  if (!value || typeof value !== "object") return false;
  if (Array.isArray(value)) {
    if (typeof value[0] === "string" && /^(wwc5|core)-[0-9]+$/.test(value[0]) && Array.isArray(value[2])) return true;
    return value.some(containsRestricted);
  }
  const metadata = value.properties ?? value; // GeoJSON keeps record metadata beside geometry.
  if ((value.coordinates || value.geometry) &&
      (/^(well|core|borehole|log)$/i.test(metadata.kind ?? "") || /^kgs-(wwc5|core)/.test(metadata.sourceId ?? "") || /^(wwc5|core)-[0-9]+$/.test(metadata.id ?? value.id ?? ""))) return true;
  if ((value.locator?.url && /subsurface/.test(value.locator.url)) || (value.tiles && value.horizontalTransform)) return true;
  return Object.values(value).some(containsRestricted);
}

// This is a denial gate, not a release validator. No manifest can approve data.
export function validateSubsurfacePublic(root) {
  const errors = [];
  const visit = directory => {
    for (const name of readdirSync(directory)) {
      const file = path.join(directory, name), relative = path.relative(root, file).split(path.sep).join("/");
      const stat = lstatSync(file);
      if (stat.isSymbolicLink()) { errors.push(relative + ": static symlink cannot be assessed"); continue; }
      if (stat.isDirectory()) { visit(file); continue; }
      if (relative.startsWith("data/subsurface/")) {
        if (relative === "data/subsurface/geophysics.json") {
          if (createHash("sha256").update(readFileSync(file)).digest("hex") !== "5150c0eb992a333142ce0754b8acd17db8cb9009125cb34ed1c32a50b6e03359") errors.push(relative + ": separate survey carrier changed; review required");
          continue;
        }
        if (relative !== "data/subsurface/manifest.json") { errors.push(relative + ": subsurface delivery is held"); continue; }
        try {
          const value = JSON.parse(readFileSync(file, "utf8"));
          // Compare the entire structure, including nested fields, without key-order dependence.
          if (JSON.stringify(sort(value)) !== JSON.stringify(sort(HOLD_MANIFEST))) errors.push(relative + ": only the empty hold notice is permitted");
        } catch { errors.push(relative + ": invalid hold notice"); }
        continue;
      }
      try {
        let bytes = readFileSync(file);
        const gzip = bytes[0] === 0x1f && bytes[1] === 0x8b;
        if (gzip) bytes = gunzipSync(bytes, { maxOutputLength: 30_000_000 });
        const text = bytes.toString("utf8").trimStart();
        if (!gzip && !/\.(json|geojson|gz)$/i.test(name) && !/^[{[]/.test(text)) continue;
        let value;
        try { value = JSON.parse(text); } catch (error) {
          if (gzip || /\.(json|geojson|gz)$/i.test(name)) throw error;
          continue; // Ordinary JS/text beginning with a brace is not a JSON carrier.
        }
        if (containsRestricted(value)) errors.push(relative + ": restricted subsurface carrier outside reserved path");
      } catch { errors.push(relative + ": static JSON carrier cannot be assessed"); }
    }
  };
  if (lstatSync(root).isSymbolicLink()) return ["Static root cannot be a symlink"];
  visit(root);
  return errors;
}
function sort(value) {
  if (Array.isArray(value)) return value.map(sort);
  if (value && typeof value === "object") return Object.fromEntries(Object.keys(value).sort().map(key => [key, sort(value[key])]));
  return value;
}
if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try {
    const errors = validateSubsurfacePublic(path.resolve(process.argv[2] ?? new URL("../public", import.meta.url).pathname));
    if (errors.length) throw new Error(errors.join("\n"));
    console.log("Subsurface static delivery held; public assets passed containment checks.");
  } catch (error) { console.error(error.message); process.exitCode = 1; }
}
