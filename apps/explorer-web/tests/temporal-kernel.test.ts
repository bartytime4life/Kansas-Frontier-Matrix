import { describe, expect, it } from "vitest";
import snapshotFixture from "../../../fixtures/contracts/v1/common/temporal_view_state/valid/valid_snapshot.json";
import comparisonFixture from "../../../fixtures/contracts/v1/common/temporal_view_state/valid/valid_comparison.json";
import geologicFixture from "../../../fixtures/contracts/v1/common/temporal_view_state/unsupported/geologic_age.json";
import naiveFixture from "../../../fixtures/contracts/v1/common/temporal_view_state/unsupported/naive_instant.json";
import {
  createTemporalRuntimeState,
  deriveTemporalQueryId,
  deriveTemporalStateId,
  reduceTemporalRuntime,
  validateTemporalFrameContext,
  validateTemporalViewState,
  type TemporalFrameContext,
  type TemporalViewState,
} from "../src/features/temporal";

const snapshot = snapshotFixture as unknown as TemporalViewState;
const comparison = comparisonFixture as unknown as TemporalViewState;

function copy(value: unknown): any {
  return JSON.parse(JSON.stringify(value));
}

describe("shared temporal kernel conformance", () => {
  it("accepts the snapshot and comparison fixtures with reproducible identities", async () => {
    await expect(validateTemporalViewState(snapshot)).resolves.toMatchObject({
      status: "SUPPORTED",
      code: "OK",
    });
    await expect(validateTemporalViewState(comparison)).resolves.toMatchObject({
      status: "SUPPORTED",
      code: "OK",
    });
    await expect(deriveTemporalStateId(snapshot)).resolves.toBe(snapshot.state_id);
    await expect(deriveTemporalStateId(comparison)).resolves.toBe(comparison.state_id);
  });

  it("returns bounded outcomes for deep time and naive instants", async () => {
    const geologic = copy(geologicFixture);
    geologic.state_id = await deriveTemporalStateId(geologic);
    const naive = copy(naiveFixture);
    naive.state_id = await deriveTemporalStateId(naive);

    await expect(validateTemporalViewState(geologic)).resolves.toMatchObject({
      status: "UNSUPPORTED",
      code: "UNSUPPORTED_PROFILE",
    });
    await expect(validateTemporalViewState(naive)).resolves.toMatchObject({
      status: "UNSUPPORTED",
      code: "UNKNOWN_TIMEZONE",
    });
  });

  it("ignores a stale response and commits only the current generation", async () => {
    const queryId = await deriveTemporalQueryId(snapshot);
    const initial = createTemporalRuntimeState();
    const requested = reduceTemporalRuntime(initial, {
      type: "REQUEST_FRAME",
      state: snapshot,
      queryId,
    });
    const frame: TemporalFrameContext = {
      profile: "kfm.temporal.frame-context.v1",
      stateId: snapshot.state_id,
      queryId,
      selectedSupport: { raw: "2024-01-01T00:00:00Z" },
      layers: [
        {
          layerId: "kfm:layer:streamflow",
          actualTime: "2024-01-01T00:00:00Z",
          availability: "AVAILABLE",
          evidenceRefs: ["kfm:evidence:fixture:streamflow-2024-01-01"],
          sourceVersionRef: "kfm:dataset:fixture:streamflow-v1",
          releaseStatus: "RELEASED",
        },
      ],
      datasetVersionRefs: ["kfm:dataset:fixture:streamflow-v1"],
      releaseRefs: ["kfm:release:fixture:streamflow-v1"],
      policyStatus: "CURRENT_POLICY",
      outcome: "ANSWER",
    };

    const stale = reduceTemporalRuntime(requested, {
      type: "COMMIT_FRAME",
      generation: requested.generation - 1,
      frame,
    });
    expect(stale.committedFrame).toBeNull();

    const committed = reduceTemporalRuntime(requested, {
      type: "COMMIT_FRAME",
      generation: requested.generation,
      frame,
    });
    expect(committed.status).toBe("COMMITTED");
    expect(committed.committedFrame).toBe(frame);
  });

  it("blocks old-frame metadata from a withheld layer", () => {
    const result = validateTemporalFrameContext({
      profile: "kfm.temporal.frame-context.v1",
      stateId: snapshot.state_id,
      queryId: "kfm:temporal-query:sha256:" + "0".repeat(64),
      selectedSupport: {},
      layers: [
        {
          layerId: "kfm:layer:restricted",
          actualTime: null,
          availability: "WITHHELD",
          evidenceRefs: [],
          sourceVersionRef: null,
          releaseStatus: "WITHHELD",
        },
      ],
      datasetVersionRefs: [],
      releaseRefs: [],
      policyStatus: "CURRENT_POLICY",
      outcome: "ANSWER",
    });
    expect(result).toMatchObject({ status: "SUPPORTED", code: "OK" });

    const leaked = validateTemporalFrameContext({
      profile: "kfm.temporal.frame-context.v1",
      stateId: snapshot.state_id,
      queryId: "kfm:temporal-query:sha256:" + "0".repeat(64),
      selectedSupport: {},
      layers: [
        {
          layerId: "kfm:layer:restricted",
          actualTime: "2024-01-01T00:00:00Z",
          availability: "WITHHELD",
          evidenceRefs: ["kfm:evidence:restricted"],
          sourceVersionRef: null,
          releaseStatus: "WITHHELD",
        },
      ],
      datasetVersionRefs: [],
      releaseRefs: [],
      policyStatus: "CURRENT_POLICY",
      outcome: "ANSWER",
    });
    expect(leaked).toMatchObject({
      status: "ERROR",
      code: "WITHHELD_DATA_LEAK",
    });
  });
});
