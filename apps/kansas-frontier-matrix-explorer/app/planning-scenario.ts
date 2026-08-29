export type ScenarioReviewMode = "held" | "missing" | "denied" | "error";
export type ScenarioOutcome = "ABSTAIN" | "DENY" | "ERROR";
export type ScenarioUncertainty = "LOW" | "MEDIUM" | "HIGH" | "UNRESOLVED";

export type PlanningScenarioReview = Readonly<{
  mode: ScenarioReviewMode;
  outcome: ScenarioOutcome;
  code: "SCENARIO_HELD" | "SCENARIO_MISSING" | "POLICY_DENIED" | "UPSTREAM_ERROR";
  heading: string;
  message: string;
  scenarioStatus: "HELD" | null;
  purpose: string | null;
  geography: string | null;
  baselineAsOf: string | null;
  horizon: string | null;
  inputs: readonly Readonly<{ id: string; label: string; sourceRef: string; uncertainty: ScenarioUncertainty }>[];
  assumptions: readonly Readonly<{ id: string; statement: string; uncertainty: ScenarioUncertainty }>[];
  equityQuestions: readonly Readonly<{ id: string; description: string; limitation: string }>[];
  participationRefs: readonly string[];
  evidenceRefs: readonly string[];
  limitations: readonly string[];
  nonAuthorityLabels: readonly string[];
}>;

const EMPTY = Object.freeze([]) as readonly never[];

const held: PlanningScenarioReview = Object.freeze({
  mode: "held",
  outcome: "ABSTAIN",
  code: "SCENARIO_HELD",
  heading: "Synthetic Kansas drought-planning exploration",
  message: "Exploratory fixture for review. It is not a prediction, recommendation, emergency alert, regulatory determination, release, or publication.",
  scenarioStatus: "HELD",
  purpose: "Explore how a generalized planning surface could compare long-horizon water-demand, precipitation, and storage assumptions without predicting conditions or recommending action.",
  geography: "Kansas (synthetic generalized fixture)",
  baselineAsOf: "2026-01-01",
  horizon: "2030-01-01 through 2040-12-31",
  inputs: Object.freeze([
    Object.freeze({ id: "demand-index", label: "Synthetic generalized water-demand index", sourceRef: "fixture:evidence:demand-series", uncertainty: "HIGH" }),
    Object.freeze({ id: "precipitation-index", label: "Synthetic generalized precipitation index", sourceRef: "fixture:evidence:precipitation-series", uncertainty: "HIGH" }),
    Object.freeze({ id: "storage-index", label: "Synthetic generalized storage index", sourceRef: "fixture:evidence:reservoir-series", uncertainty: "HIGH" }),
  ]),
  assumptions: Object.freeze([
    Object.freeze({ id: "assumption-demand-comparison", statement: "The example compares only generalized demand-index changes and does not infer household, agricultural, municipal, or industrial demand.", uncertainty: "HIGH" }),
    Object.freeze({ id: "assumption-no-forecast", statement: "The horizon is an exploratory comparison window and not a forecast interval.", uncertainty: "UNRESOLVED" }),
    Object.freeze({ id: "assumption-storage-comparison", statement: "The storage index is generalized and cannot support facility operations or emergency decisions.", uncertainty: "HIGH" }),
  ]),
  equityQuestions: Object.freeze([
    Object.freeze({ id: "equity-service-continuity", description: "Ask whether scenario assumptions could affect continuity of basic water service differently across generalized communities.", limitation: "The fixture contains no community-level measurement or finding." }),
    Object.freeze({ id: "equity-water-cost-burden", description: "Ask whether cost burdens would need separate evidence before interpreting a scenario.", limitation: "The fixture contains no household, ratepayer, or affordability data." }),
  ]),
  participationRefs: Object.freeze([
    "fixture:participation:generalized-community-review",
    "fixture:participation:water-planning-steward-review",
  ]),
  evidenceRefs: Object.freeze([
    "fixture:evidence:demand-series",
    "fixture:evidence:participation-record",
    "fixture:evidence:precipitation-series",
    "fixture:evidence:reservoir-series",
  ]),
  limitations: Object.freeze([
    "No current-condition, forecast, facility-operation, household, or regulatory claim is made.",
    "Participation references are synthetic and do not establish consent, consensus, or completeness.",
  ]),
  nonAuthorityLabels: Object.freeze([
    "NOT_A_PREDICTION",
    "NOT_EMERGENCY_ALERTING",
    "NOT_REGULATORY_DETERMINATION",
  ]),
});

const negative = (
  mode: Exclude<ScenarioReviewMode, "held">,
  outcome: ScenarioOutcome,
  code: Exclude<PlanningScenarioReview["code"], "SCENARIO_HELD">,
  heading: string,
  message: string,
): PlanningScenarioReview => Object.freeze({
  mode,
  outcome,
  code,
  heading,
  message,
  scenarioStatus: null,
  purpose: null,
  geography: null,
  baselineAsOf: null,
  horizon: null,
  inputs: EMPTY,
  assumptions: EMPTY,
  equityQuestions: EMPTY,
  participationRefs: EMPTY,
  evidenceRefs: EMPTY,
  limitations: EMPTY,
  nonAuthorityLabels: EMPTY,
});

export const PLANNING_SCENARIO_REVIEWS: Readonly<Record<ScenarioReviewMode, PlanningScenarioReview>> = Object.freeze({
  held,
  missing: negative("missing", "ABSTAIN", "SCENARIO_MISSING", "Planning scenario unavailable", "The governed planning-scenario projection is incomplete."),
  denied: negative("denied", "DENY", "POLICY_DENIED", "Planning scenario withheld", "Policy does not permit this planning-scenario projection to be displayed."),
  error: negative("error", "ERROR", "UPSTREAM_ERROR", "Planning scenario unavailable", "The governed planning-scenario projection could not be completed."),
});

export const PLANNING_SCENARIO_MODES = Object.freeze([
  Object.freeze({ id: "held", label: "Held fixture" }),
  Object.freeze({ id: "missing", label: "Missing" }),
  Object.freeze({ id: "denied", label: "Denied" }),
  Object.freeze({ id: "error", label: "Error" }),
] as const);
