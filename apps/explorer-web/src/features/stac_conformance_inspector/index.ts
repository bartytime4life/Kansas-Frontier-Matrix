import {
  parseStacConformanceInspectorProjection,
  type StacCollectionContract,
  type StacConformanceClass,
  type StacConformanceInspectorOutcome,
  type StacExtensionUse,
  type StacIdentityRule,
  type StacInspectionState,
  type StacMimeTypeCheck,
} from "../../adapters/StacConformanceInspectorProjection";

export type StacConformanceInspectorCode =
  | "INSPECTION_AVAILABLE"
  | "INSPECTION_UNAVAILABLE"
  | "POLICY_DENIED"
  | "UPSTREAM_ERROR"
  | "NO_GOVERNED_RESPONSE"
  | "INVALID_PAYLOAD";

export type StacConformanceInspectorViewModel = Readonly<{
  outcome: StacConformanceInspectorOutcome;
  code: StacConformanceInspectorCode;
  title: string;
  message: string;
  evaluatedAt: string | null;
  inspectionId: string | null;
  specHash: string | null;
  profileVersion: string | null;
  stacVersion: string | null;
  inspectionState: StacInspectionState | null;
  itemCount: number | null;
  conformanceClasses: readonly StacConformanceClass[];
  extensions: readonly StacExtensionUse[];
  identityRules: readonly StacIdentityRule[];
  mimeTypes: readonly StacMimeTypeCheck[];
  collectionContract: StacCollectionContract | null;
  canQueryCatalog: false;
  canValidateSourceBytes: false;
  canMutateCatalog: false;
  canAdmitSource: false;
  canEvaluatePolicy: false;
  canApprove: false;
  canRelease: false;
  canPublish: false;
  accessibilityLabel: string;
  ariaLive: "polite" | "assertive";
}>;

export type StacConformanceInspectorController = Readonly<{
  state: StacConformanceInspectorViewModel;
  destroy: () => void;
}>;

const EMPTY_CLASSES = Object.freeze([]) as readonly StacConformanceClass[];
const EMPTY_EXTENSIONS = Object.freeze([]) as readonly StacExtensionUse[];
const EMPTY_RULES = Object.freeze([]) as readonly StacIdentityRule[];
const EMPTY_MIME_TYPES = Object.freeze([]) as readonly StacMimeTypeCheck[];

function fixedNegativeView(
  code: "NO_GOVERNED_RESPONSE" | "INVALID_PAYLOAD",
): StacConformanceInspectorViewModel {
  const invalid = code === "INVALID_PAYLOAD";
  return Object.freeze({
    outcome: invalid ? "ERROR" : "ABSTAIN",
    code,
    title: "STAC conformance inspection unavailable",
    message: invalid
      ? "The governed projection is invalid. No inspection detail is displayed."
      : "No governed STAC conformance inspection projection is available.",
    evaluatedAt: null,
    inspectionId: null,
    specHash: null,
    profileVersion: null,
    stacVersion: null,
    inspectionState: null,
    itemCount: null,
    conformanceClasses: EMPTY_CLASSES,
    extensions: EMPTY_EXTENSIONS,
    identityRules: EMPTY_RULES,
    mimeTypes: EMPTY_MIME_TYPES,
    collectionContract: null,
    canQueryCatalog: false,
    canValidateSourceBytes: false,
    canMutateCatalog: false,
    canAdmitSource: false,
    canEvaluatePolicy: false,
    canApprove: false,
    canRelease: false,
    canPublish: false,
    accessibilityLabel: invalid
      ? "STAC conformance inspector: error"
      : "STAC conformance inspector: unavailable",
    ariaLive: invalid ? "assertive" : "polite",
  });
}

function titleFor(outcome: StacConformanceInspectorOutcome): string {
  if (outcome === "AVAILABLE") return "STAC conformance inspector";
  if (outcome === "ABSTAIN") return "STAC conformance inspection unavailable";
  if (outcome === "DENY") return "STAC conformance inspection withheld";
  return "STAC conformance inspection failed";
}

function messageFor(outcome: StacConformanceInspectorOutcome): string {
  if (outcome === "AVAILABLE") {
    return "Precomputed STAC profile findings are available for review. This surface does not query or mutate a catalog, validate source bytes, or authorize evidence, policy, release, or publication state.";
  }
  if (outcome === "ABSTAIN") {
    return "The governed inspection is unavailable. No STAC detail is displayed.";
  }
  if (outcome === "DENY") {
    return "Policy denies this projection. The inspector cannot override that decision.";
  }
  return "The upstream inspection failed. No STAC detail is displayed.";
}

/** Resolve a closed STAC conformance projection into a read-only view. */
export function resolveStacConformanceInspector(
  input?: unknown,
): StacConformanceInspectorViewModel {
  if (input === undefined) return fixedNegativeView("NO_GOVERNED_RESPONSE");
  const parsed = parseStacConformanceInspectorProjection(input);
  if (!parsed.ok) return fixedNegativeView("INVALID_PAYLOAD");
  const { payload } = parsed;
  return Object.freeze({
    outcome: payload.outcome,
    code: payload.reasonCode,
    title: titleFor(payload.outcome),
    message: messageFor(payload.outcome),
    evaluatedAt: payload.evaluatedAt,
    inspectionId: payload.inspectionId,
    specHash: payload.specHash,
    profileVersion: payload.profileVersion,
    stacVersion: payload.stacVersion,
    inspectionState: payload.inspectionState,
    itemCount: payload.itemCount,
    conformanceClasses: payload.conformanceClasses,
    extensions: payload.extensions,
    identityRules: payload.identityRules,
    mimeTypes: payload.mimeTypes,
    collectionContract: payload.collectionContract,
    canQueryCatalog: false,
    canValidateSourceBytes: false,
    canMutateCatalog: false,
    canAdmitSource: false,
    canEvaluatePolicy: false,
    canApprove: false,
    canRelease: false,
    canPublish: false,
    accessibilityLabel: `STAC conformance inspector: ${payload.outcome.toLowerCase()}`,
    ariaLive:
      payload.outcome === "ERROR" ||
      payload.outcome === "DENY" ||
      payload.inspectionState === "NON_CONFORMANT"
        ? "assertive"
        : "polite",
  });
}

