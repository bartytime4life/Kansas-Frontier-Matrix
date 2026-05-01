import crypto from "node:crypto";

export const OUTCOMES = ["PUBLISHABLE", "BLOCKED", "NEEDS_RECEIPT", "ERROR"];

const BLOCKED_ROLES = ["raw", "work", "quarantine", "canonical-private", "private", "restricted", "draft", "staging", "unreleased"];
const BLOCKED_PATH_MARKERS = ["raw", "work", "quarantine", "canonical-private", "private", "restricted", "draft", "staging", "unreleased"];

function canonicalize(value) {
  if (Array.isArray(value)) return `[${value.map(canonicalize).join(",")}]`;
  if (value && typeof value === "object") {
    const keys = Object.keys(value).sort();
    return `{${keys.map((k) => `${JSON.stringify(k)}:${canonicalize(value[k])}`).join(",")}}`;
  }
  return JSON.stringify(value);
}

function sha256String(text) {
  return `sha256:${crypto.createHash("sha256").update(text).digest("hex")}`;
}

export function isSpecHash(value) {
  return typeof value === "string" && /^sha256:[a-f0-9]{64}$/.test(value);
}

function hasBlockedMarker(value) {
  if (!value) return false;
  const norm = String(value).toLowerCase();
  return BLOCKED_PATH_MARKERS.some((m) => norm.includes(m));
}

