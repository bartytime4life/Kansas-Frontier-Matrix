import {
  EVIDENCE_DRAWER_PROJECTION_PROFILE,
  type EvidenceDrawerReasonCode,
} from "../../adapters/GovernedClient";
import {
  mountEvidenceDrawer,
  resolveEvidenceDrawer,
  type EvidenceDrawerController,
  type EvidenceDrawerViewModel,
} from "../evidence_drawer";

/**
 * Renderer-neutral feature-selection profile used by the fixture-only click bridge.
 * A selection scopes a governed resolution request; it is never evidence by itself.
 */
export const MAP_FEATURE_SELECTION_PROFILE =
  "kfm.explorer.map-feature-selection.v1" as const;

export type MapFeatureSelection = Readonly<{
  profile: typeof MAP_FEATURE_SELECTION_PROFILE;
  selectionId: string;
  layerId: string;
  featureId: string;
  evidenceRefs: readonly string[];
}>;

export type GovernedMapEvidenceResolver = (
  selection: MapFeatureSelection,
) => Promise<unknown>;

export type MapEvidenceResolutionCode =
  | EvidenceDrawerViewModel["code"]
  | "SELECTION_INVALID"
  | "DRAWER_EVIDENCE_OUTSIDE_SELECTION"
  | "GOVERNED_RESOLVER_ERROR";

export type MapEvidenceResolution = Readonly<{
  selection: MapFeatureSelection | null;
  code: MapEvidenceResolutionCode;
  drawerInput: unknown;
  drawer: EvidenceDrawerViewModel;
}>;

export type MapEvidenceFixtureCase = Readonly<{
  caseId: string;
  label: string;
  selection: unknown;
}>;

export type MapEvidenceFixtureController = Readonly<{
  select: (caseId: string) => Promise<MapEvidenceResolution | null>;
  destroy: () => void;
}>;

const SELECTION_FIELDS = new Set([
  "profile",
  "selection_id",
  "layer_id",
  "feature_id",
  "evidence_refs",
]);
const SAFE_ID = /^[A-Za-z0-9][A-Za-z0-9:._/-]{0,159}$/;
const MAX_EVIDENCE_REFS = 16;

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function hasExactFields(
  value: Record<string, unknown>,
  allowed: ReadonlySet<string>,
): boolean {
  const keys = Object.keys(value);
  return keys.length === allowed.size && keys.every((key) => allowed.has(key));
}

function isSafeId(value: unknown): value is string {
  return typeof value === "string" && SAFE_ID.test(value);
}

function parseEvidenceRefs(value: unknown): readonly string[] | null {
  if (!Array.isArray(value) || value.length > MAX_EVIDENCE_REFS) return null;
  if (!value.every(isSafeId)) return null;
  if (new Set(value).size !== value.length) return null;
  return Object.freeze([...value]);
}

/** Strictly validate one renderer-neutral feature selection. */
export function parseMapFeatureSelection(
  value: unknown,
): MapFeatureSelection | null {
  if (!isRecord(value) || !hasExactFields(value, SELECTION_FIELDS)) return null;
  if (value.profile !== MAP_FEATURE_SELECTION_PROFILE) return null;
  if (!isSafeId(value.selection_id)) return null;
  if (!isSafeId(value.layer_id)) return null;
  if (!isSafeId(value.feature_id)) return null;

  const evidenceRefs = parseEvidenceRefs(value.evidence_refs);
  if (evidenceRefs === null) return null;

  return Object.freeze({
    profile: MAP_FEATURE_SELECTION_PROFILE,
    selectionId: value.selection_id,
    layerId: value.layer_id,
    featureId: value.feature_id,
    evidenceRefs,
  });
}

function localProjection(
  id: string,
  outcome: "ABSTAIN" | "ERROR",
  reasonCode: "MISSING_EVIDENCE" | "UPSTREAM_ERROR",
  summary: string,
): Readonly<Record<string, unknown>> {
  return Object.freeze({
    profile: EVIDENCE_DRAWER_PROJECTION_PROFILE,
    id,
    outcome,
    reason_code: reasonCode,
    title:
      outcome === "ABSTAIN"
        ? "Map selection evidence not available"
        : "Map selection evidence unavailable",
    summary,
    evidence_refs: Object.freeze([]),
    citations: Object.freeze([]),
    limitations: Object.freeze([
      "Rendered feature properties are request scope, not evidence.",
      "No unsupported claim is shown.",
    ]),
    trust_state: Object.freeze({
      source_role: "context",
      policy: outcome === "ABSTAIN" ? "ABSTAIN" : "ERROR",
      review: "NOT_APPLICABLE",
      release: "UNRELEASED",
      freshness: "UNKNOWN",
      correction: "NONE",
    }),
    history: Object.freeze({
      negative_outcomes: Object.freeze([]),
      corrections: Object.freeze([]),
    }),
  });
}

function localResolution(
  selection: MapFeatureSelection | null,
  code: Extract<
    MapEvidenceResolutionCode,
    | "SELECTION_INVALID"
    | "MISSING_EVIDENCE"
    | "DRAWER_EVIDENCE_OUTSIDE_SELECTION"
    | "GOVERNED_RESOLVER_ERROR"
  >,
): MapEvidenceResolution {
  const isMissing = code === "MISSING_EVIDENCE";
  const drawerInput = localProjection(
    selection === null
      ? "kfm:drawer:invalid-map-selection"
      : `kfm:drawer:${selection.selectionId}`,
    isMissing ? "ABSTAIN" : "ERROR",
    isMissing ? "MISSING_EVIDENCE" : "UPSTREAM_ERROR",
    isMissing
      ? "The selected map feature has no governed evidence reference."
      : "The governed map-evidence request could not be completed safely.",
  );

  return Object.freeze({
    selection,
    code,
    drawerInput,
    drawer: resolveEvidenceDrawer(drawerInput),
  });
}

