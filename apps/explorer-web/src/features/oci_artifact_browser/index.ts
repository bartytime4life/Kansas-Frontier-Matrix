import {
  type GovernedOciArtifact,
  type GovernedOciArtifactBrowserProjection,
  type OciArtifactBrowserOutcome,
  type OciArtifactBrowserReasonCode,
  parseOciArtifactBrowserProjection,
} from "../../adapters/OciArtifactBrowserProjection";

export type OciArtifactBrowserViewModel = Readonly<{
  visibility: "VISIBLE" | "HIDDEN";
  outcome: OciArtifactBrowserOutcome;
  code:
    | OciArtifactBrowserReasonCode
    | "NO_GOVERNED_RESPONSE"
    | "INVALID_PAYLOAD";
  registryScope: string | null;
  reviewedAt: string | null;
  artifacts: readonly GovernedOciArtifact[];
  rollbackCandidateRef: string | null;
  message: string;
}>;

export type OciArtifactBrowserController = Readonly<{
  state: OciArtifactBrowserViewModel;
  destroy: () => void;
}>;

type ResolvedProjection = Readonly<{
  state: OciArtifactBrowserViewModel;
  payload: GovernedOciArtifactBrowserProjection | null;
}>;

const NEGATIVE_COPY: Readonly<
  Record<
    Exclude<OciArtifactBrowserReasonCode, "ARTIFACTS_AVAILABLE">,
    string
  >
> = Object.freeze({
  ARTIFACTS_MISSING:
    "No governed OCI artifact review projection is available. No registry or release inference was made.",
  POLICY_DENIED:
    "Policy denied this artifact review projection. No registry, artifact, signature, or rollback detail is displayed.",
  UPSTREAM_ERROR:
    "The governed artifact review projection could not be completed. No registry detail is displayed.",
});

function hidden(
  code: "NO_GOVERNED_RESPONSE" | "INVALID_PAYLOAD",
): OciArtifactBrowserViewModel {
  return Object.freeze({
    visibility: "HIDDEN",
    outcome: "ERROR",
    code,
    registryScope: null,
    reviewedAt: null,
    artifacts: Object.freeze([]),
    rollbackCandidateRef: null,
    message:
      "No OCI artifact browser is rendered without an exact governed projection.",
  });
}

function resolveProjection(input: unknown | undefined): ResolvedProjection {
  if (input === undefined) {
    return Object.freeze({
      state: hidden("NO_GOVERNED_RESPONSE"),
      payload: null,
    });
  }
  const parsed = parseOciArtifactBrowserProjection(input);
  if (!parsed.ok) {
    return Object.freeze({ state: hidden("INVALID_PAYLOAD"), payload: null });
  }
  const { payload } = parsed;
  if (payload.outcome !== "ANSWER") {
    return Object.freeze({
      payload: null,
      state: Object.freeze({
        visibility: "VISIBLE",
        outcome: payload.outcome,
        code: payload.reasonCode,
        registryScope: null,
        reviewedAt: null,
        artifacts: Object.freeze([]),
        rollbackCandidateRef: null,
        message:
          NEGATIVE_COPY[
            payload.reasonCode as Exclude<
              OciArtifactBrowserReasonCode,
              "ARTIFACTS_AVAILABLE"
            >
          ],
      }),
    });
  }
  return Object.freeze({
    payload,
    state: Object.freeze({
      visibility: "VISIBLE",
      outcome: "ANSWER",
      code: "ARTIFACTS_AVAILABLE",
      registryScope: payload.registryScope,
      reviewedAt: payload.reviewedAt,
      artifacts: payload.artifacts,
      rollbackCandidateRef: payload.rollbackCandidateRef,
      message:
        "Synthetic digest-pinned artifacts and recorded referrers are available for review. Tags are mutable labels; signatures are recorded but not verified here, and rollback remains unauthorized.",
    }),
  });
}

/** Resolve an exact governed projection into a read-only artifact review model. */
export function resolveOciArtifactBrowser(
  input?: unknown,
): OciArtifactBrowserViewModel {
  return resolveProjection(input).state;
}

