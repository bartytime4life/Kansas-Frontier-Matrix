import {
  type GeometryTransformSummary,
  type GovernedRedactionPreviewProjection,
  type PublicSafeAbstractionKind,
  type RedactionPreviewOutcome,
  type RedactionPreviewReasonCode,
  type SuppressionTransformSummary,
  parseRedactionPreviewProjection,
} from "../../adapters/RedactionPreviewProjection";

export type RedactionPreviewCode =
  | RedactionPreviewReasonCode
  | "NO_GOVERNED_RESPONSE"
  | "INVALID_PAYLOAD";

export type RedactionPreviewItemKind =
  | "GEOMETRY"
  | "SUPPRESSION"
  | "ZOOM_LIMIT"
  | "ABSTRACTION";

export type RedactionPreviewItem = Readonly<{
  kind: RedactionPreviewItemKind;
  label: string;
  value: string;
  explanation: string;
}>;

export type RedactionPreviewViewModel = Readonly<{
  outcome: RedactionPreviewOutcome;
  code: RedactionPreviewCode;
  title: string;
  message: string;
  evaluatedAtLabel: string;
  items: readonly RedactionPreviewItem[];
  canInspectReceipt: boolean;
  canApprove: false;
  canRelease: false;
  accessibilityLabel: string;
  ariaLive: "polite" | "assertive";
}>;

export type RedactionPreviewMountOptions = Readonly<{
  onInspectReceipt?: (payload: GovernedRedactionPreviewProjection) => void;
}>;

export type RedactionPreviewController = Readonly<{
  state: RedactionPreviewViewModel;
  destroy: () => void;
}>;

type ResolvedRedactionPreview = Readonly<{
  state: RedactionPreviewViewModel;
  payload: GovernedRedactionPreviewProjection | null;
}>;

const EMPTY_ITEMS = Object.freeze([]) as readonly RedactionPreviewItem[];

const GEOMETRY_COPY: Readonly<
  Record<GeometryTransformSummary, Readonly<{ value: string; explanation: string }>>
> = Object.freeze({
  GEOMETRY_GENERALIZED: Object.freeze({
    value: "Generalized",
    explanation:
      "The candidate exposes a public-safe generalized shape, not restricted source geometry.",
  }),
  GEOMETRY_WITHHELD: Object.freeze({
    value: "Withheld",
    explanation:
      "No geometry is exposed by this candidate preview.",
  }),
  GEOMETRY_NOT_APPLICABLE: Object.freeze({
    value: "Not applicable",
    explanation:
      "This public-safe candidate does not contain a geometry representation.",
  }),
});

const SUPPRESSION_COPY: Readonly<
  Record<SuppressionTransformSummary, Readonly<{ value: string; explanation: string }>>
> = Object.freeze({
  LOW_COUNT_SUPPRESSED: Object.freeze({
    value: "Low-count cells suppressed",
    explanation:
      "Cells below the governed disclosure threshold are absent; counts and thresholds are not displayed.",
  }),
  ALL_COUNTS_WITHHELD: Object.freeze({
    value: "Counts withheld",
    explanation:
      "The candidate exposes no count values through this preview.",
  }),
  SUPPRESSION_NOT_APPLICABLE: Object.freeze({
    value: "Not applicable",
    explanation:
      "The public-safe candidate does not contain a count-bearing representation.",
  }),
});

const ABSTRACTION_COPY: Readonly<Record<PublicSafeAbstractionKind, string>> =
  Object.freeze({
    COUNTY_AGGREGATE: "County aggregate",
    WATERSHED_AGGREGATE: "Watershed aggregate",
    GRID_AGGREGATE: "Grid aggregate",
    TEMPORAL_BUCKET: "Temporal bucket",
    PUBLIC_SAFE_SYMBOL: "Public-safe symbol",
    FEATURES_WITHHELD: "Features withheld",
  });

const NEGATIVE_COPY: Readonly<
  Record<
    Exclude<RedactionPreviewCode, "PREVIEW_READY">,
    Readonly<{
      outcome: RedactionPreviewOutcome;
      title: string;
      message: string;
      ariaLive: "polite" | "assertive";
    }>
  >
> = Object.freeze({
  NO_GOVERNED_RESPONSE: Object.freeze({
    outcome: "ABSTAIN",
    title: "Redaction preview unavailable",
    message:
      "No governed redaction-preview projection is available. Release review must remain incomplete.",
    ariaLive: "polite",
  }),
  INVALID_PAYLOAD: Object.freeze({
    outcome: "ERROR",
    title: "Redaction preview unavailable",
    message:
      "The governed redaction-preview projection is invalid. No candidate details are displayed.",
    ariaLive: "assertive",
  }),
  PREVIEW_INCOMPLETE: Object.freeze({
    outcome: "ABSTAIN",
    title: "Redaction preview incomplete",
    message:
      "Required public-safe transform summaries are incomplete. Release review must remain incomplete.",
    ariaLive: "polite",
  }),
  POLICY_DENIED: Object.freeze({
    outcome: "DENY",
    title: "Redaction preview denied",
    message:
      "Policy does not permit a redaction preview for this candidate. No candidate details are displayed.",
    ariaLive: "assertive",
  }),
  UPSTREAM_ERROR: Object.freeze({
    outcome: "ERROR",
    title: "Redaction preview unavailable",
    message:
      "The governed redaction service could not complete the preview.",
    ariaLive: "assertive",
  }),
});

