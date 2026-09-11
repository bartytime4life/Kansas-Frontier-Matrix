/**
 * Renderer-neutral, deterministic replay policy for finite atlas frames.
 *
 * This module owns playback state transitions only. It deliberately does not
 * own a timer, fetch a source, interpolate values, loop across a boundary, or
 * decide whether a frame is released. The caller supplies an already-bounded
 * ordered frame-id list and may use the reducer from a browser or a test.
 */
export const PLAYBACK_STATUSES = ["PAUSED", "PLAYING"] as const;
export type PlaybackStatus = (typeof PLAYBACK_STATUSES)[number];

export const PLAYBACK_PAUSE_REASONS = [
  "INITIAL",
  "USER",
  "USER_STEP",
  "SCRUB",
  "HIDDEN_DOCUMENT",
  "REDUCED_MOTION",
  "BOUNDARY",
  "END_OF_TIMELINE",
  "NO_FRAMES",
  "EVIDENCE_FAILURE",
  "SOURCE_WITHDRAWN",
] as const;
export type PlaybackPauseReason = (typeof PLAYBACK_PAUSE_REASONS)[number];

export type PlaybackState = Readonly<{
  status: PlaybackStatus;
  index: number;
  pauseReason: PlaybackPauseReason | null;
  reducedMotion: boolean;
}>;

export type PlaybackAction =
  | Readonly<{ type: "PLAY" }>
  | Readonly<{ type: "PAUSE"; reason?: PlaybackPauseReason }>
  | Readonly<{ type: "STEP"; delta: -1 | 1 }>
  | Readonly<{ type: "SCRUB"; index: number }>
  | Readonly<{ type: "TICK" }>
  | Readonly<{ type: "VISIBILITY_HIDDEN" }>
  | Readonly<{ type: "SET_REDUCED_MOTION"; enabled: boolean }>
  | Readonly<{ type: "RESET"; index: number }>;

function clampIndex(frameIds: readonly string[], index: number): number {
  if (frameIds.length === 0 || !Number.isFinite(index)) return 0;
  return Math.min(frameIds.length - 1, Math.max(0, Math.trunc(index)));
}

function freezeState(state: PlaybackState): PlaybackState {
  return Object.freeze(state);
}

export function createInitialPlayback(
  frameIds: readonly string[],
  initialIndex = 0,
  reducedMotion = false,
): PlaybackState {
  const index = clampIndex(frameIds, initialIndex);
  return freezeState({
    status: "PAUSED",
    index,
    pauseReason: frameIds.length === 0
      ? "NO_FRAMES"
      : reducedMotion
        ? "REDUCED_MOTION"
        : "INITIAL",
    reducedMotion,
  });
}

export function reducePlayback(
  state: PlaybackState,
  frameIds: readonly string[],
  action: PlaybackAction,
): PlaybackState {
  const index = clampIndex(frameIds, state.index);
  const maxIndex = Math.max(0, frameIds.length - 1);
  const normalized = index === state.index
    ? state
    : freezeState({ ...state, index });

  switch (action.type) {
    case "PLAY": {
      if (frameIds.length === 0) {
        return freezeState({
          ...normalized,
          status: "PAUSED",
          pauseReason: "NO_FRAMES",
        });
      }
      if (normalized.reducedMotion) {
        return freezeState({
          ...normalized,
          status: "PAUSED",
          pauseReason: "REDUCED_MOTION",
        });
      }
      if (normalized.index >= maxIndex) {
        return freezeState({
          ...normalized,
          status: "PAUSED",
          pauseReason: "END_OF_TIMELINE",
        });
      }
      if (normalized.status === "PLAYING") return normalized;
      return freezeState({
        ...normalized,
        status: "PLAYING",
        pauseReason: null,
      });
    }

    case "PAUSE":
      return freezeState({
        ...normalized,
        status: "PAUSED",
        pauseReason: action.reason ?? "USER",
      });

    case "STEP": {
      if (frameIds.length === 0) {
        return freezeState({
          ...normalized,
          status: "PAUSED",
          pauseReason: "NO_FRAMES",
        });
      }
      const nextIndex = clampIndex(frameIds, normalized.index + action.delta);
      return freezeState({
        ...normalized,
        status: "PAUSED",
        index: nextIndex,
        pauseReason: nextIndex === normalized.index
          ? "BOUNDARY"
          : "USER_STEP",
      });
    }

    case "SCRUB":
      return freezeState({
        ...normalized,
        status: "PAUSED",
        index: clampIndex(frameIds, action.index),
        pauseReason: "SCRUB",
      });

    case "TICK": {
      if (normalized.status !== "PLAYING") return normalized;
      if (frameIds.length === 0) {
        return freezeState({
          ...normalized,
          status: "PAUSED",
          pauseReason: "NO_FRAMES",
        });
      }
      if (normalized.index >= maxIndex) {
        return freezeState({
          ...normalized,
          status: "PAUSED",
          pauseReason: "END_OF_TIMELINE",
        });
      }
      return freezeState({
        ...normalized,
        index: normalized.index + 1,
        pauseReason: null,
      });
    }

    case "VISIBILITY_HIDDEN":
      return freezeState({
        ...normalized,
        status: "PAUSED",
        pauseReason: "HIDDEN_DOCUMENT",
      });

    case "SET_REDUCED_MOTION":
      if (action.enabled) {
        return freezeState({
          ...normalized,
          status: "PAUSED",
          pauseReason: "REDUCED_MOTION",
          reducedMotion: true,
        });
      }
      return freezeState({
        ...normalized,
        pauseReason: normalized.pauseReason === "REDUCED_MOTION"
          ? "INITIAL"
          : normalized.pauseReason,
        reducedMotion: false,
      });

    case "RESET":
      return createInitialPlayback(
        frameIds,
        action.index,
        normalized.reducedMotion,
      );
  }
}

export function isPlaybackPlaying(state: PlaybackState): boolean {
  return state.status === "PLAYING";
}

export function playbackFrameId(
  state: PlaybackState,
  frameIds: readonly string[],
): string | null {
  return frameIds[clampIndex(frameIds, state.index)] ?? null;
}

export function playbackHasNext(
  state: PlaybackState,
  frameIds: readonly string[],
): boolean {
  return frameIds.length > 0 && state.index < frameIds.length - 1;
}