function appendCell(row: HTMLTableRowElement, text: string): void {
  const cell = row.insertCell();
  cell.textContent = text;
}

function appendArtifactDetails(
  document: Document,
  host: HTMLElement,
  artifact: GovernedOciArtifact,
): void {
  const details = document.createElement("details");
  const summary = document.createElement("summary");
  const list = document.createElement("ul");
  summary.textContent = `Inspect ${artifact.tag} digest-pinned references`;

  const artifactItem = document.createElement("li");
  artifactItem.textContent = `Artifact: ${artifact.artifactRef}`;
  list.append(artifactItem);
  for (const referrer of artifact.referrers) {
    const item = document.createElement("li");
    item.textContent =
      referrer.artifactRef === null
        ? `${referrer.kind}: absent`
        : `${referrer.kind}: ${referrer.artifactRef} (recorded, unverified)`;
    list.append(item);
  }
  details.append(summary, list);
  host.append(details);
}

/** Mount an unstyled, text-first, unmounted-by-default OCI review table. */
export function mountOciArtifactBrowser(
  host: HTMLElement,
  input?: unknown,
): OciArtifactBrowserController {
  const resolved = resolveProjection(input);
  const { state, payload } = resolved;
  host.replaceChildren();
  if (state.visibility === "HIDDEN") {
    return Object.freeze({ state, destroy: () => host.replaceChildren() });
  }

  const document = host.ownerDocument;
  const region = document.createElement("section");
  const heading = document.createElement("h2");
  const status = document.createElement("p");
  const message = document.createElement("p");
  region.dataset.component = "oci-artifact-browser";
  region.setAttribute("role", state.outcome === "ERROR" ? "alert" : "region");
  region.setAttribute("aria-label", "OCI artifact review browser");
  heading.textContent = "OCI artifact review";
  status.dataset.artifactBrowserStatus = state.outcome;
  status.textContent = `Review status: ${state.outcome}`;
  message.textContent = state.message;
  region.append(heading, status, message);

  if (payload !== null && payload.outcome === "ANSWER") {
    const context = document.createElement("p");
    context.textContent = `Registry scope: ${payload.registryScope}; reviewed ${payload.reviewedAt}.`;
    region.append(context);

    const table = document.createElement("table");
    const caption = document.createElement("caption");
    const head = table.createTHead();
    const headRow = head.insertRow();
    const body = table.createTBody();
    caption.textContent = "Synthetic OCI artifact review projection";
    for (const label of [
      "Tag (mutable)",
      "Digest (identity)",
      "Media type",
      "Size",
      "Referrers",
      "Rollback",
    ]) {
      const cell = document.createElement("th");
      cell.scope = "col";
      cell.textContent = label;
      headRow.append(cell);
    }
    for (const artifact of payload.artifacts) {
      const row = body.insertRow();
      row.dataset.artifactDigest = artifact.digest;
      appendCell(row, artifact.tag);
      appendCell(row, artifact.digest);
      appendCell(row, artifact.mediaType);
      appendCell(row, `${artifact.sizeBytes.toLocaleString("en-US")} bytes`);
      appendCell(
        row,
        artifact.referrers
          .map((referrer) =>
            referrer.recordedState === "PRESENT_UNVERIFIED"
              ? `${referrer.kind}: recorded, unverified`
              : `${referrer.kind}: absent`,
          )
          .join("; "),
      );
      appendCell(
        row,
        artifact.artifactRef === payload.rollbackCandidateRef
          ? "Candidate only — not authorized"
          : "Not designated",
      );
    }
    table.append(caption);
    region.append(table);
    const detailGroup = document.createElement("div");
    detailGroup.setAttribute("aria-label", "Digest-pinned artifact references");
    for (const artifact of payload.artifacts) {
      appendArtifactDetails(document, detailGroup, artifact);
    }
    region.append(detailGroup);
  }

  host.replaceChildren(region);
  return Object.freeze({
    state,
    destroy: () => host.replaceChildren(),
  });
}
