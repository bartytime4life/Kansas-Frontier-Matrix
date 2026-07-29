import { describe, expect, it } from "vitest";

import { resolveBaselineShell } from "../src/features/shell";

describe("Explorer Web fail-closed baseline shell", () => {
  it("abstains with no evidence when no input is supplied", () => {
    expect(resolveBaselineShell()).toEqual({
      outcome: "ABSTAIN",
      code: "NO_GOVERNED_RESPONSE",
      message: "No governed response is available.",
      evidenceRefs: [],
    });
  });

  it("returns a fixed error and never reflects supplied input", () => {
    const untrustedCanary = "UNTRUSTED_INPUT_CANARY_7c4d1a";
    const result = resolveBaselineShell({ value: untrustedCanary });

    expect(result).toEqual({
      outcome: "ERROR",
      code: "UNSUPPORTED_BASELINE_INPUT",
      message: "This baseline does not accept input.",
      evidenceRefs: [],
    });
    expect(JSON.stringify(result)).not.toContain(untrustedCanary);
  });

  it("treats an explicitly supplied undefined value as input", () => {
    expect(resolveBaselineShell(undefined)).toMatchObject({
      outcome: "ERROR",
      code: "UNSUPPORTED_BASELINE_INPUT",
      evidenceRefs: [],
    });
  });
});
