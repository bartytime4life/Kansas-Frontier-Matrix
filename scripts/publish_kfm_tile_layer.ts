#!/usr/bin/env node
import { createHash } from "crypto";
import { readFileSync, writeFileSync, mkdirSync, existsSync } from "fs";
import { dirname, join, resolve } from "path";

export type TileReleaseOutcome = "PUBLISHABLE" | "BLOCKED" | "NEEDS_RECEIPT" | "ERROR";

export interface TileReleaseValidationResult {
  outcome: TileReleaseOutcome;
  layer_id: string;
  spec_hash?: string;
  reasons: string[];
  required_receipts_missing?: string[];
  generated?: { tilejson?: unknown; release_manifest?: unknown; catalog_record?: unknown; registry_entry?: unknown };
}

const BLOCKED_ROLE_MARKERS = ["raw", "work", "quarantine", "canonical-private", "canonical_private"];
const BLOCKED_PATH_MARKERS = ["raw", "work", "quarantine", "canonical-private", "private", "restricted", "draft", "staging", "unreleased"];
const PUBLIC_VALUES = new Set(["public", "public-safe", "public_safe"]);
const APPROVED_STATES = new Set(["approved", "released"]);

function sortValue(v: any): any {
  if (Array.isArray(v)) return v.map(sortValue);
  if (v && typeof v === "object") {
    return Object.keys(v).sort().reduce((acc: Record<string, any>, k) => { acc[k] = sortValue(v[k]); return acc; }, {});
  }
  return v;
}
function canonicalStringify(v: any): string { return JSON.stringify(sortValue(v)); }
function sha256(v: string | Buffer): string { return `sha256:${createHash("sha256").update(v).digest("hex")}`; }

function hasBlockedMarker(s?: string): boolean {
  if (!s) return false;
  const lowered = s.toLowerCase();
  return BLOCKED_PATH_MARKERS.some((m) => lowered.includes(m));
}

function publish(candidate: any, pmtilesMeta: any, publishedAt: string): TileReleaseValidationResult {
  const reasons: string[] = [];
  const missing: string[] = [];
  const layer_id = String(candidate.id || "unknown");
  const spec_hash = candidate.spec_hash;
  if (!/^sha256:[a-f0-9]{64}$/.test(spec_hash || "")) reasons.push("invalid or missing spec_hash");
  if (!PUBLIC_VALUES.has(String(candidate.policy_label || "").toLowerCase())) reasons.push("policy_label is not public");
  if (!PUBLIC_VALUES.has(String(candidate.sensitivity || "").toLowerCase())) reasons.push("sensitivity is not public");
  if (!APPROVED_STATES.has(String(candidate.review_state || "").toLowerCase())) reasons.push("review_state is not approved/released");
  if (String(candidate.release_state || "").toLowerCase() !== "released") reasons.push("release_state is not released");
  if (BLOCKED_ROLE_MARKERS.some((m) => String(candidate.role || "").toLowerCase().includes(m))) reasons.push("role is blocked for publication");
  if (hasBlockedMarker(candidate.source_pmtiles) || hasBlockedMarker(candidate.tilejson_path)) reasons.push("source path contains blocked lifecycle marker");
  if (candidate.fallback?.source && hasBlockedMarker(candidate.fallback.source)) reasons.push("fallback source is not public-safe");

  const receipts = Array.isArray(candidate.receipts) ? candidate.receipts : [];
  for (const kind of ["redaction_receipt", "generalization_receipt"]) {
    if (!receipts.find((r: any) => r.type === kind)) missing.push(kind);
  }
  for (const r of receipts) {
    if (r.layer_id && r.layer_id !== layer_id) reasons.push(`receipt layer mismatch: ${r.type || "unknown"}`);
    if (r.spec_hash && r.spec_hash !== spec_hash) reasons.push(`receipt spec_hash mismatch: ${r.type || "unknown"}`);
  }

  if (pmtilesMeta?.["kfm:spec_hash"] !== spec_hash) reasons.push("PMTiles metadata spec_hash mismatch");

  const tilejson: any = {
    tilejson: "3.0.0",
    name: candidate.title,
    tiles: [candidate.source_pmtiles],
    minzoom: candidate.minzoom,
    maxzoom: candidate.maxzoom,
    vector_layers: candidate.vector_layers,
    "kfm:spec_hash": spec_hash,
    "kfm:release_manifest": `release-manifest/${layer_id}.${spec_hash}.json`,
    "kfm:policy_label": candidate.policy_label,
    "kfm:sensitivity": candidate.sensitivity
  };
  if (candidate.catalog?.public_safe_geometry === true && candidate.bounds) tilejson.bounds = candidate.bounds;
  if (candidate.catalog?.public_safe_geometry === true && candidate.center) tilejson.center = candidate.center;

  if (tilejson["kfm:spec_hash"] !== spec_hash) reasons.push("TileJSON spec_hash mismatch");

  const catalogRecord = {
    id: layer_id,
    type: "Feature",
    collection: candidate.catalog?.collection || "kfm-map-layers",
    properties: {
      "kfm:spec_hash": spec_hash,
      "kfm:policy_label": candidate.policy_label,
      "kfm:sensitivity": candidate.sensitivity,
      datetime: candidate.time_start || candidate.created_at,
      start_datetime: candidate.time_start,
      end_datetime: candidate.time_end
    },
    geometry: candidate.catalog?.public_safe_geometry === true ? (candidate.catalog?.geometry || null) : null,
    assets: {
      tilejson: { href: candidate.tilejson_path, type: "application/json" },
      pmtiles: { href: candidate.source_pmtiles, type: "application/vnd.pmtiles" }
    },
    links: [
      { rel: "release-manifest", href: `release-manifest/${layer_id}.${spec_hash}.json` },
      ...receipts.map((r: any) => ({ rel: "receipt", href: r.ref, type: r.type }))
    ]
  };
  if (candidate.catalog?.public_safe_geometry !== true && candidate.catalog?.geometry) reasons.push("catalog includes sensitive exact geometry");

  const manifestBase = {
    manifest_type: "kfm_tile_release_manifest",
    manifest_version: "1.0.0",
    layer_id,
    spec_hash,
    tilejson,
    source_pmtiles: candidate.source_pmtiles,
    catalog_records: [catalogRecord.id],
    receipts,
    fallback: candidate.fallback,
    policy_label: candidate.policy_label,
    sensitivity: candidate.sensitivity,
    review_state: candidate.review_state,
    release_state: candidate.release_state,
    published_at: publishedAt,
    publisher: candidate.publisher,
    determinism: { canonical_json: true, hash_alg: "sha256", excludes: ["published_at"] },
    kfm_meta: { candidate_created_at: candidate.created_at }
  };

  const artifact_hashes = {
    tilejson_sha256: sha256(canonicalStringify(tilejson)),
    catalog_record_sha256: sha256(canonicalStringify(catalogRecord)),
    source_pmtiles_sha256: pmtilesMeta?.fixture_bytes_sha256 || pmtilesMeta?.pmtiles_sha256 || "sha256:missing"
  };

  const releaseManifest = { ...manifestBase, artifact_hashes };

  const registryEntry = {
    id: layer_id,
    spec_hash,
    release_state: candidate.release_state,
    visibility: "public",
    tilejson: candidate.tilejson_path,
    pmtiles: candidate.source_pmtiles,
    fallback: candidate.fallback,
    receipts: receipts.map((r: any) => ({ type: r.type, ref: r.ref }))
  };

  if (reasons.length) return { outcome: "BLOCKED", layer_id, spec_hash, reasons };
  if (missing.length) return { outcome: "NEEDS_RECEIPT", layer_id, spec_hash, reasons: ["required receipts missing"], required_receipts_missing: missing };
  return { outcome: "PUBLISHABLE", layer_id, spec_hash, reasons: [], generated: { tilejson, release_manifest: releaseManifest, catalog_record: catalogRecord, registry_entry: registryEntry } };
}

