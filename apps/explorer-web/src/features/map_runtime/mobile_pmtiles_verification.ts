/**
 * Fixture-only mobile PMTiles verification.
 *
 * The browser receives already-bounded synthetic bytes and sidecars. This
 * module performs no fetch, source access, MapLibre import, policy evaluation,
 * lifecycle-store access, release, deployment, or publication.
 *
 * A PASS proves archive/index/tile integrity and one injected decode/render
 * probe under a mobile envelope. Cryptographic verification, live MapLibre
 * boot, and release authorization remain explicit holds.
 */

export const MOBILE_PMTILES_FIXTURE_PROFILE =
  "kfm.pmtiles.mobile-verification-fixture.v1" as const;
export const MOBILE_PMTILES_SUITE_PROFILE =
  "kfm.pmtiles.mobile-verification-fixtures.v1" as const;

export type MobilePmtilesVerificationOutcome = "PASS" | "DENY" | "ERROR";

export type MobilePmtilesVerificationCode =
  | "MOBILE_PMTILES_VERIFY_DECODE_RENDER_PASS"
  | "MOBILE_PMTILES_BUNDLE_INVALID"
  | "MOBILE_PMTILES_ARCHIVE_BASE64_INVALID"
  | "MOBILE_PMTILES_ARCHIVE_DIGEST_MISMATCH"
  | "MOBILE_PMTILES_ARCHIVE_BUDGET_EXCEEDED"
  | "MOBILE_PMTILES_HEADER_INVALID"
  | "MOBILE_PMTILES_METADATA_INVALID"
  | "MOBILE_PMTILES_SPEC_HASH_MISMATCH"
  | "MOBILE_PMTILES_SIDECAR_DIGEST_MISMATCH"
  | "MOBILE_PMTILES_MERKLE_ROOT_MISMATCH"
  | "MOBILE_PMTILES_RANGE_OUT_OF_BOUNDS"
  | "MOBILE_PMTILES_RANGE_LEAF_BINDING_INVALID"
  | "MOBILE_PMTILES_TILE_DIGEST_MISMATCH"
  | "MOBILE_PMTILES_TILE_BUDGET_EXCEEDED"
  | "MOBILE_PMTILES_TILE_PAYLOAD_INVALID"
  | "MOBILE_PMTILES_SIGNATURE_SUBJECT_MISMATCH"
  | "MOBILE_PMTILES_RUNRECEIPT_SUBJECT_MISMATCH"
  | "MOBILE_PMTILES_MAPLIBRE_AUTHORITY_OVERCLAIM"
  | "MOBILE_PMTILES_AUTHORITY_OVERCLAIM"
  | "MOBILE_PMTILES_HOLDS_INVALID"
  | "MOBILE_PMTILES_DEVICE_PROFILE_INVALID"
  | "MOBILE_PMTILES_BUDGET_INVALID"
  | "MOBILE_PMTILES_VERIFY_BUDGET_EXCEEDED"
  | "MOBILE_PMTILES_TILE_DECODE_RENDER_ERROR"
  | "MOBILE_PMTILES_TILE_RENDER_MISMATCH"
  | "MOBILE_PMTILES_DECODE_RENDER_BUDGET_EXCEEDED";

export type MobilePmtilesRenderProbe = Readonly<{
  decoded: boolean;
  rendered: boolean;
  width: number;
  height: number;
  pixelRgba: readonly number[];
}>;

export type MobilePmtilesRenderAdapter = (
  tileBytes: Uint8Array,
  mediaType: "image/png",
) => Promise<MobilePmtilesRenderProbe>;

export type MobilePmtilesVerificationResult = Readonly<{
  outcome: MobilePmtilesVerificationOutcome;
  code: MobilePmtilesVerificationCode;
  authority: "NONE";
  holds: readonly string[];
  maplibreBootState: "HOLD";
  maplibreBootReason: "MAPLIBRE_RUNTIME_UNADMITTED";
  metrics: Readonly<{
    archiveBytes: number;
    tileBytes: number;
    verifyMs: number;
    decodeRenderMs: number;
  }>;
}>;

