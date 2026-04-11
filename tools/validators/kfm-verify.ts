#!/usr/bin/env node
import { createHash } from "node:crypto";
import { promises as fs } from "node:fs";
import path from "node:path";

type Manifest = {
  release_id: string;
  created?: string;
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
    sha256?: string;
    bytes?: number;
    mediaType?: string;
    role?: string;
  }>;
};

type Outcome = "ANSWER" | "ABSTAIN" | "DENY" | "ERROR";

function normalizeHash(input?: string): string | undefined {
  return input?.toLowerCase().replace(/^sha256:/, "");
}

function stableStringify(value: unknown): string {
  const seen = new WeakSet();

  const sortValue = (v: any): any => {
    if (v === null || typeof v !== "object") return v;
    if (seen.has(v)) throw new Error("Circular structure not supported");
    seen.add(v);

    if (Array.isArray(v)) return v.map(sortValue);

    const out: Record<string, any> = {};
    for (const key of Object.keys(v).sort()) out[key] = sortValue(v[key]);
    return out;
  };

  return JSON.stringify(sortValue(value), null, 2);
}

function sha256Hex(buf: Buffer): string {
  return createHash("sha256").update(buf).digest("hex");
}

async function readJson<T>(p: string): Promise<T> {
  return JSON.parse(await fs.readFile(p, "utf8")) as T;
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

function finish(result: unknown, exitCode = 0): never {
  process.stdout.write(JSON.stringify(result, null, 2) + "\n");
  process.exit(exitCode);
}

async function main(): Promise<void> {
  const args = parseArgs(process.argv);

  if (!args["manifest"]) {
    throw new Error(
      "Usage: kfm-verify --manifest release-manifest.json [--assets-root dist] [--require-bundle true] [--require-proof true]"
    );
  }

  const manifestPath = path.resolve(args["manifest"]);
  const assetsRoot = args["assets-root"] ? path.resolve(args["assets-root"]) : undefined;
  const requireBundle = args["require-bundle"] === "true";
  const requireProof = args["require-proof"] === "true";

  const manifest = await readJson<Manifest>(manifestPath);
  const reasons: string[] = [];
  const obligations: string[] = [];

  const specBasis = JSON.parse(JSON.stringify(manifest)) as Manifest;
  delete specBasis.spec_hash;
  const computedSpecHash = sha256Hex(Buffer.from(stableStringify(specBasis), "utf8"));
  const expectedSpecHash = normalizeHash(manifest.spec_hash);

  if (!expectedSpecHash) {
    finish(
      {
        ok: false,
        outcome: "DENY" as Outcome,
        reasons: ["Manifest missing spec_hash."],
        obligations: ["Provide spec_hash in the release manifest."],
        manifest: manifest.release_id,
      },
      1
    );
  }

  if (computedSpecHash !== expectedSpecHash) {
    finish(
      {
        ok: false,
        outcome: "DENY" as Outcome,
        reasons: ["Manifest spec_hash mismatch."],
        obligations: ["Regenerate manifest from declared assets before release."],
        manifest: manifest.release_id,
        expected_spec_hash: expectedSpecHash,
        actual_spec_hash: computedSpecHash,
      },
      1
    );
  }

  reasons.push("Manifest spec_hash verified.");

  if (requireBundle && !manifest.bundle_ref) {
    finish(
      {
        ok: false,
        outcome: "DENY" as Outcome,
        reasons: ["bundle_ref required but missing."],
        obligations: ["Attach a Sigstore/Cosign verification bundle reference."],
        manifest: manifest.release_id,
      },
      1
    );
  }

  if (requireProof && !manifest.proof_ref) {
    finish(
      {
        ok: false,
        outcome: "DENY" as Outcome,
        reasons: ["proof_ref required but missing."],
        obligations: ["Attach a KFM proof pack reference."],
        manifest: manifest.release_id,
      },
      1
    );
  }

  const assetResults: Array<Record<string, unknown>> = [];

  if (assetsRoot) {
    for (const asset of manifest.assets) {
      const expected = normalizeHash(asset.sha256);
      if (!expected) {
        finish(
          {
            ok: false,
            outcome: "DENY" as Outcome,
            reasons: [`Asset "${asset.id}" missing sha256.`],
            obligations: ["Declare sha256 for every release asset."],
            manifest: manifest.release_id,
          },
          1
        );
      }

      // Map uri to local path conservatively.
      const rel = asset.uri.replace(/^[a-z]+:\/\//i, "").replace(/^\/+/, "");
      const filePath = path.join(assetsRoot, rel);

      let hashed;
      try {
        hashed = await hashFile(filePath);
      } catch {
        finish(
          {
            ok: false,
            outcome: "DENY" as Outcome,
            reasons: [`Declared asset not found under assets-root: ${asset.uri}`],
            obligations: ["Ensure release asset paths match manifest uris."],
            manifest: manifest.release_id,
            asset_id: asset.id,
            checked_path: filePath,
          },
          1
        );
      }

      const ok = hashed.sha256 === expected;
      assetResults.push({
        id: asset.id,
        uri: asset.uri,
        ok,
        expected_sha256: expected,
        actual_sha256: hashed.sha256,
        expected_bytes: asset.bytes,
        actual_bytes: hashed.bytes,
      });

      if (!ok) {
        finish(
          {
            ok: false,
            outcome: "DENY" as Outcome,
            reasons: [`Asset "${asset.id}" sha256 mismatch.`],
            obligations: ["Rebuild or republish the release asset and regenerate the manifest."],
            manifest: manifest.release_id,
            asset_id: asset.id,
            expected_sha256: expected,
            actual_sha256: hashed.sha256,
          },
          1
        );
      }

      if (typeof asset.bytes === "number" && asset.bytes !== hashed.bytes) {
        finish(
          {
            ok: false,
            outcome: "DENY" as Outcome,
            reasons: [`Asset "${asset.id}" byte length mismatch.`],
            obligations: ["Regenerate manifest after finalizing release bytes."],
            manifest: manifest.release_id,
            asset_id: asset.id,
            expected_bytes: asset.bytes,
            actual_bytes: hashed.bytes,
          },
          1
        );
      }
    }

    reasons.push("Declared assets verified against local release bytes.");
  } else {
    obligations.push("Asset bytes were not checked because --assets-root was not provided.");
  }

  finish({
    ok: true,
    outcome: "ANSWER" as Outcome,
    reasons,
    obligations,
    manifest: manifest.release_id,
    spec_hash: manifest.spec_hash,
    bundle_ref: manifest.bundle_ref,
    proof_ref: manifest.proof_ref,
    assets_checked: assetResults.length,
    asset_results: assetResults,
    checked_at: new Date().toISOString(),
  });
}

main().catch((err) => {
  finish(
    {
      ok: false,
      outcome: "ERROR" as Outcome,
      reasons: [err instanceof Error ? err.message : String(err)],
      checked_at: new Date().toISOString(),
    },
    1
  );
});
