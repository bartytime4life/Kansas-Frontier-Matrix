import { describe, expect, it } from "vitest";
import {
  createLivingAtlasStatusController,
  resolveHeldInteractionStatus,
  resolveLivingAtlasRuntimeStatusMutation,
} from "../src/site/living-atlas-runtime-status";

describe("Living Atlas command and runtime status ownership", () => {
  it("retains temporal abstention across initialization completion and camera readiness updates", () => {
    const rendered: string[] = [];
    const status = createLivingAtlasStatusController((message) => rendered.push(message));
    const abstain = "ABSTAIN · Layer is outside the committed time bucket";
    status.showRuntime("Renderer INITIALIZING");
    status.showAction(abstain);
    status.showRuntime("Renderer READY", true);
    status.showRuntime("Renderer READY", true);
    expect(rendered).toEqual(["Renderer INITIALIZING", abstain, abstain, abstain]);
  });

  it.each(["ERROR", "DENIED", "ABSTAINED", "DEGRADED", "WITHDRAWN", "DISPOSED"])(
    "lets runtime %s replace a command and does not resurrect it on recovery",
    (outcome) => {
      const rendered: string[] = [];
      const status = createLivingAtlasStatusController((message) => rendered.push(message));
      status.showAction("ABSTAIN · Layer is outside the committed time bucket");
      status.showRuntime(`Renderer ${outcome}`);
      status.showRuntime("Renderer READY", true);
      expect(rendered.slice(-2)).toEqual([`Renderer ${outcome}`, "Renderer READY"]);
    },
  );

  it("clears prior action guidance for the next command and preserves the latest runtime status", () => {
    const rendered: string[] = [];
    const status = createLivingAtlasStatusController((message) => rendered.push(message));
    status.showRuntime("Renderer READY", true);
    status.showAction("Measure HELD · reason");
    status.showAction(null);
    expect(rendered.at(-1)).toBe("Renderer READY");
    status.showAction("ABSTAIN · Layer is outside the committed time bucket");
    status.showRuntime("Map runtime initializing…");
    status.showRuntime("Renderer READY", true);
    expect(rendered.slice(-2)).toEqual(["Map runtime initializing…", "Renderer READY"]);
  });
});

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