function appendDefinition(
  document: Document,
  list: HTMLDListElement,
  label: string,
  value: string,
): void {
  const term = document.createElement("dt");
  const definition = document.createElement("dd");
  term.textContent = label;
  definition.textContent = value;
  list.append(term, definition);
}

function cell(document: Document, value: string): HTMLTableCellElement {
  const element = document.createElement("td");
  element.textContent = value;
  return element;
}

function header(document: Document, value: string): HTMLTableCellElement {
  const element = document.createElement("th");
  element.scope = "col";
  element.textContent = value;
  return element;
}

function addCheckTable(
  document: Document,
  section: HTMLElement,
  captionText: string,
  rows: readonly Readonly<{
    id: string;
    status: string;
    count: number;
    findings: readonly string[];
  }>[],
): void {
  const table = document.createElement("table");
  const caption = document.createElement("caption");
  const head = document.createElement("thead");
  const headerRow = document.createElement("tr");
  const body = document.createElement("tbody");
  caption.textContent = captionText;
  headerRow.replaceChildren(
    ...["Check", "Status", "Count", "Findings"].map((label) =>
      header(document, label),
    ),
  );
  head.replaceChildren(headerRow);
  body.replaceChildren(
    ...rows.map((item) => {
      const row = document.createElement("tr");
      row.replaceChildren(
        cell(document, item.id),
        cell(document, item.status),
        cell(document, String(item.count)),
        cell(document, item.findings.join(", ") || "None"),
      );
      return row;
    }),
  );
  table.replaceChildren(caption, head, body);
  section.append(table);
}

/** Mount an accessible, non-interactive STAC conformance inspector. */
export function mountStacConformanceInspector(
  host: HTMLElement,
  input?: unknown,
): StacConformanceInspectorController {
  const state = resolveStacConformanceInspector(input);
  const document = host.ownerDocument;
  const section = document.createElement("section");
  const heading = document.createElement("h2");
  const outcome = document.createElement("p");
  const message = document.createElement("p");
  const details = document.createElement("dl");

  section.dataset.component = "stac-conformance-inspector";
  section.dataset.outcome = state.outcome;
  if (state.inspectionState !== null) {
    section.dataset.inspectionState = state.inspectionState;
  }
  section.setAttribute("role", "region");
  section.setAttribute("aria-label", state.accessibilityLabel);
  heading.textContent = state.title;
  outcome.textContent = `${state.outcome} / ${state.code}`;
  outcome.setAttribute("aria-live", state.ariaLive);
  message.textContent = state.message;
  appendDefinition(document, details, "Inspection state", state.inspectionState ?? "unavailable");
  appendDefinition(document, details, "Inspection identity", state.inspectionId ?? "unavailable");
  appendDefinition(document, details, "Spec hash", state.specHash ?? "unavailable");
  appendDefinition(document, details, "STAC version", state.stacVersion ?? "unavailable");
  appendDefinition(document, details, "KFM profile version", state.profileVersion ?? "unavailable");
  appendDefinition(document, details, "Items inspected", state.itemCount === null ? "unavailable" : String(state.itemCount));
  appendDefinition(document, details, "Evaluated at", state.evaluatedAt ?? "unavailable");
  section.replaceChildren(heading, outcome, message, details);

  if (state.outcome === "AVAILABLE" && state.collectionContract !== null) {
    addCheckTable(
      document,
      section,
      "STAC conformance classes",
      state.conformanceClasses.map((item) => ({
        id: item.classId,
        status: item.status,
        count: item.checkedCount,
        findings: item.findingCodes,
      })),
    );
    addCheckTable(
      document,
      section,
      "STAC identity rules",
      state.identityRules.map((item) => ({
        id: item.ruleId,
        status: item.status,
        count: item.checkedCount,
        findings: item.findingCodes,
      })),
    );
    addCheckTable(
      document,
      section,
      "Declared asset media types",
      state.mimeTypes.map((item) => ({
        id: item.mediaType,
        status: item.status,
        count: item.assetCount,
        findings: item.findingCodes,
      })),
    );

    const extensionList = document.createElement("dl");
    for (const extension of state.extensions) {
      appendDefinition(
        document,
        extensionList,
        `Extension ${extension.extensionId}`,
        `${extension.status}; ${extension.itemCount} items`,
      );
    }
    appendDefinition(
      document,
      extensionList,
      "Collection contract",
      `${state.collectionContract.status}; ${state.collectionContract.presentFieldCount}/${state.collectionContract.requiredFieldCount} required fields; findings: ${state.collectionContract.findingCodes.join(", ") || "None"}`,
    );
    appendDefinition(
      document,
      extensionList,
      "Collection reference",
      state.collectionContract.collectionRef,
    );
    section.append(extensionList);
  }

  host.replaceChildren(section);
  return Object.freeze({ state, destroy: () => host.replaceChildren() });
}
