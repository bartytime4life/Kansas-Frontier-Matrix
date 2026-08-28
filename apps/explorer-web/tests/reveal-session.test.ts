import { describe, expect, it } from "vitest";

import activeFixture from "../../../fixtures/ui/reveal_session_projection/valid/active.json";
import denyFixture from "../../../fixtures/ui/reveal_session_projection/valid/deny.json";
import invalidExtraFieldFixture from "../../../fixtures/ui/reveal_session_projection/invalid/extra-field.json";
import invalidTtlFixture from "../../../fixtures/ui/reveal_session_projection/invalid/ttl-too-long.json";
import adapterSource from "../src/adapters/RevealSessionProjection.ts?raw";
import featureSource from "../src/features/reveal_session/index.ts?raw";
import { parseRevealSessionProjection } from "../src/adapters/RevealSessionProjection";
import {
  createRevealSessionController,
  resolveRevealSession,
  type RevealSessionClock,
} from "../src/features/reveal_session";

class ManualClock implements RevealSessionClock {
  private current: number;
  private nextHandle = 1;
  private readonly timers = new Map<
    number,
    Readonly<{ at: number; callback: () => void }>
  >();

  constructor(now: string) {
    this.current = Date.parse(now);
  }

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

const FIXED_NOW = "2026-08-10T14:59:55Z";

describe("Explorer reveal session HUD", () => {
  it("projects fixed scope labels and a whole-second countdown", () => {
    expect(resolveRevealSession(activeFixture, { now: FIXED_NOW })).toEqual(
      expect.objectContaining({
        outcome: "ANSWER",
        code: "REVEAL_ACTIVE",
        status: "ACTIVE",
        remainingSeconds: 5,
        timerLabel: "Time remaining: 00:05",
        scopeLabels: [
          "Generalized display only",
          "Export is disabled",
          "Redistribution is prohibited",
          "Restricted steward session",
        ],
        canRevoke: true,
      }),
    );
  });

  it("discards the local reference and attempts every teardown effect in order", () => {
    const clock = new ManualClock(FIXED_NOW);
    const effects: string[] = [];
    const controller = createRevealSessionController(activeFixture, {
      clock,
      onDiscardKeyMaterial(reference) {
        effects.push(`discard:${reference}`);
      },
      onOverlayVisibilityChange() {
        effects.push("remove-overlay");
      },
      onRestoreObfuscatedState(layerRef) {
        effects.push(`restore:${layerRef}`);
      },
      onFinalizeAudit(event) {
        effects.push(`audit:${event.cause}`);
        expect(event.localKeyReferenceDiscarded).toBe(true);
        expect(event.authority).toBe("NONE");
      },
    });

    clock.advance(5_000);

    expect(controller.state).toMatchObject({
      outcome: "ABSTAIN",
      code: "REVEAL_EXPIRED",
      status: "EXPIRED",
      remainingSeconds: 0,
      canRevoke: false,
      teardownStatus: "COMPLETE",
    });
    expect(effects).toEqual([
      "discard:kfm://key-handle/synthetic/reveal-001",
      "remove-overlay",
      "restore:kfm://layer/synthetic/restricted-generalized-overlay",
      "audit:TTL_EXPIRED",
    ]);
    expect(controller.revoke()).toBe(false);
  });

  it("does not let a failed key-store callback skip later teardown actions", () => {
    const clock = new ManualClock(FIXED_NOW);
    const effects: string[] = [];
    const controller = createRevealSessionController(activeFixture, {
      clock,
      onDiscardKeyMaterial() {
        effects.push("discard-attempted");
        throw new Error("synthetic key-store failure");
      },
      onOverlayVisibilityChange() {
        effects.push("remove-overlay");
      },
      onRestoreObfuscatedState() {
        effects.push("restore-obfuscated");
      },
      onFinalizeAudit(event) {
        effects.push("audit-attempted");
        expect(event.unresolvedActionsBeforeAudit).toEqual([
          "DISCARD_KEY_MATERIAL",
        ]);
      },
    });

    clock.advance(5_000);

    expect(effects).toEqual([
      "discard-attempted",
      "remove-overlay",
      "restore-obfuscated",
      "audit-attempted",
    ]);
    expect(controller.state).toMatchObject({
      status: "EXPIRED",
      teardownStatus: "INCOMPLETE",
      canRevoke: false,
    });
  });

  it("uses the same fail-closed teardown path for viewer revocation", () => {
    const clock = new ManualClock(FIXED_NOW);
    const causes: string[] = [];
    const controller = createRevealSessionController(activeFixture, {
      clock,
      onDiscardKeyMaterial() {},
      onOverlayVisibilityChange() {},
      onRestoreObfuscatedState() {},
      onFinalizeAudit(event) {
        causes.push(event.cause);
      },
    });

    expect(controller.revoke()).toBe(true);
    expect(controller.state).toMatchObject({
      code: "REVEAL_REVOKED",
      status: "REVOKED",
      teardownStatus: "COMPLETE",
    });
    expect(causes).toEqual(["VIEWER_REVOKED"]);
  });

  it("rejects unknown detail and intervals longer than 24 hours", () => {
    for (const fixture of [invalidExtraFieldFixture, invalidTtlFixture]) {
      expect(parseRevealSessionProjection(fixture)).toEqual({
        ok: false,
        code: "MALFORMED_REVEAL_SESSION_PROJECTION",
      });
      expect(resolveRevealSession(fixture, { now: FIXED_NOW })).toMatchObject({
        outcome: "ERROR",
        code: "INVALID_PAYLOAD",
        canRevoke: false,
      });
    }
    expect(JSON.stringify(resolveRevealSession(invalidExtraFieldFixture))).not.toContain(
      "SENSITIVE_REVEAL_CANARY_82f7",
    );
  });

  it("keeps policy denial detail-free and exposes no revoke override", () => {
    expect(resolveRevealSession(denyFixture, { now: FIXED_NOW })).toMatchObject({
      outcome: "DENY",
      code: "POLICY_DENIED",
      scopeLabels: [],
      remainingSeconds: 0,
      canRevoke: false,
    });
  });

  it("keeps adapter and feature code free of transport and lifecycle-store reads", () => {
    const source = `${adapterSource}\n${featureSource}`;
    expect(source).not.toMatch(/\bfetch\s*\(/);
    expect(source).not.toMatch(/XMLHttpRequest|WebSocket/);
    expect(source).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
    expect(source).not.toMatch(
      /\bAuthorization\b|BEGIN (?:RSA )?PRIVATE KEY|\.(?:vcf|fasta)\b/i,
    );
  });
});
