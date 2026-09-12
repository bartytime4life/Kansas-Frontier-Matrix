/**
 * Review-only projection for the human-selected Phase 4 Living Waters
 * candidate. This module carries no observation payload and never fetches,
 * resolves a source, evaluates policy, or binds a renderer.
 */

export const PHASE_4_LIVING_WATERS_PRODUCT_SELECTION_PROFILE =
  "kfm.explorer.living-waters-product-selection.v1" as const;

export const PHASE_4_LIVING_WATERS_PRODUCT_SELECTION_ID =
  "proposal:hydrology:phase-4:usgs-07146500" as const;

const USGS_CONTINUOUS_VALUES_REFERENCE =
  "https://api.waterdata.usgs.gov/ogcapi/v0/collections/continuous" as const;
const USGS_07146500_REFERENCE =
  "https://waterdata.usgs.gov/monitoring-location/USGS-07146500/" as const;

const freezeArray = <T>(values: readonly T[]): readonly T[] =>
  Object.freeze([...values]);

export type Phase4LivingWatersProductSelection = Readonly<{
  selectionId: string;
  profile: string;
  selectionState: string;
  product: Readonly<{
    publisher: string;
    product: string;
    parameterCode: string;
    parameterName: string;
    statisticName: string;
    unitCode: string;
  }>;
  gauge: Readonly<{
    agency: string;
    siteNumber: string;
    displayName: string;
    state: string;
  }>;
  sourceReferences: readonly string[];
  governance: Readonly<{
    sourceAdmitted: boolean;
    sourceActivated: boolean;
    sourcePayloadRetrieved: boolean;
    policyEvaluated: boolean;
    released: boolean;
    deployed: boolean;
    published: boolean;
    floodWarningAuthority: boolean;
  }>;
}>;

/**
 * The user-selected product-and-gauge pair. It is a review fixture only:
 * no observation, endpoint response, source descriptor, or publication
 * authority is represented here.
 */
export const PHASE_4_LIVING_WATERS_PRODUCT_SELECTION = Object.freeze({
  selectionId: PHASE_4_LIVING_WATERS_PRODUCT_SELECTION_ID,
  profile: PHASE_4_LIVING_WATERS_PRODUCT_SELECTION_PROFILE,
  selectionState: "HUMAN_SELECTED_REVIEW_PENDING",
  product: Object.freeze({
    publisher: "USGS",
    product: "continuous-values",
    parameterCode: "00060",
    parameterName: "discharge",
    statisticName: "instantaneous",
    unitCode: "ft3/s",
  }),
  gauge: Object.freeze({
    agency: "USGS",
    siteNumber: "07146500",
    displayName: "Arkansas River at Arkansas City, KS",
    state: "KS",
  }),
  sourceReferences: freezeArray([
    USGS_CONTINUOUS_VALUES_REFERENCE,
    USGS_07146500_REFERENCE,
  ]),
  governance: Object.freeze({
    sourceAdmitted: false,
    sourceActivated: false,
    sourcePayloadRetrieved: false,
    policyEvaluated: false,
    released: false,
    deployed: false,
    published: false,
    floodWarningAuthority: false,
  }),
}) satisfies Phase4LivingWatersProductSelection;

export type Phase4LivingWatersProductSelectionFrame = Readonly<{
  profile: typeof PHASE_4_LIVING_WATERS_PRODUCT_SELECTION_PROFILE;
  selectionId: typeof PHASE_4_LIVING_WATERS_PRODUCT_SELECTION_ID;
  selectionState: "HUMAN_SELECTED_REVIEW_PENDING";
  product: Readonly<{
    publisher: "USGS";
    product: "continuous-values";
    parameterCode: "00060";
    parameterName: "discharge";
    statisticName: "instantaneous";
    unitCode: "ft3/s";
  }>;
  gauge: Readonly<{
    agency: "USGS";
    siteNumber: "07146500";
    displayName: "Arkansas River at Arkansas City, KS";
    state: "KS";
  }>;
  sourceReferences: readonly string[];
  observation: Readonly<{
    state: "NOT_RETRIEVED";
    value: null;
    observedAt: null;
  }>;
  trust: Readonly<{
    evidenceState: "REFERENCED_NOT_RESOLVED";
    sourceAdmitted: false;
    sourceActivated: false;
    sourcePayloadRetrieved: false;
    policyEvaluated: false;
    released: false;
    deployed: false;
    published: false;
    floodWarningAuthority: false;
  }>;
  render: Readonly<{
    representation: "REVIEW_RECORD_ONLY";
    visible: false;
    rendererBound: false;
  }>;
}>;

