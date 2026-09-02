import { describe, expect, it } from "vitest";

import {
  MAP_RUNTIME_TERRAIN_COORDINATOR_PROFILE,
  MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE,
  MAP_RUNTIME_TERRAIN_TRANSITION_PROFILE,
  createMapRuntimeTerrainTransitionCoordinator,
  planMapRuntimeTerrainTransition,
  resolveMapRuntimeTerrainState,
} from "../src/map-runtime-terrain-fallback";

const terrainRequest = {
  profile: MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE,
  mode: "TERRAIN",
  exaggeration: 1.5,
  fallback: "FLAT",
} as const;

describe("renderer-neutral terrain fallback", () => {
  it("retains flat mode without requiring terrain capabilities", () => {
    const state = resolveMapRuntimeTerrainState(
      {
        profile: MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE,
        mode: "FLAT",
        exaggeration: 0,
        fallback: "FLAT",
      },
      { terrainSupported: false, demSourceReady: false },
    );

    expect(state).toEqual({
      profile: MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE,
      mode: "FLAT",
      exaggeration: 0,
      reason: null,
    });
    expect(Object.isFrozen(state)).toBe(true);
  });

  it("selects terrain only when renderer support and source readiness are supplied", () => {
    expect(
      resolveMapRuntimeTerrainState(terrainRequest, {
        terrainSupported: true,
        demSourceReady: true,
      }),
    ).toEqual({
      profile: MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE,
      mode: "TERRAIN",
      exaggeration: 1.5,
      reason: null,
    });
  });

  it("falls back to flat when terrain is unsupported", () => {
    expect(
      resolveMapRuntimeTerrainState(terrainRequest, {
        terrainSupported: false,
        demSourceReady: true,
      }),
    ).toEqual({
      profile: MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE,
      mode: "FLAT",
      exaggeration: 0,
      reason: "TERRAIN_UNSUPPORTED",
    });
  });

  it("falls back to flat when the supplied DEM readiness fact is false", () => {
    expect(
      resolveMapRuntimeTerrainState(terrainRequest, {
        terrainSupported: true,
        demSourceReady: false,
      }),
    ).toEqual({
      profile: MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE,
      mode: "FLAT",
      exaggeration: 0,
      reason: "TERRAIN_SOURCE_UNAVAILABLE",
    });
  });

  it.each([
    { ...terrainRequest, profile: "wrong" },
    { ...terrainRequest, mode: "GLOBE" },
    { ...terrainRequest, exaggeration: 0 },
    { ...terrainRequest, exaggeration: 5.1 },
    { ...terrainRequest, exaggeration: Number.NaN },
    { ...terrainRequest, fallback: "TERRAIN" },
    { ...terrainRequest, extra: true },
    {
      profile: MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE,
      mode: "FLAT",
      exaggeration: 1,
      fallback: "FLAT",
    },
  ])("rejects malformed terrain requests", (request) => {
    expect(() =>
      resolveMapRuntimeTerrainState(request as never, {
        terrainSupported: true,
        demSourceReady: true,
      }),
    ).toThrow(expect.objectContaining({ code: "MAP_RUNTIME_STATE_INVALID" }));
  });

  it.each([
    { terrainSupported: true },
    { terrainSupported: true, demSourceReady: "yes" },
    { terrainSupported: true, demSourceReady: true, extra: true },
  ])("rejects malformed supplied capabilities", (capabilities) => {
    expect(() =>
      resolveMapRuntimeTerrainState(terrainRequest, capabilities as never),
    ).toThrow(expect.objectContaining({ code: "MAP_RUNTIME_STATE_INVALID" }));
  });
});