function negativeState(
  code: Exclude<RedactionPreviewCode, "PREVIEW_READY">,
): RedactionPreviewViewModel {
  const copy = NEGATIVE_COPY[code];
  return Object.freeze({
    outcome: copy.outcome,
    code,
    title: copy.title,
    message: copy.message,
    evaluatedAtLabel: "Evaluation time: unavailable",
    items: EMPTY_ITEMS,
    canInspectReceipt: false,
    canApprove: false,
    canRelease: false,
    accessibilityLabel: `Redaction preview: ${copy.outcome.toLowerCase()}`,
    ariaLive: copy.ariaLive,
  });
}

function positiveItems(
  payload: GovernedRedactionPreviewProjection,
): readonly RedactionPreviewItem[] {
  const geometry = GEOMETRY_COPY[payload.geometryTransform as GeometryTransformSummary];
  const suppression =
    SUPPRESSION_COPY[payload.suppressionTransform as SuppressionTransformSummary];
  return Object.freeze([
    Object.freeze({
      kind: "GEOMETRY" as const,
      label: "Geometry",
      value: geometry.value,
      explanation: geometry.explanation,
    }),
    Object.freeze({
      kind: "SUPPRESSION" as const,
      label: "Low-count protection",
      value: suppression.value,
      explanation: suppression.explanation,
    }),
    Object.freeze({
      kind: "ZOOM_LIMIT" as const,
      label: "Maximum public zoom",
      value: `z${payload.maximumPublicZoom as number}`,
      explanation:
        "The preview reports the governed public zoom ceiling; it grants no access above that limit.",
    }),
    Object.freeze({
      kind: "ABSTRACTION" as const,
      label: "Public-safe abstraction",
      value: ABSTRACTION_COPY[payload.abstractionKind as PublicSafeAbstractionKind],
      explanation:
        "The label describes the released representation class, not canonical or restricted source truth.",
    }),
  ]);
}

function resolveProjection(input: unknown | undefined): ResolvedRedactionPreview {
  if (input === undefined) {
    return Object.freeze({
      state: negativeState("NO_GOVERNED_RESPONSE"),
      payload: null,
    });
  }
  const parsed = parseRedactionPreviewProjection(input);
  if (!parsed.ok) {
    return Object.freeze({
      state: negativeState("INVALID_PAYLOAD"),
      payload: null,
    });
  }
  const { payload } = parsed;
  if (payload.outcome !== "ANSWER") {
    return Object.freeze({
      state: negativeState(
        payload.reasonCode as Exclude<RedactionPreviewReasonCode, "PREVIEW_READY">,
      ),
      payload: null,
    });
  }

  return Object.freeze({
    payload,
    state: Object.freeze({
      outcome: "ANSWER",
      code: "PREVIEW_READY",
      title: "Public-safe redaction preview",
      message:
        "Review the declared public-safe transforms before release. This preview is not policy approval, release approval, publication, or proof that the transform is sufficient.",
      evaluatedAtLabel: `Evaluation time: ${payload.evaluatedAt as string}`,
      items: positiveItems(payload),
      canInspectReceipt: true,
      canApprove: false,
      canRelease: false,
      accessibilityLabel: "Redaction preview: public-safe transforms ready",
      ariaLive: "polite",
    }),
  });
}

/** Resolve a strict governed projection into a read-only reviewer summary. */
export function resolveRedactionPreview(
  input?: unknown,
): RedactionPreviewViewModel {
  return resolveProjection(input).state;
}

/** Mount a text-first preview with receipt inspection as its only action. */
export function mountRedactionPreview(
  host: HTMLElement,
  input?: unknown,
  options: RedactionPreviewMountOptions = {},
): RedactionPreviewController {
  const resolved = resolveProjection(input);
  const { state, payload } = resolved;
  const document = host.ownerDocument;
  const section = document.createElement("section");
  const heading = document.createElement("h2");
  const outcome = document.createElement("p");
  const message = document.createElement("p");
  const evaluated = document.createElement("p");
  const list = document.createElement("dl");
  let inspectButton: HTMLButtonElement | null = null;

  section.dataset.component = "redaction-preview";
  section.dataset.outcome = state.outcome;
  section.setAttribute("role", state.outcome === "ERROR" ? "alert" : "region");
  section.setAttribute("aria-label", state.accessibilityLabel);
  outcome.setAttribute("aria-live", state.ariaLive);
  heading.textContent = state.title;
  outcome.textContent = `${state.outcome} / ${state.code}`;
  message.textContent = state.message;
  evaluated.textContent = state.evaluatedAtLabel;

  list.replaceChildren(
    ...state.items.flatMap((item) => {
      const term = document.createElement("dt");
      const detail = document.createElement("dd");
      const value = document.createElement("strong");
      const explanation = document.createElement("span");
      term.textContent = item.label;
      term.dataset.previewKind = item.kind;
      value.textContent = item.value;
      explanation.textContent = item.explanation;
      detail.append(value, document.createTextNode(" "), explanation);
      return [term, detail];
    }),
  );
  list.hidden = state.items.length === 0;
  section.append(heading, outcome, message, evaluated, list);

  if (
    state.canInspectReceipt &&
    payload !== null &&
    options.onInspectReceipt !== undefined
  ) {
    const inspectablePayload = payload;
    inspectButton = document.createElement("button");
    inspectButton.type = "button";
    inspectButton.textContent = "Inspect redaction receipt";
    inspectButton.addEventListener("click", () => {
      options.onInspectReceipt?.(inspectablePayload);
    });
    section.append(inspectButton);
  }

  host.replaceChildren(section);

  function destroy(): void {
    inspectButton?.replaceWith();
    host.replaceChildren();
  }

  return Object.freeze({ state, destroy });
}
