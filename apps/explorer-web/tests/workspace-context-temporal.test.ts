import assert from "node:assert/strict";
import { describe, it } from "vitest";
import {
  buildTemporalViewStateFromPublicContext,
  PUBLIC_WORKSPACE_CONTEXT_PROFILE,
  PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM,
  parsePublicWorkspaceContext,
  parsePublicWorkspaceContextQuery,
  parsePublicWorkspaceContextUrl,
  serializePublicWorkspaceContext,
  withPublicWorkspaceContext,
  type PublicWorkspaceContext,
} from "../src/site/workspace-context";

// Synthetic public context only: no provider payload, evidence, or network.
const fixture: PublicWorkspaceContext = {
  profile: PUBLIC_WORKSPACE_CONTEXT_PROFILE,
  workspaceId: "explore",
  domainIds: [],
  placeIds: [],
  layerIds: ["layer:synthetic-temporal-regression"],
  camera: null,
  selection: null,
  time: {
    validAt: "2026-09-10T12:00:00Z",
    observedAt: null,
    asOf: null,
    releaseId: null,
  },
  compare: { mode: "NONE", leftContextId: null, rightContextId: null },
  storyNodeId: null,
  publicSafe: true,
};
const fields = ["validAt", "observedAt", "asOf"] as const;

function contextWith(
  field: (typeof fields)[number],
  raw: string | null,
): PublicWorkspaceContext {
  return { ...fixture, time: { ...fixture.time, [field]: raw } };
}

function uncheckedQuery(context: PublicWorkspaceContext): URLSearchParams {
  const params = new URLSearchParams();
  params.set(PUBLIC_WORKSPACE_CONTEXT_QUERY_PARAM, JSON.stringify(context));
  return params;
}

const invalidTimes = [
  "2026-02-29",
  "2026-02-30",
  "2026-02-31",
  "1900-02-29",
  "2100-02-29",
  "2026-04-31",
  "2026-06-31",
  "2026-09-31",
  "2026-11-31",
  "2026-00-10",
  "2026-13-10",
  "2026-09-00",
  "2026-09-32",
  "2026-02-30T12:34:56.123456789-05:00",
  "2026-09-10T24:00:00Z",
  "2026-09-10T24:00:00.000000000+05:30",
  "2026-09-10T12:60:00Z",
  "2026-09-10T12:00:60Z",
  "2026-09-10T12:00:00+24:00",
  "2026-09-10T12:00:00+05:60",
  "2026-09-10T12:00:00",
  "2026-09-10T12:00:00.1234567890Z",
];
const validTimes = [
  null,
  "2000-02-29",
  "2024-02-29",
  "0096-02-29",
  "0000-01-01",
  "9999-12-31",
  "2026-04-30",
  "2026-09-10T00:00:00Z",
  "2026-09-10T23:59:59Z",
  "2026-09-10T12:34:56.123456789+05:45",
  "2026-09-10T12:34:56.1-03:30",
  "2026-09-10T12:34:56+00:00",
  "2026-09-10T12:34:56-00:00",
];

