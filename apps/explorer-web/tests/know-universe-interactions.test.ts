import { describe, expect, it, vi } from "vitest";

import {
  createExplorationModeController,
  resolveExplorationShortcut,
} from "../src/features/map_runtime/exploration-mode";
import {
  VIEW_CONTEXT_PROFILE,
  resolveViewContext,
} from "../src/features/map_runtime/view-context-strip";
import {
  CROSSHAIR_CANDIDATE_PROFILE,
  resolveCrosshairSelection,
} from "../src/features/map_runtime/crosshair-selection";
import {
  SYNTHETIC_POINT_CLOUD_BENCHMARK_PROFILE,
  buildSyntheticPointCloudBenchmarkPlan,
  evaluatePointCloudBenchmark,
  sampleSyntheticPoint,
} from "../src/features/map_runtime/point-cloud-benchmark";

describe("explicit app-local exploration modes", () => {
  it("starts in inspectable 2D orientation and exposes a persistent traverse escape state", () => {
    const controller = createExplorationModeController();

    expect(controller.getSnapshot()).toMatchObject({
      state: "ACTIVE",
      mode: "ORIENT",
      traversalSpeed: 1,
      reason: "INITIALIZED",
      escapeHintVisible: false,
    });

    expect(controller.selectMode("TRAVERSE")).toMatchObject({
      mode: "TRAVERSE",
      reason: "USER_SELECTED",
      escapeHintVisible: true,
    });

    expect(controller.interrupt("ESCAPE")).toMatchObject({
      mode: "ORIENT",
      reason: "ESCAPE",
      escapeHintVisible: false,
    });
  });

  it("interrupts traversal when evidence or browser context takes precedence", () => {
    const controller = createExplorationModeController();

    controller.selectMode("TRAVERSE");
    expect(controller.interrupt("DRAWER_OPENED")).toMatchObject({
      mode: "ORIENT",
      reason: "DRAWER_OPENED",
    });

    controller.selectMode("STORY");
    expect(controller.interrupt("ROUTE_CHANGED")).toMatchObject({
      mode: "ORIENT",
      reason: "ROUTE_CHANGED",
    });
  });

  it("fails safely for reduced motion, invalid modes, and invalid speed", () => {
    const controller = createExplorationModeController({
      prefersReducedMotion: true,
      initialMode: "TRAVERSE",
    });

    expect(controller.getSnapshot()).toMatchObject({
      mode: "ORIENT",
      reason: "REDUCED_MOTION",
    });
    expect(controller.selectMode("TRAVERSE")).toMatchObject({
      mode: "ORIENT",
      reason: "REDUCED_MOTION",
    });
    expect(controller.selectMode("FLY")).toMatchObject({
      mode: "ORIENT",
      reason: "INVALID_MODE",
    });
    expect(controller.setTraversalSpeed(9)).toMatchObject({
      traversalSpeed: 1,
      reason: "INVALID_SPEED",
    });
    expect(controller.setTraversalSpeed(0.5)).toMatchObject({
      traversalSpeed: 0.5,
      reason: "SPEED_CHANGED",
    });
  });

  it("keeps single-key shortcuts out of text-entry and modifier contexts", () => {
    expect(
      resolveExplorationShortcut({ key: "t", targetKind: "OTHER" }),
    ).toBe("TRAVERSE");
    expect(
      resolveExplorationShortcut({ key: "i", targetKind: "TEXT_ENTRY" }),
    ).toBeNull();
    expect(
      resolveExplorationShortcut({
        key: "s",
        targetKind: "OTHER",
        ctrlKey: true,
      }),
    ).toBeNull();
    expect(
      resolveExplorationShortcut({ key: "Escape", targetKind: "OTHER" }),
    ).toBeNull();
  });

  it("freezes the controller after disposal", () => {
    const listener = vi.fn();
    const controller = createExplorationModeController();
    const unsubscribe = controller.subscribe(listener);
    expect(listener).toHaveBeenCalledTimes(1);

    const disposed = controller.dispose();
    expect(disposed).toMatchObject({ state: "DISPOSED", reason: "DISPOSED" });
    expect(controller.selectMode("TRAVERSE")).toBe(disposed);
    unsubscribe();
  });
});

