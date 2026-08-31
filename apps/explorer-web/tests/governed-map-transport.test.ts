import { describe, expect, it, vi } from "vitest";

import answerFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/answer-corrected.json";
import abstainFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/abstain-stale.json";
import denyFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/deny-sensitive.json";
import {
  GOVERNED_LAYER_SLICE_PROFILE,
  INLINE_GEOJSON_LAYER_PROFILE,
  createGovernedHttpTransport,
  parseGovernedLayerSlice,
} from "../src/adapters/GovernedClient";
import { resolveEvidenceDrawer } from "../src/features/evidence_drawer";

const selection = Object.freeze({
  profile: "kfm.explorer.map-feature-selection.v1" as const,
  selectionId: "selection:flow-001",
  layerId: "layer:synthetic-streamflow",
  featureId: "feature:flow-001",
  evidenceRefs: Object.freeze(["kfm:evidence:synthetic:flow-001"]),
});

describe("Governed evidence outcome partition", () => {
  it.each([
    "POLICY_DENIED",
    "RIGHTS_UNRESOLVED",
    "SENSITIVE_DETAIL_RESTRICTED",
  ] as const)(
    "rejects the DENY-only %s reason on ABSTAIN without leaking evidence refs",
    (reasonCode) => {
      const forbiddenEvidenceRef =
        "kfm:evidence:private:abstain-reason-mismatch-canary";
      const mismatched = {
        ...abstainFixture,
        reason_code: reasonCode,
        evidence_refs: [forbiddenEvidenceRef],
      };

      const result = resolveEvidenceDrawer(mismatched);
      expect(result).toMatchObject({
        outcome: "ERROR",
        code: "INVALID_PAYLOAD",
        evidenceRefs: [],
      });
      expect(JSON.stringify(result)).not.toContain(forbiddenEvidenceRef);
    },
  );

  it.each([
    "MISSING_EVIDENCE",
    "STALE_EVIDENCE",
    "CITATION_UNRESOLVED",
    "HELD_EVIDENCE",
    "SUPERSEDED_EVIDENCE",
    "WITHDRAWN_EVIDENCE",
    "REVOKED_EVIDENCE",
  ] as const)("rejects the ABSTAIN-only %s reason on DENY", (reasonCode) => {
    const result = resolveEvidenceDrawer({
      ...denyFixture,
      reason_code: reasonCode,
    });

    expect(result).toMatchObject({
      outcome: "ERROR",
      code: "INVALID_PAYLOAD",
      evidenceRefs: [],
    });
  });
});

function supportedLayerSlice(): Record<string, unknown> {
  return {
    profile: GOVERNED_LAYER_SLICE_PROFILE,
    scope: "slice-local",
    outcome: "ANSWER",
    reason_code: "SUPPORTED",
    layers: [
      {
        source_id: "source:synthetic-streamflow",
        layer_id: selection.layerId,
        kind: "circle",
        title: "Synthetic streamflow demonstration",
        description:
          "One generalized, fixture-only Kansas streamflow feature for the bounded governed map slice.",
        geojson: {
          type: "FeatureCollection",
          features: [
            {
              type: "Feature",
              id: selection.featureId,
              geometry: { type: "Point", coordinates: [-98.5, 38.5] },
              properties: null,
            },
          ],
        },
        selection: {
          profile: selection.profile,
          selection_id: selection.selectionId,
          layer_id: selection.layerId,
          feature_id: selection.featureId,
          evidence_refs: [...selection.evidenceRefs],
        },
      },
    ],
    limitations: [
      "Fixture-only synthetic demonstration; not live data, release authority, or life-safety guidance.",
    ],
  };
}

function finiteLayerError(
  reason_code: "INVALID_REQUEST" | "UPSTREAM_ERROR",
): Record<string, unknown> {
  return {
    profile: GOVERNED_LAYER_SLICE_PROFILE,
    scope: "slice-local",
    outcome: "ERROR",
    reason_code,
    layers: [],
    limitations: [
      "Fixture-only synthetic demonstration; not live data, release authority, or life-safety guidance.",
    ],
  };
}

