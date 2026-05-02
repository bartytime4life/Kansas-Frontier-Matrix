import { describe, expect, test, vi } from "vitest";
import { guardedRegisterLayer } from "../verifyBeforeRender";
import bad from "../../../../tests/fixtures/maps/trust/invalid/hash_mismatch.json";

describe("no-bypass render gate", () => {
  test("blocks registration before render on verification failure", async () => {
    const register = vi.fn();
    const setStatus = vi.fn();
    const setEvidenceReceiptRef = vi.fn();
    const out = await guardedRegisterLayer({ manifest: bad, expectedArtifactDigest: "sha256:1111111111111111111111111111111111111111111111111111111111111111", register, setStatus, setEvidenceReceiptRef });
    expect(out.decision).not.toBe("ALLOW_RENDER");
    expect(register).not.toHaveBeenCalled();
  });
});
