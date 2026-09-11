/**
 * App-local projection boundary for the closed Living Waters proof packet.
 *
 * This module deliberately accepts an already-bounded fixture packet. It does
 * not fetch, resolve a source, evaluate policy, release data, or bind a
 * renderer. The canonical packet and its validator remain outside this UI
 * feature.
 */

export const LIVING_WATERS_FIXTURE_PROJECTION_PROFILE =
  "kfm.explorer.living-waters-fixture-projection.v1" as const;

export const LIVING_WATERS_FIXTURE_PACKET_ID =
  "fixture:hydrology:living-waters:first-proof" as const;

export const LIVING_WATERS_SCENARIO_IDS = [
  "current",
  "stale",
  "no-results",
  "unavailable",
  "ambiguous-reach",
] as const;

export type LivingWatersScenarioId = (typeof LIVING_WATERS_SCENARIO_IDS)[number];

export const LIVING_WATERS_FRAME_STATES = [
  "AVAILABLE",
  "STALE",
  "NO_RESULTS",
  "UNAVAILABLE",
  "ABSTAIN",
] as const;

export type LivingWatersFrameState = (typeof LIVING_WATERS_FRAME_STATES)[number];

export type LivingWatersFixturePoint = Readonly<{
  observed_at: string;
  value: number;
}>;

export type LivingWatersFixtureScenario = Readonly<{
  id: string;
  state: string;
  join_outcome: string;
  reason_codes: readonly string[];
  display_message: string;
}>;

/** A decoded packet shape; schema validation is owned by the hydrology lane. */
export type LivingWatersFixturePacket = Readonly<{
  packet_id: string;
  profile: string;
  snapshot: Readonly<{
    identity: string;
    version: string;
    content_digest: string;
    huc12: string;
    reach_ids: readonly string[];
    role: string;
  }>;
  gauge: Readonly<{
    site_id: string;
    state: string;
    spatial_support: string;
    role: string;
  }>;
  series: Readonly<{
    parameter_code: string;
    parameter_name: string;
    statistic_code: string;
    statistic_name: string;
    unit_code: string;
    qualifier_code: string;
    qualifier_name: string;
    points: readonly LivingWatersFixturePoint[];
  }>;
  scenarios: readonly LivingWatersFixtureScenario[];
  governance: Readonly<{
    source_admitted: boolean;
    source_activated: boolean;
    policy_evaluated: boolean;
    released: boolean;
    deployed: boolean;
    published: boolean;
    fixture_only: boolean;
  }>;
}>;

export type LivingWatersFramePoint = Readonly<{
  observedAt: string;
  value: number;
}>;

export type LivingWatersFrame = Readonly<{
  profile: typeof LIVING_WATERS_FIXTURE_PROJECTION_PROFILE;
  packetId: typeof LIVING_WATERS_FIXTURE_PACKET_ID;
  scenarioId: LivingWatersScenarioId;
  state: LivingWatersFrameState;
  joinOutcome: "EXACT" | "NOT_ATTEMPTED" | "AMBIGUOUS";
  reasonCodes: readonly string[];
  displayMessage: string;
  spatial: Readonly<{
    huc12: string;
    reachIds: readonly string[];
    spatialSupport: "generalized_county";
  }>;
  measurement: Readonly<{
    parameterCode: "00060";
    parameterName: "discharge";
    statisticCode: "00000";
    statisticName: "instantaneous";
    unitCode: "ft3/s";
    qualifierCode: "P";
    qualifierName: "provisional";
    points: readonly LivingWatersFramePoint[];
  }>;
  temporal: Readonly<{
    observedAtStart: string | null;
    observedAtEnd: string | null;
    pointCount: number;
  }>;
  trust: Readonly<{
    state: "SITE_LOCAL_DEMO";
    fixtureRef: typeof LIVING_WATERS_FIXTURE_PACKET_ID;
    evidenceRefs: readonly string[];
    sourceAdmitted: false;
    sourceActivated: false;
    released: false;
    deployed: false;
    published: false;
    fixtureOnly: true;
  }>;
  render: Readonly<{
    layerId: "layer:watershed-storage";
    representation: "CATALOG_ONLY";
    visible: false;
    rendererBound: false;
  }>;
}>;

const isScenarioId = (value: string): value is LivingWatersScenarioId =>
  (LIVING_WATERS_SCENARIO_IDS as readonly string[]).includes(value);

const isFrameState = (value: string): value is LivingWatersFrameState =>
  (LIVING_WATERS_FRAME_STATES as readonly string[]).includes(value);

const isJoinOutcome = (
  value: string,
): value is LivingWatersFrame["joinOutcome"] =>
  value === "EXACT" || value === "NOT_ATTEMPTED" || value === "AMBIGUOUS";

const freezeArray = <T>(values: readonly T[]): readonly T[] =>
  Object.freeze([...values]);