export function publishTileLayer(candidate, pmtilesMetadata = {}, publishedAt = new Date().toISOString()) {
  const reasons = [];
  const missingReceipts = [];
  const layerId = candidate?.id ?? "unknown";

  try {
    if (!isSpecHash(candidate?.spec_hash)) reasons.push("missing_or_malformed_spec_hash");
    if (String(candidate?.policy_label || "").toLowerCase() !== "public") reasons.push("policy_label_not_public");
    if (String(candidate?.sensitivity || "").toLowerCase() !== "public") reasons.push("sensitivity_not_public");
    if (!["approved", "released"].includes(String(candidate?.review_state || "").toLowerCase())) reasons.push("review_state_not_approved_or_released");
    if (String(candidate?.release_state || "").toLowerCase() !== "released") reasons.push("release_state_not_released");
    if (BLOCKED_ROLES.some((r) => String(candidate?.role || "").toLowerCase().includes(r))) reasons.push("role_not_publishable");
    if (hasBlockedMarker(candidate?.source_pmtiles) || hasBlockedMarker(candidate?.tilejson_path)) reasons.push("source_path_not_public_safe");
    if (candidate?.fallback?.public_safe !== true) reasons.push("fallback_not_public_safe");

    const required = candidate?.receipts?.required_types || [];
    const provided = candidate?.receipts?.items || [];
    for (const t of required) {
      if (!provided.find((r) => r.type === t)) missingReceipts.push(t);
    }
    for (const r of provided) {
      if (r.layer_id !== candidate?.id || r.spec_hash !== candidate?.spec_hash) {
        reasons.push("receipt_identity_mismatch");
      }
    }

    if (missingReceipts.length > 0) {
      return { outcome: "NEEDS_RECEIPT", layer_id: layerId, spec_hash: candidate?.spec_hash, reasons: ["required_receipts_missing"], required_receipts_missing: missingReceipts };
    }

    const tilejson = {
      tilejson: "3.0.0",
      name: candidate.title,
      tiles: [candidate.source_pmtiles],
      minzoom: candidate.minzoom,
      maxzoom: candidate.maxzoom,
      vector_layers: candidate.vector_layers,
      "kfm:spec_hash": candidate.spec_hash,
      "kfm:release_manifest": `manifests/${candidate.id}.${candidate.spec_hash}.json`,
      "kfm:policy_label": candidate.policy_label,
      "kfm:sensitivity": candidate.sensitivity,
    };

    if (candidate.public_safe_geometry === true) {
      if (candidate.bounds) tilejson.bounds = candidate.bounds;
      if (candidate.center) tilejson.center = candidate.center;
    }

    if (candidate?.tilejson_fixture?.["kfm:spec_hash"] && candidate.tilejson_fixture["kfm:spec_hash"] !== candidate.spec_hash) reasons.push("tilejson_spec_hash_mismatch");
    if (pmtilesMetadata?.["kfm:spec_hash"] && pmtilesMetadata["kfm:spec_hash"] !== candidate.spec_hash) reasons.push("pmtiles_spec_hash_mismatch");
    if (candidate?.catalog?.geometry_exact === true) reasons.push("catalog_sensitive_geometry_detected");

    const tilejsonHash = sha256String(canonicalize(tilejson));
    const catalogRecord = {
      id: candidate.id,
      type: "Feature",
      stac_version: "1.0.0",
      collection: candidate.catalog?.collection || "kfm-map-layers",
      properties: {
        "kfm:spec_hash": candidate.spec_hash,
        "kfm:policy_label": candidate.policy_label,
        "kfm:sensitivity": candidate.sensitivity,
        datetime: candidate.time_start ?? null,
        start_datetime: candidate.time_start,
        end_datetime: candidate.time_end,
      },
      assets: {
        tilejson: { href: candidate.tilejson_path, type: "application/json", roles: ["metadata"] },
        pmtiles: { href: candidate.source_pmtiles, type: "application/vnd.pmtiles", roles: ["data"] },
      },
      links: [
        { rel: "release_manifest", href: `manifests/${candidate.id}.${candidate.spec_hash}.json` },
        ...provided.map((r) => ({ rel: r.type, href: r.href })),
      ],
    };

    const manifestBase = {
      manifest_type: "KFM_TileReleaseManifest",
      manifest_version: "1.0.0",
      layer_id: candidate.id,
      spec_hash: candidate.spec_hash,
      artifact_hashes: {
        tilejson: tilejsonHash,
        pmtiles: pmtilesMetadata?.artifact_hash || "sha256:fixture",
      },
      tilejson: { path: candidate.tilejson_path, hash: tilejsonHash },
      source_pmtiles: { path: candidate.source_pmtiles, hash: pmtilesMetadata?.artifact_hash || "sha256:fixture" },
      catalog_records: [{ path: `data/catalog/stac/kfm-map-layers/${candidate.id}.json` }],
      receipts: provided.map((r) => ({ type: r.type, href: r.href, layer_id: r.layer_id, spec_hash: r.spec_hash })),
      fallback: candidate.fallback,
      policy_label: candidate.policy_label,
      sensitivity: candidate.sensitivity,
      review_state: candidate.review_state,
      release_state: candidate.release_state,
      publisher: candidate.publisher,
      determinism: { canonical_json: true, hash_algorithm: "sha256", excludes: ["published_at"] },
      kfm_meta: { block_version: 2, artifact_type: "release_manifest" },
    };

    const manifestDeterministicHash = sha256String(canonicalize(manifestBase));
    const releaseManifest = { ...manifestBase, published_at: publishedAt, artifact_hashes: { ...manifestBase.artifact_hashes, manifest: manifestDeterministicHash } };

    const registryEntry = {
      id: candidate.id,
      title: candidate.title,
      release_state: candidate.release_state,
      policy_label: candidate.policy_label,
      sensitivity: candidate.sensitivity,
      spec_hash: candidate.spec_hash,
      source_pmtiles: candidate.source_pmtiles,
      tilejson: candidate.tilejson_path,
      fallback: candidate.fallback,
      receipts: provided.map((r) => ({ type: r.type, href: r.href })),
    };

    if (reasons.length > 0) return { outcome: "BLOCKED", layer_id: layerId, spec_hash: candidate?.spec_hash, reasons };

    return {
      outcome: "PUBLISHABLE",
      layer_id: layerId,
      spec_hash: candidate.spec_hash,
      reasons,
      generated: { tilejson, release_manifest: releaseManifest, catalog_record: catalogRecord, registry_entry: registryEntry },
    };
  } catch (error) {
    return { outcome: "ERROR", layer_id: layerId, spec_hash: candidate?.spec_hash, reasons: [String(error?.message || error)] };
  }
}

export { canonicalize, sha256String };