describe("what-you-are-seeing context strip", () => {
  const derivedContext = {
    profile: VIEW_CONTEXT_PROFILE,
    placeLabel: "Kansas synthetic stage",
    timeLabel: "Fixture snapshot 2026-09-02",
    mode: "INSPECT",
    visibleLayerCount: 3,
    representationRole: "derived",
    release: "UNRELEASED",
    freshness: "UNKNOWN",
    correction: "NONE",
    publicSafe: true,
  } as const;

  it("summarizes place, time, mode, visible layers, and trust state", () => {
    const result = resolveViewContext(derivedContext);

    expect(result).toMatchObject({
      visibility: "VISIBLE",
      reason: "SUPPORTED",
      heading: "What you are seeing",
    });
    expect(result.labels).toEqual([
      "Place: Kansas synthetic stage",
      "Time: Fixture snapshot 2026-09-02",
      "Mode: INSPECT",
      "Visible layers: 3",
      "Representation: derived",
      "Release: UNRELEASED",
      "Freshness: UNKNOWN",
      "Correction: NONE",
    ]);
    expect(result.derivedDisclosure).toContain(
      "not a source-observed relationship or event",
    );
  });

  it("fails closed for private, extra-field, or malformed context", () => {
    expect(
      resolveViewContext({ ...derivedContext, publicSafe: false }),
    ).toMatchObject({ visibility: "HIDDEN", reason: "NOT_PUBLIC_SAFE" });
    expect(
      resolveViewContext({ ...derivedContext, privateNotes: "do not expose" }),
    ).toMatchObject({ visibility: "HIDDEN", reason: "INVALID_CONTEXT" });
    expect(
      resolveViewContext({ ...derivedContext, visibleLayerCount: -1 }),
    ).toMatchObject({ visibility: "HIDDEN", reason: "INVALID_CONTEXT" });
  });
});

describe("crosshair candidate selection", () => {
  const candidate = {
    profile: CROSSHAIR_CANDIDATE_PROFILE,
    candidateId: "selection:crosshair:flow-001",
    layerId: "layer:synthetic-streamflow",
    featureId: "feature:flow-001",
    evidenceRefs: ["kfm:evidence:synthetic:flow-001"],
    historyEvidenceRefs: ["kfm:evidence:synthetic:flow-000"],
    visibility: "PUBLIC_VISIBLE",
    publicSafe: true,
  } as const;

  it("converts one public-safe candidate into the existing map-selection wire shape", () => {
    expect(resolveCrosshairSelection([candidate])).toMatchObject({
      outcome: "ANSWER",
      code: "SUPPORTED",
      selection: {
        profile: "kfm.explorer.map-feature-selection.v1",
        selection_id: "selection:crosshair:flow-001",
        layer_id: "layer:synthetic-streamflow",
        feature_id: "feature:flow-001",
        evidence_refs: ["kfm:evidence:synthetic:flow-001"],
        history_evidence_refs: ["kfm:evidence:synthetic:flow-000"],
      },
    });
  });

  it("abstains instead of silently choosing among overlapping candidates", () => {
    const second = {
      ...candidate,
      candidateId: "selection:crosshair:flow-002",
      featureId: "feature:flow-002",
      evidenceRefs: [],
      historyEvidenceRefs: [],
    } as const;

    const result = resolveCrosshairSelection([candidate, second]);
    expect(result).toMatchObject({
      outcome: "ABSTAIN",
      code: "DISAMBIGUATION_REQUIRED",
      selection: null,
    });
    expect(result.candidates).toHaveLength(2);
  });

  it("abstains on no hit and rejects hidden, private, malformed, or duplicate candidates", () => {
    expect(resolveCrosshairSelection([])).toMatchObject({
      outcome: "ABSTAIN",
      code: "NO_CANDIDATE",
    });
    expect(
      resolveCrosshairSelection([{ ...candidate, visibility: "RESTRICTED" }]),
    ).toMatchObject({ outcome: "ERROR", code: "INVALID_CANDIDATE" });
    expect(
      resolveCrosshairSelection([{ ...candidate, publicSafe: false }]),
    ).toMatchObject({ outcome: "ERROR", code: "INVALID_CANDIDATE" });
    expect(
      resolveCrosshairSelection([{ ...candidate, rendererPayload: "pixel" }]),
    ).toMatchObject({ outcome: "ERROR", code: "INVALID_CANDIDATE" });
    expect(resolveCrosshairSelection([candidate, candidate])).toMatchObject({
      outcome: "ERROR",
      code: "INVALID_CANDIDATE",
    });
  });
});

