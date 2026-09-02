import {
  parseHucCrosswalkProjection,
  type HucCrosswalkOutcome,
  type HucCrosswalkStatus,
} from "../../adapters/HucCrosswalkProjection";

export type HucCrosswalkExplorerOutcome = HucCrosswalkOutcome | "ERROR";
export type HucCrosswalkExplorerCode =
  | "CROSSWALK_REFERENCE_READY"
  | "CROSSWALK_REFERENCE_HELD"
  | "CROSSWALK_REFERENCE_DENIED"
  | "NO_GOVERNED_RESPONSE"
  | "INVALID_PAYLOAD";

export type HucCrosswalkExplorerViewModel = Readonly<{
  outcome: HucCrosswalkExplorerOutcome;
  code: HucCrosswalkExplorerCode;
  title: string;
  message: string;
  countyFips: string | null;
  huc12: string | null;
  status: HucCrosswalkStatus | null;
  sourceHash: string | null;
  crosswalkRef: string | null;
  crosswalkDigest: string | null;
  validationReceiptRef: string | null;
  stationRefs: readonly string[];
  evaluatedAt: string | null;
  canFetch: false;
  canChangeCrosswalk: false;
  canRelease: false;
  accessibilityLabel: string;
  ariaLive: "polite" | "assertive";
}>;

export type HucCrosswalkExplorerController = Readonly<{
  state: HucCrosswalkExplorerViewModel;
  destroy: () => void;
}>;

const EMPTY_STATIONS = Object.freeze([]) as readonly string[];

function fixedNegativeView(
  code: "NO_GOVERNED_RESPONSE" | "INVALID_PAYLOAD",
): HucCrosswalkExplorerViewModel {
  const invalid = code === "INVALID_PAYLOAD";
  return Object.freeze({
    outcome: invalid ? "ERROR" : "ABSTAIN",
    code,
    title: "HUC crosswalk reference unavailable",
    message: invalid
      ? "The governed projection is invalid. No crosswalk detail is displayed."
      : "No governed HUC crosswalk projection is available.",
    countyFips: null,
    huc12: null,
    status: null,
    sourceHash: null,
    crosswalkRef: null,
    crosswalkDigest: null,
    validationReceiptRef: null,
    stationRefs: EMPTY_STATIONS,
    evaluatedAt: null,
    canFetch: false,
    canChangeCrosswalk: false,
    canRelease: false,
    accessibilityLabel: invalid
      ? "HUC crosswalk explorer: error"
      : "HUC crosswalk explorer: unavailable",
    ariaLive: invalid ? "assertive" : "polite",
  });
}

function titleFor(outcome: HucCrosswalkOutcome): string {
  if (outcome === "AVAILABLE") return "HUC crosswalk reference available";
  if (outcome === "DENY") return "HUC crosswalk reference denied";
  return "HUC crosswalk reference held";
}

function messageFor(outcome: HucCrosswalkOutcome): string {
  if (outcome === "AVAILABLE") {
    return "Digest-bound station references are available for review. This surface does not verify or release them.";
  }
  if (outcome === "DENY") {
    return "The governed projection denies display of station references. This surface cannot override the decision.";
  }
  return "The crosswalk is ambiguous, stale, or unresolved. No station reference is displayed.";
}

/** Resolve a closed projection into a read-only reviewer view. */
export function resolveHucCrosswalkExplorer(
  input?: unknown,
): HucCrosswalkExplorerViewModel {
  if (input === undefined) return fixedNegativeView("NO_GOVERNED_RESPONSE");
  const parsed = parseHucCrosswalkProjection(input);
  if (!parsed.ok) return fixedNegativeView("INVALID_PAYLOAD");
  const code =
    parsed.payload.outcome === "AVAILABLE"
      ? "CROSSWALK_REFERENCE_READY"
      : parsed.payload.outcome === "DENY"
        ? "CROSSWALK_REFERENCE_DENIED"
        : "CROSSWALK_REFERENCE_HELD";
  return Object.freeze({
    outcome: parsed.payload.outcome,
    code,
    title: titleFor(parsed.payload.outcome),
    message: messageFor(parsed.payload.outcome),
    countyFips: parsed.payload.countyFips,
    huc12: parsed.payload.huc12,
    status: parsed.payload.status,
    sourceHash: parsed.payload.sourceHash,
    crosswalkRef: parsed.payload.crosswalkRef,
    crosswalkDigest: parsed.payload.crosswalkDigest,
    validationReceiptRef: parsed.payload.validationReceiptRef,
    stationRefs: parsed.payload.stationRefs,
    evaluatedAt: parsed.payload.evaluatedAt,
    canFetch: false,
    canChangeCrosswalk: false,
    canRelease: false,
    accessibilityLabel: `HUC crosswalk explorer: ${parsed.payload.outcome.toLowerCase()}`,
    ariaLive: "polite",
  });
}

function textOrUnavailable(label: string, value: string | null): string {
  return `${label}: ${value ?? "unavailable"}`;
}

/** Mount a read-only, accessible HUC crosswalk reference surface. */
export function mountHucCrosswalkExplorer(
  host: HTMLElement,
  input?: unknown,
): HucCrosswalkExplorerController {
  const state = resolveHucCrosswalkExplorer(input);
  const document = host.ownerDocument;
  const section = document.createElement("section");
  const heading = document.createElement("h2");
  const outcome = document.createElement("p");
  const message = document.createElement("p");
  const details = document.createElement("dl");
  const stationsHeading = document.createElement("h3");
  const stations = document.createElement("ol");

  section.dataset.component = "huc-crosswalk-explorer";
  section.dataset.outcome = state.outcome;
  section.setAttribute("role", "region");
  section.setAttribute("aria-label", state.accessibilityLabel);
  heading.textContent = state.title;
  outcome.textContent = `${state.outcome} / ${state.code}`;
  outcome.setAttribute("aria-live", state.ariaLive);
  message.textContent = state.message;

  const detailRows = [
    textOrUnavailable("County FIPS", state.countyFips),
    textOrUnavailable("HUC12", state.huc12),
    textOrUnavailable("Crosswalk status", state.status),
    textOrUnavailable("Source hash", state.sourceHash),
    textOrUnavailable("Crosswalk digest", state.crosswalkDigest),
    textOrUnavailable("Crosswalk reference", state.crosswalkRef),
    textOrUnavailable("Validation receipt", state.validationReceiptRef),
    textOrUnavailable("Evaluated at", state.evaluatedAt),
  ];
  details.replaceChildren(
    ...detailRows.flatMap((row) => {
      const [label, ...valueParts] = row.split(": ");
      const term = document.createElement("dt");
      const value = document.createElement("dd");
      term.textContent = label;
      value.textContent = valueParts.join(": ");
      return [term, value];
    }),
  );

  stationsHeading.textContent = "Station references";
  stations.replaceChildren(
    ...state.stationRefs.map((reference) => {
      const item = document.createElement("li");
      const code = document.createElement("code");
      code.textContent = reference;
      item.replaceChildren(code);
      return item;
    }),
  );
  stations.hidden = state.stationRefs.length === 0;
  section.replaceChildren(
    heading,
    outcome,
    message,
    details,
    stationsHeading,
    stations,
  );
  host.replaceChildren(section);

  return Object.freeze({
    state,
    destroy(): void {
      host.replaceChildren();
    },
  });
}
