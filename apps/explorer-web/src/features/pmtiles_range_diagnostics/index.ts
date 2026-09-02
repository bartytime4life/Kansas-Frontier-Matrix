import {
  type PmtilesHeadlessRender,
  type PmtilesHttpDiagnostics,
  type PmtilesRangeDiagnosticsOutcome,
  type PmtilesRangeDiagnosticsReasonCode,
  type PmtilesSidecarDiagnostics,
  type PmtilesVerifiedRange,
  parsePmtilesRangeDiagnosticsProjection,
} from "../../adapters/PmtilesRangeDiagnosticsProjection";

export type PmtilesRangeDiagnosticsViewModel = Readonly<{
  visibility: "VISIBLE" | "HIDDEN";
  outcome: PmtilesRangeDiagnosticsOutcome;
  code:
    | PmtilesRangeDiagnosticsReasonCode
    | "NO_GOVERNED_RESPONSE"
    | "INVALID_PAYLOAD";
  heading: string;
  summary: string;
  observedAt: string | null;
  artifactRef: string | null;
  verificationState: "STRUCTURAL_HOLD" | null;
  http: PmtilesHttpDiagnostics | null;
  sidecars: PmtilesSidecarDiagnostics | null;
  verifiedRange: PmtilesVerifiedRange | null;
  checks: readonly string[];
  holds: readonly string[];
  headlessRender: PmtilesHeadlessRender | null;
  ariaLive: "polite" | "assertive";
}>;

export type PmtilesRangeDiagnosticsController = Readonly<{
  state: PmtilesRangeDiagnosticsViewModel;
  destroy: () => void;
}>;

const EMPTY: readonly string[] = Object.freeze([]);
const NEGATIVE_COPY: Readonly<
  Record<
    Exclude<PmtilesRangeDiagnosticsReasonCode, "DIAGNOSTICS_AVAILABLE">,
    Readonly<{
      outcome: Exclude<PmtilesRangeDiagnosticsOutcome, "ANSWER">;
      heading: string;
      summary: string;
      ariaLive: "polite" | "assertive";
    }>
  >
> = Object.freeze({
  DIAGNOSTICS_UNAVAILABLE: Object.freeze({
    outcome: "ABSTAIN",
    heading: "PMTiles diagnostics unavailable",
    summary: "A complete governed diagnostic projection is not available.",
    ariaLive: "polite",
  }),
  VERIFICATION_DENIED: Object.freeze({
    outcome: "DENY",
    heading: "PMTiles diagnostics withheld",
    summary: "The supplied verification result is denied for this display surface.",
    ariaLive: "assertive",
  }),
  UPSTREAM_ERROR: Object.freeze({
    outcome: "ERROR",
    heading: "PMTiles diagnostics unavailable",
    summary: "The governed diagnostic projection could not be completed.",
    ariaLive: "assertive",
  }),
});

function hidden(
  code: "NO_GOVERNED_RESPONSE" | "INVALID_PAYLOAD",
): PmtilesRangeDiagnosticsViewModel {
  return Object.freeze({
    visibility: "HIDDEN",
    outcome: "ERROR",
    code,
    heading: "PMTiles diagnostics unavailable",
    summary: "No diagnostics are rendered without a valid governed projection.",
    observedAt: null,
    artifactRef: null,
    verificationState: null,
    http: null,
    sidecars: null,
    verifiedRange: null,
    checks: EMPTY,
    holds: EMPTY,
    headlessRender: null,
    ariaLive: "polite",
  });
}

/** Resolve one bounded PMTiles range-diagnostics projection. */
export function resolvePmtilesRangeDiagnostics(
  input?: unknown,
): PmtilesRangeDiagnosticsViewModel {
  if (input === undefined) return hidden("NO_GOVERNED_RESPONSE");
  const parsed = parsePmtilesRangeDiagnosticsProjection(input);
  if (!parsed.ok) return hidden("INVALID_PAYLOAD");
  const { payload } = parsed;

  if (payload.outcome !== "ANSWER") {
    const copy = NEGATIVE_COPY[
      payload.reasonCode as Exclude<
        PmtilesRangeDiagnosticsReasonCode,
        "DIAGNOSTICS_AVAILABLE"
      >
    ];
    return Object.freeze({
      visibility: "VISIBLE",
      outcome: copy.outcome,
      code: payload.reasonCode,
      heading: copy.heading,
      summary: copy.summary,
      observedAt: null,
      artifactRef: null,
      verificationState: null,
      http: null,
      sidecars: null,
      verifiedRange: null,
      checks: EMPTY,
      holds: EMPTY,
      headlessRender: null,
      ariaLive: copy.ariaLive,
    });
  }

  return Object.freeze({
    visibility: "VISIBLE",
    outcome: "ANSWER",
    code: "DIAGNOSTICS_AVAILABLE",
    heading: "PMTiles range diagnostics",
    summary:
      "The captured range is structurally bound to supplied compatibility sidecars, but the result remains on STRUCTURAL_HOLD. It does not prove cryptographic trust, whole-archive integrity, policy approval, artifact health, release, or publication.",
    observedAt: payload.observedAt,
    artifactRef: payload.artifactRef,
    verificationState: payload.verificationState,
    http: payload.http,
    sidecars: payload.sidecars,
    verifiedRange: payload.verifiedRange,
    checks: payload.checks,
    holds: payload.holds,
    headlessRender: payload.headlessRender,
    ariaLive: "polite",
  });
}

