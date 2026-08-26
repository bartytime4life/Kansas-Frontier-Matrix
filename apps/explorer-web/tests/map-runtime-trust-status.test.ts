import { describe, expect, it } from "vitest";

import {
  MAP_RUNTIME_TRUST_STATES,
  MAP_RUNTIME_TRUST_STATE_REASONS,
  createNullMapRuntime,
} from "@kfm/maplibre";
import presenterSource from "../src/features/map_runtime/runtime-trust-status.ts?raw";
import { resolveMapRuntimeTrustStatus } from "../src/features/map_runtime/runtime-trust-status";

describe("MapRuntimePort trust-status presenter", () => {
  it("projects every finite trust transition without making it selection-eligible", async () => {
    const runtime = createNullMapRuntime();
    await runtime.initialize();

    expect(resolveMapRuntimeTrustStatus(runtime.getSnapshot())).toMatchObject({
      valid: true,
      state: "READY",
      reason: null,
      canResolveSelection: true,
      role: "status",
    });

    for (const runtimeState of MAP_RUNTIME_TRUST_STATES) {
      const status = resolveMapRuntimeTrustStatus(
        runtime.emitTrustState(runtimeState),
      );
      expect(status, runtimeState).toMatchObject({
        valid: true,
        state: runtimeState,
        reason: MAP_RUNTIME_TRUST_STATE_REASONS[runtimeState],
        canResolveSelection: false,
      });
      expect(status.title).toContain("Map runtime");
      expect(status.accessibilityLabel).toContain(
        runtimeState.toLocaleLowerCase(),
      );
    }
  });

  it("keeps critical states assertive and non-critical states polite", async () => {
    const runtime = createNullMapRuntime();
    await runtime.initialize();

    for (const runtimeState of ["DENIED", "WITHDRAWN", "ERROR"] as const) {
      expect(
        resolveMapRuntimeTrustStatus(runtime.emitTrustState(runtimeState)),
      ).toMatchObject({ role: "alert", ariaLive: "assertive" });
    }

    for (const runtimeState of [
      "STALE",
      "ABSTAINED",
      "CONFLICT",
      "DEGRADED",
      "ROLLED_BACK",
    ] as const) {
      expect(
        resolveMapRuntimeTrustStatus(runtime.emitTrustState(runtimeState)),
      ).toMatchObject({ role: "status", ariaLive: "polite" });
    }
  });

  it("fails closed on malformed, widened, or inconsistent snapshots", async () => {
    const runtime = createNullMapRuntime();
    await runtime.initialize();
    const snapshot = runtime.getSnapshot();
    const canary = "PRIVATE_RUNTIME_DIAGNOSTIC_CANARY_3bc6f0";

    for (const invalid of [
      undefined,
      { ...snapshot, reason: "MAP_RUNTIME_ERROR" },
      { ...snapshot, prompt: canary },
      { ...snapshot, state: "STALE", selection: snapshot.selection },
    ]) {
      const status = resolveMapRuntimeTrustStatus(invalid);
      expect(status).toMatchObject({
        valid: false,
        state: "ERROR",
        reason: "MAP_RUNTIME_STATE_INVALID",
        canResolveSelection: false,
      });
      expect(JSON.stringify(status)).not.toContain(canary);
    }
  });

  it("projects disposal without retaining selection authority", async () => {
    const runtime = createNullMapRuntime();
    await runtime.initialize();
    runtime.dispose();

    expect(resolveMapRuntimeTrustStatus(runtime.getSnapshot())).toMatchObject({
      valid: true,
      state: "DISPOSED",
      reason: "MAP_RUNTIME_DISPOSED",
      canResolveSelection: false,
      role: "status",
    });
  });

  it("contains no transport, lifecycle-store, renderer, policy, or model authority", () => {
    expect(presenterSource).not.toMatch(/\bfetch\s*\(/);
    expect(presenterSource).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
    expect(presenterSource).not.toMatch(
      /(?:from\s+|import\s*\()\s*["'](?:maplibre-gl|@maplibre\/[^"']+)["']/i,
    );
    expect(presenterSource).not.toMatch(/(?:ollama|model[-_ ]?runtime)/i);
    expect(presenterSource).not.toMatch(/(?:approve|promote|publish)\s*\(/i);
  });
});
