import { describe, expect, it } from "vitest";

import fixture from "../../../fixtures/ui/acs_population_context/acs-2024-dp05-bounded.json";
import adapterSource from "../src/adapters/AcsPopulationContextAdapter.ts?raw";
import { reconcileAcsPopulationContext } from "../src/adapters/AcsPopulationContextAdapter";

const counties = Object.freeze([
  Object.freeze({ geoid: "20053", name: "Ellsworth County" }),
  Object.freeze({ geoid: "20169", name: "Saline County" }),
]);

describe("ACS population context reconciliation", () => {
  it("joins the pinned aggregate estimate by exact GEOID without evidence authority", () => {
    const output = reconcileAcsPopulationContext(counties, fixture);
    expect(output).toHaveLength(2);
    expect(output[0]).toMatchObject({
      state: "JOINED", geoid: "20053", population: 6242,
      sourceRole: "EXTERNAL_CONTEXT_ONLY",
      knowledgeCharacter: "AGGREGATE_ESTIMATE",
      evidenceRefs: [], reportEligible: false, exportEligible: false,
    });
  });

  it("does not convert an empty or unavailable response into zero population", () => {
    const empty = reconcileAcsPopulationContext(counties, { ...fixture, rows: [] });
    const unavailable = reconcileAcsPopulationContext(counties, { ...fixture, status: "UNAVAILABLE" });
    expect(empty).toEqual([expect.objectContaining({ state: "EMPTY_RESPONSE", population: null })]);
    expect(unavailable).toEqual([expect.objectContaining({ state: "UNAVAILABLE", population: null })]);
  });

  it("fails closed on stale or unexpected vintage", () => {
    expect(reconcileAcsPopulationContext(counties, fixture, { stale: true })[0]).toMatchObject({ state: "STALE_VINTAGE", population: null });
    expect(reconcileAcsPopulationContext(counties, { ...fixture, vintage: "2023" })[0]).toMatchObject({ state: "UNEXPECTED_VINTAGE", population: null });
  });

  it("fails closed when the saved Sites comparison checkpoint drifts", () => {
    expect(reconcileAcsPopulationContext(counties, { ...fixture, sites_source_commit: "0".repeat(40) })[0]).toMatchObject({
      state: "SOURCE_CHECKPOINT_MISMATCH", population: null,
    });
  });

  it("keeps missing, unmatched, duplicate, and malformed GEOIDs explicit", () => {
    const input = {
      ...fixture,
      rows: [
        { GEOID: "20053", DP05_0001E: "6242" },
        { GEOID: "20053", DP05_0001E: "6242" },
        { GEOID: "20999", DP05_0001E: "5" },
        { GEOID: "20169", DP05_0001E: "unknown" },
      ],
    };
    expect(reconcileAcsPopulationContext([...counties, { geoid: "20001", name: "Allen County" }], input).map((item) => item.state)).toEqual([
      "JOINED", "DUPLICATE_GEOID", "UNMATCHED_GEOID", "MALFORMED_ESTIMATE", "MISSING_ACS_ROW",
    ]);
  });

  it("contains no network, storage, evidence resolution, report, export, or lifecycle mutation path", () => {
    expect(adapterSource).not.toMatch(/\bfetch\s*\(/);
    expect(adapterSource).not.toMatch(/\b(?:localStorage|sessionStorage)\b/);
    expect(adapterSource).not.toMatch(/(?:resolveEvidence|createReport|exportData|admitSource|authorizeRelease|publishArtifact)\s*\(/);
    expect(adapterSource).not.toMatch(/https?:\/\//);
  });
});