const assertPhase4LivingWatersProductSelection = (
  selection: Phase4LivingWatersProductSelection,
): void => {
  if (
    selection.selectionId !== PHASE_4_LIVING_WATERS_PRODUCT_SELECTION_ID ||
    selection.profile !== PHASE_4_LIVING_WATERS_PRODUCT_SELECTION_PROFILE ||
    selection.selectionState !== "HUMAN_SELECTED_REVIEW_PENDING"
  ) {
    throw new Error("LIVING_WATERS_PRODUCT_SELECTION_IDENTITY_MISMATCH");
  }

  if (
    selection.product.publisher !== "USGS" ||
    selection.product.product !== "continuous-values" ||
    selection.product.parameterCode !== "00060" ||
    selection.product.parameterName !== "discharge" ||
    selection.product.statisticName !== "instantaneous" ||
    selection.product.unitCode !== "ft3/s" ||
    selection.gauge.agency !== "USGS" ||
    selection.gauge.siteNumber !== "07146500" ||
    selection.gauge.displayName !== "Arkansas River at Arkansas City, KS" ||
    selection.gauge.state !== "KS" ||
    selection.sourceReferences.length !== 2 ||
    selection.sourceReferences[0] !== USGS_CONTINUOUS_VALUES_REFERENCE ||
    selection.sourceReferences[1] !== USGS_07146500_REFERENCE
  ) {
    throw new Error("LIVING_WATERS_PRODUCT_SELECTION_SEMANTICS_MISMATCH");
  }

  if (
    selection.governance.sourceAdmitted ||
    selection.governance.sourceActivated ||
    selection.governance.sourcePayloadRetrieved ||
    selection.governance.policyEvaluated ||
    selection.governance.released ||
    selection.governance.deployed ||
    selection.governance.published ||
    selection.governance.floodWarningAuthority
  ) {
    throw new Error("LIVING_WATERS_PRODUCT_SELECTION_GOVERNANCE_BOUNDARY_VIOLATION");
  }
};

/**
 * Projects one exact human-selected nomination into a renderer-neutral record.
 * The frame intentionally has no observed discharge or time: obtaining either
 * requires later source, evidence, policy, and lifecycle decisions.
 */
export const projectPhase4LivingWatersProductSelection = (
  selection: Phase4LivingWatersProductSelection,
): Phase4LivingWatersProductSelectionFrame => {
  assertPhase4LivingWatersProductSelection(selection);

  return Object.freeze({
    profile: PHASE_4_LIVING_WATERS_PRODUCT_SELECTION_PROFILE,
    selectionId: PHASE_4_LIVING_WATERS_PRODUCT_SELECTION_ID,
    selectionState: "HUMAN_SELECTED_REVIEW_PENDING" as const,
    product: Object.freeze({
      publisher: "USGS" as const,
      product: "continuous-values" as const,
      parameterCode: "00060" as const,
      parameterName: "discharge" as const,
      statisticName: "instantaneous" as const,
      unitCode: "ft3/s" as const,
    }),
    gauge: Object.freeze({
      agency: "USGS" as const,
      siteNumber: "07146500" as const,
      displayName: "Arkansas River at Arkansas City, KS" as const,
      state: "KS" as const,
    }),
    sourceReferences: freezeArray(selection.sourceReferences),
    observation: Object.freeze({
      state: "NOT_RETRIEVED" as const,
      value: null,
      observedAt: null,
    }),
    trust: Object.freeze({
      evidenceState: "REFERENCED_NOT_RESOLVED" as const,
      sourceAdmitted: false as const,
      sourceActivated: false as const,
      sourcePayloadRetrieved: false as const,
      policyEvaluated: false as const,
      released: false as const,
      deployed: false as const,
      published: false as const,
      floodWarningAuthority: false as const,
    }),
    render: Object.freeze({
      representation: "REVIEW_RECORD_ONLY" as const,
      visible: false as const,
      rendererBound: false as const,
    }),
  });
};
