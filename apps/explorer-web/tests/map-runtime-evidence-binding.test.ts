import { describe, expect, it, vi } from "vitest";

import answerFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/answer-corrected.json";
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
});

async function settle(): Promise<void> {
  await Promise.resolve();
  await Promise.resolve();
}

describe("MapRuntimePort to governed Evidence Drawer binding", () => {
  it("translates an internal runtime selection through the existing strict bridge", async () => {
    const resolver = vi.fn(async () => answerFixture);
    const result = await resolveMapRuntimeSelectionEvidence(selection, resolver);

    expect(resolver).toHaveBeenCalledTimes(1);
    expect(result).toMatchObject({
      selection,
      code: "SUPPORTED",
      drawer: {
        outcome: "ANSWER",
        code: "SUPPORTED",
        evidenceRefs: ["kfm:evidence:synthetic:flow-001"],
      },
    });
  });

  it("fails closed before transport for an invalid or evidence-free runtime selection", async () => {
    const resolver = vi.fn(async () => answerFixture);

    const invalid = await resolveMapRuntimeSelectionEvidence(
      { ...selection, evidenceRefs: ["duplicate", "duplicate"] },
      resolver,
    );
    const missing = await resolveMapRuntimeSelectionEvidence(
      { ...selection, evidenceRefs: [] },
      resolver,
    );

    expect(resolver).not.toHaveBeenCalled();
    expect(invalid).toMatchObject({
      code: "SELECTION_INVALID",
      drawer: { outcome: "ERROR", code: "UPSTREAM_ERROR" },
    });
    expect(missing).toMatchObject({
      code: "MISSING_EVIDENCE",
      drawer: { outcome: "ABSTAIN", code: "MISSING_EVIDENCE" },
    });
  });

  it("delivers a NullMapRuntime selection through the governed resolver", async () => {
    const runtime = createNullMapRuntime();
    await runtime.initialize();
    const consume = vi.fn();
    const binding = bindMapRuntimeEvidence(
      runtime,
      async () => answerFixture,
      consume,
    );

    runtime.emitSelection(selection);

    await vi.waitFor(() => expect(consume).toHaveBeenCalledTimes(1));
    expect(consume.mock.calls[0]?.[0]).toMatchObject({
      selection,
      code: "SUPPORTED",
      drawer: { outcome: "ANSWER" },
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
    const binding = bindMapRuntimeEvidence(runtime, resolver, consume);

    runtime.emitSelection({ ...selection, selectionId: "selection:slow" });
    runtime.emitSelection({ ...selection, selectionId: "selection:newest" });

    await vi.waitFor(() => expect(consume).toHaveBeenCalledTimes(1));
    expect(consume.mock.calls[0]?.[0].selection?.selectionId).toBe(
      "selection:newest",
    );

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
    const binding = bindMapRuntimeEvidence(runtime, resolver, consume);

    runtime.emitSelection(selection);
    runtime.emitTrustState("WITHDRAWN");
    releasePending?.(answerFixture);
    await settle();

    expect(resolver).toHaveBeenCalledTimes(1);
    expect(consume).not.toHaveBeenCalled();
    expect(runtime.getSnapshot()).toMatchObject({
      state: "WITHDRAWN",
      reason: "MAP_RUNTIME_WITHDRAWN",
      selection: null,
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
