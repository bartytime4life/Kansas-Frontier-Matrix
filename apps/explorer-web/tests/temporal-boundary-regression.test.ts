import { describe, expect, it } from "vitest";
import snapshot from "../../../fixtures/contracts/v1/common/temporal_view_state/valid/valid_snapshot.json";
import {
  normalizeTemporalBoundary,
  normalizeTemporalQuery,
  type TemporalBoundaryProfile,
} from "../src/features/temporal";

const calendarCases = [
  ["date_only", "2024-01-01", "2024-02-01"],
  ["month", "2024-01", "2024-02"],
  ["year", "2023", "2024"],
] as const;

function windowState(profile: TemporalBoundaryProfile, start: unknown, end: unknown) {
  return {
    ...snapshot,
    selection: {
      ...snapshot.selection,
      selection_mode: "WINDOW",
      start: { ...snapshot.selection.start, profile, raw: start, normalized: null },
      end: { ...snapshot.selection.start, profile, raw: end, normalized: null },
    },
  };
}

describe("temporal boundary narrowing regressions", () => {
  it.each(calendarCases)("preserves %s precision and rejects invented normalization", (profile, raw) => {
    expect(normalizeTemporalBoundary({ profile, raw, normalized: null })).toEqual({
      status: "SUPPORTED", code: "CALENDAR_PRESERVED", profile, raw, normalized: null,
    });
    expect(normalizeTemporalBoundary({ profile, raw, normalized: "2024-01-01T00:00:00Z" }))
      .toMatchObject({ status: "ERROR", code: "NORMALIZED_PRECISION_VIOLATION" });
  });

  it.each(calendarCases)("orders %s windows without null coercion", async (profile, earlier, later) => {
    for (const [start, end] of [[earlier, later], [earlier, earlier]]) {
      await expect(normalizeTemporalQuery(windowState(profile, start, end)))
        .resolves.toMatchObject({ status: "SUPPORTED", code: "OK" });
    }
    await expect(normalizeTemporalQuery(windowState(profile, later, earlier)))
      .resolves.toMatchObject({ status: "ERROR", code: "REVERSED_INTERVAL", queryId: null });
    for (const missing of [null, undefined, "", 0]) {
      for (const [start, end] of [[missing, earlier], [earlier, missing]]) {
        await expect(normalizeTemporalQuery(windowState(profile, start, end)))
          .resolves.toMatchObject({ status: "ERROR", code: "BOUNDARY_RAW_REQUIRED", queryId: null });
      }
    }
  });

  it.each([null, undefined, 1, "", "DATE_ONLY", "not_a_profile"])("rejects an unrecognized profile: %s", (profile) => {
    expect(normalizeTemporalBoundary({ profile, raw: "2024", normalized: null }))
      .toMatchObject({ status: "ERROR", code: "BOUNDARY_PROFILE_INVALID", profile: null });
  });

  it("preserves unsupported outcomes rather than treating them as ordered windows", async () => {
    expect(normalizeTemporalBoundary({ profile: "instant", raw: "2024-01-01T00:00:00", normalized: null }))
      .toMatchObject({ status: "UNSUPPORTED", code: "UNKNOWN_TIMEZONE" });
    expect(normalizeTemporalBoundary({ profile: "geologic_age", raw: "120 Ma", normalized: null }))
      .toMatchObject({ status: "UNSUPPORTED", code: "UNSUPPORTED_PROFILE" });
    await expect(normalizeTemporalQuery(windowState("uncertain_range", "1900?", "1910?")))
      .resolves.toMatchObject({ status: "UNSUPPORTED", code: "UNCERTAIN_ORDERING" });
  });
});