describe("synthetic high-density spatial benchmark contract", () => {
  it("builds the required deterministic 50k, 250k, and 1m fixture matrix", () => {
    const first = buildSyntheticPointCloudBenchmarkPlan(42);
    const second = buildSyntheticPointCloudBenchmarkPlan(42);

    expect(first).toEqual(second);
    expect(first.authority).toBe("NONE");
    expect(first.cases.map((item) => item.pointCount)).toEqual([
      50_000,
      250_000,
      1_000_000,
    ]);
    expect(first.cases.every((item) => item.synthetic && item.publicSafe)).toBe(
      true,
    );
    expect(sampleSyntheticPoint(42, 7)).toEqual(
      sampleSyntheticPoint(42, 7),
    );
    expect(sampleSyntheticPoint(42, 7)).not.toEqual(
      sampleSyntheticPoint(42, 8),
    );
  });

  it("passes a safe in-budget result without claiming production readiness", () => {
    expect(
      evaluatePointCloudBenchmark({
        profile: SYNTHETIC_POINT_CLOUD_BENCHMARK_PROFILE,
        caseId: "synthetic-point-cloud-50000",
        pointCount: 50_000,
        initializationMs: 500,
        p95FrameMs: 20,
        mainThreadBlockMs: 50,
        selectionLatencyMs: 70,
        peakMemoryMb: 120,
        disposedCleanly: true,
        reducedMotionFallback: true,
        synthetic: true,
        publicSafe: true,
      }),
    ).toEqual({
      outcome: "PASS",
      reasons: ["BUDGETS_SATISFIED"],
      pointCount: 50_000,
      recommendedCarrier: "POINTS_3D",
    });
  });

  it("holds over-budget work and denies missing safety closure", () => {
    expect(
      evaluatePointCloudBenchmark({
        profile: SYNTHETIC_POINT_CLOUD_BENCHMARK_PROFILE,
        caseId: "synthetic-point-cloud-1000000",
        pointCount: 1_000_000,
        initializationMs: 8_000,
        p95FrameMs: 80,
        mainThreadBlockMs: 500,
        selectionLatencyMs: 400,
        peakMemoryMb: 2_000,
        disposedCleanly: true,
        reducedMotionFallback: true,
        synthetic: true,
        publicSafe: true,
      }),
    ).toMatchObject({
      outcome: "HOLD",
      recommendedCarrier: "CLUSTERED_2D",
    });

    expect(
      evaluatePointCloudBenchmark({
        profile: SYNTHETIC_POINT_CLOUD_BENCHMARK_PROFILE,
        caseId: "synthetic-point-cloud-250000",
        pointCount: 250_000,
        initializationMs: 1_000,
        p95FrameMs: 30,
        mainThreadBlockMs: 100,
        selectionLatencyMs: 100,
        peakMemoryMb: 300,
        disposedCleanly: false,
        reducedMotionFallback: false,
        synthetic: true,
        publicSafe: true,
      }),
    ).toEqual({
      outcome: "DENY",
      reasons: [
        "DISPOSAL_NOT_PROVEN",
        "REDUCED_MOTION_FALLBACK_MISSING",
      ],
      pointCount: 250_000,
      recommendedCarrier: "CLUSTERED_2D",
    });
  });

  it("errors on an unknown or expanded payload rather than accepting partial measurements", () => {
    expect(
      evaluatePointCloudBenchmark({
        profile: SYNTHETIC_POINT_CLOUD_BENCHMARK_PROFILE,
        caseId: "synthetic-point-cloud-50000",
        pointCount: 50_000,
        initializationMs: 500,
        p95FrameMs: 20,
        mainThreadBlockMs: 50,
        selectionLatencyMs: 70,
        peakMemoryMb: 120,
        disposedCleanly: true,
        reducedMotionFallback: true,
        synthetic: true,
        publicSafe: true,
        productionReady: true,
      }),
    ).toEqual({
      outcome: "ERROR",
      reasons: ["INVALID_MEASUREMENT"],
      pointCount: null,
      recommendedCarrier: null,
    });
  });
});