const assertClosedFixturePacket = (packet: LivingWatersFixturePacket): void => {
  if (
    packet.packet_id !== LIVING_WATERS_FIXTURE_PACKET_ID ||
    packet.profile !== "living-waters-fixture-v1"
  ) {
    throw new Error("LIVING_WATERS_FIXTURE_IDENTITY_MISMATCH");
  }

  if (
    packet.snapshot.role !== "synthetic_reference" ||
    packet.gauge.role !== "synthetic_site_metadata" ||
    packet.gauge.state !== "KS" ||
    packet.gauge.spatial_support !== "generalized_county"
  ) {
    throw new Error("LIVING_WATERS_FIXTURE_SPATIAL_ROLE_MISMATCH");
  }

  if (
    packet.series.parameter_code !== "00060" ||
    packet.series.parameter_name !== "discharge" ||
    packet.series.statistic_code !== "00000" ||
    packet.series.statistic_name !== "instantaneous" ||
    packet.series.unit_code !== "ft3/s" ||
    packet.series.qualifier_code !== "P" ||
    packet.series.qualifier_name !== "provisional"
  ) {
    throw new Error("LIVING_WATERS_FIXTURE_SERIES_IDENTITY_MISMATCH");
  }

  if (
    !packet.governance.fixture_only ||
    packet.governance.source_admitted ||
    packet.governance.source_activated ||
    packet.governance.policy_evaluated ||
    packet.governance.released ||
    packet.governance.deployed ||
    packet.governance.published
  ) {
    throw new Error("LIVING_WATERS_FIXTURE_GOVERNANCE_BOUNDARY_VIOLATION");
  }

  const scenarioIds = packet.scenarios.map((scenario) => scenario.id);
  if (
    scenarioIds.length !== LIVING_WATERS_SCENARIO_IDS.length ||
    new Set(scenarioIds).size !== LIVING_WATERS_SCENARIO_IDS.length ||
    !LIVING_WATERS_SCENARIO_IDS.every((id) => scenarioIds.includes(id)) ||
    packet.scenarios.some(
      (scenario) => !isScenarioId(scenario.id) || !isFrameState(scenario.state),
    )
  ) {
    throw new Error("LIVING_WATERS_FIXTURE_SCENARIO_SET_MISMATCH");
  }
};

/**
 * Project a validated, closed packet into a renderer-neutral UI frame.
 *
 * `AVAILABLE` and `STALE` retain the synthetic points for a bounded chart.
 * Empty, unavailable, and ambiguous joins intentionally contain no points.
 */
export const projectLivingWatersFixture = (
  packet: LivingWatersFixturePacket,
  scenarioId: LivingWatersScenarioId,
): LivingWatersFrame => {
  assertClosedFixturePacket(packet);

  const scenario = packet.scenarios.find((entry) => entry.id === scenarioId);
  if (!scenario || !isFrameState(scenario.state) || !isJoinOutcome(scenario.join_outcome)) {
    throw new Error("LIVING_WATERS_FIXTURE_SCENARIO_NOT_FOUND");
  }

  const state = scenario.state;
  const retainsPoints = state === "AVAILABLE" || state === "STALE";
  const points = retainsPoints
    ? freezeArray(
        packet.series.points.map((point) =>
          Object.freeze({ observedAt: point.observed_at, value: point.value }),
        ),
      )
    : freezeArray<LivingWatersFramePoint>([]);
  const reasonCodes = freezeArray(scenario.reason_codes);
  const reachIds = freezeArray(packet.snapshot.reach_ids);

  return Object.freeze({
    profile: LIVING_WATERS_FIXTURE_PROJECTION_PROFILE,
    packetId: LIVING_WATERS_FIXTURE_PACKET_ID,
    scenarioId,
    state,
    joinOutcome: scenario.join_outcome,
    reasonCodes,
    displayMessage: scenario.display_message,
    spatial: Object.freeze({
      huc12: packet.snapshot.huc12,
      reachIds,
      spatialSupport: "generalized_county" as const,
    }),
    measurement: Object.freeze({
      parameterCode: "00060" as const,
      parameterName: "discharge" as const,
      statisticCode: "00000" as const,
      statisticName: "instantaneous" as const,
      unitCode: "ft3/s" as const,
      qualifierCode: "P" as const,
      qualifierName: "provisional" as const,
      points,
    }),
    temporal: Object.freeze({
      observedAtStart: points[0]?.observedAt ?? null,
      observedAtEnd: points.at(-1)?.observedAt ?? null,
      pointCount: points.length,
    }),
    trust: Object.freeze({
      state: "SITE_LOCAL_DEMO" as const,
      fixtureRef: LIVING_WATERS_FIXTURE_PACKET_ID,
      evidenceRefs: freezeArray<string>([]),
      sourceAdmitted: false as const,
      sourceActivated: false as const,
      released: false as const,
      deployed: false as const,
      published: false as const,
      fixtureOnly: true as const,
    }),
    render: Object.freeze({
      layerId: "layer:watershed-storage" as const,
      representation: "CATALOG_ONLY" as const,
      visible: false as const,
      rendererBound: false as const,
    }),
  });
};

