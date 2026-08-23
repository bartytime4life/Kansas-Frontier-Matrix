import {
  FOCUS_COMPOSED_CLAIM_REQUEST_PROFILE,
  mountFocusComposedClaimFixture,
  type FocusComposedClaimFixtureCase,
  type FocusComposedClaimFixtureController,
} from "../features/focus_panel";

export type SyntheticFocusWorkspaceController = Readonly<{
  destroy: () => void;
}>;

const focusWorkspaceProjection = Object.freeze({
  profile: "kfm.explorer.focus-composed-claim.public-safe.v1",
  request_id: "request:focus:workspace-policy-withheld-3373",
  claim_id: "claim:synthetic:workspace-policy-withheld-3373",
  outcome: "ANSWER",
  reason_code: "COMPOSED_CLAIM_QUALIFIED",
  closure_id: "kfm:closure:synthetic:workspace-policy-withheld-3373",
  closure_outcome: "QUALIFIED",
  answer:
    "The endorsed synthetic soil summary supports a bounded general statement. Restricted synthetic context remains withheld by policy.",
  evidence_refs: Object.freeze([
    "kfm:evidence:synthetic:endorsed-soil-summary-3373",
  ]),
  citations: Object.freeze([
    Object.freeze({
      evidence_ref: "kfm:evidence:synthetic:endorsed-soil-summary-3373",
      label: "Endorsed synthetic soil summary",
      href: "https://example.invalid/kfm/evidence/endorsed-soil-summary-3373",
    }),
  ]),
  resolved_roles: Object.freeze(["ENDORSED_SUMMARY"]),
  unavailable_roles: Object.freeze(["RESTRICTED_CONTEXT"]),
  limitations: Object.freeze([
    "One synthetic restricted-context role is withheld by policy; no protected detail is exposed.",
    "Fixture-only demonstration; no live source, model runtime, release, or publication action occurs.",
  ]),
  policy: "ALLOW",
  review: "REVIEWED",
  release: "RELEASED",
  freshness: "CURRENT",
  ai_receipt_ref: "kfm:receipt:ai:synthetic:focus-workspace-3373",
  evidence_drawer: Object.freeze({
    profile: "kfm.explorer.evidence-drawer.public-safe.v1",
    id: "kfm:ui:evidence-drawer:focus-workspace-policy-withheld-3373",
    outcome: "ANSWER",
    reason_code: "SUPPORTED",
    title: "Endorsed synthetic Focus summary",
    summary:
      "The bounded answer is supported only by the cited endorsed synthetic summary.",
    evidence_refs: Object.freeze([
      "kfm:evidence:synthetic:endorsed-soil-summary-3373",
    ]),
    citations: Object.freeze([
      Object.freeze({
        label: "Endorsed synthetic soil summary",
        href: "https://example.invalid/kfm/evidence/endorsed-soil-summary-3373",
      }),
    ]),
    limitations: Object.freeze([
      "One synthetic restricted-context role is withheld by policy; no protected detail is exposed.",
      "Fixture-only demonstration; no live source, model runtime, release, or publication action occurs.",
    ]),
    trust_state: Object.freeze({
      source_role: "official",
      policy: "ALLOW",
      review: "REVIEWED",
      release: "RELEASED",
      freshness: "CURRENT",
      correction: "NONE",
    }),
    history: Object.freeze({
      negative_outcomes: Object.freeze([]),
      corrections: Object.freeze([]),
    }),
  }),
});

const focusCases: readonly FocusComposedClaimFixtureCase[] = Object.freeze([
  Object.freeze({
    caseId: "governed-summary",
    label: "Run bounded governed Focus request",
    request: Object.freeze({
      profile: FOCUS_COMPOSED_CLAIM_REQUEST_PROFILE,
      request_id: "request:focus:workspace-policy-withheld-3373",
      claim_id: "claim:synthetic:workspace-policy-withheld-3373",
      question:
        "What does the endorsed synthetic summary support inside the active evidence scope?",
      allowed_evidence_refs: Object.freeze([
        "kfm:evidence:synthetic:endorsed-soil-summary-3373",
      ]),
    }),
  }),
]);

function text<K extends keyof HTMLElementTagNameMap>(
  document: Document,
  tag: K,
  value: string,
  className?: string,
): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  if (className !== undefined) node.className = className;
  node.textContent = value;
  return node;
}

/**
 * Mount the single fixture-only issue #3373 request into the existing public
 * Explore composition. This adds no route, transport, model, policy engine,
 * source, lifecycle store, release action, deployment, or publication path.
 */
export function mountSyntheticFocusWorkspace(
  root: HTMLElement,
): SyntheticFocusWorkspaceController {
  const mapWorkspace = root.querySelector<HTMLElement>("#map");
  if (mapWorkspace === null) {
    throw new Error("Explorer map workspace is missing for the synthetic Focus mount.");
  }

  const document = root.ownerDocument;
  const workspace = document.createElement("div");
  const fixtureHost = document.createElement("div");
  let fixture: FocusComposedClaimFixtureController | null = null;
  let destroyed = false;

  workspace.className = "selection-lab card";
  workspace.dataset.component = "focus-mode-workspace";
  workspace.append(
    text(document, "p", "Focus Mode workspace", "eyebrow"),
    text(document, "h3", "One governed request → one finite response"),
    text(
      document,
      "p",
      "The browser submits one bounded request through an injected governed boundary. Only the endorsed synthetic summary crosses the client boundary; raw governed data and protected policy context never enter the model-facing or client projection.",
    ),
    text(
      document,
      "p",
      "The restricted context role remains visible only as a machine-readable withheld state and a generic limitation. This fixture does not activate a source, execute a model, authenticate release, or publish an answer.",
      "guardrail",
    ),
  );
  fixtureHost.className = "selection-lab__fixture";
  workspace.append(fixtureHost);
  mapWorkspace.append(workspace);

  fixture = mountFocusComposedClaimFixture(
    fixtureHost,
    focusCases,
    async (request) => {
      await Promise.resolve();
      if (
        request.requestId !== "request:focus:workspace-policy-withheld-3373" ||
        request.claimId !== "claim:synthetic:workspace-policy-withheld-3373"
      ) {
        throw new Error("Synthetic Focus workspace request identity mismatch.");
      }
      return focusWorkspaceProjection;
    },
  );

  return Object.freeze({
    destroy(): void {
      if (destroyed) return;
      destroyed = true;
      fixture?.destroy();
      fixture = null;
      workspace.remove();
    },
  });
}