describe("renderer-neutral terrain transition planning", () => {
  it("enables terrain from the safe initial flat assumption", () => {
    const plan = planMapRuntimeTerrainTransition(null, terrainRequest, {
      terrainSupported: true,
      demSourceReady: true,
    });

    expect(plan).toEqual({
      profile: MAP_RUNTIME_TERRAIN_TRANSITION_PROFILE,
      effect: "ENABLE_TERRAIN",
      target: {
        profile: MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE,
        mode: "TERRAIN",
        exaggeration: 1.5,
        reason: null,
      },
    });
    expect(Object.isFrozen(plan)).toBe(true);
    expect(Object.isFrozen(plan.target)).toBe(true);
  });

  it("disables active terrain when capability support is lost", () => {
    const current = resolveMapRuntimeTerrainState(terrainRequest, {
      terrainSupported: true,
      demSourceReady: true,
    });

    expect(
      planMapRuntimeTerrainTransition(current, terrainRequest, {
        terrainSupported: false,
        demSourceReady: true,
      }),
    ).toEqual({
      profile: MAP_RUNTIME_TERRAIN_TRANSITION_PROFILE,
      effect: "DISABLE_TERRAIN",
      target: {
        profile: MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE,
        mode: "FLAT",
        exaggeration: 0,
        reason: "TERRAIN_UNSUPPORTED",
      },
    });
  });

  it("avoids renderer churn while still refreshing flat fallback metadata", () => {
    const current = resolveMapRuntimeTerrainState(terrainRequest, {
      terrainSupported: false,
      demSourceReady: true,
    });

    expect(
      planMapRuntimeTerrainTransition(current, terrainRequest, {
        terrainSupported: true,
        demSourceReady: false,
      }),
    ).toEqual({
      profile: MAP_RUNTIME_TERRAIN_TRANSITION_PROFILE,
      effect: "NONE",
      target: {
        profile: MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE,
        mode: "FLAT",
        exaggeration: 0,
        reason: "TERRAIN_SOURCE_UNAVAILABLE",
      },
    });
  });

  it("is idempotent for an already-applied terrain state", () => {
    const current = resolveMapRuntimeTerrainState(terrainRequest, {
      terrainSupported: true,
      demSourceReady: true,
    });

    expect(
      planMapRuntimeTerrainTransition(current, terrainRequest, {
        terrainSupported: true,
        demSourceReady: true,
      }).effect,
    ).toBe("NONE");
  });

  it("updates active terrain when the governed exaggeration changes", () => {
    const current = resolveMapRuntimeTerrainState(terrainRequest, {
      terrainSupported: true,
      demSourceReady: true,
    });

    expect(
      planMapRuntimeTerrainTransition(
        current,
        { ...terrainRequest, exaggeration: 2 },
        { terrainSupported: true, demSourceReady: true },
      ),
    ).toEqual({
      profile: MAP_RUNTIME_TERRAIN_TRANSITION_PROFILE,
      effect: "UPDATE_TERRAIN",
      target: {
        profile: MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE,
        mode: "TERRAIN",
        exaggeration: 2,
        reason: null,
      },
    });
  });

  it.each([
    {
      profile: MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE,
      mode: "FLAT",
      exaggeration: 0,
      reason: null,
      extra: true,
    },
    {
      profile: MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE,
      mode: "FLAT",
      exaggeration: 1,
      reason: null,
    },
    {
      profile: MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE,
      mode: "TERRAIN",
      exaggeration: 1,
      reason: "TERRAIN_UNSUPPORTED",
    },
    {
      profile: "wrong",
      mode: "FLAT",
      exaggeration: 0,
      reason: null,
    },
  ])("rejects malformed current terrain state", (current) => {
    expect(() =>
      planMapRuntimeTerrainTransition(current as never, terrainRequest, {
        terrainSupported: true,
        demSourceReady: true,
      }),
    ).toThrow(expect.objectContaining({ code: "MAP_RUNTIME_STATE_INVALID" }));
  });
});

