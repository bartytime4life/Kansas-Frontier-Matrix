import { describe, expect, it } from "vitest";

import invalidCandidate from "../../../fixtures/ui/source_availability_watchlist_projection/invalid/candidate-binding.json";
import invalidExtra from "../../../fixtures/ui/source_availability_watchlist_projection/invalid/extra-field.json";
import availableFixture from "../../../fixtures/ui/source_availability_watchlist_projection/valid/available.json";
import deniedFixture from "../../../fixtures/ui/source_availability_watchlist_projection/valid/denied.json";
import errorFixture from "../../../fixtures/ui/source_availability_watchlist_projection/valid/error.json";
import heldFixture from "../../../fixtures/ui/source_availability_watchlist_projection/valid/held.json";
import adapterSource from "../src/adapters/SourceAvailabilityWatchlistProjection.ts?raw";
import panelSource from "../src/features/source_availability_watchlist/index.ts?raw";
import { resolveSourceAvailabilityWatchlist } from "../src/features/source_availability_watchlist";

describe("Explorer source availability watchlist", () => {
  it("shows stable and material-change review routing without creating work", () => {
    const result = resolveSourceAvailabilityWatchlist(availableFixture);
    expect(result).toMatchObject({
      visibility: "VISIBLE",
      outcome: "ANSWER",
      code: "WATCHLIST_AVAILABLE",
      state: "REVIEW_REQUIRED",
      watchlistId: "kfm:source-availability-watchlist:0123456789abcdef01234567",
    });
    expect(result.entries).toHaveLength(2);
    expect(result.entries[0]).toMatchObject({
      sourceId: "ks-mesonet",
      route: "NO_ACTION",
      candidateWorkRef: null,
    });
    expect(result.entries[1]).toMatchObject({
      sourceId: "nrcs-ssurgo",
      route: "REVIEW_CANDIDATE",
      candidateWorkRef: "kfm://candidate-work/synthetic/nrcs-ssurgo-schema-001",
    });
    expect(result.summaryText).toContain("does not probe sources");
  });

  it("keeps unresolved availability visible as HOLD rather than guessing", () => {
    const result = resolveSourceAvailabilityWatchlist(heldFixture);
    expect(result).toMatchObject({
      visibility: "VISIBLE",
      outcome: "ANSWER",
      state: "HOLD",
    });
    expect(result.entries[0]).toMatchObject({
      availability: "UNKNOWN",
      route: "HOLD",
    });
  });

  it.each([
    [deniedFixture, "DENY", "POLICY_DENIED"],
    [errorFixture, "ERROR", "UPSTREAM_ERROR"],
  ] as const)("renders fixed %s state without source detail", (fixture, outcome, code) => {
    const result = resolveSourceAvailabilityWatchlist(fixture);
    expect(result).toMatchObject({
      visibility: "VISIBLE",
      outcome,
      code,
      entries: [],
      watchlistId: null,
    });
    expect(JSON.stringify(result)).not.toContain("kfm://source/");
  });

  it.each([invalidExtra, invalidCandidate])(
    "fails closed on unknown fields or candidate-binding contradictions",
    (fixture) => {
      const result = resolveSourceAvailabilityWatchlist(fixture);
      expect(result).toMatchObject({
        visibility: "HIDDEN",
        code: "INVALID_PAYLOAD",
        entries: [],
      });
      expect(JSON.stringify(result)).not.toContain(
        "SOURCE_WATCHLIST_INTERNAL_CANARY_41d8e2",
      );
    },
  );

  it("renders nothing without a governed response", () => {
    expect(resolveSourceAvailabilityWatchlist()).toMatchObject({
      visibility: "HIDDEN",
      code: "NO_GOVERNED_RESPONSE",
    });
  });

  it("contains no transport, persistence, lifecycle-store, policy, work execution, or model access", () => {
    const source = `${adapterSource}\n${panelSource}`;
    expect(source).not.toMatch(/\bfetch\s*\(/);
    expect(source).not.toMatch(/\b(?:localStorage|sessionStorage)\b/);
    expect(source).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
    expect(source).not.toMatch(/(?:ollama|model[-_ ]?runtime)/i);
    expect(source).not.toMatch(/(?:executeCandidate|activateSource|authorizeRelease)\s*\(/);
  });
});