/**
 * Resolve one map click through an injected governed resolver.
 *
 * This function performs no network, source, policy, evidence-store, lifecycle,
 * renderer, or model access. The injected resolver owns transport. The browser
 * bridge only validates candidate scope and ensures returned evidence remains a
 * subset of the clicked selection's declared governed evidence references.
 */
export async function resolveMapFeatureEvidence(
  selectionInput: unknown,
  resolver: GovernedMapEvidenceResolver,
): Promise<MapEvidenceResolution> {
  const selection = parseMapFeatureSelection(selectionInput);
  if (selection === null) {
    return localResolution(null, "SELECTION_INVALID");
  }

  if (selection.evidenceRefs.length === 0) {
    return localResolution(selection, "MISSING_EVIDENCE");
  }

  let drawerInput: unknown;
  try {
    drawerInput = await resolver(selection);
  } catch {
    return localResolution(selection, "GOVERNED_RESOLVER_ERROR");
  }

  const drawer = resolveEvidenceDrawer(drawerInput);
  const allowedEvidence = new Set(selection.evidenceRefs);
  if (drawer.evidenceRefs.some((evidenceRef) => !allowedEvidence.has(evidenceRef))) {
    return localResolution(selection, "DRAWER_EVIDENCE_OUTSIDE_SELECTION");
  }

  return Object.freeze({
    selection,
    code: drawer.code,
    drawerInput,
    drawer,
  });
}

function isFixtureCase(value: MapEvidenceFixtureCase): boolean {
  return isSafeId(value.caseId) && value.label.trim().length > 0;
}

/**
 * Mount a deterministic browser fixture that models map-feature clicks.
 *
 * Real MapLibre integration can later translate renderer click events into the
 * same strict selection shape. This fixture deliberately uses ordinary buttons
 * so keyboard, focus, finite outcomes, and no-leak behavior can be proven before
 * a renderer dependency is admitted.
 */
export function mountMapFeatureEvidenceFixture(
  host: HTMLElement,
  cases: readonly MapEvidenceFixtureCase[],
  resolver: GovernedMapEvidenceResolver,
): MapEvidenceFixtureController {
  if (cases.length === 0 || !cases.every(isFixtureCase)) {
    throw new Error("Map evidence fixture cases are invalid.");
  }
  if (new Set(cases.map((item) => item.caseId)).size !== cases.length) {
    throw new Error("Map evidence fixture case IDs must be unique.");
  }

  const document = host.ownerDocument;
  const region = document.createElement("section");
  const heading = document.createElement("h2");
  const guidance = document.createElement("p");
  const controls = document.createElement("div");
  const status = document.createElement("p");
  const drawerHost = document.createElement("div");
  const buttons = new Map<string, HTMLButtonElement>();
  let drawerController: EvidenceDrawerController | null = null;
  let requestVersion = 0;
  let destroyed = false;

  heading.id = "map-evidence-fixture-title";
  heading.textContent = "Synthetic map feature selections";
  guidance.textContent =
    "Each control represents a rendered feature click. Feature properties scope a governed request; they are not evidence.";

  controls.setAttribute("aria-label", "Synthetic map feature selections");
  for (const item of cases) {
    const button = document.createElement("button");
    button.type = "button";
    button.textContent = item.label;
    button.dataset.mapEvidenceCase = item.caseId;
    controls.append(button);
    buttons.set(item.caseId, button);
  }

  status.setAttribute("role", "status");
  status.setAttribute("aria-live", "polite");
  status.dataset.component = "map-evidence-status";
  status.textContent = "ABSTAIN / SELECTION_REQUIRED";

  region.dataset.component = "map-feature-evidence-fixture";
  region.setAttribute("aria-labelledby", heading.id);
  region.replaceChildren(heading, guidance, controls, status, drawerHost);
  host.replaceChildren(region);

  function setButtonsDisabled(disabled: boolean): void {
    for (const button of buttons.values()) button.disabled = disabled;
  }

  async function select(caseId: string): Promise<MapEvidenceResolution | null> {
    const fixtureCase = cases.find((item) => item.caseId === caseId);
    if (fixtureCase === undefined || destroyed) return null;

    const currentRequest = ++requestVersion;
    setButtonsDisabled(true);
    status.textContent = "Resolving governed evidence...";
    status.dataset.mapEvidenceOutcome = "PENDING";

    const result = await resolveMapFeatureEvidence(
      fixtureCase.selection,
      resolver,
    );
    if (destroyed || currentRequest !== requestVersion) return result;

    drawerController?.destroy();
    drawerController = mountEvidenceDrawer(drawerHost, result.drawerInput);
    status.textContent = `${result.drawer.outcome} / ${result.code}`;
    status.dataset.mapEvidenceOutcome = result.drawer.outcome;
    status.dataset.mapEvidenceCode = result.code;
    setButtonsDisabled(false);
    drawerController.open();
    return result;
  }

  const listeners = new Map<HTMLButtonElement, () => void>();
  for (const item of cases) {
    const button = buttons.get(item.caseId);
    if (button === undefined) continue;
    const listener = (): void => {
      void select(item.caseId);
    };
    listeners.set(button, listener);
    button.addEventListener("click", listener);
  }

  function destroy(): void {
    if (destroyed) return;
    destroyed = true;
    requestVersion += 1;
    drawerController?.destroy();
    drawerController = null;
    for (const [button, listener] of listeners) {
      button.removeEventListener("click", listener);
    }
    host.replaceChildren();
  }

  return Object.freeze({ select, destroy });
}