describe("governed Explorer map transport and layer adapter", () => {
  it("normalizes the exact-one layer response into the package-owned bundle", () => {
    const parsed = parseGovernedLayerSlice(supportedLayerSlice());

    expect(parsed).toMatchObject({
      ok: true,
      payload: {
        outcome: "ANSWER",
        reasonCode: "SUPPORTED",
        layers: [
          {
            title: "Synthetic streamflow demonstration",
            runtimeLayer: {
              profile: INLINE_GEOJSON_LAYER_PROFILE,
              sourceId: "source:synthetic-streamflow",
              layerId: selection.layerId,
              selection,
              data: {
                features: [
                  {
                    id: selection.featureId,
                    properties: null,
                    geometry: { coordinates: [-98.5, 38.5] },
                  },
                ],
              },
            },
          },
        ],
      },
    });
    expect(parsed.ok && Object.isFrozen(parsed.payload.layers[0].runtimeLayer)).toBe(true);
  });

  it.each([
    (value: any) => ({ ...value, private_field: "PRIVATE_CANARY" }),
    (value: any) => ({
      ...value,
      layers: [
        {
          ...value.layers[0],
          selection: {
            ...value.layers[0].selection,
            feature_id: "feature:other",
          },
        },
      ],
    }),
    (value: any) => ({
      ...value,
      layers: [
        {
          ...value.layers[0],
          geojson: {
            ...value.layers[0].geojson,
            features: [
              ...value.layers[0].geojson.features,
              value.layers[0].geojson.features[0],
            ],
          },
        },
      ],
    }),
  ])("fails closed on widened or identity-inconsistent layer data", (mutate) => {
    expect(parseGovernedLayerSlice(mutate(supportedLayerSlice()))).toEqual({
      ok: false,
      code: "MALFORMED_GOVERNED_LAYER_PAYLOAD",
    });
  });

  it.each([
    {
      field: "source_id",
      mutate: (value: any) => {
        value.layers[0].source_id = "source:synthetic-streamflow-drift";
      },
    },
    {
      field: "layer_id",
      mutate: (value: any) => {
        value.layers[0].layer_id = "layer:synthetic-streamflow-drift";
      },
    },
    {
      field: "feature.id",
      mutate: (value: any) => {
        value.layers[0].geojson.features[0].id = "feature:flow-drift";
      },
    },
    {
      field: "selection.selection_id",
      mutate: (value: any) => {
        value.layers[0].selection.selection_id = "selection:flow-drift";
      },
    },
    {
      field: "selection.layer_id",
      mutate: (value: any) => {
        value.layers[0].selection.layer_id = "layer:synthetic-streamflow-drift";
      },
    },
    {
      field: "selection.feature_id",
      mutate: (value: any) => {
        value.layers[0].selection.feature_id = "feature:flow-drift";
      },
    },
    {
      field: "selection.evidence_refs[0]",
      mutate: (value: any) => {
        value.layers[0].selection.evidence_refs[0] =
          "kfm:evidence:synthetic:flow-drift";
      },
    },
    {
      field: "longitude",
      mutate: (value: any) => {
        value.layers[0].geojson.features[0].geometry.coordinates[0] = -98.4;
      },
    },
    {
      field: "latitude",
      mutate: (value: any) => {
        value.layers[0].geojson.features[0].geometry.coordinates[1] = 38.4;
      },
    },
    {
      field: "title",
      mutate: (value: any) => {
        value.layers[0].title = "Synthetic streamflow demonstration drift";
      },
    },
    {
      field: "description",
      mutate: (value: any) => {
        value.layers[0].description =
          "A bounded synthetic point used to prove governed browser selection.";
      },
    },
    {
      field: "limitations[0]",
      mutate: (value: any) => {
        value.limitations[0] =
          "Synthetic slice only; no live observation is represented.";
      },
    },
  ])("fails closed when the exact Gate1 $field byte drifts", ({ mutate }) => {
    const value = supportedLayerSlice();
    mutate(value);
    expect(parseGovernedLayerSlice(value)).toEqual({
      ok: false,
      code: "MALFORMED_GOVERNED_LAYER_PAYLOAD",
    });
  });

  it("accepts only the two finite empty layer errors", () => {
    for (const reason_code of ["INVALID_REQUEST", "UPSTREAM_ERROR"]) {
      expect(parseGovernedLayerSlice(finiteLayerError(reason_code))).toMatchObject({
        ok: true,
        payload: { outcome: "ERROR", reasonCode: reason_code, layers: [] },
      });
    }
  });

  it.each([
    { endpoint: "layers", status: 400, payload: supportedLayerSlice() },
    { endpoint: "evidence", status: 500, payload: answerFixture },
  ])(
    "rejects an ANSWER payload from non-success $status on /$endpoint",
    async ({ endpoint, status, payload }) => {
      const transport = createGovernedHttpTransport(
        "https://explorer.example",
        async () =>
          new Response(JSON.stringify(payload), {
            status,
            headers: { "content-type": "application/json" },
          }),
      );

      const operation =
        endpoint === "layers"
          ? transport.loadLayers()
          : transport.loadEvidence(selection);
      await expect(operation).rejects.toThrow("status and outcome conflict");
      transport.close();
    },
  );

  it("rejects an ERROR payload from a success status", async () => {
    const transport = createGovernedHttpTransport(
      "https://explorer.example",
      async () =>
        new Response(JSON.stringify(finiteLayerError("UPSTREAM_ERROR")), {
          status: 200,
          headers: { "content-type": "application/json" },
        }),
    );

    await expect(transport.loadLayers()).rejects.toThrow(
      "status and outcome conflict",
    );
    transport.close();
  });

  it.each([
    { status: 400, reasonCode: "INVALID_REQUEST" as const },
    { status: 500, reasonCode: "UPSTREAM_ERROR" as const },
  ])(
    "keeps the finite Gate1 ERROR payload parseable on HTTP $status",
    async ({ status, reasonCode }) => {
      const transport = createGovernedHttpTransport(
        "https://explorer.example",
        async () =>
          new Response(JSON.stringify(finiteLayerError(reasonCode)), {
            status,
            headers: { "content-type": "application/json" },
          }),
      );

      const parsed = parseGovernedLayerSlice(await transport.loadLayers());
      expect(parsed).toMatchObject({
        ok: true,
        payload: { outcome: "ERROR", reasonCode },
      });
      transport.close();
    },
  );

  it("uses fixed same-origin endpoints, exact evidence query keys, and no-store", async () => {
    const request = vi.fn(async (input: RequestInfo | URL) => {
      const url = new URL(input.toString());
      return new Response(
        JSON.stringify(url.pathname === "/layers" ? supportedLayerSlice() : answerFixture),
        { headers: { "content-type": "application/json; charset=utf-8" } },
      );
    });
    const transport = createGovernedHttpTransport(
      "https://explorer.example",
      request,
    );

    await transport.loadLayers();
    await transport.loadEvidence(selection);

    expect(request).toHaveBeenCalledTimes(2);
    expect(request.mock.calls[0]?.[0].toString()).toBe(
      "https://explorer.example/layers",
    );
    const evidenceUrl = new URL(request.mock.calls[1]?.[0].toString() ?? "");
    expect(evidenceUrl.origin).toBe("https://explorer.example");
    expect([...evidenceUrl.searchParams.entries()]).toEqual([
      ["layer_id", selection.layerId],
      ["feature_id", selection.featureId],
      ["evidence_ref", selection.evidenceRefs[0]],
    ]);
    expect(request.mock.calls[0]?.[1]).toMatchObject({
      method: "GET",
      credentials: "same-origin",
      cache: "no-store",
      redirect: "error",
    });
    transport.close();
  });

  it("deadline-bounds unresolved response headers without poisoning later requests", async () => {
    vi.useFakeTimers();
    let transport: ReturnType<typeof createGovernedHttpTransport> | null = null;
    try {
      let callCount = 0;
      let firstSignal: AbortSignal | undefined;
      const request = vi.fn((_input: RequestInfo | URL, init?: RequestInit) => {
        callCount += 1;
        if (callCount === 1) {
          firstSignal = init?.signal ?? undefined;
          return new Promise<Response>(() => undefined);
        }
        return Promise.resolve(
          new Response(JSON.stringify(supportedLayerSlice()), {
            headers: { "content-type": "application/json" },
          }),
        );
      });
      transport = createGovernedHttpTransport(
        "https://explorer.example",
        request,
        { requestDeadlineMs: 25 },
      );

      const pending = transport.loadLayers();
      const rejection = expect(pending).rejects.toMatchObject({
        name: "TimeoutError",
        message: "Governed request deadline exceeded.",
      });
      await vi.advanceTimersByTimeAsync(25);
      await rejection;
      expect(firstSignal?.aborted).toBe(true);

      await expect(transport.loadLayers()).resolves.toEqual(
        supportedLayerSlice(),
      );
      expect(request).toHaveBeenCalledTimes(2);
      expect(vi.getTimerCount()).toBe(0);
    } finally {
      transport?.close();
      vi.useRealTimers();
    }
  });

  it("deadline-bounds a stalled response body without awaiting stream cancellation", async () => {
    vi.useFakeTimers();
    let transport: ReturnType<typeof createGovernedHttpTransport> | null = null;
    try {
      let markPullStarted!: () => void;
      const pullStarted = new Promise<void>((resolve) => {
        markPullStarted = resolve;
      });
      const neverSettles = new Promise<void>(() => undefined);
      const cancel = vi.fn(() => neverSettles);
      const stalledBody = new ReadableStream<Uint8Array>({
        pull() {
          markPullStarted();
          return neverSettles;
        },
        cancel,
      });
      transport = createGovernedHttpTransport(
        "https://explorer.example",
        async () =>
          new Response(stalledBody, {
            headers: { "content-type": "application/json" },
          }),
        { requestDeadlineMs: 25 },
      );

      const pending = transport.loadEvidence(selection);
      const rejection = expect(pending).rejects.toMatchObject({
        name: "TimeoutError",
        message: "Governed request deadline exceeded.",
      });
      await pullStarted;
      await vi.advanceTimersByTimeAsync(25);
      await rejection;
      expect(cancel).toHaveBeenCalledTimes(1);
      expect(vi.getTimerCount()).toBe(0);
    } finally {
      transport?.close();
      vi.useRealTimers();
    }
  });

  it("cancels an oversized streamed response and closes active requests idempotently", async () => {
    const cancel = vi.fn();
    const oversized = new ReadableStream<Uint8Array>({
      start(controller) {
        controller.enqueue(new Uint8Array(32 * 1024 + 1));
      },
      cancel,
    });
    const oversizedTransport = createGovernedHttpTransport(
      "https://explorer.example",
      async () =>
        new Response(oversized, {
          headers: { "content-type": "application/json" },
        }),
    );
    await expect(oversizedTransport.loadLayers()).rejects.toThrow(
      "exceeds the browser bound",
    );
    expect(cancel).toHaveBeenCalledTimes(1);
    oversizedTransport.close();

    let observedSignal: AbortSignal | undefined;
    const pendingTransport = createGovernedHttpTransport(
      "https://explorer.example",
      (_input, init) =>
        new Promise<Response>((_resolve, reject) => {
          observedSignal = init?.signal ?? undefined;
          observedSignal?.addEventListener("abort", () =>
            reject(new DOMException("Aborted", "AbortError")),
          );
        }),
    );
    const pending = pendingTransport.loadLayers();
    pendingTransport.close();
    pendingTransport.close();
    expect(observedSignal?.aborted).toBe(true);
    await expect(pending).rejects.toMatchObject({ name: "AbortError" });
    await expect(pendingTransport.loadLayers()).rejects.toThrow("closed");
  });
});
