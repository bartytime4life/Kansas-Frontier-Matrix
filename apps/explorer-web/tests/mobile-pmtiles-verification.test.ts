import { describe, expect, it, vi } from "vitest";

import fixtureSuite from "../../../fixtures/pmtiles/mobile_verification/cases.json";
import moduleSource from "../src/features/map_runtime/mobile_pmtiles_verification.ts?raw";
import {
  canonicalJsonSha256,
  decodeMobilePmtilesArchive,
  verifyMobilePmtilesFixture,
  type MobilePmtilesRenderAdapter,
} from "../src/features/map_runtime/mobile_pmtiles_verification";

type FixtureBundle = typeof fixtureSuite.base;

function clone<T>(value: T): T {
  return JSON.parse(JSON.stringify(value)) as T;
}

function encodeBase64(bytes: Uint8Array): string {
  let binary = "";
  for (const value of bytes) binary += String.fromCharCode(value);
  return btoa(binary);
}

async function mutateFixture(
  base: FixtureBundle,
  mutation: string,
): Promise<FixtureBundle> {
  const bundle = clone(base);
  if (mutation === "NONE") return bundle;

  if (mutation === "ARCHIVE_BYTE_FLIP") {
    const archive = decodeMobilePmtilesArchive(bundle.archive_base64);
    if (archive === null) throw new Error("fixture archive is invalid");
    archive[archive.length - 1] ^= 0x01;
    bundle.archive_base64 = encodeBase64(archive);
    return bundle;
  }

  if (mutation === "PMIDX_ROOT_MISMATCH") {
    bundle.pmidx.merkle.root =
      "sha256:34df63b0b7ef7f8ad3ea78bcba59f78aa6f9f5cbde52b223f2f7cddb6f823e46";
    bundle.sidecar_digests.pmidx_sha256 =
      await canonicalJsonSha256(bundle.pmidx);
    return bundle;
  }

  if (mutation === "PMSIG_SUBJECT_MISMATCH") {
    bundle.pmsig.subject.pmtiles_sha256 =
      "sha256:e863a58944db349c2f3e69e815d953b0af0ef76dc9258b485bbabacfd40ce4a3";
    bundle.sidecar_digests.pmsig_sha256 =
      await canonicalJsonSha256(bundle.pmsig);
    return bundle;
  }

  if (mutation === "RANGE_OUT_OF_BOUNDS") {
    const archive = decodeMobilePmtilesArchive(bundle.archive_base64);
    if (archive === null) throw new Error("fixture archive is invalid");
    bundle.pmidx.ranges[0].offset = archive.length;
    bundle.sidecar_digests.pmidx_sha256 =
      await canonicalJsonSha256(bundle.pmidx);
    return bundle;
  }

  if (mutation === "TILE_DIGEST_MISMATCH") {
    bundle.pmidx.ranges[0].sha256 =
      "sha256:bc62c4df74b2c2f0ce4f0fb95c5eb1b0b835a33fc4ea63d4aa62d5744069734b";
    bundle.sidecar_digests.pmidx_sha256 =
      await canonicalJsonSha256(bundle.pmidx);
    return bundle;
  }

  if (mutation === "MAPLIBRE_READY_OVERCLAIM") {
    bundle.maplibre_boot_state = "READY" as never;
    bundle.maplibre_boot_reason = "UNSUPPORTED_CLAIM" as never;
    return bundle;
  }

  if (mutation === "RELEASE_AUTHORITY_OVERCLAIM") {
    bundle.authority.release = true;
    return bundle;
  }

  throw new Error(`unknown mutation: ${mutation}`);
}

function clock(): () => number {
  let value = 0;
  return () => {
    value += 1;
    return value;
  };
}

const passingRenderer: MobilePmtilesRenderAdapter = async (tileBytes, mediaType) => {
  expect(mediaType).toBe("image/png");
  expect(Array.from(tileBytes.slice(0, 8))).toEqual([
    0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a,
  ]);
  return {
    decoded: true,
    rendered: true,
    width: 1,
    height: 1,
    pixelRgba: [17, 34, 51, 255],
  };
};

describe("mobile PMTiles verification fixture", () => {
  it("replays every declared case with exact finite outcomes", async () => {
    expect(fixtureSuite.profile).toBe(
      "kfm.pmtiles.mobile-verification-fixtures.v1",
    );
    expect(fixtureSuite.source_idea).toBe("ML-Y-111");

    for (const declared of fixtureSuite.cases) {
      const bundle = await mutateFixture(fixtureSuite.base, declared.mutation);
      const renderer = vi.fn(passingRenderer);
      const result = await verifyMobilePmtilesFixture(bundle, renderer, clock());

      expect(
        { outcome: result.outcome, code: result.code },
        declared.case_id,
      ).toEqual({
        outcome: declared.expected_outcome,
        code: declared.expected_code,
      });
      if (declared.mutation === "NONE") {
        expect(renderer).toHaveBeenCalledTimes(1);
      } else {
        expect(renderer).not.toHaveBeenCalled();
      }
    }
  });

  it("retains crypto, MapLibre-runtime, and release holds on PASS", async () => {
    const result = await verifyMobilePmtilesFixture(
      clone(fixtureSuite.base),
      passingRenderer,
      clock(),
    );

    expect(result).toMatchObject({
      outcome: "PASS",
      code: "MOBILE_PMTILES_VERIFY_DECODE_RENDER_PASS",
      authority: "NONE",
      maplibreBootState: "HOLD",
      maplibreBootReason: "MAPLIBRE_RUNTIME_UNADMITTED",
      metrics: {
        archiveBytes: 347,
        tileBytes: 70,
      },
    });
    expect(new Set(result.holds)).toEqual(
      new Set([
        "CRYPTOGRAPHIC_VERIFICATION_UNWIRED",
        "MAPLIBRE_RUNTIME_UNADMITTED",
        "RELEASE_AUTHORIZATION_NOT_EVALUATED",
      ]),
    );
  });

  it("returns ERROR when the injected decode/render adapter fails", async () => {
    const result = await verifyMobilePmtilesFixture(
      clone(fixtureSuite.base),
      async () => {
        throw new Error("synthetic decode failure");
      },
      clock(),
    );

    expect(result).toMatchObject({
      outcome: "ERROR",
      code: "MOBILE_PMTILES_TILE_DECODE_RENDER_ERROR",
      authority: "NONE",
      maplibreBootState: "HOLD",
    });
  });

  it("contains no transport, MapLibre import, or authority shortcut", () => {
    for (const forbidden of [
      "fetch(",
      "XMLHttpRequest",
      "WebSocket",
      'from "maplibre',
      "import(\"maplibre",
      "source_admission: true",
      "release: true",
      "publication: true",
    ]) {
      expect(moduleSource).not.toContain(forbidden);
    }
    expect(moduleSource).toContain("MAPLIBRE_RUNTIME_UNADMITTED");
    expect(moduleSource).toContain('authority: "NONE"');
  });
});
