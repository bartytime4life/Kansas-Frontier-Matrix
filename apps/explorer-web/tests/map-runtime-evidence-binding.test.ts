import { describe, expect, it, vi } from "vitest";

import answerFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/answer-corrected.json";
import layerAdmissionFixture from "../../../fixtures/runtime/layer_manifest_admission/cases.json";
import {
  MAP_FEATURE_SELECTION_PROFILE,
  createNullMapRuntime,
  type MapFeatureSelection,
} from "@kfm/maplibre";
import bindingSource from "../src/features/map_runtime/runtime-evidence-binding.ts?raw";
import {
  bindMapRuntimeEvidence,
  resolveMapRuntimeSelectionEvidence,
} from "../src/features/map_runtime/runtime-evidence-binding";

const selection: MapFeatureSelection = Object.freeze({
  profile: MAP_FEATURE_SELECTION_PROFILE,
  selectionId: "selection:synthetic:flow-001",
  layerId: "layer:released:synthetic-streamflow",
  featureId: "feature:synthetic:flow-001",
  evidenceRefs: Object.freeze(["kfm:evidence:synthetic:flow-001"]),
  historyEvidenceRefs: Object.freeze([
    "kfm:evidence:synthetic:flow-000",
  ]),
});

function admittedLayerManifest(): typeof layerAdmissionFixture.base {
  const value = structuredClone(layerAdmissionFixture.base);
  value.layer_id = selection.layerId;
  value.runtime_request.layer_id = selection.layerId;
  return value;
}

async function settle(): Promise<void> {
  await Promise.resolve();
  await Promise.resolve();
}

