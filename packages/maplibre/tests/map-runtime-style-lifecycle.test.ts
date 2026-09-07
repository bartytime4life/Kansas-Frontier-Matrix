import { describe, expect, it } from "vitest";

import {
  MAP_RUNTIME_STYLE_COORDINATOR_PROFILE,
  MAP_RUNTIME_STYLE_LAYER_PROFILE,
  MAP_RUNTIME_STYLE_PLAN_PROFILE,
  MAP_RUNTIME_STYLE_PROFILE,
  MAP_RUNTIME_STYLE_SOURCE_PROFILE,
  createMapRuntimeStyleLifecycleExecutor,
  createMapRuntimeStyleLifecycleCoordinator,
  freezeMapRuntimeStyleState,
  planMapRuntimeStyleLifecycle,
  type MapRuntimeStyleState,
} from "../src/map-runtime-style-lifecycle";

function style(
  sources: readonly [sourceId: string, revision: string][],
  layers: readonly [layerId: string, sourceId: string, revision?: string][],
): MapRuntimeStyleState {
  return {
    profile: MAP_RUNTIME_STYLE_PROFILE,
    sources: sources.map(([sourceId, revision]) => ({
      profile: MAP_RUNTIME_STYLE_SOURCE_PROFILE,
      sourceId,
      revision,
    })),
    layers: layers.map(([layerId, sourceId, revision = "v1"], order) => ({
      profile: MAP_RUNTIME_STYLE_LAYER_PROFILE,
      layerId,
      sourceId,
      revision,
      order,
    })),
  };
}

