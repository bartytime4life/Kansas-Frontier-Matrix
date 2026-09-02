import {
  parseViewRegistryInspectionProjection,
  type GovernedViewRegistryEntry,
  type ViewRegistryInspectionOutcome,
  type ViewRegistryInspectionStatus,
} from "../../adapters/ViewRegistryInspectorProjection";

export type ViewRegistryInspectorOutcome = ViewRegistryInspectionOutcome;

export type ViewRegistryInspectorCode =
  | "REGISTRY_INSPECTION_READY"
  | "REGISTRY_INSPECTION_HELD"
  | "REGISTRY_INSPECTION_DENIED"
  | "UPSTREAM_ERROR"
  | "NO_GOVERNED_RESPONSE"
  | "INVALID_PAYLOAD";

export type ViewRegistryInspectorViewModel = Readonly<{
  outcome: ViewRegistryInspectorOutcome;
  code: ViewRegistryInspectorCode;
  title: string;
  message: string;
  status: ViewRegistryInspectionStatus | null;
  registryId: string | null;
  specHash: string | null;
  entries: readonly GovernedViewRegistryEntry[];
  evaluatedAt: string | null;
  canBindRoute: false;
  canActivateLayer: false;
  canEvaluatePolicy: false;
  canApprove: false;
  canRelease: false;
  canPublish: false;
  accessibilityLabel: string;
  ariaLive: "polite" | "assertive";
}>;

export type ViewRegistryInspectorController = Readonly<{
  state: ViewRegistryInspectorViewModel;
  destroy: () => void;
}>;

const EMPTY_ENTRIES = Object.freeze([]) as readonly GovernedViewRegistryEntry[];

function fixedNegativeView(
  code: "NO_GOVERNED_RESPONSE" | "INVALID_PAYLOAD",
): ViewRegistryInspectorViewModel {
  const invalid = code === "INVALID_PAYLOAD";
  return Object.freeze({
    outcome: invalid ? "ERROR" : "ABSTAIN",
    code,
    title: "View Registry inspection unavailable",
    message: invalid
      ? "The governed projection is invalid. No registry detail is displayed."
      : "No governed View Registry inspection projection is available.",
    status: null,
    registryId: null,
    specHash: null,
    entries: EMPTY_ENTRIES,
    evaluatedAt: null,
    canBindRoute: false,
    canActivateLayer: false,
    canEvaluatePolicy: false,
    canApprove: false,
    canRelease: false,
    canPublish: false,
    accessibilityLabel: invalid
      ? "View Registry inspector: error"
      : "View Registry inspector: unavailable",
    ariaLive: invalid ? "assertive" : "polite",
  });
}

function codeFor(
  outcome: ViewRegistryInspectionOutcome,
): Exclude<
  ViewRegistryInspectorCode,
  "NO_GOVERNED_RESPONSE" | "INVALID_PAYLOAD"
> {
  if (outcome === "AVAILABLE") return "REGISTRY_INSPECTION_READY";
  if (outcome === "ABSTAIN") return "REGISTRY_INSPECTION_HELD";
  if (outcome === "DENY") return "REGISTRY_INSPECTION_DENIED";
  return "UPSTREAM_ERROR";
}

function titleFor(outcome: ViewRegistryInspectionOutcome): string {
  if (outcome === "AVAILABLE") return "View Registry inspection ready";
  if (outcome === "ABSTAIN") return "View Registry inspection held";
  if (outcome === "DENY") return "View Registry inspection denied";
  return "View Registry inspection failed";
}

function messageFor(outcome: ViewRegistryInspectionOutcome): string {
  if (outcome === "AVAILABLE") {
    return "Proposed inactive route metadata is available for maintainer review. This surface cannot bind or publish a view.";
  }
  if (outcome === "ABSTAIN") {
    return "The upstream registry assessment is held. No route or layer detail is displayed.";
  }
  if (outcome === "DENY") {
    return "The governed projection denies registry detail. This surface cannot override the decision.";
  }
  return "The upstream registry assessment failed. No route or layer detail is displayed.";
}

