import { describe, expect, it } from "vitest";
import { MAP_RUNTIME_PORT_PROFILE } from "@kfm/maplibre";
import { formatRendererDiagnostic } from "../src/features/diagnostics";

describe("public renderer diagnostics", () => {
  const snapshot = (state: unknown, reason: unknown) => ({
    profile: MAP_RUNTIME_PORT_PROFILE,
    state,
    reason,
  });

  it("shows only the finite runtime state and reason code", () => {
    expect(formatRendererDiagnostic(snapshot("READY", null))).toBe("Renderer READY");
    expect(formatRendererDiagnostic(snapshot("ERROR", "MAP_RUNTIME_INITIALIZATION_FAILED")))
      .toBe("Renderer ERROR · MAP_RUNTIME_INITIALIZATION_FAILED");
  });

  it("does not show arbitrary renderer error text or a forged ready state", () => {
    const secret = "https://private.example/?token=secret";
    for (const candidate of [
      snapshot("ERROR", secret), snapshot(secret, null),
      { ...snapshot("READY", null), profile: "unknown" },
      snapshot("READY", undefined),
      snapshot("READY", "MAP_RUNTIME_ERROR"),
    ]) {
      const rendered = formatRendererDiagnostic(candidate);
      expect(rendered).toBe("Renderer ERROR · MAP_RUNTIME_STATE_INVALID");
      expect(rendered).not.toContain(secret);
    }
  });

  it("fails closed on throwing accessors without echoing their exception", () => {
    const candidate = { profile: MAP_RUNTIME_PORT_PROFILE,
      get state(): never { throw new Error("private stack and token"); }, reason: null };
    expect(formatRendererDiagnostic(candidate)).toBe("Renderer ERROR · MAP_RUNTIME_STATE_INVALID");
  });
});
