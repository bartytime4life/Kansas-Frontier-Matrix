import { describe, expect, test } from "vitest";
import valid from "../../../../tests/fixtures/maps/trust/valid/signed_manifest.valid.json";
import missingBundle from "../../../../tests/fixtures/maps/trust/invalid/missing_bundle.json";
import { verifyManifest } from "../sigstoreVerify.worker";

describe("sigstore worker mapping", () => {
  test("valid => ALLOW_RENDER", () => {
    const out = verifyManifest({ manifest: valid, expectedArtifactDigest: valid.artifacts[0].digest });
    expect(out.decision).toBe("ALLOW_RENDER");
  });
  test("missing bundle => DENY_RENDER", () => {
    const out = verifyManifest({ manifest: missingBundle, expectedArtifactDigest: missingBundle.artifacts[0].digest });
    expect(out.decision).toBe("DENY_RENDER");
    expect(out.reason_codes).toContain("MISSING_BUNDLE");
  });
});