type RecordValue = Record<string, unknown>;

type ParsedRange = Readonly<{
  tileId: "0/0/0";
  offset: number;
  length: number;
  leaf: number;
  sha256: string;
  mediaType: "image/png";
}>;

type ParsedBundle = Readonly<{
  archiveName: "mobile-base.pmtiles";
  archiveBytes: Uint8Array;
  pmidx: RecordValue;
  pmsig: RecordValue;
  runreceipt: RecordValue;
  sidecarDigests: Readonly<{
    pmidxSha256: string;
    pmsigSha256: string;
    runreceiptSha256: string;
  }>;
  budgets: Readonly<{
    maxArchiveBytes: number;
    maxTileBytes: number;
    maxVerifyMs: number;
    maxDecodeRenderMs: number;
  }>;
  holds: readonly string[];
  expectedPixelRgba: readonly number[];
}>;

type ParsedHeader = Readonly<{
  metadataOffset: number;
  metadataLength: number;
  tileDataOffset: number;
  tileDataLength: number;
  internalCompression: number;
  tileType: number;
  minZoom: number;
  maxZoom: number;
}>;

const SHA256_PATTERN = /^sha256:[a-f0-9]{64}$/;
const ZERO_HASH = `sha256:${"0".repeat(64)}`;
const HEADER_BYTES = 127;
const EXPECTED_HOLDS = Object.freeze([
  "CRYPTOGRAPHIC_VERIFICATION_UNWIRED",
  "MAPLIBRE_RUNTIME_UNADMITTED",
  "RELEASE_AUTHORIZATION_NOT_EVALUATED",
]);
const BUNDLE_FIELDS = new Set([
  "profile",
  "archive_name",
  "archive_base64",
  "pmidx",
  "pmsig",
  "runreceipt",
  "sidecar_digests",
  "mobile_profile",
  "budgets",
  "maplibre_boot_state",
  "maplibre_boot_reason",
  "holds",
  "authority",
  "expected_pixel_rgba",
]);
const AUTHORITY_FIELDS = new Set([
  "source_admission",
  "evidence",
  "policy",
  "promotion",
  "release",
  "deployment",
  "publication",
  "public_use",
]);
const MOBILE_FIELDS = new Set([
  "viewport_width",
  "viewport_height",
  "device_scale_factor",
  "has_touch",
  "is_mobile",
]);
const BUDGET_FIELDS = new Set([
  "max_archive_bytes",
  "max_tile_bytes",
  "max_verify_ms",
  "max_decode_render_ms",
]);
const SIDECAR_DIGEST_FIELDS = new Set([
  "pmidx_sha256",
  "pmsig_sha256",
  "runreceipt_sha256",
]);