describe("renderer-neutral terrain transition coordination", () => {
  it("advances state only after the exact pending ticket is committed", () => {
    const coordinator = createMapRuntimeTerrainTransitionCoordinator();
    const ticket = coordinator.plan(terrainRequest, {
      terrainSupported: true,
      demSourceReady: true,
    });

    expect(ticket).toEqual({
      profile: MAP_RUNTIME_TERRAIN_COORDINATOR_PROFILE,
      revision: 1,
      plan: {
        profile: MAP_RUNTIME_TERRAIN_TRANSITION_PROFILE,
        effect: "ENABLE_TERRAIN",
        target: {
          profile: MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE,
          mode: "TERRAIN",
          exaggeration: 1.5,
          reason: null,
        },
      },
    });
    expect(coordinator.getState()).toBeNull();
    expect(coordinator.commit(ticket)).toEqual(ticket.plan.target);
    expect(coordinator.getState()).toEqual(ticket.plan.target);
    expect(Object.isFrozen(ticket)).toBe(true);
  });

  it("keeps current state when renderer application is rejected", () => {
    const initial = resolveMapRuntimeTerrainState(terrainRequest, {
      terrainSupported: true,
      demSourceReady: true,
    });
    const coordinator = createMapRuntimeTerrainTransitionCoordinator(initial);
    const ticket = coordinator.plan(terrainRequest, {
      terrainSupported: false,
      demSourceReady: true,
    });

    expect(ticket.plan.effect).toBe("DISABLE_TERRAIN");
    expect(coordinator.reject(ticket)).toEqual(initial);
    expect(coordinator.getState()).toEqual(initial);
  });

  it("rejects stale tickets after a newer capability sample supersedes them", () => {
    const coordinator = createMapRuntimeTerrainTransitionCoordinator();
    const first = coordinator.plan(terrainRequest, {
      terrainSupported: true,
      demSourceReady: false,
    });
    const latest = coordinator.plan(terrainRequest, {
      terrainSupported: true,
      demSourceReady: true,
    });

    expect(first.revision).toBe(1);
    expect(latest.revision).toBe(2);
    expect(() => coordinator.commit(first)).toThrow(
      expect.objectContaining({ code: "MAP_RUNTIME_STATE_INVALID" }),
    );
    expect(coordinator.commit(latest).mode).toBe("TERRAIN");
  });

  it("commits only after asynchronous renderer execution succeeds", async () => {
    const coordinator = createMapRuntimeTerrainTransitionCoordinator();
    const ticket = coordinator.plan(terrainRequest, {
      terrainSupported: true,
      demSourceReady: true,
    });
    const applied: unknown[] = [];

    const state = await coordinator.execute(ticket, async (plan) => {
      expect(coordinator.getState()).toBeNull();
      applied.push(plan);
    });

    expect(applied).toEqual([ticket.plan]);
    expect(state).toBe(ticket.plan.target);
    expect(coordinator.getState()).toBe(ticket.plan.target);
  });

  it("normalizes renderer failure and preserves the applied state", async () => {
    const initial = resolveMapRuntimeTerrainState(terrainRequest, {
      terrainSupported: true,
      demSourceReady: true,
    });
    const coordinator = createMapRuntimeTerrainTransitionCoordinator(initial);
    const ticket = coordinator.plan(terrainRequest, {
      terrainSupported: false,
      demSourceReady: true,
    });

    await expect(
      coordinator.execute(ticket, () => {
        throw new Error("renderer detail must not escape");
      }),
    ).rejects.toMatchObject({
      code: "MAP_RUNTIME_TERRAIN_TRANSITION_FAILED",
      message: "Map runtime terrain transition execution failed.",
    });
    expect(coordinator.getState()).toBe(initial);
    expect(() => coordinator.commit(ticket)).toThrow(
      expect.objectContaining({ code: "MAP_RUNTIME_STATE_INVALID" }),
    );
  });

  it("serializes renderer execution and reconciles the next plan", async () => {
    const coordinator = createMapRuntimeTerrainTransitionCoordinator();
    const ticket = coordinator.plan(terrainRequest, {
      terrainSupported: true,
      demSourceReady: true,
    });
    let finishExecution: (() => void) | undefined;
    const execution = coordinator.execute(
      ticket,
      () =>
        new Promise<void>((resolve) => {
          finishExecution = resolve;
        }),
    );

    expect(() =>
      coordinator.plan(
        {
          profile: MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE,
          mode: "FLAT",
          exaggeration: 0,
          fallback: "FLAT",
        },
        { terrainSupported: true, demSourceReady: true },
      ),
    ).toThrow(expect.objectContaining({ code: "MAP_RUNTIME_STATE_INVALID" }));
    expect(() => coordinator.commit(ticket)).toThrow(
      expect.objectContaining({ code: "MAP_RUNTIME_STATE_INVALID" }),
    );
    expect(() => coordinator.reject(ticket)).toThrow(
      expect.objectContaining({ code: "MAP_RUNTIME_STATE_INVALID" }),
    );
    await expect(coordinator.execute(ticket, () => undefined)).rejects.toMatchObject({
      code: "MAP_RUNTIME_STATE_INVALID",
    });

    finishExecution?.();
    await expect(execution).resolves.toBe(ticket.plan.target);

    const flatPlan = coordinator.plan(
      {
        profile: MAP_RUNTIME_TERRAIN_FALLBACK_PROFILE,
        mode: "FLAT",
        exaggeration: 0,
        fallback: "FLAT",
      },
      { terrainSupported: true, demSourceReady: true },
    );
    expect(flatPlan.plan.effect).toBe("DISABLE_TERRAIN");
  });
});