describe("Public workspace temporal calendar and normalization boundaries", () => {
  for (const field of fields) {
    for (const raw of invalidTimes) {
      it(`rejects ${field}=${raw} at every context and URL boundary`, async () => {
        const context = contextWith(field, raw);
        const query = uncheckedQuery(context);
        const incoming = new URL(`https://example.test/explorer?${query}#map`);
        const base = new URL("https://example.test/explorer?lang=en#trust");
        const before = base.href;
        assert.equal(parsePublicWorkspaceContext(context), null);
        assert.equal(serializePublicWorkspaceContext(context), null);
        assert.equal(parsePublicWorkspaceContextQuery(query), null);
        assert.equal(parsePublicWorkspaceContextQuery(`?${query}`), null);
        assert.equal(parsePublicWorkspaceContextUrl(incoming), null);
        assert.equal(withPublicWorkspaceContext(base, context), null);
        assert.equal(base.href, before);
        assert.deepEqual(await buildTemporalViewStateFromPublicContext(context), {
          status: "ERROR", code: "PUBLIC_CONTEXT_INVALID", state: null,
        });
      });
    }
    for (const raw of validTimes) {
      it(`preserves the raw ${field}=${raw} through a URL round-trip`, () => {
        const context = contextWith(field, raw);
        const parsed = parsePublicWorkspaceContext(context);
        assert.ok(parsed);
        assert.equal(parsed.time[field], raw);
        const query = serializePublicWorkspaceContext(context);
        assert.ok(query);
        assert.deepEqual(parsePublicWorkspaceContextQuery(query), parsed);
        const url = withPublicWorkspaceContext(
          new URL("https://example.test/explorer?lang=en#trust"), context,
        );
        assert.ok(url);
        assert.equal(url.searchParams.get("lang"), "en");
        assert.equal(url.hash, "#map");
        assert.deepEqual(parsePublicWorkspaceContextUrl(url), parsed);
      });
    }
  }

  for (const field of fields) {
    for (const raw of [
      "0000-01-01T00:00:00+00:01",
      "9999-12-31T23:59:59.123456789-00:01",
    ]) {
      it(`withholds expanded-year normalization for ${field}=${raw}`, async () => {
        const original = contextWith(field, raw);
        const context = field === "observedAt"
          ? { ...original, time: { ...original.time, validAt: null } }
          : original;
        assert.ok(parsePublicWorkspaceContext(context));
        assert.deepEqual(await buildTemporalViewStateFromPublicContext(context), {
          status: "UNSUPPORTED", code: "NORMALIZED_YEAR_OUT_OF_RANGE", state: null,
        });
      });
    }
    it(`preserves the unknown-offset outcome for ${field}`, async () => {
      const original = contextWith(field, "2026-09-10T12:00:00-00:00");
      const context = field === "observedAt"
        ? { ...original, time: { ...original.time, validAt: null } }
        : original;
      assert.ok(parsePublicWorkspaceContext(original));
      assert.deepEqual(await buildTemporalViewStateFromPublicContext(context), {
        status: "UNSUPPORTED", code: "UNKNOWN_TIMEZONE", state: null,
      });
    });
  }

  const conversions = [
    ["2024-03-01T00:15:00.123456789+00:30", "2024-02-29T23:45:00.123456789Z"],
    ["2026-12-31T23:30:00-01:00", "2027-01-01T00:30:00Z"],
    ["0099-12-31T23:30:00-01:00", "0100-01-01T00:30:00Z"],
    ["0000-01-01T00:01:00+00:01", "0000-01-01T00:00:00Z"],
    ["9999-12-31T23:58:59-00:01", "9999-12-31T23:59:59Z"],
  ];
  for (const [raw, normalized] of conversions) {
    it(`normalizes the valid offset ${raw} without corrupting precision`, async () => {
      const result = await buildTemporalViewStateFromPublicContext(contextWith("validAt", raw));
      assert.equal(result.status, "SUPPORTED");
      assert.equal(result.state?.selection.start.raw, raw);
      assert.equal(result.state?.selection.start.normalized, normalized);
    });
  }
  for (let precision = 1; precision <= 9; precision += 1) {
    it(`preserves all ${precision} fractional digits`, async () => {
      const fraction = "123456789".slice(0, precision);
      const raw = `2026-09-10T12:00:00.${fraction}+05:45`;
      const result = await buildTemporalViewStateFromPublicContext(contextWith("validAt", raw));
      assert.equal(result.status, "SUPPORTED");
      assert.equal(result.state?.selection.start.raw, raw);
      assert.equal(result.state?.selection.start.normalized, `2026-09-10T06:15:00.${fraction}Z`);
    });
  }

  it("keeps date-only selection typed rather than inventing a midnight observation", async () => {
    const result = await buildTemporalViewStateFromPublicContext(contextWith("validAt", "2024-02-29"));
    assert.equal(result.status, "SUPPORTED");
    assert.equal(result.state?.selection.start.profile, "date_only");
    assert.equal(result.state?.selection.start.raw, "2024-02-29");
    assert.equal(result.state?.selection.start.normalized, null);
  });

  it("retains the existing zoned-instant requirement for the knowledge cutoff", async () => {
    assert.deepEqual(await buildTemporalViewStateFromPublicContext(contextWith("asOf", "2024-02-29")), {
      status: "UNSUPPORTED", code: "AS_OF_REQUIRES_ZONED_INSTANT", state: null,
    });
  });
});
