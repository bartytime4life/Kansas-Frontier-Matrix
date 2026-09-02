import {
  parseWatcherRegistryBrowserProjection,
  type WatcherRegistryBrowserEntry,
  type WatcherRegistryBrowserOutcome,
} from "../../adapters/WatcherRegistryBrowserProjection";

export type WatcherRegistryBrowserCode =
  | "REGISTRY_AVAILABLE"
  | "REGISTRY_UNAVAILABLE"
  | "POLICY_DENIED"
  | "UPSTREAM_ERROR"
  | "NO_GOVERNED_RESPONSE"
  | "INVALID_PAYLOAD";

export type WatcherRegistryBrowserViewModel = Readonly<{
  outcome: WatcherRegistryBrowserOutcome;
  code: WatcherRegistryBrowserCode;
  title: string;
  message: string;
  evaluatedAt: string | null;
  registryId: string | null;
  registrySpecHash: string | null;
  registryStatus: "PROPOSED_INACTIVE" | null;
  watchers: readonly WatcherRegistryBrowserEntry[];
  canReadRegistry: false;
  canRunWatcher: false;
  canActivateSource: false;
  canWriteLifecycle: false;
  canEvaluatePolicy: false;
  canRelease: false;
  canPublish: false;
  accessibilityLabel: string;
  ariaLive: "polite" | "assertive";
}>;

export type WatcherRegistryBrowserController = Readonly<{
  state: WatcherRegistryBrowserViewModel;
  destroy: () => void;
}>;

const EMPTY_WATCHERS = Object.freeze([]) as readonly WatcherRegistryBrowserEntry[];

function fixedNegativeView(
  code: "NO_GOVERNED_RESPONSE" | "INVALID_PAYLOAD",
): WatcherRegistryBrowserViewModel {
  const invalid = code === "INVALID_PAYLOAD";
  return Object.freeze({
    outcome: invalid ? "ERROR" : "ABSTAIN",
    code,
    title: "Watcher Registry unavailable",
    message: invalid
      ? "The governed projection is invalid. No watcher detail is displayed."
      : "No governed Watcher Registry browser projection is available.",
    evaluatedAt: null,
    registryId: null,
    registrySpecHash: null,
    registryStatus: null,
    watchers: EMPTY_WATCHERS,
    canReadRegistry: false,
    canRunWatcher: false,
    canActivateSource: false,
    canWriteLifecycle: false,
    canEvaluatePolicy: false,
    canRelease: false,
    canPublish: false,
    accessibilityLabel: invalid
      ? "Watcher Registry browser: error"
      : "Watcher Registry browser: unavailable",
    ariaLive: invalid ? "assertive" : "polite",
  });
}

function titleFor(outcome: WatcherRegistryBrowserOutcome): string {
  if (outcome === "AVAILABLE") return "Watcher Registry browser";
  if (outcome === "ABSTAIN") return "Watcher Registry unavailable";
  if (outcome === "DENY") return "Watcher Registry withheld";
  return "Watcher Registry failed";
}

function messageFor(outcome: WatcherRegistryBrowserOutcome): string {
  if (outcome === "AVAILABLE") {
    return "Inactive watcher metadata is available for review. This surface cannot read the registry, run a watcher, activate a source, or authorize lifecycle, release, or publication actions.";
  }
  if (outcome === "ABSTAIN") {
    return "The governed projection is unavailable. No watcher detail is displayed.";
  }
  if (outcome === "DENY") {
    return "Policy denies this projection. The browser cannot override that decision.";
  }
  return "The upstream projection failed. No watcher detail is displayed.";
}

/** Resolve a closed Watcher Registry projection into a read-only view. */
export function resolveWatcherRegistryBrowser(
  input?: unknown,
): WatcherRegistryBrowserViewModel {
  if (input === undefined) return fixedNegativeView("NO_GOVERNED_RESPONSE");
  const parsed = parseWatcherRegistryBrowserProjection(input);
  if (!parsed.ok) return fixedNegativeView("INVALID_PAYLOAD");
  const { payload } = parsed;
  return Object.freeze({
    outcome: payload.outcome,
    code: payload.reasonCode,
    title: titleFor(payload.outcome),
    message: messageFor(payload.outcome),
    evaluatedAt: payload.evaluatedAt,
    registryId: payload.registryId,
    registrySpecHash: payload.registrySpecHash,
    registryStatus: payload.registryStatus,
    watchers: payload.watchers,
    canReadRegistry: false,
    canRunWatcher: false,
    canActivateSource: false,
    canWriteLifecycle: false,
    canEvaluatePolicy: false,
    canRelease: false,
    canPublish: false,
    accessibilityLabel: `Watcher Registry browser: ${payload.outcome.toLowerCase()}`,
    ariaLive: payload.outcome === "ERROR" || payload.outcome === "DENY" ? "assertive" : "polite",
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

/** Mount an accessible, non-interactive Watcher Registry browser. */
export function mountWatcherRegistryBrowser(
  host: HTMLElement,
  input?: unknown,
): WatcherRegistryBrowserController {
  const state = resolveWatcherRegistryBrowser(input);
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

  section.dataset.component = "watcher-registry-browser";
  section.dataset.outcome = state.outcome;
  section.setAttribute("role", "region");
  section.setAttribute("aria-label", state.accessibilityLabel);
  heading.textContent = state.title;
  outcome.textContent = `${state.outcome} / ${state.code}`;
  outcome.setAttribute("aria-live", state.ariaLive);
  message.textContent = state.message;

  appendDefinition(document, details, "Registry status", state.registryStatus ?? "unavailable");
  appendDefinition(document, details, "Registry identity", state.registryId ?? "unavailable");
  appendDefinition(document, details, "Registry spec hash", state.registrySpecHash ?? "unavailable");
  appendDefinition(document, details, "Evaluated at", state.evaluatedAt ?? "unavailable");

  caption.textContent = "Closed Watcher Registry projection entries";
  headerRow.replaceChildren(
    ...[
      "Watcher",
      "State",
      "Version",
      "Poll mode",
      "Endpoint",
      "Policy",
      "Outputs",
      "Schema",
      "Spec hash",
      "Signature",
    ].map((label) => header(document, label)),
  );
  head.replaceChildren(headerRow);
  body.replaceChildren(
    ...state.watchers.map((watcher) => {
      const row = document.createElement("tr");
      row.dataset.watcherId = watcher.watcherId;
      row.dataset.watcherState = watcher.state;
      row.replaceChildren(
        cell(document, watcher.watcherId),
        cell(document, watcher.state),
        cell(document, watcher.version),
        cell(document, watcher.pollMode),
        cell(document, watcher.endpointRef ?? "None"),
        cell(document, watcher.policyRef ?? "None"),
        cell(document, watcher.outputTypes.join(", ") || "None"),
        cell(document, watcher.schemaRef ?? "None"),
        cell(document, watcher.specHash),
        cell(document, watcher.signatureRef ?? "None"),
      );
      return row;
    }),
  );
  table.replaceChildren(caption, head, body);
  section.replaceChildren(heading, outcome, message, details, table);
  host.replaceChildren(section);
  return Object.freeze({ state, destroy: () => host.replaceChildren() });
}