/** Resolve a closed projection into a read-only maintainer view. */
export function resolveViewRegistryInspector(
  input?: unknown,
): ViewRegistryInspectorViewModel {
  if (input === undefined) {
    return fixedNegativeView("NO_GOVERNED_RESPONSE");
  }
  const parsed = parseViewRegistryInspectionProjection(input);
  if (!parsed.ok) {
    return fixedNegativeView("INVALID_PAYLOAD");
  }

  return Object.freeze({
    outcome: parsed.payload.outcome,
    code: codeFor(parsed.payload.outcome),
    title: titleFor(parsed.payload.outcome),
    message: messageFor(parsed.payload.outcome),
    status: parsed.payload.status,
    registryId: parsed.payload.registryId,
    specHash: parsed.payload.specHash,
    entries: parsed.payload.entries,
    evaluatedAt: parsed.payload.evaluatedAt,
    canBindRoute: false,
    canActivateLayer: false,
    canEvaluatePolicy: false,
    canApprove: false,
    canRelease: false,
    canPublish: false,
    accessibilityLabel:
      "View Registry inspector: " + parsed.payload.outcome.toLowerCase(),
    ariaLive: parsed.payload.outcome === "ERROR" ? "assertive" : "polite",
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

function tableCell(document: Document, value: string): HTMLTableCellElement {
  const cell = document.createElement("td");
  cell.textContent = value;
  return cell;
}

function tableHeader(document: Document, value: string): HTMLTableCellElement {
  const cell = document.createElement("th");
  cell.scope = "col";
  cell.textContent = value;
  return cell;
}

/** Mount an accessible, read-only View Registry inspection surface. */
export function mountViewRegistryInspector(
  host: HTMLElement,
  input?: unknown,
): ViewRegistryInspectorController {
  const state = resolveViewRegistryInspector(input);
  const document = host.ownerDocument;
  const section = document.createElement("section");
  const heading = document.createElement("h2");
  const outcome = document.createElement("p");
  const message = document.createElement("p");
  const details = document.createElement("dl");
  const table = document.createElement("table");
  const caption = document.createElement("caption");
  const head = document.createElement("thead");
  const headerRow = document.createElement("tr");
  const body = document.createElement("tbody");

  section.dataset.component = "view-registry-inspector";
  section.dataset.outcome = state.outcome;
  section.setAttribute("role", "region");
  section.setAttribute("aria-label", state.accessibilityLabel);
  heading.textContent = state.title;
  outcome.textContent = state.outcome + " / " + state.code;
  outcome.setAttribute("aria-live", state.ariaLive);
  message.textContent = state.message;

  appendDefinition(
    document,
    details,
    "Registry status",
    state.status ?? "unavailable",
  );
  appendDefinition(
    document,
    details,
    "Registry identity",
    state.registryId ?? "unavailable",
  );
  appendDefinition(
    document,
    details,
    "Registry spec hash",
    state.specHash ?? "unavailable",
  );
  appendDefinition(
    document,
    details,
    "Evaluated at",
    state.evaluatedAt ?? "unavailable",
  );

  caption.textContent = "Proposed inactive View Registry entries";
  headerRow.replaceChildren(
    ...[
      "View",
      "Route",
      "Delivery",
      "Layers",
      "Renderer",
      "Protocol",
      "Performance budget",
      "Access policy",
      "Sensitivity policy",
      "Activation",
    ].map((label) => tableHeader(document, label)),
  );
  head.replaceChildren(headerRow);

  body.replaceChildren(
    ...state.entries.map((entry) => {
      const row = document.createElement("tr");
      row.replaceChildren(
        tableCell(document, entry.viewId),
        tableCell(document, entry.routePath),
        tableCell(document, entry.deliveryKind),
        tableCell(document, entry.layerManifestRefs.join(", ")),
        tableCell(document, entry.renderer),
        tableCell(document, entry.protocol),
        tableCell(document, entry.performanceBudgetRef),
        tableCell(document, entry.accessPolicyRef),
        tableCell(document, entry.sensitivityPolicyRef),
        tableCell(document, entry.activationState),
      );
      return row;
    }),
  );
  table.replaceChildren(caption, head, body);
  table.hidden = state.entries.length === 0;
  section.replaceChildren(heading, outcome, message, details, table);
  host.replaceChildren(section);

  return Object.freeze({
    state,
    destroy(): void {
      host.replaceChildren();
    },
  });
}