describe("renderer-neutral source and layer lifecycle", () => {
  it("adds canonical sources before bottom-up layers", () => {
    const target = style(
      [
        ["roads", "v1"],
        ["places", "v3"],
      ],
      [
        ["roads-line", "roads"],
        ["places-label", "places"],
      ],
    );

    expect(planMapRuntimeStyleLifecycle(null, target)).toEqual({
      profile: MAP_RUNTIME_STYLE_PLAN_PROFILE,
      current: style([], []),
      target: freezeMapRuntimeStyleState(target),
      actions: [
        {
          effect: "ADD_SOURCE",
          source: {
            profile: MAP_RUNTIME_STYLE_SOURCE_PROFILE,
            sourceId: "places",
            revision: "v3",
          },
        },
        {
          effect: "ADD_SOURCE",
          source: {
            profile: MAP_RUNTIME_STYLE_SOURCE_PROFILE,
            sourceId: "roads",
            revision: "v1",
          },
        },
        {
          effect: "ADD_LAYER",
          layer: {
            profile: MAP_RUNTIME_STYLE_LAYER_PROFILE,
            layerId: "roads-line",
            sourceId: "roads",
            revision: "v1",
            order: 0,
          },
        },
        {
          effect: "ADD_LAYER",
          layer: {
            profile: MAP_RUNTIME_STYLE_LAYER_PROFILE,
            layerId: "places-label",
            sourceId: "places",
            revision: "v1",
            order: 1,
          },
        },
      ],
    });
  });

  it("removes top-down layers before their sources", () => {
    const current = style(
      [
        ["roads", "v1"],
        ["places", "v3"],
      ],
      [
        ["roads-line", "roads"],
        ["places-label", "places"],
      ],
    );

    expect(planMapRuntimeStyleLifecycle(current, style([], [])).actions).toEqual([
      { effect: "REMOVE_LAYER", layerId: "places-label" },
      { effect: "REMOVE_LAYER", layerId: "roads-line" },
      { effect: "REMOVE_SOURCE", sourceId: "places" },
      { effect: "REMOVE_SOURCE", sourceId: "roads" },
    ]);
  });

  it("rebuilds dependent layers around a source revision change", () => {
    const current = style(
      [["terrain", "2026-08"]],
      [
        ["hillshade", "terrain"],
        ["contours", "terrain"],
      ],
    );
    const target = style(
      [["terrain", "2026-09"]],
      [
        ["hillshade", "terrain"],
        ["contours", "terrain"],
      ],
    );

    expect(planMapRuntimeStyleLifecycle(current, target).actions).toEqual([
      { effect: "REMOVE_LAYER", layerId: "contours" },
      { effect: "REMOVE_LAYER", layerId: "hillshade" },
      { effect: "REMOVE_SOURCE", sourceId: "terrain" },
      {
        effect: "ADD_SOURCE",
        source: {
          profile: MAP_RUNTIME_STYLE_SOURCE_PROFILE,
          sourceId: "terrain",
          revision: "2026-09",
        },
      },
      {
        effect: "ADD_LAYER",
        layer: {
          profile: MAP_RUNTIME_STYLE_LAYER_PROFILE,
          layerId: "hillshade",
          sourceId: "terrain",
          revision: "v1",
          order: 0,
        },
      },
      {
        effect: "ADD_LAYER",
        layer: {
          profile: MAP_RUNTIME_STYLE_LAYER_PROFILE,
          layerId: "contours",
          sourceId: "terrain",
          revision: "v1",
          order: 1,
        },
      },
    ]);
  });

  it("rebuilds reordered layers without churning their source", () => {
    const current = style(
      [["boundaries", "v1"]],
      [
        ["county-fill", "boundaries"],
        ["county-line", "boundaries"],
      ],
    );
    const target = style(
      [["boundaries", "v1"]],
      [
        ["county-line", "boundaries"],
        ["county-fill", "boundaries"],
      ],
    );

    expect(planMapRuntimeStyleLifecycle(current, target).actions).toEqual([
      { effect: "REMOVE_LAYER", layerId: "county-line" },
      { effect: "REMOVE_LAYER", layerId: "county-fill" },
      {
        effect: "ADD_LAYER",
        layer: {
          profile: MAP_RUNTIME_STYLE_LAYER_PROFILE,
          layerId: "county-line",
          sourceId: "boundaries",
          revision: "v1",
          order: 0,
        },
      },
      {
        effect: "ADD_LAYER",
        layer: {
          profile: MAP_RUNTIME_STYLE_LAYER_PROFILE,
          layerId: "county-fill",
          sourceId: "boundaries",
          revision: "v1",
          order: 1,
        },
      },
    ]);
  });

  it("rebuilds a changed lower layer and every higher layer", () => {
    const current = style(
      [
        ["lower-source", "v1"],
        ["higher-source", "v1"],
      ],
      [
        ["lower-layer", "lower-source", "paint-v1"],
        ["higher-layer", "higher-source", "paint-v1"],
      ],
    );
    const target = style(
      [
        ["lower-source", "v1"],
        ["higher-source", "v1"],
      ],
      [
        ["lower-layer", "lower-source", "paint-v2"],
        ["higher-layer", "higher-source", "paint-v1"],
      ],
    );

    expect(planMapRuntimeStyleLifecycle(current, target).actions).toEqual([
      { effect: "REMOVE_LAYER", layerId: "higher-layer" },
      { effect: "REMOVE_LAYER", layerId: "lower-layer" },
      {
        effect: "ADD_LAYER",
        layer: {
          profile: MAP_RUNTIME_STYLE_LAYER_PROFILE,
          layerId: "lower-layer",
          sourceId: "lower-source",
          revision: "paint-v2",
          order: 0,
        },
      },
      {
        effect: "ADD_LAYER",
        layer: {
          profile: MAP_RUNTIME_STYLE_LAYER_PROFILE,
          layerId: "higher-layer",
          sourceId: "higher-source",
          revision: "paint-v1",
          order: 1,
        },
      },
    ]);
  });

  it("is immutable and idempotent for an equivalent canonical state", () => {
    const current = style(
      [
        ["zoning", "v2"],
        ["roads", "v1"],
      ],
      [["roads-line", "roads"]],
    );
    const plan = planMapRuntimeStyleLifecycle(current, current);

    expect(plan.actions).toEqual([]);
    expect(plan.target.sources.map(({ sourceId }) => sourceId)).toEqual([
      "roads",
      "zoning",
    ]);
    expect(Object.isFrozen(plan)).toBe(true);
    expect(Object.isFrozen(plan.actions)).toBe(true);
    expect(Object.isFrozen(plan.target)).toBe(true);
    expect(Object.isFrozen(plan.target.sources[0])).toBe(true);
  });

  it.each([
    {
      ...style([["roads", "v1"]], []),
      extra: true,
    },
    style(
      [
        ["roads", "v1"],
        ["roads", "v2"],
      ],
      [],
    ),
    style([["roads", "v1"]], [["road-line", "missing"]]),
    {
      ...style([["roads", "v1"]], [["road-line", "roads"]]),
      layers: [
        {
          profile: MAP_RUNTIME_STYLE_LAYER_PROFILE,
          layerId: "road-line",
          sourceId: "roads",
          revision: "v1",
          order: 1,
        },
      ],
    },
    style([["unsafe/id", "v1"]], []),
    {
      profile: MAP_RUNTIME_STYLE_PROFILE,
      sources: new Array(1),
      layers: [],
    },
    {
      profile: MAP_RUNTIME_STYLE_PROFILE,
      sources: [
        {
          profile: MAP_RUNTIME_STYLE_SOURCE_PROFILE,
          sourceId: "roads",
          revision: "v1",
        },
      ],
      layers: new Array(1),
    },
  ])("fails closed for malformed lifecycle state", (candidate) => {
    expect(() => freezeMapRuntimeStyleState(candidate as never)).toThrow(
      expect.objectContaining({ code: "MAP_RUNTIME_STATE_INVALID" }),
    );
  });
});

