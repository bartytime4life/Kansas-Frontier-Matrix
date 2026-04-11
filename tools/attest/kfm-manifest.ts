#!/usr/bin/env node
import { createHash } from "node:crypto";
import { promises as fs } from "node:fs";
import path from "node:path";

type AssetInput = {
  id: string;
  uri: string;
  path: string;
  mediaType?: string;
  role?: string;
};

type Manifest = {
  release_id: string;
  created: string;
  spec_hash?: string;
  bundle_ref?: string;
  proof_ref?: string;
  publisher?: {
    identity?: string;
    issuer?: string;
  };
  assets: Array<{
    id: string;
    uri: string;
    sha256: string;
    bytes: number;
    mediaType?: string;
    role?: string;
  }>;
};

function stableStringify(value: unknown): string {
  const seen = new WeakSet();

  const sortValue = (v: any): any => {
    if (v === null || typeof v !== "object") return v;
    if (seen.has(v)) throw new Error("Circular structure not supported");
    seen.add(v);

    if (Array.isArray(v)) return v.map(sortValue);

    const out: Record<string, any> = {};
    for (const key of Object.keys(v).sort()) {
      out[key] = sortValue(v[key]);
    }
    return out;
  };

  return JSON.stringify(sortValue(value), null, 2);
}

function sha256Hex(buf: Buffer): string {
  return createHash("sha256").update(buf).digest("hex");
}

async function readJsonFile<T>(p: string): Promise<T> {
  const raw = await fs.readFile(p, "utf8");
  return JSON.parse(raw) as T;
}

async function hashFile(p: string): Promise<{ sha256: string; bytes: number }> {
  const buf = await fs.readFile(p);
  return { sha256: sha256Hex(buf), bytes: buf.byteLength };
}

function parseArgs(argv: string[]): Record<string, string> {
  const out: Record<string, string> = {};
  for (let i = 2; i < argv.length; i++) {
    const arg = argv[i];
    if (!arg.startsWith("--")) continue;
    const key = arg.slice(2);
    const value = argv[i + 1] && !argv[i + 1].startsWith("--") ? argv[++i] : "true";
    out[key] = value;
  }
  return out;
}

async function main(): Promise<void> {
  const args = parseArgs(process.argv);

  if (!args["config"] || !args["out"]) {
    throw new Error(
      "Usage: kfm-manifest --config manifest-input.json --out release-manifest.json [--release-id id] [--bundle-ref ref] [--proof-ref ref] [--publisher-identity id] [--publisher-issuer issuer]"
    );
  }

  const configPath = path.resolve(args["config"]);
  const outPath = path.resolve(args["out"]);

  const input = await readJsonFile<{
    release_id?: string;
    bundle_ref?: string;
    proof_ref?: string;
    publisher?: { identity?: string; issuer?: string };
    assets: AssetInput[];
  }>(configPath);

  if (!Array.isArray(input.assets) || input.assets.length === 0) {
    throw new Error("Config must include a non-empty assets array.");
  }

  const assets = [];
  for (const asset of input.assets) {
    const resolvedPath = path.resolve(asset.path);
    const { sha256, bytes } = await hashFile(resolvedPath);
    assets.push({
      id: asset.id,
      uri: asset.uri,
      sha256,
      bytes,
      mediaType: asset.mediaType,
      role: asset.role,
    });
  }

  const manifest: Manifest = {
    release_id: args["release-id"] || input.release_id || `kfm-release-${Date.now()}`,
    created: new Date().toISOString(),
    bundle_ref: args["bundle-ref"] || input.bundle_ref,
    proof_ref: args["proof-ref"] || input.proof_ref,
    publisher: {
      identity: args["publisher-identity"] || input.publisher?.identity,
      issuer: args["publisher-issuer"] || input.publisher?.issuer,
    },
    assets,
  };

  const specBasis = JSON.parse(JSON.stringify(manifest)) as Manifest;
  delete specBasis.spec_hash;

  const specHash = sha256Hex(Buffer.from(stableStringify(specBasis), "utf8"));
  manifest.spec_hash = `sha256:${specHash}`;

  await fs.mkdir(path.dirname(outPath), { recursive: true });
  await fs.writeFile(outPath, `${stableStringify(manifest)}\n`, "utf8");

  process.stdout.write(
    JSON.stringify(
      {
        ok: true,
        out: outPath,
        release_id: manifest.release_id,
        spec_hash: manifest.spec_hash,
        asset_count: manifest.assets.length,
      },
      null,
      2
    ) + "\n"
  );
}

main().catch((err) => {
  process.stderr.write(
    JSON.stringify(
      {
        ok: false,
        outcome: "ERROR",
        error: err instanceof Error ? err.message : String(err),
      },
      null,
      2
    ) + "\n"
  );
  process.exit(1);
});