describe("MapRuntimePort to governed Evidence Drawer binding", () => {
  it("translates an internal runtime selection through the existing strict bridge", async () => {
    const resolver = vi.fn(async () => answerFixture);
    const result = await resolveMapRuntimeSelectionEvidence(
      selection,
      admittedLayerManifest(),
      resolver,
    );

    expect(resolver).toHaveBeenCalledTimes(1);
    expect(result).toMatchObject({
      layerAdmission: {
        outcome: "PASS",
        code: "LAYER_MANIFEST_REGISTER_ELIGIBLE",
      },
      evidence: {
        selection,
        code: "SUPPORTED",
        drawer: {
          outcome: "ANSWER",
          code: "SUPPORTED",
          evidenceRefs: ["kfm:evidence:synthetic:flow-001"],
        },
      },
    });
  });

  it.each([
    ["HOLD", "LEGACY", "ABSTAIN", "MISSING_EVIDENCE"],
    ["DENY", "POLICY", "DENY", "POLICY_DENIED"],
    ["ERROR", "INVALID", "ERROR", "UPSTREAM_ERROR"],
  ])(
    "returns a visible %s state before governed resolution",
    async (expectedAdmission, mutation, expectedDrawer, expectedCode) => {
      const manifest: unknown =
        mutation === "INVALID"
          ? { invalid: true }
          : (() => {
              const value = admittedLayerManifest();
              if (mutation === "LEGACY") value.manifest_profile = "LEGACY";
              if (mutation === "POLICY") {
                value.release_binding.policy_allowed = false;
              }
              return value;
            })();
      const resolver = vi.fn(async () => answerFixture);

      const result = await resolveMapRuntimeSelectionEvidence(
        selection,
        manifest,
        resolver,
      );

      expect(resolver).not.toHaveBeenCalled();
      expect(result).toMatchObject({
        layerAdmission: { outcome: expectedAdmission },
        evidence: {
          drawer: { outcome: expectedDrawer, code: expectedCode },
        },
      });
    },
  );

  it("denies reuse of an admitted projection for a different selected layer", async () => {
    const resolver = vi.fn(async () => answerFixture);
    const result = await resolveMapRuntimeSelectionEvidence(
      { ...selection, layerId: "layer:released:other" },
      admittedLayerManifest(),
      resolver,
    );

    expect(resolver).not.toHaveBeenCalled();
    expect(result).toMatchObject({
      layerAdmission: {
        outcome: "DENY",
        code: "LAYER_MANIFEST_SELECTION_LAYER_MISMATCH",
      },
      evidence: { drawer: { outcome: "ERROR", code: "UPSTREAM_ERROR" } },
    });
  });

  it("fails closed before transport for an invalid or evidence-free runtime selection", async () => {
    const resolver = vi.fn(async () => answerFixture);

    const invalid = await resolveMapRuntimeSelectionEvidence(
      { ...selection, evidenceRefs: ["duplicate", "duplicate"] },
      admittedLayerManifest(),
      resolver,
    );
    const missing = await resolveMapRuntimeSelectionEvidence(
      { ...selection, evidenceRefs: [], historyEvidenceRefs: [] },
      admittedLayerManifest(),
      resolver,
    );

    expect(resolver).not.toHaveBeenCalled();
    expect(invalid).toMatchObject({
      layerAdmission: null,
      evidence: {
        code: "SELECTION_INVALID",
        drawer: { outcome: "ERROR", code: "UPSTREAM_ERROR" },
      },
    });
    expect(missing).toMatchObject({
      layerAdmission: { outcome: "PASS" },
      evidence: {
        code: "MISSING_EVIDENCE",
        drawer: { outcome: "ABSTAIN", code: "MISSING_EVIDENCE" },
      },
    });
  });

  it("delivers a NullMapRuntime selection through the governed resolver", async () => {
    const runtime = createNullMapRuntime();
    await runtime.initialize();
    const consume = vi.fn();
    const binding = bindMapRuntimeEvidence(
      runtime,
      admittedLayerManifest,
      async () => answerFixture,
      consume,
    );

    runtime.emitSelection(selection);

    await vi.waitFor(() => expect(consume).toHaveBeenCalledTimes(1));
    expect(consume.mock.calls[0]?.[0]).toMatchObject({
      kind: "EVIDENCE_RESOLVED",
      resolution: {
        layerAdmission: { outcome: "PASS" },
        evidence: {
          selection,
          code: "SUPPORTED",
          drawer: { outcome: "ANSWER" },
        },
      },
    });

    binding.destroy();
  });

  it("suppresses stale async results and stops all delivery after idempotent teardown", async () => {
    const runtime = createNullMapRuntime();
    await runtime.initialize();
    const consume = vi.fn();
    let releaseSlow: ((value: unknown) => void) | undefined;
    const slow = new Promise<unknown>((resolve) => {
      releaseSlow = resolve;
    });
    const resolver = vi.fn((current: MapFeatureSelection) =>
      current.selectionId === "selection:slow"
        ? slow
        : Promise.resolve(answerFixture),
    );
    const binding = bindMapRuntimeEvidence(
      runtime,
      admittedLayerManifest,
      resolver,
      consume,
    );

    runtime.emitSelection({ ...selection, selectionId: "selection:slow" });
    runtime.emitSelection({ ...selection, selectionId: "selection:newest" });

    await vi.waitFor(() => expect(consume).toHaveBeenCalledTimes(1));
    expect(consume.mock.calls[0]?.[0]).toMatchObject({
      kind: "EVIDENCE_RESOLVED",
      resolution: {
        evidence: { selection: { selectionId: "selection:newest" } },
      },
    });

    releaseSlow?.(answerFixture);
    await settle();
    expect(consume).toHaveBeenCalledTimes(1);

    binding.destroy();
    binding.destroy();
    runtime.emitSelection({ ...selection, selectionId: "selection:after-destroy" });
    await settle();
    expect(consume).toHaveBeenCalledTimes(1);
  });

  it("invalidates pending evidence when the runtime leaves READY", async () => {
    const runtime = createNullMapRuntime();
    await runtime.initialize();
    const consume = vi.fn();
    let releasePending: ((value: unknown) => void) | undefined;
    const pending = new Promise<unknown>((resolve) => {
      releasePending = resolve;
    });
    const resolver = vi.fn(() => pending);
    const binding = bindMapRuntimeEvidence(
      runtime,
      admittedLayerManifest,
      resolver,
      consume,
    );

    runtime.emitSelection(selection);
    runtime.emitTrustState("WITHDRAWN");
    releasePending?.(answerFixture);
    await settle();

    expect(resolver).toHaveBeenCalledTimes(1);
    expect(consume).toHaveBeenCalledTimes(1);
    expect(consume.mock.calls[0]?.[0]).toEqual({
      kind: "RUNTIME_INVALIDATED",
      selectionId: selection.selectionId,
      runtimeState: "WITHDRAWN",
      runtimeReason: "MAP_RUNTIME_WITHDRAWN",
    });
    expect(runtime.getSnapshot()).toMatchObject({
      state: "WITHDRAWN",
      reason: "MAP_RUNTIME_WITHDRAWN",
      selection: null,
    });

    binding.destroy();
  });

  it.each([
    ["STALE", "MAP_RUNTIME_STALE"],
    ["ABSTAINED", "MAP_RUNTIME_ABSTAINED"],
    ["DENIED", "MAP_RUNTIME_DENIED"],
    ["CONFLICT", "MAP_RUNTIME_CONFLICT"],
    ["DEGRADED", "MAP_RUNTIME_DEGRADED"],
    ["WITHDRAWN", "MAP_RUNTIME_WITHDRAWN"],
    ["ROLLED_BACK", "MAP_RUNTIME_ROLLED_BACK"],
    ["ERROR", "MAP_RUNTIME_ERROR"],
  ] as const)(
    "retracts delivered evidence without synthesizing a Drawer result for %s",
    async (runtimeState, runtimeReason) => {
      const runtime = createNullMapRuntime();
      await runtime.initialize();
      const consume = vi.fn();
      const binding = bindMapRuntimeEvidence(
        runtime,
        admittedLayerManifest,
        async () => answerFixture,
        consume,
      );

      runtime.emitSelection(selection);
      await vi.waitFor(() => expect(consume).toHaveBeenCalledTimes(1));
      runtime.emitTrustState(runtimeState);

      expect(consume).toHaveBeenCalledTimes(2);
      expect(consume.mock.calls[1]?.[0]).toEqual({
        kind: "RUNTIME_INVALIDATED",
        selectionId: selection.selectionId,
        runtimeState,
        runtimeReason,
      });
      expect(JSON.stringify(consume.mock.calls[1]?.[0])).not.toContain(
        selection.evidenceRefs[0],
      );
      expect(consume.mock.calls[1]?.[0]).not.toHaveProperty("resolution");

      binding.destroy();
    },
  );

  it("invalidates delivered evidence when the runtime is disposed", async () => {
    const runtime = createNullMapRuntime();
    await runtime.initialize();
    const consume = vi.fn();
    const binding = bindMapRuntimeEvidence(
      runtime,
      admittedLayerManifest,
      async () => answerFixture,
      consume,
    );

    runtime.emitSelection(selection);
    await vi.waitFor(() => expect(consume).toHaveBeenCalledTimes(1));
    runtime.dispose();

    expect(consume.mock.calls[1]?.[0]).toEqual({
      kind: "RUNTIME_INVALIDATED",
      selectionId: selection.selectionId,
      runtimeState: "DISPOSED",
      runtimeReason: "MAP_RUNTIME_DISPOSED",
    });

    binding.destroy();
  });

  it("keeps the runtime binding renderer-neutral, no-network, and outside lifecycle stores", () => {
    expect(bindingSource).not.toMatch(/\bfetch\s*\(/);
    expect(bindingSource).not.toMatch(
      /(?:from\s+|import\s*\()\s*["'](?:maplibre-gl|@maplibre\/[^"']+)["']/i,
    );
    expect(bindingSource).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
    expect(bindingSource).not.toMatch(/(?:ollama|model[-_ ]?runtime)/i);
  });
});