describe("renderer-neutral style lifecycle coordination", () => {
  it("executes lifecycle actions sequentially with immutable progress", async () => {
    const plan = planMapRuntimeStyleLifecycle(
      style([["roads", "v1"]], [["roads-line", "roads"]]),
      style([["places", "v1"]], [["places-label", "places"]]),
    );
    const observed: Array<{
      effect: string;
      index: number;
      total: number;
      frozen: boolean;
    }> = [];
    let active = 0;

    const execute = createMapRuntimeStyleLifecycleExecutor(
      async (action, context) => {
        active += 1;
        expect(active).toBe(1);
        observed.push({
          effect: action.effect,
          index: context.index,
          total: context.total,
          frozen: Object.isFrozen(context),
        });
        await Promise.resolve();
        active -= 1;
      },
    );

    await execute(plan, new AbortController().signal);

    expect(observed).toEqual(
      plan.actions.map((action, index) => ({
        effect: action.effect,
        index,
        total: plan.actions.length,
        frozen: true,
      })),
    );
  });

  it("does not start actions when execution is already cancelled", async () => {
    const plan = planMapRuntimeStyleLifecycle(
      style([], []),
      style([["roads", "v1"]], [["roads-line", "roads"]]),
    );
    const controller = new AbortController();
    controller.abort();
    let calls = 0;
    const execute = createMapRuntimeStyleLifecycleExecutor(() => {
      calls += 1;
    });

    await expect(execute(plan, controller.signal)).rejects.toMatchObject({
      code: "MAP_RUNTIME_STYLE_LIFECYCLE_CANCELLED",
    });
    expect(calls).toBe(0);
  });

  it("stops before the next action when an active action ignores cancellation", async () => {
    const coordinator = createMapRuntimeStyleLifecycleCoordinator(
      style([["roads", "v1"]], [["roads-line", "roads"]]),
    );
    const ticket = coordinator.plan(
      style([["places", "v1"]], [["places-label", "places"]]),
    );
    let finishFirst: (() => void) | undefined;
    const effects: string[] = [];
    const execute = createMapRuntimeStyleLifecycleExecutor(
      (action) => {
        effects.push(action.effect);
        return new Promise<void>((resolve) => {
          finishFirst = resolve;
        });
      },
    );
    const execution = coordinator.execute(ticket, execute);

    coordinator.cancel(ticket);
    finishFirst?.();

    await expect(execution).rejects.toMatchObject({
      code: "MAP_RUNTIME_STYLE_LIFECYCLE_CANCELLED",
    });
    expect(effects).toEqual([ticket.plan.actions[0].effect]);
    expect(coordinator.requiresReconciliation()).toBe(true);
  });

  it("advances confirmed state only for the exact pending ticket", () => {
    const initial = style([["roads", "v1"]], [["roads-line", "roads"]]);
    const coordinator = createMapRuntimeStyleLifecycleCoordinator(initial);
    const stale = coordinator.plan(style([["roads", "v2"]], []));
    const latest = coordinator.plan(
      style([["places", "v1"]], [["places-label", "places"]]),
    );

    expect(stale).toMatchObject({
      profile: MAP_RUNTIME_STYLE_COORDINATOR_PROFILE,
      revision: 1,
    });
    expect(latest.revision).toBe(2);
    expect(coordinator.getState()).toEqual(freezeMapRuntimeStyleState(initial));
    expect(() => coordinator.commit(stale)).toThrow(
      expect.objectContaining({ code: "MAP_RUNTIME_STATE_INVALID" }),
    );
    expect(coordinator.commit(latest)).toBe(latest.plan.target);
    expect(coordinator.getState()).toBe(latest.plan.target);
    expect(Object.isFrozen(latest)).toBe(true);
  });

  it("commits only after asynchronous renderer execution succeeds", async () => {
    const coordinator = createMapRuntimeStyleLifecycleCoordinator();
    const target = style([["roads", "v1"]], [["roads-line", "roads"]]);
    const ticket = coordinator.plan(target);
    const empty = freezeMapRuntimeStyleState(style([], []));
    let observedSignal: AbortSignal | undefined;

    const result = await coordinator.execute(ticket, async (plan, signal) => {
      observedSignal = signal;
      expect(plan).toBe(ticket.plan);
      expect(coordinator.getState()).toEqual(empty);
      await Promise.resolve();
    });

    expect(observedSignal?.aborted).toBe(false);
    expect(result).toBe(ticket.plan.target);
    expect(coordinator.getState()).toBe(ticket.plan.target);
    expect(coordinator.requiresReconciliation()).toBe(false);
  });

  it("fails closed for a partial renderer failure until reconciliation", async () => {
    const initial = style([["roads", "v1"]], [["roads-line", "roads"]]);
    const target = style([["roads", "v2"]], [["roads-line", "roads"]]);
    const coordinator = createMapRuntimeStyleLifecycleCoordinator(initial);
    const ticket = coordinator.plan(target);

    await expect(
      coordinator.execute(ticket, () => {
        throw new Error("renderer detail must not escape");
      }),
    ).rejects.toMatchObject({
      code: "MAP_RUNTIME_STYLE_LIFECYCLE_FAILED",
      message: "Map runtime style lifecycle execution failed.",
    });
    expect(coordinator.getState()).toEqual(freezeMapRuntimeStyleState(initial));
    expect(coordinator.requiresReconciliation()).toBe(true);
    expect(() => coordinator.plan(target)).toThrow(
      expect.objectContaining({
        code: "MAP_RUNTIME_STYLE_RECONCILIATION_REQUIRED",
      }),
    );

    const observed = style([], []);
    expect(coordinator.reconcile(observed)).toEqual(
      freezeMapRuntimeStyleState(observed),
    );
    expect(coordinator.requiresReconciliation()).toBe(false);
    expect(coordinator.reject(coordinator.plan(target))).toEqual(
      freezeMapRuntimeStyleState(observed),
    );
  });

  it("serializes renderer execution", async () => {
    const coordinator = createMapRuntimeStyleLifecycleCoordinator();
    const ticket = coordinator.plan(
      style([["roads", "v1"]], [["roads-line", "roads"]]),
    );
    let finish: (() => void) | undefined;
    const execution = coordinator.execute(
      ticket,
      () => new Promise<void>((resolve) => {
        finish = resolve;
      }),
    );

    expect(() => coordinator.plan(style([], []))).toThrow(
      expect.objectContaining({ code: "MAP_RUNTIME_STATE_INVALID" }),
    );
    expect(() => coordinator.commit(ticket)).toThrow(
      expect.objectContaining({ code: "MAP_RUNTIME_STATE_INVALID" }),
    );
    await expect(coordinator.execute(ticket, () => undefined)).rejects.toMatchObject({
      code: "MAP_RUNTIME_STATE_INVALID",
    });

    finish?.();
    await expect(execution).resolves.toBe(ticket.plan.target);
  });

  it("cancels exact work and contains late renderer completion", async () => {
    const initial = style([["roads", "v1"]], [["roads-line", "roads"]]);
    const coordinator = createMapRuntimeStyleLifecycleCoordinator(initial);
    const cancelled = coordinator.plan(style([], []));
    let finishCancelled: (() => void) | undefined;
    let cancelledSignal: AbortSignal | undefined;
    const cancelledExecution = coordinator.execute(
      cancelled,
      (_plan, signal) => new Promise<void>((resolve) => {
        cancelledSignal = signal;
        finishCancelled = resolve;
      }),
    );

    expect(coordinator.cancel(cancelled)).toEqual(
      freezeMapRuntimeStyleState(initial),
    );
    expect(cancelledSignal?.aborted).toBe(true);
    expect(coordinator.requiresReconciliation()).toBe(true);

    coordinator.reconcile(initial);
    const replacement = coordinator.plan(
      style([["roads", "v2"]], [["roads-line", "roads"]]),
    );
    await expect(
      coordinator.execute(replacement, () => undefined),
    ).resolves.toBe(replacement.plan.target);

    finishCancelled?.();
    await expect(cancelledExecution).rejects.toMatchObject({
      code: "MAP_RUNTIME_STYLE_LIFECYCLE_CANCELLED",
      message: "Map runtime style lifecycle execution was cancelled.",
    });
    expect(coordinator.getState()).toBe(replacement.plan.target);
  });

  it("disposes idempotently and prevents late completion from committing", async () => {
    const initial = style([["roads", "v1"]], [["roads-line", "roads"]]);
    const coordinator = createMapRuntimeStyleLifecycleCoordinator(initial);
    const ticket = coordinator.plan(style([], []));
    let finish: (() => void) | undefined;
    let signal: AbortSignal | undefined;
    let abortEvents = 0;
    const execution = coordinator.execute(
      ticket,
      (_plan, nextSignal) => new Promise<void>((resolve) => {
        signal = nextSignal;
        nextSignal.addEventListener("abort", () => {
          abortEvents += 1;
        });
        finish = resolve;
      }),
    );

    coordinator.dispose();
    coordinator.dispose();
    expect(signal?.aborted).toBe(true);
    expect(abortEvents).toBe(1);
    expect(coordinator.getState()).toEqual(freezeMapRuntimeStyleState(initial));
    expect(() => coordinator.plan(style([], []))).toThrow(
      expect.objectContaining({ code: "MAP_RUNTIME_DISPOSED" }),
    );

    finish?.();
    await expect(execution).rejects.toMatchObject({
      code: "MAP_RUNTIME_DISPOSED",
      message: "Map runtime style lifecycle coordinator is disposed.",
    });
    expect(coordinator.getState()).toEqual(freezeMapRuntimeStyleState(initial));
  });
});
