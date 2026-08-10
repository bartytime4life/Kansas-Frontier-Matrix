import activeFixture from "../../../../fixtures/ui/reveal_session_projection/valid/active.json";
import denyFixture from "../../../../fixtures/ui/reveal_session_projection/valid/deny.json";
import invalidFixture from "../../../../fixtures/ui/reveal_session_projection/invalid/extra-field.json";
import {
  mountRevealSessionHud,
  type RevealSessionClock,
} from "../../src/features/reveal_session";

class BrowserManualClock implements RevealSessionClock {
  private current = Date.parse("2026-08-10T14:59:55Z");
  private nextHandle = 1;
  private readonly timers = new Map<
    number,
    Readonly<{ at: number; callback: () => void }>
  >();

  now = (): number => this.current;

  setTimer = (callback: () => void, delayMs: number): number => {
    const handle = this.nextHandle++;
    this.timers.set(handle, {
      at: this.current + Math.max(0, delayMs),
      callback,
    });
    return handle;
  };

  clearTimer = (handle: unknown): void => {
    if (typeof handle === "number") this.timers.delete(handle);
  };

  advance(milliseconds: number): void {
    const target = this.current + milliseconds;
    while (true) {
      const due = [...this.timers.entries()]
        .filter(([, timer]) => timer.at <= target)
        .sort((left, right) => left[1].at - right[1].at)[0];
      if (due === undefined) break;
      const [handle, timer] = due;
      this.timers.delete(handle);
      this.current = timer.at;
      timer.callback();
    }
    this.current = target;
  }
}

declare global {
  interface Window {
    __advanceRevealClock: (milliseconds: number) => void;
    __revealEffects: readonly string[];
  }
}

const root = document.querySelector<HTMLElement>("#fixture-root");
const visibility = document.querySelector<HTMLElement>("[data-layer-visible]");
const eventLog = document.querySelector<HTMLElement>("[data-event-log]");
if (root === null || visibility === null || eventLog === null) {
  throw new Error("Reveal session fixture surface is incomplete.");
}
const fixtureRoot = root as HTMLElement;
const visibilityStatus = visibility as HTMLElement;
const callerEventLog = eventLog as HTMLElement;

const requested = new URL(window.location.href).searchParams.get("fixture");
const input =
  requested === "deny"
    ? denyFixture
    : requested === "invalid"
      ? invalidFixture
      : activeFixture;
const clock = new BrowserManualClock();
const effects: string[] = [];
visibilityStatus.textContent = `Overlay visible: ${String(requested !== "deny" && requested !== "invalid")}`;

function record(value: string): void {
  effects.push(value);
  window.__revealEffects = Object.freeze([...effects]);
  callerEventLog.textContent = JSON.stringify(effects);
}

mountRevealSessionHud(fixtureRoot, input, {
  clock,
  onDiscardKeyMaterial(reference) {
    record(`DISCARD_KEY_MATERIAL:${reference}`);
  },
  onOverlayVisibilityChange(visible) {
    visibilityStatus.textContent = `Overlay visible: ${String(visible)}`;
    record("REMOVE_OVERLAY");
  },
  onRestoreObfuscatedState(layerRef) {
    record(`RESTORE_OBFUSCATED_STATE:${layerRef}`);
  },
  onFinalizeAudit(event) {
    record(`FINALIZE_AUDIT:${event.cause}`);
  },
});

window.__revealEffects = Object.freeze([...effects]);
window.__advanceRevealClock = (milliseconds: number): void => {
  clock.advance(milliseconds);
};
