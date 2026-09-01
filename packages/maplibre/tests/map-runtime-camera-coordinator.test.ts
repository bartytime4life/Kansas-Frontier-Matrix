import { describe, expect, it } from "vitest";

import type { MapRuntimeCamera } from "../src/map-runtime-port";
import {
  createMapRuntimeCameraCoordinator,
} from "../src/map-runtime-camera-coordinator";
import type { MapRuntimeFrameScheduler } from "../src/map-runtime-resize-coordinator";
import { NullMapRuntime } from "../src/null-map-runtime";

const CAMERA_A: MapRuntimeCamera = Object.freeze({
  longitude: -100,
  latitude: 38,
  zoom: 6,
  bearing: 0,
  pitch: 0,
});

const CAMERA_B: MapRuntimeCamera = Object.freeze({
  longitude: -99,
  latitude: 39,
  zoom: 7,
  bearing: 10,
  pitch: 20,
});

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
  readonly cameraCalls: MapRuntimeCamera[] = [];
  failNextWithRawError = false;

  override setCamera(camera: MapRuntimeCamera) {
    this.cameraCalls.push(camera);
    if (this.failNextWithRawError) {
      this.failNextWithRawError = false;
      throw new Error("synthetic raw navigation failure");
    }
    return super.setCamera(camera);
  }
}

describe("MapRuntime camera coordinator", () => {
  it("coalesces a camera burst to the latest valid camera in one frame", async () => {
    const runtime = new CountingNullMapRuntime();
    await runtime.initialize();
    const scheduler = new ManualFrameScheduler();
    const coordinator = createMapRuntimeCameraCoordinator(runtime, scheduler);

    const first = coordinator.schedule(CAMERA_A);
    const second = coordinator.schedule(CAMERA_B);

    expect(first).toBe(second);
    expect(coordinator.hasPending()).toBe(true);
    expect(scheduler.requestCalls).toBe(1);
    expect(scheduler.pendingCount).toBe(1);
    expect(runtime.cameraCalls).toEqual([]);

    scheduler.runNext();

    await expect(first).resolves.toMatchObject({ camera: CAMERA_B });
    expect(runtime.cameraCalls).toEqual([CAMERA_B]);
    expect(coordinator.hasPending()).toBe(false);
    expect(scheduler.pendingCount).toBe(0);
  });

  it("does not let an invalid later request replace a valid pending camera", async () => {
    const runtime = new CountingNullMapRuntime();
    await runtime.initialize();
    const scheduler = new ManualFrameScheduler();
    const coordinator = createMapRuntimeCameraCoordinator(runtime, scheduler);

    const pending = coordinator.schedule(CAMERA_A);
    await expect(
      coordinator.schedule({ ...CAMERA_B, zoom: 99 }),
    ).rejects.toMatchObject({
      name: "MapRuntimePortError",
      code: "MAP_RUNTIME_CAMERA_INVALID",
    });

    scheduler.runNext();

    await expect(pending).resolves.toMatchObject({ camera: CAMERA_A });
    expect(runtime.cameraCalls).toEqual([CAMERA_A]);
  });

  it("flushes the latest pending camera exactly once", async () => {
    const runtime = new CountingNullMapRuntime();
    await runtime.initialize();
    const scheduler = new ManualFrameScheduler();
    const coordinator = createMapRuntimeCameraCoordinator(runtime, scheduler);

    const pending = coordinator.schedule(CAMERA_A);
    coordinator.schedule(CAMERA_B);
    const snapshot = coordinator.flush();

    await expect(pending).resolves.toEqual(snapshot);
    expect(snapshot.camera).toEqual(CAMERA_B);
    expect(runtime.cameraCalls).toEqual([CAMERA_B]);
    expect(scheduler.cancelCalls).toBe(1);
    expect(scheduler.pendingCount).toBe(0);
    expect(coordinator.hasPending()).toBe(false);
  });

  it("returns the current snapshot when flush has no pending navigation", async () => {
    const runtime = new CountingNullMapRuntime();
    await runtime.initialize(CAMERA_A);
    const coordinator = createMapRuntimeCameraCoordinator(
      runtime,
      new ManualFrameScheduler(),
    );

    expect(coordinator.flush()).toEqual(runtime.getSnapshot());
    expect(runtime.cameraCalls).toEqual([]);
  });

  it("normalizes scheduler startup failures and remains reusable", async () => {
    const runtime = new CountingNullMapRuntime();
    await runtime.initialize();
    const scheduler = new ThrowOnceFrameScheduler();
    const coordinator = createMapRuntimeCameraCoordinator(runtime, scheduler);

    await expect(coordinator.schedule(CAMERA_A)).rejects.toMatchObject({
      name: "MapRuntimePortError",
      code: "MAP_RUNTIME_NAVIGATION_FAILED",
    });
    expect(coordinator.hasPending()).toBe(false);
    expect(runtime.cameraCalls).toEqual([]);

    const retry = coordinator.schedule(CAMERA_B);
    scheduler.runNext();
    await expect(retry).resolves.toMatchObject({ camera: CAMERA_B });
    expect(runtime.cameraCalls).toEqual([CAMERA_B]);
  });

  it("normalizes raw runtime failures without wedging later navigation", async () => {
    const runtime = new CountingNullMapRuntime();
    await runtime.initialize();
    runtime.failNextWithRawError = true;
    const scheduler = new ManualFrameScheduler();
    const coordinator = createMapRuntimeCameraCoordinator(runtime, scheduler);

    const failed = coordinator.schedule(CAMERA_A);
    scheduler.runNext();
    await expect(failed).rejects.toMatchObject({
      name: "MapRuntimePortError",
      code: "MAP_RUNTIME_NAVIGATION_FAILED",
    });
    expect(coordinator.hasPending()).toBe(false);

    const recovered = coordinator.schedule(CAMERA_B);
    scheduler.runNext();
    await expect(recovered).resolves.toMatchObject({ camera: CAMERA_B });
    expect(runtime.cameraCalls).toEqual([CAMERA_A, CAMERA_B]);
  });

  it("preserves finite MapRuntimePort readiness failures", async () => {
    const runtime = new CountingNullMapRuntime();
    const scheduler = new ManualFrameScheduler();
    const coordinator = createMapRuntimeCameraCoordinator(runtime, scheduler);

    const pending = coordinator.schedule(CAMERA_A);
    scheduler.runNext();

    await expect(pending).rejects.toMatchObject({
      name: "MapRuntimePortError",
      code: "MAP_RUNTIME_NOT_READY",
    });
    expect(runtime.cameraCalls).toEqual([CAMERA_A]);
  });

  it("cancels pending navigation on disposal and fails closed afterwards", async () => {
    const runtime = new CountingNullMapRuntime();
    await runtime.initialize();
    const scheduler = new ManualFrameScheduler();
    const coordinator = createMapRuntimeCameraCoordinator(runtime, scheduler);

    const pending = coordinator.schedule(CAMERA_A);
    coordinator.dispose();
    coordinator.dispose();

    await expect(pending).rejects.toMatchObject({
      name: "MapRuntimePortError",
      code: "MAP_RUNTIME_DISPOSED",
    });
    await expect(coordinator.schedule(CAMERA_B)).rejects.toMatchObject({
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
    expect(runtime.cameraCalls).toEqual([]);
  });
});
