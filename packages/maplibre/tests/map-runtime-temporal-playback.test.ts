import { describe, expect, it } from "vitest";

import {
  MAP_RUNTIME_TEMPORAL_PLAYBACK_PROFILE,
  MapRuntimeTemporalPlaybackError,
  createMapRuntimeTemporalPlayback,
  type MapRuntimeTemporalScheduler,
} from "../src/map-runtime-temporal-playback";

function createScheduler() {
  let nextHandle = 1;
  const callbacks = new Map<number, () => void>();
  const delays = new Map<number, number>();
  const scheduler: MapRuntimeTemporalScheduler = {
    request(callback, delayMs) {
      const handle = nextHandle++;
      callbacks.set(handle, callback);
      delays.set(handle, delayMs);
      return handle;
    },
    cancel(handle) {
      callbacks.delete(handle);
      delays.delete(handle);
    },
  };
  return {
    scheduler,
    get size() {
      return callbacks.size;
    },
    nextDelay() {
      return delays.values().next().value as number | undefined;
    },
    runNext() {
      const entry = callbacks.entries().next().value as [number, () => void] | undefined;
      if (!entry) throw new Error("no scheduled callback");
      callbacks.delete(entry[0]);
      delays.delete(entry[0]);
      entry[1]();
    },
  };
}

describe("map runtime temporal playback", () => {
  it("advances a finite aligned timeline and stops exactly at the end", () => {
    const fake = createScheduler();
    const playback = createMapRuntimeTemporalPlayback(
      { startMs: 1_000, endMs: 4_000, stepMs: 1_000, frameDelayMs: 20 },
      fake.scheduler,
    );

    expect(playback.getSnapshot()).toMatchObject({
      profile: MAP_RUNTIME_TEMPORAL_PLAYBACK_PROFILE,
      state: "PAUSED",
      cursorMs: 1_000,
    });
    expect(playback.play().state).toBe("PLAYING");
    expect(fake.size).toBe(1);
    expect(fake.nextDelay()).toBe(20);

    fake.runNext();
    expect(playback.getSnapshot()).toMatchObject({ state: "PLAYING", cursorMs: 2_000 });
    fake.runNext();
    expect(playback.getSnapshot()).toMatchObject({ state: "PLAYING", cursorMs: 3_000 });
    fake.runNext();
    expect(playback.getSnapshot()).toMatchObject({ state: "ENDED", cursorMs: 4_000 });
    expect(fake.size).toBe(0);
  });

  it("supports deterministic seek, step, loop, and pause behavior", () => {
    const fake = createScheduler();
    const playback = createMapRuntimeTemporalPlayback(
      { startMs: -2_000, endMs: 2_000, stepMs: 1_000, loop: true },
      fake.scheduler,
    );

    expect(playback.seek(2_000).cursorMs).toBe(2_000);
    expect(playback.step(1)).toMatchObject({ state: "PAUSED", cursorMs: -2_000 });
    expect(playback.step(-1).cursorMs).toBe(2_000);
    playback.play();
    expect(fake.size).toBe(1);
    expect(playback.pause().state).toBe("PAUSED");
    expect(fake.size).toBe(0);
  });

  it("fails closed on malformed or misaligned timelines and cursors", () => {
    expect(() =>
      createMapRuntimeTemporalPlayback({ startMs: 0, endMs: 10, stepMs: 3 }),
    ).toThrowError(MapRuntimeTemporalPlaybackError);

    const playback = createMapRuntimeTemporalPlayback({
      startMs: 0,
      endMs: 10_000,
      stepMs: 1_000,
    });
    expect(() => playback.seek(1_500)).toThrowError(
      expect.objectContaining({ code: "MAP_RUNTIME_TEMPORAL_INVALID" }),
    );
  });

  it("isolates throwing listeners from later listeners and playback", () => {
    const fake = createScheduler();
    const playback = createMapRuntimeTemporalPlayback(
      { startMs: 0, endMs: 2_000, stepMs: 1_000 },
      fake.scheduler,
    );
    const observed: number[] = [];
    playback.subscribe(() => {
      throw new Error("consumer fault");
    });
    playback.subscribe((snapshot) => observed.push(snapshot.cursorMs));

    playback.play();
    fake.runNext();
    fake.runNext();

    expect(observed).toEqual([0, 1_000, 2_000]);
    expect(playback.getSnapshot().state).toBe("ENDED");
  });

  it("contains stale callbacks after pause/dispose and rejects later mutation", () => {
    let stale: (() => void) | null = null;
    const scheduler: MapRuntimeTemporalScheduler = {
      request(callback) {
        stale = callback;
        return 1;
      },
      cancel() {},
    };
    const playback = createMapRuntimeTemporalPlayback(
      { startMs: 0, endMs: 2_000, stepMs: 1_000 },
      scheduler,
    );

    playback.play();
    playback.pause();
    stale?.();
    expect(playback.getSnapshot()).toMatchObject({ state: "PAUSED", cursorMs: 0 });

    playback.play();
    playback.dispose();
    stale?.();
    expect(playback.getSnapshot().state).toBe("DISPOSED");
    expect(() => playback.seek(1_000)).toThrowError(
      expect.objectContaining({ code: "MAP_RUNTIME_TEMPORAL_DISPOSED" }),
    );
  });

  it("normalizes scheduler startup failure to a finite playback error", () => {
    const playback = createMapRuntimeTemporalPlayback(
      { startMs: 0, endMs: 1_000, stepMs: 1_000 },
      {
        request() {
          throw new Error("scheduler failed");
        },
        cancel() {},
      },
    );

    expect(() => playback.play()).toThrowError(
      expect.objectContaining({ code: "MAP_RUNTIME_TEMPORAL_SCHEDULER_FAILED" }),
    );
    expect(playback.getSnapshot().state).toBe("PAUSED");
  });
});
