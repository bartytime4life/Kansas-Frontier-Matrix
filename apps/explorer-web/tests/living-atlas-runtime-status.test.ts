import { describe, expect, it } from "vitest";
import {
  resolveHeldInteractionStatus,
  resolveLivingAtlasRuntimeStatusMutation,
} from "../src/site/living-atlas-runtime-status";

describe("Living Atlas runtime status precedence", () => {
  it("projects held interaction reasons from the authoritative tool catalog", () => {
    expect(resolveHeldInteractionStatus("interaction:measure")).toBe(
      "Measure HELD · Measurement, projection, units, uncertainty, and export contracts are not bound.",
    );
  });

  it("does not manufacture held status for available or unknown actions", () => {
    expect(resolveHeldInteractionStatus("interaction:select")).toBeNull();
    expect(resolveHeldInteractionStatus("interaction:unknown")).toBeNull();
    expect(resolveHeldInteractionStatus(undefined)).toBeNull();
  });

  it("restores held explanations after late renderer readiness chatter", () => {
    expect(
      resolveLivingAtlasRuntimeStatusMutation(
        "Renderer READY",
        "Measure HELD · reason",
      ),
    ).toBe("RESTORE");
  });

  it("releases held precedence for runtime errors and newer user outcomes", () => {
    expect(
      resolveLivingAtlasRuntimeStatusMutation(
        "Renderer ERROR · WebGL context unavailable",
        "Measure HELD · reason",
      ),
    ).toBe("RELEASE");
    expect(
      resolveLivingAtlasRuntimeStatusMutation(
        "Select ready · choose a bounded layer",
        "Measure HELD · reason",
      ),
    ).toBe("RELEASE");
  });
});