function appendDefinition(
  document: Document,
  list: HTMLDListElement,
  term: string,
  value: string,
): void {
  const dt = document.createElement("dt");
  const dd = document.createElement("dd");
  dt.textContent = term;
  dd.textContent = value;
  list.append(dt, dd);
}

/** Mount a text-first, non-interactive PMTiles diagnostic panel. */
export function mountPmtilesRangeDiagnostics(
  host: HTMLElement,
  input?: unknown,
): PmtilesRangeDiagnosticsController {
  const state = resolvePmtilesRangeDiagnostics(input);
  host.replaceChildren();
  if (state.visibility === "HIDDEN") {
    return Object.freeze({ state, destroy: () => host.replaceChildren() });
  }

  const document = host.ownerDocument;
  const section = document.createElement("section");
  const heading = document.createElement("h2");
  const summary = document.createElement("p");
  const headingId = "kfm-pmtiles-range-diagnostics-heading";
  section.dataset.component = "pmtiles-range-diagnostics";
  section.dataset.outcome = state.outcome;
  if (state.verificationState !== null) {
    section.dataset.verificationState = state.verificationState;
  }
  section.setAttribute("role", state.outcome === "ANSWER" ? "region" : "status");
  section.setAttribute("aria-live", state.ariaLive);
  section.setAttribute("aria-labelledby", headingId);
  heading.id = headingId;
  heading.textContent = state.heading;
  summary.textContent = state.summary;
  section.append(heading, summary);

  if (
    state.outcome === "ANSWER" &&
    state.observedAt !== null &&
    state.artifactRef !== null &&
    state.verificationState !== null &&
    state.http !== null &&
    state.sidecars !== null &&
    state.verifiedRange !== null &&
    state.headlessRender !== null
  ) {
    const metadata = document.createElement("dl");
    appendDefinition(document, metadata, "Verification state", state.verificationState);
    appendDefinition(document, metadata, "Observed at", state.observedAt);
    appendDefinition(document, metadata, "Artifact", state.artifactRef);
    appendDefinition(
      document,
      metadata,
      "Verified range",
      `offset ${state.verifiedRange.offset}; length ${state.verifiedRange.length}; leaf ${state.verifiedRange.leaf}`,
    );
    appendDefinition(
      document,
      metadata,
      "HTTP",
      `Range ${state.http.acceptRanges}; Content-Range ${state.http.contentRange}; ETag ${state.http.etag}; cache ${state.http.cache}`,
    );
    appendDefinition(
      document,
      metadata,
      "Sidecars",
      `PMIDX ${state.sidecars.pmidxState}; PMSIG ${state.sidecars.pmsigState}; cryptographic verification ${state.sidecars.cryptographicState}`,
    );
    appendDefinition(
      document,
      metadata,
      "Headless render",
      state.headlessRender.state,
    );

    const checksHeading = document.createElement("h3");
    const checks = document.createElement("ul");
    checksHeading.textContent = "Structural checks";
    for (const check of state.checks) {
      const item = document.createElement("li");
      item.textContent = check;
      checks.append(item);
    }

    const holdsHeading = document.createElement("h3");
    const holds = document.createElement("ul");
    holdsHeading.textContent = "Unresolved holds";
    for (const hold of state.holds) {
      const item = document.createElement("li");
      item.textContent = hold;
      holds.append(item);
    }
    section.append(metadata, checksHeading, checks, holdsHeading, holds);
  }

  host.replaceChildren(section);
  return Object.freeze({ state, destroy: () => host.replaceChildren() });
}
