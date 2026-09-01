import { describe, expect, it } from "vitest";

import { MapRuntimePortError } from "../src/map-runtime-port";
import {
  createMapRuntimeResizeCoordinator,
  type MapRuntimeFrameScheduler,
} from "../src/map-runtime-resize-coordinator";
import { NullMapRuntime } from "../src/null-map-runtime";

class ManualFrameScheduler implements MapRuntimeFrameScheduler {
  private nextHandle = 1;
  private readonly callbacks = new Map<number, () => void>();
  requestCalls = 0;
  cancelCalls = 0;

  request(callback: () => void): number {
    this.requestCalls += 1;
    const handle = this.nextHandle++;
    this.callbacks.set(handle, callback);
    return handle;
  }

  cancel(handle: number): void {
    this.cancelCalls += 1;
    this.callbacks.delete(handle);
  }

  get pendingCount(): number {
    return this.callbacks.size;
  }

  runNext(): void {
    const entry = this.callbacks.entries().next();
    if (entry.done) throw new Error("No scheduled frame is pending.");
    const [handle, callback] = entry.value;
    this.callbacks.delete(handle);
    callback();
  }
}

class ThrowOnceFrameScheduler extends ManualFrameScheduler {
  throwNext = true;

  override request(callback: () => void): number {
    if (this.throwNext) {
      this.throwNext = false;
      throw new Error("synthetic scheduler failure");
    }
    return super.request(callback);
  }
}

class CountingNullMapRuntime extends NullMapRuntime {
  resizeCalls = 0;
  failNextWithRawError = false;

  override resize() {
    this.resizeCalls += 1;
    if (this.failNextWithRawError) {
      this.failNextWithRawError = false;
      throw new Error("synthetic raw resize failure");
    }
    return super.resize();
  }
}

describe("MapRuntime resize coordinator", () => {
  it("coalesces repeated responsive resize requests into one frame", async () => {
    const runtime = new CountingNullMapRuntime();
    await runtime.initialize();
    const scheduler = new ManualFrameScheduler();
    const coordinator = createMapRuntimeResizeCoordinator(runtime, scheduler);

    const first = coordinator.schedule();
    const second = coordinator.schedule();
    const third = coordinator.schedule();

    expect(first).toBe(second);
    expect(second).toBe(third);
    expect(coordinator.hasPending()).toBe(true);
    expect(scheduler.requestCalls).toBe(1);
    expect(scheduler.pendingCount).toBe(1);
    expect(runtime.resizeCalls).toBe(0);

    scheduler.runNext();

    await expect(first).resolves.toEqual(runtime.getSnapshot());
    expect(coordinator.hasPending()).toBe(false);
    expect(scheduler.pendingCount).toBe(0);
    expect(runtime.resizeCalls).toBe(1);
  });

  it("flushes a pending resize exactly once and settles the shared promise", async () => {
    const runtime = new CountingNullMapRuntime();
    await runtime.initialize();
    const scheduler = new ManualFrameScheduler();
    const coordinator = createMapRuntimeResizeCoordinator(runtime, scheduler);

    const pending = coordinator.schedule();
    const snapshot = coordinator.flush();

    await expect(pending).resolves.toEqual(snapshot);
    expect(runtime.resizeCalls).toBe(1);
    expect(scheduler.cancelCalls).toBe(1);
    expect(scheduler.pendingCount).toBe(0);
    expect(coordinator.hasPending()).toBe(false);
  });

  it("normalizes scheduler startup failures and remains reusable", async () => {
    const runtime = new CountingNullMapRuntime();
    await runtime.initialize();
    const scheduler = new ThrowOnceFrameScheduler();
    const coordinator = createMapRuntimeResizeCoordinator(runtime, scheduler);

    await expect(coordinator.schedule()).rejects.toMatchObject({
      name: "MapRuntimePortError",
      code: "MAP_RUNTIME_RESIZE_FAILED",
    });
    expect(coordinator.hasPending()).toBe(false);
    expect(runtime.resizeCalls).toBe(0);

    const retry = coordinator.schedule();
    scheduler.runNext();
    await expect(retry).resolves.toEqual(runtime.getSnapshot());
    expect(runtime.resizeCalls).toBe(1);
  });

  it("normalizes raw runtime failures without wedging later resize work", async () => {
    const runtime = new CountingNullMapRuntime();
    await runtime.initialize();
    runtime.failNextWithRawError = true;
    const scheduler = new ManualFrameScheduler();
    const coordinator = createMapRuntimeResizeCoordinator(runtime, scheduler);

    const failed = coordinator.schedule();
    scheduler.runNext();
    await expect(failed).rejects.toMatchObject({
      name: "MapRuntimePortError",
      code: "MAP_RUNTIME_RESIZE_FAILED",
    });
    expect(coordinator.hasPending()).toBe(false);

    const recovered = coordinator.schedule();
    scheduler.runNext();
    await expect(recovered).resolves.toEqual(runtime.getSnapshot());
    expect(runtime.resizeCalls).toBe(2);
  });

  it("preserves finite MapRuntimePort errors from the underlying runtime", async () => {
    const runtime = new CountingNullMapRuntime();
    const scheduler = new ManualFrameScheduler();
    const coordinator = createMapRuntimeResizeCoordinator(runtime, scheduler);

    const pending = coordinator.schedule();
    scheduler.runNext();

    await expect(pending).rejects.toMatchObject({
      name: "MapRuntimePortError",
      code: "MAP_RUNTIME_NOT_READY",
    });
    expect(runtime.resizeCalls).toBe(1);
  });

  it("cancels pending work on disposal and fails closed afterwards", async () => {
    const runtime = new CountingNullMapRuntime();
    await runtime.initialize();
    const scheduler = new ManualFrameScheduler();
    const coordinator = createMapRuntimeResizeCoordinator(runtime, scheduler);

    const pending = coordinator.schedule();
    coordinator.dispose();
    coordinator.dispose();

    await expect(pending).rejects.toMatchObject({
      name: "MapRuntimePortError",
      code: "MAP_RUNTIME_DISPOSED",
    });
    await expect(coordinator.schedule()).rejects.toMatchObject({
      name: "MapRuntimePortError",
      code: "MAP_RUNTIME_DISPOSED",
    });
    expect(() => coordinator.flush()).toThrow(
      expect.objectContaining({
        name: "MapRuntimePortError",
        code: "MAP_RUNTIME_DISPOSED",
      }),
    );
    expect(scheduler.cancelCalls).toBe(1);
    expect(scheduler.pendingCount).toBe(0);
    expect(runtime.resizeCalls).toBe(0);
  });

  it("uses MapRuntimePortError for normalized failures", () => {
    const error = new MapRuntimePortError(
      "MAP_RUNTIME_RESIZE_FAILED",
      "synthetic finite error",
    );
    expect(error).toBeInstanceOf(Error);
    expect(error.name).toBe("MapRuntimePortError");
  });
});