function main() {
  const [candidatePath, pmtilesMetaPath, outDir] = process.argv.slice(2);
  if (!candidatePath || !pmtilesMetaPath || !outDir) throw new Error("usage: publish_kfm_tile_layer.ts <candidate.json> <pmtiles_metadata.json> <out_dir>");
  const candidate = JSON.parse(readFileSync(candidatePath, "utf8"));
  const pmtilesMeta = JSON.parse(readFileSync(pmtilesMetaPath, "utf8"));
  const publishedAt = new Date().toISOString();
  const result = publish(candidate, pmtilesMeta, publishedAt);
  mkdirSync(outDir, { recursive: true });
  writeFileSync(join(outDir, "result.json"), JSON.stringify(result, null, 2) + "\n");
  if (result.outcome === "PUBLISHABLE" && result.generated) {
    writeFileSync(join(outDir, "tilejson.json"), JSON.stringify(result.generated.tilejson, null, 2) + "\n");
    writeFileSync(join(outDir, "release_manifest.json"), JSON.stringify(result.generated.release_manifest, null, 2) + "\n");
    writeFileSync(join(outDir, "catalog_record.json"), JSON.stringify(result.generated.catalog_record, null, 2) + "\n");
    const registryPath = resolve("data/registry/layers/layers.json");
    let registry: any[] = [];
    if (existsSync(registryPath)) registry = JSON.parse(readFileSync(registryPath, "utf8"));
    registry = registry.filter((e) => e.id !== result.layer_id);
    registry.push(result.generated.registry_entry as any);
    writeFileSync(registryPath, JSON.stringify(registry, null, 2) + "\n");
    const stacPath = resolve(`data/catalog/stac/kfm-map-layers/${result.layer_id}.json`);
    mkdirSync(dirname(stacPath), { recursive: true });
    writeFileSync(stacPath, JSON.stringify(result.generated.catalog_record, null, 2) + "\n");
  }
  console.log(JSON.stringify(result, null, 2));
}

if (require.main === module) {
  try { main(); } catch (e: any) {
    const fail: TileReleaseValidationResult = { outcome: "ERROR", layer_id: "unknown", reasons: [e.message] };
    console.error(JSON.stringify(fail, null, 2));
    process.exit(1);
  }
}