function isRecord(value: unknown): value is RecordValue {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function hasExactFields(value: RecordValue, fields: ReadonlySet<string>): boolean {
  const keys = Object.keys(value);
  return keys.length === fields.size && keys.every((key) => fields.has(key));
}

function isPositiveInteger(value: unknown): value is number {
  return Number.isInteger(value) && typeof value === "number" && value > 0;
}

function isByte(value: unknown): value is number {
  return Number.isInteger(value) && typeof value === "number" && value >= 0 && value <= 255;
}

function isDigest(value: unknown): value is string {
  return (
    typeof value === "string" &&
    SHA256_PATTERN.test(value) &&
    value !== ZERO_HASH
  );
}

function equalStringSets(left: readonly string[], right: readonly string[]): boolean {
  return (
    left.length === right.length &&
    new Set(left).size === left.length &&
    left.every((value) => right.includes(value))
  );
}

function failure(
  code: MobilePmtilesVerificationCode,
  outcome: "DENY" | "ERROR" = "DENY",
  metrics?: Partial<MobilePmtilesVerificationResult["metrics"]>,
): MobilePmtilesVerificationResult {
  return Object.freeze({
    outcome,
    code,
    authority: "NONE",
    holds: EXPECTED_HOLDS,
    maplibreBootState: "HOLD",
    maplibreBootReason: "MAPLIBRE_RUNTIME_UNADMITTED",
    metrics: Object.freeze({
      archiveBytes: metrics?.archiveBytes ?? 0,
      tileBytes: metrics?.tileBytes ?? 0,
      verifyMs: metrics?.verifyMs ?? 0,
      decodeRenderMs: metrics?.decodeRenderMs ?? 0,
    }),
  });
}

function toArrayBuffer(bytes: Uint8Array): ArrayBuffer {
  return bytes.buffer.slice(
    bytes.byteOffset,
    bytes.byteOffset + bytes.byteLength,
  ) as ArrayBuffer;
}

function bytesToHex(bytes: Uint8Array): string {
  let result = "";
  for (const value of bytes) result += value.toString(16).padStart(2, "0");
  return result;
}

function hexToBytes(value: string): Uint8Array | null {
  if (!/^[a-f0-9]+$/.test(value) || value.length % 2 !== 0) return null;
  const output = new Uint8Array(value.length / 2);
  for (let index = 0; index < output.length; index += 1) {
    output[index] = Number.parseInt(value.slice(index * 2, index * 2 + 2), 16);
  }
  return output;
}

async function sha256(bytes: Uint8Array): Promise<string> {
  const digest = await crypto.subtle.digest("SHA-256", toArrayBuffer(bytes));
  return `sha256:${bytesToHex(new Uint8Array(digest))}`;
}

function canonicalJson(value: unknown): string {
  if (
    value === null ||
    typeof value === "string" ||
    typeof value === "boolean"
  ) {
    return JSON.stringify(value);
  }
  if (typeof value === "number") {
    if (!Number.isFinite(value)) throw new Error("non-finite JSON number");
    return JSON.stringify(value);
  }
  if (Array.isArray(value)) {
    return `[${value.map((item) => canonicalJson(item)).join(",")}]`;
  }
  if (isRecord(value)) {
    const entries = Object.keys(value)
      .sort()
      .map((key) => `${JSON.stringify(key)}:${canonicalJson(value[key])}`);
    return `{${entries.join(",")}}`;
  }
  throw new Error("unsupported JSON value");
}

export async function canonicalJsonSha256(value: unknown): Promise<string> {
  return sha256(new TextEncoder().encode(canonicalJson(value)));
}

export function decodeMobilePmtilesArchive(value: string): Uint8Array | null {
  try {
    const decoded = atob(value);
    const bytes = new Uint8Array(decoded.length);
    for (let index = 0; index < decoded.length; index += 1) {
      bytes[index] = decoded.charCodeAt(index);
    }
    return bytes.length >= HEADER_BYTES ? bytes : null;
  } catch {
    return null;
  }
}

function getUint64(view: DataView, offset: number): number | null {
  const value = view.getBigUint64(offset, true);
  return value <= BigInt(Number.MAX_SAFE_INTEGER) ? Number(value) : null;
}

function parseHeader(bytes: Uint8Array): ParsedHeader | null {
  if (bytes.length < HEADER_BYTES) return null;
  const magic = new TextDecoder().decode(bytes.subarray(0, 7));
  if (magic !== "PMTiles" || bytes[7] !== 3) return null;

  const view = new DataView(toArrayBuffer(bytes));
  const rootOffset = getUint64(view, 8);
  const rootLength = getUint64(view, 16);
  const metadataOffset = getUint64(view, 24);
  const metadataLength = getUint64(view, 32);
  const leafOffset = getUint64(view, 40);
  const leafLength = getUint64(view, 48);
  const tileDataOffset = getUint64(view, 56);
  const tileDataLength = getUint64(view, 64);
  if (
    [
      rootOffset,
      rootLength,
      metadataOffset,
      metadataLength,
      leafOffset,
      leafLength,
      tileDataOffset,
      tileDataLength,
    ].some((value) => value === null)
  ) {
    return null;
  }

  const regions = [
    [rootOffset as number, rootLength as number],
    [metadataOffset as number, metadataLength as number],
    [leafOffset as number, leafLength as number],
    [tileDataOffset as number, tileDataLength as number],
  ]
    .filter(([, length]) => length > 0)
    .map(([offset, length]) => [offset, offset + length] as const)
    .sort((left, right) => left[0] - right[0]);

  for (const [offset, end] of regions) {
    if (offset < HEADER_BYTES || end < offset || end > bytes.length) return null;
  }
  for (let index = 1; index < regions.length; index += 1) {
    if (regions[index][0] < regions[index - 1][1]) return null;
  }

  const internalCompression = bytes[97];
  const tileType = bytes[99];
  const minZoom = bytes[100];
  const maxZoom = bytes[101];
  if (
    internalCompression !== 1 ||
    tileType !== 2 ||
    minZoom !== 0 ||
    maxZoom !== 0
  ) {
    return null;
  }

  return Object.freeze({
    metadataOffset: metadataOffset as number,
    metadataLength: metadataLength as number,
    tileDataOffset: tileDataOffset as number,
    tileDataLength: tileDataLength as number,
    internalCompression,
    tileType,
    minZoom,
    maxZoom,
  });
}

function parseBundle(input: unknown): ParsedBundle | MobilePmtilesVerificationResult {
  if (!isRecord(input) || !hasExactFields(input, BUNDLE_FIELDS)) {
    return failure("MOBILE_PMTILES_BUNDLE_INVALID");
  }
  if (
    input.profile !== MOBILE_PMTILES_FIXTURE_PROFILE ||
    input.archive_name !== "mobile-base.pmtiles" ||
    typeof input.archive_base64 !== "string" ||
    !isRecord(input.pmidx) ||
    !isRecord(input.pmsig) ||
    !isRecord(input.runreceipt)
  ) {
    return failure("MOBILE_PMTILES_BUNDLE_INVALID");
  }

  if (
    input.maplibre_boot_state !== "HOLD" ||
    input.maplibre_boot_reason !== "MAPLIBRE_RUNTIME_UNADMITTED"
  ) {
    return failure("MOBILE_PMTILES_MAPLIBRE_AUTHORITY_OVERCLAIM");
  }

  if (
    !Array.isArray(input.holds) ||
    !input.holds.every((value): value is string => typeof value === "string") ||
    !equalStringSets(input.holds, EXPECTED_HOLDS)
  ) {
    return failure("MOBILE_PMTILES_HOLDS_INVALID");
  }

  if (
    !isRecord(input.authority) ||
    !hasExactFields(input.authority, AUTHORITY_FIELDS) ||
    Object.values(input.authority).some((value) => value !== false)
  ) {
    return failure("MOBILE_PMTILES_AUTHORITY_OVERCLAIM");
  }

  if (
    !isRecord(input.mobile_profile) ||
    !hasExactFields(input.mobile_profile, MOBILE_FIELDS) ||
    !isPositiveInteger(input.mobile_profile.viewport_width) ||
    !isPositiveInteger(input.mobile_profile.viewport_height) ||
    !isPositiveInteger(input.mobile_profile.device_scale_factor) ||
    input.mobile_profile.has_touch !== true ||
    input.mobile_profile.is_mobile !== true
  ) {
    return failure("MOBILE_PMTILES_DEVICE_PROFILE_INVALID");
  }

  if (
    !isRecord(input.budgets) ||
    !hasExactFields(input.budgets, BUDGET_FIELDS) ||
    !isPositiveInteger(input.budgets.max_archive_bytes) ||
    !isPositiveInteger(input.budgets.max_tile_bytes) ||
    !isPositiveInteger(input.budgets.max_verify_ms) ||
    !isPositiveInteger(input.budgets.max_decode_render_ms)
  ) {
    return failure("MOBILE_PMTILES_BUDGET_INVALID");
  }

  if (
    !isRecord(input.sidecar_digests) ||
    !hasExactFields(input.sidecar_digests, SIDECAR_DIGEST_FIELDS) ||
    !isDigest(input.sidecar_digests.pmidx_sha256) ||
    !isDigest(input.sidecar_digests.pmsig_sha256) ||
    !isDigest(input.sidecar_digests.runreceipt_sha256)
  ) {
    return failure("MOBILE_PMTILES_BUNDLE_INVALID");
  }

  if (
    !Array.isArray(input.expected_pixel_rgba) ||
    input.expected_pixel_rgba.length !== 4 ||
    !input.expected_pixel_rgba.every(isByte)
  ) {
    return failure("MOBILE_PMTILES_BUNDLE_INVALID");
  }

  const archiveBytes = decodeMobilePmtilesArchive(input.archive_base64);
  if (archiveBytes === null) {
    return failure("MOBILE_PMTILES_ARCHIVE_BASE64_INVALID");
  }

  return Object.freeze({
    archiveName: "mobile-base.pmtiles",
    archiveBytes,
    pmidx: input.pmidx,
    pmsig: input.pmsig,
    runreceipt: input.runreceipt,
    sidecarDigests: Object.freeze({
      pmidxSha256: input.sidecar_digests.pmidx_sha256,
      pmsigSha256: input.sidecar_digests.pmsig_sha256,
      runreceiptSha256: input.sidecar_digests.runreceipt_sha256,
    }),
    budgets: Object.freeze({
      maxArchiveBytes: input.budgets.max_archive_bytes,
      maxTileBytes: input.budgets.max_tile_bytes,
      maxVerifyMs: input.budgets.max_verify_ms,
      maxDecodeRenderMs: input.budgets.max_decode_render_ms,
    }),
    holds: Object.freeze([...input.holds]),
    expectedPixelRgba: Object.freeze([...input.expected_pixel_rgba]),
  });
}

function parseRange(value: unknown): ParsedRange | null {
  if (!isRecord(value)) return null;
  if (
    value.tile_id !== "0/0/0" ||
    !Number.isInteger(value.offset) ||
    typeof value.offset !== "number" ||
    value.offset < 0 ||
    !isPositiveInteger(value.length) ||
    !Number.isInteger(value.leaf) ||
    typeof value.leaf !== "number" ||
    value.leaf < 0 ||
    !isDigest(value.sha256) ||
    value.media_type !== "image/png"
  ) {
    return null;
  }
  return Object.freeze({
    tileId: "0/0/0",
    offset: value.offset,
    length: value.length,
    leaf: value.leaf,
    sha256: value.sha256,
    mediaType: "image/png",
  });
}

async function computeMerkleRoot(
  leaves: readonly string[],
  arity: number,
): Promise<string | null> {
  if (!Number.isInteger(arity) || arity < 2 || arity > 64) return null;
  let level: Uint8Array[] = [];
  for (const leaf of leaves) {
    if (!isDigest(leaf)) return null;
    const bytes = hexToBytes(leaf.slice(7));
    if (bytes === null) return null;
    level.push(bytes);
  }
  if (level.length === 0) {
    return sha256(new Uint8Array());
  }
  while (level.length > 1) {
    const next: Uint8Array[] = [];
    for (let start = 0; start < level.length; start += arity) {
      const group = level.slice(start, start + arity);
      const combined = new Uint8Array(group.length * 32);
      group.forEach((item, index) => combined.set(item, index * 32));
      const digest = await sha256(combined);
      const bytes = hexToBytes(digest.slice(7));
      if (bytes === null) return null;
      next.push(bytes);
    }
    level = next;
  }
  return `sha256:${bytesToHex(level[0])}`;
}

function parseMetadata(
  archive: Uint8Array,
  header: ParsedHeader,
): RecordValue | null {
  try {
    const raw = archive.subarray(
      header.metadataOffset,
      header.metadataOffset + header.metadataLength,
    );
    const parsed: unknown = JSON.parse(new TextDecoder().decode(raw));
    return isRecord(parsed) ? parsed : null;
  } catch {
    return null;
  }
}

function parsePmidx(value: RecordValue): {
  specHash: string;
  archiveDigest: string;
  merkleRoot: string;
  arity: number;
  chunkBytes: number;
  leaves: readonly string[];
  range: ParsedRange;
} | null {
  if (
    value.schema_version !== "kfm.pmidx.v1" ||
    !isDigest(value.spec_hash) ||
    !isDigest(value.pmtiles_sha256) ||
    !isRecord(value.merkle) ||
    !Array.isArray(value.ranges) ||
    value.ranges.length !== 1
  ) {
    return null;
  }
  const merkle = value.merkle;
  if (
    !Number.isInteger(merkle.arity) ||
    typeof merkle.arity !== "number" ||
    merkle.arity < 2 ||
    merkle.arity > 64 ||
    !isPositiveInteger(merkle.chunk_bytes) ||
    !isDigest(merkle.root) ||
    !Array.isArray(merkle.leaves) ||
    !merkle.leaves.every(isDigest)
  ) {
    return null;
  }
  const range = parseRange(value.ranges[0]);
  if (range === null) return null;
  return {
    specHash: value.spec_hash,
    archiveDigest: value.pmtiles_sha256,
    merkleRoot: merkle.root,
    arity: merkle.arity,
    chunkBytes: merkle.chunk_bytes,
    leaves: Object.freeze([...merkle.leaves]),
    range,
  };
}

function sameRgba(left: readonly number[], right: readonly number[]): boolean {
  return (
    left.length === 4 &&
    right.length === 4 &&
    left.every((value, index) => value === right[index])
  );
}

export async function verifyMobilePmtilesFixture(
  input: unknown,
  renderTile: MobilePmtilesRenderAdapter,
  now: () => number = () => performance.now(),
): Promise<MobilePmtilesVerificationResult> {
  const parsed = parseBundle(input);
  if ("outcome" in parsed) return parsed;

  const verifyStart = now();
  const archiveBytes = parsed.archiveBytes;
  if (archiveBytes.length > parsed.budgets.maxArchiveBytes) {
    return failure("MOBILE_PMTILES_ARCHIVE_BUDGET_EXCEEDED", "DENY", {
      archiveBytes: archiveBytes.length,
    });
  }

  const [
    archiveDigest,
    pmidxDigest,
    pmsigDigest,
    runreceiptDigest,
  ] = await Promise.all([
    sha256(archiveBytes),
    canonicalJsonSha256(parsed.pmidx),
    canonicalJsonSha256(parsed.pmsig),
    canonicalJsonSha256(parsed.runreceipt),
  ]);

  if (
    pmidxDigest !== parsed.sidecarDigests.pmidxSha256 ||
    pmsigDigest !== parsed.sidecarDigests.pmsigSha256 ||
    runreceiptDigest !== parsed.sidecarDigests.runreceiptSha256
  ) {
    return failure("MOBILE_PMTILES_SIDECAR_DIGEST_MISMATCH", "DENY", {
      archiveBytes: archiveBytes.length,
      verifyMs: now() - verifyStart,
    });
  }

  const pmidx = parsePmidx(parsed.pmidx);
  if (pmidx === null) {
    return failure("MOBILE_PMTILES_BUNDLE_INVALID", "DENY", {
      archiveBytes: archiveBytes.length,
      verifyMs: now() - verifyStart,
    });
  }
  if (archiveDigest !== pmidx.archiveDigest) {
    return failure("MOBILE_PMTILES_ARCHIVE_DIGEST_MISMATCH", "DENY", {
      archiveBytes: archiveBytes.length,
      verifyMs: now() - verifyStart,
    });
  }

  const header = parseHeader(archiveBytes);
  if (header === null) {
    return failure("MOBILE_PMTILES_HEADER_INVALID", "DENY", {
      archiveBytes: archiveBytes.length,
      verifyMs: now() - verifyStart,
    });
  }
  const metadata = parseMetadata(archiveBytes, header);
  if (metadata === null || !isDigest(metadata.spec_hash)) {
    return failure("MOBILE_PMTILES_METADATA_INVALID", "DENY", {
      archiveBytes: archiveBytes.length,
      verifyMs: now() - verifyStart,
    });
  }
  if (metadata.spec_hash !== pmidx.specHash) {
    return failure("MOBILE_PMTILES_SPEC_HASH_MISMATCH", "DENY", {
      archiveBytes: archiveBytes.length,
      verifyMs: now() - verifyStart,
    });
  }

  const computedLeaves: string[] = [];
  for (
    let offset = 0;
    offset < archiveBytes.length;
    offset += pmidx.chunkBytes
  ) {
    computedLeaves.push(
      await sha256(archiveBytes.subarray(offset, offset + pmidx.chunkBytes)),
    );
  }
  if (
    computedLeaves.length !== pmidx.leaves.length ||
    computedLeaves.some((value, index) => value !== pmidx.leaves[index])
  ) {
    return failure("MOBILE_PMTILES_ARCHIVE_DIGEST_MISMATCH", "DENY", {
      archiveBytes: archiveBytes.length,
      verifyMs: now() - verifyStart,
    });
  }
  const root = await computeMerkleRoot(computedLeaves, pmidx.arity);
  if (root !== pmidx.merkleRoot) {
    return failure("MOBILE_PMTILES_MERKLE_ROOT_MISMATCH", "DENY", {
      archiveBytes: archiveBytes.length,
      verifyMs: now() - verifyStart,
    });
  }

  const range = pmidx.range;
  const rangeEnd = range.offset + range.length;
  if (
    rangeEnd < range.offset ||
    rangeEnd > archiveBytes.length ||
    range.offset < header.tileDataOffset ||
    rangeEnd > header.tileDataOffset + header.tileDataLength
  ) {
    return failure("MOBILE_PMTILES_RANGE_OUT_OF_BOUNDS", "DENY", {
      archiveBytes: archiveBytes.length,
      tileBytes: range.length,
      verifyMs: now() - verifyStart,
    });
  }
  const firstLeaf = Math.floor(range.offset / pmidx.chunkBytes);
  const lastLeaf = Math.floor((rangeEnd - 1) / pmidx.chunkBytes);
  if (
    firstLeaf !== lastLeaf ||
    range.leaf !== firstLeaf ||
    range.leaf >= pmidx.leaves.length
  ) {
    return failure("MOBILE_PMTILES_RANGE_LEAF_BINDING_INVALID", "DENY", {
      archiveBytes: archiveBytes.length,
      tileBytes: range.length,
      verifyMs: now() - verifyStart,
    });
  }

  const tileBytes = archiveBytes.slice(range.offset, rangeEnd);
  if (tileBytes.length > parsed.budgets.maxTileBytes) {
    return failure("MOBILE_PMTILES_TILE_BUDGET_EXCEEDED", "DENY", {
      archiveBytes: archiveBytes.length,
      tileBytes: tileBytes.length,
      verifyMs: now() - verifyStart,
    });
  }
  if ((await sha256(tileBytes)) !== range.sha256) {
    return failure("MOBILE_PMTILES_TILE_DIGEST_MISMATCH", "DENY", {
      archiveBytes: archiveBytes.length,
      tileBytes: tileBytes.length,
      verifyMs: now() - verifyStart,
    });
  }
  const pngMagic = [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a];
  if (!pngMagic.every((value, index) => tileBytes[index] === value)) {
    return failure("MOBILE_PMTILES_TILE_PAYLOAD_INVALID", "DENY", {
      archiveBytes: archiveBytes.length,
      tileBytes: tileBytes.length,
      verifyMs: now() - verifyStart,
    });
  }

  const pmsig = parsed.pmsig;
  const subject = pmsig.subject;
  if (
    pmsig.schema_version !== "kfm.pmsig.v1" ||
    !isRecord(subject) ||
    subject.pmtiles_sha256 !== archiveDigest ||
    subject.pmidx_merkle_root !== pmidx.merkleRoot ||
    subject.spec_hash !== pmidx.specHash ||
    pmsig.key_id !== "TEST_ONLY_UNAPPROVED_KEY" ||
    pmsig.signature !==
      "DEVELOPMENT_PLACEHOLDER_NOT_A_VALID_COSE_SIGNATURE"
  ) {
    return failure("MOBILE_PMTILES_SIGNATURE_SUBJECT_MISMATCH", "DENY", {
      archiveBytes: archiveBytes.length,
      tileBytes: tileBytes.length,
      verifyMs: now() - verifyStart,
    });
  }

  const receipt = parsed.runreceipt;
  const receiptSubject = receipt.subject;
  const predicate = receipt.predicate;
  const receiptItem =
    Array.isArray(receiptSubject) && receiptSubject.length === 1
      ? receiptSubject[0]
      : null;
  const receiptDigest = isRecord(receiptItem) ? receiptItem.digest : null;
  const buildDefinition = isRecord(predicate)
    ? predicate.buildDefinition
    : null;
  const externalParameters = isRecord(buildDefinition)
    ? buildDefinition.externalParameters
    : null;
  if (
    receipt.schema_version !== "kfm.runreceipt.pmtiles.v1" ||
    !isRecord(receiptItem) ||
    receiptItem.name !== parsed.archiveName ||
    !isRecord(receiptDigest) ||
    receiptDigest.sha256 !== archiveDigest.slice(7) ||
    !isRecord(externalParameters) ||
    externalParameters.spec_hash !== pmidx.specHash
  ) {
    return failure("MOBILE_PMTILES_RUNRECEIPT_SUBJECT_MISMATCH", "DENY", {
      archiveBytes: archiveBytes.length,
      tileBytes: tileBytes.length,
      verifyMs: now() - verifyStart,
    });
  }

  const verifyMs = now() - verifyStart;
  if (verifyMs > parsed.budgets.maxVerifyMs) {
    return failure("MOBILE_PMTILES_VERIFY_BUDGET_EXCEEDED", "DENY", {
      archiveBytes: archiveBytes.length,
      tileBytes: tileBytes.length,
      verifyMs,
    });
  }

  const renderStart = now();
  let probe: MobilePmtilesRenderProbe;
  try {
    probe = await renderTile(tileBytes, "image/png");
  } catch {
    return failure("MOBILE_PMTILES_TILE_DECODE_RENDER_ERROR", "ERROR", {
      archiveBytes: archiveBytes.length,
      tileBytes: tileBytes.length,
      verifyMs,
      decodeRenderMs: now() - renderStart,
    });
  }
  const decodeRenderMs = now() - renderStart;
  if (decodeRenderMs > parsed.budgets.maxDecodeRenderMs) {
    return failure("MOBILE_PMTILES_DECODE_RENDER_BUDGET_EXCEEDED", "DENY", {
      archiveBytes: archiveBytes.length,
      tileBytes: tileBytes.length,
      verifyMs,
      decodeRenderMs,
    });
  }
  if (
    probe.decoded !== true ||
    probe.rendered !== true ||
    probe.width !== 1 ||
    probe.height !== 1 ||
    !sameRgba(probe.pixelRgba, parsed.expectedPixelRgba)
  ) {
    return failure("MOBILE_PMTILES_TILE_RENDER_MISMATCH", "DENY", {
      archiveBytes: archiveBytes.length,
      tileBytes: tileBytes.length,
      verifyMs,
      decodeRenderMs,
    });
  }

  return Object.freeze({
    outcome: "PASS",
    code: "MOBILE_PMTILES_VERIFY_DECODE_RENDER_PASS",
    authority: "NONE",
    holds: parsed.holds,
    maplibreBootState: "HOLD",
    maplibreBootReason: "MAPLIBRE_RUNTIME_UNADMITTED",
    metrics: Object.freeze({
      archiveBytes: archiveBytes.length,
      tileBytes: tileBytes.length,
      verifyMs,
      decodeRenderMs,
    }),
  });
}
