import {
  FOCUS_COMPOSED_CLAIM_REQUEST_PROFILE,
  mountFocusComposedClaimFixture,
  type FocusComposedClaimFixtureCase,
  type FocusComposedClaimFixtureController,
  type FocusComposedClaimRequest,
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

const correctedFocusWorkspaceProjection = Object.freeze({
  profile: "kfm.explorer.focus-composed-claim.public-safe.v1",
  request_id: "request:focus:corrected-evidence-001",
  claim_id: "claim:synthetic:corrected-evidence-001",
  outcome: "ANSWER",
  reason_code: "COMPOSED_CLAIM_SUPPORTED",
  closure_id: "kfm:closure:synthetic:corrected-evidence-001",
  closure_outcome: "SUPPORTED",
  answer:
    "The corrected synthetic soil summary supports a bounded statement. The superseded summary remains visible only in correction history.",
  evidence_refs: Object.freeze([
    "kfm:evidence:synthetic:corrected-soil-summary-001",
  ]),
  citations: Object.freeze([
    Object.freeze({
      evidence_ref: "kfm:evidence:synthetic:corrected-soil-summary-001",
      label: "Corrected synthetic soil summary",
      href: "https://example.invalid/kfm/evidence/corrected-soil-summary-001",
    }),
  ]),
  resolved_roles: Object.freeze(["ENDORSED_SUMMARY"]),
  unavailable_roles: Object.freeze([]),
  limitations: Object.freeze([
    "The superseded synthetic summary is history, not current claim support.",
    "Fixture-only demonstration; no live source, model runtime, release, or publication action occurs.",
  ]),
  policy: "ALLOW",
  review: "REVIEWED",
  release: "RELEASED",
  freshness: "CURRENT",
  ai_receipt_ref: "kfm:receipt:ai:synthetic:focus-corrected-001",
  evidence_drawer: Object.freeze({
    profile: "kfm.explorer.evidence-drawer.public-safe.v1",
    id: "kfm:ui:evidence-drawer:focus-corrected-evidence-001",
    outcome: "ANSWER",
    reason_code: "SUPPORTED",
    title: "Corrected synthetic Focus summary",
    summary:
      "The bounded answer is supported only by the active corrected synthetic summary.",
    evidence_refs: Object.freeze([
      "kfm:evidence:synthetic:corrected-soil-summary-001",
    ]),
    citations: Object.freeze([
      Object.freeze({
        label: "Corrected synthetic soil summary",
        href: "https://example.invalid/kfm/evidence/corrected-soil-summary-001",
      }),
    ]),
    limitations: Object.freeze([
      "The superseded synthetic summary is history, not current claim support.",
      "Fixture-only demonstration; no live source, model runtime, release, or publication action occurs.",
    ]),
    trust_state: Object.freeze({
      source_role: "official",
      policy: "ALLOW",
      review: "REVIEWED",
      release: "RELEASED",
      freshness: "CURRENT",
      correction: "CORRECTED",
    }),
    history: Object.freeze({
      negative_outcomes: Object.freeze([
        Object.freeze({
          evidence_ref:
            "kfm:evidence:synthetic:superseded-soil-summary-001",
          state: "SUPERSEDED",
          reason_code: "SUPERSEDED_EVIDENCE",
          recorded_at: "2026-08-20T00:00:00Z",
          visible_in_runtime: true,
          resolvable_as_current: false,
        }),
      ]),
      corrections: Object.freeze([
        Object.freeze({
          prior_evidence_ref:
            "kfm:evidence:synthetic:superseded-soil-summary-001",
          active_evidence_ref:
            "kfm:evidence:synthetic:corrected-soil-summary-001",
          status: "ACTIVE_CORRECTION",
          recorded_at: "2026-08-20T00:00:00Z",
        }),
      ]),
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
  Object.freeze({
    caseId: "corrected-evidence",
    label: "Run corrected-evidence Focus request",
    request: Object.freeze({
      profile: FOCUS_COMPOSED_CLAIM_REQUEST_PROFILE,
      request_id: "request:focus:corrected-evidence-001",
      claim_id: "claim:synthetic:corrected-evidence-001",
      question:
        "What does the corrected synthetic summary support inside the active evidence scope?",
      allowed_evidence_refs: Object.freeze([
        "kfm:evidence:synthetic:corrected-soil-summary-001",
      ]),
    }),
  }),
]);

export async function resolveSyntheticFocusWorkspaceProjection(
  request: FocusComposedClaimRequest,
): Promise<unknown> {
  await Promise.resolve();
  if (
    request.requestId === "request:focus:workspace-policy-withheld-3373" &&
    request.claimId === "claim:synthetic:workspace-policy-withheld-3373"
  ) {
    return focusWorkspaceProjection;
  }
  if (
    request.requestId === "request:focus:corrected-evidence-001" &&
    request.claimId === "claim:synthetic:corrected-evidence-001"
  ) {
    return correctedFocusWorkspaceProjection;
  }
  throw new Error("Synthetic Focus workspace request identity mismatch.");
}

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
 * Mount bounded fixture-only requests into the existing public Explore
 * composition. This adds no route, transport, model, policy engine,
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
    text(document, "h3", "Governed requests → finite responses"),
    text(
      document,
      "p",
      "Each control submits a bounded request through an injected governed boundary. Only active endorsed synthetic support crosses the answer boundary; raw governed data and protected policy context never enter the model-facing or client projection.",
    ),
    text(
      document,
      "p",
      "Withheld context remains a generic limitation, and superseded evidence remains correction history rather than active support. These fixtures do not activate a source, execute a model, authenticate release, or publish an answer.",
      "guardrail",
    ),
  );
  fixtureHost.className = "selection-lab__fixture";
  workspace.append(fixtureHost);
  mapWorkspace.append(workspace);

  fixture = mountFocusComposedClaimFixture(
    fixtureHost,
    focusCases,
    resolveSyntheticFocusWorkspaceProjection,
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
