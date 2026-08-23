import { describe, expect, it } from "vitest";
import trustPrimitiveSource from "../src/site/trust-state-primitives.ts?raw";
import trustSurfaceSource from "../src/site/trust-surface.ts?raw";
import { resolveEvidenceDrawer } from "../src/features/evidence_drawer";
import { resolveTrustHeader } from "../src/features/trust_header";
import {
  TRUST_STATE_PRIMITIVE_PROFILE,
  resolveTrustStateSummary,
} from "../src/site/trust-state-primitives";
import {
  PUBLIC_TRUST_CASE_IDS,
  PUBLIC_TRUST_SURFACE_CASES,
  findPublicTrustSurfaceCase,
  resolvePublicTrustSurfaceCase,
} from "../src/site/trust-surface";

describe("Unified Workspace public trust surface", () => {
  it("registers one deterministic case for every bounded public trust state", () => {
    expect(PUBLIC_TRUST_SURFACE_CASES.map((entry) => entry.id)).toEqual(
      PUBLIC_TRUST_CASE_IDS,
    );
    expect(new Set(PUBLIC_TRUST_CASE_IDS).size).toBe(
      PUBLIC_TRUST_CASE_IDS.length,
    );
    expect(findPublicTrustSurfaceCase("admin")).toBeNull();
  });

  it("uses the same six text-first labels for every supported finite fixture", () => {
    for (const entry of PUBLIC_TRUST_SURFACE_CASES) {
      const resolved = resolvePublicTrustSurfaceCase(entry.id);
      expect(resolved).not.toBeNull();
      expect(resolved?.state.valid).toBe(true);
      expect(resolved?.state.badges.map((badge) => badge.label)).toEqual([
        "Outcome",
        "Evidence",
        "Freshness",
        "Sensitivity",
        "Release",
        "Correction",
      ]);
      expect(resolved?.state.accessibilityLabel).toContain(
        entry.summary.outcome.toLocaleLowerCase(),
      );
    }
  });

  it("keeps existing governed projections aligned with the shared outcome", () => {
    for (const entry of PUBLIC_TRUST_SURFACE_CASES) {
      if (entry.governedProjection === undefined) continue;
      const summary = resolveTrustStateSummary(entry.summary);
      const drawer = resolveEvidenceDrawer(entry.governedProjection);
      const header = resolveTrustHeader(entry.governedProjection);

      expect(drawer.outcome).toBe(summary.outcome);
      expect(header.visibility).toBe("VISIBLE");
      expect(header.state).toBe(
        summary.outcome === "ANSWER" ? "SUPPORTED" : summary.outcome,
      );
    }
  });

  it("distinguishes transient loading from a governed finite outcome", () => {
    const loading = resolvePublicTrustSurfaceCase("loading");
    expect(loading?.state).toMatchObject({
      outcome: "LOADING",
      ariaBusy: true,
      role: "status",
    });
    expect(loading?.entry.governedProjection).toBeUndefined();
  });

  it("fails closed on extra, malformed, or inconsistent presentation metadata", () => {
    const supported = findPublicTrustSurfaceCase("supported");
    expect(supported).not.toBeNull();

    const extraField = resolveTrustStateSummary({
      ...(supported?.summary ?? {}),
      prompt: "PRIVATE_PROMPT_CANARY_3e8f1a",
    });
    const inconsistent = resolveTrustStateSummary({
      profile: TRUST_STATE_PRIMITIVE_PROFILE,
      caseId: "bad-answer",
      outcome: "ANSWER",
      evidence: "UNRESOLVED",
      freshness: "UNKNOWN",
      sensitivity: "UNKNOWN",
      release: "UNRELEASED",
      correction: "NONE",
      title: "Bad answer",
      message: "This combination must not render as support.",
    });

    expect(extraField).toMatchObject({
      valid: false,
      code: "INVALID_TRUST_STATE",
      outcome: "ERROR",
    });
    expect(inconsistent.valid).toBe(false);
    expect(JSON.stringify(extraField)).not.toContain(
      "PRIVATE_PROMPT_CANARY_3e8f1a",
    );
  });

  it("contains no transport, persistence, lifecycle-store, policy mutation, or model access", () => {
    const source = `${trustPrimitiveSource}\n${trustSurfaceSource}`;
    expect(source).not.toMatch(/\bfetch\s*\(/);
    expect(source).not.toMatch(/\b(?:localStorage|sessionStorage)\b/);
    expect(source).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
    expect(source).not.toMatch(/(?:ollama|model[-_ ]?runtime)/i);
    expect(source).not.toMatch(/(?:approve|promote|publish)\s*\(/i);
  });
});
